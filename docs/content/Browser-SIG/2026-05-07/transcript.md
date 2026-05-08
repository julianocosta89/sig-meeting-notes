SIG: Browser SIG
Date: 2026-05-07
Duration: 33 minutes
============================================================

## Zoom Recording Transcript

**Jared Freeze** 01:30 Hey, everybody.
**martinkuba** 01:32 Hey, how's it going?
Joaquin and Jared, do you have anything that you want to talk about today?
Nothing specifically.
**Jared Freeze** 02:39 No, not really. I think we have a good amount of tickets for migrations.
So, I was thinking maybe we mark those as good first ticket?
because they're kind of copy-paste? Like, I don't know. I was reading in another repo that you know, they were getting praised for having, like, good tags, and I was like, oh, maybe we should start doing more.
labels, you know. That, that, honestly, was really it. Otherwise, Just cranking through… I did some stuff in Core Repo.
But, yeah.
one announcement, I guess, would just be that, It looks like Protobuff is coming out.
of JS Core.
Which is cool. So… it means that a lot of the Webpack consumers, like, there's been a lot of unevenness You know, over the last… you know, 6 months, where we've been recommending, like, to use, you know, use a hotel for web, but certain bundlers were having warnings, and they were, you know, we had that, ticket filed from Cloudflare?
I think, somebody like that, that was doing server-side SSR stuff. So, Mark is replacing it fully, and it looks like it's really close to being merged. So, that's kinda… that's kinda nice. So, also take a dependency away, which is always good.
But yeah, other than that, I don't really have anything official.
**martinkuba** 04:08 Sorry, I missed how is it affecting… the browser…
**Jared Freeze** 04:14 Whenever you import OTLP Transformer.
certain bundlers will tree shake out protobuf, the protobuf serializer, but it statically walks the tree to figure out what to tree shake, and it's like, hey, you're using Node APIs.
you know, this is… it's not… it's not browser-friendly, and then wound up tree-shaking at the end anyways. So, it's really just those warnings are gonna quiet down for everybody.
**martinkuba** 04:43 Okay, okay.
**Jared Freeze** 04:44 Yeah, that's the idea.
**martinkuba** 04:53 Alright, well, I… I have just… I have one topic, it's mostly… Just, for awareness, but I also wanted to, like, see, like, if any of you have any questions or, you know, or thoughts on this. I'm gonna share my screen really quick.
Alright, sorry about that. Okay, so… So I'm… well, one thing that I've been kind of thinking about for a long time is the… the entities… I don't know how they fit in into our model, data model.
Modeling sessions and page views, as, as entities, and this is, like, kind of the main reason that I wanted to, work on the demo, the prototype demo, so that we could Gonna show, the entities, SIG.
How we are planning to… to approach this?
And then, once they give us the thumbs up, I think we should go to the spec, and… You know, show the sh… you know, kind of demo it there.
And, see if there's anything… we need to do in the spec. But anyway, for… So I opened this discussion. Thanks, thanks, Joaquin, for… for taking a look at it.
And… I also… Worked on adding… adding support for the entities to the prototype.
to our demo, so I opened a pull request yesterday, Which is, this one.
So, yeah, this is not going to main, this is going to the prototype demo branch, so it's like we can… I don't, you know, it doesn't have to be, like, thorough here. I excluded all the tests, and… and it's not, like, super… Finalized, but just to, like, show the idea here.
essentially, for, I think, for logs, for events, which is most of what we do right now.
It should not be that difficult. So what I'm doing here is… I have… This… So, by the way, I kind of prototyped the… just, like, the initialized SDK, just to see… just to show that… how it would be put together in one place, but… but essentially, there is, behind the scenes, the SDK would create this… use this entity-aware blogger provider, which is like a proxy pattern.
And it has the… The provider has a setEntity method on it, so… and every time you set an entity, like, it rebuilds, The resource, like, merges the resource from what it already has, and with the new entity, and then it creates a new logger provider behind the scenes that this one delegates to.
So, you know, any instrumentation that gets logged through the global, through this global logger provider, we just get it through here, which would delegate to the one that's kind of, held under the scene. And then, you would have… We have the session manager, and we have, we would have to figure out some way to, to manage the session for the document, for the page view document URL.
For the, for the session management, like, if you look at the, the SDK here… It's, so it's using the session manager that we already have, and it's just, like, you know, once the… when the session, rotates, like, when it started, then it just, you know, creates a new session entity here, and then it calls set entity on the logger provider.
And the same thing is happening for the document. Like, I don't really know how, at this point, how to, you know, where exactly this would fit.
For the document tracking.
But for now, I just created this document tracker class that does kind of similar thing as the session manager.
No, I think, Maxime had, had, has the, draft instrumentation open for… for managing the document entity, but I don't think it's… it should be an instrumentation, but that's TBD.
But in any way, I think this kind of shows One… the, like, one way to do it, if you have, like, other ideas how to handle this, like, I'd be, you know, open to discussing it, like, we can discuss it either on, you know, here on this issue, or on the PR.
Yeah.
Any thoughts or comments on this so far?
**Santosh** 10:30 Hey, Martin, some basic questions, if you don't mind.
So the… the… the motivation for doing this is, like, resources were, immutable, and therefore we wanted, To use entities, and entities, if they also end up… Getting merged into resource.
How do you… Like, how does the spec allow for modification of the resource? In this case.
**martinkuba** 11:02 Yeah.
So it doesn't, right? I mean, that's the whole thing, like, the… This is kind of just a workaround around this, like, it's, But they, like, in the spec, they, they recently, merged this, four-entity method, I don't think I'm gonna find it.
It's this thing.
So, yeah, this was merged in the spec, which essentially allows you to do things like this here. Like, you have an existing provider, and that provider is going to have a four-entity method.
Which essentially creates a new… Instance of the provider, but with this entity merged into the resource.
So that, this… so my… this is basically… the idea is based on this, essentially. Is that, like, you know, we have this, this kind of proxy provider that doesn't actually hold the resource itself, but it uses, you know, a delegate provider behind the scenes, and that delegate provider can be swapped. So…
**Santosh** 12:17 And that can take on… Additional attributes.
**martinkuba** 12:21 Yeah, yeah.
**Santosh** 12:22 Via entity.
**martinkuba** 12:23 Yeah.
So, yeah, essentially, if you called setEntity… Like, look at 3 bills.
**Santosh** 12:32 Wider APIs are being extended to… allow for…
**martinkuba** 12:40 Yeah, I mean, this is the part that I think we'll need to, like, show, like, why we… why this is not good enough for us.
Because, like, we… we need… we need… when we… when the entity changes for us, like, we need it to apply to everyone, to all the instrumentations, not just one place in the code, like, this… what this would be doing.
So, like, once we have the use case and we have a demo, end-to-end demo, I would like to take it to the spec and get feedback there.
Like, I don't know, like, if we could just go forward, but, like, with this in the SDK and make it just, like, browser-specific, or, like, if they would require us to do something in the spec.
**Joaquín Díaz** 13:26 So, the spec right now allows for entity, but it doesn't have anything with, like, set entity, which… what you're doing here?
**martinkuba** 13:35 Yeah.
**Joaquín Díaz** 13:38 Yeah, I agree, I think… we need something like that, because otherwise it's complicated for us.
Having to define, like, doing four entity everywhere.
Every time that it changes, which is quite often for us.
**martinkuba** 13:55 Yeah. So… I think, like, what I have here, like, is not that complicated for logger provider.
It gets a little bit more complicated for… for sessions, sorry, for metrics, which I described in this, in this issue as well.
And it's mostly because… The resource is actually part of the series, like, metric series identity per spec.
So it might have some implications on the back end, but I'm not 100% sure on this. But I just wanted to call out in this discussion here, but I think, for now.
Like, we're not… we don't have any instrumentations that generate metrics, and… I don't, you know, like, I think we're not planning to implement any at this point, so… in my opinion, that's… that's, like, a secondary thing that needs to be resolved. If we can resolve it for logs and traces, then I think that's, in my opinion, possible with this… with this approach, and I think we could, just get, like, the okay from From the rest of the… From other SIGs, yeah.
**Joaquín Díaz** 15:12 When… so, on the spec, when you use foreign entity, is that just… Using that as a resource internally, the same as you're doing?
Or is… Like, I guess my question is, like, in the payload.
Entities are separated, or are they just resources?
**martinkuba** 15:37 In the payload, they're just resources.
**Joaquín Díaz** 15:41 Okay, so… Like, while you're doing… Makes sense in a way that… It's… the output is the same as using four entities, just a quick way for us to set in them.
**martinkuba** 15:54 Yeah.
**Santosh** 15:57 I think it allows that, that, that, that four entity approach allows different resources in the same SDK.
I think that seems to be the motivation there.
**martinkuba** 16:10 Yeah, it allows you to basically…
**Santosh** 16:11 necessarily modify You know, the entity… For a, you know, once… for a given resource instance, once it's, created.
And that's what you are trying to do.
**martinkuba** 16:24 Yeah, essentially. And I think it's essentially, like, the… I think the… immutability of the resource, like, has to do, like, with what spec says about the providers, about the SDK.
And, like, they essentially got around it by saying, okay, well, you can't change the resource for an existing provider.
Let's just, like… Fork a new instance, a new provider that has You know, that has a new resource, essentially.
Which is, like, what this… what this prototype does as well, so… Yeah. Okay, Yeah, please take a look at this, look at this prototype, you know, I think we can… if you agree with this approach in general, I think we can probably merge it without getting into too much details. It's just going to the demo branch, so… you know, I think if you have agreement on this approach, then I can then take the demo and… show it in the entities, SIG and in the spec SIG.
So please, please take a look at it.
Cool, okay.
**Santosh** 17:43 So what are you, expecting from the, spec sync? Is it the… Requirement, or are you also Asking them to… review the APIs.
you're introducing.
It's more of the first one, right? I think as long as they are hints that this requirement is valid.
**martinkuba** 18:04 Yeah.
**Santosh** 18:04 That's the first step, yeah.
**martinkuba** 18:06 Yeah.
Yeah, I mean, I… essentially, they don't really… my understanding is that, like, they don't really know, like, what we're thinking.
as a SIG, you know how we are thinking of solving this, and… You know, the four entity, Method that they worked on was partially motivated by, you know, to solve the problem for us.
But it doesn't solve the problem for us, so we need to show why. I don't know, like, if they would then say, this, what you have is good enough, you know, go ahead, or, like, if you need to actually modify the spec.
**Santosh** 18:42 Yeah, actually, I, I just remembered, many years ago, you know, in one of the discussions, on this topic, I brought up an example, where this might be relevant to.
the backend, situations too, so let's say there is a service that is emitting telemetry, and then that service state could change. So let's say in a Kubernetes pod, it could, you know, it could be under memory pressure, its state could change, and that modified state will be good to reflect in the In the… in the resource.
So, I think it'll be helpful to identify some valid… You know, use cases.
For the backend, too, because that crowd understands the backend concepts much more easily than… than the browser.
And the client world.
**martinkuba** 19:41 Yeah, I think there was… I think there was a use case described in that, in that OTEP, But I'll have to… I'll have to find it.
- Yeah, audio.
Okay.
there is… I think there is a use case of, The one I was thinking is that there may be some delayed resources.
not going to start up. Like, you… when you initially start up, you may not have all the resources available. They will… they will be resolved a little bit later.
I think that's one of the use cases for it.
For the backend.
**Santosh** 20:47 Yeah, and there, you know, this applies, right? Your… Your solution would be helpful there.
**martinkuba** 20:54 Yeah.
Cool, okay, anything else?
You've got 10 minutes, like, should we, should we look at the board and see?
See what we have.
**Jared Freeze** 21:13 Yeah, that's a good idea.
I was wondering, is this overlapped with David's PRs, by any chance? For the SDK?
Is… is that… Is there any overlap there, or am I misleading notes?
**martinkuba** 21:31 There is, so I included the… yeah. I'm not… I'm not, like, taking that away from you, David. I just wanted to, like, show… show, like, how it would work together with the SDK, because there's, like, some plumbing that he needs to do between, the logger provider and, like, the session manager, so… like, I kind of envision that to be part of the SDK.
Hold on.
**David Luna Bistuer** 21:58 I'm fine.
**martinkuba** 22:08 Actually… Can just use, Okay, so this is what we have.
I think this PR from Maxime… We had some UN… UN… Jared, you and I had some… requests, so he just needs to make those changes, but otherwise it looks, I think, good.
And then we have these three draft ones. This one… also from Maxime, like, I… that's the one for capturing document URL, like, I think he prototyped it as an instrumentation, and Yeah, that's what I was saying. I don't think it should be instrumentation, but I'm not 100% sure on this, We also have the, the navigation instrumentation?
So, there would be some… there's some overlap.
So, basically, they're tracking the same thing. One is just generating events, one is managing the entity.
So that's something that needs to be resolved, and I don't have an answer on this one yet.
**Joaquín Díaz** 23:44 So, this… Like, eventually, we will have an entity.
But you're all right.
where, I guess, where will something that sets NGTs live? Like, is that an instrumentation, or is that something else?
**martinkuba** 24:02 Yeah, that's the question, I don't know.
I don't know if it's gonna be a different… different concept, like… like resource detector, maybe? You know, something similar to the resource detector.
**Joaquín Díaz** 24:14 Yep.
**martinkuba** 24:15 No.
**Joaquín Díaz** 24:18 I mean, technically it's not… creating a new telemetry, so at least we know it shouldn't be an instrumentation, but I guess we don't know what… why it shouldn't be.
**martinkuba** 24:32 Yeah, I don't know. I thought the instrumentation, like, is really just… for managing… For generating telemetry, not for managing resources, but, yeah.
I mean… The browser package… David, do you need anything here? Like, or just… are you just looking for review?
**David Luna Bistuer** 24:56 Well… Mmm… Maybe if you have a question that I should keep adding… if… That may be… so now it's, it's browser. I remember from the, from a previous issue that we have, talking about how to release.
We were discussing about, there is something that we call the SDK package that contains SDK components and the building blocks to… to create SDKs.
And to create, instrumental applications, and the other one that is a distro.
I would… ask you what's your opinion about this package, if it's becoming a distro, or maybe it should stay as an SDK or something like that.
But do you think we should aim first for the SDK and then go for the distro one?
Because the scope is different, so I guess SDK, it's smaller.
Just providing the, the components that, that conform the SDK, the different SDKs, and then the distro.
what we call distro, what we could call… could call distro, it's, it's… the scope is wider.
So, what do you think?
**martinkuba** 26:13 So I think originally we discussed this… we discussed this a while ago, and… I think originally I was in favor of having a separate package for the SDK and a separate package for the distro.
But I think, Jared, like, you wanted… you thought it would be better if you just have, like, one browser package that's, like, the… that kind of serves both purposes?
**Jared Freeze** 26:36 Yeah, I mean, I thought it would be easier because… You know, it makes it a lot safer for everybody to use utilities and things, like, across the two, and to have the versions in sync, because some of the feedback we initially got was.
nobody knows what instrumentation goes with what, right? Because it's, like, 0.46.0, and that works with 0.216, and then there's other things at 1.0. So, it was sort of to solve that problem, and just, like I said, to make it more convenient for everybody just To have code across… You know, across the repo, just works, right, when we release.
that… that was how it started. And when you say distro, what do you… how is that different than the SDK? What do you mean by that?
**David Luna Bistuer** 27:25 Maybe, maybe the distro also provides some, Receipts, let's say, let's say it that way, so receipts or some… things that are actually going in this together, I don't know, maybe giving some patterns or something that it's easier to… For the user, just to… You know, build up, an instrument in their applications.
At least in Elastic, what we… in our sense, what you call it, is just a rubber, and it's just, you know, we just expose a small function.
that gets the configuration object, and then you have everything. Here, I guess, that's not the target, because we want to control the bundle size, but, you know, okay, give me the configuration, maybe requires you to import some extra things, so make things happy for the bundlers.
But kind of the same, so… Try to make things… easier, as much as we can for users, so maybe… Having some code, or, or some, Implement some patterns that… that are, come handy to just to start up.
as soon as possible, an SDK, and start absorbing the application.
And maybe calling distro, that's… there is a definition, I think, in OpenTranity, what they call it is distro. It's a prop around a component, or a set of components.
So, should we call it this run?
Make this kind of, conformed to this specific… to this definition.
Or should be… Should this package be called something else?
Another disregard.
**Jared Freeze** 29:10 I mean, if you're talking about helpers, like, set up default instrumentation, right? Is that what you're suggesting? Something like that?
**David Luna Bistuer** 29:17 Hmm.
**Jared Freeze** 29:18 Like, the convenience stuff, or…
**David Luna Bistuer** 29:25 So…
**Joaquín Díaz** 29:25 I'm still striving to see the difference between this show and this.
But I… in any case, if there's a difference, I think we shouldn't have two, because that is also confusing, like, then you know which one to use, unless you know. I think, that we will have two specific kind of users, like, the users that are used to open sedent Entry, they can use instrumentation directly, or they can use the staff directly, and then people that are not, and those will use either this, what you call distro, or these RSCK functions.
And I think… If we're going to make it simple, we should just make it simple by having one, and if that one is a little bit more… heavy, then that's an option the user… they… that's something they have to decide, like.
If they want to set up things on their own, then they can do that using the packages directly, or if they don't want to do that, then they can use the little bit more heavier distro, whatever we call it.
**David Luna Bistuer** 30:36 Okay.
**martinkuba** 30:38 So my understanding, or my kind of… understanding of the difference was that, like, the SDK is just, like, the… the pieces that you put the distro together with.
Yeah, so yeah, like, you know, it's… like, the distro would be, like, our… our recommended configuration and set of… set of, instrumentations that, like, is ready to go.
But if someone wanted to, like, build their own distro that's, like, configured differently, has different instrumentations, they could use the different pieces from the SDK.
But then again, like, you can't just… you can just import specific things from the same package and have it… have the rest be shaken out. So…
**Jared Freeze** 31:25 Yeah, I think… Yeah, I mean, without, you know, we ban wildcards and things like that, so package size… You know, unless you're using a very old bundler, which doesn't even work with exports keys, mostly.
Tree shaking works really well these days. So, having multiple entry points for whatever people are interested in… OTLP transform is a great example, right? Where, in 3.0, the idea is to expose JSON serializer and expose the OTLP Or, excuse me, the Protobus serializer. Same idea here. I think we would have something like INIT SDK, which is, like, the easy one, and then maybe something like, you know.
set up default instrumentations. That can all live in the same package. I don't think that's really a concern. And then, we'll just have examples that show, you know, here's the easy way, you know, here's the… everything included, you know, and we have 5 recommended defaults. And then here, you know, an array, and you can just plug in whatever you feel like. That could even be the same… in the same internet SDK. That's actually how it works, in our SDK. So, yeah, you can do either one. I think the entry point I would probably use the same one. I would use a tel browser slash SDK, and then just have whatever special functions we're interested in.
That's what I would say. I don't think you need another one. And if you, you know.
Want to get more specific, maybe there's another… entry point, like, slash, you know, and then there's… there's more under it. Something more specific.
That's probably what I would recommend.
**David Luna Bistuer** 33:02 Okay, so… okay, I'll follow up on this, Vianna, I'm gonna work with, maybe… on the config, and provide some defaults, and then alternatives to actually override these defaults in a 3-shakable way. So, that would be my next step.
Okay, then I'll ping you on Slack, whenever it's… at least… well, not ready, because it's going to be big, but at least to… when I have enough to have another round of reviews.
Okay? And thank you for your time.
**martinkuba** 33:35 Thanks, David. Cool.
**Jared Freeze** 33:37 Thanks a lot.
**martinkuba** 33:38 Bread times, so… So, see you later.
**Jared Freeze** 33:41 Cheer.
**David Luna Bistuer** 33:41 Bye.
