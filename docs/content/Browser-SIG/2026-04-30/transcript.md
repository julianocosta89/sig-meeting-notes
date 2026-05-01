SIG: Browser SIG
Date: 2026-04-30
Duration: 31 minutes
Zoom Recording URL: https://zoom.us/rec/share/oMs0Xg5S854xop7smhYQoapYr5OnFuHyKVsHvKAbh3zTgQh9JF9tvXyqJBp_FiLZ.VimT0Nf_gh_JrXAm
============================================================

## Zoom Recording Transcript

**Martin Kuba** 01:22 Hey, guys.
**Jared Freeze** 01:27 Did we kick out this note-taker?
Looks like the person's not here.
**Maxime Quentin** 01:36 Hello?
**Martin Kuba** 01:40 Hi, Maxim.
**Jared Freeze** 01:43 Looks like I'm not an admin.
**Ted Young** 02:10 Yo…
**Martin Kuba** 02:14 Hey, Ted.
**Jared Freeze** 02:25 Hey, Ted, what's your, what's your take on these note-takers that just show up for people that don't attend?
**Ted Young** 02:34 I feel like we have a policy that says we can kick them out.
Because it's weird.
**Jared Freeze** 02:45 Yeah, it's already recorded, so I feel like just, like, come or don't come.
**Ted Young** 02:49 Yeah, we… we have, you know, a set of publicly recorded videos, and then we… we cull them. From the list.
in general, it's like… it feels like one of these, singularity moments, where… We wanted to not have, like, an endless history of recordings, because that could be used for weird purposes, but now it feels like… like, any amount of recording can be used for evil, so we're actually a little confused about what to do. But we… I generally agree that it's creepy.
Right, the difference between, like.
creepy versus not creepy recording is intent, right? Like, we know why we're recording it, but when someone shoves a camera in your face and you don't know why you… They're doing it, it… it's creepy.
So having, like, a bot show up and be like, I'm recording everything, and I'm not gonna tell you why.
**Jared Freeze** 04:00 Yeah, Dan's link just said it's prohibited, is what they decided, so…
**Ted Young** 04:04 So…
**Daniel Dyla (Dynatrace)** 04:05 destination.
**Jared Freeze** 04:05 Kick it.
**Daniel Dyla (Dynatrace)** 04:06 I was on the GC when we decided this a long time ago. I mean.
this is the official policy. Realistically, it's so hard to… it's such a pain. You have to, like, take… I don't know if anybody is the host right now. You have to take host permissions and… kick a note taker. In this case.
like, we know who Brandon is. I think there's no real way to stop this.
And… I don't know.
**Ted Young** 04:37 Yeah.
**Jared Freeze** 04:37 Perfect.
**Ted Young** 04:38 I could go track down the host privileges, that's probably a good thing.
**Daniel Dyla (Dynatrace)** 04:42 It is the policy, so if anybody wants the note-taker kicked out, I think we should.
Otherwise, why have the policy?
**Jared Freeze** 04:53 Agreed.
**Ted Young** 04:55 Should I go find the…
**Daniel Dyla (Dynatrace)** 04:59 I was on the GC when we made this policy, and things have evolved very quickly since then, but even at that time, because… Zoom doesn't require login credentials for… Like, you know, they have anonymous join.
It's almost impossible to combat this in any systematic way.
Unless we make the meetings, like, logged-in people only, in which case we require everybody that wants to join the meeting to have a Zoom account.
**Ted Young** 05:29 Yep.
Yeah, the only reason why I was, like, I was expressing, like, I'm not sure is, like, I know we made that policy a long time ago, but things have evolved so much, so it's like, did we give up?
I posted a link to the policy.
**Daniel Dyla (Dynatrace)** 05:48 I think general sentiment around these tools has also shifted, too. When they first showed up, everybody was creeped out by them. Yeah. And now, I think… There still are, for sure, people who are creeped out by them, but… a lot less.
**Jared Freeze** 06:07 Well, if you know Brandon, great. I just wasn't sure if it was a drive-by.
**Daniel Dyla (Dynatrace)** 06:12 Brandon is a, A regular contributor, particularly to… The collector, he's a… in Prometheus.
He's a Google engineer.
**Jared Freeze** 06:26 Sweet.
Kudos to Martin for, Doing the hotel thing yesterday, that was… that was very cool.
**Ted Young** 06:35 Yeah.
**Martin Kuba** 06:38 Hmm, it was nice to just give them quick updates to the community.
I was expecting tough questions, I didn't get any questions.
I think it went well.
**Ted Young** 06:50 Nice.
**Martin Kuba** 06:56 Jared, do you want me to drive, or do you want to…
**Jared Freeze** 07:00 Yeah, it looks like David got the first topic, fraction XHR.
**David Luna Bistuer** 07:06 Yeah, well, maybe it just stumped my… Thoughts here, and maybe this is not a specific topic, but… Let's summarize a little bit. The SDK, or at least there was, there is the intent to have an SDK by summer.
A new measure, and… One specific thing that happens is in trace, we have three different packages for SDK Trace Web. We have one specific for browser, one specific for Node.
And… and one basic, but it has some utilities that maybe are not So, the intent is that… is to have a… At the end, to have a… just one, through all the mall, like the… the ring, which is, platform agnostic, basically, okay? And we, I've been looking at the changes that are needed, and there are some Utilities that are in the CKA Trace web.
that are, imported by the fetch and the XHR instrumentations. So there was a discussion about, okay, where should we… this code should we live?
should live. There is kind of two opinions. One is like, okay, just put the code in the instrumentation that needs it.
And the other one was, okay, maybe just for now, we have a webcommon package to host it.
If we want to go to the, to move the code into the instrumentation, it's a lot of code to share. So, if somebody's using Fetch and XHR to have spans on their requests, they're shelling… they are… they're duplicating a lot of code.
That's Asia. I know there is a plan, or at least we have an issue to move.
things into… into the browser instrument editions, but we are kind of hesitant to have Instruments are using, are using traces, or using the trace signal.
So… now it's time for you to say your thoughts, or… I don't know, let's have a discussion, let's not… I was wondering if it's a good idea just to try to move them already in the browser installment edition.
because we have a utils, then we can actually share the code, and we don't have this kind of duplication. But I know that maybe we could… it caused a bit of friction, because those instrumentations are using, well, are using drizzle, and also using the span, events, which I think is something that we don't want to have.
So… Penny, for your thoughts.
**Jared Freeze** 09:44 Yeah, so my… my initial thought is that if we're gonna move it, I would refactor, right? So, if we really don't want span events.
I wouldn't really want to see that moved over, because that means if you're a developer, you've already added the new package.
And then you're getting something that we're saying, hey, it's… You know, that's not recommended.
I don't think we should do both.
Martin?
**Martin Kuba** 10:13 Yeah, I've been… I've been… I think we should move them at some point. Like, I think my kind of hesitation about these two specifically, about the XHR and Fetch, is that they are now separate packages, and they have very high usage.
So I don't know, like, if, you know, I think we should talk about how, you know, how we would want to see this happening, like, should we… Should we move them? Move them?
To our… Kind of consolidated.
instrumentations package, and deprecate the… the other packages, you know, I… Or should we just move them, as, as, you know, separate packages into the browser repo and support, you know, what's actually published on NPM, for now, until we have… until we, like, move to, like, to the next major version.
Yeah, I think it's… I think, like, that migration is easier with the… with the… the other instrumentations, because they don't have high usage, but, like, with these two, like, I'm… I don't wanna, like, Affect a lot of… a lot of users, because, like, they have… they do have a lot of downloads.
**Joaquín Díaz** 11:40 I agree, like, I think… we shouldn't just, out of nowhere, change that. I'm making people update their NPM, like, installs.
So I think we should move them, but if we can keep the same… like, npm URL or whatever in the package JSON, so they don't need to change that, and they can install it from the inner repo, but, without updating their apps.
That would be great. And then, once we do that, we can just set a timeline, a deadline, and say, in 6 months, in a year.
We are going to change this from this to the actual, like, where we have all the other instrumentation.
And give people time, and I guess… I don't know how… I don't even know if it is possible or not, but… If we can support both.
And then just let people slowly migrate.
And then eventually deprecate the… or if, like, the current URL.
Until we see that the downloads are, like, low or low enough, low ER.
Good to migrate, but to deprecate it.
That's for the, like, the downloading or the role.
Going back to this balance conversation, I… we had a similar conversation on Embrace with our… with a similar topic.
And I think there are places where spans make sense, and this is one of the places where it makes sense. We shouldn't change them to logs. I don't know about the span events, moving them to logs.
they will be out of context. You have to manually match.
The, like, patches span to the new logs instead of spun events.
I don't know how far over it is that to the collector side, but… We should keep them as spoons.
Mainly because they are. That's what they are, and also… If we… if we want to do, like, you want to set up trace parent or something, you want to trace that up to the backend and everything, I think it's easier to do with spams.
**Martin Kuba** 13:50 Yeah, I think those events on those spans are essentially the resource timing data, right? So, that would be duplicated, like, we now have a separate instrumentation for resource timing, so, like, I think we should probably You know, like, for future, like, we should think about how, like, those instrumentations could work together.
Instead of duplicating the data? Or, like, I guess, what would our recommendation be? Like, either use the span-based instrumentations, or the log… or the resource timing instrumentations, or, like, have them work together.
Hmm.
**David Luna Bistuer** 14:24 Because you want to spun, right? Sorry, you wanted…
**Joaquín Díaz** 14:28 Yeah, I didn't raise my phone.
Do you get the same information from the… resource signing than, like, patching, fetch, and XHR.
Because I think we had that discussion before, at least on Embrace, and there is not the same information. There is some missing information when you get for resource timing.
That is why we then move it, I don't remember.
What was what's missing, but you get more information when you patch.
regardless of that, I think we should have spans, because I think it's important, then if we have the same information, I think it's the same. I mean, I'd rather not patch on HKR. I don't like patching methods, so if we can get the same information from the observation, the observer, that's better, but it will stick to spams, I think.
**Martin Kuba** 15:25 Yeah, I think we definitely should keep those spam instrumentations. They, you know, they have a purpose, for sure.
**Jared Freeze** 15:36 So, just to add, it is a lot less information. I forget what exactly, but it's… there's a very clear line, I think around… Headers, body size, things like that. So… they are truly different, because I think, you know, observation would be perfect.
But there's gonna be a lot missing that I think we all rely on, so… Any other comments? Yeah.
**Joaquín Díaz** 16:08 Show me as a first step.
just make a draft PR of… What's the instrumentation will look like on the browser repo, like.
maybe do a little bit of cold linea, I believe those are very old.
So, just a path without changing the actual telemetry.
And see how they look like, and we can start with that.
**Jared Freeze** 16:33 I like… I like that idea. I was gonna say, so you mentioned previously, like, we could keep the URL in the package. I think that's gonna be really complicated, because it's already inside another package, and the way the publishing works is it, like, uses a wildcard.
And so, we would have to do a lot of stuff to exempt it, and keep, like, new code… old code in the new repo, but using the previous URL. I think that might be kind of tricky, so I like that idea. I think let's just make a PR for what we really want.
And just seats.
We'll see what it looks like, I like that.
**David Luna Bistuer** 17:16 We'll rather talk, but, one of my doubts was about how they did to coexist the… because I'm not mistaken, the span events that these instrumentations are using is To correlate the logs, these logs, what happened.
Using the Observer API to the actual span.
I wonder if there is a way to actually, I don't know, complement, so have One is in addition to creating the spans, and the other is already collecting the events.
Just set the span context there.
And that's it.
I don't know, we were talking… I remember that at the beginning of this week, we were talking about APIs, which API do we need for that? I don't know, maybe we need some APIs to enrich the observer APIs that we already have in the browser.
So maybe we have, I don't know, we can just set the, okay, for these resources, this is the spam context.
Somehow. So maybe, you know, like, okay, FET instrumentation says, okay, There is a fetch request.
Boom, this is the spam context.
And then anyone that is observing any resource, or is using the observer, the observer API, just gets the records.
But it could query, okay, is this record, related to any spam context or not?
Something like that. So maybe we need… when we were talking about APIs, I don't know, maybe I'm just mistaken, I'm just making my own idea of the APIs, but we were talking about the browser APIs somehow, or APIs for instrumentation, maybe… We need this kind of, maybe it's another utility, maybe it's a shared video API with instrumentations, that they could query about things that are happening.
What do you think?
In the past.
**Joaquín Díaz** 19:10 Is there any presence of… instrumentations talking to each other, I… But they were, like, independent, so you need something that sits on top of instrumentations, right, to share some state.
**Daniel Dyla (Dynatrace)** 19:23 There is some, precedent for that.
Using the context object.
The… HTTP instrumentation, on Node, the HTTP server instrumentation doesn't know… It doesn't have enough information to properly name this fan, because the name comes from… HTTP libraries, or, like, you know, server… Frameworks.
So, there is some precedent there, but in general, no, the instrumentations are meant to be… Isolated from one another, because… they communicate using the API.
And… Like, if you have one but not the other, it still needs to work.
**Martin Kuba** 20:18 But, like, for the…
**Daniel Dyla (Dynatrace)** 20:19 If you use some… if you use some third-party SDK, they also still need to work.
**Martin Kuba** 20:30 For this particular use case.
it might be good enough to just look for the trace context in the context object, right? Like… Like you're describing.
**Daniel Dyla (Dynatrace)** 20:47 I wasn't paying enough attention to the actual use case that's being Disgust, I'm sorry.
**Martin Kuba** 20:54 Yeah, so, like, if one instrumentation is generating logs or events, and… and another instrumentation is setting trace context, then… The event instrumentation could just look in the context object for, like, is there a trace context here?
**Daniel Dyla (Dynatrace)** 21:13 Yeah, I mean, that works if the span is started before the logs are generated. Like, if you click a button, and a log is generated, and then the span is started, that doesn't do you any good.
If it's the other way around, then yeah, you can just take whatever the current, Context is in, like, the currently active context object.
But… Even that… Would depend on, like, ZoneJS, which… I think we should move to, as much as possible, a contextless model for the web.
**Martin Kuba** 21:55 Damn.
**Daniel Dyla (Dynatrace)** 21:56 So it might be a good idea for us to… You know… Have some way to manually pass that information around.
**Joaquín Díaz** 22:06 Also, I think… the observer gets the resource entries after the fact they happened, so the spawn is ended. And then you get the resource timing, so even though… even then, the spawn is closed, so I don't know if you've had the context or not.
**Daniel Dyla (Dynatrace)** 22:23 Yeah, and if you look at the XHR and fetch instrumentations, it's not, like… I mean.
It's non-trivial to get the correct resource timing entry from a particular request, which is kind of annoying.
Like, tying everything together is really frustrating.
**Ted Young** 22:53 Is how, long-term, do we think the situation is with context and… the web.
**Daniel Dyla (Dynatrace)** 23:03 3 years, more likely 5.
It's… I forget the exact stage that they're in for the… the… TC proposal, but… There are working prototypes that do… Like, have polyfills, but they depend on… Either on Zone.js or on mechanisms that are very similar to ZoneJS. They don't work with native async await.
I mean, obviously, that's why The proposal exists in the first place, is to modify the runtimes to make that work.
Yeah, years.
**Ted Young** 23:45 So, I feel like one aspect of OpenTelemetry's design philosophy that you were just talking about Daniel's, like, loose coupling, right? Like, we want… things to be loosely coupled, right? We want the implementation to be loosely coupled from the instrumentation. We want the instrumentation packages to be loosely coupled from each other, so we don't end up shipping a giant hairball, right? Like, that's… that's what, like… proprietary agents and stuff, you know, they have the ability to, like… Like, coordinate everything, but anyone who's worked on those over a long period of time knows what hairballs they turn into.
So I feel like the loose coupling is important, but the other aspect of OpenTelemetry SDK design is, like, very context-centric, right? Like, that's, like, the core of Like, how everything is supposed to pass information to each other.
And if that's just, like, not available, if that's just, like, just not a good pattern for the web, that's really, like, an indictment for, like.
you know… our whole SDK design.
As far as doing something for the web.
So… if that's just something that's not even on the horizon, I think that means, like, yeah, we should just assume it's not there, and start really going our own way in terms of making a design that works for the web, that's at least an SDK design that works for the web.
That just doesn't worry too much about Those patterns, that we use everywhere else.
**Jared Freeze** 25:27 Yeah, I think we need to talk about what the priority is of tying a network request to a button click, or whether we can live with everything being on… on whatever we decide a session is, and you have a timeline, and you just sort of see what's going on, right? That's still helpful. It's not… perfect. But, you know, I mean, if that's all we can do, I… we should do as much as we can, but, you know, having perfect contact, like you said, it's like.
you can get timestamps, they're not gonna be identical, you can guess. I mean, that's terrible, right? Like, that's not good enough, so… Yeah, I think tying this together is really tough.
**Ted Young** 26:06 Yeah.
**David Luna Bistuer** 26:06 Okay.
**Ted Young** 26:09 I mean, if it was just a technical challenge.
I would say it's worth it, right, to not have to guess and use heuristics when we're reconstructing.
you know, these graphs later, right? Like, it's worth it if the answer is, like, it's just tricky to figure out how to do it. But if it's, like, the implementation itself is just, like, cumbersome and inefficient and shitty.
That's… that's different from it's tricky to figure out.
**Jared Freeze** 26:37 Yeah, for sure.
We only have a couple minutes left. I do think that's a really important conversation. We should… probably pick it up next week, talking about, like, spans and logs and events, and kind of, you know, where we want to go with that, because I do think that open question is… kind of… it… I know, like, I write instrumentation every day, it's making it difficult, so, definitely put that on the agenda next week. But yeah, if we can move on to Waco… Demo metrics?
**Joaquín Díaz** 27:07 Yeah, just, created an issue with the demo metrics I used for the demo, but, if you have any other things in mind… please add them there, and I can update the demo.
So, yes, that's it.
**Jared Freeze** 27:24 Okay.
Thanks for that. And then, Abinet?
Looks like, hi. Yeah, you… yeah, the traces.
**Abinet Debele** 27:35 Yeah, I just created a discussion issue in the repo. Maybe I can share my screen and then… Yeah, so, this, issue, I think something similar has been raised before for some other reason, but this one is the, just, suggest a proposal, like, to separate the XHR and FH tracers from the user interaction. So this is assuming that we are still using the XHR and fetch limitations in the JS repo.
As well as the user interaction instrumentation in there, which is emitting response at this time. So the… when a click, event happens, for example, and there are some multiple XHR or FH calls happening, and if that application is also instrumented on the server side. There is an APM call happening, or an APM instrumentation.
the… the traces at the back end, at the APM side. We want to do, like, some business transaction correlations, so we want to see what initiated that transaction, that call.
So the backend implementation usually is, like, using the trace information from the initiator.
So since one click has one trace and everything under it is under a single trace, usually the B correlation is not properly, properly showing up, so, the same BT will be applied to the… all of the calls, all of the APM calls, and… Since this, this is a bit difficult to solve on the backend side, but it's easier on the… on the agent side, we can… if we have separate traces, if XHR and fake trace are independent traces that are, created by their own, on their own, like, not, Not using the active context from the user interaction.
then we can have separate traces, so the APM will have a single trace to deal with, so the correlation can be fixed that way, so… So, it's just a suggestion, like, if we have a flag.
Like, a config where we separate the traces.
So… at the instrumentation level, we can have this configuration. So if this is happening, then we can have… we can create a new… a new trace with root context instead of using the active context from the, The user interaction instrument implementation.
And still, we can… we can, maintain the relationship with the parent clique through… maybe spun links, like, we can have a spawn link where the context is saved, and also the attribute, the link type is saved. You can have something like this to maintain the link, and we can… we can still show them in the UI, like, using this information, that they are linked in some way.
So this, is, it's just a suggestion, like, if, if it looks good, I can… I can create a PR, and we can, we can proceed on it, so… I just want to know what you think about it.
**Jared Freeze** 31:13 Okay.
Well, thank… yeah, thanks for doing that. We'll, we'll definitely check out the link.
Yeah, and we'll figure out, you know, next steps, or, you know, if it needs a PR, whatever, so… Yeah, thanks for doing that. I think we're at time now, so I'll see everybody next week.
**Abinet Debele** 31:32 Alright, thank you, bye.
**David Luna Bistuer** 31:33 My…
