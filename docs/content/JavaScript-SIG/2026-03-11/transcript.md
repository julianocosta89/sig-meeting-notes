SIG: JavaScript SIG
Date: 2026-03-11
Duration: 59 minutes
Zoom Recording URL: https://zoom.us/rec/share/RBTVTDVjwLw61F31PlVgXFTk8V97AY0h-gzq7LDwReyXHUxNneMCnIYfd76GKkzC.IYBYVUZh2_m6nT0W
============================================================

## Zoom Recording Transcript

**Trent Mick** 00:39 Damn.
**Hector Hernandez** 00:42 Hello?
**Marc Pichler (Dynatrace)** 01:44 I didn't…
**Trent Mick** 01:46 Hey.
**Hector Hernandez** 01:47 Hello.
**Trent Mick** 01:49 Jack Berg here for about half a second, and then he ran away, realizing it was JavaScript.
Acha.
I have no idea why he left, but… external click.
boy, next to.
Wrong link in a big table or something.
I think we'll wait a minute or two.
**Marc Pichler (Dynatrace)** 02:19 I'll also, put a note in the AutoJS channel, letting people know that… Following… That's the time zone difference.
**Trent Mick** 02:32 Oh, yeah.
**Marc Pichler (Dynatrace)** 02:32 For two weeks, that'll be different.
**Trent Mick** 02:34 Weird.
**Marc Pichler (Dynatrace)** 02:35 Yeah.
**Trent Mick** 03:52 Okay, why wait? Might as well get started.
Small group.
That's cool.
Let me share.
Yeah, as ever, feel free to add topics, everyone. I will monopolize a little bit, so… this… I noticed, Oh man, I think it's last week now, but I haven't had a chance to come back to it. So… The tab tests for instrumentation SQLized, I noticed, were failing. We run the full test all versions, that's what TAB is, tests every week.
And I just happened to go look at that job, and it was failing.
only failing in CI.
And I didn't know why. I did manage to reproduce it locally when I do what CI is doing, which is use Node 18 to build everything.
and then use Node… I can't remember if it was 24, but one of the other versions to, yeah, 24 to run the things. Something is different. I haven't had enough… time to go back and to see what was different, because then I tried to, like, oh, well, obviously it's going to be this, so I tried to make some change, and then I couldn't reproduce it anymore, so… I, like, had to build the entire tree with Node 18.
reproducing exactly what CI was doing, I was able to get it to fail, but I have to go back to that, so anyway. If anyone wants to pick that up.
Feel free.
I have to go look to see, naively, if I could find a difference in the node modules Trees that are built.
Or in the builds that are… but I can't imagine… I don't know what the difference is yet. I don't have any good ideas on that one, but interesting.
And then also, I think I had a small PR… Let's see if I can find it.
The reason we didn't notice this on other PRs, for example, when we're updating the hotel depths, is that the Component label map is out of date, and it wasn't adding a package.
label for the SQLized instrumentation.
So it didn't… when we run tab tests on both things, it didn't actually run tab tests on that package.
And… I think… oh yeah, so here I had a… PR, if someone's able to review that.
That's a point that updates the component label map and also adds a script to regenerate it.
appropriately. I think some of the… It does sorting here, so it's kind of hard to see, but there were a few packages where we didn't have the component label map.
Stuff going.
Great.
So, let's say… On that one.
And then… This PR is still in draft, so… But, NRAG has been working through the… spec for basically self-metrics, so OTEL SDK metrics on various things.
Which… Is in still development status, so… what we've been doing on previous PRs for this is having opt-in.
For these, but it's so that the hotel SDK can provide metrics on itself.
There are a lot of them, so he's been working through in smaller chunks and doing things, but this one… is on… Metrics on the exporters, which gets really big, because we have, like, a thousand exporters in the system.
If you get a chance, Mark, I'd appreciate your looking at it, because he asked for some early review in draft, because it gets kind of gross.
Right now, the thing that makes me cry about this one is, the exporter metrics got added to Core and exported on the existing export of an internal thing in Core, which makes me cry that Core has a… dumping ground internal thing that has stuff that is used by exporters, because that was the only… I'm guessing the reason is because that was the only place to share stuff amongst all exporters, because not all exporters are OTLP exporters. There's an OTLP exporter base package, but that doesn't apply to the Zipkin and Jager exporters.
So they don't share or depend on that one.
So… As a part of that, Go ahead.
**Marc Pichler (Dynatrace)** 08:41 Isn't this internal export thing intended for… the SDKs… I seem to remember that this was used in the processors somehow.
So… I think the export thing is… it just wraps the card to export.
Toolset. Yeah, the only thing it…
**Trent Mick** 09:11 Yes. Yeah.
Yeah, the, suppressed tracing slide, right?
Okay Okay, so maybe I'm wrong about this one, but this one, I feel like, and I'll… I asked NREG, but we'll see, that it felt like core was the only shared dependency amongst all of the exporters.
So, an indirect question I have there is.
Do we need to maintain this Jaeger and Zipkin exporters anymore? There was a blog post in November about the Zipkin exporter being deprecated, and I don't know what the status of Jaeger is.
**Daniel Dyla (Dynatrace)** 09:48 Jaeger…
**Carlos Alberto Cortez** 09:49 I think?
**Marc Pichler (Dynatrace)** 09:50 Jaeger uses OTLP.
**Trent Mick** 09:54 Right, they both support it now, right? In newer… recent versions, at least.
**Daniel Dyla (Dynatrace)** 09:58 Well, I don't know about Zipkin, I just know that I know Jaeger has for a while, and they actually deprecated their own format.
**Carlos Alberto Cortez** 10:07 Yeah, I went into Florida.
Yeah, I want to confirm that. Both of them are deprecated.
**Trent Mick** 10:13 Yeah. Okay.
**Daniel Dyla (Dynatrace)** 10:14 So I don't think we really need to maintain either of them.
**Trent Mick** 10:18 Okay, so we definitely don't need to add features like these SDK metrics to them.
**Daniel Dyla (Dynatrace)** 10:22 No.
**Trent Mick** 10:22 Okay, so maybe, maybe that simplifies then, so the sharing of how to… sharing of some of the logic, that one class that I was pointing to, sharing some of the logic on generating these metrics that are related to exporters. They could be shared in the OTLP exporter base, then, rather than something else that Jaeger and Zookin can latch onto.
**Daniel Dyla (Dynatrace)** 10:42 This is not the first time I've had this thought, probably not even the first time I've verbalized it, but that core package, just its existence, has been a thorn in my side for, like, 5 years now.
I really want to remove it.
**Trent Mick** 10:58 I was channeling you there when I just, in the comment on that draft thing, talked… called it a dumping ground. So, yeah, yeah, I remember you mentioning it, so you have publicly mentioned that before.
**Daniel Dyla (Dynatrace)** 11:08 There's a couple of things that it does that are shared in a lot of places, but I think… splitting that, like, the time handling code, I think we could have a time package that does that. You know, I don't think there's any reason to have that all in some poorly named… Core package.
**Marc Pichler (Dynatrace)** 11:28 Yeah, there's also a lot of stuff that we just used twice, and it would be totally fine to just duplicate it, because it's so simple.
**Daniel Dyla (Dynatrace)** 11:36 Yeah.
I would personally deprecate, like.
split this stuff out and deprecate it. There's, like, a couple of things that it does related to context.
That I think could be moved into… you know, a context package. There's a lot of time stuff. It's almost all time conversions. That's, like, the bulk of the code.
**Trent Mick** 11:59 These end things, but… yeah.
**Daniel Dyla (Dynatrace)** 12:04 Yeah, environment things, propagators, like, the built-in propagators are in here for some reason. Like, they're… it's… it's a dumping ground. Like, I… If people are willing to… commit to it, I would be willing to start actually working on splitting all this stuff out and deprecating it.
**Trent Mick** 12:27 Okay, I mean, sure, that wasn't my goal from this thing, but yeah.
**Daniel Dyla (Dynatrace)** 12:30 I know it wasn't. Understood.
**Trent Mick** 12:31 Yeah, yeah, yeah.
**Daniel Dyla (Dynatrace)** 12:34 Yeah.
**Trent Mick** 12:35 It would take a while to excise all of this stuff. I think most of this feels like he could find a natural place, but… don't know.
**Daniel Dyla (Dynatrace)** 12:42 I don't think we need to add features to Zipkin or Jaeger. We do have Prometheus as a non-OTLP exporter that we do need to still worry about.
**Trent Mick** 12:53 Oh, let me go look at… this thing… I can't remember if his draft PR was covering Prometheus, or maybe it's not.
Okay, noted. I'll take a look. I have to go back and look at the PR.
**Marc Pichler (Dynatrace)** 13:13 Is it…
**Trent Mick** 13:14 Okay.
**Marc Pichler (Dynatrace)** 13:14 Is it common that these metrics are all implemented in the exporters?
I'm not sure if you've seen that happen in other SDKs, too. I've just been looking through the list of, Which metrics exist here, and it seems like all of these could get recorded on the processor as well.
**Trent Mick** 13:39 There are a number of processor ones.
that he…
**Marc Pichler (Dynatrace)** 13:41 It's been.
**Trent Mick** 13:42 Implementing on processors.
Excellent.
**Daniel Dyla (Dynatrace)** 13:47 Sounds like he's implementing it, you know, on the component that is actually, like, the closest component, I guess, for lack of a better word.
**Marc Pichler (Dynatrace)** 13:59 Yeah, because one of the things that I'm thinking of is usually you have one final, Processor component that you use to export.
your things. So if all of these implement these metrics, then… Not every… every exporter needs to do it.
And you have that information, right? Because if you hand it off to an exporter.
Then you know how many spans are in flight, because the exporter will either report that the export is… Succeeded or failed.
And you will know, which ones are exported, because after it's succeeded, if you keep track of, like, how many you passed in.
You will know, how many you exported, so you might be able to… Do it on the processor instead of the exporter, but still record exporter metrics.
**Trent Mick** 14:58 I don't know if this… expected attribute on those metrics means that you want to be… like, the intent was that they're actually done on the exporters.
**Marc Pichler (Dynatrace)** 15:11 Right, yeah.
**Trent Mick** 15:12 One design thing he did mention is that he found the code was smaller in the Java side, because he was able to instrument this internal transport object, which… similar to our transport, but he said the retry transport, wrapping the transport that's passed in made that… felt like he couldn't do it in the current JS implementation.
**Marc Pichler (Dynatrace)** 15:31 Anyway, that's maybe a bit too deep. Yeah, if you wanted… if you had a chance to look at the PR.
**Trent Mick** 15:36 Your opinions would be welcome there.
So I think you know the exporters way better.
I was looking for an hour, and then I just wanted to blow everything up and just rewrite… have two exporters.
We would have the node exporter package, which had all of them, and the browser ones, which only supported JSON or whatever, and was specific to them. Yeah, that's…
**Marc Pichler (Dynatrace)** 15:54 I think that's what we're going towards anyway, having a single exporter package, because it being split by signer and then being split by transport is… is a lot, and there's a lot of just… stuff sitting around, and since the OTRP transformer package depends on all the SDKs anyway, we might as well just Combine everything.
So I think that would make sense. And also, there's, the… the browser, browser exporters, they have a slightly different public API than the Node.js ones.
And it just… is… Impossible to do with the types that we're shipping. So, There's some pain point there as well, still.
Combining everything into one makes things a lot easier.
**Trent Mick** 16:58 Okay.
Okay, I wasn't crazy then.
Cool.
Okay, done.
Carlos.
**Carlos Alberto Cortez** 17:11 Yeah, just for your information, we were talking about this one last week, I think, about the always record, sampler, and because there's a PR, Open somewhere, and yeah, basically, we, This has been in the specification as in development since December… early December, so hopefully we can get some approvals there, so it's easier for us to merge that. As you can see, Java, Go, and PHP, they already merged that, although it was merged as experimental in their respective repos.
Oh yeah, I just figured information, yeah.
That's all.
**Trent Mick** 17:57 Okay, I haven't taken a look. I don't know if any of the other guys have.
Or anyone else?
**Marc Pichler (Dynatrace)** 18:03 I was meaning to, but didn't find the time yet. It's a very simple component, so… Yeah, correct. We should be able to merge it soon.
**Daniel Dyla (Dynatrace)** 18:11 13 files changed, but 13 of them are boilerplate for creating a new package.
**Marc Pichler (Dynatrace)** 18:16 Yep.
**Trent Mick** 18:18 David did have a comment in the reviews asking, would this fit in the SDK trace in an existing package, or do you want a separate one for this?
**Daniel Dyla (Dynatrace)** 18:25 There's the…
**Trent Mick** 18:27 Experimental nut question, but… Okay.
**Marc Pichler (Dynatrace)** 18:39 Yeah, I guess… This is an experimental feature, but we could just put an experimental annotation on it and ship it from… Buh.
trace package.
**Daniel Dyla (Dynatrace)** 18:54 Especially since we, like, spec is trying to stabilize it right now. It's… it's… you don't expect changes, it's dead simple.
**Marc Pichler (Dynatrace)** 19:05 Yeah, and we've done, some experimental features like that.
already, or send a trace package, I think the last one was… the on-ending, in the span processor.
And that should also reduce the diff, quite a bit, so reviewing should be easy then.
**Trent Mick** 19:38 Okay, cool. Yeah, thanks, Carlos. One of us will try to take a look soon.
I'm trying to finish up stuff this week, and then I'm off for a week and a half, so… might not happen for me right away.
Don't help but the rest of you.
Did David make this? I was chatting with him earlier.
**David Luna Bistuer** 20:00 Yep.
**Daniel Dyla (Dynatrace)** 20:01 Yeah, he did.
**David Luna Bistuer** 20:02 at the…
**Trent Mick** 20:03 Oh, there you are. Okay. Cool.
**David Luna Bistuer** 20:05 Yeah, So, basically, one thing that I just found out on… well, I need to prepare a reproduction for that, but we have already instrumentations that are patching the same APIs, browsers, and since that's shimmer, what it does is, like, okay, that is one of the, When we are patching the same API, one of them wins over the other.
The result is, like, okay, one instrumentation is working, and the other is doing… silently is doing nothing.
Well, this is just for… to know, I will prepare that, and then maybe we can discuss an issue, but I want to know your thoughts about should we allow half double instrument… double patching on… on… on the same APIs, like, in this situation?
Or what the…
**Trent Mick** 20:50 What's the API, just for discussion, that they're both…
**David Luna Bistuer** 20:53 The API is History API. So, basically, we have user interaction, instrumentation, which is an old one, and we have a new one, which is the browser navigation. So both are trying to, know when the user is going back and forth on the history.
And, yeah, they're patching the push state, replaceState, methods.
And it seems, so I was trying to instrument an application with both instrumentations, and it seems that, well, we get… the user instrumentation wins over the other.
Maybe it's because of the order?
**Trent Mick** 21:31 Press it.
Patch history, there we go.
Okay, so it's the wrap thing that is doing unwrap first, right? And that's why it happens?
**David Luna Bistuer** 21:40 Yeah, pro results.
**Trent Mick** 21:43 So, it didn't… I think it didn't always used to do that, it's just, what?
**Marc Pichler (Dynatrace)** 21:52 still, I think it's the instrumentation-based package. This.
**Trent Mick** 21:58 RIP.
**David Luna Bistuer** 21:59 No.
**Marc Pichler (Dynatrace)** 22:00 On the instrumentation pace, it doesn't unwrap before.
list, so yeah.
**David Luna Bistuer** 22:06 That's no plans.
**Daniel Dyla (Dynatrace)** 22:09 Do we…
**David Luna Bistuer** 22:09 Yes, that's the one.
**Daniel Dyla (Dynatrace)** 22:10 I'm here.
remember why?
We're unwrapping before wrapping?
**Trent Mick** 22:16 I think it happened accidentally when the node… oh, but that was the node-specific stuff that didn't.
Didn't it?
I have to look at the history again, because when… There was a point at which we brought Wrap and unwrap.
As methods on the instrumentation class, when it used to be just import shimmer and call wrap.
Yeah.
**David Luna Bistuer** 22:40 I see what's…
**Trent Mick** 22:41 And it was… it was added when the ESM support was added to deal with proxies, something, something proxies.
this code.
And… Thank you.
**Daniel Dyla (Dynatrace)** 22:54 unwrapped.
**Trent Mick** 22:56 Say again?
**Daniel Dyla (Dynatrace)** 22:57 Can you blame real quick?
Line 64, I think.
**Trent Mick** 23:06 Let's see… Okay, well, it was done separately.
**David Luna Bistuer** 23:18 Was it Amir?
Yeah, Amira.
**Daniel Dyla (Dynatrace)** 23:25 So the instrumentations were already doing it, and he centralized it.
**Trent Mick** 23:31 Most instrumentations are already doing it, yeah.
**David Luna Bistuer** 23:34 Yeah.
**Daniel Dyla (Dynatrace)** 23:36 That still doesn't… Say why, though.
I wonder… It'd be interesting to see if you just remove it, do the tests pass. I would almost guarantee that some of the tests are relying on this behavior.
**Trent Mick** 24:03 They're probably missing.
**Daniel Dyla (Dynatrace)** 24:05 I… I personally, and again, this is… today is a day for dredging up ancient history. I think unwrap is a mistake.
It's essentially for tests only. I would not want any user to use it in production.
**Marc Pichler (Dynatrace)** 24:27 It also doesn't work with input in the middle, I think.
**Daniel Dyla (Dynatrace)** 24:33 Yeah.
**Trent Mick** 24:43 Yeah, I actually don't care to challenge that, because I also want to kill unwrapped, so…
**Daniel Dyla (Dynatrace)** 24:47 I'd be interested to see what happens if you just remove the unwrap.
And when you asked how many tests pass and how many fail?
**Marc Pichler (Dynatrace)** 24:58 I think changing it in the instrumentation phase is a bit of a tricky… Way of going about it.
I wonder if we could have…
**Trent Mick** 25:12 This is the node-specific one. Is that… is the browser side one doing it? Because we're talking the browser side.
**David Luna Bistuer** 25:18 yeah, I think not.
But maybe the behavior is… If you go there, you'll see that we are exporting shimmer as is.
So, in platform browser.
**Trent Mick** 25:34 Alright, yeah, I guess instrumentation is just using… Instrumentation abstract… Sure, I'm not looking in the browser right now.
**David Luna Bistuer** 25:46 You're looking at VS Code, maybe?
**Trent Mick** 25:48 I am, yeah, I know, I know, you're not following. It's just a straight-up shimmer wrap.
So shimmerwrap does not do it, does it?
**David Luna Bistuer** 25:58 should… I guess it should… Combine both functions, so the original is the first patch.
So, yeah, the patch function becomes the original, and then we have the second patch. But… I did just a quick test, and it wasn't working, so… My kind of question would be that if that's okay if they need to make some changes to make it work, or should we, since the browser sick.
We are focusing around instrumentations, but we are not this… well… one of the things that we have to do is also to find out which are the best APIs for instrumentations and so on.
maybe, I don't know.
**Trent Mick** 26:41 I think in controlled situations, if, like, the browser maintainers feel that it makes sense to have both of those instrumentations, and they both need to wrap the same API, that they should both be able to do so. I don't think… The instrumentation tooling should prevent that happening.
I guess the only question is whether that's a Bigfoot gun that you give to… Or if it breaks a whole bunch of existing stuff, but…
**Daniel Dyla (Dynatrace)** 27:06 Yeah, or… Maybe it should be… Yeah, I… I was gonna say, maybe it should be an option that you pass to RAP, but… Then, if it's applied inconsistently, it's probably more of a foot gun.
**Trent Mick** 27:26 I'm kind of wondering why that's not working, though.
**Daniel Dyla (Dynatrace)** 27:31 Well, Shimmer… Shimmer may…
**Trent Mick** 27:34 Well, this is the wrap code, and this is the browser-side instrumentation, it's just calling this wrap directly.
**Daniel Dyla (Dynatrace)** 27:40 Yeah.
**Trent Mick** 27:41 And it's not… Unwrapping, is it?
**David Luna Bistuer** 27:48 Unless both…
**Trent Mick** 27:51 Must that… must that do it.
**David Luna Bistuer** 27:54 Ugh.
**Trent Mick** 27:55 But I gotta jump around in this.
No, that's fine.
**Daniel Dyla (Dynatrace)** 28:04 Yeah.
**David Luna Bistuer** 28:05 I need to check.
**Trent Mick** 28:10 Yeah, I would… I'd have to dig in. Debugs.
**David Luna Bistuer** 28:13 Yeah, yeah, I'll…
**Trent Mick** 28:13 Specific example to see what's going on.
**David Luna Bistuer** 28:16 I'll create additional input here. But that's okay if the… if… so, it's okay to… to allow double grabbing on… So…
**Trent Mick** 28:25 I think so.
**David Luna Bistuer** 28:25 This is gonna…
**Trent Mick** 28:26 Yeah. And I think, arguably, I would consider backing this out to not have… Whatever I lost it in the code, but… To not have rap.
Unwrap, like, if your instrumentation really needs to unwrap, then… call unwrap.
Also, I'd love to revisit this, and why that's… Good idea.
**David Luna Bistuer** 29:02 Okay, good.
**Trent Mick** 29:02 Thank you. Okay, good.
Andre, you here?
Sorry, when I'm sharing, I can't see the… Oldest.
Okay… HP Patch Guard breaks ESM instrumentation on Lambda.
Sounds like something I was involved in. Yes.
So I change this to guard against double instrumentation, and that breaks.
You can't win.
Okay, I guess I'll have to take a look at this.
ESN proxy.
Yeah, land is fun. I've talked.
Unless someone else wants to.
Excited to take this.
Triple importing of HTTP from Lambda, pretty exciting.
No takers, Ken.
Got on my list, take a look at.
Great. Triage.
Oh, that's one. Okay, so now I'll take a look.
Anyone here use Connex?
**Daniel Dyla (Dynatrace)** 31:50 Nope.
**Trent Mick** 31:59 Okay, I mean, sounds like a buck, right?
This gives you… is that P2? You just know them?
Okay.
Incorrect telemetry, yeah. Okay.
And should I stay up for grabs?
**Daniel Dyla (Dynatrace)** 32:19 Yeah.
**Trent Mick** 32:21 Sweet.
I haven't used it a whole bunch, but I've had a little bit of luck with creating an issue, not for grabs, and some people picked them up, so… Maybe someone will.
Okay, cool.
Wait a second, this is the one that we've had sticking around for a while, right?
Okay, so we're still waiting for needs author response. He said he was gonna come back, right?
He or she, I don't, care.
Okay, so, great. I'm still waiting for a response.
**Marc Pichler (Dynatrace)** 33:14 And one thing that I just noticed, has anybody seen… The problem with approvers from… Approvals not counting towards…
**Trent Mick** 33:31 Being able to merge?
**Marc Pichler (Dynatrace)** 33:33 Yeah.
**Trent Mick** 33:35 I did.
**Marc Pichler (Dynatrace)** 33:35 Justice.
**Trent Mick** 33:36 Didn't… Marillia had a question. I thought there was an issue last… because she posted… in JSDev, saying that she'd approved two PRs, but couldn't merge them.
Was the intent not that it can be merged after an approver is?
Or does the maintainer still need to… Click the button or something, I don't.
**Marc Pichler (Dynatrace)** 33:55 Usually, it should work. So I just, saw this PR here. I'm just gonna put it on the agenda really quick.
**Hector Hernandez** 34:03 Yeah, that is happening to me.
Looks like it.
You're not component owner or maintainer, you cannot merge anything in Contrape.
**Trent Mick** 34:14 Oh, okay, contribute to your example. Marilla had posted two examples from The core repo.
So, for example, Maria has approved this one.
Because… If I can merch it, can someone else?
**Daniel Dyla (Dynatrace)** 34:29 Well, you're a maintainer, so, like, you.
**Trent Mick** 34:31 Yeah, yeah, no, I can, for sure, yeah, I'm just… I don't know if, Hector, can you…
**Hector Hernandez** 34:35 I can try now, give me a second.
**Trent Mick** 34:37 Yeah, 6435.
I put in chat.
**Marc Pichler (Dynatrace)** 34:43 One in Contrip is actually approved by both, Jackson and… Hector.
**Trent Mick** 34:52 I don't know.
**Marc Pichler (Dynatrace)** 34:52 And yesterday, I just wanted to merge it real quick, and apparently I just enabled auto-merge.
But it was supposed to be merged.
**Hector Hernandez** 35:04 I can merge.
**Trent Mick** 35:04 It's waiting…
**Hector Hernandez** 35:05 435.
**Trent Mick** 35:07 Oh, so you do have the ability to do it, okay.
Okay, so that's, I think, as we expected.
So that's good. Here is Contrib Repo.
**Hector Hernandez** 35:19 Yeah, this one I cannot merge.
**Trent Mick** 35:24 This one has auto-merge, what's it waiting for?
**Daniel Dyla (Dynatrace)** 35:28 It's waiting for a maintainer approval.
If the code owner, like, if you go to a PR that's not been approved by anyone.
you'll see that there's, like, multiple teams on the… I've seen this in the past with auto-merge in other repos.
**Trent Mick** 35:48 This one only requires… okay, because this one has a code owner, so you were… you want…
**Marc Pichler (Dynatrace)** 35:56 Maybe something went wrong with the code owner's file.
**Daniel Dyla (Dynatrace)** 35:59 Yeah, that wasn't what I expected to see.
**Trent Mick** 36:03 So… Connects… this one… Is it provers…
**Daniel Dyla (Dynatrace)** 36:12 Inners get added to the other one, then?
**Trent Mick** 36:14 Yeah, what was the other one now?
This one.
**Daniel Dyla (Dynatrace)** 36:22 Because it definitely says maintainers there. What added it? In the…
**Trent Mick** 36:27 Request, requested a review, specifically.
**Daniel Dyla (Dynatrace)** 36:30 their review.
**Trent Mick** 36:31 That's why.
**Daniel Dyla (Dynatrace)** 36:33 Complain yourself.
**Trent Mick** 36:40 How to make it harder on yourself to get code in.
**Daniel Dyla (Dynatrace)** 36:42 Yeah, so I think… If you just click approve, it will get merged.
**Trent Mick** 36:51 Okay, I'll let you do that, Mark. Yeah.
Add initial skeleton for link chain.
Anyway.
If…
**Marc Pichler (Dynatrace)** 37:06 Yeah, I was about to just do the… I was about to trust to the… I will trust the true… to approve us, to, have had a look and merge it in, but now I have to have a look myself.
**Trent Mick** 37:21 Yeah, yeah, yeah, I know, right?
**Marc Pichler (Dynatrace)** 37:22 Because you're… Because I'm the one approving, so… I'm just gonna take a quick look. But I imagine we can continue with the other stuff.
**Trent Mick** 37:32 I had thought Langshan… I guess they have a whole bunch of packages under that, at Langshan.
Org, NPMorg, do that? But I thought it… I didn't think they had the top-level one, but… Mystery solved.
Thanks.
Core has more PRs, so we looked at that last week.
This will carry on forever.
Though Hector is here, do we want to discuss this more?
**Hector Hernandez** 38:08 Is this something that we want to include? Like, I mentioned before to Trent, I added this, like, years ago, because there was some issue, but that we fixed immediately in Azure's monitor site. So, this was just… replicate that kind of issue upstream.
in the correct way at that moment. So, I don't know if we really want to have this proxy, Meter providers, and instruments, and that kind of stuff.
**Marc Pichler (Dynatrace)** 38:37 I think it's fairly… complex to do, and I haven't seen a lot of issues mentioning that recently.
I'd be fine not adding it, but… I don't know, Dan, you wanted to say something as well.
**Daniel Dyla (Dynatrace)** 38:54 Yeah, I was gonna say the proxy stuff handles, like, a real problem with load order, with instrumentations, but… it is a nightmare of complexity. It adds a lot of code. We haven't had problems or bugs related to it, which is shocking to me.
Since I wrote the initial implementation in, like, one day, 5 years ago.
And it seems to work, but I… I don't like it, but it's been…
**Trent Mick** 39:28 Initial implementation of which?
**Daniel Dyla (Dynatrace)** 39:31 A tracing, proxy tracer?
Proxy tracer provider, proxy tracer.
**Trent Mick** 39:39 Yeah, yeah, I know what you mean. Okay, so for tracing, though. No.
**Daniel Dyla (Dynatrace)** 39:42 Yeah, metrics is even more complex, which is why we haven't done it yet, because nobody's complained.
**Trent Mick** 39:47 Yeah, two levels, but I think people notice Missing metrics less than they will missing spans, so… It's less… it's less surprising to me than no one's complained, even if there have been issues, potentially, but… Yeah.
there's a part of me, like, I was coming, I wanted to… Redo instrumentations as well, but… I was playing around, and if you move this, there was a PR, like, 4 years ago that specifically moved register instrumentations to be before all of the providers are registered, in the SDK usage, at least.
**Daniel Dyla (Dynatrace)** 40:23 If you move this.
**Trent Mick** 40:24 Register instrumentations down, or there's some complexity about when instrumentations get enabled.
That kind of stuff, but if you move that down to the bottom after all the providers have been registered, I kind of wonder if we don't need the proxies at all. It's a hard, kind of.
jump to make, because people doing SDK stuff on their own will all of a sudden find it more difficult, because they'll be more strict about order of things, so… I don't know.
But there's a part of me that wants to kill it.
**Daniel Dyla (Dynatrace)** 40:56 Yeah. You know what else?
fixes or alleviates the load ordering problem is the API POC that I made. Completely does away with all the proxy stuff.
It works way more reliably.
**Trent Mick** 41:12 Yep.
Yeah, that's true.
Okay, food for thought.
It's easy to go off intangency.
**Hector Hernandez** 41:24 Yeah, I think I'm going to close this one then, so we can take a different kind of approach, and if this becomes, like, a real big deal, we can just talk about it.
**Trent Mick** 41:34 can… Yeah, we can always reopen it, if we… I think we want it back. Okay, thanks.
Draft…
**Hector Hernandez** 41:47 I have also a question for Lux.
I also have this PR for years. Is there a board of what we're tracking for LUX stabilization? Yeah.
**Trent Mick** 41:57 There's, let's go to milestones… It is actually the focus topic right now, so… though I know people get busy focused. So, like, David, I don't know if you've had a chance to come back on this one. I had some review. I am sorry, yeah, I know you're… you're psycho-busy with all this stuff right now, so… I haven't… I don't know if there are PRs for a number of these other things waiting for reviews, but…
**Hector Hernandez** 42:23 Okay, we'll take a look.
**Marc Pichler (Dynatrace)** 42:25 There's your logger enabled.
**Trent Mick** 42:26 That's an issue, yeah. Oh, that's awaiting me, as well.
Sorry, I haven't gotten back on that one.
Yeah.
**Marc Pichler (Dynatrace)** 42:42 So yeah, she's one thing…
**Trent Mick** 42:44 It's the focus topic right now.
Sorry, go ahead.
**Marc Pichler (Dynatrace)** 42:48 There's one thing that I noticed, I, every once in a while, have a look at, what is implemented and what isn't, and I try to match that with the spec, and I found that we haven't implemented, scope, Attributes yet, so that's also something that we still need to do.
**Trent Mick** 43:10 So, has anyone.
**Marc Pichler (Dynatrace)** 43:11 ever.
**Trent Mick** 43:12 We're asked for scope attributes.
**Daniel Dyla (Dynatrace)** 43:15 It's funny, Carlos just left the call. He… he opened an OTEP in the spec related to… Like, context-scoped attributes.
**Trent Mick** 43:27 Oh, that's a different issue.
**Daniel Dyla (Dynatrace)** 43:30 Yeah.
**Trent Mick** 43:31 Yeah, yeah.
**Daniel Dyla (Dynatrace)** 43:33 Nobody has ever asked me about scoped attributes in any signal.
**Marc Pichler (Dynatrace)** 43:40 So, the reason, like.
**Trent Mick** 43:41 schema URL, we don't really use that.
I don't even know if we've…
**Daniel Dyla (Dynatrace)** 43:45 Somebody complained about Team URL and added support for it recently, I thought.
**Trent Mick** 43:50 Okay.
**Marc Pichler (Dynatrace)** 43:52 Yeah, it was in resources, I think. There we have the error now.
**Daniel Dyla (Dynatrace)** 44:00 I think the fact that the schema… like, the schema file and, what's the… like, the upgrader? Whatever it's… either didn't exist or was broken for a really long time. There's essentially nothing you could do with the schema, even if you had it.
There was nothing… there was no support for it anywhere.
that's changing now. There's, like, Schema 2.0 has reference implementations for… Upgrading and downgrading schema versions.
So, we'll probably see more people wanting that in the near future.
**Trent Mick** 44:36 This is a processor and a collector. Yeah. Yeah.
**Daniel Dyla (Dynatrace)** 44:40 I… actually, I think it's in Weaver, but it doesn't, yeah. Yes.
**Trent Mick** 44:45 Okay.
That was it, Mark. You did an absolute…
**Marc Pichler (Dynatrace)** 44:53 Yeah, so I guess there's no chance that we just can't, we can just keep implementing, these.
**Trent Mick** 45:02 Well, there's other stuff… there's always other stuff to do, so you can keep pushing it, but yeah.
**Marc Pichler (Dynatrace)** 45:06 Yeah, it's, if it's a feature that isn't asked for a lot.
I would actually probably prefer skipping it.
But it is a requirement in the spec, so, I guess we just have to do it.
**Daniel Dyla (Dynatrace)** 45:22 Yeah, I mean, we don't… it's kind of a gray area, a little bit of a fuzzy line, like, we don't have the authority to say, we don't like this spec feature, we're not going to implement it.
But we also have a backlog 6 miles long, and if it never gets to the front and never gets implemented, is that effectively the same?
I mean, if nobody asks for it, I think nobody will complain, you know, kind of… Tautologically there, right?
**Marc Pichler (Dynatrace)** 45:51 Yeah, the thing is that it's there in the API already, so… We may have to remove it from the API, if we…
**Daniel Dyla (Dynatrace)** 46:02 I don't think we can remove it from the API.
**Trent Mick** 46:06 We can do anything.
**Marc Pichler (Dynatrace)** 46:06 Excellent.
**Trent Mick** 46:07 experimental package.
**Marc Pichler (Dynatrace)** 46:08 just a logs API package that's…
**Daniel Dyla (Dynatrace)** 46:10 Yeah, it's, like, it's a specified feature.
**Marc Pichler (Dynatrace)** 46:15 Yeah.
It's just so… it's just so difficult to do, In an efficient way, because now that the attributes are complex attributes, you have to go through all of them, you have to compute some Form of, hash.
And then… Like, get a logger from that.
So, whoever is starting to use that is going to have, like, a huge lookup, overhead.
That's why I'm kind of…
**Daniel Dyla (Dynatrace)** 46:52 But that only happens on acquiring a logger, right? That doesn't happen.
**Trent Mick** 46:55 Yeah, it's silly.
**Marc Pichler (Dynatrace)** 46:56 Yeah.
**Trent Mick** 46:57 Shouldn't be too bad, yeah.
I… do we have that hashing code anywhere? Like, do we… do we have scope attributes on the other signals?
**Marc Pichler (Dynatrace)** 47:04 We, we don't have that, that code yet, so…
**Trent Mick** 47:12 One, one time.
**Marc Pichler (Dynatrace)** 47:13 to implement.
**Trent Mick** 47:13 But, yeah, okay.
**Marc Pichler (Dynatrace)** 47:15 Yeah, one of the problems is also, if you don't put it there, you have the overhead on serializing.
Which is where you definitely wouldn't want it, so you need to do it.
On… on obtaining a logger.
**Trent Mick** 47:30 Yep.
**Marc Pichler (Dynatrace)** 47:31 Anyway, if I have time, I will look into doing that then.
So that we can move on.
**Trent Mick** 47:41 And the rest of the backlog, too.
**Daniel Dyla (Dynatrace)** 47:42 Yeah.
**Trent Mick** 47:44 I mean, we can… we can GA this thing without scope attributes if it comes to that, right? If this is the last ticket on the thing and we want to GA, I don't know.
**Daniel Dyla (Dynatrace)** 47:53 I mean, it's not… Can you not cheat if you're missing, I must.
It's not implemented in other signals either, right?
**Trent Mick** 48:00 Yep.
**Daniel Dyla (Dynatrace)** 48:00 So I think if we do remove it from the API in order to GA and say we don't have it anywhere, and we want to implement it in all places consistently when we do, I think that that would be fair.
I don't… as far as… I don't know of any scope attributes defined in semantic conventions, or, like, I'm not aware of any use of it anywhere.
**Marc Pichler (Dynatrace)** 48:28 to whales. Agreed.
**Trent Mick** 48:29 Yeah, same in SimComp. I think it's just a wide open bucket in case… Someone thought maybe someone wants to.
Separate on attributes, sir.
Okay.
Next.
Jamie's not here, nor Marilla, don't think so, wait on that one.
Okay. I'd had a… well, a few… Y'all remember this.
I think we discussed that we want… We'd suggest that we just bump up the default depth on DER to be sufficient for the metrics case… was it Metric's case, or what was the case where…
**Marc Pichler (Dynatrace)** 49:19 Gen AI. It's deeper.
**Trent Mick** 49:21 objects.
**Marc Pichler (Dynatrace)** 49:21 Same conference.
**Trent Mick** 49:22 Okay. Yeah.
So we could go… Yeah, a bit deeper or a bunch deeper and be fine, and then either kick off another issue or a PR for the Cloudflare issue. I was… I have it on my soft backlog. If I get there, then I'll just do those PRs myself, but for now, I can just sit there, I think.
**Marc Pichler (Dynatrace)** 49:41 Come on.
**Trent Mick** 49:44 I guess we'll.
**Marc Pichler (Dynatrace)** 49:45 So, I have a policy for… controversial idea, that I want to float.
I'm not sure if we have, as the OpenTelemetry org have any way to use GitHub Copilot for some simple contributions like that?
But for stuff like that, where you're just changing a setting and stuff like that, telling it from… the GitHub UI to do it, and having it do it itself, and then reviewing that and merging that in could be… Really speeding up some of these things.
I'm wondering what you all think about… Something like that.
**Trent Mick** 50:34 Letting others go first.
**Daniel Dyla (Dynatrace)** 50:37 Seems fine. I mean… I don't know what options there even are, I've never… used Copilot through the GitHub UI before. I don't know what it can and can't do.
**Hector Hernandez** 50:49 Yeah, we use it a lot in Microsoft, and… Well, it depends on which model is being used. If you use the cheap model, it's going to cause more trouble than Salt, but if you use the expensive models, it will be really, really effective.
I think…
**Daniel Dyla (Dynatrace)** 51:06 We already get, like, Like, we have some free Copilot stuff, just because, like, OpenTelemetry.org has some… I don't know what is and is not available.
It's not… yeah. Like, I can pick Claude Opus. I don't know where… who's paying for this if I do it.
I think it's open telemetry, though.
**Trent Mick** 51:38 There was some prompt for your computer at 3 AM, three and a half months ago, that you gave your credit card.
**Daniel Dyla (Dynatrace)** 51:44 Yeah, I guarantee it wasn't my credit card.
**Trent Mick** 51:47 Okay.
Yeah, I'm not strongly opposed. I think, I mean.
Someone still has to review these things.
And I hope no one's gonna start auto-approving stuff from… Gen AI things, so…
**Hector Hernandez** 52:03 the moment you add Copilot, you need to have two approvals forced by GitHub, so it could be more trouble.
Like I said.
**Trent Mick** 52:11 But someone just putting it up, and I used Cloud to do this, or used whatever to do this, is not gonna trigger needing more reviews or anything, but…
**Daniel Dyla (Dynatrace)** 52:19 We may have to have it enabled on specific repos, because I can… I can… like, start a coding task on semantic conventions, but not on JS for some reason, so we may need.
**Marc Pichler (Dynatrace)** 52:34 Yeah, it's…
**Daniel Dyla (Dynatrace)** 52:35 ping the TC and have them enable it.
**Marc Pichler (Dynatrace)** 52:38 It is disabled right now. I've seen it sometimes review PRs.
When it was specifically requested, but I've never seen contribution generated by it.
So the main use case I see for it is, You know, these smart things where there's, like, a three-line change, and you go through the whole process of opening it in your IDE, you make the change, you commit it, you push it, you, write a PR, body, a PR title, and then… like, that takes some time, whereas if you just tell it to, like, change these lines to that, and have it open the PR on its own, might be a lot quicker and save us some time for these specific things.
I haven't used Copilot myself, I've used, Claude for these sorts of things, and It's… it's been quite helpful to just speed up these tedious tasks.
We don't have to make a decision right now, I've just been wondering what your, Even it's the worst for us.
**Daniel Dyla (Dynatrace)** 53:57 for that stuff. I think the stuff you're thinking of is, like, you know, adding something to the component owner's file, right?
**Marc Pichler (Dynatrace)** 54:04 Yeah, stuff like that.
**Daniel Dyla (Dynatrace)** 54:05 maintenance tasks.
**Marc Pichler (Dynatrace)** 54:11 And we could… I'm not sure if we can, do some permission stuff there.
But we can… Probably lock it down to just approvers or something like that.
Or people with red access to the repo.
To try running it.
**Daniel Dyla (Dynatrace)** 54:35 That is, approvers.
I'd be fine with trying it if it's… Reasonably easy to set up.
**Marc Pichler (Dynatrace)** 54:51 Then I will take a look and bring… back what I found, to the next seat meeting at some point.
**Trent Mick** 55:01 Okay.
Yada yada, same old on those.
Let's draft. We all want to rewrite instrumentations.
And then that's the one that Carlos brought up earlier.
**Marc Pichler (Dynatrace)** 55:32 Yeah, that's 300.
**Trent Mick** 55:33 assist.
**Marc Pichler (Dynatrace)** 55:33 look into that.
**Daniel Dyla (Dynatrace)** 55:35 No idea what that is.
**Marc Pichler (Dynatrace)** 55:37 it's kind of in my bucket with the PRs for the RenovateBot update.
**Trent Mick** 55:44 God. Okay.
**Daniel Dyla (Dynatrace)** 55:45 I don't even know what CLO monitor is.
**Trent Mick** 55:48 It's a CNCF thing.
But… not that that necessarily means something we have to jump to, but it's got… Some cred there, I guess.
Sorry, I should go back to what the… Description was… failed check on CLO monitor.
Okay.
And this allows… Exempts us completely?
**Daniel Dyla (Dynatrace)** 56:21 It exempt.
**Trent Mick** 56:21 It doesn't support JavaScript packages, and don't… Because we look… bad here, I guess.
No, that looks fine.
100%.
Where's the other one?
**Daniel Dyla (Dynatrace)** 56:38 100% of, whoa, what do the columns represent?
**Trent Mick** 56:43 Doesn't matter. I don't know.
Are licenses bad?
**Daniel Dyla (Dynatrace)** 56:51 recent scanning…
**Trent Mick** 56:54 Okay, whatever. If it doesn't support JS, then maybe it's got problems with…
**Marc Pichler (Dynatrace)** 57:00 I think it's because we don't have any action that specifically is for license scanning. We just use the lint step to ensure that the license header is there.
**Trent Mick** 57:13 Okay. Anyway, if… yeah.
**Daniel Dyla (Dynatrace)** 57:17 Is this person from the CNCF that's doing this?
**Trent Mick** 57:22 He's a member of Ruby's…
**Daniel Dyla (Dynatrace)** 57:25 rib.
**Trent Mick** 57:26 triages. I've seen him… doing small PRs on a number of repos, but I don't know anything more than that.
Yeah, okay. Not a high priority, but if you're gonna take a look, Mark, great.
**Marc Pichler (Dynatrace)** 57:42 Yeah, I'm planning to have a look, because I've also been looking at the security, the OSSF Scorecard thing.
**Trent Mick** 57:52 We're kind of in the same bucket for that.
There's 3 minutes left, one more box.
Okay.
Looks like you'd reviewed a while back.
So that's ongoing.
Okay, I guess he's looking for another review from me then.
**Marc Pichler (Dynatrace)** 58:37 I need to take another look. I think there's still one export I'm missing, but I'm not sure.
Follow up on that.
**Trent Mick** 58:50 Wait, if this is just gRPC, this… it's only these 3, right?
**Marc Pichler (Dynatrace)** 58:55 Yes, you're right. So I guess we should be fine then.
Last time I checked, it was just two of them, I think, but looks like it's all of them now.
**Trent Mick** 59:11 Pence.
Okay.
Okay, cool.
And I think that's time. Didn't quite get to me.
Much better.
Mine.
Boop.
Thank you.
**Marc Pichler (Dynatrace)** 59:28 Thanks for listening.
**Trent Mick** 59:28 See you guys later. Yeah, I'm off next week, and maybe the week after, I'm away for a week and a half, so… See you guys in a while.
**Daniel Dyla (Dynatrace)** 59:36 Enjoy.
**Trent Mick** 59:37 Thanks.
**Marc Pichler (Dynatrace)** 59:38 Thank you.
