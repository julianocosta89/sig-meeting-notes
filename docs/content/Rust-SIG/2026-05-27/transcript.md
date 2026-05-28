SIG: Rust SIG
Date: 2026-05-27
Duration: 20 minutes
Zoom Recording URL: https://zoom.us/rec/share/PpO-_IGuN3sLHDMDBl0C8OouZ3GuHHTpD4SzIaaha2RNMapyNaiGkL9LwTJy1CfG.S7zvY04RMivtTqAv
============================================================

## Zoom Recording Transcript

**Cijo Thomas (Microsoft)** 01:35 Hello, Scott. How are you?
**Scott Gerring** 01:40 Hey, how's it going?
**Cijo Thomas (Microsoft)** 01:42 Goat?
**Scott Gerring** 01:44 Long time no speak.
**Cijo Thomas (Microsoft)** 01:46 Yep, yep. I'll have to find a different slot to… have the community calls, because morning, 8 o'clock, morning 9 o'clock, both are, times when I'll be on a bus, or driving on my way to work.
**Scott Gerring** 02:05 Yeah, maybe the thing to do is to move… the Tuesday one… that I think was originally intended to work better for you folks later in the day, and then… Bjorn and I can cover this one, Euro time, you folks can cover the…
**Cijo Thomas (Microsoft)** 02:21 Bluetooth one? Yeah.
Yeah, I'll do a poll to see if anyone else has opinions. We have very light attendance, so it should be relatively straightforward.
**Scott Gerring** 02:33 Yeah, I think if we moved the Euro one… maybe if we'd make them both sensible for the two continents, then we would get more attendance as well, and we can start hyping it up a bit more in the channel.
**Cijo Thomas (Microsoft)** 02:45 For the Wednesday one, do you prefer making it even earlier? Because this is 8 o'clock Pacific time, but it's still, like, quite evening for you, right?
**Scott Gerring** 02:54 Yeah, it's 5pm here, which is fine, right? But I think if we… if we just, accept that we have two separate meetings that are kind of independently useful, then they can both be more useful on both ends, and then maybe we can ad hoc have catch-ups with everyone periodically.
**Cijo Thomas (Microsoft)** 03:10 Okay.
**Scott Gerring** 03:11 Wouldn't make sense?
**Cijo Thomas (Microsoft)** 03:13 Yeah, yeah, look, so I'll do a cube poll to move Wednesday one, one hour earlier, and Tuesday 1, 2 hours later, so it will be more friendly to both time zones.
**Scott Gerring** 03:25 Cool How are you otherwise? I guess, quite busy outside of our hotel room.
**Cijo Thomas (Microsoft)** 03:29 Oh, yeah, I mean, like… it's very hard to get to touch anything related to SDKs these days.
Because we are spending most of our energy elsewhere.
Yeah, and I had a talk on the conference last week, the Surability Summit, so last week was… Yeah, but yeah, it's still doing Rust, not a lot on client side, but… Anyway, I think… so last week, we had Bjorn and myself, so just two of us. Yeah, it's just not reflected here.
Yeah, that was, like, after a long time we spoke, we discussed a few things.
**Scott Gerring** 04:16 Cool.
Yeah, I've got a few big PRs open, but I appreciate that that's also a bit off-putting when you know that there's, like… I mean, especially the runtime thing, right? That's gonna be such a pain.
**Cijo Thomas (Microsoft)** 04:29 Yeah, I should be spending more time on those things, but I also want to get to a place where we can close the OTLP exporter and start working on tracing.
Oh.
**Scott Gerring** 04:42 Yeah, I think that would be really good. I think that, aside from the runtime stuff, I mean, that's the big… That's the lurking one.
**Cijo Thomas (Microsoft)** 04:49 Because…
**Scott Gerring** 04:50 I think there's still a few small ones, but… That'll be easier to get through.
**Cijo Thomas (Microsoft)** 04:56 Okay, yeah, let me just do a quick cleanup. So, 3.2 was shipped.
And 3.3 is what I opened with June 30 as the… I mean, these are things which not really tracked elsewhere, so I just put it into this milestone.
**Scott Gerring** 05:13 Yeah, none of that is super traumatizing, I think.
**Cijo Thomas (Microsoft)** 05:16 Yeah, so this is the key part, the exporter one.
**Scott Gerring** 05:20 What else do we still have open that looks big in here?
**Cijo Thomas (Microsoft)** 05:23 So… The OTL page support is the highest priority one.
And tracing APS table, yeah, we need to do a couple of things here. One is on me, which is to… Get a single issue which tracks All the changes we need to do on the API itself.
These are, like, general, like, collection of things.
Not really organized, I think some of the things which I want to work on, like, they are all covered here, but it's just, like, too hard to find.
Which one, we should be looking at.
**Scott Gerring** 06:03 Yeah, I've also, over the past… or so, burnt through everything, marked triage, and closed a bunch of issues that were just stale and whatnot. And I know you've done that PR auto-closing bot, which I think is also a really good idea, because there's just so much stuff that's not relevant anymore sitting around there.
**Cijo Thomas (Microsoft)** 06:21 Yeah, we need to get to a state where we can focus on things which matter. So, by end of this week, we would be closing most of the inactive PRs, and the thing which still survives are the ones which we need to focus attention to.
But that aside, like, yeah, I mean, I only have, like, two goals. One is to get the API for tracing stable.
Because that 5-year, 6-year-old project, people are still asking, hi, where are we with tracing?
Yes, I'll be spending most of my time there, and just help you with whatever is needed to get ODLP2 stable, and from my understanding, it's mostly waiting on the runtime stabilization.
Yeah.
**Scott Gerring** 07:08 Let me… let me also go through that whole list again. I had a tracking issue for a bunch of this stuff, yeah, down.
**Cijo Thomas (Microsoft)** 07:16 You created this Uber issue, which covers almost all of them nicely.
**Scott Gerring** 07:22 Yeah, I need to… I need to catch up on the stuff that is in the runtimes as well, because there's probably some other things in there, but I think it's mostly little… or things that are non-blocking for stability, but I… I can take that as an action and clean it up in the next couple of days.
**Cijo Thomas (Microsoft)** 07:36 Feel free to… feel free to aggressively cut things which are not required, so anything which is a nice-to-have, feel free to defer so we can, officially…
**Scott Gerring** 07:47 Looks good.
**Cijo Thomas (Microsoft)** 07:47 And then we can address things afterwards.
**Scott Gerring** 07:51 Yep, I will sort that out this week, in fact. I'm just finding the link… Issues, milestones… Yeah, the other thing which is… Probably easier, but also probably less important, is this process context thing that we need as the foundation for the thread context, that we need for the eBPF profiling.
**Cijo Thomas (Microsoft)** 08:17 Yeah.
**Scott Gerring** 08:18 DR for that as well. It's…
**Cijo Thomas (Microsoft)** 08:20 I…
**Scott Gerring** 08:21 standalone, but yeah.
**Cijo Thomas (Microsoft)** 08:22 I have asked, like, Lilith to look at it. He should be able to offer more guidance on that one. He said he will look at it soon, so I'll…
**Scott Gerring** 08:31 Yeah, that'd be cool. Also, if… I think he was interested in the thread context stuff.
**Cijo Thomas (Microsoft)** 08:35 Yes.
**Scott Gerring** 08:36 We'll be able to do the nice request-correlated profiling, which would be cool.
**Cijo Thomas (Microsoft)** 08:40 We explored a lot of eBPF and Rust, for the last 2 years, and, so he has… The context already on, like, why we are doing this thing.
So, hopefully, like, he can do the best review.
**Scott Gerring** 08:57 Yeah, we've got it all… we've got it all going.
with… slightly forked OpenTelemetry Rust.
with slightly forked eBPF profilers, so it all can work, it's just a matter of upstreaming it now into the full host profiler, the OTEP for the thread context, and then some SDKs.
But it'll be… it'll be a cool one, I think.
**Cijo Thomas (Microsoft)** 09:21 Are you working on eBPF yourself, or, like, or… Tetadog as a company is working on eBPF.
**Scott Gerring** 09:28 I've been drawing myself more and more into the profiling team. I'm gonna be working with them on heap profiling.
or an embed for 2 months from the middle of June, and that inevitably moves more into the eBPF world. And I like that stuff, I like the systems thing, so it's gonna be cool. And getting heat profiling out of it is gonna be really exciting.
**Cijo Thomas (Microsoft)** 09:51 Okay, so your interest in eBPF would be mostly for the profiling and not the auto-instrumentation, right? The OB effort?
**Scott Gerring** 09:58 Yeah, yeah, we're aware of the OBI stuff, and there's some points where they sort of overlap in the middle in terms of exposing context outwards, but yeah, it's a bit different. I'm not so interested in the auto-instrumentation stuff, personally, no. I think it's a cool thing, to be clear, it's just not what I spent time on.
**Cijo Thomas (Microsoft)** 10:16 Yeah, that is another area which Lalith was particularly interested in looking at, because we are currently having a situation where a lot of services which are originally written in C or C++, they're trying to migrate to Rust, and they are not able to do it in one shot.
**Scott Gerring** 10:35 Yeah.
**Cijo Thomas (Microsoft)** 10:35 We write some components in Rust, some in C++, and that creates a lot of problem, because the span created in one Library is not aware of the span in other ones, so they're not able to Do the parent-child correlation properly.
Similar to the issue we had with the Tokyo Tracing Library, like, it has its own context, we have our own. So Lilith was exploring, like, eBPF to see if we can intercept the… Async, context jumps across threads, and restore the right one.
from eBPF, so that irrespective of whether you use Rust SDK or a C++ SDK, you still see the same context. That was one of his motivation.
But it's not a officially funded project, so it was mostly just exploration. He did a presentation in the Rust conference a year ago, but that's it, and after that, we never continued that work.
**Scott Gerring** 11:32 Yeah, that's It's not an easy one, that.
**Cijo Thomas (Microsoft)** 11:35 Oh yeah, of course, it's very tough, but yeah.
**Scott Gerring** 11:37 But it's definitely interesting.
**Cijo Thomas (Microsoft)** 11:39 Yeah, if someone is interested in that kind of kernel-level stuff, then it's a very technically rewarding project also.
Yeah.
**Scott Gerring** 11:48 Yeah, I'll keep my ear out for stuff, because we… the profiling team we have are really interested in all those sort of things, and it might turn out we've done something similarly internally. Although at Datadog, we didn't have… we haven't had so much C and C++ historically. Before we got into Rust, we mostly just did things that were common between languages once per language, and now that we're using Rust, we've kind of… got this LibDadog thing that pulls out all the commonalities when we have it there, so I guess what I'm saying is there's not so much native code aside from Rust here.
**Cijo Thomas (Microsoft)** 12:21 Okay, yeah, yeah, Microsoft is, like, very much C++.
**Scott Gerring** 12:26 You've been around for a bit longer than us, it turns out.
**Cijo Thomas (Microsoft)** 12:30 It's not just C++, some of them are in C, for which there is no open elementary support either, so… And there is no motivation for people to build an Open Elementary C, so most of them are trying to do FFI into Rust.
So, it's very messy, because you load, like, two SDKs into the same process, one the Rust SDK, one C++ SDK, and both have their own understanding of the world.
**Scott Gerring** 12:59 I think if you do it in a way… if Rust is always on the outside, and it's always calling over FFI into C, and C is never doing its own threading underneath.
then you really just have to check the Rust context, hey? But I guess it must be more complicated than that.
**Cijo Thomas (Microsoft)** 13:18 Yeah, I mean, there is no, like, no official person working on it, so it was more like… Let it… he has personal interests, or let me go explore something.
**Scott Gerring** 13:28 Yeah, fair enough. I'll ping him if I see anything related, anyway.
**Cijo Thomas (Microsoft)** 13:32 Yeah, so anyway, I'll send him a remainder to help review the two PRs which you mentioned.
**Scott Gerring** 13:37 Yeah, that'd be cool. Also, it would be really good to get his… feedback on the second OTAB, so the… there's, like, the process one, which we've got in, and now there's the thread context one that we've got open at the moment. I can ping the link into the docs, but that… he expressed an interest in that before, so this is the one where you put magical things in thread local in a specific way, and the profiler can find them.
**Cijo Thomas (Microsoft)** 14:02 Okay, yeah, I was just taking a quick look at our overall status, it's still accurate, like, we still need to touch the… OTLP exporter, mainly, and then Tracing API, and there is some propagator stuff which we never looked at closely, but I think it can wait a bit, because Tracing API is more important than that.
**Scott Gerring** 14:26 Yeah, I… I feel the same way as you, like, tracing OTLP.
Everything else?
**Cijo Thomas (Microsoft)** 14:33 Also have some interest in the country report specifically.
The instrumentation, I think we wrote the guidance, which, like, we merged… no, I don't think we merged it, I think I… I think you reviewed it, and I am waiting for more people to sign up, let me just quickly… Take that, Pierre. You're able to see my screen, right?
**Scott Gerring** 14:58 Yep, yep, yep, yep.
**Cijo Thomas (Microsoft)** 15:00 Yeah, so there's document for distributed tracing and logs guidance, which is somewhat unusual.
For any Open Elementary repo, because it's too obvious the answer, just go and use Open Elementary, but for us, we have to do it specially.
Yeah, I think we already started using the word, like, prefer instrumentation libraries, which kind of puts us in a spot, like, we need to make sure at least one instrumentation library is, reasonably usable, performance tested.
So I'm going to pick Tower, because I think… Based on my understanding, it can be used in any framework as long as you plug in the tower middleware, so… This has more… Value than ethics.
So I'll be spending some time on this one. There are open PRs already, to fix some of them.
So if you ever get, like, interested, like, just also help with the, tower side of things. This is directly helping us with the, stability of… Tracing itself. Yeah.
**Scott Gerring** 16:05 also be a good one to try and pull in new contributors, I think.
**Cijo Thomas (Microsoft)** 16:09 Yeah, we already have, like, a couple of folks, so I recently officially listed them as owners for… That particular crate.
So we got, like, two people, from Grafana. I don't know which company hand works, but at least it's someone different than the usual approver, so that's very good to know.
Yeah, and I've been playing with few ideas in this repo, which is specifically like this one.
This is a very new concept in OpenTelemetry. There is this Weaver tool. You can actually do a live check to prove that your instrumentation is… actually producing things following the semantic convention. It did work, it actually catches things, it's very interesting, and I'm also helping Weaver itself, the upstream Weaver report to improve their tooling, so we can easily Test things here.
So these are, like, not really tied to any particular project, but general, quality improvements, And my main focus, or my main motivation is, if we have, like, concrete, very solid validation that instrumentation libraries are working as they intend to, we can generally let AI take care of, like, instrumentation, updating, fixes, because all we need is a… sign off from the Weaver life check that, are you compliant or not? If they're good, then we can do a very quick review.
**Scott Gerring** 17:37 That'll be helpful, and this is… this is a bit less, A bit less fraught than the main repository in terms of complexity as well.
**Cijo Thomas (Microsoft)** 17:46 And there is a effort across OpenTelemetry, which is… improve the overall stability and quality of OpenTelemetry, and one of the issues which is being discussed is who wants the instrumentation libraries.
So, historically, the maintainers say that it's not… Like, it's not part of the main repo, so they don't own it, and in country repo, like, anyone can own it.
There is no clear accountability, so we're trying to like, figure out a model where the maintainers take responsibility for at least some of the core instrumentation libraries for their respective language. It's still being discussed, it's not, like, settled or anything, so I'm trying to be a little bit ahead of that by trying to own the instrumentation libraries by the… same group who maintains the report itself. Yeah.
**Scott Gerring** 18:38 Yeah, at the very least, it's like a fallback maintainer or something, I suppose.
**Cijo Thomas (Microsoft)** 18:43 Yeah, I mean, by default, we are the maintainer for anything. If there is no one expl… I think we put that somewhere here also, like, if it's not… Taken by anyone, then it's assumed to be the, same people who own everything else. I think we put it here.
Yeah, for anything not taken by someone else, it's the same people.
**Scott Gerring** 19:06 Yep, cool.
But yeah.
**Cijo Thomas (Microsoft)** 19:10 Okay, anything we want to look at together right now, or we can split off and do offline reviews?
**Scott Gerring** 19:17 No, I think it's good. Let me know how you go with those PRs when you get a chance, and maybe give Lilith a ping, I'll chuck in a link for our latest OTAC thing. And yeah, stay in touch. It was good talking to you again.
**Cijo Thomas (Microsoft)** 19:32 Yeah, nice meeting you again after a gap. Let's talk again another week. Hopefully, by next week, I will reschedule the calendar, so we may not meet each other in the calls, but at least the calls will be at least occurring with two people or more.
**Scott Gerring** 19:47 Yeah, yeah, and I think we can periodically have bigger ones as well that suck a little bit for everyone, but are manageable.
**Cijo Thomas (Microsoft)** 19:54 Oh, yeah, by the way, like, starting mid-June, I'll be, like, in a different country, I'll be flying to India for KubeCon for a couple of weeks. So those two weeks, I'll be in a different time zone. Maybe it's easier for me to attend, so we'll see how it goes.
**Scott Gerring** 20:07 Yeah, yeah, sounds good. Enjoy it anyway.
**Cijo Thomas (Microsoft)** 20:09 Alright, see you then.
**Scott Gerring** 20:11 Cheers, Asia. Ciao.
