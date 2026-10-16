SIG: Browser SIG
Date: 2026-10-15
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Martin Kuba** 01:18 How's it going?
**Jared Freeze (Palo Alto Networks)** 01:20 Hey, can you hear me?
**Martin Kuba** 01:21 Yeah, I can hear you.
**Jared Freeze (Palo Alto Networks)** 01:23 Cool.
**Hector Hernandez** 01:24 Hello.
**Martin Kuba** 01:25 Hector.
**Jared Freeze (Palo Alto Networks)** 01:26 What's up?
I believe it's the 15th.
**Martin Kuba** 01:49 Kind of…
**Joaquin** 01:50 Cool.
**Jared Freeze (Palo Alto Networks)** 01:52 Hey, what's up?
Okay, let me share… Okay.
Zoom in here and go.
Okay, let's get started. Let's see.
Yeah, Martin, you wanna go over the big release?
**Martin Kuba** 02:32 Yeah, no, so this is just, I guess for sharing across SIGs, the JS… as you know, Jared, the JS SIG is having a major release, and they're planning to actually run it next Monday.
The reason I'm mentioning it is because, actually, mostly of the next topic that Maxime posted, which he is… Looking to, update the demo.
And the V3 release has, like, the changes in the, the tracing SDK dependencies, the classes. So I think what I… just… just a heads up that I think next… after the V3 releases, we should update our dependencies, and then.
then, like, it would make sense, like, to follow up on Maxime's work here with the Auto demo.
Okay.
**Jared Freeze (Palo Alto Networks)** 03:32 Sounds good.
Is this… did we want to keep… like a web… This, I mean, the hotel demo has sort of everything in it, right? It's like a… An e-commerce store that's got…
**Martin Kuba** 03:51 Yeah.
**Jared Freeze (Palo Alto Networks)** 03:52 It's everything top to bottom, right?
**Martin Kuba** 03:54 Yeah.
**Jared Freeze (Palo Alto Networks)** 03:55 So, is he proposing… Is he here?
**Martin Kuba** 03:59 He's not here.
**Jared Freeze (Palo Alto Networks)** 04:01 Yeah, I guess I'll have to look at what he's proposing, but are we just gonna use the new SDK in here? He said migrate. I'm not sure.
**Martin Kuba** 04:09 Yeah, I think that's the idea. Yeah, just move from the legacy instrumentations to the new ones, to ours.
**Jared Freeze (Palo Alto Networks)** 04:16 Got it. Undercut.
**Martin Kuba** 04:19 I think he said that reached out to the, Demo… demo maintainers, but… Yeah.
So, let's see.
**Jared Freeze (Palo Alto Networks)** 04:29 Yeah, we have a demo maintainer, in our group at work, so, I can ask him, too.
**Martin Kuba** 04:38 Yeah, I think the big thing there is to, I don't know, like, what they would prefer as far as communicating this to the people.
That, there will be… It's a demo, but I'm… I know that… I know how… I don't know how people out there are using it, but it's gonna be breaking changes, obviously.
**Jared Freeze (Palo Alto Networks)** 04:58 I think from the feedback we've seen, like, people… are using our demo page when they're, like, looking at Browser, not necessarily the hotel demo, but for people doing backend work, they are probably going to see it first.
So, I'd be curious to see what the traffic is on that, but Yeah. I wonder if we can we had talked about this a long time ago, but like Oracle, I think, provides like a free.
a pretty solid free tier that we could host, like, a Groupon endpoint on.
Just to, like, point all these little demos at it, and just see what happens.
I don't know if we still want to do that. I mean, it's kind of ripe for abuse, but… I feel like everything kind of ends at this point.
So, okay, TBD.
Okay, let's see, so… Are the… Yeah, started doing some of this… started working on the migration plan.
Yeah, there's a lot of information here.
Yeah, he's…
**Martin Kuba** 06:15 He's been doing a lot of work over the last week, and I've been looking at some of his PRs.
**Jared Freeze (Palo Alto Networks)** 06:32 Yeah, I think, we definitely need, like, an overall, like, a kind of holistic review, because… I said this in the JSIG yesterday, but, you know, if we're recommending people switch, and we do this too, right, as a vendor, you know, we're relying on these, and we just need to call out exactly what the data model changes are, for what the data gets exported. So, it looks like he started to do that, or has done that.
**Martin Kuba** 07:04 There is a PR open for the migration guide.
**Jared Freeze (Palo Alto Networks)** 07:07 Yeah.
**Martin Kuba** 07:08 can find it.
**Jared Freeze (Palo Alto Networks)** 07:12 I believe.
**Martin Kuba** 07:20 Yeah, hold on.
**Jared Freeze (Palo Alto Networks)** 07:22 Yeah, it's it's it's one of these.
Yeah.
So I've got a couple up for contrib as well.
Let's see what he put here.
So this is the readme here.
**Martin Kuba** 07:48 Yeah, he was also asking one of the PRs, like, if you want to do, like, one sweep of the deprecation.
My take is that, like, once there is an alternative in our repo, like, we should just go ahead and do the self-deprecation in Contrib.
**Jared Freeze (Palo Alto Networks)** 08:07 Yeah, I'm okay with that. They… the JS SIG was talking about.
The big PR that's gonna update the dependencies.
So once JS goes out, it bumps to 3, and then 0.300.0, then the contrib… dependency bump for SDK Trace will go out.
Right away, and not have too much stuff in it, unless it's truly incompatible.
And then they're gonna hold that release until we bump all of the… failing code. They… like, we had talked about, like, jamming everything in one PR, or, like, stacking, and knowing that some of the tests are gonna fail until a few of the other instrumentations get upgraded. I think that was the idea, instead of having just a monolith.
And so… This may be… Part of that sort of sweep.
you know, in the… in the sort of second… the second PR before the first release of Kindred.
**Martin Kuba** 09:15 I see.
**Jared Freeze (Palo Alto Networks)** 09:15 I well, yeah. Well, I we need to, I'll keep a list.
We'll keep a list because there's there's a few of these. I have a few out as well, I believe.
Okay.
Oops.
Yeah, and then let's take a look at the guide real quick.
So I think there might have been a table here.
So…
**Martin Kuba** 09:54 Yeah, there's…
**Joaquin** 10:00 Yeah, but as you were saying, This is, like, a… how the code change migration guide, but there is no, like, how the output changes, which is what you were saying about, like, the new… Data structure and all that.
**Jared Freeze (Palo Alto Networks)** 10:18 Yeah, that's… that's what I… that's what I want to see.
I mean, it's basically required, you know.
So I think here, yeah, it's… it's… this is probably too generic.
Yeah, I mean, honestly, I'd… I'd… I'd want to see… yeah.
more spec… like, I want to see a table of, like, keys.
Yep.
I don't think that is here.
Okay, well, we can provide that feedback.
**Martin Kuba** 10:54 Sorry, like, you want… you want more details, like, about, like, what the shape of the data is in here?
**Jared Freeze (Palo Alto Networks)** 11:00 Yeah, because, I mean…
**Joaquin** 11:03 Like, a table with keys will be… Maybe easier to read, instead of all this text.
I probably say, like, this key is no longer here, this is a new key.
Or this was the… Span now is low, or this was a span event, now it's low.
Okay.
**Martin Kuba** 11:24 Yeah, he does.
Yeah, sorry, like, he does talk about that in kind of a generic way here, like, if you look at the… the…
**Jared Freeze (Palo Alto Networks)** 11:35 Yeah, like…
**Martin Kuba** 11:36 Yeah, if you go to the table, packages without the directive replacement.
**Jared Freeze (Palo Alto Networks)** 11:44 Sit up here.
**Martin Kuba** 11:46 Where is it? Keep going.
Yeah, here, here, this one.
**Jared Freeze (Palo Alto Networks)** 11:51 Okay.
**Martin Kuba** 11:51 The packages without a direct replacement section below.
So, like, for example, like, document load, like, it says that, you know, It's no longer a spy.
And it's replaced by these other three events.
**Jared Freeze (Palo Alto Networks)** 12:10 Yeah, I think one of the most, important ones is… The fetch no longer has the older keys for, body size.
There's two… there's two keys that are gone-gone. Like, there's no option to do the old CENTCOM.
I think those are extremely important, because we definitely have customers relying on older keys for third-party collectors that don't necessarily come straight to us.
I'd like to see that called out here, like, in bold. Like, hey, you know, you're gonna be missing data if you rely directly on these two.
So… I don't know.
Yep, okay, we can provide guidance on that.
Okay.
Okay, Martin.
**Martin Kuba** 13:17 Yeah, this one, we already had a discussion.
About this, I think, at some point… Last few weeks, this is about, Do we want to keep the span that represents document load?
And this issue kind of left it open.
without the decision. So I wanted to see if you can move it forward. So I'm added a proposal here.
And, you know, I don't… I can talk about this, but I think we discussed enough, what I'm looking for is, like, if nobody has objections, that maybe by next week we can… We can, we can… create issues, like, to go ahead with this proposal.
**Joaquin** 14:15 Yeah, I'll take a look.
**Martin Kuba** 14:17 Yeah, this is a big one, because that is probably the biggest change.
The document load instrumentation is… was very different previously.
But yeah, I'm I'm essentially, I'm proposing mostly to use events. But but there's 1 use case that that is, is in favor of having the the span, which is when the context arrives from the from the server that is serving the the web page.
So I'm proposing just having that one span.
But, yeah, take a look at this, and… If you have any objections, please comment on this, on this issue.
**Jared Freeze (Palo Alto Networks)** 15:05 Okay, cool.
**Martin Kuba** 15:08 This is… I opened this, to… Clarify… how we should, handle breaking changes, you know, specifically before we go to, to, to, 111X version.
Hector, this applies to, to your question about the, The apply… apply custom attributes.
callbacks that we were trying to deprecate or remove, so I wanted to just document this so that we can… we know how to handle deprecations going forward. So yeah, this is a proposal, again.
If you have any objections, please, please comment.
Yeah.
**Jared Freeze (Palo Alto Networks)** 16:02 Yeah.
what… yeah, what does experimental mean? Like, how nuclear do we want to go? I think one of the reasons, not… I'm not recalling exactly, but I think one of the reasons we did this is because it hadn't Been published yet?
**Martin Kuba** 16:18 Right, yeah, yeah, this one.
**Jared Freeze (Palo Alto Networks)** 16:19 Yeah. Not yeah. Not to defend myself, but I I think it I think the name was not released.
**Martin Kuba** 16:27 I think so, I think that's right, yeah.
But yeah, but you wouldn't want to go back and and like, take it as a precedent, you know, so.
**Jared Freeze (Palo Alto Networks)** 16:34 No, for sure. For sure. I mean, that's so circumstantial. Yeah.
Okay.
Okay.
Sounds good.
Oh, yeah, Hector, this one was interesting.
**Hector Hernandez** 16:48 Yeah, I agree with this issue.
was pretty much trying to help with the migration, I realized that the resource detector is not there, so I just didn't realize, okay, maybe there's some open issues, open questions, open decisions here.
Because I can see that you guys do not accept the resource detector as a parameter as well. So, that's why I created this issue, is just to… bring up the conversation, if that's really the case. If it's already decided, you just let me know, and… but.
One of the… The things that mentioned here is also about adding defaults and stuff like that.
I can tell you right now, we don't want to have this as default for Azure Monitor. Most of this calculation is done in the backend for us.
using the user agent, so… but it's always nice to have… there's some customers that need this kind of information from the browser, so we definitely want to have it. But it's more about deciding, do we want it, by default? Do we want it to be passed for… we have, like, multiple initialization entry points right now, right? Depending on what you want to use. It's, like, logs, or only traces, or the entire thing. We want to allow people to pass this. I also saw this to-do that David added, I think, is, like, to-do.
decide what to do with resource detectors, so that's why I created this.
Yeah, if you think it makes sense, I can give my opinion about every single thing here, then people can comment on that.
**Jared Freeze (Palo Alto Networks)** 18:30 Yeah, I mean, I think that would be good. Yeah, let's… looking at the code.
**Hector Hernandez** 18:36 I just wonder how many of these are gonna…
**Jared Freeze (Palo Alto Networks)** 18:38 have, you know.
**Hector Hernandez** 18:40 Yeah, this is just moving the code. It's not… you need to initialize it and pass the attributes right. It's not integrated in the in the initialization yet.
**Jared Freeze (Palo Alto Networks)** 18:54 Yeah, I think you added it here, so what that would look like… Well, I mean, I think we've all seen the demo, but yes. Yeah, it'd be good to know what your thoughts are, specifically.
**Hector Hernandez** 19:09 Yeah, definitely. Happy to add some… my opinions there.
**Martin Kuba** 19:16 And by the way, there's a… there's another package with, with a separate set of… Resource detection detector.
For, like, the use… There was one in the CoreJS, and one was in Contrib, so…
**Hector Hernandez** 19:33 Oh, really?
Oh, okay.
**Martin Kuba** 19:36 Yeah.
**Hector Hernandez** 19:36 Yeah, there's so much things going on. Okay.
**Jared Freeze (Palo Alto Networks)** 19:39 Yes.
**Martin Kuba** 19:40 Yeah, and they're not the same, so… Okay.
Okay.
**Jared Freeze (Palo Alto Networks)** 19:51 Oh yeah, this one as well.
Can bring that up next week.
Is async compression.
PR, forgot about that one.
Okay. Does anybody else have anything?
Not on the list.
Okay, cool.
I can talk a little more about the V3 migration that we've been working on. So SDK Trace Web is gone entirely.
So, a lot of it really was just… shifting the… some of the APIs out of, like, SDK logs.
into… just SDK, or into the API. or, excuse me, API logs into API. So, a lot of it was kind of just a find and replace. That was a big part of it. Sdk trace web was the larger change, and we actually saw that.
I have an open PR against 3.0 in our vendor repo.
And one of the bigger changes is the, the register function.
when you're using the Stack Context Manager and all that good stuff. So, I can post that next week after this goes out, as an example for others.
Claude's pretty good at attacking that sort of stuff, once the example's out there, but it might be good to see, just generally. It actually… things get easier, it's actually less code, but it… It's a much different approach, so… And post that as well.
So… And… yeah, I think the… Contrib ranges too, I mean, we're gonna have to be really careful about.
Guidance on instrumentation, on altering instrumentation, because I think that some of the work.
we've been doing in the Browser repo around instrumentation base, so the one that David commented on and said I went totally overboard, which is fair, because I said the same thing. I was trying to accommodate everybody all the time in every single way they want to enable and disable instrumentation.
The funny thing is that I had a DM going with, Trent, and he just wrote, like, why do we even do this? Like, why do we do any of this? Why on earth would we enable or disable? Like, if you… register instrumentation, you're saying, I would like instrumentation. Like, what is the point? And the case I made is that, you know, we do actually care about GDPR. That is a model that I think lends itself well to enable, you know, to sort of instantiate disabled.
Now, the question… I'm not… I'm not in the EU, I haven't done this specifically, but I think initializing everything and not sending telemetry is probably… like, legal, it's probably something you're allowed to do, as long as you don't send the telemetry. I think sending the telemetry is probably the issue, not necessarily, like, collecting in memory. I don't know if that's the case.
That's also… that could be something people do not want to do, because they're using resources to do that, so that was kind of the other part of it, is, like, what does initialize mean, and then what does enable mean? So, enable to me was, like, export, like, exporting the data, truly, and then initialize was kind of, like, patch fetch, but don't actually do anything with it yet.
that's… so thank you very much for that, response, David, but I would say that's probably the big difference between Node and Browser, is that, you know, on Browser, you might actually want to be ready, you know, and then the second somebody hits the, you know, accept performance cookies, that you're just ready to go. You know, that you can just flip the switch.
Now, could you also do that with register instrumentations function, or just adding them to the array? Yeah, you could do that too, and then there's… You know, I but at that point, I guess you also have to keep track of the instrumentation itself.
And then use the callback to disable it, instead of having an explicit .disable.
So I do think that's kind of convenient, you know, I don't know what others think, but I see the case.
for keeping it on web, you know, even if, you know, Node is saying, I know what state I'm in on the server, like, just don't use it on the server, or whatever. Oh, the other… the other thing I realized was, like, I think on some pages, especially slower pages, when you have runaway telemetry, and I say runaway, like, 2,000 events.
not necessarily, like, a bug, but it's just a lot of data, and at a certain point, you're just like, okay, you know what? I don't care about this any longer. This session has just got, like, plenty of data, this is an anomaly. I am a customer, I'm gonna stop paying for logs.
Like, I only… I never want a session with more than 2,000 logs or something like that. Now, you can cap it and drop it, but also just, like, turning it off to sort of take the burden off of the page, I think is important.
So, you know, for those reasons, I was kind of like, we should probably keep enable-disable for ourselves.
But as far as passing enable and disable.
during instantiation. I think that was sort of the detail that we were getting into on that PR, so… I'll try to work a little more on that after, 3 releases, because… The Browser repo itself, I think, should bump to 3 as a minimum.
And then… My preference would be provide guidance that you should not be basing.
Browser instrumentation on core JS repo any longer.
like, when we stabilize our instrumentation base, we say, hey, if you're using Browser Repo, third-party Instrumentation that you may have at your company or coming out of core.
or contrib, if you really are relying on the old fetch. The old fetch will be supported by 3.0, but the instrumentation base will not be.
exactly the same.
And I think that's important for us not to try to match the interface for back-compat reasons. That's the whole point of the Browser repo.
So that's… that's my two cents on this. And then I think it's just a documentation problem. We just say, hey, you know, if you are using the new Browser SDK, and you have old instrumentation, like, just know that it's gonna be breaking, and that, you know, if you'd like to update your you know, customer versions, that's fine. You know, and I know as a vendor, we're having to do that work as well. We're actually going to do a major bump to be able to move forward with Browser Repo Libraries, and to be able to modify our stuff, and then upstream that as well, because we have some other instrumentation I think would be good for the community, so… That's the long version of… I should work more in instrumentation-based. Yeah, Mike, you have a question?
**Mike Kozicki** 26:52 Yeah, just to touch on something you had mentioned for basically consent management, is it something that we would plan to include as part of the SDK with, you know, simple cookie consent management and collection consent? Or is that going to be something that would be part of the people building on the SDK?
**Jared Freeze (Palo Alto Networks)** 27:16 I like that a lot. Yeah, I mean, the whole point of the Quick Start SDK is to have helpers, so I think disable all, enable all would be really useful.
**Mike Kozicki** 27:25 Okay.
Is there an issue for that? I couldn't find one, I just… before I…
**Jared Freeze (Palo Alto Networks)** 27:30 there.
**Mike Kozicki** 27:30 anymore.
**Jared Freeze (Palo Alto Networks)** 27:31 There is, there is not. Yeah, that'd be great to have.
**Mike Kozicki** 27:34 Okay.
Alright, thanks.
**Jared Freeze (Palo Alto Networks)** 27:37 Yeah, for sure.
Yeah.
**Joaquin** 27:40 I agree on having, like, an easy way of disable or enable everything, but I don't think we should go as far as having a… Take the cookie butter thingy.
Managed by the SDK.
Like, maybe that's pushing too far off what the SCK scope and responsibilities are.
like, we should make it easier for people doing that, but then, like, having UI embedded on the SDK, eventually someone's going to try to change that, or need a different UI, so we will have to expose a way of changing the text, or changing the UI, or whatever.
So I think it can be problematic.
**Jared Freeze (Palo Alto Networks)** 28:19 Yeah, I think I would.
I would probably encourage people just to add.
something to the demo that they can copy and paste, but yeah, just the callbacks only would be in the SDK.
**Joaquin** 28:30 Yep.
**Jared Freeze (Palo Alto Networks)** 28:37 It's a… Okay, we're at time. Anybody else has anything else or doesn't? We can Wrap it up.
Okay, cool. Well, we'll post in the Slack channel about the 3.0 release, and just status updates since we meet on Thursday and the release is Monday.
I'll try to cross-post, but, OTEL JS Dev is where the development for Core happens, not OTEL JS. So I'll post a link to that as well if, you know, you guys are not aware of that.
Okay. See y'all next week.
**Hector Hernandez** 29:17 Thank you.
**Mike Kozicki** 29:19 Oops.
