SIG: Browser SIG
Date: 2026-06-04
Duration: 31 minutes
============================================================

## Zoom Recording Transcript

**Jared Freeze** 00:41 It's a…
**Ted Young** 00:41 Hey, how's it going, Jared?
**Jared Freeze** 00:44 Bing.
Did you go, did you go home this year?
**Ted Young** 00:52 Go home?
**Jared Freeze** 00:54 Yeah, have you been back to… Oh, they…
**Ted Young** 00:56 island?
**Jared Freeze** 00:57 Yeah.
**Ted Young** 00:57 No! I want to go back, though. I need to visit my stepdad. He's still… he decided he's gonna hold on to the farm and just… just stay there.
He was originally trying to sell it, and that was kind of gonna be, like, my last sort of connection to the Big Island, but now he's gonna stay, so I need to go visit him.
**Jared Freeze** 01:21 Nice.
**Ted Young** 01:22 Yeah.
He should sell it, that's my opinion, but he's…
**Jared Freeze** 01:26 Really?
**Ted Young** 01:27 I think so.
Running a farm's a lot of work.
And… not to get totally in the weeds, but, you know, it's all leasehold land with Bishop Estates. I don't know if you… I don't know why you would know any of those kinds of.
**Jared Freeze** 01:42 I know a little bit.
**Ted Young** 01:43 But, like, Bishop Estates is kind of a crazy entity to have to deal with, and… those… they turn those leases into, like, agricultural contracts, basically, so that you're sort of like business partners with Bishop Estates.
**Jared Freeze** 01:56 Plastic.
**Ted Young** 01:57 Yeah.
**Jared Freeze** 02:12 Yeah, thanks, everybody, already, for all the SDK work. It's cool, it's nice to see so many comments.
**Ted Young** 02:20 Yes.
**Jared Freeze** 03:12 Okay.
Then 33.
Ridiculous.
Cool. So, David, it looks like you had a link to… Utils.
**David Luna Bistuer** 03:27 Yeah, I'll try to keep it short. First, a heads up, on some PR that, Trent is doing on the… on the JavaScript repository.
the… as I think I mentioned a couple of weeks ago, there's this intention of having a single SDK trace.
package, which works on both sides, on a node and a browser, okay? So, we don't have any specific code for Node or for browser there.
So, the next measure will deprecate SDK3 space, SDK3 is node, SDK3 is what?
Well, that's intent, okay? So, we should make it to that.
There is some comments, there is a README file on… on this PR, explain how to do the migration, I gave some feedback on that, but if you can have a look and check that PR, not only the random file, check the OPR. Basically, it's just, removing everything that was, there was a lot of things about the environment.
You know, checking environment variables and using them for default values and so on.
So now this SDK trace… Package is just the code, the logic itself, it doesn't do any weird stuff or anything to get defaults from the environment itself.
It's cleaner, then it works for browser as well.
But still, please have a look at this PR, and if you can provide some feedback on the README, On… on how to help with the… the… The migration, then it would be good.
So… Okay, that's the first point. So, just a heads up.
Second, maybe, is just, Pitting a bit the Bosch on the SDK package.
There is a couple of comments, one from Martin and another from Jagin.
So, yeah, the first one, maybe, is a simple one. So, Martin, you asked about if we should rename this to SDK.
Yeah, I'm fine with that.
But then, maybe, kind of to keep it in sync with the instrumentation, so we have an instrumentation folder which contains browser.
Process instrumentation package, then… rename it to SDK, and then have it the browser SDK package. Does that… Does that sound good?
**Jared Freeze** 05:58 I'm not sure you need the suffix. What else would be a sibling testy case?
Good dear.
**David Luna Bistuer** 06:09 No, but… While on Node, we have SDK node. We have OpenTelemetry slash SDK node.
Which is a packet.
So we want to have a kind of a similar naming, then we might need just to… And here, what we have is, yeah… SDK, not SDK browser would be… yeah, the name and… we can name it to SDK Browser, yeah.
My browser is again, let me check…
**Jared Freeze** 06:40 Yeah, I think we could probably just dump everything out of here.
I'm not sure… we need to reserve this for now, but…
**David Luna Bistuer** 06:48 Yeah, that's because we're using exports, so we are providing a specific export for signals, for traces, for logs.
And for our… yeah, in the future, if we want to provide something else that is reshakeable, maybe we want to… an SDK, a slash SDK was kind of… Something that I tried for… for getting the… The whole is again at once, but…
**Jared Freeze** 07:15 Yeah, I guess if that's the case, I might drop this. I'll leave it as a comment.
But I might get rid of that, and then you'll have SDK here, and then traces and logs, something like that.
**David Luna Bistuer** 07:28 Okay.
**Jared Freeze** 07:30 Yeah, I'll definitely check it out in depth.
**David Luna Bistuer** 07:38 Okay, and then the other comment is from the… from here, there's a comment about processors, so… The core implementation, it says what kind of… I was following a little bit on the Node implementation, is if you provide processors, you have to provide all of them. So, the SDK, or at least the… this init function, this start function, is not going to provide something by default.
Okay, so… If you don't provide any processor.
You can, it's going to create the backspam processor with the default URL, the export URL local host, whatever.
Or you can configure the byte spam processor and the exporter. At the moment that you give a processor's array in the configuration, then that byte spam processor or batch log record processor, it's, it's gone.
Joaquin asked if… maybe it's just, we can consider to have a kind of a adding them.
So the user… Sends a list of, you know, passes a list of processors.
And then, in addition, we are at, at the end, the bytes processor of the signal.
So, that's the… that's the question. So, should we have it always? Yes, no, maybe we have an apparently answer is yes or no. I thought that maybe there is a workaround, or kind of a, yeah, an alternative, which is, okay, if you want to have, the default one… explicitly, set an exporter configuration. So set the URL.
Then you are kind of, explicitly telling that, yeah, I want my processors, but also I want to export to this URL.
The spans, or logs, or whatever.
**Jared Freeze** 09:26 Is there… is there any precedent for… oh, sorry, go ahead, Watka.
**Joaquín Díaz** 09:32 I just wanted to clarify my thinking here. I think the SDK show… Like, when you start it, like, the first time you use it, it should be… almost ready to work. Like, all you need to do is set up your all, and that's it, or some, like, really small settings.
And then as you go deeper into what you want to customize, it should also be, like.
not as hard to customize something. That is why I thought you maybe heard of, like, my thinking was… No, no, I want some simple processor, but then if I do that, I also have to start creating my own batch processor for spans and logs.
so, yeah, and given that, I guess, most people will use that as a default.
If we've gotten… If you have some way of avoiding them having to do that work, it would be easier for them.
**Jared Freeze** 10:31 Yeah, I was gonna say, you know, I think, you know, it's definitely attractive to just… like, have a lot of options and docs to go with it and things like that. But it may be even easier To just have a new entry point.
That would be, like, start simple SDK, something like that, where it's immediately obvious you know, what the function name is to get started, and it only takes a URL, or a very small config object, or something like that, at the helper level, instead of having, like, all this config that forks internally.
Maybe an option. I don't know if Node uses anything like the word simple.
You know, like, like, simple processes or something like that.
Maybe we could consider that, so that way it's not all… you know, driven by, like, like I said, config. Like, oh, I have, you know, 10 keys to sort of do what I need here, but if I don't provide that, I get defaults. It's like, you know, giving people less, sort of, buttons, but like, oh, when I set it up, like, it was going to the console, and now it's not, you know, and I'm not sure why. It's because they added one processor, why did it delete two others, you know, or something like that.
I'm typically a fan of just different top levels, so that way… It's really clear what's happening, I can definitely propose that in code.
Let's see how it looks.
But there's thought.
**Joaquín Díaz** 11:59 Wouldn't… having something that is called, like, Star Simple… Be just the default of… not sending any configuration to the start SDK, but only the required ones.
It's some, like, it's like doing an alias of the same function without any configuration, basically.
Isn't that implicit that you are doing it simple by not setting any configuration?
**Jared Freeze** 12:26 Yeah, I think the idea would be… Yeah, I mean, yes, you could, but I guess the idea would be that you're strictly limited. Like, if you do start simple, like, there's no… array that you could add things to. Like, you couldn't add processors. Like, if it's simple, it's simple, right? Something like that. That would not be extensible. Whereas the other one, it's very clear, like, you're starting with you know, empty things. You know, you need to add what you need, or something like that.
Might not be a great idea.
Something I was thinking of.
**Joaquín Díaz** 13:02 I agree on the concept of being simple, but I don't think it's worth having two separate entry points, because Like, as soon as you see simple working, and you want to do something, then you want to… you have to switch back to non-simple.
And then it's, like, more work for them to customize settings.
Like, given that… All the configuration keys are optional, then you don't even have to… Like, have an empty list of processors or whatever, it's just you don't use them.
**Jared Freeze** 13:35 Yeah, I think maybe, too, yeah, I mean, I agree with that also. I think just good logging would really help here.
So, like, when you're in debug mode, it spits out, like, your config, like, you know, everything you passed it, you know, things like that. Maybe just the feedback loop is all you need. So that way, you know, the first time you start it, it's like, hey, here's… everything that's happening under the hood, you don't have to guess, you don't have to go to docs, you know, it's all in the TypeScript, and then also being mirrored back to you.
I just, you know, as easy as we can, right, to get started, so… In our examples, if we're just like, hey, start with debug as your log level, you know, and then you get everything you need. Hopefully, you can just tell the story that way, so that way it's just easier to onboard.
That's… that's my goal. Not necessarily… I don't… I'm not saying we need to have something that's sports, right?
**Joaquín Díaz** 14:27 Yeah, thanks, Hustle.
Maybe for, for some users, seeing the logs and response in the console, like, using the console exporter is also useful.
at least it was useful for me when I started, because otherwise it's like.
well, I don't have a collector, I just want to know what is this thing creating, and then you see the spans on the logs, and then after that, maybe it makes sense to you, and then you want to send them somewhere.
But again, like, I think the question here is whether How hard we are on the defaults, like… Are we going to force… people to use the batch processors, unless they say otherwise, or… Are we, like, dumb in a way that you either… if you send us all the processor, or if you send us any processor, we just use that list, and that's it, and we don't make any decisions for you.
**Jared Freeze** 15:29 Yeah, I mean, I guess that's what I was kind of getting at, is like… If there's two, and it looks empty, and then you add 1, and now the list is 1 and not three… You know, is that intuitive?
But… Yeah, we can try it out. That reminded me of something else, which is, so in our vendor SDK, we have an API server that's not… a real collector. Literally all it does is just mirror whatever you just gave it, so that way you can use multiple endpoints, but one of those can just be this debugger that doesn't run in Docker, that isn't, like, the full container that's running.
I don't know if that might be useful, or if the container… or… Martin, I think you're the one that's added added that, right? Or you have that on a branch, where there's something running that's, like, a local collector?
**Martin Kuba** 16:21 Oh, I think Joaquin did that.
**Jared Freeze** 16:23 Oh, okay. Yeah.
**Joaquín Díaz** 16:25 Yeah, it's, yeah, but that's the whole thing, it's different from what we have on Embrace.
On Facebook Hub.
Basically, an old server that logs.
It, spans and logs, like, into the console.
So we use that locally for debugging, like.
Yeah, what happens when we send something to the collector, how it looks like?
And what I did was an actual… Refine a collector that shows the autumn response.
Alongside Tempo and other stuff.
Yeah, I guess… it can be useful.
But also, I mean, it's the same as useful as a console exporter, maybe. I know, I think they are useful.
Different things, I guess.
**Jared Freeze** 17:11 Yeah, definitely. Just making sure, like, that the onboarding's super smooth, that's all. That's my feedback.
**Joaquín Díaz** 17:17 Yeah.
**Jared Freeze** 17:17 I think the best.
**Joaquín Díaz** 17:21 Yeah, definitely everything helps. But then, like.
back to the question, I… I don't know if there are other opinions on… on the defaults, or how smart the SDK should be.
**Martin Kuba** 17:37 Yeah, I'm all for making it as simple as possible, but I think, like, that's what we're trying to accomplish with this, with partially, with this configuration, because… The configuration with the existing components from JS is so complex.
I, I think, I think maybe, and I think that's probably, like, the most important thing in this PR that I think we need to get right, is, like, get the API config right.
So I wonder if he can… if he should just, like, Took some time.
To, like, go through this and test it out, and then next week, maybe, like, look at Look at, like, the… the options, like, and actually, like, compare and see… make a decision.
**Jared Freeze** 18:30 Cool. Yeah, I'll definitely review, try to run this.
Locally, and see what we get.
Really?
Cool. Joaquin?
**Joaquín Díaz** 18:48 Yep, looks like the only open question for the fetch instrumentation migration is what do we want to do with resource timing?
Honestly, I go back and forth with the answer, I think.
Like, I agree that, instrumentation shouldn't be doing more than one thing, so in this case, fetch is doing spans for requests, and then we have a resource-time instrumentation doing the logs.
But I'm also worried about losing the context within the two of them, given that Kernie as far as I am aware, there is no way of connecting the spans created by the patch instrumentation with the logs created by the resource assignment instrumentation.
So, we will… That responsibility will fall into the user and in the collector, if they can't do something, or if they need to manually Connect them to the… So, yeah, I'm opening up a question for the rest, because honestly, I don't know, like… I think they will have pros and cons, but I don't know.
**Martin Kuba** 19:55 Right.
That's a sh…
**Santosh** 20:00 Yeah, okay. My preference is to have one instrumentation for the fetch as a single concern.
to emit both the span and the, you know, the event separately. But one instrumentation. That way.
I have both… I capture… with the same instrumentation, I capture both the, you know, the span, and then the… the corresponding timing information as a… As an event.
Maybe have options to… Aww.
Enable, disable the timing.
**Martin Kuba** 20:43 My… my concern is, like, there's… there would be a duplication of, of… Of, like, this emitting the same kind of events from two different instrumentations.
So I think we're just, like, shifting the concern from, like, Yeah, like, instead of, like, maintaining, like.
some kind of mechanism that makes it possible for those two instrumentations to get context, or share context. We're now having duplicated… duplicated code into instrumentations.
Which I think creates, like, a different type of confusion for users, in my opinion.
or… Yeah.
And I think, like, now that we have… we have a single package for all instrumentations, like, is that really an issue? Like, to have… to synchronize between instrumentations?
**Joaquín Díaz** 21:43 I think it's something worth exploring, I don't know if there's… presses, soft… instrumentation being coupled together, in a way.
Maybe not that much. I mean, it's not that one is reading the other. It's just they're sharing context.
I think it's… Yeah, I think it's worth doing, or trying to do something to… Big study that way.
Sorry, Tantashi, for you, like, you… prefer that approach, because you will want to have them tied together, like, the context being the same for them? Or is there any other reason to it being the single instrumentation?
**Santosh** 22:27 Well, I didn't realize, you know, they were part of a single package now, so you would… the moment you include the package, you would get both.
I'm not up to date, but… Depending on how the… You know, instrumentations are, configured.
if I need… To configure these two concerns separately, that's an additional you know, step. So, all concerns related to Fetch, you know, it would be… Easier if I configure them once.
But, you know, based on what's the right fit, you know, we, the instrumentation, could emit you know, the span and the event separately. I don't see a problem with… You know, one instrumentation emitting, you know, both the span and the event.
Simultaneously.
**Joaquín Díaz** 23:25 Hmm.
Yeah, I guess… so the two problems we have is… Context and configuration being shared using this instrumentation, and how we can solve that.
**Martin Kuba** 23:38 So my concern here is, like, the opposite, Santosh. Like, if you have… If you have a user start with just a fetch instrumentation, and they configure it to send both spans and… And… and events.
And then later on, they maybe want to include the resource timing, because they want to capture additional. Now you have to, like, configure which instrumentation, like.
Filters which events so that you don't duplicate, or you have to, like, turn off the one in one instrumentation, in the fetch instrumentation. So now you have complexity of, like.
**Santosh** 24:17 Where is the second one coming from? Where is the duplication you're talking about?
**Martin Kuba** 24:21 Resource timing?
**Santosh** 24:24 Right, right. So the resource timing, I'm suggesting that we include it as part of the same fetch instrumentation.
**Joaquín Díaz** 24:31 Yeah, bud.
**Santosh** 24:32 feasible?
**Joaquín Díaz** 24:33 we have a separate resource, so there is a resource timing instrumentation that just reads a resource timing as its own thing. Correct.
**Santosh** 24:42 we started.
**Joaquín Díaz** 24:43 I won't…
**Santosh** 24:44 Yeah, yeah, yeah, we started with that approach, but, you know, at that point, we didn't have any instrumentation, you know, generating spans, but now that we are… moving, the fetch and XHR instrumentations from the other repo into this repo, into the new browser repo. I… you know, one option is to you know, merge the concerns into a single instrumentation. I'm just throwing an option, but… Oh.
**Martin Kuba** 25:18 Now, what if I wanted to just generate just the events, but not spans?
Like, it would just, like, be an OAP.
Like, I… like, I don't include, tracing SDK, so it would be an OAP in that instrumentation.
**Santosh** 25:36 I think it has to go back to the agenda of this, This whole initiative, right? I think it was meant for, open, like, browser… Troubleshooting?
In that case, you know, won't… are there situations we anticipate where people only want Research timing, but not the… press… Telemetry.
**Jared Freeze** 26:12 Well, because fetch monkey patches, there will be people that don't want that.
They potentially do not want to be digging into APIs, and they just say, whatever the browser gives me, I'll take it.
You know?
I think it's possible, I don't think it's gonna be common. They do answer different questions, right? Because resource timing has images in it and fetch does not, so… It's not exactly the same question, there's a ton of overlap.
So…
**Santosh** 26:45 Yeah, yeah, I mean, theoretically, it's possible, but I think… It also makes our, in a design complex.
So maybe… if we… can think of… Situations where our software is going to be used, and If we can… Narrow down a subset which we want to support, rather than keeping it all open.
In case it helps simplify our technical design, that may be considered as well.
**Martin Kuba** 27:23 Yeah, Sandosh, I guess my counter-argument was that it's not gonna be any more complex than… then… Having two separate instrumentations in the same package.
**Santosh** 27:35 Yeah, that, that is, yeah.
Yeah, I think that approach is fine, too. I just, initially, when I… started, I, I didn't remember that… There's only one package now.
It's still better, Compared to having two packages, but still, the two instrumentations need to be configured separately, though, you know, when you set up the SDK.
**Martin Kuba** 28:02 That's true, but I think it's…
**Santosh** 28:05 That's a relatively smaller concern, yeah.
**Martin Kuba** 28:11 Yeah, I mean, and the trade-off is, like, do we want to have… Have users, like, direct them to configuring two different instrumentations, or add complexity if they want to.
Like, switch later on.
**Santosh** 28:27 Yeah, I think we can… we can stick with your approach, Martin. I think, also remember that the fetch and XHR Will be to independent instrumentation, and the resource timing is common.
**Joaquín Díaz** 28:40 Yep.
that currently is… Share using, like, helper functions, but it's the same thing, basically, what it's doing.
**Santosh** 28:51 So keeping them as separate instrument… three separate instrumentations, but in the same package, and having, you know, interdependencies between the instrumentation is fine. They are anyway part of the same package.
**Joaquín Díaz** 29:03 Yeah, I mean, there is always CS if we go forward with this SDK.
The configuration can be simplified by having one key on the configuration when you need the SDK. That applies to all Like, the three instrumentations.
**Jared Freeze** 29:21 Yeah, that's what I was thinking, is there's something like network config?
Or just network.
that, you know, I'm not sure where the logic for deduplicating between resource timing and fetch would live.
Like, that's what I was just thinking about.
I might be off-base, but… If you do want to deduplicate, I mean, I guess they're matching timestamps and stuff.
I'm not… I'm not sure where that would live.
**Joaquín Díaz** 29:46 You don't need to deduplicate if the instrumentation is separated. There is only one resource standard instrumentation.
The only thing you're missing is context.
**Jared Freeze** 30:09 Cool. Anything else?
**Joaquín Díaz** 30:16 I'll, like, I'll try to think something for next week on how we can share context with the instrumentation, because… I think that's a problem that we talked about many times on the browser side, like, the lack of context sharing.
So maybe… maybe we need something else.
yeah, something that… go through the instrumentations and helping connect context with it, I don't know.
**Jared Freeze** 30:49 Cool, that sounds good.
Okay, we're out of time. I'll see you guys next week.
**David Luna Bistuer** 30:56 My bet.
