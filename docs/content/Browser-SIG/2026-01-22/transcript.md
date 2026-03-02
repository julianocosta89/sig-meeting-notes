SIG: Browser SIG
Date: 2026-01-22
Duration: 11 minutes
============================================================

## Zoom Recording Transcript

**martinkuba** 02:12 Hello.
**Benoît Zugmeyer** 02:18 Nope.
**martinkuba** 02:23 I was sort of wondering…
Good, good.
So there's, there's nothing on the agenda right now. Does… if anyone has anything they want to talk about, can you please put it on the agenda?
Hey, Benoit, I, your PR.
I can merge it, but it needs to be, synced with the main branch?
**Benoît Zugmeyer** 03:28 Okay.
**martinkuba** 03:29 Yeah, if you can do that, then I'll merge it.
**David Luna Bistuer** 03:49 So, well, I'm going to bring a topic, maybe… Low level, but…
And I just found it today, so I don't have much information, so I'll file an issue here.
in the correpon, there is,
An issue if you don't set a…
Context Manager the Zone 1, or something more elaborated and using the default stack context manager.
And this is because, but basically, so we are instrumenting the exports. So whenever you have, you get to create a web disk provider, and you don't provide a context manager, it uses the default one, which is the stack one.
The HTTP exporters, they're doing some asynchronous shop.
Before doing the export, the actual fetch.
To, to the endpoint.
That fetch is also instrumented, it's taken as a span, and then we get into this kind of endless loop that we're sending another
Another fetch to export, that gets instrumented again, and then, and again, and again, and again, and again.
So that's the TL.
TLDR, okay, I'll file an issue and try to find a solution for that.
Okay.
I guess…
most of other people are using other context managers, but I guess that out of the box, it should work.
Song.
So yeah, I'll create an issue for that.
So, if I understand correctly, the issue is that it creates… generates continuous traffic?
**martinkuba** 05:26 This way? Yeah. Okay.
**David Luna Bistuer** 05:27 The problem… so there was a PR, let me check if…
Yeah, let me check if I can find it. There is NPR that actually added a new,
Feature, which was kind of the… they wanted to resolve the headers in a way, an asynchronous way.
So you can provide a factory function for headers, and it could be synchronous. That was because some people, some customers wanted to
Asked for having, kind of,
Be able to just update these headers dynamically, to add all tokens, or something similar.
then the result of that is, like, okay, previous to the fetch, there is a… there is an async call, there is an async function that is running, then the stat context manager is one of the mana… the context there, it's lost.
And then the fetch, there is no… the supress tracing entry for the context, it's gone, it's not there.
So then the fetch gets instrumented, and then gets, the span gets created. Instead of getting a no-op span, non-recorded span.
You get the, an actual span.
So, that's… that's a culprit.
Yeah, so I'll work on that. I guess the idea is, I think, if I'm not mistaken, the superstacing, happens in… I think that it's done in the,
Spam processors?
So before the exports, right? Spanish processing, that's… we're doing the supressing, maybe,
Kind of a naive approach would be that
Get it closer to the low level, and then suppress this thing only.
Instead of doing… so, being the exporters that actually are the ones that are doing it, it's super stressing for that.
Instead of the… of being, several other years before, because…
That might get lost, at least for browser.
Okay, I'll add more information, maybe I'll take that document pointing to the issue, and then feel free to add your comments, your observations, or your questions there.
**martinkuba** 07:32 Okay, sounds good. So, like, is this issue with, with Node as well, or is it just… or is it, like, specific to browser?
**David Luna Bistuer** 07:38 Nope.
Is it specific to the browser?
Note is using the async Context Manager, so the… yeah, the single color storage.
With that, you get the right… because we all have something similar, we don't have the same in browser yet.
We are experiencing that with this one.
One solution may be just using a different context manager, like the zone one, but I've seen already that there are some issues that people are asking about having a zoneless context manager.
So there… there is an interest of
having the option to… to remove that… that context manager. So, yeah, if we can make it work.
with the default one would be a good… a good thing to have. Nice to have.
Okay, so yeah, I'll keep you posted.
**martinkuba** 08:28 Thanks for catching that and working on that.
So I guess this is the only… is that the only topic? Does anyone have anything else? Is there anyone stuck on something, or do they need help?
**Jared Freeze** 08:50 I was just gonna bring up, like, the sort of publishing and versioning. I think it needs, like, a champion, to get that stuff out the door, so… I know that there's already a ticket, there. Like, there's an issue for first instrumentation being published.
So, just wanted to bring that up again.
**Ted Young** 09:13 Is anyone feeling like there isn't enough available to work on? Like, we could paralyze more than we currently are?
I don't feel that way, but I'm just curious.
Sounds like no.
**martinkuba** 09:39 Yeah, I'm thinking, I feel like, like, all the, like, we touched on this a little bit last week, I think, like, as far as instrumentation goes, like, we have… all the instrumentation tasks are assigned.
I think people are working on that, on those,
There are a couple of people, like, who work on two instrumentations that have not been attending.
So, yeah, I'll just… maybe I'll check with them.
I think… but I… but I think, probably our primary
Goal, like, right now should be just to get to a point where we can release
And after that,
Kinda move on to the next step, which would be, you know, to probably generate more tasks, tasks of things to work on.
**Ted Young** 10:30 Cool.
Yeah, when we release, we can maybe… we'll make a blog post and stuff, see if we can get more interest in the SIG, more people coming in and help.
**martinkuba** 10:40 Got it.
Alright, well, I don't have anything specific for Els for this meeting,
I guess it'd be done, if nobody else has, then… We can end it early.
**Ted Young** 11:04 Sounds good.
**martinkuba** 11:05 Alright, thanks everyone.
See you.
