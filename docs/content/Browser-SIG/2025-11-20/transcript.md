SIG: Browser SIG
Date: 2025-11-20
Duration: 19 minutes
Zoom Recording URL: https://zoom.us/rec/share/3HWv6iL7MW0c9AXD8wimWZR8e5z3ZAO3XGodNLkD9Zje8n4MwLjyYFXmFYOcMmNS._uhMuLwr27OV_M-s
============================================================

## Zoom Recording Transcript

**Benoît Zugmeyer** 01:35 Hello.
**Ted Young** 01:40 Hello, hello!
Nice… have we met before? I don't think we've met.
**Benoît Zugmeyer** 01:47 Yeah, we met.
Okay.
A few times, yeah.
**Ted Young** 01:52 Oh, cool.
**Benoît Zugmeyer** 01:52 But, I'm in the office now, usually I'm from… I'm from home.
**Ted Young** 01:57 Oh, okay.
**Benoît Zugmeyer** 01:58 Yep.
**Ted Young** 02:00 Well, good to see you.
Cool. Well… Feel free to add things to the agenda. You might have a light week this week.
**Benoît Zugmeyer** 03:12 Yeah.
**Ted Young** 03:13 I feel like I… I've been out for a while, so… it's good to be back. Seems like all things have been getting done, just looking… looking over the old meeting notes.
**Benoît Zugmeyer** 03:24 Yeah, definitely, things are moving.
Quite fast now. We have many instrumentation, that's… that's great.
**Ted Young** 03:31 A… Okay.
Well, Might as well kick it off.
Benoit, do you wanna… Yep. …start us?
**Benoît Zugmeyer** 03:57 Yeah, so, at Datalog, we are starting to get serious about supporting Ram Hotel.
In our own product.
And so, yeah, we… one of our requirements is… is to have a session ID.
**Ted Young** 04:17 And so, we were wondering if…
**Benoît Zugmeyer** 04:19 what's the process to kind of stabilize it? Because for now, it's… it's in a development state.
**Ted Young** 04:29 Yeah.
So, the… The problem we've had with session, traditionally, is that, we would like it… To be a resource.
But we've traditionally said that resources are immutable, because they don't change over the lifespan.
of, the application. This was true on the server side for the resources that we were thinking about back then, but it was one of those all swans are white moments in the spec, right? And then we get to the client side, and we discover, oh, there's these resources that maybe change on different timescales.
Oops.
There's an effort called Entities to try to improve how resources work in general in OpenTelemetry.
And as part of that effort, allowing mutable resources has been kind of the goal. But that whole thing, because it's a big hairball, has been taking a long time.
So that's… that's, like, the real holdup with… with resources. We now have a resource provider, so we should be able to actually start modeling, like, session management and stuff like that.
But we need to get that kind of stood up here, and, for entities to kind of settle down before we can mark that as stable.
**Benoît Zugmeyer** 05:57 So… I see.
**Ted Young** 05:59 It's… it's unfortunate. It's like the one thing left, this… this SIG has been, like, the tip of the sphere for, like, everything that was, like, missing from OpenTelemetry in, like, the first push. I feel like this SIG… hit all of that stuff, right? We really, really need events, right? So we need logging sorted out. And we really needed session management and stuff that… Was, like, needed to, like, advance how… resources worked in a fundamental way, and that… that has been blocking the SIG forever, basically.
**Benoît Zugmeyer** 06:39 So…
**Ted Young** 06:40 We're now finally unblocked in the sense that we're prototyping all of this stuff, but that's the reason why it's still not stable.
**Benoît Zugmeyer** 06:48 Okay.
So, so resources will be mutable?
**Ted Young** 06:53 Huh.
**Benoît Zugmeyer** 06:55 Yeah, I mean, it's like a thing…
**Ted Young** 06:59 I mean, this is a thing we're still kind of exploring, right? Like, you should be able to get an entity stream and a concept of an entity, so you should be able to get a changelog of when the entities change. And an entity is basically a collection of resources.
But, we also want to be backwards compatible, in the sense that, like.
all of the entities still get pushed into this dictionary we call resources in OTLP.
Because we don't want to break… that would be, like, a huge breaking change if entities started putting the resources somewhere else, right?
So this does mean that, potentially, you could get a batch of resources, like a batch of OTLP from a service with a service ID, and then later you could get another batch of OTLP, and the resources on that batch might be different in some way.
they should only be the resources you should expect to change changing, right? Like, service name should not be just randomly changing.
**Benoît Zugmeyer** 08:02 Yeah.
**Ted Young** 08:03 But, there are one or two places out there in the universe where people were just taking… basically trying to use the resource as an identifier, like, the entire object, just, like, taking a hash of it, and saying, because… hey, because resources are immutable, I can just take a hash of this object, and that fingerprint is my identifier for this service? Don't do that.
So, I would say if that's happening at Datadog, maybe double-check. That's, like, the one follow-up there.
It was happening in a couple places in the collector, but we haven't heard reports from anyone else doing it.
Anyways, that's where things are at with sessions.
**Benoît Zugmeyer** 08:46 Okay, thank you.
**Ted Young** 08:47 Yup.
Okay.
What's up next? Ebene?
**Abinet Debele** 08:58 Yeah, hi, yeah, so I wanted to just show a quick demo of the NavVision instrumentation.
And, let me see if I can share my screen.
Alright, can you see my screen?
**Ted Young** 09:18 Yeah.
**Abinet Debele** 09:19 Alright, okay.
So, the navigation instrumentation, I have, put some examples in, in the code, and… I can go through that and see, what the looks look like, and the various, just… I tried to simulate some of the, events that are, that we're trying to track.
So I… in the examples, I have added two examples, actually. The navigation, like, you can see it here.
For the navigation, I have one example, which actually is not a SPA app, it's not a single-page application, but it's, it kind of simulates the things that happen in a single-page application.
So it listens to the history push, or the navigation, API calls, and then it makes, changes in the page, accordingly.
it's kind of simulating that, but I also have… I wanted to test it on a real Spa app, and I created a React Spa navigation.
So we… I can go through both of them quickly and see what… what's happening.
So, when you go to the page for the first time, so the navigation instrumentation has to fire, a page load, A hard… a heart navigation, log.
the first time you access a page, that's, like, the first page load. In that case, the logs that are, That, that looks at… Our fire should contain, like, the… for example, some of the… we can see some of the… Fields that are… The attributes in the, in the, in the, in the, in the event.
for example, the URL will be the actual URL, but the navigation same document will be forced, because this is the first, hardload.
Hash change will be false.
And, the… Navigation type will not be available here. We can decide whether it has to be available, like, it can be a push or something, but for hardload, currently the navigation type is not available.
So if I go to a route, for example, Route 1, So it'll be fired again, and… Sorry, If you go here, URL will be, again, navigation route1.
The same document is true, so it's… like a spa, and the hash change is false, there's no hash change now. The navigation type will be push.
So, I can test a hash change, for example, here. The hash change will bring hash… In here, and then… You can see… So yeah, the route is here, here, but now the same document is still true. Hash change is also true.
the type would be Wish, in this case.
Yeah, we can go back and see also another look.
So… Yeah, same document is still true, hash change is true. Because I came from hash change, hash, I think that's why I said sash.
change, navigation type is, again, it's push.
So this is, example that, as I said, this is a simulation of the spa up.
We can go to the… react and see the same thing, I think.
So, in the same… in the same way, for first time we go to a page, it'll be… A hardload, so… Same document is supposed to be false, yeah.
Those changes for us.
We can also do, go to another route.
See if that happens.
So, same document is true, hash changes false, navigation type is push.
And these are, custom attributes added. It's just to show that we can also add custom values to that.
So we can also change this task change here, So in this case, hashtang will be true.
Yeah, so this is just a quick, look into it.
Yeah, we can discuss if you have questions or something like that.
**Ted Young** 14:20 That's really cool.
**Abinet Debele** 14:21 But… so the React app is not in the code. If you think it should be in the code, I can also push that one.
**Martin Kuba** 14:32 So I want to quickly point out to the group that, the, the URL changes, like, for the same document changes, currently are not distinguishing like, what's… what actually represents a route change or not. So that's something that we still would need to follow up on this PR, but I think this is, like, a first good pass.
First, like, iteration, and then we can, we can add some… maybe some heuristics for figuring out how to distinguish soft navigations from just, like, a random URL change.
Yeah.
**Abinet Debele** 15:09 Yeah.
**Martin Kuba** 15:11 I think this is a good, good, kind of a good… First… first pass on this.
Yeah, thanks for the demo, Abinas.
**Abinet Debele** 15:23 Alright, okay, thank you.
**Ted Young** 15:26 It would be great to make a note of the things that are missing from this somewhere, I don't know, in the README for the instrumentation, or an issue, or something.
**Martin Kuba** 15:35 Yeah.
**Ted Young** 15:38 But yeah, really cool.
**Martin Kuba** 15:41 I would ask if, like, so I… I have re-added a review, Abinet, yesterday, actually.
**Abinet Debele** 15:50 Yeah, I'm gonna look into it, yeah.
**Martin Kuba** 15:53 But if folks here, if you can please take a look at the PR and do a review, that would be very helpful.
So we can… Get this through, and then… Keep improving on that.
**Ted Young** 16:10 Nice.
**Abinet Debele** 16:14 Alright, okay, thank you. Yeah, I'll stop sharing and… Nope.
**Ted Young** 16:21 Yeah, that's awesome.
Where does that demo live that you were using?
**Abinet Debele** 16:30 It's in the… in the same repo in the example… under the examples?
**Ted Young** 16:34 Okay, cool.
**Abinet Debele** 16:35 We have examples there.
**Ted Young** 16:37 Great.
Alright, moving on, Hector.
**Hector Hernandez** 16:44 Yeah, I just want to bring this PR for people's attention. This is something that Carly has been working for a while in my team in Microsoft. She transitioned to a different thing, so I'm actually grabbing this and trying to push it forward. I already have some approvals, but please take a look at it. Let me see if there's any feedback or any concerns with it.
Yeah, that's it.
**Ted Young** 17:10 Awesome.
**Martin Kuba** 17:12 I think, didn't Joaquin… start a new PR for this? Like, I just…
**Hector Hernandez** 17:19 It was for another one that Carly was also driving, yeah.
**Martin Kuba** 17:23 Okay, I just want to make sure there's no duplicate work here, so…
**Hector Hernandez** 17:26 Yeah, yeah, we're… we're aware.
**Martin Kuba** 17:28 Sounds good.
**Ted Young** 17:34 Cool.
Yeah, awesome.
I've been pretty out of the loop, I'm sure.
People haven't been updating our, GitHub project, but I'll try to do a pass of that, and the… the GitHub issues on a repo.
And see if I can clean those up a little bit.
getting… less and less… In love with GitHub projects, the more… the more I use them.
It's unfortunate.
like, they're only half integrated with issues. I'm discovering anything that's… if you can't see it on the issue page or the PR page, it's, like, basically pointless, right? Like… It only will get looked at by nerds during this meeting.
So… Trying to come up with a better middle ground going forwards for how to do this.
But that's all I got.
**Trent Mick** 18:43 There's milestones, but those are limited, and then there's pen and paper.
**Ted Young** 18:48 Yeah.
There's a… it's basically… it just… it comes back down to labels, basically. Labels work everywhere, and are very visible.
So, people will see it if it's a label, and will probably miss it if it's represented as just about anything else.
Because everything else is kind of, like, hidden.
**Trent Mick** 19:09 Yeah.
**Ted Young** 19:10 Yeah.
Anyways… Anything else to discuss, or… We're actually gonna end it… end a little early.
Well, it's great to see stuff in flight.
**Hector Hernandez** 19:34 Thank you very much.
**Wolfgang Therrien** 19:36 Thank you.
**Ted Young** 19:37 See you next time.
**Trent Mick** 19:38 Okay, thanks.
