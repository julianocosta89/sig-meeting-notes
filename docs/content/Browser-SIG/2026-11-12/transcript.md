SIG: Browser SIG
Date: 2026-11-12
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Trent Mick** 00:47 I think David had created a new section, but I didn't change the dates on there, too, no 5s there.
Ocean, we're so sorry.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 00:55 Oh, I see. My bad.
**Trent Mick** 00:57 That's me guessing.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 00:59 Yeah, I didn't notice that.
I'll move it, hold on.
**Trent Mick** 01:06 Okay, I'll change, I'll change the date.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 01:49 I'm a little gun, it's been, it's been a while.
How are you?
**Wolfgang Therrien** 01:54 I'm doing alright, I'm doing alright.
It's good to be… good to be back.
Hopefully things are a little bit less, more predictable.
Great, but I'm happy to be back.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 02:13 Alright, Yeah, so if you have anything to talk about, put it on the agenda. I think we have some topics today.
Right, I guess we can get started, David, you have the first two topics?
Meetings.
**David Luna Bistuer** 02:58 Well, it's just the PRs that I just, linked to the first topic, but actually, when I'm seeing that is, Okay, there are some new cases or situations that we found that Maybe the configuration option that we… Provide at the… from the beginning wasn't enough.
So, for example, one is the log level, and the other one is the one that Hector is working with, resource.
But then, kind of the solutions that I'm seeing that it's kind of making a new configuration option actually overrides or demotivates the other.
And… I want to have your thoughts, or maybe just put these in common.
So we can have a discussion about this. It's okay for us to add new options.
That overrides existing ones.
at least knowing that we are still, you know, it's a… SDK process is still… Kind of young.
So, it's been months since it released the first time, it was in July, so… Yeah, I want to hear your opinions, and… And… and see what's kind of the… Yeah, the consensus in the six, so then we can move forward on those PRs for with what we decide here.
Do you want me to come to more details?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 04:26 So is this, so we start, like, the diagnostic logger internally.
**David Luna Bistuer** 04:33 Yeah.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 04:34 And like you're saying, like, There might be a different implementation.
**David Luna Bistuer** 04:39 Yeah, exactly. So, for example, in this case, you know, the customer, the user, we might say, might set up a logger first.
And then tried to start the SDK, but then the SDK Resisters another logger, and then, you know, just overrides it.
Okay, so… the common case is just, you know, using the DIAC logger from the API, which is fine, so I guess Most people will not use, will register a logger, but… there is a situation that they maybe just they want to just register a logger first, and then start the SDKs. Then, my logger is gone.
My implementation is never, you know, it's never working on the application, the host application.
That's one. I think that the PR from Hector, it's about resource.
Which, I actually think that what he offers, it's a function that actually creates a resource.
From the attributes and the detectors. So, Maybe I'm just considering that maybe what's… okay, maybe the browser, the resource attributes, config option was a good idea, maybe with something that We can provide that function as a utility, and then just pass the resource to the SDK directly.
Instead of having, kind of, a… two different options, or three different options that I… then I, you know, kind of, Collided with each other, or overlapping, and then, okay, now this one overrides the other.
So if you set resource attributes, but you said a resource, then resource attributes are ignored.
And you get the resource,
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 06:17 And this, this applies to both the, the quick, quick start, and the… So we have, like, the Quick Start SDK, and then we have, like, the Start SDK one.
**David Luna Bistuer** 06:28 Yeah… So when you're using the start and quick start, because they're, you know, merging, or at least they are hiding the details, and they are starting the SDK logs and traces SDKs by itself, by themselves. It's kind of hidden, but if someone was just to start the SDK locks, the 3SS unlocks SDKs individually, then this problem arises, so it's, it's more, It's more evident, so it's like it sits right into your face.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 07:03 Right.
Yeah.
So, I think… so I can't… I can't… I don't recall all the details, but, Like, I would, like… I was thinking, like, my kind of thinking was that, like, the quick, quick start would be the one that has all these defaults, right?
Like, so…
**David Luna Bistuer** 07:28 Fair enough.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 07:28 It's for, like, what… for, like, the, like, very… the most common… setups that, like, don't require these customizations, and then, like, if you want to customize them, like, you would… you would use the other… the Start Browser.
**David Luna Bistuer** 07:40 SDK.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 07:41 Function, like, which would provide you all the configuration that you need, like, to override these things.
Does that align with what you're also thinking, or…
**David Luna Bistuer** 07:56 Do you mean that then, Default should live in the Quick Start, but not on the… on the SDKs.
Dante already suggest you should get…
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 08:15 I don't remember, like, for this one, for the diagnostic logger, I don't… For the diagnostic loader, like, is that, How is that… is… it's not configurable right now? Like, it's… you can't…
**David Luna Bistuer** 08:48 How could you have to… Yeah, it's not…
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 08:51 It's not.
**David Luna Bistuer** 08:52 So you can just pass the log level.
That's the only thing, and then… each SDK is using registering the logger. There is an utility function that we use to… just to both avoid double resistation between SDKs, so you start the Lux SDK resistor, then later you start the address SDK, You know, it knows, already knows that it's registered, so it doesn't… do another registration. But, you know, if you do something outside the… the SDK realm, yeah, you get this problem. And there is no… the API doesn't offer a way to actually know that it was already registered or something.
So you can set up.
You do your own setup, and then later, you start the SDK.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 09:44 So is there…
**David Luna Bistuer** 09:45 There are differences, yeah, yeah.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 09:47 Sorry, so… so, like, is there… is there, like, an… Sorry, I think I'm still not understanding fully. So, like, if you… if we added, like, an override for the diagnostic logger in this configuration here.
Then if you didn't override it, then it would use the default one, but if you did override it, it would just use the one that you provide.
**David Luna Bistuer** 10:12 Yeah, but, at the moment, it's overriding always, so it's always setting a dialogger when you're starting.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 10:20 Okay, okay.
**David Luna Bistuer** 10:21 Okay.
So that's… that's one problem. So, I was doing a talk with Trent, before his meeting.
There are different solutions, so Aditya already provided a couple of options. I offered a third one.
there is also a fourth one, so if there is a different solution, so maybe you can, I don't know, maybe just set, there was an option that is not registered here, I'm going to put it here, but maybe just, you know, say you can register your own logger, and then say, okay, the level is none, so when you start the SDK, say, okay, none.
And then that put me in, kind of, this value would mean… no longer is resisted by the SDK.
Diana uses my own.
And the SDK does nothing. So that's a way of avoiding it. So there are different solutions, but… Okay, maybe that… that's not the best case.
But, kind of, for example, for resources, I think that, you know, maybe it's sometimes a… kind of my question would be, it's okay to just review configuration options, and then maybe make decisions, and maybe just, you know, drop some.
Considering that we are still, you know, experimental… Yeah.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 11:33 Okay.
Yeah, that's…
**David Luna Bistuer** 11:35 It's not… that's not what I meant on the logger thing, okay? So I guess it's… its configuration has, you know, its own use… its own cases and… and so on. Sorry, just give me a minute, they're calling on to…
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 12:16 Hector, do you have any, any, like, Opinions on, like, your… The one that you have, or David's fine.
**Hector Hernandez** 12:22 Well, this is… yeah, I'm not, very into a specific way of handling this, right? Whatever is discussed here is the best option that applies to all this user will be fine to me. The thing with the resource detector, it's supposed to be immutable.
Right, so that's another thing. So, it's even, A special case on top of that, so… But, yeah, I don't have any strong opinions. Please take a look at the PR. Okay.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 12:54 Right, I'll take a look at both.
David, did you want to add anything more to that?
**David Luna Bistuer** 13:00 No, that's fine. So, we can keep that conversation, so it's not to have the conversation right now, because it's kind of a wide topic. But yeah, but the idea of, you know, at least… No, no, no, maybe I just propose something to say, okay, let's remove this, maybe change something, make somebody change the configuration.
If that applies. But, you know, just to let you know, and… and to see if that's… there is a problem with that, if we want to kind of, Keep the configuration, Not frozen, but, you know, more stable.
It's been pretty… it has been pretty… it has been pretty stable, though.
But, sometimes we have to break things.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 13:40 Yeah, I mean, we're very much in… still in experimental stage, so I think… breaking thing is okay.
If you have a good reason.
Alright,
**David Luna Bistuer** 13:53 So, let's continue on those PRs. Let's continue the conversation there.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 13:56 Sounds good, alright. Thank you.
I do have, some… so I have the next topic, which is, this… this issue that I opened a while ago, which was essentially just fixing these… the path in the export URL that we, that we have. So, like, right now we have, you can provide a single URL, Right? It selects the… it's the top-level export URL.
And we, like, the… we add, like, the… V1 logs and V1 traces, suffixes, and… the… the discussion in, like, so… so there's this PR open… That's… To address this, and it went in a little bit different direction, like, it… When, there was… there's a discussion about… Basically, just removing the, the top export URL altogether, and we would have to provide two, like, exact URLs for spams and for logs.
But, like, a decision hasn't been made on this, so this PR started with just a fix, with just a simple fix, and then, like, it moved over to this new proposal.
But it seems like it's a bit stuck, so I wanted to see if we could make a decision on this, so it's essentially… the decision… the main decision is, like, do we want to keep the base URL at all?
And then… then there are some additional decisions that, like, come out of that.
I think my stance on this is that… the quick start, I think it would be useful to have a base URL, so that the user doesn't have to provide two.
Just make it as simple as possible, and to get started for, like, the most common cases.
But, like, in the… in the other… the start, in the other… Start method.
We could… we could just go back to just… you have to provide individual… URLs.
What do you all think? Or if you want to take a look at this and think about it, that's fine too.
**David Luna Bistuer** 16:25 I'm with you, Martin. I think that, you know, the quick start, it's meant to… for everyone that's using the defaults.
So it means that in the collector, at least it will have the default path for each signal.
And then we can have kind of a more grain… fine-grained configuration in the start process, okay?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 16:45 Okay.
**David Luna Bistuer** 16:45 I'll put it in my list, so I forgot about this, I don't remember. There is a comment from me in the PR.
Yes, yes. Yeah, I lost track of time, yeah.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 16:56 Okay, and then, I guess… The Dean… the question that would come out of this is that whether it would make sense to… to rename the URL to be something… More intuitive, like, have the base, like, in the name.
Yeah, rather than just export URL.
Right, if there's, like, no strong opinions, I mean, we can… I can just propose… proposed time.
Alright, I'll make a note on this, and then also… put, like, put a comment on the… on the PR so that it can… it can get unstuck.
Alright, next topic, Addie?
**Aditya Reddy** 18:01 Yeah, this was already reviewed, and David already approved, just, wanted to bring… so it unblocks for the next part.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 18:11 Oh, okay. So it's… it can be merged, then?
Alright, I'll… I'll… after the meeting, I'll… I'll… Review it, and we can merge it.
**David Luna Bistuer** 18:23 That's good, thanks.
One comment on that, There is kind of… we talk about having a kind of a follow-up on A way to actually share, or link, yeah, correlate the logs.
The resource timing logs from the… From that span, I don't know if the issue is it's created or not.
Just wondering if there, if there is, Aditya, is your plan to, to follow up with the… with the resource timings?
**Aditya Reddy** 18:56 Yeah, that is the plan. I haven't gotten to it yet, but yeah.
**David Luna Bistuer** 19:00 Okay, okay, good.
Thank you.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 19:07 Alright.
Cool, thanks, Addy.
And… Chris?
Alright, is Chris here?
**Chris Chestnut (Firebase)** 19:18 Yeah. Yeah, I am. How's it going, y'all?
Yeah, so I saw the chatter in, the Slack channel, last night and realized that, yeah, we probably should have, mentioned that, we were going public preview with, some dependencies with the browser, the Browser Lib, so… Just wanted to come and say, hey, what's up? You probably remember Cleo, who's currently out right now. They've been attending this meeting really regularly, but I'm going to try to make it more often, as the representative for Crashlytics, part of Firebase, part of Google Cloud.
But yeah, just wanted to say, hey, we're in this public preview phase right now for our SDK, for customers trying to get Crashlytics in their web apps.
And, the Browser Instrumentation Lib, is in a private preview feature, that we're currently actively developing on, but, but looking to, yeah, expose it to more folks who are looking to get, OTEL in their apps, so… Yeah, there's some docs there on, like, the, the Crash for Web, initiative, but that doesn't include the new stuff, the stuff that's in… the Browser SIG in particular, at least not quite yet. But if folks are interested in joining the earlier access, the private preview with the breadcrumb stuff, let me know. I can get that arranged.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 20:46 Awesome, that's awesome, Chris. It's good to hear that it's gonna be actually running in, you know, in production, or… For actual users. I'm curious, like, are these, which instrumentations are you pulling in, and, are they, are they enabled by default for you, or…
**Chris Chestnut (Firebase)** 21:05 So during our private preview, the intermentations are enabled by default, but we are currently working on allowing folks to customize what instrumentations they want in their app. The instrumentations we're using are Web Vitals, user action interactions, Network, Fetch and XHR.
instrumentations, and document load. I wanna say that's… I wanna say that's all of them.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 21:34 Okay. Are you, are you using, like, are you using the… So, we recently migrated the XHR and FEG instrumentations over to this repository. Are you using those versions, or are you still using the old versions?
**Chris Chestnut (Firebase)** 21:50 Let's see, which… Which repository are you talking about?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 21:54 Yeah, so I mean, so we have, like, in here… In… in, like, this… our new, browser SDK repository, we have… the XHR and Fetch?
instrumentations that have been moved over from the JS SDK repo.
**Chris Chestnut (Firebase)** 22:16 Yeah, let me check the, the repo real quick. I thought we had updated that, but I'm not quite sure.
I know our browser is still pretty old right now, I think we're on, like, 0.6.0.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 22:30 Okay.
They're a little bit different in that they, they work together with the resource timing.
instrumentation now, so I think it would be good to have feedback on how that works for you, if you're gonna switch to those.
**Chris Chestnut (Firebase)** 22:47 Oh, yeah, and I'm looking at our code, yeah, we're still using the old, the old, Fetch and XHR libraries, so, yeah, we'll definitely report back. Oh, Addy, yes, saw your, your PR. I think we're going to likely attempt a more holistic approach to get folks, like, to, to try to move all the way over to OTEL 3.0, rather than just resolving the browser instrumentation stuff, but appreciate that PR, because it helped, you know, figure… us figure out what we needed to do to update, update the code and make sure things worked when we updated to OTEL3.
So thanks, Adity.
**Aditya Reddy** 23:27 Sounds good, yeah. I'll close it out.
**Chris Chestnut (Firebase)** 23:31 Appreciate it.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 23:33 Yeah, and Chris, just so you know, like, we were planning to do Do migrate to… to the, 3.0 as well, here.
Like, we, we had, we just… we finished the instrumentation base refactor.
Which just shipped, and which was kind of… which was blocking.
the… the V3 migration, but now we're unblocked on that, so… Damn.
**Chris Chestnut (Firebase)** 23:58 Oh, excellent. So once that rolls out, what would that be, like, 12, like, 0.12.0?
Or something for…
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 24:06 I think so, yeah.
Yeah, yeah, it should be, it should be soon, so…
**Chris Chestnut (Firebase)** 24:13 Awesome, looking forward to that as well.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 24:15 Alright.
Okay, we have 5 more minutes, are there any other topics that folks want to discuss?
Alright, if not, we can, we can end it soon.
Thanks, everyone.
**Hector Hernandez** 24:36 Thank you.
**David Luna Bistuer** 24:37 Yep.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 24:37 So…
**Chris Chestnut (Firebase)** 24:38 Thanks, y'all.
**David Luna Bistuer** 24:38 with it.
