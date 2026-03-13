SIG: Profiling WG
Date: 2026-03-12
Duration: 63 minutes
Zoom Recording URL: https://zoom.us/rec/share/YkKZQhJ56bXX0nL_k6z2l81rzrA4jnMMpytXuXXueUAx73aQnuESNeq88kurTUrU.zx60jN3r573oSTOc
============================================================

## Zoom Recording Transcript

Damien Mathieu 00:01:19 Hi.
Florian Lehner 00:01:22 Nope.
Frederic Branczyk 00:02:22 Hey, hey!
Felix Geisendörfer 00:03:48 Did the invite show up on everybody's calendar automatically in the end?
Okay, good.
I'll still keep an eye out. Somebody has problems joining, but I think we can get started in a second.
Okay, I guess we can get started if somebody comes in later, that's also fine.
I'll share my screen.
Let's see… Anybody see this?
Florian Lehner 00:05:09 Yep.
Felix Geisendörfer 00:05:11 Then, Yeah, a few action items. We probably at some point need to decide if we want to use this list or this one here. I kind of created a mess by creating a second list, so I apologize for that. I would want to probably start with this list, because I'm kind of treating it as the source of truth for figuring out what we need to do for the alpha, which should be top priority.
I think we're making really good progress, and I'm cautiously optimistic that we're gonna make it, so… I'm excited about that. So to recap, all the collector PRs that Florian had in flight are merged now, so that's good. We got some V10 proto-release out.
And now we're basically waiting for, the review from the, PC, to basically just approve us, like, calling things alpha, which I think basically would be formalized by merging this pull request right here.
Which would, basically mark all the components, as alpha.
And… Then, I think we are down to getting the blog post and the documentation, out, and… giving the presentation, so I think we're really on the home stretch here, unless something comes up with the TC review. I'm still waiting to hear from Josh, who… apparently they had a TC meeting yesterday, I don't know if anybody heard something. I think Josh is not here today, right?
So I will continue pinging him async.
But yeah, I think unless something goes wrong with the TC review, I think we're… the remaining steps are pretty straightforward, so we can just go through, like, updates on the open tasks and talk about them, and then go to the other to-dos that we sort of have on the list. So maybe I'll just start with those two.
Copy this right here, into our… If you… let's see if this is copy and pasting well… no, it's not.
We do not have… Okay.
So, the first one would be the, blog post, Alexi, I think, is here. Do you want to give an update on how that's going?
Alexey A 00:07:45 Yeah, I think it's… I would say it's, 70%? 80% ready? I'm hopeful that I can turn it to, to a PR early next week, and hopefully that… So, one question is, I assume we want to actually, like, publish it… yeah, one thing I need to understand, like, I assume, like, publishing it, it's basically, like, merging the pull request, because I think this is… like… I'm not sure, but I assume… I don't know, like, what the publishing system for this thing is, but… Presumably, it's just merging DPR.
Felix Geisendörfer 00:08:26 I see some nuts in Florent, I guess… You've done this before?
Damien Mathieu 00:08:32 merging with PR.
Alexey A 00:08:34 Okay.
Okay.
Damien Mathieu 00:08:35 The OpenTeameter.io website is, you go static site, and so you merge, it gets auto-declared, and that's… Alexey A 00:08:44 Okay, okay. And then I think… so I think there's, I think, like, the content is there, it's just, like, I need to take another pass and see… what… like, clean up some of the comments and see if there's anything missing. Like, I would… I would encourage everyone to take a look, just, like, scan the content.
to see if everything is missing. I'm… I'm kind of… I'm less concerned about this not being, not being, like, fully polished, I'm more concerned about missing any… any large pieces.
And then for specific… for specific questions, so, like, I have… there's also one terminology discussion, should we say… like, what the title should be? Should the title be Open Telemetry Profiling Enters Public Alpha, or Open Telemetry Profiles Enter Public Alpha? Because they, like, profiling versus profiles.
there's… there's a… because I think, like, the official signal name is Profiles. Should we use that in the title? And I think Florian… I see Florian nodding, and I think Florian also commented that, yeah, we should use profiles. I don't have objection, but… so I'm going to change to profiles, but if anyone I kind of, like, I like how profiling flows better, because profiles… just fills… but yeah, official name is official name, so I'm happy to use that.
Felix Geisendörfer 00:10:16 Yeah, I mean, that's metrics, locks, and traces, I guess, then that's profiles, right?
Christos Kalkanis 00:10:21 We also use profiles in the documentation. Like, all the pages I worked on, that's consistent terminology.
Alexey A 00:10:28 Okay, then I'll also take a pass to fix that. And also, there was discussion around the screenshot.
One thing, I asked Christos At one point, to use… simpler tra… Yeah, and I think, I think it was updated, to… back to what it was, or something similar. So… My con… my concern is, like, the screenshot that… the newer that I, was added, I think, this night, well, this night for me, and this day for some of you.
It's like, it's very loaded. The names are long… .
Florian Lehner 00:11:10 Yeah, it was me that suggested to use this new screenshot. The reasoning is, I think it makes sense to showcase that more than just Go and the kernel is supported, you can get playinggrounds from Go with Kyle in some multiple ways, so I just wanted to have something that have Node.js and Java as an example. Yeah, but Java names tend to be long, so that's… That's the case, yeah. But I also see the… Yeah, I'm… Could be… playing grass could… can look different, so whatever you prefer, I'm not a strong opinion on this.
just thought that it would be better to showcase, hey, there's more than just Go and the car.
Christos Kalkanis 00:11:56 I think… so, my point of view here is that this blog post is not really about DevFiler, so the reason we even added this credentials of DevFiler there is just to kind of spice it up a little bit, but the focus of the blog post is not really on DevFiler, it's on the alpha.
So, the less visually complex the screenshot is, and the faster and easier they can just look at the screenshot and immediately parse it and see, you know, get the gist of it, I think the better. So… I mean, I prefer the… the simpler screenshot.
Felix Geisendörfer 00:12:28 Yeah, I want to second that. I also prefer the simpler screenshot, because it also has, like, fully symbolicated screenshot, like, this other screenshot has a lot of symbols that are not resolved, which makes it seem like, oh yeah, you mean alpha when you say alpha, which is maybe not how we want to… pitch it. So I think I like the simpler one, too, and I think we can have separate blog posts where we talk about the EVPF profile again, and all the cool things it can do, where we can show that off. I think it's just, yeah, different story, right?
Florian Lehner 00:12:59 Okay, and then I will remove my image.
Felix Geisendörfer 00:13:10 Okay, yeah, so otherwise, Alexi, you still want some more feedback on it, or any call to action here, or it's mostly on your plate?
Alexey A 00:13:20 It's mostly on my plate, but, Felix… Felix, if you in particular could, Felix Geisendörfer 00:13:27 Take a scan.
Alexey A 00:13:29 And, and see if anything is missing.
Felix Geisendörfer 00:13:32 Yeah, I will do it first thing tomorrow morning, my time, so you'll have it once you get… Good luck.
Okay.
Alexey A 00:13:51 One quick note, I wonder if anyone has opinion, is, like, one… since the blog post is about profiles, not about DevFiler, one thing we could even consider doing is, hiding this screenshot behind a link.
like, don't… sorry, don't embed it into the text, but put it on the link. I think the trade-off is that The picture makes the blog post much more visual.
But at the same time, also, as you said, like, the blog post is not about DevFiler, it's about, it's about profiles, so, I think I'm slightly inclined to leave it in text, because it's… I think it makes it more attractive.
But if anyone has any thoughts, just wanted to bring this up.
Christos Kalkanis 00:14:34 Yeah, I think having the screenshot in there just also, you know, whets people's appetite to try it out, right? Like, it's one thing to just read a blog post that's full text, and another to just see it. So, I would say, let's leave it in.
Alexey A 00:14:47 Okay.
Felix Geisendörfer 00:14:48 Yeah, I would also be for leaving it in the text.
Okay.
But yeah, then the… just on the publishing plan, I think the idea would be for somebody to press a button during the presentation for it to go live. We'll have to figure out who has merge permissions, if it's merge gated, and make sure somebody with such permissions will be in the room when that happens.
Alexey A 00:15:27 Yeah, on the timing of publishing the blog post, like, should it happen, like, an hour before you KubeCon talk, or… Felix Geisendörfer 00:15:38 I think, like, for some of the stuff, hotel has done it, like, on stage before, where, like, say, like, say, like, now it's going live, and you can find the blog post, but we could also do it an hour before, I don't think it greatly matters.
Alexey A 00:15:48 Okay. But not, like, days before, so, like, it's, like… Felix Geisendörfer 00:15:53 Yeah, I would probably not do it days before, I mean… Alexey A 00:15:55 We do want to time it, okay, okay.
Felix Geisendörfer 00:15:58 I think so, unless somebody who feels like… Damien Mathieu 00:16:01 I think the easiest is probably to synchronize with a comms maintainer. I think severing will be at a coupon.
And just, like, check in with him so that he can push the merge button at the start of the dark art a bit earlier.
Alexey A 00:16:23 Can you record the full name? Because I would… I think I'll try to find them in Slack, and just give a heads up that, like, this PR is coming, and this is… And we will have some time sensitivity.
Seems like a good idea to just, like, make sure that, like, the person is not… It's not on PGO that they were… just like I… Damien Mathieu 00:16:45 I just… Alexey A 00:16:45 approach.
Damien Mathieu 00:16:46 did their GitHub handle in chat.
Alexey A 00:16:49 Cool, thank you.
Felix Geisendörfer 00:16:56 Okay, yeah, but I think if there's, like, some blocker where we can't have somebody press a button, then we'll just do it a little bit earlier or a little bit later. I think it would be nice to have it, like, doing it during the talk, but it's not a deal-breaker if not. Okay, any other thoughts on blog post?
Alexey A 00:17:10 That's it from my side, thank you.
Felix Geisendörfer 00:17:13 Then documentation would be the next one. Crystalos, can maybe give an update?
Christos Kalkanis 00:17:19 Yeah, so I created this meta-issue in sync profiling. So the documentation work has split it into, kind of, two strands. One is purely the documentation that's available in OpenTelemetry I.O, and also the specifications, so that's the first part there.
And I plan three pull requests for that. One is already merged, that's the Profiles Concepts signal page. The second one is in review, has some approvals already, that's the specification page. And the third one, that's actually most of the work, is the data model.
So I'm currently working on that, and I think I will have it finished by the middle of next week. Now, I'm flying back to the US end of this week, so the weekend for me is just gonna be gone completely.
But yeah, I should have it ready by next Wednesday.
And then, the other strand of documentation is purely DPF Profiler and DevFiler related. I want to clean up some of the instructions over there, just to give people a much more straightforward way to try it out.
But that's, like, less than an hour of work for me, so I can, I can do it at any point.
But yeah, my plan right now is this middle of next week to have all of this wrapped up.
And then for the data model, yeah, I would welcome, like, all of you to actually take a look there, because it is kind of the page that's the more meaty and the more important one, in terms of, like, it has to be clear enough for people to understand.
Felix Geisendörfer 00:18:51 Right, and let's be clear on the target audience. Would that be, for example, for SDK maintainers who want to add profiling to the SDKs, or who do you target with that?
Christos Kalkanis 00:19:01 what I'm doing right now, I calibrate that, like, I look at how logs did it, how metrics did it, so I kind of try to have kind of an equivalent level of abstraction for profiles, so it's going to be technical. I'm going to basically take the protobuaff.
split the messages out, visualize them, solve the relationships. Essentially, the ASCII diagram that we have in the protopath is going to be the skeleton of the data model, and then cover all the corner cases that I can think of.
Regarding the data model, like, and the decisions that we made, and if I can find reasons for those decisions, at least for the important bits, I'll try to have those. For example, I think we absolutely need to describe why we went with a custom attribute, a key value in unit, instead of using open telemetry attributes.
We do use open language attributes, but not everywhere, right? So we have to make that kind of distinction clear there.
And maybe the application scheme that you use, that we use is not the strings, it's multiple messages, we have this dictionary there, so just explain some of that.
And so on. And I'll probably go back to the benchmarks that we did, and maybe pull some data out of those as a justification for why we ended up with the model as it is today.
Felix Geisendörfer 00:20:17 Makes sense.
Yeah, we're happy to review that once it lands. I think the… the more we have there, the better, but also, like, if you're in a time crunch, and, like, I think a simpler version of that page would also do, or if we have to launch that page after the KubeCon, I think that's also not, like… to me, it wouldn't be a deal-breaker, I think. Like, I think it's most important that we have high-level information about the signal and how to try it out and get some feedback. I think, like, the nitty-gritty of how the signal works is of interest to a much smaller audience than who we're targeting with the alpha, I guess.
Christos Kalkanis 00:20:57 Yeah, so the skeleton data model will be there for sure, and then, you know, it's up to, like, I'll try to add as much as I think makes sense for now. And… but what I don't have planned is any API-related documentation, because I haven't really… Delve into that, so… People who would like to programmatically generate profiles.
I don't have anything for them. I don't know if we should have, if we absolutely need to have something.
then I'm probably not the right person to do that.
Felix Geisendörfer 00:21:31 You said you're not going to cover API, and then the last thing, was it still about API, or did you say something else?
Christos Kalkanis 00:21:36 Yeah, API, yeah. Okay.
Felix Geisendörfer 00:21:43 Do we have an API for now?
Christos Kalkanis 00:21:45 Well, we do have, you know, the RASP data. I don't know if we can… if we want to go into that.
Felix Geisendörfer 00:21:51 I don't think that's what OTEL considers API, I think. I think OTEL considers API, it seems that the SDKs are supposed to.
Christos Kalkanis 00:21:58 Alright.
Felix Geisendörfer 00:21:59 Right.
Florian Lehner 00:21:59 I think Jonathan had some document on the Java API, but for Go, I think there is no such API.
Jonathan Halliday (IBM) 00:22:06 Yeah, we're unique amongst hotel signals in defining the wire spec and not the corresponding API, because I think that use case is going to be very rare. There's just not that many things that are going to be encoding profiles.
It's essentially people who are making profilers.
Felix Geisendörfer 00:22:37 Yeah, I mean, we might still want to, like, give some sense of, like.
But, yeah, maybe this can be done while we're in alpha, like, how to, like, in an SDK where you can explicitly start and stop the profiler, what that should look like in an abstract way, right? I think that's what we would understand as, like, API for the profiling signal.
Jonathan Halliday (IBM) 00:23:06 I think even that is going to be much more language-specific than the other hotel signals.
in the… Felix Geisendörfer 00:23:14 Yeah.
Jonathan Halliday (IBM) 00:23:14 In a number of cases, you're not using the same language.
To do the profiling, as you are to… You know, write the app that is being profiled.
Ebpf in particular, yeah.
You're not doing the profiling yourself.
Hmm.
Felix Geisendörfer 00:23:30 Yeah, no, absolutely, and for Java, you might.
Jonathan Halliday (IBM) 00:23:31 Starting and stopping it.
Felix Geisendörfer 00:23:33 Yeah, and for Java, you might inject an agent or something.
Jonathan Halliday (IBM) 00:23:36 Yes, yeah, the likelihood is you're calling down to either JFR or to async Profiler for Java.
Part of my long-term plan is perhaps to offer some way to configure both those two through the Java SDK, so that you set up Configuration for all the signal types.
in the config file for the agent, and it will take care of, you know, using a plugin or something to talk to JFR or async Profiler.
Which I think is a cleaner way to do it than having to… Configure the… the one signal sort of out of bound in… in some… Weird way that isn't consistent with the rest of the hotel.
But even that, I'm… It's not an API in the same programmatic, here's a set of Java classes, sense that the other signals have in the Java SDK.
Felix Geisendörfer 00:24:35 Yeah, maybe we can do, like, on this roadmap here, do a post-alpha, like, think about documenting APIs and what that means.
I'm just gonna put it down like this for now, and then create a sub-issue later, so we don't forget about it. But I think… I don't… I don't think it's on the… on the critical path for Alpha. I think we can skip, say, API for now.
Unless somebody feels strongly about it.
No strong opinions.
auditable from my end, so let's carry on. Anything else on documentation?
Christos Kalkanis 00:25:27 I think that's it from my side. Do we need anything else? So, essentially, we have three phases, right? The concepts, which is already live, so you can go on this document telemetry site and already see it. Specification, that's waiting final approvals and meds. It already has 3 or 4 approvals.
And the data model.
Felix Geisendörfer 00:25:48 Yup.
I think that's pretty much it, together with the blog post. I think for Alpha, this is a pretty good starting point, from my point of view. I don't think there's… are there formal requirements for Alpha? I don't think anybody's written down what docs are technically required, right?
So it seems kind of obstacle to the side.
So, yeah, thank you so much for working on this, Chris. It looks really good, what you've done so far, and I'm looking forward to reviewing the new PRs.
Alexi?
Alexey A 00:26:23 The date is March 26th, that's when the, that's when your talk is, Felix, just confirming, like, the exact, date, because I'm, I'm messaging Sivir in.
I just want to… Felix Geisendörfer 00:26:35 I have linked it here. I think that sounds about right, but yes, it is. This is the exact time.
Alexey A 00:26:42 Okay, okay, and it's linked from the task list, okay, thanks.
Felix Geisendörfer 00:26:46 Yes, yes, you can find it from there.
I'll try to link later.
Okay, then I will see if we have some other action items from up here, Okay, I'm gonna delete this since we're tracking this in GitHub for now.
Context propagation OTAB, do we have Evo here already?
Ivo Anjo 00:27:29 Yep, I'm here.
Felix Geisendörfer 00:27:31 Okay, you wanna… Talk about it.
Ivo Anjo 00:27:35 Yes, so, the, I think the TLDR is that we have, draft PR now that implements the, thread context and the process context in the eBPF Profiler.
They are kind of, like, stacked on top of each other, because if you remember, one of the things we are trying to… one of the tricks we have is we kind of use the process context to announce the thread context, so we kind of need them both to detect the thread context is there.
We… I think… I would… we've been holding back on opening a PR upstream on the OpenTelemetry specification repo, because we wanted to have, like, the PR on the BPF side, and people give it a look, so I… I think at this point, the question is, like.
Do we think, we're ready to open a, to open a PR on the OpenTelemetry specification side? Do we want to… do we think it's worth iterating a bit more before we open this to a wider hotel?
I'm seeking for some guidance slash opinions here.
Florian Lehner 00:28:49 I watched a GC and TC meeting that happened last week because I wanted to look for a decision on the… from TC about our alpha status.
This was not included, but a big topic on the GCTC meeting was the workload of the GCTC meeting, and they don't know how to deal with all the OTEPs and specification work.
And, as we see, your existing spec… OTEP for the process context propagation already takes We can already count months, I think.
So, yeah, I'm… Just a personal thing, maybe we just should land process first, and then… Good for the thread context.
But that's just a personal impression, Overloading the people that are responsible, that bring us these merges.
Would probably not help us.
Christos Kalkanis 00:29:45 I think… I think we should open the thread context… I mean, with the opposite opinion, actually, because we're not overloading anyone, right? Like, if somebody has time, they can look at the OTEP. What we're trying to do here is to get the most people that are willing to take a look, or are interested in this, to take… actually take a look, and the sooner we open the thread context OTEP, The sooner the whole process starts to take place, right?
So more people can see it, more people can discuss it, review it, and so on. Like, why wait?
That's my way soon.
Florian Lehner 00:30:15 Evo pushed already, quite often, the SIC meetings and specification meetings and asked for feedback.
And, The feedback is… Not coming in, so… asking for more feedback is more like, yeah, here's even more work to do, please… Do it, and… yeah.
Christos Kalkanis 00:30:37 But the process context has a lot of feedback already. Like, if you look at all the discussions that took place in that total… Yes.
Florian Lehner 00:30:43 The key people are missing.
Christos Kalkanis 00:30:46 Okay, but the OTEP is not just about the two or three key people, right, that are responsible for finally merging it. Like, if you look at the discussion for the process context, it actually saved the implementation, right? We changed parts of the proposal.
based on threads that took place, discussion threads that took place in the top 10, and maybe the same thing ends up happening for thread context. So I think… The sooner we get to start having those discussions with anyone that feels invested in this, the better.
Florian Lehner 00:31:18 I leave it up to Ivo. That's… just wanted to share my impression.
Felix Geisendörfer 00:31:29 Alexi, you have entered.
Alexey A 00:31:31 Just as a note, when I was writing… when I was updating a blog post to mention process and thread context work, as a note, like, I was not sure, like, should we… mention it as part of alpha… I think I ended up mentioning it as, like, work in progress, because technically we don't have, like, OTEPs, merged.
So if… Anyone is willing to review that specific wording in the… in the post would be good.
Felix Geisendörfer 00:32:02 Yeah, I think we could have, like, at the end, like, a section on future work.
Alexey A 00:32:07 there is what's next, but currently I mention it above, like, in the section that is about open telemetry ecosystem and how profiling integrates, but… Take a look if you think it should be moved down, happy to do that.
Felix Geisendörfer 00:32:22 Maybe Ivo could. Do you, I don't remember off the top of my head, in the What's Next section, do you have, something talking about symbolication needing standardization?
Alexey A 00:32:33 No, not right now, that's a good point.
Felix Geisendörfer 00:32:35 I think that's an important one that we should mention in the blog post.
Alexey A 00:32:44 I'm adding a note to myself.
Ivo Anjo 00:32:50 Yeah, I see that we have the reference in the… yeah, we have in the hotel ecosystem section, and we have it in the what's Next.
Yeah.
Alexey A 00:33:01 Okay.
Ivo Anjo 00:33:03 I… the only thing is, like, is it too weird to be linking to the Google Docs? I think that's one of the advantages of having the PR as being, like, a more… Centralized, less off-to-the-side location to link people to, but.
Alexey A 00:33:22 I didn't see, APR for thread context. I couldn't find it.
Ivo Anjo 00:33:28 That's… yeah, that's the… that's the one we were kind of, that's the one.
Alexey A 00:33:32 Yeah, I would prefer… I would prefer to only have links to GitHub. I would prefer, like, not to link to Google Docs, but I… I think the only link I found was in your branch, and then I didn't want to link to your branch.
Ivo Anjo 00:33:45 Yeah.
Alexey A 00:33:46 But, yeah, if there's a better way to… yeah, just comment on the doc, feel free.
Felix Geisendörfer 00:33:52 Yeah, Ivo, why don't you just open the thread context one as a draft? This way, there's no pressure on people to review, but we have a link, and it's already out there, and it's kind of a nice halfway point between, like, waiting and going forward.
Ivo Anjo 00:34:10 Yeah, I think that, oh, I think that may be a reasonable middle term.
But yes, I will… I think, to kind of Florian's point, I do kind of agree with the… and that's why I've been kind of like, when are we ready? Are we not ready? I think I will open it as a draft, but I will try to kind of push on the process context and not bring this up.
Very widely, in the… in the other six, to see that… to see if we can land that one first, and then kind of start working on this one so that we don't try to muddle, things up.
Alexey A 00:34:47 I don't know if it's a good idea, but would it make sense to merge them? Like, would… is there benefit for people to just review both at the time, or is… does this become too big then?
Ivo Anjo 00:34:59 I think it's, it's a, I… I… like, we could, but I think it's easier to… to have them separately. That's why I've been trying to do it like this. But again, I… my guess, I don't think… it's like an informed guess. I have no data to back it up.
Christos Kalkanis 00:35:23 The process context is big enough already, I think. If we merge them, then we're risk delaying both of them significantly. Like, even if we get the process context in first, like, sooner, it's going to be a win.
Ivo Anjo 00:35:37 And I like that it's having the process context in, even though it's not the full solution, it kind of starts breaking the chicken and egg situation. Like, we learn that, then we start learning stuff, then we… so I think it kind of helps in getting the foot in the door, in a nice way.
Felix Geisendörfer 00:35:59 Yeah, sounds good to me, I think that makes sense to me as well.
Ivo Anjo 00:36:03 Thank you, I'll do that.
Felix Geisendörfer 00:36:05 And then I'll share the link with Alexa in particular, so that we'll have it on the… Ivo Anjo 00:36:10 Well, I'll update the, the, the, the… Felix Geisendörfer 00:36:12 Yeah, just make an edit suggests or something.
Ivo Anjo 00:36:14 Yeah, yep.
Felix Geisendörfer 00:36:15 Cool.
Okay, any more on this? If not, I think we have a bunch of things, including stuff from last time we didn't get to, so let's try to pick up pace a little bit.
Alexi, do you want to talk about other updates to the conformance checking? I assume you were busy with all those stuff, right?
Alexey A 00:36:38 No, it didn't. No updates on those two.
Felix Geisendörfer 00:36:41 Okay, that's easy. So, I haven't updated, I haven't raised the PR yet, but, I did create an issue on the roadmap for this, which is… Right here, so just for a refresher for what this is, when profiling goes alpha, we might still want to, at some point, make breaking changes, but it would kind of suck to, again, break every consumer of profiles, especially if we want more people to use it and get feedback. So, one thing we discussed with Josh at the last meeting was sending the OTLP version in the payload somehow. There are several ideas. Florian brought up a new one, which is we could use, and attributes that we could standardize in semantic conventions. Another way would be to put a dedicated field somewhere on the proto that says OTLP version. Another one would be to have an HTTP header or gRPC metadata for the OTLP version. But, the main thing is, like, it would somehow have to yeah, be something that the collector could receive, or a backend could receive, in order to potentially make transformations. Like, if it sees an older version of the profiling signal, and it knows that the data structures have changed in the latest version, it can deal with the old data.
Differently, and still make it work, whereas otherwise we might not be able to do such things.
So this, I think, right now is in discussion stage, and I think I will spend some more time thinking about this, and coming up with what I think is the best solution. Right now, I'm unsure, just exploring right now, I would say.
Yeah, I don't know if anybody has thoughts on that, but I've just said issue.
Yep.
Alexey A 00:38:30 We… probably don't want to have full design discussion, and I should rather leave this as a comment. But the one complication I could see, if there is, like, a pipeline of, players who update the profile with some information, then what version you capture. I wonder if this… if this can be a challenge at any… Like, for example, if, like, a collector… if there's, like, this initial producer that produces the profile, but then there's a collector that also has its own view of the OTLP version, I don't know if this could be kind of like a challenge, if… basically, if information is added incrementally.
Felix Geisendörfer 00:39:08 Yeah, I think one challenge there is if, like, something would just transparently carry it forward, like an attribute by default, I think, would just flow through the pipeline, which is maybe an argument against the attribute, because maybe the pipeline is actually changing the… data model, right? Like, you have an older eBPF profiler and a newer collector, and so the collector would do a conversion, or would be expected to do one.
So I think maybe it's really just a hint for the receiver side. Like, the receiver looks at it, and if it's, like, an older version, it just updates it to the new P data model, and from that point on, it's in the latest version.
But yeah, I don't know yet, is the answer, but… Christos Kalkanis 00:40:08 So, when I initially, raise the question about this.
the main problem we're trying to solve is we have clients that are on an older version connecting to the backend, and then we want to have a fast way, and also letting the clients know that what they're sending is not compatible with what the backend supports. So, mostly as an optimization.
So that we can quickly, shut them down without having to do expensive, validation, which we have to do regardless, though, right? Like, if we don't have that pathway to immediately close the connection client and return an error.
We have to do data validation also because, you know, versions can be faked, any client can send, you know, all sorts of garbage.
The validation layer on the backend has to be there if you're ingesting.
But if we do have versioning in place, then the backend can do a very fast version check, and just, you know, not go through the validation phase, and just immediately abort.
Felix Geisendörfer 00:41:16 Oh, interesting. I actually thought the problem statement was wider than that, not just rejecting payloads, it was about potentially doing convergence.
Christos Kalkanis 00:41:23 That's a good idea, yeah, it's just that, you know, from my… like, in my mind, with the… while we're still in alpha, and maybe even better, I wouldn't want to spend resources to do something like what you described. Obviously, if someone has the resources to spend, it's a nice feature.
Felix Geisendörfer 00:41:41 Yeah.
Yeah, let's continue hashing it out. I think for today's meeting, we don't need to spend more cycles here, but we can bring it up once we have more bandwidth again, and see where we land. And of course, async conversations appreciated on the issue.
But yeah, thanks. Unless somebody has a strong thought, I would move us to the next one.
Which I think, actually, those we've covered already, right?
Christos Kalkanis 00:42:07 Yeah, yeah, yeah.
Felix Geisendörfer 00:42:08 So I'll just drop these right now.
And, okay, cool, then we have made it through the backlog, and have Frederick's, discussion point from, the last meeting that we didn't get to.
Frederic Branczyk 00:42:23 Yeah, I mean, this is a quick one, and if the answer is we don't want to change anything anymore this, close to the… To the alpha, that's fine as well, but we were adding support for source maps, and it kind of made us pause that column and line numbers, you know, are signed integers.
Which doesn't make sense to us. I would agree with Alexei's comment, that, you know, it doesn't really matter, like, the bit width doesn't matter, because they're variant, encoded.
But, yeah, just curious what people think about that.
Alexey A 00:43:05 Yeah, it's also… it's also in Proprof, it's 64-bit, so one argument is, like, for round-trip conversion, it's just, like, reducing the bitness doesn't feel exciting, and adds the headache of, like, oh, what to do if, like… I doubt that's… Well, I don't know, because there's many people who use PProf profiles in all kinds of ways.
But my guess would be that at least, like, for the users that I know about, it should be, like, very unlikely you have more than 2 gigs of offline numbers.
Frederic Branczyk 00:43:39 I think column, I can make a case for, right? Like, column, if there's, like, some minified JavaScript thing. It's still crazy that it's 4GB, but, you know, I can… Alexey A 00:43:51 Yeah.
Frederic Branczyk 00:43:52 Potentially see that happening.
Yeah.
Alexey A 00:43:57 And also, for Dwarf, for example, I think, like, in Dwarf 64, technically, you also, like, at least, like, the business doesn't strictly… And of course, like, Dwarf is just one of debug information formats, but at least, like, I think in Dwarf 64, I can check, but I think line numbers and column numbers are also 64-bit.
So… Frederic Branczyk 00:44:20 Yeah, I guess I'm less, I'm less worried about the width than… and, you know, I'm not worried about the one bit missing in terms of, you know, sizes that we can represent. It's more about what do we communicate to people who read the spec with this.
If we allow them to be signed.
Felix Geisendörfer 00:44:46 We communicate with them that we have not thought this through as much as we would like theft.
Now there's an ex… now there's an exciting opportunity for you to come up with a use case for negative numbers, and your reader.
Frederic Branczyk 00:44:58 We could not, that's why I brought this up.
Felix Geisendörfer 00:45:03 Yeah, I would say that's something we could consider, like, tweaking, like, to an unsigned integer as we go to, to better, could be one of the changes we still make. I don't think it's a reasonable change to make for the alpha now.
Frederic Branczyk 00:45:20 Agreed.
Felix Geisendörfer 00:45:21 And then I think we should do another survey, like, I think Alexi brought up a good point about, like, looking at the ecosystem. What does Prov do? What does PProv do? And, like, if everybody does signed integers, then we can justify it, I think, just for round-trip compatibility. If there is a lot of mix, like, some people do unsigned, then maybe we should do the right thing here, which probably would be unsigned, in my… Frederic Branczyk 00:45:40 Yeah, the other reason why I wanted to bring it up is because there are several instances where we did make this change, going from PPROF to OTLP profiling, and so… So, like, I want to say, if I remember correctly, duration, for example.
was assigned integer in PProf, and isn't anymore in… Otlp profiling, so… .
Alexey A 00:46:09 Yeah, I think… I think changing sign to unsigned makes sense. I'm like, for the bitness, I would reserve… I would just, like.
Frederic Branczyk 00:46:15 I agree.
Alexey A 00:46:15 the wider, but yeah, I think making it unsigned, I think it, yeah, it makes sense to consider.
Felix Geisendörfer 00:46:23 Okay, who's first, Christos?
Christos Kalkanis 00:46:26 If I remember correctly, Jonathan wasn't the one reason that we switched to unsigned, to Java, to Shine, sorry, Shine 64-bit, because Java SDK.
Jonathan Halliday (IBM) 00:46:39 For array indexes, the problem is… I've only got 32-bit arrays in Java.
So anything that's an index into the dictionary tables, we… we changed.
Christos Kalkanis 00:46:50 So wouldn't this be a problem for Java SDK that wants to… Produce, column numbers.
Jonathan Halliday (IBM) 00:46:58 That's not an index into anything, it's a standalone value.
Christos Kalkanis 00:47:02 Okay.
Just a second.
Jonathan Halliday (IBM) 00:47:04 There's no point at which you're going to take that value and try to use it as an array index.
I mean, it's a problem in the Java… Just has signed values, not unsigned ones.
So… Yeah, if you want to… render it properly, you're gonna probably have to convert it to, you know, big integer, but there.
That's… that's more of a problem for… for front ends than it is for, java itself.
Florian Lehner 00:47:40 That's.
Felix Geisendörfer 00:47:40 join.
Florian Lehner 00:47:41 maybe, just as a side note, in, in OTEL, and in particular OTTL, so the transformation language inside, hotel.
every number is int64. So if you use int8, It will be in 64 anyway, so… at the moment, this is really, really convenient that we just use the same Unless it's, some kind of timestamp, then it's time-time.orgl.
Felix Geisendörfer 00:48:12 So it's never unsigned in OTTL.
Florian Lehner 00:48:15 Nope.
Felix Geisendörfer 00:48:20 Okay, good to know.
Right, so in the worst case, we could actually produce a number that would not be representable in OTL.
That would be a pretty big bylaw. Is this something we need to… Frederic Branczyk 00:48:37 Review for other things?
Felix Geisendörfer 00:48:46 I think it's mostly if we have unsigned 64 in somewhere, do we?
I don't seem to recall we did, right?
Christos Kalkanis 00:49:17 Duration is currently unsigned 64.
Florian Lehner 00:49:22 Okay, duration is, some kind of time-related, so that's a different representation in OTTL, at least.
Felix Geisendörfer 00:49:30 Yeah, I was just gonna say file offset, memory limit, and memory start.
Frederic Branczyk 00:49:40 I'd like to see… A machine that produces this, but… Oh, address… interesting.
I think there can be some funky, like, kernel stuff.
Where the… First bit is sent, no.
Felix Geisendörfer 00:50:04 Yeah, I mean, I don't know, address randomization or whatever crazy stuff is happening these days.
Frederic Branczyk 00:50:12 That's not… Great.
Felix Geisendörfer 00:50:19 I think we should create an item to look into this. I think we also can, like, sort of brush it aside for the alpha, but I think this is worth considering.
Take a note here for the post-alpha. Where's my issues?
Awesome.
Okay.
Okay, that's good. Let's keep track of this and see if we need to make a change staff, but… I think more likely than not, like, we cannot change what, like.
data the operating system wants to give us, so, OTL… we might have to talk to the OTL people instead.
I think we should bring that up with them early, if we can.
Okay, any more thoughts on this?
Going once… I think twice, and ivo had another one here… Ivo Anjo 00:52:12 Oh, no, this is the one we already discussed.
Felix Geisendörfer 00:52:16 Oh, we did discuss this already? Okay, then I'm gonna scratch this. Oops.
Florian Lehner 00:52:20 Maybe, Dr. Sorry to interrupt, maybe a question. Should we turn the process context PR on the UPF profiler from draft into… into ready for review?
Personally, I don't expect, OTEP to change that much anymore.
And if so, we can still adapt. But at the moment, it feels like, hey, should I look into this draft? Should I spend time for it? Or, what's the stage for the expectations?
Ivo Anjo 00:52:55 Okay, yes, okay, I understand. I think we're in good shape. Let me double-check with my colleague, Nicola, and I will… if everything is okay, I'll ask him to mark it as non-drive.
Florian Lehner 00:53:12 I don't know how Christus or Felix feel about this, but I think it would be nice To at least land the process one.
don't have to maintain order backlog, and don't know, hey, it's draft, should I look at the draft, should I don't spend the… Will not… maybe not happen today, maybe not tomorrow, but .
Felix Geisendörfer 00:53:33 I think it would be nice to have it. I mean, I think we all agree that we want that functionality, right? And we're trying to convince the TC and others to adopt what we're proposing. Showing a working implementation is always good, I guess.
We, I mean, we could change it again, like, if there's changes, but probably not. So, I think, yeah, why not?
Christos Kalkanis 00:53:54 Yeah, the process context is important to us. I think… I'm not sure if we should merge it before the old tip is accepted.
that would also set the precedent, like in the EBF Profiler repository, we've had something similar come out before, so I would wait until the OTEP is accepted before merging the pull request in the profiler, but we can certainly review it whenever Evo feels it's ready.
Ivo Anjo 00:54:21 Sounds like a plan?
Felix Geisendörfer 00:54:25 Yeah, I mean, I'll leave it to you to decide when to merge, but, like, yeah, I think starting with looking into the code more and reviewing it probably makes sense.
Cool.
Then, I think we're almost at the end of our agenda. Alexi had one about marking this OTAP as deprecated. I guess this was our early, like, profile data model, thing.
Alexey A 00:54:52 Yeah, I was curious, like, what people do to all the apps, like, should there be, like, a banner at the top? This is, like, this is old, don't… don't study it, or… or no?
Felix Geisendörfer 00:55:05 Hmm.
Does it have a date? No, it doesn't have a date or something.
Are these OTAPs just in this repository, or are they published on some website somewhere?
Alexey A 00:55:17 I found it just here, I don't know if it's published anywhere.
Damien Mathieu 00:55:21 They are not published on the website, only specifications are.
Christos Kalkanis 00:55:25 I do have a link to it from the pull request that's currently in review in the specification page, and I actually added the commenter, but I wasn't sure if I should add a link to this first iteration of the data model, maybe because people get confused and think it's the actual one or the current one.
So I think once we… I have the data, the current data model in place.
I'll either remove the link to the OTAP, or advocate market deprecated, both in the OTEP and in the specification phase.
Felix Geisendörfer 00:55:59 Yep.
Honestly, I think it couldn't hurt to, like, mark it as deprecated, so I would just suggest to raise a pull request, post it, and see if you can get a review on it. If not, it's also not the end of the world. I don't know what the process is, but I think somebody from the TC needs to decide that, not us, probably.
It's a lack of a reply.
I don't care about it that much, or… Alexey A 00:56:35 And also, in the new world, maybe it's useful if LLMs see that it's deprecated.
Felix Geisendörfer 00:56:41 Oh, do we want to help them? Are we on their side?
That's… we should… Alexey A 00:56:46 People still… people still use them.
Felix Geisendörfer 00:56:48 Sure, but we want to have advantages over those people, don't we?
No, just kidding. Yeah, no, I think it would be nice to mark it as deprecated, so if you want to send a pull request, but again, I think somebody from the TC has to say if OTEPs are updated after the fact, or if they're sort of, like, just meant as historical documents anyway. I think that's probably the case, I would.
Jonathan Halliday (IBM) 00:57:10 Yeah, I think… I think there's a life cycle for withdrawing or rejecting them.
Felix Geisendörfer 00:57:15 this one.
Jonathan Halliday (IBM) 00:57:16 Let's see, there's a… there's a lifecycle thing that allows for withdrawing Rejecting a proposal.
So I think this one's probably withdrawn as… Being replaced by the the actual one.
Let's see if I can find it… Felix Geisendörfer 00:57:36 Okay, that could be interesting.
We take it back, we didn't mean it, we don't want profiling.
Alexey A 00:57:43 Yeah, withdrawn sounds, like, too dramatic to my taste, I don't know, like, superseded is maybe, like, something that I would kind of, like.
But, yeah.
Felix Geisendörfer 00:57:54 Huh.
Alexey A 00:57:55 Whatever… whatever the process is.
Felix Geisendörfer 00:57:57 The last KubeCon presentation that I did with Damien was on April 1st, and the opening joke from Damien was actually that we changed our mind profiling. Who needs that? We're stopping.
Damien Mathieu 00:58:10 And we were the only ones to do an April school of the day.
Felix Geisendörfer 00:58:15 That, I can't believe, that's crazy.
But this time it's March 26th, no chance to do it again.
Alexey A 00:58:23 People got too serious.
Felix Geisendörfer 00:58:26 Yeah.
Damien Mathieu 00:58:29 Or they didn't appreciate our joke, and so we changed the coupon date because of us.
Felix Geisendörfer 00:58:35 No, I mean, I think it landed with the audience, okay, Charleston has the link.
Okay, do we cross this page when it says the repository was archived?
Seems like the repo was withdrawn.
Florian Lehner 00:59:11 I think for us, the point, implementing the OTAB is the important one, and especially the last one, when the OTEP moves into the specification.
And the specification is the most up-to-date for us, I think.
But specification lives now the same.
repository as OTEPs.
Alexey A 00:59:47 Maybe we can also take a look at some older OTAPs that are also, like, likely to be superseded or obsolete and see if people add anything.
Maybe there is some kind of convention that exists in place.
Felix Geisendörfer 01:00:01 I think the simplest thing is honestly to fire a Slack message at, like, Tigran and Josh, and just see if they have an opinion, and if they do, we can do it. If not, then we don't. I don't think it's terribly important.
Will you maybe ping them, Alexi?
Alexey A 01:00:18 Yeah, I can take an action right now.
Felix Geisendörfer 01:00:25 Of course.
All right, then, I think that finishes us right on time. Thank you, everybody, for all the work, leading up to the Alpha. It seems like we're… Just before the finish line now, so that's all, send our, best thoughts and wipes to make sure this continues staying on track, and the TC review happens, but, yeah, it would be very exciting, and I hope to see, some of you. Who else is coming to… I know Florian's going to Cuban. Are you going again, Damien? Awesome.
Yeah, so, looking forward to seeing anybody who's gonna be there.
Ivo Anjo 01:01:04 Enjoy Amsterdam!
Felix Geisendörfer 01:01:06 Will do.
All right, then, thank you everybody, and have a nice local time.
Florian Lehner 01:01:13 Dear.
