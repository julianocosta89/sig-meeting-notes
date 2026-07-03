SIG: Browser SIG
Date: 2026-07-02
Duration: 14 minutes
============================================================

## Zoom Recording Transcript

**Martin Kuba** 01:49 Hi, Jared.
Two jarreds. It's two jar.
**Jared Lewis** 01:56 birds, but… I bet.
**Martin Kuba** 02:01 Bye, Maxine.
**Jared Freeze** 02:11 Hey, I'm still a little sick, so I'm just listening in.
**Martin Kuba** 02:32 I'm just, just catching up after vacation. How are things going?
**Joaquín Díaz** 02:42 All good.
I think we need good progress.
Wimmer Steam Network.
Not network, sorry, like, context special tree, and that for network.
And, do I see… fashion instrumentation PR up, only one now on, jared and I did that.
for our review, I think, is pretty good. So, yeah, I think we're closer to merging that.
**Martin Kuba** 03:11 That's… that's great.
Awesome.
Does anyone have any topics today? There's nothing on the agenda right now.
**Maxime Quentin** 03:30 Not on my side. Just wanted to let you know that I've updated the issue about, you know, deprecating the browser command.
So, last… I think the last move is just to duplicate the… The package within… That's pretty much it on my side.
**Martin Kuba** 03:53 Yeah, that's… that sounds great, yeah, thanks for doing that, and… I have updated the issue with the checklist, so… Yeah, and same thing has to be done for a bunch of other packages in Contrib.
They also have to be deprecated, so we can… maybe we can do, like, the one sweep, and do all of them together.
**Maxime Quentin** 04:16 No, a lot of performance.
If you don't mind, like, guiding me a bit on what are the priority, it's perfect for me.
**Martin Kuba** 04:24 Okay, cool, sounds good Thanks.
**Joaquín Díaz** 04:28 Yeah, as I was saying, like, if you can take a look at the fetch Instrumentation PR, I also created another PR with a small end-to-end setup. I did originally for my instrumentation PR, but I closed that one. I just opened a new one with the end-to-end setup, so we can start having also end-to-end tests, alongside the unit test.
**Martin Kuba** 04:55 Okay, let me find that PR, just put it in the notes, Is that… is that David's PR… PR?
**Joaquín Díaz** 05:06 Yes, that's CFetch.
PR, and mine is… I cannot agree.
**Martin Kuba** 05:16 Hold on.
**Joaquín Díaz** 05:42 Yep.
**Martin Kuba** 05:43 Okay, great, thank you.
The only thing that I wanted to follow up on, is… Jared's PR on… Renaming the folder in the SDK package?
David and I proposed the name, so… if, God, let me just put it in the notes as well.
Yeah, Jared, if you have any thoughts on this, you don't need to speak, but there's been… I'm just curious about your thoughts about what would be proposed there, so… That's, cool.
Anything else?
**Maxime Quentin** 07:07 I had a question about, like, shared, context.
Do you plan to have it, like, I mean, what's the plan on the long term? Do we rely on it a lot, or do we just use it as a temporary approach before entities, or is it something…
**Joaquín Díaz** 07:31 I think it's a workaround for… Having a proper context monitor on the web, which we don't have.
Like, I think ideally we shouldn't be doing that, but that's the easiest solution that we found, just to unblock the fetch instrumentation migration.
I mean, it can be useful to… solve these kind of issues that we're having with it, but ideally, I will… Like, to have, like, a proper context monitor.
Instead of having to share, like, context manually.
And where she's sitting, and where she's sitting, yeah.
**Maxime Quentin** 08:13 And… What's the long-term strategy do we want to, kind of.
all the state of stuff, like counting errors, counting resources, or is it just to enable some instrumentation and, like, just share some… Like, live, live state.
**Joaquín Díaz** 08:34 Yeah, I think it's only when necessary. I don't think we need to share everything, I think… instrumentation should be as inevitable as possible, and this case was only required so we can break down They… not having fetch, relying on resource-time instrumentation, and having something in the mail, but I kind of think of another example where we would want to share context within instrumentations right now.
But I guess… Once we find another example, we can review the approach and see if that works, or we want to try something else.
But yeah, for now, I think ideally, we should try to avoid it, if possible.
Yeah, right.
mainly, as Terry is saying, like, I think we should have proper context propagation, and not having something like that.
**Maxime Quentin** 09:31 P.
Interesting.
**Martin Kuba** 09:40 Yeah, I'd be curious, like, to know, like, what other use cases there are.
And this seems to me like a very unique use case, just because of the timing of the… The spans and the resource timing.
Events are getting emitted.
I mean, the other use case that's been around is the, the user action instrumentation that generates spans.
But we've, we've kind of sort of, I think.
Maybe something to talk… we should discuss, But I kind of have the feeling that we probably want to deprecate that instrumentation in favor of the just event or event-based instrumentation for user actions.
So, I'd be curious, like, if there are any other use cases that come up.
**Joaquín Díaz** 10:32 Yeah. Again, I don't have any right now. I think, as you were saying, like.
As we kept… kept moving towards… logs for events-based instrumentation that I don't think we'll have A lot of context to share.
We also have Once we do, like, measures, like, performance measure, that will create a span.
That we may wanna… tied to something else, but, right now I can't think of another example.
**Maxime Quentin** 11:09 Or maybe, like, errors and, like, user actions and errors, or stuff like that, if you… Spots that NR occur during, During a user action, maybe you need some kind of shared context to… like, to tie the two, but I don't know.
**Joaquín Díaz** 11:31 Yeah, but I don't know if a user action should be a span, I think it's more like an event. I think then you can, of course, have spuns representing some job on your page, right? I don't know.
checkout form, or whatever, that has many things inside it, and in that case, you will want to share context, but… Right now, I think… I think that falls into the user's responsibility, given that we don't have a context manager.
**Maxime Quentin** 11:59 Makes sense.
**Martin Kuba** 12:14 Okay, Mr. Edd, does anyone have any other topics they would like to bring up?
Jared, the other Jared, Jared Lewis, are you, are you here for the first time?
**Jared Lewis** 12:32 I am. I, am trying to get into contributing to OpenTelemetry, and, my background is in web dev, so, and with JavaScript, I'm… I've been attending the JavaScript meetings and trying out this one, seeing if there's issues I can help contribute to, but pretty new to the, OTEL world, aside from just looking at logs and metrics through Splunk that somebody else used OTEL to connect to, right? So… Yeah.
**Martin Kuba** 13:05 Do you have any… any specific, questions or… or interests in… for this group?
**Jared Lewis** 13:11 Not yet, but I will say, the… I mean, well, the browser SIG feels new to me, right? Like, are… is it somewhat new, and… This instrumentation for the browser, it's a new addition, or am I incorrect about that?
**Martin Kuba** 13:29 It's fairly new, yes, like, it's… compared to other SDKs, yeah.
**Jared Lewis** 13:35 Yeah. Well, most of my questions I can research on my own, but, yeah, I'll just be looking into, like, the status of it, what's been done so far, what's coming up, and see if I can contribute in any ways.
**Martin Kuba** 13:47 Awesome, man, welcome.
Alright, well, if, there are no other topics, maybe we can… we can end early today.
**Maxime Quentin** 13:59 Nope.
Bye-bye.
**Martin Kuba** 14:01 Bye, thanks everyone.
