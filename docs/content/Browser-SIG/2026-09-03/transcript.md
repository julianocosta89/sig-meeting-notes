SIG: Browser SIG
Date: 2026-09-03
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**David Luna Bistuer** 00:55 Morning.
**Trent Mick** 01:03 Bonjour.
**Jared Freeze (Palo Alto Networks)** 01:04 Here we go.
You speak French? Trent?
**Trent Mick** 01:10 Lieuten at the end?
Bienieur… no, pas ditu. I take French immersion in… up to grade 12, and then… language took for my sister. For me, it was programming languages, so I can't really speak in.
And then, like, every vacation and… elastic European meetup that we've had has been in Spain, so I don't get to use the French at all. I have to learn some Spanish, which I tried… I tried hard the first time we had that meetup, David, and… But then, yeah, I didn't get very far.
What's that, what's that application or service you can do to help you with languages? I mean, there are a million of them, but there was…
**Jared Freeze (Palo Alto Networks)** 02:02 Oh, Duolingo?
**Trent Mick** 02:03 Yeah, there you go. I was using Digolingo for a while, but… I… I struggle with languages.
**Jared Freeze (Palo Alto Networks)** 02:10 Half our company's in Argentina, so…
**Trent Mick** 02:14 Yeah.
**Jared Freeze (Palo Alto Networks)** 02:15 use… I get to use poor Spanish with guaco all the time.
**Joaquin** 02:20 Hello.
**Jared Freeze (Palo Alto Networks)** 02:53 Hmm… I think Martin may have studies out this week.
Is that right?
Give it one more second, let's see.
Yeah, okay, cool. We can get started.
So I have the first topic today. We had talked about… there's a, so the client-side instrumentation SIG has… Got their own repo.
And so there's, client-side keys that are gonna get moved into there.
Or attributes. And so we… you know, are maintaining our own Weaver instance.
here.
And then some of those will be shared, so the things we sort of agree on that are not browser-specific, and then I think as things stabilize, maybe they get moved to client-side, as well. We'll have to see exactly how that works. It's literally just getting started. I think they're still in talks about it, but one of the things that I noticed was One of the things we do in our SDK is take certain keys blindly, from certain kinds of instrumentations.
which in JavaScript or a camel case. And so my question to the group is, do we want to commit to, underscores? Because I know that, like, in the HTTP SunCom, there's a wildcard, so it's like… I'm gonna mess it up, but I think it's http.headers.star, and you can sort of, you know, whatever headers you've got, you can sort of jam… jam in there. I was wondering if we kind of want to do the same thing, because, like, Web Vitals will give you, you know, 20 things.
Depending on the You may or may not want to, like.
hardcode those directly into CENCOM. So, looking more for direction here than anything, but, you know, should we be explicit with every single one of these keys, or is that a place, really, where we should leave it, like a wild card?
**Joaquin** 05:12 I don't think we should wildcar, even when there are, like, a lot of keys. I think wildcar is fine when… Anything can go into that… Like, bug of attributes, like the headers, you can create your own headers, so you don't have to follow any… Existing list.
different from the World Vitals.
Subparts, even though there are a lot… there are a limited number of them.
So I think, in that case, we should… define them in the conventions as we start collecting them, and I guess in the State case questioned.
Like, if everyone uses Snake Case, even for, like, non-client conventions, I think we should use Snake Case.
I don't think… I don't… I don't think we should match… we should mix, formats, even though we have our own conventions and our own dancing.
**Jared Freeze (Palo Alto Networks)** 06:17 Yeah, that's… that's my thought as well, is just convert everything, you know, maybe we have the utility.
That's bringing things from, JavaScript.
**Joaquin** 06:25 Yeah, yeah, we could have a function where, but, we got… we should definitely keep the same names that we get from the browser, that we don't need to change them, but… oh, yeah, just in case.
**Trent Mick** 06:37 The Weaver templating does have a… filter for converting things to snake case. I don't know… yeah.
Yeah. I don't know if you'd get away from Snake Case, if you're gonna… Probably not, I don't know if you're gonna fight any tooling.
in Weaver that already exists there.
Because there's some… Rego… they have, like, Rego language for doing… tests to make sure that they don't break whatever compatibility rules they have in SEMCOM versions. And some of those are to check that you never define a… SamConf.
variable that's been used before, where the only difference is, like, you do this normalization, so they had a thing where it was, like, foo.bar changed to foo underscore bar, but then that's represented the exact same way in… SEMCOM packages for languages, because they can't use dots, they normalize those to underscores, and I don't know if… Probably not, that's what I'm saying. I don't know if you run into some surprise there, if you're betting against the stream, if you try to move away from snake keys.
**Jared Freeze (Palo Alto Networks)** 07:42 Okay.
**Trent Mick** 07:43 I mean, there is… you're right, there is that… that… that wildcard for htp.request.header.key.
And I think there's some other examples, but obviously that's… common one. I don't know if that's because, like.
I mean, I guess some headers are specified, but otherwise it's a wide-open thing. As opposed to Web Vitals, it's a… well-defined, specified set, right? I don't know how many…
**Jared Freeze (Palo Alto Networks)** 08:07 It changes over time with versioning, which is why, like, the implementation itself is, like, run through. If I get a string or a number, go ahead and, like.
you know, shove it in to the payload. But yeah, if we need to be explicit, that's fine. It's really just a versioning thing. Like, as it moves forward, they'll add more, and then we can just add more. You know, maybe we can put the version in the notes of what's available, or… What the newest is, so…
**Trent Mick** 08:35 Okay.
**Joaquin** 08:35 Yeah, yeah, I think we control that with the instrumentation, like.
Maybe there are new kits, but we control when they are available through the instrumentation versioning.
**Jared Freeze (Palo Alto Networks)** 09:06 Okay, cool. See, moving on, so David…
**David Luna Bistuer** 09:13 Okay, so recently we got the SPR, but it's about adding instrumentations to the SDK.
Well, it's, using resistor instrumentation method from the instrumentation.
So I'm not going to discuss the details on the PR, so it's enabling instrumentation, but it's using this.
But from experience, I know that, there are some nuances in the resistance that basically, it enables everything. So, long story short, the LDR, it enables everything, no matter what configuration you passed.
So, I wonder if that's the behavior that we want, so… I can think on… on some… cases that maybe, you know, you're using the SDK and you want just to have this rotations, but not enabled yet.
And then… I don't know, maybe an update from the server, maybe from something that happened, and you want to enable something.
So then at the beginning, you don't have… you want to keep the data low, and then when it's something that is interesting, maybe you enable instrumentation to get more information about that.
So, I can think about this use case.
So, I want the traffic flow, and then at the same moment. So, here I'm talking something maybe on another one.
That is another feature, which is dynamic configuration.
But yeah, that's… that could be… that's doable.
But if you're using your registered instrumentations, what we're doing is, like, okay, no matter what you pass, you're getting everything enabled, and you're getting all the data, and you want to keep the traffic low, but you're not interested in one of the instrumentations for now, you just have to just remove it from the registry instrumentation.
So, okay, I was wondering, oh, I have a doubts if that's a heavy movement on… on the process again.
That's… that's a.
And then… Yeah, go ahead.
**Joaquin** 11:12 No, finish, finish.
**David Luna Bistuer** 11:14 Oh, the second point is, also then I noticed that, okay, enable, it's not enabled, but also it's patching and enable.
So we have something that is state-enabled or disabled that decides if we send telemetry or we generate the alimony or not, logs and traces.
But the same method is used for patching, or also… I can think of… We want to inject the SDK as soon as possible to get the, you know, the reference, the proper reference to the APIs.
So maybe I want to just do… But as soon as possible.
But then enabled later, so start sending data. Also, this comes with the same idea of, you want to enable right away or not, so it's, okay, maybe I want just to load the SDK between some editions, have everything patched, so I have to… the Bristol reference, no other script, you know, if that's the first script, no other script had to change to… tamper my… the APIs before me.
And then I decide on the runtime, let's say, okay, now I'm going to enable web titles. Now I'm going to enable errors.
**Joaquin** 12:29 I… it sounds like everything you're mentioning is just, like, changes on how the instrumentation works.
Or the different APIs, instrumentation call.
But, to me, these patties just take a… quick way of starting the SDK with a set of instrumentations.
I agree that we need those tissues you're mentioning, but I don't know if… that's something that we should pour in here. Like, I think what is in here is just really simple, it's just… Allowing people to… set a list of instrumentations that will be registered at the start of the SDK.
I wouldn't… do it more complex than that. Yeah, and then if you want to do something different, you can always just not send them in there, and you can do it, outside the Star SDK, right?
like, you use… like, it is now, what is released. You can just call Rochester Instrumentation later. That will work.
Like, the only difference with this is that you can… Send them.
when you start the SDK, so you don't have to import versus your instrumentation in your own call.
**David Luna Bistuer** 13:59 So then…
**Joaquin** 14:10 Anyways, I approve the PR, but I'm open to remove the approval if we need more time to discuss, or if we want to discuss on the self.
**David Luna Bistuer** 14:17 Well…
**Joaquin** 14:18 Thank you, what was…
**David Luna Bistuer** 14:20 We're setting here a behavior, so it's like, okay, so it's… whatever you pass, it's going to be there, you know.
It's, it's enabled.
So whatever invites Naples to the, and then… If you want to have an instrumentation, I don't know, it's like, if I want to have a… enable instrumentation later, or at least I… if I just find a subset of the instrumentation is being enabled, I need… I need to be sure to disable them later. So, register them on the SDK, disable them later for… to enable them later. So I was just thinking about, you know, people, sometimes some customers want to control The amount of data that they're receiving.
Maybe they are not interested in certain things.
Okay, then, you can set a mechanism somehow. You can set something that you can, on runtime, say, okay, now, I don't want to start with this, or this is from the, you know, from the beginning.
But then maybe I want to enable them later. So that's what I'm thinking. So if we say that that's the behavior, then… they have the… maybe some kind of a dynamic registration of the instrumentations later, so it's like, okay, I don't want… Let's say I don't want the eggs and beans to have tasted.
But then, maybe I'm interested later to have it, so then I have to create the instrumentation and Register again, or have a late registration of that.
So then maybe we do have to provide an API for that purpose? Say, okay, now append this instrumentation, now remove that one. Well, not removing, because now you can… if you have access to the instrumentation, you can disable it.
**Joaquin** 15:57 Yeah, so how do you do that now? Like, how do you… Today, what would you do to… to have these, as you were to describe it, like, do you… called Statar SDK, and then you call resistor instrumentation.
With a set of instrumentations, then you call register instrumentation again with the other ones that you want to be… to have enabled later.
**David Luna Bistuer** 16:23 Yeah, well, this is sick.
**Joaquin** 16:24 something new that we need, from the.
**David Luna Bistuer** 16:26 It's, yeah, it's some, some, something… well, I would say something new, so it's… The constructor calls enable.
Okay, we can discuss if that's a good pattern or not.
**Joaquin** 16:39 Because…
**David Luna Bistuer** 16:39 Doctor calls enabled if the configuration allows it. So, okay, repeat configuration, we can, you know… decide this. But then, the resistance limitations, no matter what, it's enabling average.
Okay.
If we can, if we, I don't know, if we still honor the configuration.
And I have a reference to this list of instrumentations, I can just, you know, enable the ones I want.
And then later on, just call directly on that to say, okay, now enable.
I'll be safe.
I can just call the API.
**Trent Mick** 17:15 You're not talking… you're talking beyond this PR now, right?
**David Luna Bistuer** 17:18 Yes, yeah, could be. Well, but that, you know, that sense of behavior.
So, that one sets the behavior. That one says, okay, no matter… if you are adding into an instrumentation data, right, it's enabled, no matter what.
And it's sending telemetry.
**Trent Mick** 17:35 Yep, this PR is not.
**Joaquin** 17:36 Are you gold?
**Trent Mick** 17:37 to enabling or not, is it? Is… maybe I'm missing something. It's just about…
**David Luna Bistuer** 17:43 It's a.
**Joaquin** 17:43 That's funny.
**David Luna Bistuer** 17:44 VR.
It's a side effect that everything is enabled.
**Joaquin** 17:48 Because it runs fresh history instrumentation inside the star SDK functions, so whatever you pass down to the SDK, It will refuse for them.
And then, by that, it will enable them.
But then you can keep the references, because you create the instances outside… on your own call, you create the instrumentations, and you just send them to the SDK.
So you can keep the… The references and disabled, but you are saying that There's no way of… Like, if you set enable false.
When you create instrumentation, and then you call register instrumentation, that will enable it anyways, even if you set the same as false.
So that sounds like a… Issue with the… instrumentation call itself, like… you would expect that to be on or. Like, if you said disable, then nothing is going to enable, and then you can enable on your own call, because you have… still have the reference of the instrumentation, right?
When you create instrumentation to pass down to the status decay.
And you can enable later.
So the API… This is still the same, like, you have a list of instrumentations, that you can enable later, if the owner… like, if enable will work as you'd expect, that nothing will enable your stuff if it's disabled.
Then… This makes sense, right?
**Trent Mick** 19:20 I think a major problem here is that the instrumentation package is already… Done a bad job of mixing different concepts.
So… The language is difficult here, so I might add to the confusion, but… Instrumentation's doing their patching.
And then… Separately, an instrumentation Deciding that it's enabled, so it's gonna do something with the monkey patches that it has.
in place.
Should probably be separate concepts, in that patching needs to happen right early in application startup.
At least in Node.js.
**Jared Freeze (Palo Alto Networks)** 20:09 But…
**Trent Mick** 20:10 But enable-disabled can, and in this time of op-amp and those kind of things, which maybe doesn't impact Browser and stuff, but for dynamic configuration, enable-disabled can happen later.
Through the lifetime of the application. So, separating those concepts can help.
clarify what the… what the interfaces should be. Right now, the instrumentation classes kind of mix that up, because, like, at least on the Node.js side, instrumentation base.enable is called in the constructor of an instrumentation, so they're generally already enabled on the way in.
So yeah, it gets… it's hard to separate those without looking at breaking or changing the instrumentation-based classes.
**Jared Freeze (Palo Alto Networks)** 20:55 So, I have a branch already, I think, that solves this, which actually divorces these two and makes a browser instrumentation base.
I'll put that up and see if that is something people would be interested in, but it also means that we would not be using this.
I don't know if that's appropriate, but I was trying to solve this problem.
As well.
Because some of the… you know, some of the patches can't be undone, right? They can't be unwrapped as well, so you're doing a bunch of work that you may immediately try to disable, but it's already doing certain things, so… I know that… I noticed in the, so in this… register instrument… well, in this package. The browser version also doesn't have init, I think.
**Trent Mick** 21:44 Yeah, so another problem from the browser point of view is that the instrumentation classes have been set up with kind of poorly defined interfaces that are node-specific sometimes.init is one of them, yeah.
**Jared Freeze (Palo Alto Networks)** 21:57 Yeah, and so I think, there is… that kind of… there's the package fork where it's got a browser folder, but TypeScript doesn't actually walk that folder.
And so what winds up happening is that you have to override in it in custom instrumentation.
But then it doesn't get used.
Whenever you compile.
So, that was another reason I thought Browser-specific instrumentation, class might be.
a nice thing, so… I'll put it up, this is probably hard to talk about.
**Trent Mick** 22:30 Okay, cool. David mentioned that you had had something, or some thoughts there, as well.
mostly on the Node.js side, or, like, for maintaining the instrumentation package, it's mostly just been hand-wringing by me, because it's really hard to change, and other things have been the priority right now. Like, certainly I'm not going to do anything in September.
Now that we're gonna try to get 3.0 going, but yeah, yeah. It scares me a little bit, the thought of the browser instrumentations moving away from that package, but I can totally understand why, and I don't think it… something that needs to get blocked, so yeah, if you guys need to do that. It'd be nice if we came up with some… basically, I wanted instrumentation to just be an interface, and this is what an SDK expects.
to… I provide two instrumentations or a call on their interfaces, and part of that is divorcing the this setup where you do your patching and the enable-disable process. So, yeah, maybe you come up with something that's… Let's… That's good for that.
**Jared Freeze (Palo Alto Networks)** 23:32 Well, the reason I was sort of pursuing this was, you know, I think the… The dream of, sort of, Is it, you know, isomorphic, or iso… isometric code on both platforms is… I think we're finding it doesn't really cross over, and so… That's the only reason I was pursuing this, because I, you know, I'm… I heard you say this before, right? Where, you know, it's like, if we… you know, changing things is hard. So, Okay.
Cool. So I'll… yeah, I'll…
**Trent Mick** 24:05 Would you then land?
**Jared Freeze (Palo Alto Networks)** 24:06 see if it happened.
**Trent Mick** 24:07 So, say you dropped.
the instrumentation package as a DEP, and you had a registered instrumentation. You said you're going to put up the things, but would you then change to something close to what this Or at least the spirit of what this… PR is doing, in that you pass instrumentations into the Start Browser SDK function, and then it's up to the SDK to do whatever it does for its instrumentation interface with those things.
Or… Are you thinking in the current state, where it looks like… I was surprised, actually, to see that Star Browser SDK doesn't take instrumentations, it's up to the user to do a separate register instrumentations call.
**Jared Freeze (Palo Alto Networks)** 24:45 Yeah, I… I mean, so, I think we just hadn't gotten to this yet.
I mean, I think this was always intended. But, yeah, I think, you know, passing in… I would like to see it both ways, which is, like, we determine, like, if the default is enabled.
And then being able to pass an option, or to call.disable, or enable.
It requires you to explicitly handle everything and keep a reference, but… I… if we could do it in the… Yeah, I just like to give people options, so…
**Trent Mick** 25:23 Yep. No, I can understand that, too, and it, like, it is a separate concern in Node.js LAN, too, right now. It's like, you have the SDK components, and then you have instrumentations that are mostly independent, and they'll use the globally registered providers.
Generally, though they can be assigned providers. The thing I was thinking longer term, and as you said, I've been talking about this forever and haven't done anything, actually is the… on Node.js side, the idea of the SDK providing services to instrumentations is maybe interesting, because require in the middle and import in the middle, having a single instance of those provided by the SDK singleton is probably… a better design, but is a departure from the way things work right now, so it's another thing that's hard to change. On the browser side, you probably don't have that. For an instrument… a browser instrumentation to do its monkey patching, it doesn't need a whole bunch of, like, utilities or anything for doing that, it just… Replaces a function, right, and wraps it, so… If I understand correctly.
But, sorry, I'm dominating.
**Jared Freeze (Palo Alto Networks)** 26:24 No, it's all good.
**Joaquin** 26:26 I still think we should leave the option always open to people to not use the SDK. Like, if you want to do something really custom, you can just bypass the SDK and… Initialize all this stuff all by yourself into an instrumentation.
So, I agree that we should… help people with the SDK and make it easier, but I'll always have the option to make it so you don't need the SDK at all.
Like, if we are going to have a new, like, instrumentation for, like, base class for Browser.
I still think we need some kind of a Shasta instrumentation function.
That you can use from the… like, that the SDK uses, or you can use by yourself.
That will be similar to what we have, or even the same, I don't know. Like, we can use the same restrictor on just a different base class, or whatever.
With this new interface where you can, patch and then enable later.
**Jared Freeze (Palo Alto Networks)** 27:26 That's a really good point. I hadn't considered that… Yeah, custom instrumentation is still going… is not going to be using the internal import.
Of instrumentation base in the browser.
Like, we'd… it'd either have to be a new package.
Or some modification to the existing package, like, with a separate export.
Because, you know, if you're using, like, hash instrumentation base.
In the browser repo, that's good and fine, but then no one else will be able to use it.
So…
**Joaquin** 28:05 Yeah, you can… yeah, you should… we should probably explore that. I think… I still think… base instrumentation class is something that should be shared across Node, and… Browser. But I think maybe, like.
It is the opposite way of we are doing things, that we can… Define the new basis orientation class on Browser, and then move that back to Node once we all agree that what's something that works for both.
Like, I don't think… like, we have both to patch, and we have both to enable. I think the interface is the same, it's just, like, we just need a new interface that works for both known Browser. We can start on Browser and then move back to known.
**Trent Mick** 28:47 Yeah, I think you guys should totally work on that on the browser side and not be limited by what's on the node side.
one… thought is that I don't know that there necessarily needs to be a class involved here. I don't know that the instrumentation package needs to provide… or that every instrumentation needs to have some of the shared code functionality. I think it's just an interface in a TypeScript sense that they need to follow, like, there's a contract on how instrumentations are meant to work and expose an interface if they're passed to this registry instrumentations things, but they can just be a vanilla object that implements those methods. It doesn't need to… Inherit from a class.
To the degree that helps.
Because right now, the base classes don't for… other than for requiring the middle import and the middle stuff, they don't do anything useful, they just add some confusion with the enable, disable, and the set config, get config. Those things are kind of intertwined and gross right now.
Alright, so…
**Jared Freeze (Palo Alto Networks)** 29:46 Okay.
**Joaquin** 29:47 Yeah, yeah, I agree. I guess the question is, like.
do we stop this PR until we have that base class, or do we think this PR is… Independent of… that we'll do there.
**Jared Freeze (Palo Alto Networks)** 30:05 Yeah, let's… yeah, let's chat about it on the PR, or we can take it to Slack, either way.
Real quick, Maxine, did you… you just want us to take a look at this one?
**maxime** 30:17 Yes, I mean, very quickly, otherwise, it's not your threat, we can talk about it later. It's just like, I merge and fix the commit, David, and… if you feel it's too early to merge, or if you feel it doesn't… we don't need it yet, we can just postpone the PR for later.
Long story short, I added a… on top of the noop SDK, I added a new class that is invalid SDK that makes the difference between the two.
But also, it was just a suggestion out of my previous PR, so if we feel it's not urgent and we don't want this till now, we can just postpone it.
**Jared Freeze (Palo Alto Networks)** 31:12 Okay.
Okay, cool, yeah, we can look at this one again, and… yeah, comment and Slack if we need to, so… Yeah, we're at time.
Thanks, everybody.
**maxime** 31:27 Thank you. Bye.
**David Luna Bistuer** 31:30 I…
