SIG: Browser SIG
Date: 2026-04-23
Duration: 31 minutes
============================================================

## Zoom Recording Transcript

**Martin Kuba** 00:16 Alright, Jared.
**Jared Freeze** 00:18 Hey, how's it going?
**Martin Kuba** 00:21 I'm doing okay, how are you?
**Jared Freeze** 00:23 Nice. Good. Yeah, I'll let you lead today, since you have a full agenda.
**Martin Kuba** 00:29 I do.
**Jared Freeze** 00:29 I'll take the next one.
**Martin Kuba** 00:31 Okay, no worries.
**Jared Freeze** 00:34 I don't know why I'm so zoomed in. It's just… It's Mac.
There you go.
**Martin Kuba** 00:59 Alright, sir, B.
**Surbhi Agarwal** 01:02 Hello?
**Martin Kuba** 01:04 How are you?
**Surbhi Agarwal** 01:06 I'm doing good, how are you guys?
**Martin Kuba** 01:09 That's good.
**Surbhi Agarwal** 01:15 I wanted to chat about the… differences between mobile and browser. I came across something else. I would add it to the agenda. I am trying to fetch the docs.
**Martin Kuba** 01:30 Yeah, I actually have it on… I have the resource timing as the first item on the agenda, so we can talk about it at the same time.
**Surbhi Agarwal** 01:38 Okay.
**Jared Freeze** 01:41 I just posted a link for you. Shortcut.
**Surbhi Agarwal** 01:44 Yeah, got to it now.
**Maxime Quentin** 01:49 Hello?
**Martin Kuba** 01:51 Right there.
**Jared Freeze** 01:53 Hey, guys.
**Martin Kuba** 02:03 I guess we'll just, like, wait one more minute, I don't know if Ted is going to join.
**Jared Freeze** 02:55 Yes. Guess not.
**Martin Kuba** 02:57 Yeah, let's just get started. We can talk about the resource timing.
Let me shut my screen.
Okay, so I did want to talk about… I have, I have a bunch of things… On the agenda, hopefully they will not take too much time.
The first time… the first thing, this is the resource timing.
instrumentation and semantic conventions, we talked about it last week. There is that proposal from Serbi about… About the unified, semantic conventions, and… my… My concern is that it's gonna take… take some time, still to… to finalize the unified semantic conventions.
And right now it's, like, last week we talked about not waiting for that to finalize before we do a release.
I wanted to propose… That we just go ahead and do a release with the semantic conventions we have right now.
And… We can… we can update later, it's experimental, and… we can get some feedback, and maybe, maybe, like, one idea that, that Serbia and I had was that maybe we could… Ship that instrumentation with both sets of semantic conventions, and let users, You know, choose which ones to test, like, with using configuration, and get feedback from that.
All that to say, my proposal is, let's do a release.
With, the semantic conventions we have right now.
And just a… just a reminder what they are, Essentially, they're… they now align, like, I just merged, pr, thanks, Chaird, for approving it.
That basically aligns with, From Hector's… Hector's, PR.
So it has, the event… the event is called Browser… Browser… data resource timing, and all the attributes have the same namespace, browser, resource underscore timing, and then the field name that basically exactly matches what's in the resource timing API for web.
So, yeah.
Any, so any, if you ha- if you have any… Has, you know, if you have any concerns about this, let me know, but… I'm curious what your thoughts are.
**Jared Freeze** 06:00 So, are you saying if we were to ship both, what instrumentation would ship both? This one?
**Martin Kuba** 06:07 Yeah, so it would be the same instrumentation.
**Jared Freeze** 06:10 Okay.
**Martin Kuba** 06:10 It would have this set of semantic conventions.
Then, once… once we make a decision whether to go with the unified HTTP conventions or not, we can either replace it, or we can add it as an optional Said, you know, said that users can opt in into if they want to.
**Jared Freeze** 06:30 Gotcha.
I don't like the branching, just typically, because I feel like we should be leading and just, like, say what they are. I think being experimental and then having, like, a double set of experimental is a little bit confusing for people that are new.
**Martin Kuba** 06:47 Hmm.
**Jared Freeze** 06:48 That's my two cents, just as a general comment. And then real quick, Serbi, is this unified, what you were… gonna bring up later? Yeah. Like, using HTTP?
**Surbhi Agarwal** 07:00 Yeah, using the same conventions across mobile and browser, so… We discussed it before, right?
There are some differences, for sure, between browser and mobile, and we decided… we thought that we would document it nicely, so it's clear.
to the browser world as well, and to the mobile world as well.
there are these differences, right? One thing that I wanted to talk about today was also, in mobile, what happens is, when there is a redirect or a retry, those span instrumentations create different spans. They treat each of those as separate requests, because Sometimes URL can also change.
domain can also change, so DNS query happens again, right? So there is… all that data is… needs to be fetched again. So, like, similarly, the event needs to be… separate as well on each redirect retry, because the network timing data is available there. It has to be one-on-one with the request, whereas in browser, it looks like the retries are… handled differently.
like, Martin is… Showing here on the screen.
**Martin Kuba** 08:38 Yeah.
**Jared Freeze** 08:39 Okay, I see.
**Surbhi Agarwal** 08:41 This difference is also there.
So the span instrumentations in your case would create one span for this as well, right?
**Martin Kuba** 08:57 Yeah, so we have… I think we have… two separate instrumentations, one is for… for the resource timing events specifically, because that's just what… what the browser gives us, and then we have, like, fetch and XHR instrumentations that generate spans.
The fetch and XHR ones.
They don't link right now, those two instrumentations, The fetch and XHR obviously only apply to certain types of calls.
But they don't cover all of the network traffic from browser, which is why we need the resource timing one.
There's no other way to get information about all network traffic from browser, you know, aside from this API.
So… and we don't.
we don't… We basically just want to capture these as events.
Rather than spans. Because… because they can… those… if you capture them as spans, then they can't really link to any other spans.
Because they're… They would be, like, synth… they would be created after the fact, not as they're happening.
**Surbhi Agarwal** 10:13 Hmm?
Here, also, I think, like, browser treats it differently. The start time and the redirect start should be different, right? Like, the actual, if you think, the first call versus the final redirect call, there should be some difference, but it sort of treats the final request as the one that is being emitted by the browser API, probably.
**Martin Kuba** 10:41 Yeah.
**Surbhi Agarwal** 10:43 Yeah, in mobile, we capture all of them, and we add the HTTP request resend count.
As 0, 1, 2, like that, for each of those trials.
**Martin Kuba** 10:59 Okay.
**Surbhi Agarwal** 11:02 But I guess.
**Jared Freeze** 11:02 Okay.
**Surbhi Agarwal** 11:03 Yeah. Like, this is also not a big difference.
This can be documented, right, to clarify?
This is just the treatment, which is different in browser world and mobile world, right? So people are aware of it.
Yeah.
**Jared Freeze** 11:23 Okay, yeah, I think that's good enough to get started. I mean, if we can't get it, we can't get it, you know? I mean, we do our best with what the browser gives. I can test this, we have an example.
like, not in the browser repo, just a separate example, that I can add redirects to and just find out.
exactly what's going on, based on the instrumentation that's already there, because it's using OTEL.
libraries directly, not, like, recreations. So, we'll come back around to that, I think. But yeah, we can probably move on. We'll have to review this, there's a lot of information, I think, so…
**Surbhi Agarwal** 12:00 Yo.
Some other subtle differences, right? Like, there is, like… In mobile, we get a content length, which is what we put in the body size for request and response, whereas here, you have both the compressed and the decompressed sizes, and there are separate attributes that need to be defined for niche.
Some of these things that we need to figure out.
I can mention the open questions and tag the browser sick. Is there a handle to tag the entire browser sick?
**Jared Freeze** 12:43 Yeah, outbreak.
Top browser maintainers. Browser-maintainers.
**Surbhi Agarwal** 12:48 Okay, yeah, that makes sense. I will do that. I will… and you guys let me know what you guys think about that.
**Jared Freeze** 12:57 Cool.
**Surbhi Agarwal** 13:01 I also plan, maybe, to propose the basic conventions.
For now, and then we can enhance them further, right? To add the browser use case as well, until we are ready to do that. So mobile can also progress, right?
like, the generic ones that mobile uses, I'll try to propose semantic conventions. With that, I'll plan to come up with a PR sometime next two weeks.
**Martin Kuba** 13:34 Okay.
Yeah, thanks for… thanks for moving… moving that forward, yeah.
**Surbhi Agarwal** 13:42 Yeah, and we'll, enhance them as needed for browser use case as well.
**Martin Kuba** 13:51 Okay.
**Surbhi Agarwal** 13:55 That's all for my site today, yeah.
**Martin Kuba** 13:58 Okay, great.
I'm gonna move on just for the sake of time.
So the next thing that, is kind of related is the navigation timing.
And I have an open PR for this, also like to… Bring it more in line with the resource timing.
Because the semantic conventions that we have in this… in this instrumentation that's already out there, by the way, is… is completely different than anything else. Like, it has… it doesn't even have the browser prefix for… for any of the attributes.
It just has, like, navigation, which is also wrong, I think.
So… So my proposal here is to, make it consistent, like, with the other resource timing one.
And just, like, have it prefix browser, navigation underscore timing.
And then also, the other thing that I wanted to bring up is… Whether or not we should… have, Like, some of the attributes in the spec for navigation timing basically are inherited from the resource timing.
So, instead of having… instead of having, like, navigation timing, like, for example, fetch start.
I would… I'm proposing to have to reuse the resource standing one here.
Obviously, like, if we end up going with the… unified HTTP semantic conventions, that those would be different again.
Here, and, like, in this instrumentation also.
But, you know, but for now, this is what I'm proposing.
**Jared Freeze** 15:50 Yeah, I'm cool with approving this. This… I guess at this point, I would need to hear arguments against Unified.
You know what I mean? Because… You know, fetch start is fetch start.
like, it truly is one thing, so it seems weird to, like, extend one timing and then also be different than Unified, especially because it's in the HTTP namespace.
I believe as a vendor, we already do this. I think we use the HTTP namespace, and I believe I extended it. I'll have to review, but Yeah, that's my… that's my opinion. I think I'd need to hear, again, against using HTTP namespace for all this stuff when, you know, networking is general enough.
Regardless of what API it comes from.
**Martin Kuba** 16:39 Yeah, yeah, I mean, so I think the main counter-argument, or the main argument for using this set of conventions is that they… there is, like, one-to-one mapping to what the browser gives us. So, like, if you were… if you were a browser developer, and you were looking at resource timing data from the browser API, and, like, what we capture.
Then, like, you can see, like, one-on-one, you can see exactly that they're the same, and you can understand, like, exactly what they represent.
Whereas, like, when we… when we map them to the unified semantic conventions, that they're… you know, you have to kind of have, like, a map in your… in your mind, like, to see, like, what… what represents what.
And the, the other, the other… Argument is… that the data that we get from the browser API is relative timestamps to time origin, which is the beginning of the document load.
Whereas, I think what we'll need to do with the semantic… with the unified semantics, is calculate relative to the start of the call, to the HTTP call, so, like, the values… the values are going to be different as well.
**Jared Freeze** 17:50 Yeah, yeah, understood.
**Martin Kuba** 17:52 Yeah.
**Jared Freeze** 17:53 I'm… I'm okay with both of those, but yeah, we can… we can discuss more formally.
Third time.
**Martin Kuba** 18:03 Okay.
Next one, We have… We still have, this issue… Let's see… This issue that I opened a while ago… this migration of browser packages from Contrib and JS. There's, like, a bunch of packages that basically we have that are in different repos, and we want to move them over. So I started started by… by migrating this first one, the… the browser navigation instrumentation from Contrib. There is… The PR is open here.
So, this is a request for review. Please take a look at it. It's basically adding, Let's see… did I… yeah, it's basically adding, A new, new, like… Instrumentation to the, to the single instrumentation package.
Once this is merged, then… then I think we would, deprecate the, the NPM package for that instrumentation.
And remove it from… that code from contribib.
But this is just, like, one of… one of many that we'll have to do.
And I also added this sub-issue for moving the exception instrumentation from contrib.
Same thing. So, and this one is up for grabs. If anyone has cycles to work on this, that would be a lot of help.
**Jared Freeze** 19:59 Does anyone on this call want to take that?
It's okay if not.
Cool. We'll figure it out later.
**Martin Kuba** 20:13 The other, next topic, demo… So we have, I appreciate, like, a great, like, Maxime, thanks for your work on the, the sandbox. Also, Joaquin worked on the end-to-end demo, which is great.
I think the sandbox, I would… I think we should… we should just merge. I think that's very useful.
I think, Jared, you had some… some comments on that, right?
**Jared Freeze** 20:43 Just one thing left. So the code itself is solid, the lock file is greatly expanded, and it now includes metrics, and I just want to double-check what's coming in, because I would like not to have a release that just has extra stuff in it.
**Martin Kuba** 20:59 Just…
**Jared Freeze** 21:00 just gotta do one more once-over. I will do that today, so we can probably merge, later on, because, like I said, the… the content is fine, I just… these… the package, something's going on with the package, so…
**Martin Kuba** 21:13 Yeah, okay.
Yeah, I'll have one more look at this as well today.
And then… but then there's also the, the end-to-end demo, end-to-end demo that, Joaquin… Worked on… Here… And I think this is a great start, But, you know, I think there's more work that I would like to get… work on this, and… My question was… If you look at… if you… just a reminder that we have this discussion, this discussion, post that I… that I put out there a while ago that kind of summarizes the… our primary goal for the demo. And the primary goal was, we've been basically asked by, people from the spec, from TC, to, To be able to, demo, like, how we envisioned things working end-to-end.
This would be… this would include things like… how we capture sessions, how we capture the document URL, how we… do we plan to support metrics or not?
You know, is our proposal… if not, then is our proposal to generate metrics on the backend, and kind of demonstrate how that would work?
You know, so all these things, kind of end-to-end.
they don't have to be polished, it's basically just a demo, like, to, to show other people in the community. So my, my proposal here is, is to, Maybe not… not focused, that it's too polished at this point, but, But, and not, you know, not necessarily merge it to main, but have it on a separate branch that we can collaborate on and build this out, kind of end-to-end, how we envision that to be.
Yeah, I did create this… this branch, It's just this prototype branch that we could just merge things into, like, without doing, like, too much… too much, like, detailed reviews.
And… That would kind of allow us to be able to demo it to other people, and then we can pull things into the main branch as we think we would be helpful to our users.
Any objections about taking this approach?
**Maxime Quentin** 23:38 No, I like it. It will also be a good way to, kind of, poke at a QA, or way of, providing the session ID, and probably maybe, like, the browser document URL. Like you told me, we might start with the first, not a resource.
And then, an entity, and then migrate to the concept of resource.
I would like to help if needed. I'm not very sure how I will do that, but if I can use your demo environment to kind of poke an instrumentation for the browser URL, documentary URL… And maybe from that, we can have something to demo?
**Martin Kuba** 24:24 Yeah.
Yeah, that sounds good. Yeah, I think the session and the document URL are the big, big pieces that, like, we have to figure out how to… how to exactly handle it in… You know, like, we need to be able to demonstrate how it affects like, collecting different types of events as, like, sessions and documents and the URLs are changing.
And, like, you know, like, you were asking, Maxim, about, like, the instrumentation. I'm not sure, like, if… you know, if these are entities, then, like, there's, like, no precedent for this yet. Like, there's, like, no… as far as I know, there's no… Instrumentation or, like, mechanism to… to, like, generate these entity resource attributes, so something we need to figure out, and I was hoping we could do it in the demo.
Yeah.
Cool.
Maxim, did you want to talk about the next thing?
**Maxime Quentin** 25:31 Yeah, like, very quickly, with, Martin, we kind of, agreed on, the semantic, and before… I mean, I've already asked semantic a convention review, but just wanted to make sure, like, everyone were okay with the semantic.
For the browser document URL.fool.
It's my first contribution, so I like to the semantics, so I just wanted to make sure I did not do anything crazy.
If it was clear enough, if the notes I added about why we need an entity, separate entities, and the other one, like, everything. If you can have a look, and just let me know if I'm… Messed up something, or… Would be great.
**Martin Kuba** 26:22 So I think this looks good. I think my main thing was… like, where this attribute should go. I think it should go on an entity and become a resource attribute, but I think what's gonna probably happen is, like, as we… as we get someone from the semantic conventions to look at this, they'll… they'll say… they'll probably want us to, like, demonstrate that… how we envision That to work with as an entity.
**Maxime Quentin** 26:49 So…
**Martin Kuba** 26:50 Yeah, that's why I was kind of linking it to the demo as well.
**Maxime Quentin** 26:55 I mean, if we… if we succeed to merge a sandbox.
maybe we can have the sandbox in your demo, and I can work on a small processor or instrumentation that populates this entity, and we can come back to the CMT convention and showcase what happens when we generate several clicks after navigating or stuff like that.
and showcase that the browser URL mutated, and we need to change the entity and stuff like that.
**Martin Kuba** 27:24 Yeah, okay.
**Jared Freeze** 27:28 So, I have a question about entities. So, is it like a namespace? So, I see here, you have entity.browser.document. So, would the resource attribute be url.full, or do you include Like, is it really browser.document.url.full?
**Martin Kuba** 27:46 I think it's this, yeah.
**Jared Freeze** 27:52 Okay.
I'll have to read more about entities, I don't quite understand why you would have to do that.
Like, it's scoping within a scope already, But like I said, I'm new to this, so I'll read more about it.
**Martin Kuba** 28:10 Okay, yeah.
Okay.
We've got one more minute, This is, like, a request for review, Jared.
**Jared Freeze** 28:26 Yeah, so… Basically, there are, sites, I suppose it's at the site level. They're using object.freeze on fetch so that it can be tampered with by bots, etc. Malicious code.
Which means it cannot be patched, and Arcad doesn't really account for this. I think, David, you actually have a… you have something out for XHR, yeah. Okay, so, I would like to get yours in first. It has no impact on this bug. It's not really a bug, it's, like, kind of just… very strange behavior. It is fine. I do have an issue with this code.
Small one, which is that it sets enabled to true, even if it's not patched.
Which, to me, is… not specific enough. It's not enabled.
It's attempted, and it is… unsuccessful.
So, patched is false, for sure, but what is enabled?
you know, we don't really have this middle state of, like, I called Enable.
But it is not possible, so retrying is… Not needed or not wanted.
It kind of presents, you know, a different… situation. I mean, it's just something totally new, so… Not sure what exactly, but if other people have opinions, like, definitely check it out.
It is not enabled. I think that's the wrong word to use.
So…
**David Luna Bistuer** 30:04 Maybe then the name it's better to be active.
So, actually, it is enabled, it's a flag, they just use it to… If everything's, you know, if the patching is… the patching successfully, and then we are instrumenting, so we get the… we call fetch, then it goes through our batch version.
We are checking this enabled, this flag to actually decide if to create the span or not.
**Jared Freeze** 30:33 Okay.
**David Luna Bistuer** 30:34 Yeah, yeah, you're saying that, okay, if we are not… if we do not patch successfully, then we can say that the instrumentation is not enabled, right?
**Jared Freeze** 30:43 Yes.
**David Luna Bistuer** 30:45 Because it's words, naming things is hard, yeah. Okay, so maybe we can call it that the… maybe we can call it the instrumentation is active.
Or… well, but then it… you have the same, so you can have an API to activate or deactivate this notation.
And enable, disabled, so yeah, I don't know.
**Jared Freeze** 31:05 Well, I get… I mean, maybe… maybe just line 640… 643 just needs enabled false, and that's… We just live with it.
But anyways, yeah, you guys check it out. I know we're over on time, but…
**David Luna Bistuer** 31:24 Okay, we'll do it. Thank you.
**Martin Kuba** 31:26 Alright, sounds good. Thanks, everyone. See you next week.
**David Luna Bistuer** 31:32 That's good. Bye.
