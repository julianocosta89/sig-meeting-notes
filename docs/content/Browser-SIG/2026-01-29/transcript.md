SIG: Browser SIG
Date: 2026-01-29
Duration: 26 minutes
============================================================

## Zoom Recording Transcript

**martinkuba** 00:20 Hey, Jared, how's it going?
**Marco Schäfer** 00:21 Everyone.
**Jared Freeze** 00:23 What's up, Marco?
Jesus, one dance.
They said they weren't coming? Was it David?
**martinkuba** 00:36 David, yeah.
**Jared Freeze** 00:47 Also known as a shared solution.
**martinkuba** 00:49 I'm not sure if, if,
If that's gonna be able to attend today, we're going to the hotel unplugged.
which is Monday, and Fosden.
Conferences.
So he might be traveling. I'm actually going… I'm going there tomorrow.
**Jared Freeze** 01:12 Excellent.
**Marco Schäfer** 01:21 So you have the whole weekend to visit faster anyway.
Oh, nice.
That's cool.
**martinkuba** 01:28 Have you been at Foston before?
**Marco Schäfer** 01:31 No, not, but I would like to. Yeah. But they have, like, in Belgium, there is a strike, like a public transport strike, so…
**martinkuba** 01:42 I don't know.
**Marco Schäfer** 01:42 hesitating a bit going… I mean, it's only a four and a half hours train ride, but…
**martinkuba** 01:47 Right.
**Marco Schäfer** 01:47 It's… It's too dangerous, like, that I…
Can't make it, can't make it.
**martinkuba** 02:33 Okay, I guess we can get started. I don't know if anyone else is joining.
So I do have, three topics, the first one…
Just a quick announcement that,
We merged the navigation timing, instrumentation.
Thanks, Marco, for working on it, and thanks, Jared, for the reviews.
I think that's a win.
The other thing… we have,
There's a PR for the council instrumentation.
And I think what's blocking it now is,
Is the conflict with the diagnostic, diagnostic… Logger?
That Mark, commented on.
And I would be just curious, like, if we have thoughts about how to solve this.
Let me see.
**Daniel Dyla (Dynatrace)** 03:34 diagnostic logger built into the API.
**martinkuba** 03:38 Yeah, the SDK, I think, is probably used in the SDK and API, yeah.
**Daniel Dyla (Dynatrace)** 03:41 Yeah, it's used in both. It's built into the API.
Yeah, I've… always hated it, to be completely honest. The way we solved this with…
Because you have the same problem with, like, exporters, you know, if you have tracing enabled and the exporter makes an HTTP call, we set a context object.
As far as I know, all of the… diagnostics, like, API…
Stuff is, it's all synchronous.
I don't think there's any async work done at all, so you should be able to just set, like, even a global Boolean, or, you know, whatever.
**martinkuba** 04:23 Yeah.
**Daniel Dyla (Dynatrace)** 04:23 Have it read in the…
And, you know, I'm sure that you could wrap that in a convenience method of some kind to… you don't want users to have to call that or anything like that, but,
To avoid the… the loop.
**martinkuba** 04:40 So do you mean global, like, in the API?
**Daniel Dyla (Dynatrace)** 04:47 I mean, wherever. It hardly even matters. Like, you could create a global, like, just a global variable.
I don't think it necessarily needs to be stored anywhere… Right, because the…
Oh, I see what you're saying. You want something that would be automatically picked up by the SDK?
And ignored.
**martinkuba** 05:18 So, I guess… Yeah, I mean, so I looked at the one…
there are a couple of things, so I think there are two options that I was looking into. One was, like, global in the console instrumentation itself.
Like, when it's calling logger.
You know, that log to create the message, like, then basically say, like, if you re-enter here.
synchronously, right? Like, then ignore. So… but that doesn't work because the exporter is async.
Right, so, like, even, like, you will block synchronous…
Re-entry, but not… not asynchronous, like in… if the exporter…
So… so I guess the other option would be, like, and I think that's what you were describing, is you have this,
This… Tracing? What is it, like… Suppressed tracing option.
So, like, maybe something similar like that that's, you know, that's sad globally.
For everything.
**Daniel Dyla (Dynatrace)** 06:35 I'm assuming.
**martinkuba** 06:35 And then the instrumentation would have to be looking for that, right?
**Daniel Dyla (Dynatrace)** 06:39 Yeah, and the diagnostic logger would set it.
**martinkuba** 06:43 Okay, yeah.
Yeah.
**Daniel Dyla (Dynatrace)** 06:47 It's not so… there have been a bunch of, Attempts to…
standardize that, like, suppressed tracing thing, because it's useful for a lot of other things, this included, but it never really goes anywhere, because too many… there's too many different use cases to solve. So it's not in the spec or anything like that.
But I think if you duplicate what was done for tracing and just have suppressed logs.
I doubt anyone will complain.
**martinkuba** 07:23 Okay, okay, that sounds simple enough.
Yeah, I did, let me just, the other options that I thought of is, like, the diagnostic logger has… you can set the logger itself.
the logger implementation.
So we could have our own logger implementation in the instrumentation, and, like.
It would say, like, if you use this instrumentation, like, you have to use this logger.
Instead of the default one.
But I think this… This global is probably a safer and better option.
**Daniel Dyla (Dynatrace)** 08:02 Yeah, cause you'd run into the…
Yeah, I think… I think relying on using a different logger… there's too many ways that could go wrong if somebody accidentally, you know, calls the wrong one, or… Yeah.
I guess you could make it reliable, but this just seems more straightforward to me.
**martinkuba** 08:23 Yeah, okay, cool.
That sounds easy enough.
**Daniel Dyla (Dynatrace)** 08:34 I would…
personally, and, you know, this isn't the right group for it or anything, but just to say it, I would personally get rid of that diagnostic logger entirely from the API if it was up to me.
**martinkuba** 08:50 Is it, like, useful to users, and why would users have it in production?
**Daniel Dyla (Dynatrace)** 08:57 Nobody enables it in production unless they are having some problem. I shouldn't say nobody, some people do.
But for the most part, it's off.
Most of the time, unless you're having some problem. And the idea is, like.
If your tracing is so broken that you're not getting any exports, like, you need something to, to be able to figure out what's happening.
**martinkuba** 09:23 Right.
Okay.
Yeah, the comment that Mark put in, put in that,
PR, he made it sound like
It is, and it can be enabled in production.
Which… I guess it can.
**Daniel Dyla (Dynatrace)** 09:42 We didn't want to just call the direct console log, because, you know, That would affect…
User applications sometimes, so we wanted to make it so that they.
**martinkuba** 09:52 We're able to configure specifically where it went to.
Yeah Okay.
Okay, sounds good, and then I have,
Opened… God, let me share my screen real quick.
I can see the… The agenda.
Okay, this issue for… Release and versioning…
So I just, wanted to call it out that,
This is kind of key for us right now, like, we need to…
Set up to… make some decisions here.
We discussed the version interest strategy.
But I think the next step is,
Decide on, like, what, what tooling to use, and, like, what process to use for…
For release and publishing.
So, I… I don't… I do have an opinion on the versioning strategy. I know that, Jared, you said here that you would… you think they'd be… they should be…
in sync, but I think the opposite, actually.
I think, like, we should be, you know, for instrumentations, especially.
We should… we should be able to have independent versioning so we can…
Stabilize them on a different cadence, and we can…
publish them on different cadence, like, similar to what Contrib does.
I think that's what we discussed in the past, also.
Yes, Marco?
**Marco Schäfer** 11:46 I have a question, how are the rules, then, for, like, backwards compatibility, like, between different package versions? Like.
Because if they update independently, like, how is the contract like for supporting, like, or ensuring that all the different versions can work with each other, or, like.
isn't there anything like that? So, like, always, like, only the most recent versions are guaranteed to work together.
**martinkuba** 12:22 Well, so my thinking was that, like, the instrumentations really are separate,
they have dependency on the API, which…
like, similar to, like, what Contrape does, is,
Peer dependency that has, like, on a range.
Yeah, I mean, can we think of, like, a use case, like, where the instrumentations would need to be in sync, I guess?
**Marco Schäfer** 13:05 Good question. I think I don't have a use case on that.
**martinkuba** 13:13 Yeah.
**Jared Freeze** 13:18 I can look into the custom ones we have and see if there is…
This, you know, this sort of setup.
And let you know. I can't think off the top of my head.
**martinkuba** 13:33 I mean, so we do have dependencies also, like, the instrumentation package has a dependency on the API, it also has dependency on the instrumentation package, which is in the CoreJS.
And we will also have, likely, like, a common package.
Which will contain… right now, it contains the…
I like the session management, and some… some, like, util… utilities.
So that… that will be some dependency between that and instrumentations.
**Jared Freeze** 14:13 Webcommon, maybe?
**martinkuba** 14:14 Rob common, yeah.
**Jared Freeze** 14:16 Yeah, if you pull in, like, a helper function from Webcommon and…
You're just using an older one, and you have not pulled it in.
That will be a nice view.
**martinkuba** 14:26 Yeah.
Alright, well, it's maybe something to… to think through some more.
And then, I guess, I don't know, like, if anyone has any preference on the tooling.
Like, using, like, the release, please, or change sets, or something else, we'll learn now.
We can start with something that, like, this is the easiest option, and then we can always…
You can always improve later, if you need to.
**Jared Freeze** 15:10 I don't have a strong preference here, but I would be willing to set it up
I like doing the build pipeline stuff, so I'll take it once we decide.
I'm familiar with Lerna. I think that's what Gorg uses?
To publish?
So…
I don't know how strictly we… I mean, we talked about this in the past, but how strictly we want to stick to it. You know, I know, and you were saying, you know, Browser Repo is kind of our playground for new stuff you might want to backboard, or try out, or whatever, so…
Yeah, if that's the case for anybody else. We had discussed that previously, of like, new tooling's okay in this… in this place, but…
Yeah, I don't… I'm cool with whatever. I saw there was also another tool called Semantic Release?
Which is basically, like, fully automated, so it's like, if you merge a feature or a fix, it goes out, like, just blindly goes out. They call it unemotional, which I thought was a funny way to describe releasing. But,
Yeah, that was… An option as well, so…
I can add it to the list.
**martinkuba** 16:16 That seems little, too.
Too risky, maybe.
At least for this, yeah.
Alright, yeah, so… I guess, some things to think about, like, if you…
If you have opinions, like, please, like, comment on this, on this issue.
Alright, Dan, you have the next topic.
**Daniel Dyla (Dynatrace)** 16:57 Yeah, this is, this comes from the entities SIG.
I'm just looking for the browser,
take on this OTEP. It's been open for a while, it's… obviously, you can see it's got quite a few comments and reviews already.
But this is… Essentially, what we believe will be the solution for…
mutable resources, or, you know, sessions in this case. With the idea being that
When you have a provider of some kind, so say the logger provider, or event provider, or whatever it's called, you can bind it to an entity, in this case a session entity, and that would be an API concept.
And then…
when you call that bind method, you get, as a result, a new provider of the same type, which goes to the same export pipeline, all the same SDK, except it has a different resource with the new entity attached to it.
And then, when you're done with that entity, you shut down the provider. So you'd still use the parent provider for anything that's not directly tied to the session.
But for something, you're… if you have an entity.
In this case, a session that you want specifically tied to telemetry data, you would bind a provider to get a new provider that exports stuff against that entity.
So that's the gist of it. I'm happy to answer any questions if you have them.
But we… yeah, since this is…
I think the browser use case is, like, the… The target,
you know, almost motivation behind this. It's important to get the input of the people here.
**martinkuba** 19:04 Is there any plan to… to create a prototype… prototype in the JS… with the JS SDK?
**Daniel Dyla (Dynatrace)** 19:11 Yeah, I've been working on the prototype, it's not quite ready, I can,
hopefully today, wrap it up and get it pushed up. Yeah. I was working on it before the new year, I honestly haven't worked on it since…
early December, but…
there is a prototype in Java and Go, but obviously JS is important, so I'll try to get that wrapped up this week.
**martinkuba** 19:46 Okay, yeah, I'll take a look at this, I'm not sure that I…
100% followed, like, the difference between the previous proposal.
**Daniel Dyla (Dynatrace)** 19:58 the…
In terms of how it's used, it's not all that different.
The previous proposal… you're talking about the one that, was using the instrumentation scope that tied a resource to an instrumentation scope?
**martinkuba** 20:17 I don't even know, like, there was… there was, like, a few, I think. There was… there was one…
Like, there was, like, an entity provider?
**Daniel Dyla (Dynatrace)** 20:30 Yeah, Ted wrote that OTEP.
**martinkuba** 20:35 Yeah.
**Daniel Dyla (Dynatrace)** 20:38 Yeah, I mean, so you can see that the two code blocks in the top, you know, in the description here, the bottom one was the old version, the top one is what the…
**martinkuba** 20:51 Okay.
**Daniel Dyla (Dynatrace)** 20:51 That was… that was essentially…
Suggesting that we would have a, like, a global resource, and then you would attach and detach entities from it, where this is… it creates an entirely new resource that has all the same entities and attributes, and a new one merged into it.
**martinkuba** 21:12 I see. Okay.
**Daniel Dyla (Dynatrace)** 21:13 So the global resource has not changed, so any other instrumentations would not be reporting against the same resource.
**martinkuba** 21:29 Okay, and so… so, like, you're merging…
You know, merging, like, the resources that don't change with, like, the entity-specific resources into one.
And then… There is, like, a…
I guess, like, it doesn't break, like, the requirement that, resources should not change.
**Daniel Dyla (Dynatrace)** 21:55 No, well, yeah, so it kind of stretches the definition of it a little bit.
Because… it exports…
an entirely new resource. It doesn't modify, like, the global resource. It copies it and uses that one instead in the export pipeline. I mean, if you're just receiving OTLP data.
the end result is you start seeing different resource data, so it depends how you define changed, I guess.
The immutability constraints… Have never really been followed all that closely anyways,
We've seen a lot of people that
Reach in and modify the resource, so…
Yeah, it could be argued either way.
**martinkuba** 22:47 Okay.
But essentially, it means, like, from consumer perspective, like, you might be getting Different set of resource.
Data, yeah. Yeah.
Okay.
Yeah, I was never clear, like, super clear on, like, on the motivation behind that, like.
Ted said in the past a few times that maybe, like, some consumers were, like, hashing all the resource attributes.
**Daniel Dyla (Dynatrace)** 23:15 Yeah, the important one that I know of is that… Google,
like, Google Cloud Tracing is using the resource, for some, like, internal routing things, where when you change certain properties, you can cause problems. But they're actually… they only look at specific properties that they know typically don't change. They don't hash the whole resource.
**martinkuba** 23:40 Okay.
**Daniel Dyla (Dynatrace)** 23:42 You know, and…
I guess, moreover, Josh Sireth wrote this hotep, and he's from Google and has validated that it's not breaking what they're doing.
There may be others, but that's the one that I'm aware of.
**martinkuba** 23:55 Okay.
Okay, it'd be, it'll be good, good to,
Work on that prototype for us.
So I think… I think if we could…
Get that working with sessions before we actually release You know…
Using the session ID attribute, which I don't… I'm not sure if anyone's using right now.
That would be preferable.
So I don't know how far you are from getting that prototype, but I think we'd be happy to help with that.
**Daniel Dyla (Dynatrace)** 24:28 Yeah, the biggest problem, like, the…
it's reasonably far along, but the metrics SDK, like, sharing the export pipeline with two different, providers turned out to be…
a little bit more of a nightmare than I expected.
the metrics SDK is…
**martinkuba** 24:46 Yeah.
**Daniel Dyla (Dynatrace)** 24:48 More complicated than I initially realized.
**martinkuba** 24:51 So we don't use metrics. If you have something working for blogs only, logs and spans, then might be good enough for us.
**Daniel Dyla (Dynatrace)** 24:59 Okay, yeah, that's good to know. I think…
for this group, that's fine, I'll focus the prototype efforts on that.
And… but I think to get this OTEP, like, merged, I think we're gonna need all three, but .
**martinkuba** 25:18 Hi.
**Daniel Dyla (Dynatrace)** 25:18 Yeah.
**martinkuba** 25:19 Okay.
Okay.
Cool, yeah, thanks for the… thanks for the update.
**Jared Freeze** 25:30 Yeah, and then mine's just a reminder that now that the code owners, is updated, we're getting pinged as a group just for reviews, so I've been kind of hopping on everything because
Just trying to stay involved, but, there's plenty of… PRs to look at,
I don't know exactly what the process is, we can talk about this on Slack, but just kind of, like, the triage and stuff, like, if I see something wild come in, I'll comment on it, but…
A lot of the approvals need, like, JAS approval first, like, conceptually, so…
just be aware that there are going to be a lot more DRs coming through because of how the folders have been added, so it's more of just a reminder, like I said.
**martinkuba** 26:13 Okay.
Cool.
Sounds good. A few more minutes,
Does anyone have any other thoughts or things to talk about?
**Jared Freeze** 26:38 I'm not gonna go.
**martinkuba** 26:41 Alright, sounds good. Well, thanks, everyone.
**Jared Freeze** 26:45 Nope, dear. See you later.
