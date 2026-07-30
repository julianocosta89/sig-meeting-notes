SIG: Ruby SIG
Date: 2026-07-28
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Kayla Reopelle** 00:29 Hello!
Hey, Matt.
**Matt Wear** 01:10 Whoa.
**Kayla Reopelle** 01:21 Okay, I think this might be all this for today.
Yeah, so in the spec SIG today, I was able to go. The thing that felt the most interesting to me was the span type discussion.
And… It's kind of this idea of adding… One more, attribute to spans.
The… the type. And the type would be different from kind… Because it's a little more specific, and it doesn't require… kind of combining… Both span kind with some other attribute to determine a span's type.
I'm trying to find where in here… So, like, HTTP server request, being one example of a type, or DB client call. So, instead of needing to… you know, figure out that something is a database spam from another attribute, or the spam name, or something like that in the payload. You can just come… you can just look at this type instead.
So that's something that's being discussed. I guess, was there any other elements of this, Matt, since you were also there, that, you want to touch on in this meeting?
**Matt Wear** 03:01 I don't know, I feel like there was a lot of conversation about whether a span can be classified by a single type.
Multiples, like, an array of types was necessary.
Yeah, I don't know where any of that really went, and I… I do kind of feel… feel the pain in that situation, when you're writing instrumentation, like, not really knowing If your span fits directly into one box, you know?
**Kayla Reopelle** 03:31 Yeah.
**Matt Wear** 03:33 Bones.
But anyways.
In general, like, yeah, I think it's a good idea, and I think we'll probably end up moving forward with this, just… I think it will be a huge benefit to, like, backends being able to easily, you know, identify what kind of span this is, rather than just trying to kind of, like.
Match on various attributes and guess.
**Kayla Reopelle** 03:58 Yeah.
So true. And I think it helps, too, with verifying that the semantic conventions are in order, because if, you know, every convention group kind of has one type, that might make it easier to tell what something is supposed to be.
But yeah, I'm curious where they'll land on the multiple types versus single type, debate.
That was the main one I wanted to talk about today. Was there anything else that you think we should… look at…
**Matt Wear** 04:40 No, I don't think so.
**Kayla Reopelle** 04:43 Okay.
I'll put this in the meeting notes… Okay, so… In core…
**Matt Wear** 05:05 Yeah, I dropped this one on here, because I.
**Kayla Reopelle** 05:07 Okay.
Sweet.
**Matt Wear** 05:09 Yeah, I feel bad, but I just kind of got around to looking at these two PRs, dealing with decorative config, but… At the same time, I think these… landed just before I kind of… had time to get back to hotel, so… I don't know, I've been working my way down in the pull requests, and sometimes it's hard because things… creep back up. But anyways, Yeah, I saw that, Xuan, you have, like, a PR that's pretty far along in… Implementing declarative config for, for trace… for the trace machinery, And that, that James has kind of a, I don't really want to say it's an alternative, but was just looking at some different aspects of declarative config, I think both of them I think some combination of both of those approaches probably actually fits what we're looking for.
But… Yeah, I just wanted to talk about this a little bit to see if… you can… Try to align on… on some direction, to move forward, just so that this work is… is unblocked, or… Yeah, I'm not sure if this work has stalled because it is kind of blocked, or if, it's just not important at this point in time, but… Pose.
But, yeah, I think, I don't know, I just kind of wrote down my… my thoughts, and I think with… I think, Xuan's work is on the right track, making this a separate gem. I do think that, like, the ergonomics could be just, like, a little bit better, so I kind of have just this code snippet of how… of how those could actually look. I think, Xuan, your work really kind of, is very similar to, like, what is in the Go SDK, and in the Go SDK, you… of… you basically configure an SDK, and you get back just an SDK object, and then you take that SDK object, and then you… Use that to manually kind of set the globals, like the global tracer provider, meter provider, etc.
And I was thinking that… we could just have, like, an open telemetry config… configure, and that will construct the SDK, and then actually set the, set the globals for you, so you don't have to do that extra step.
And that's kind of what those three steps are that I'm kind of showing below here.
you'll parse the YAML, you'll create, so that will kind of be, like, the thing that returns an SDK, and then install will actually take that returned SDK and, Assign it to all of the proper globals, and… in the, yeah, for the application.
And then, I think that the work that James was trying to do was trying to just make sure that all these, like.
top-level components own their children, so that config can, like, kind of pass through, like, the tracer provider, and then, down to, kind of, the things that nest below that, if I was understanding his work properly.
And I think that makes, Yeah, makes… makes it a lot easier to kind of assign the config.
And then… What else? I feel like I had one more thought here.
Oh, yeah, he… at least in the draft PR, it kind of looked like he was trying to make the configurator the thing that applies to config, but I'm not… based on his comment below, I'm not sure that that is really… was the intention, because he sounds like he's on board with a separate gem.
And, Yeah, I think a good end state would just be the SDK has, like, the SDK components, like, the configurator is kind of there for now, because we've had it and people are using it, but eventually, when we get the clarity config working, that would be a separate gem, and… I guess we'd keep both of them around, or we could consider retiring the configurator at some point.
Or somehow rolling that into the configuration gem.
leaving just the SDK as, like, the raw components, if that makes sense.
And then… Yeah, lastly, I was just thinking about environment variable handling, and I was thinking that we needed to kind of get all of that out of the components, because they kind of read that at construction time and just, like, lift that up further, so it can pass it back down and… James was saying, leave it, leave it in the components, but it would only get applied if config wasn't pass in, and that… that actually sounds fine to me, so I don't have a strong feeling about how we handle environment variables, as long as we get the right behavior out of it.
So, I don't know, I just said a lot. Does anybody have… Thoughts on… On this, and just any, like… I don't know if we've discussed this stuff before, and I wasn't around. Oh, just idiot.
Any past conversations?
to know.
**Xuan** 11:02 Yeah, so… Yeah, we had a lot of discussion before, marked them all resolved, but if, I'm not sure if you have a look at them. So he wanted to… he really wanted something like a custom components.
That's something that the Java and the PHP can do.
Those components are something like, for example.
If you, if you said something, like, neurotic, processor that, You can automatically detect a newer processor and something.
Some kind of, customization, I think that's what he wanted to have, and I clearly state that it's not easy to do with Ruby.
I'm not sure… I haven't… I only scheme, like, quickly look at it is, drafted PR.
Yeah, I looked at it a few months ago, I probably need to look again to see what he's trying to, to do.
Yeah, and then, I probably also needed to read your comments, and I also saw your comments on my PR as well.
**Matt Wear** 12:34 Alright, yeah, that's useful. I didn't read all the resolved comments, and I wasn't aware of this, Wanting to be able to kind of, like, discover, you know, various, types of components.
I don't think that's totally impossible with Ruby, but… I'm not… sure that it needs to be in, like, a V1, for example, you know, like… if… If our initial work for this Oomph.
Could configure any of the, or all of the SDK components, I feel like… We can always extend this a little bit later.
I mean, I'm sure it would be some changes, like, underneath, but… I don't know, like… Having not looked at those comments, and having not thought about this all that much, but… I know, like, Ruby has this inherited hook, so if there's, like, a common kind of base class for all, like, you know, processors, exporters, whatever.
you could… You know, use that inherited hook to, like, To maintain, like, a registry of, like, what's actually available, and use that to install.
But… But I don't know that that needs to be, like, in… in V1, unless, you know, whatever we take.
whatever approach we take for V1 kind of, like, paints us into a corner, you know, to make that impossible.
Homes.
**Xuan** 14:13 Yeah, I mean, it is possible, it just needs to take a lot of work and considerations to make things, easier for users if they want to customize this, component.
**Matt Wear** 14:30 Do you think it's possible to kind of ignore that for V1, but not…
**Xuan** 14:33 Yeah, yeah, yeah.
**Matt Wear** 14:34 but not, like, you know, paint ourselves into a corner to where it's not possible, because I feel like that would… Boom.
**Xuan** 14:41 Yeah, yeah, we can, definitely. Yeah, we can.
definitely put this as, like, part of a roadmap, or, like, another milestone for this, the current application is.
Yeah, and I… I just need the time to look at the comments you have for this, like, But usually I would say something like that. Oh, I needed to take a look at,
**Matt Wear** 15:11 Yeah.
Most of those comments were not, like, big deals, on… on your PR, I think, like, the biggest one is that were… We're kind of auto-generating all of the kind of config classes.
Yeah.
We're doing that in the top-level namespace, which I thought was a little dangerous.
**Xuan** 15:36 Yeah, yeah.
**Matt Wear** 15:37 Yeah, they're all minor things. I think, like, one thing that would be, like, nice, though, is, I don't know, kind of this… Code snippet that is on this issue is kind of, like, making Making that just, like, a little bit more ergonomic, so you don't, So the user doesn't have to kind of worry about getting back the SDK, and then assigning the SDK to the globals. That is kind of like…
**Xuan** 16:04 Yeah, yeah, I was, actually, I had a, so I made a lot of edits for my, on my original PR, so, before, I think the first, like.
first a couple… couple comments. I actually… do this, like, I… pack everything into the, like, you don't have to define, have to have to, give, get this tracer parameter or meter paradeter from this, other, authorized, care configuration that… Oh, and then I, I think James points out something, and I look at the spec.
Yeah, it says, it has to return those, those, component… those meters and the riders.
then, I, I can, I can, I can, I can, commence also.
those, on specs, on the comments, but… And then after that, I switch to return those values, and the user can just, If they wanted to have this vote.
auto-generated… traditional or metaphridor, then they can do it, or they can just use their own.
So… Oh.
I, I can't, I can't write something down that we can, discuss further about, how it works.
But I'm okay with both. Either users have to do it by themselves, or we could do it for them.
I think they are fine, because we still can change the global, Trace provider or a video provider by themselves, if they really wanted to do.
Yeah.
**Matt Wear** 17:46 Yeah, yeah, I think the spec, does have it kind of returning an SDK, so that would be kind of like this create function, and then I feel like our install function, that's just kind of like one convenience, you know, it's a convenience function, convenience wrapper over all of that.
So that, you know, we can set everything up for them, but if they would rather, like, do something more manual, they can… We can expose, you know, all of those, other methods. So I think the spec will probably, you know, prescribe Bum.
some of the methods and the return values, but I think there's nothing stopping us from wrapping that in some convenience in the end, if that is going to be what works best with us.
But… But yeah, if… yeah, if this is stuff that you're interested in continuing to work forward, I think the main reason I brought this up was just to have some discussions to try to get it, like, unblocked and see if, like.
us and James and everyone can kind of get on the same page as to, like, how to move this forward, and just kind of start… start moving it forward, because I think this would be… Helpful to have.
**Xuan** 18:56 Yeah, yeah, definitely. I think this one, because I took a, this, declared configuration, I think the… it's only, I think the… from my perspective, I think the most beneficial.
And how this is to, when users have a lot of reviews, instead of a… creating those views in their code, they, they can just have this conversation, it's easier to, keep track on all the views, to, they, they, they created. So, LSS, is, beneficial.
Another, another thing I want to point out is those, generated, generated, constants, so I, I wasn't aware all those, components, in Go, they are all generated, so that's why I also kind of want to have these generator constants here.
This kind of, to, make sure the… The structure, is, in the span, so… Although those are generated, So, which means, every time the upstream, they update their, like, the current configuration.
YAML file, like, spec, then I would have to really generate this, which is kind of annoying. It's something like, CENCOM, so… Yeah, that's something I wanted to bring up, those, Constance.
**Matt Wear** 20:33 Yeah, yeah, I saw that they're being generated, and yeah, we'll have to come up with something, to make that as… painless as possible, but I think… What you have for now is working.
**Xuan** 20:47 Yeah, yeah, I basically asked, ask, AI to… to help me to create those, the function intuition and stuff. They really are pretty, system, systematic, Yeah.
**Matt Wear** 21:14 Oh, yeah, that's all I had, I just wanted to kind of bring this up. So, like, if you've had a chance to kind of… look at those comments on your PR, and if you… I don't know if, If ultimately you want to have some more discussions on this issue to kind of, like.
plot the path forward, I'll try to be active and responsive to those.
**Xuan** 21:40 Yeah, okay, I'll, I'll take… Look, I'll… I'll stream.
The peers, and then the issues, and then, yeah, I'll respond. I'll… yeah.
**Matt Wear** 21:51 Cool.
**Kayla Reopelle** 21:53 Awesome. Thanks for bringing this up, Matt. I haven't had a chance to look at it yet, so I'm glad that we're working on moving it forward, because I do think this would be a really helpful feature.
**Matt Wear** 22:05 Yeah, no problem.
**Kayla Reopelle** 22:11 Okay, let's see… So, I think I added this one… And… I think… I don't remember why I did.
Let me see what some of the other issues are, maybe that… I think I might have copied a strange list onto the agenda, so I'm sorry about that.
So… Here, I think this one is maybe just a little bit stuck, and I'm not sure if this is something that we actually want to do or not, and whether we should leave this open more, because it's been tagged with the stalebot a few times. But the… the question is whether we should allow, Errors to be… Raised record invalid errors for save, create, and update with Bennings.
It seems like from… the spec with, like, control flow and inspection. I like what Arielle said, that, You know, we might not actually need… To do this, but, you know, Yeah, I'm sorry, I'm not really sure what's… what to do here with this one, so… I should have been a little more prepared with these. I think we can postpone discussion on these, because I don't really have anything specific.
for them today, they were probably just issues that I saw that felt a little blocked.
before I just close the discussion entirely, does anyone have any… like, initial takes or thoughts on… on this topic? I know it kind of is out of the blue.
**Matt Wear** 24:43 I'm just trying to scan it to see if I have any thoughts, So the issue is, currently, as instrumented, it's like these… bang methods do not have, like, an error associated with the span, because the Error actually technically is happening after the fact.
Or because we're rescuing it?
No, we're not rescuing. The rescuers must have.
**Kayla Reopelle** 25:44 Yeah, I think it's the inverse, that they… that we're recording these errors right now, and they don't want them to be recorded. They don't see, like, record invalid as something that should have an exception event.
**Matt Wear** 25:56 pricing.
**Kayla Reopelle** 26:10 But, yeah, I think… We can postpone this one for another time.
**Xuan** 26:17 I feel like this is another piece that, if the user wants something that's special, customized, they can do it on their own, with the… Processor, oh, better.
**Kayla Reopelle** 26:29 That's a great point.
**Matt Wear** 26:33 Yeah, yeah, I do feel like this is something you could filter out in a collector, for sure.
And… Yay.
Given that only this user seems to be, be talking about it at this point in time, I think.
It's probably safe to suggest that, and… I guess one thing that usually ends up happening is if Something is really necessary, it will get brought up more than once.
So I feel pretty comfortable if there's, like, a alternative, As long as we can suggest one, then… suggest that.
Okay.
**Kayla Reopelle** 27:23 I guess for that, then, would it be recommending, like, a custom error handler?
That excludes this, or… Does this seem like something that a sampler or a span processor would be better equipped to handle?
**Matt Wear** 27:47 I'm thinking more, like, collector side, I feel like you could… Just drop these fans at a collector.
Oh.
And… generally, like, it gets tricky if your spans are in the middle of the trace. If you drop them, you're going to break the trace, but these are usually, like, leaf… Should be leaves, I'm guessing, so I don't think… that, That should… there should be a problem with that?
**Kayla Reopelle** 28:20 Yeah.
That makes sense.
Okay, great, thank you.
I removed the other two because I'm not quite sure what the context was there, so, we can talk about them later on.
Okay… We have this one.
When did you add this one?
**Xuan** 28:51 Yeah, this is just a, very simple change, because, Oh, there's some code. They upgrade from… 0.22 to, to 1.
And then, they don't have this… option anymore. And they actually… this SIM code running is, is, like, this function wraps the coverage running, so… Yeah. What Jim suggests is a totally different thing, I… I don't… I don't really think that's… that's necessary for this, for this, fix.
Oh.
Yeah, that's pretty much it, yeah.
**Kayla Reopelle** 29:32 Nice, thanks. Is this what you'd recommend? Because I think our SimpleCov implementation is pretty similar in other… repos too, do you think that that would be the right solution there as well?
**Xuan** 29:46 I… I'm not sure, because I think… I think he has, his, approach for the change, but to be honest, I don't… Because ACP are so, so big, I don't know which part to look at for this particular change, so…
**Kayla Reopelle** 30:03 Okay.
**Xuan** 30:04 Boom.
Yeah, I can, I can take a look, to maybe comment on his, on his peer about this account update.
**Kayla Reopelle** 30:14 Yeah, that would be great, since you already looked into what it would take to upgrade to 1.0 for this one. I'd be curious about your thoughts on his other…
**Xuan** 30:23 Okay.
**Kayla Reopelle** 30:24 Thank you.
Okay, nice. Is there anything else that people want to talk about today?
**Xuan** 30:37 Oh, yeah, so, I have a, one PR about the update, agent, markdown, in the quarrel, kind of like that to, to, be reviewed.
The reason I brought that up, because if you look at the… look at the list, the new, the latest PR on the, sorry, not core, and look… uncontrolled, yeah.
Yeah, if you notice this person, the PR is very, very interesting. The first one, yeah.
Yeah.
Yeah, what is the path to helper produce?
No, no, it's in the, in the, in the root file, root folder.
You can see the path to helper.
**Kayla Reopelle** 31:23 Oh, yeah, yeah.
**Xuan** 31:25 It's a… it's just… yeah.
**Kayla Reopelle** 31:29 I wonder… yeah, I feel like that might just be… A mistake?
Of, like, maybe something in their fork?
**Xuan** 31:41 I don't know. But anyway, I'd like to have this AI edge agent to, in the country.
**Kayla Reopelle** 31:47 Yeah, yeah.
And we do already have, I think, maybe even, like, 2 other pull requests open for this specific… Issue?
Yeah, there's, like, 3. I think this one seemed… Closer… It does have two reviews on it right now, so it might just be something we… end up disregarding… Entirely.
Yeah, there's also some concerns.
But, that is an interesting… Yeah, red flag for AI implementations, because it doesn't seem like they ran the tests.
Was there, like, a process you wanted to propose for when we see things like that, or… Aww.
**Xuan** 32:53 Oh, I don't know.
Oh… Alright, I don't…
**Kayla Reopelle** 33:00 Yeah, no problem. I just wanted to make sure that I had, like, addressed… addressed your point fully.
**Xuan** 33:05 Yeah.
**Kayla Reopelle** 33:06 Cool.
Oh, cool. Thanks for calling that out.
Okay, well, if there… Isn't anything… Else, then maybe we call it here. We can walk through all the issues and PRs, if y'all want to.
Okay, then I guess let's call it for today. Thanks, everyone, for coming, and for the great discussion on the, config.
declarative config work.
**Matt Wear** 33:59 Thanks.
**Xuan** 34:00 Okay, thank you.
