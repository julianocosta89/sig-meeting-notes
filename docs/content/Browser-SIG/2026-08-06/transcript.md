SIG: Browser SIG
Date: 2026-08-06
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Cleo Schneider** 01:29 Sorry, my speakers were… Hey, Martin, how's it going?
**Martin Kuba** 01:32 I'm fine, how are you.
**Cleo Schneider** 01:32 Alright. Doing alright.
**David Luna (Elastic)** 01:40 Hello? Good morning.
**Martin Kuba** 01:43 Hi, David.
Yeah, I think, I think Jared and Joaquin are not joining today.
And I think Ted is out as well.
So, again… Hey, Wolfgang.
**Wolfgang Therrien** 02:46 Hello, hello.
**Martin Kuba** 02:48 How are you?
**Wolfgang Therrien** 02:50 I'm doing pretty well, I'm happy to be able to be back at it.
It's been a hot minute.
**Martin Kuba** 02:56 It's good to see you back.
Okay, we can, we can get started. David and Maxime.
You have the first one.
**David Luna (Elastic)** 03:14 Yep, okay, so maybe I'll try to give as context as possible. So, this started as a PR that I think it's going to be merged, so the PR from Maxim, basically what it does is just, do, I think we discussed last week, a validation of the URLs, and then just… You know, I don't know.
No, skips?
the, the, the, the initialization of the SDK is if, if the, if those URLs are wrong.
I remember Trent commenting that that's what the configuration does, and therefore, having a similar behavior between JavaScript SDKs makes sense.
But then there was a slight change in one of the types, and it generated a discussion that the link is in the… in… here, it's pasted on the document. So, basically, so long story short, as I said, so there is this… is, this function that combines different SDKs, now we are using the combined, logs SDK and Trace SDK. At the beginning was meant to, be kind of a… and utility function for users to be able to create their own SDKs, or, yeah, short of SDKs, so if you want to have metrics, or any different SDKs, or something similar, they can just combine it with the logs and the Traces SDK, okay?
When we publish the, the SDK package.
that got excluded from the exports. So, now.
At the moment, it says that combined is the case.
It's, it's just used a utility function that it's just inside, okay?
So… The change that, the type change that, that Maxime is doing, it's fine.
Until… as long as the combined SDKs, it's internal.
Because it limits the properties, so that function was used in genetics, so whenever you're adding a new SDK under that key, then the resulting function, the composite function.
has a property with that given name, and accepts specifically the type of that SDK.
With the change of maxim, it just accepts both… a couple of entries, so it's locks configuration, entries configuration, and that's it.
So… I guess the question is not about the type itself or whatever, but, maybe kind of a more… metaphor, more high-level question about this, like, okay, do we want to, maybe now, or in the near future, or maybe later, to expose that function on the public API and let people compose and have their things, or… the alternative is to say, okay, if you want to use your own SDK, you just have to wrap the former SDKs, like logs and traces, and then do something by your own.
So… that's why I'm explaining here, so maybe we don't have to resolve it, like, today, but, you know, if you have any thoughts, so what do you think? Should an SDK expose functions to have composition and then let them build from that, or should we just expose the components that we have?
And let the customers glue themselves.
**Martin Kuba** 06:43 I mean, the composition, would… would be useful… Only if we… if we add the metrics SDK as well.
**David Luna (Elastic)** 06:52 Yeah, that… in that sense, you have, for example, I'm going to say it, so Elastic has… We are having a distribution, so we as the users, we would like to have the compos… it's convenient for us to have this, because we are just, you know, pulling the logs and traces SDK from upstream. We have our own metrics SDK, and we just combine them together into a single function.
We expose that function to the user, and then just… the user just starts the SDK that actually is just a combination of the three of them.
Okay.
So yeah, or the alternative is just to say, you know, it's like, for people that are using FCM, say, okay, maybe you just provide that document and say, okay, if you want to use your one of the SDKs, or both as the SDKs.
And do something else.
You have to create a wrapper function, or whatever, and do your own business, so… pass the configuration to the AppSum SDKs, and then do something with… with the API, and… and other components to create your own SDK and having that wrapped in a single function.
**Martin Kuba** 08:03 I see.
Yeah, I don't know off the top of my head. I think… I don't see, like, a reason not to… not to expose that function, if that's useful.
But I'll take a look at the context that you're…
**David Luna (Elastic)** 08:19 Hmm.
**Martin Kuba** 08:19 This, in this, in this pull request, and…
**David Luna (Elastic)** 08:24 Would it make sense, maybe we could create a discussion in the, in the, In the repository, maybe can try to expose different examples.
Yeah? Yeah.
**Martin Kuba** 08:35 Yeah, examples would be good, yeah.
**David Luna (Elastic)** 08:44 Okay.
Okay, so yeah, that's me. Martin, you can… Continue.
**Martin Kuba** 09:09 Okay, yeah, I have, I have to think I can share my screen, I have two things, Yeah, so this one, David, you've been… you just commented on this one. There's a… So we have… we have these, These callback functions on the instrumentations to add custom attributes.
And right now, we have 3 instrumentations that have them, and 4 that don't.
the, the signatures and these functions are duplicated on the instrumentation, so I created… this issue… This one… Which… proposes, adding, like, the same… the same thing on the SDK level, like a global, callback, so… which would automatically apply the custom attributes to all the instrumentations.
That would have to be done using, processors, so the signature there is a little bit different, or the approach is a little bit different.
So, and then I was thinking maybe we could then deprecate these functions on the individual instrumentations.
David, you, you noted that, Maybe sometime we might, need, like, the instrumentation-specific event.
In the, in the function, so… I guess my question is, Do we want to still pursue this global, callback, I think yes, because it… I think the answer is yes there, because it makes it a lot easier to… to, add kind of generic attributes. But then, like, we would… Keep the… these functions On the instrumentations only if it's useful for that specific instrumentation to have access to the event.
it's… it's not ideal, in my… because, like, there's still two ways to add custom attributes, so we'd have to, like, documentation around this. Like, if you… if you need to make a decision based on the instrumentation specifically, you would need to use this approach. If you want to do the global attributes, use this approach.
So I just wanted to see if people have any thoughts, or… on this one.
**Wolfgang Therrien** 11:47 Yeah, I think it resonates to have it sort of at both levels. I can definitely see where you'd want to apply custom attributes across everything that sort of comes through, but… and also maybe only for a specific subset that's emitted for a particular instrumentation.
I'm wondering if we've considered, sort of, a way to… inject some of that instrumentation-specific, like, sourcing so that maybe it could be filtered out, so we would still just have one way to do it, but we have enough information for the consumer to.
Either, you know, drop it or omit it based on, you know, what their needs are without having to configure it at every instrumentation level.
And if that's preferable over having these two entry points, I'm not sure what would be more straightforward for customers.
**Rebecca He** 12:39 The goal…
**Martin Kuba** 12:41 Right.
**Rebecca He** 12:42 Sorry, is the goal to make it easier for customers, or is the goal to make it easier for us to maintain?
Because, like, those are two slightly different goals. If it's for easier for customers, it's, like.
like, we're doing this now, right? And it's not that hard to create a block.
For the callback, and then just pass it into each of the instrumentation lives.
It's not… really that complicated or non-performant. I don't know how the, like, the global thing works, but if it's just a single processor that applies to all the instrumentations, I could see that being, like, easier for us to maintain, rather than having to pipe this logic through each of the instrumentation code, so I was just, like, wondering.
**Martin Kuba** 13:27 Yeah, I think it's probably both. Like, one… one is, to make it easier, because otherwise you'd have to… I don't know if I have an example… You know, like you… so you're passing… you're registering, like, each instrumentation individually, and you have to pass, like, the configuration to each of… like, that function to each of these constructors, right? So you have to do it in multiple places. Not a big deal, but it's a little bit of… not as ideal as just having it in one place.
And then, like, the other motivation was just to have a duplicated code across all these instrumentations. But, I mean, if… sounds like we might need to have it anyway, because… because of… Instrumentations that need specific, like, context.
in those functions.
Amen.
**Trent Mick** 14:20 Is… is… is this perf… Doing the same… Sorry, could… could a user not just create a log record processor and a SPAN processor? Is that…
**Martin Kuba** 14:32 Well, yes, they could, but then, like, you can't pass the log… the processors have… signature where you can't pass the context, right? You'd have to, like, add it to the… You'd have to add, like, the event, like, the browser event, like, maybe to a context?
**Trent Mick** 14:47 Oh, sorry, I don't… I don't mean the instrumentation-specific ones. I mean this feature… forget… like, I understand the reason, potentially, for the instrumentation-specific ones, if they want to base it on… the event data. But… Is this feature providing another way to create a span processor?
And if so, what's the point?
**Martin Kuba** 15:13 Okay.
Yeah, so, like, instead of, like, having it built in, like, they would… they could just add their own processor.
**Trent Mick** 15:22 Yeah, if the only thing that serves is to do another way to create a span processor, or a log record processor, then… I don't know if I'd wanna… if it's my thing to maintain, have another way to do it, rather than just providing some docs. Like, if you have this use case, here's how you, like, the SDK Bless technique for doing this is a processor.
**Martin Kuba** 15:46 Yeah, I guess… I guess that's a good point. Maybe we don't need it at all.
**Wolfgang Therrien** 15:57 Yeah, I like that approach, and I think if there's… if there's increased friction, we could always Try to figure out a way to increase the visibility of that documentation, or maybe it's better examples, or maybe it is sort of like a a simplified configuration hook that just uses a spend processor underneath, or a log processor underneath, if that becomes a huge problem for folks, but… If it… if we already have a mechanism for it, that makes a lot of sense.
**Martin Kuba** 16:26 Okay.
Yeah, I mean, so, like, these… So maybe I'll close this issue, and just, like, instead of, document that use case somewhere.
And then, the other thing is that all these… let's see… these, These functions right now, like, are… Don't actually have the instrumentation context.
If you look at all these, like, bivirals, it doesn't have it in the signature.
User action doesn't have it, so… Maybe, Maybe, like, we should be adding, like, these callbacks only to the instrumentations that actually need it, that's what I'm saying.
**Trent Mick** 17:21 Yeah, earlier you asked for feedback on those things. If I had to do it again as an instrumentation, or as a maintainer when instrumentations are going in, I'd want there to be a good justification for why this specific instrumentation needs this callback to do it, because it's possible that some of those were added just because, oh, well, we've seen it in some other instrumentation, so we feel like we can, let's do it. Yeah.
**Martin Kuba** 17:43 Yeah.
**Trent Mick** 17:43 At least from the point of view of working on the declarative config stuff, you can't model a callback function in declarative config, so the tendency has been to avoid doing those in instrumentations where we can. So yeah, if you see a case where there isn't any instrumentation-specific data being passed to that callback, then we'll… Processors may be a better answer.
**Martin Kuba** 18:06 Yeah, okay, that makes sense, that makes sense to me.
Okay, cool.
Right, I'll… so we have one PR open for this, so I'll make that comment on that PR.
Okay, The other thing that I had is I have had this roadmap here open for a couple of weeks now, and I'd like to merge it.
Today or tomorrow, so this is last call.
For anyone who wants to look at it.
So… David, okay, next one.
**David Luna (Elastic)** 18:54 Sorry, mute. Same thing. Last call on the fetch instrumentation.
So, the last, discussion was about The registry of, for context, for navigation, no, for network context registry. I think Jared discovered that it was a problem that, we could have a registry that's growing endlessly.
If nobody is just, you know, unregistering context, there was a PR… I did the fix in a separate PR instead of in the fetch one, just to avoid more noise on the fetches. The fetch PR is big enough, in my opinion.
So now the PR is, the fix for context registry is already merged.
I did the sync with my branch.
So… Same thing here. So, last call for reviews.
And… yeah, I'm trying to… Merge this, Maybe tomorrow or next week, the beginning of the next week.
Okay, and then, hopefully then… Xhr, comes next.
With the same approach.
**Martin Kuba** 20:09 Thanks, Jed. I'll take one more look, must merge it.
Alright, I just have… I wanted to… this is just inform, I did a presentation at the, Spec SIG this week.
About the status of our browser's SIG.
The talking points are in this document.
Feel free to take a look.
It, it very much aligns with the, with the roadmap documents.
Okay, and Cleo?
**Cleo Schneider** 20:56 Yeah, so I, I threw up a draft PR, and posted in Slack. This is just for updating onboarding documents based on some of the stuff that we've learned as we have onboarded. So would love some eyes on that. In particular, I added one new doc that was SIG operations, just to document what our processes are. But I had some open questions, because I actually… I don't… I don't know exactly what, what, what, what they are, or what we would like them to be. So… folks have feelings about that, feel free to chime in on the Slack, or if you want to have that conversation now, we can do that.
**Martin Kuba** 21:40 Awesome. Thanks for doing that.
**Cleo Schneider** 21:42 Yeah.
**Martin Kuba** 21:48 Okay, does anyone have anything else they want to talk about today?
Right? If not, we can… we can probably call it then.
Thanks, everyone.
**David Luna (Elastic)** 22:05 Thank you. Have a nice day.
**Trent Mick** 22:06 Nice.
