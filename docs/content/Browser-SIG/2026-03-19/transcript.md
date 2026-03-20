SIG: Browser SIG
Date: 2026-03-19
Duration: 31 minutes
============================================================

## Zoom Recording Transcript

**Maxime Quentin** 01:36 Hello?
**Martin Kuba** 01:39 Hi, Maxim, how are you?
**Maxime Quentin** 01:41 Doing great, and you?
**Martin Kuba** 01:43 I'm doing fine.
**Jared Freeze** 02:30 Hey, everybody.
Hey, Dan, I was gonna ask you, do you work on… Web stuff, or mostly Node stuff?
Like, out… at work, or… Just curious.
**Daniel Dyla (Dynatrace)** 03:06 I mean, I guess… Currently.
Neither, is kind of the answer.
Okay. I mean, I'm working on, OpenTelemetry Node, obviously, or OpenTelemetry JS, which is both… But most of my professional experience is with Node, so that's just where my experience lies.
And, like.
agent development for server-side agents. I was never working on our RUM team or anything like that.
**Jared Freeze** 03:40 Oh, okay.
**Daniel Dyla (Dynatrace)** 03:41 in the past, some, you know, full stack. I've been on full-stack teams, but to be completely honest, the web half of that was never, my strong half.
**Jared Freeze** 03:56 Cool.
**Daniel Dyla (Dynatrace)** 04:00 And it was a long time ago.
**Jared Freeze** 04:39 Diggling.
But I think we're gonna run out of time, so I'll just save it for next week.
**Martin Kuba** 04:44 Yeah, let's, let's, let's get started.
Just a quick announcement to start with, Exciting, we had our first release last week.
We… Jared and I… Jared and I worked on it, and thanks to Mark for helping us with… Pushing things to NPM.
We're still trying to, Get the Reese process all ironed out, but but it's… it's, like, first… first Reese is out there, so… This includes the three instrumentations we have in this repo.
The second topic that I have is… Related to your Maxim, to your issue, Let me share my screen really quick.
So, I'm… I'm… my question is, like, are we okay to merge this? Like, so, basically, right now, the… The attribute is named browser page URL full.
Which I am okay with.
My, my only… question here, or a hesitation is, I'm not sure if this… belongs to… A browser entity.
Buds.
That's what I wanted to, that's what I wanted to discuss.
**Maxime Quentin** 06:27 I mean… My input is, like, the addition of the page and face makes sense.
Because you were mentioning, like, both are more, like, environment-oriented.
But I think Paige kind of makes it clear that, It also has another context, so… would make sense for me. Having app.page would also make sense for me, but no, it's not, like, super… Well, I mean, I don't know… I don't think it's well seen by mobile folks, because they… I don't think they consider, like, a web app as an app, so I don't know.
But whether that page, for me, looks good.
**Jared Freeze** 07:23 I would prefer not to have page, or app in these, only because that… like, you know, for, like, SaaS customers, like, they don't really call it Page.
Like, it's a document, but not really a page.
And then app… I think until we solve this kind of microservices issue, app could be, like, multiple in the same You know, do you pork.
So… browser.url.full, I think, makes a lot of sense, because it is a singleton. Now, it doesn't account for, like, iframes, but I would argue those are a different document. We kind of talked about this last time.
The reason I would do that also is, so, you just asked… In the chat.
if there's a splitter, that's already done for URL as a namespace, so there's, like, URL dot… route, url. All these other things that are done in the… when they did HTTP. So if we just prefix it with browser, I feel like that gives us ownership, and then we can do the URL parts, but… I guess I would want to hear, like, what else would go in page if we were to use that. So, like, browser.page.what else.
**Maxime Quentin** 08:42 Navigation, stuff like that could be useful, like, I would say, like, browser.page.navigation, or browser.page.
document, information.
I mean, the page namespace also brings some kind of room to add new stuff, so… I kind of like it, but I'm not blocked. I would also be happy with the browser.urr.fool, in a sense, like you say, we can provide a lot of other, like, we could provide the path directly in browser.url.path, or stuff like that.
I mean, we can enrich work, we can enrich URL, For me, everything makes sense.
**Joaquín Díaz** 09:34 I think once we add the page namespace, then it's hard to argue against like, everything may go into the page namespace, because in the browser, like, that's a top-level thing that is always there.
So Bye. Bye.
do we want to have something that is confusing in terms of, like, do I want… if I am adding something new.
to the browser, some of the conventions, like, I have to think about whether it goes to the page space or not, and I think that question is hard to answer, because everything may go there. Like, at all times, we have a page.
And everything belongs to the page.
The same as the Belancer, also.
That's my only concern, like… If we add beige as an expense here.
**Jared Freeze** 10:25 I think I thought of an example. So, like, right now there's, browser.resourcetiming.whatever.
that's been proposed, like, is that… would that go under page or not, right? Like, for that specific example.
**Martin Kuba** 10:45 Browser.resource timing, like, for the name of the event.
Or for you, like, for the attributes?
**Jared Freeze** 10:52 For attributes, yeah.
**Joaquín Díaz** 10:54 I mean, you can say that the resources belong to the page, because it's the page that is triggering the load of the resources, so that's… that's what I'm saying, is I… I don't know, maybe there's an argument where it doesn't belong to the page, but… I'm just saying, like.
if we add… if we start adding patients' names face, then we have to also think on all these new cases, whether we want to add page to other places as a name space.
**Martin Kuba** 11:24 Yeah, so… So the reason that I did suggest the page to add to the name is because it seems to me like the attribute, just browser URL.full is not… concrete enough? Like, you made… it doesn't really… communicate, like, what URL that is.
And the other attributes in the browser namespace right now are related to the… to the platform, not the context of the page.
And if you think… if you think of, like, resources having, like, a, you know, a set of entities, and the browser entity's gonna be, representing the platform.
does it make sense for URL to be part of the platform entity? Or would it make sense to have, like, a separate entity that represents the page context?
**Jared Freeze** 12:21 Yeah, and that's what I was just thinking as you're saying this, right? Like, browser.page doesn't make any sense in that model. Like, it would be page, right? Page.url.full. Because everything we do is browser, like, I think that would be a lot of overhead.
to just put browser in front of everything, because it's a differentiator. Like, if browser is an entity, I would argue that Page is a sibling to browser.
If we want to do it that way. The same way that, like, mobile uses app, right? Like, app is their, like.
Super container for everything.
**Maxime Quentin** 12:54 Me too.
One option could be, like, going for the browser API, and be, like, browser.location.url.
like this, at least, we don't have, I mean, it's sticking to the web API in… It's self-explanatory.
And then we kind of think about having a new page, a namespace for everything buzzer-related.
For the platform itself, I mean?
**Joaquín Díaz** 13:33 I like the idea of… like, I like the idea of having a separate patient entity, where we can… fit these things, and it's not browsed for that page.
And then keeping browser for platform-only attributes.
but also, like, I think browser delegation is more… like, clear of where the URL is coming from, so that may also be an option in here.
**Martin Kuba** 14:07 Go ahead, Hugo, you go.
**Hugo Levy** 14:09 Yes, hello, I have just one question about the fact we would like to add a new, let's say, namespace, which would be page. So for the event, we think about adding URL, but what other attributes do you think we might add in this namespace as well?
Like, for example, let's say we want to also track the dimension of the page, for example, like, the user resized the page or something like this. Would it make sense to have, in the same namespace, the URL and the dimensions of the page, or… What would be, basically, the idea of having a page as a namespace?
**Jared Freeze** 14:47 I mean, if Paige is the direct analog to document.
then… I mean, if you're measuring the viewport, I guess that would make sense, right? So, like, if you had an iframe, like, that would be a separate page, which would have its own dimension. So, I mean, I could see that being the place where that lives.
Yeah, that was my first thought.
**Hugo Levy** 15:11 And do you think it would still make sense to have at the same time URL and, let's say, the viewport attributes in the page attributes? I mean, URL and the viewport attributes in the page, or do you think it might have something different? I mean, I don't really know about how to, let's say, order the attributes, but in my mind, it would make a bit of sense to say, this is the page, like, as it is.
there is the URL on which the user is when he's on this page, and you can have, like, other attributes, let's a viewport as an example, but that might, be order in the next, Any next ones.
**Jared Freeze** 15:44 Yeah, I guess I would… I mean, if we're… because in the browser, it's document, right? Not page. I mean, we could just use document. We could just say document.url.full, or whatever, for that context.
**Maxime Quentin** 15:58 Like, even without document… document?
dot URL.
**Jared Freeze** 16:05 Yeah, just document.url.full, and then document would contain everything that's, like, in that rendered space, just the way it's represented today.
**Maxime Quentin** 16:15 And let's say I'm a mobile fork, will I understand what is the document?
**Jared Freeze** 16:24 If you're trying to match up keys to a mobile app, is that what you're saying?
**Maxime Quentin** 16:28 like, what I'm saying is, like, for mobile folks, app is very straightforward, but for me, an app can also be a browser app.
And then, I feel like if we add the namespace document, people might not understand what document is it, or… Could be, like, a WebView document, could be, like, a… And then… I like the idea of having a document instead of page, because a page can be a bit, like, not very straightforward, but having browsed the document, for me, it's very clear, like, what is… You can go to the web API and you'll find what is the document.
You have, like, I mean, I don't know, but, having documents at the root could be a bit misunderstood.
Understood by a mobile folk, maybe.
I don't know.
**Jared Freeze** 17:26 Yeah, I think let's, let's move this to a document, because I… to an issue, because I think that it probably is going to take more thinking, and I know we have, like, a bunch of other stuff on the list, so… I also want to talk to, like, my mobile team and, like, see, like, what they're already thinking. Yeah.
**Martin Kuba** 17:48 Yes, okay, sounds good, so let's move that discussion to that issue.
David, you have two issues you wanted to discuss?
**David Luna Bistuer** 17:58 Yeah, just, maybe a quick one, asking. So, last week we were talking about the moving… instrumentations, but, if I remember properly, they were… we just committed to moving the… a couple of, the new ones that we added in Constrip.
I would open that question to, should we move all instrumentations, all browser instrumentations, to here? Maybe review them?
You can say yes or not, or maybe you can just put it here.
That's my first, nope.
**Daniel Dyla (Dynatrace)** 18:31 There's some of them. I happened to come across, an old issue on the… user interaction instrumentation.
**David Luna Bistuer** 18:43 Reminded.
**Daniel Dyla (Dynatrace)** 18:43 It may mean that it exists.
it's been essentially unmaintained for a really long time. I think there's some of them that might be worth just, like.
completely dropping and redoing from scratch. That's one of them that I think is… likely has more problems than it's worth to use as a starting place. It's probably easier to start over.
**David Luna Bistuer** 19:11 Okay.
**Jared Freeze** 19:12 Yeah, I mean, because the names are changing, right, the, like, the… like, the import path is changing, It can all be refactored, like, it won't be a one-to-one anyways, so somebody that already has it will not get, like, a version bump, and then just have a new version from the browser repo. So, if we want to just mark those deprecated, if you really don't think it's that useful, or it's got, like, bugs.
But maybe we should just, like, make a mapping, because I know there's also vendors that have hotel instrumentation that may be good replacements, for user interaction, for instance. Like, we already have that, so maybe we can mash them together, or just bring in that one, or whatever, but I think that long list that's on the homepage, we should just go through one by one, and, like.
maybe just post in Slack, and Dan, you can comment, like, whether… I mean, we can all see, like, how old they are, but, you know, if we want to sort of vote on, like, hey, like, do we really want to keep Fetch in its current form? It seems to, like, have a lot of node code in it or something like that. We may want to update those things. You know, maybe drop XHR, you know, I don't… I don't know how many people are using that.
Stuff like that. So, what do you guys think about that?
**David Luna Bistuer** 20:29 Well, I think it's a good idea. I mean, I can open an issue, and then we can discuss that mapping, make a list of all these simulations, and maybe have a conversation there.
And just moved, yeah.
So, for now, for example, I've been using, like, an instrumentation.
We… we have a pure dependency in ZoneJS, but we already… I already saw some issues that people are asking about Zoneless.
Context manager and all this kind of stuff, so maybe people are already moving away, so maybe… I don't know, maybe it's just… It's better just to, add some extra… add some extra features to user action. We have a user action instrumentation, which is in the browser repository already.
So yeah, maybe it's just a matter of just improving the… these new instrumentations and, just deprecate the old ones.
I can create the issue, I can create the issue there, and now that we have a release process, and we have a way, actually, to check those things.
Feels… feels kind of a good time to actually… Start thinking about what's going to be there.
So yeah, I'll create this one, and we can have a discussion, instrumentation by instrumentation, it's one of them, on that.
**Daniel Dyla (Dynatrace)** 21:42 I also want.
**David Luna Bistuer** 21:42 Okay.
**Daniel Dyla (Dynatrace)** 21:43 About the zone context manager, but not today. I'll create an issue.
**David Luna Bistuer** 21:48 Okay, good.
And… yeah.
**Martin Kuba** 21:52 Dan, do you think it would make sense to also move the XHR and fetch instrumentations which are in the core JS?
**Daniel Dyla (Dynatrace)** 22:01 Yes.
**Martin Kuba** 22:03 Okay.
**Daniel Dyla (Dynatrace)** 22:04 I mean, if all of the browser instrumentations are gonna live together, then yeah, I think it makes sense.
**Martin Kuba** 22:10 So my only hesitation is that those are, like, Kind of important key instrumentations.
And they have, they have a lot of downloads.
So, for, you know, I'm assuming there are a lot of people out there who have… who have those, who are installing those, they have them in their dependencies, so… Moving them to, like, a new install package.
It's kind of a headache for a lot of people.
**Daniel Dyla (Dynatrace)** 22:39 Well, they're not installed by the SDK by default anyways.
They need to be installed by, like, the auto instrumentation packages.
I… I'm not sure… I mean, we can keep them if you want to, in the core, but they're not included in, like.
you know, the SDK instru- like, installation package, as far as I'm aware.
**Martin Kuba** 23:07 Right.
**Joaquín Díaz** 23:09 I think we should move them, but we can, like, keep… vaccine… Bucks on the old ones for a while.
**Daniel Dyla (Dynatrace)** 23:18 And then the first.
**Joaquín Díaz** 23:19 version of the new ones should be API compatible, so the only thing you have to change is, like, the package name.
But we shouldn't be doing breaking changes by asking people to change the package as well.
**Daniel Dyla (Dynatrace)** 23:37 Yeah, we can, of course, continue to maintain them. They don't take a lot of maintenance. People don't complain about them very often, they tend to just work. Like, they're not APIs that change very regularly.
**Joaquín Díaz** 23:57 Yeah, ideally the first time they move to an installation from the browser repo, it's just changing the… package Jason, like.
Right, like, not the kind, the name of the application, that's it, and installing, and then, well, changing the import, whatever they're using. But they shouldn't be… We shouldn't do any braking changes on the movement itself.
On the migration. Then, in the future, we may release this version on Solamba.
Not on… no more in packages.
**Martin Kuba** 24:32 Okay, yeah, I was just more concerned about the, just… Forcing all users to change their, you know, configuration.
Okay, david, the patches show.
**David Luna Bistuer** 24:50 Yeah, so yeah, that's the petition. So I put here the result. So basically, it's easier than we thought. It's just a matter that One instrumentation is doing the… just unpatching things. So, the order matters, and then, when you activate that instead given instrumentation, which is user interaction, just unpatch the complete history API, Completely destroying the browser navigation, the project initiation one. Also, this means that if at a given point, I don't know, you have your own configuration, and at some given point, you decide to disable one of these instrumentations.
Because of the unpatch, we're breaking the other one.
And I think, you know, okay, maybe with the order, now we have only these two instrumentations that are overlapping on the patching, on the APIs that they're patched.
So, okay, just make the right order, and that's it, you're good to go. But at the moment that you want to disable one of them, at the moment you disable one, you break the other, and then you're not collecting the three searchable blocks from the other, from the other instrumentation. And that's… I think that's, Aisha, a buck.
Basically, it's, the patch that we are using, Shimmer, is just, you know.
Making the good guess that we just patch once and that's it.
Or, you know, we are good citizens, and we are only patching and not unpatching before.
So yeah, I was thinking about maybe just, what is the way to go? Kind of… this is kind of restumbling, so maybe just reapplying patches, or… I made kind of a pet project to work on that, so having kind of a shimmer-like function.
That keeps track of all the patches and reapplies it, so… similar to… Attaching a listener or not.
But they compose the function, so when you detach something, when you… unpatch something.
Because it keeps track, it replaces everything. So, that's maybe what's our solution, maybe we can… Still thinking, so I know that from the node land, Tracing channels are quite sexy.
maybe we can do something similar to that, so we subscribe or unsubscribe some… to some channels and get information from that, maybe thinking on future APIs.
Well, that's, just a heads up, an update on this.
If you have, If you have a comment right now, you can just say it, but if not, don't worry, use the issue and put your thoughts there.
**Jared Freeze** 27:28 I just have one quick thing, which is, I don't think… I think we should commit to never unpatching.
Because you don't know if somebody patched after you, and when you unpatch, you have the copy from before you patched.
So, you're not just unpatching yourself, you're unpatching everyone who came after. If you have… this happens a lot when people are A-B testing vendors, right? Where they're like, oh, I want to try a new product, and they add them together.
I think we should probably just disable without unpatching. I… that just seems so dangerous. That's my first thought, yeah.
**David Luna Bistuer** 28:02 That's a good thing, so then it's just a matter of the, kind of the strategies we have to follow. So it's disabled, so, okay, you disable your instrumentation, then you're not, creating any logs or whatever, but you keep the patch there, so you don't unpatch and disable.
Daniel?
**Daniel Dyla (Dynatrace)** 28:22 Yeah, I just wanted to add some context. We've been considering removing the ability to unpatch entirely, because of problems similar to what Jared was just getting at. It's not really useful in production use cases.
it exists primarily as, like, a helper for tests, right? If you wanna… you're testing your patching, and stuff like that.
And we've been considering either completely removing the ability, or, putting a warning on it, or hiding it in some way so that it's only usable for tests.
Because we don't really want anyone to actually unpatch anything in production. If you need to disable an instrumentation, you should just set some Boolean flag, and the instrumentation checks, like, am I enabled or not? Should I… Just delegate to the original function instead.
It's much more reliable.
Yeah, so, and any unpatching anything, I don't recommend.
**David Luna Bistuer** 29:25 Okay, sometimes it seems that we have kind of a… Already a path forward.
Okay, I'll put that on the issue, maybe I'll work on that.
So this means that, yeah, we need to update the instrumentation to make sure that we are not unpatching.
One disabling.
Okay, thank you.
That's it for Martin.
return.
**Martin Kuba** 29:47 Okay, we're almost out of time, I just wanted to really quickly… Just note that we've been asked now a few times to To work on an end-to-end prototype and demo.
I would like to work on this. If anyone else wants to collaborate, please let me know, so… The things that I would like to… Have… be part of… part of this demo, this prototype, is… His prototyping sessions, or even other things as entities.
Generating metrics on the backend.
We also still have to design the SDK configuration layer, and then we could also, later on, work on protocol optimization.
An API.
Yeah, we're out of time, but if you're interested in working on this, let me know.
**David Luna Bistuer** 30:43 Are you gonna aggregate issue, or maybe a PR tool?
**Martin Kuba** 30:45 Yeah, yeah.
**David Luna Bistuer** 30:46 Congrat on that?
**Martin Kuba** 30:47 Okay.
**David Luna Bistuer** 30:48 Yeah.
**Martin Kuba** 30:51 Alright, anything else?
**David Luna Bistuer** 30:54 Nope.
**Jared Freeze** 30:56 All good.
**Martin Kuba** 30:56 Thanks.
Alright, thanks everyone.
**David Luna Bistuer** 30:59 Bye.
**carredondo** 31:00 Have a date.
