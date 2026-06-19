SIG: Browser SIG
Date: 2026-06-18
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Martin Kuba** 03:00 Hey, everyone.
Just waiting a couple more minutes, I guess.
Alright, yeah, let's get started.
Joaquin, does anyone have any… Things they want to discuss. If you do, please put it on the agenda.
**David Luna Bistuer** 04:00 There is none. Okay. Okay.
**Cleo Schneider** 04:12 Yeah, I got one.
So as… as Brian and I are kind of getting ramped up, we've been digging through some old stuff and some… and all of the old chats, and we saw some… comments sort of alluding to a bias towards log events, especially around user interactions, a bias towards log events over spans. And I just wanted to better understand that context, because… Well, first I want to better understand that context, and then… and then I want to explore some use cases.
**Martin Kuba** 04:52 So is this specifically just for user interactions? Are you talking about, like, the distinction between, like, the span-based instrumentation we had in the past, and, like, moving on to more just events?
**Cleo Schneider** 05:06 Yeah, and… and the… the two libraries that exist, and kind of, do we intend to sunset the user interaction library in favor of the user action? Are they complementary? Like, what is kind of the stance of the group here? And just… just some… Better understanding of that historical context.
**Martin Kuba** 05:26 So I'm just gonna tell it from my perspective.
**Cleo Schneider** 05:29 Okay, yeah.
**Martin Kuba** 05:30 So, like, the user interactions, instrumentations that was on spans, based on spans, is very old. It was developed, like, at the very early stages of the JavaScript SDK. At that point, there was no logs in OpenTelemetry, so the only signal that people could use was spans.
So that was one reason.
It is in my… it is currently… it's not maintained, there's no one… no one maintaining it. So I think, I… I would, from my perspective, I think we should deprecate it, or… or sun, sunset it. In, It relies on the idea… the idea is that Even, like, the idea of it is kind of experimental, because it's essentially trying to create a span that represents some kind of duration of What effect the interaction had.
It does that through, like, async… async context propagation, which is… really problematic in browsers. Currently, it relies on Zone.js, which we do not want to support. Zone.js itself is no longer, I think, Yeah, I think it's no longer supported.
And, and even, even then, even if he did have a good, good, good support for async context propagation in the browser. I think still, I think it's up to debate whether or not that functionality makes sense, because, like, how do you determine, like, when that interaction, like, actually finishes? .
**Cleo Schneider** 07:17 Yeah.
**Martin Kuba** 07:18 I think that's…
**Cleo Schneider** 07:20 Yeah, I think that's something we've been… we've been playing around with and thinking about a lot, because intuitively, like, from a debugging sense, when someone's, like, coming in to look at what the heck happened, right? They're kind of… they're kind of… three different layers. There's, okay, what views was this customer looking at, or this developer looking at, right? Of, like, okay, they were on this page, then they were on this page, then they're on this page, and then… Underneath that, there are kind of, like, the actions that they took, okay? They scrolled here, they clicked here, they did… did something, right?
And each of those, you know, actions spurred some number of executions. And I think that that, from a, like, from a customer perspective.
makes a lot of sense. You're like, okay, well, what did the customer do? What did my… as a developer, what did my customer do? And then, what happened after that?
And I also think from the perspective of if we consider session replay at some point in the future for this group, that also becomes somewhat relevant. And so, I just wanted to sort of… See, what are your thoughts on… on that?
**Martin Kuba** 08:35 Yeah, I mean, so… so I think… I'm not sure, like, where… how, like, you said, you're modeling the page.
like, somebody, like, went to this page, this view, and, like, you want to see what they did. So, I think from this higher perspective.
like, we… I think there were attempts, like.
In the past, to model it using spans or traces.
But, like, we've… like, we very early on decided that there was not the right way to model it, that, like, the correct model for… for… The user experience is the session, it's not a trace.
**Cleo Schneider** 09:08 Yeah, right, totally.
**Martin Kuba** 09:09 Yeah, so, like, within a session, you have a lot of different events that happen, and you could also have… you could also start traces within, like, that session, right? So I think the, so, like, page… page view is not modeled as a trace.
**Cleo Schneider** 09:25 Yeah, agreed.
**Martin Kuba** 09:26 Yeah. Yeah. So the, but it does make sense… to model HTTP requests as traces, because they connect to the backend, right? Yeah. So you want to see… you want to connect client span that represents the start, the root span, to, like, what happened in the backend. Now, the question is, do you want to go one level higher? Is it useful to go to one level higher, to see, like…
**Cleo Schneider** 09:49 Yeah.
**Martin Kuba** 09:50 what the interaction is, that's the… I think that's the thing that's up to debate.
**Cleo Schneider** 09:55 Yeah. I think also one thing that we're… we're thinking about is, like.
the… the time of… of UI render as well, and, like, how would you measure a UI render?
Duration, through various mechanisms, you know, and… and so… and… a UI render in isolation is maybe not as helpful as seeing, like, oh, we initiated a network request, we got data back.
And then there was this UI render event. But I hear what you're saying in terms of the async context propagation is messy, right? You can't directly say, okay, this, you know, network call resulted in this.
But I guess… Yeah, I'm trying to think about… does that matter, right? Like, is the collection of those events still useful from a debugging perspective?
**Martin Kuba** 10:50 Yeah, I mean, so that's why we're collecting the events, right? I mean, so…
**Cleo Schneider** 10:55 Yeah.
**Martin Kuba** 10:55 If you wanted to have… If you wanted to, like, represent user interactions as spans, then you have to solve this issue of, like, of context propagation.
**Cleo Schneider** 11:05 Yes, yep, totally. Totally.
Yeah.
Yep.
Okay, we're gonna noodle on it more, because… oh, yeah, who… who said something?
**Joaquín Díaz** 11:18 Alright. No, I just wanted to add that, I think at some point we have to figure out how smart we want the SDK to be, and I think there are a lot of these issues that maybe need to be solved by the user implementing the SDK and not by us. Mostly around.
**Martin Kuba** 11:35 What?
**Joaquín Díaz** 11:36 goes with what? Like, I think maybe for you and for me, it also makes sense that if you click something that triggers a request, and that triggers a render. That also goes together, right? But maybe for someone else, it doesn't. So, I think it's… Hard to say, Given that, I think the approach we mostly take is we emit the information, and then we let the user do whatever they want with that.
**Cleo Schneider** 11:59 them together, yeah.
**Joaquín Díaz** 12:00 Yeah, there are places where we take decisions and we make it more easy for the user, but most of the times we choose to just be more… Object and say, this is what the process says that happened, and then it's up to you to take that information and make it whatever you need to do.
**Cleo Schneider** 12:23 Yeah.
That's really… that's really helpful context, and and useful as I'm, like, starting to get to know the… the instrumentation libraries a little bit to… To understand that stance, so… Appreciate it.
**Joaquín Díaz** 12:37 Yeah, and then there's a lot of debate around events and spans in a way of… events is usually easier, to deal with, it's just one single thing, and that's it.
Overall, as for… sometimes I'll… We may even thought about, like, we may send an event that has a duration as an attribute, and that maybe solves the issue, but then… The spans are better represented by many different tools, if you actually beat out the span.
I think that's also something you have to have in mind, that… there are already a lot of things that exist that collect spans and logs and then show them differently, like tempo or Locky.
And then you have to also think about them when you are trying to figure out how you are going to collect your information.
**Cleo Schneider** 13:30 Yeah.
Yeah, totally. And I guess there's some… some… like, if a log has a duration on it, like, is it just a span without a parent, you know? It's…
**Joaquín Díaz** 13:46 Yeah, you know, I mean, you may have spans that they don't have children or parents, that's fine.
**Cleo Schneider** 13:52 Yeah.
**Joaquín Díaz** 13:52 But also, like.
I think, yeah, again, I don't think we have a proper answer for this. I think it's a case-by-case basis.
But yeah, it's just a lot of things you have to have in mind, mostly around the tools that will actually use this later.
**Martin Kuba** 14:09 I mean, the other thing that, like, I think we're… we have to take into account is, just the overhead of the additional code. Like, we have, you know.
if… like, it's important for some users, it might be important to, like, keep the bundle as small as possible, and then, like, they don't need the overhead of the trace SDK.
Yeah, I mean, the trace SDK kind of implies that you're, like, measuring something, right? Like, you start something, you add something, and also a lot of the signals… A lot of the signals that we get from browser don't happen like that.
you know, maybe the interaction might happen like that, but, like, a lot of the signals, like, where we actually send, like, a numeric, numeric duration value, like, we get it from a browser API, After the fact that it happened, so, like, at that point you're not tracing, you're just collecting the data that you already got in the browser.
**Cleo Schneider** 15:03 Yeah, that makes sense.
**Martin Kuba** 15:11 Okay, Happy to talk about this some more if you have more questions later, or just, like, jump in the Slack.
**Cleo Schneider** 15:19 Yeah, I'm… yeah, I think this is useful context, and I definitely have more to think about before I have more questions for y'all. I really appreciate it.
**Martin Kuba** 15:30 Cool.
David, you wanna talk about… this one…
**David Luna Bistuer** 15:34 Okay. Well, not to talk to have a discussion, but maybe just to, highlight it and ask for feedback on this one.
for the ones that need context is, as Martin said, so we have APIs that tell us info… that give us information after the fact. For example, for HTTP requests, with using the Fetch API or, XHR, we're getting resource timings after the fact, so after a few milliseconds, or… Something like that. And we have a resource timing instrumentation that actually collects that information, and we don't want to duplicate data. The former instrumentations are, Kind of holding the span.
until we get the resource entries and generate the span events, we want to change that and just correlate from spans, the HTTP spans, with the logs, so we add the context on the logs. Joaquin here offered kind of a solution for that, having kind of a intermediate… manager that… that, gives… gets information, you can stash information of the contacts there, and then you can query it later, okay? Okay, just… I just made a question, so I follow up the discussion, but I… I would like to have more feedback.
Just in case, you know, the more aisles, the better on this one.
**Joaquín Díaz** 16:54 Yeah, sorry, I didn't have time to answer, and also I was.
**David Luna Bistuer** 16:58 No worries.
**Joaquín Díaz** 16:59 to, proposal with some code, but again, it was…
**David Luna Bistuer** 17:04 seemingly.
**Joaquín Díaz** 17:04 for me. But yeah, as you were saying, like, the idea is to have something that sits on top of instrumentations, that has the context of Which network requests happen, so we can tie them to the resources.
I think your question was related to configuration, I think… I… wouldn't want users to have to do this. I don't want them to know that we have to do this.
I think it should work out of the box.
But given that we allow, like, a list of instrumentations. I don't know.
Yeah, I don't know if we have an option that will Do it by play for them, or do we… Yeah, I don't know how the API looks like, but I think that we shouldn't let… we shouldn't need them to do it, we should do it by… for them.
And there's… there should be some… generic configuration that applies to the three of them when it matters, like, for example.
if you want to ignore some URL, you don't need to set it 3 times, just once, and it says that, yeah, ignore these resources or other requests, whether you're using Fetch or XSR.
**David Luna Bistuer** 18:22 And maybe something that maybe I didn't get from your comment, so it means that the manager is going to be… you proposed having a couple of configurations.
Some kind of hook functions, and then use the manager to orchestrate sharing the context.
Would that configuration be the default one? And then that configuration is going to be available for users, for consumers of the package, so if someone… overrides or passes its own… his own configuration. Should we wrap it and then use, you know, wrap the function to use Context Manager and then apply the user-provided function?
that kind of is my… that's why I don't, I'm not sure about what should be… what we should be doing.
**Joaquín Díaz** 19:16 Yeah, I don't know, like, I… I mean, I think this is a… you get this from using the SDK, so it's like a… You get value from not having to eat.
On your own.
And then if you want to do it on your own, then I don't know if… That takes away the responsibility from us and to them to do it.
Like, I think there's only so… so much we can do for the users, and I think if we… only want to do it on the SDK, I will be fine with that, and then if we have documentation on how to do it, in case you don't want to use the SDK.
**David Luna Bistuer** 19:58 Oh, dear.
**Joaquín Díaz** 20:00 Because, yeah, I… yeah.
But all these things that are, like.
helping them, setting up the SDK in an easy way. I think they all live on the SDK packet, and it only applies if you use the SDK, and then otherwise… I think, again, we should, for example, export the manager so they can use it, but they have to set it up on their own.
**David Luna Bistuer** 20:27 Okay. So, for example, in that good snippet, good snippet that I shared.
that situation, then the user is responsible to, user manager, import the network manager, and then use it in the configurations.
**Joaquín Díaz** 20:41 In that case, I don't know, because they are using the SDK. It's not that they are… what I'm saying is that if they don't use the SDK at all, then they have to set up the manager. But if they use the SDK, I think we should set it up for them.
But with this API, I don't know how that would work, unless we… Iterate over the instrumentation survey internally and search for the ones that we want to Update, basically.
So that I don't know, that we may have to see if… Yeah, if there is other configurations that we can set up, so they don't have to send us a list of instrumentations. But at least the ones are… or maybe we create, like, a new new whatever instrumentation dropper that drops.
fetch XHR and the manager all together, and they work, and we instantiate them internally.
At least, like, something.
**David Luna Bistuer** 21:37 Huh.
**Joaquín Díaz** 21:39 Like, wrapper that they use in case they want to use, like, these three themes together.
I don't know how it… how it'll look, I have to… think about it. But in general, the pattern that I will follow is that on the SDK, if they use the SDK, they don't need to do it. If they don't use the SDK, they have to do it, if they want.
**David Luna Bistuer** 22:02 Okay.
By the way, that example is just using a scenario. Instrument, this is, I think, is not part of the configuration type yet. Okay.
we need to think about it, so maybe I'll create an issue for that, regarding this, this kind of, of behavior, about having defaults for instruments.
Or configurations.
**Joaquín Díaz** 22:27 Yeah, like, what we do at Embrace, we allow people to set their own list of instrumentations, but we also.
Create… that we also have our own default list of instrumentations.
I don't see anyone not using… Any network instrumentation.
I don't even see them choosing between one or the other. I think you don't know if you have a third-party library that is using XHR, and you only choose to use Fetch. You may miss those.
But that won't solve any other cases where we want people actually configuring.
There's also an option that where we create the instances, but they just send, like, a configuration object.
If they want, yeah, I think we have to think out of that API.
**David Luna Bistuer** 23:23 Okay.
Thank you.
**Martin Kuba** 23:34 Okay, I just had, like, one… I was looking at this, one more topic on this, on this PR that Jared opened.
David, I think I agree with you that it's… that it doesn't make sense… it doesn't make sense to me to… to move everything into an SDK folder.
I think all of… everything here is SDK.
And… these… I did comment on that this morning. It seems to me like this is more Aldi's… files that we have currently are more about initialization and configuration of the SDK.
So I was thinking maybe we could… instead of having an SDK folder, we could have, like, a config folder, or… You know, initialize folder.
Something like that, I'm not sure which… and I was just wondering, like, what you think about that.
**David Luna Bistuer** 24:31 That works for me, more… both work for me, but maybe… Config… Maybe it relates more to the type, right?
Maybe you should pass. So maybe initialize, initializers, maybe it's a better category for that.
**Martin Kuba** 24:49 Yeah, I mean, it's… it's…
**David Luna Bistuer** 24:52 Naming is hard.
**Martin Kuba** 24:53 Naming, naming's the worst, yeah.
But, you know, in the end, like, this is… I don't… we're not gonna be exporting these folders, like, like we do in the instrumentation package.
So, it's just, like, internal organization that you can always, like.
**David Luna Bistuer** 25:08 Yeah.
**Martin Kuba** 25:08 String more things… more things around.
So… but I just… but I do think that the SDK folder doesn't make… doesn't make sense, so…
**David Luna Bistuer** 25:17 Okay, so I'll… okay, I'll… I'll put a comment back, again, agreeing with that, so maybe, Jared can just change it and… We can merge it right away.
**Martin Kuba** 25:31 Right, anything else?
Alright, sounds good. Thanks, everyone.
**David Luna Bistuer** 25:38 Thank you. Dr. Leiter. Have a good day.
Bye.
