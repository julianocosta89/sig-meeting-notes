SIG: JavaScript SIG
Date: 2026-06-24
Duration: 61 minutes
============================================================

## Zoom Recording Transcript

Jared Lewis 00:00:38 Bye.
Marc Pichler (Dynatrace) 00:00:42 Boom.
Welcome, everybody. Let's… kick it off. As always, if you have a topic that you would like to discuss, feel free to add your topic on the agenda, and then… We can get started. I did spam… agenda with a few topics on my own, already. So, the first one here is… PR that keeps coming up on old PR triage, the person here didn't, get back to us, so I just… Re-looked into, finishing… putting the finishing touches on that one. And one of the comments that I had put on here was to use a factory function instead of exporting exporting the class directly. It does add this now to the new SDK trace package, where we have all the other samplers.
Which are currently exported as classes, so I was just wondering if any of you have a preference Either to keep adding new classes, or to use factory functions for new stuff.
It's mostly a consistency thing.
Trent Mick 00:02:58 I'm just… sorry, checking. I'm pretty sure we use factory functions for the new composite samplers, right?
Marc Pichler (Dynatrace) 00:03:05 Yes. And probably…
Trent Mick 00:03:06 That same discussion and said, yeah, we prefer factory, all things being equal.
Marc Pichler (Dynatrace) 00:03:14 It is in a… so the new samplers, I think they're in a separate package, right? They're not in a separate package. They're in a separate package, yeah.
Trent Mick 00:03:22 Yeah, yeah.
So yeah, right, they didn't have that prior art thing so much.
Marc Pichler (Dynatrace) 00:03:29 Hmm.
Trent Mick 00:03:35 I don't know, I guess if we're gonna do a factory function, I'd wanna… Consider providing factory functions for the other ones, and migrating people that way, if that's our preference.
And we can certainly have crossover where we have both.
For a while.
Marc Pichler (Dynatrace) 00:03:50 Yeah.
I think that makes sense. So we would, for the new one, just have the factory functions, then open the second PR for factory functions for the old samplers.
-Oh.
To move people over, and then we deprecate the classes for it.
Does that sound like a plan?
Trent Mick 00:04:13 I'm cool with that.
Daniel Dyla (Dynatrace) 00:04:15 Seems fair to me.
Marc Pichler (Dynatrace) 00:04:19 Brent.
Denver.
adjust the PR, I will just undo the last commit that I had here.
Or these two, and we'll go back to the factory function.
And then I'll open the second PR to follow up on adding factory functions for the old, samples as well.
And… then hopefully we can get that PR merged.
Trent Mick 00:04:49 And perhaps to reiterate, our preference for factory functions is the usual, kind of, exporting classes.
ends up exporting internal properties and the types? Is that… yeah, I don't know if there are other reasons.
Huh.
Marc Pichler (Dynatrace) 00:05:02 Yeah, that's the main one. I think with… with this always required sampler, it's… not that much of an issue, because I don't expect it to change, like, ever. It is, super simple, it just takes the, not record decision and upgrades it to record. There's not much that can change.
But it's kind of a principle thing. If we… Start doing it now, then we have precedence to follow through with later, so…
Trent Mick 00:05:38 Yep. Okay, cool.
Marc Pichler (Dynatrace) 00:05:40 Alright.
And moving on to the next topic, also mine, this is just a call for reviews.
You probably remember, previously I had opened this draft PR, which… did, like, a prototype for context at HDAC, and also had this, tracing channel example in here.
Where is it now? It's tracing China hair plus thing.
I now moved just the context attached stuff to, separate PR, so that can be reviewed.
And I marked it as ready for review. There's a few things about this PR that are… I made some conscious decisions to make it a bit… Less easy to use, but… Bit more performant.
I opted to… Use the context object as the token.
To avoid allocating another object, that just has this, dispose on it, tool.
make it usable with, using and stuff like that, and there's a few extra problems, yeah.
So, would appreciate, if you would have a look. I don't expect anything, any, any deep discussions today, on this PR, but, I think it would be worthwhile to have this in the API.
I will also follow up with… Implementations for the other context managers.
But these will be more of, like, best effort implementations, because we can't really match that same, behavior that we have in the async local storage context manager due to the… Due to the limitations in the language.
So, yeah.
Trent Mick 00:08:03 And, okay, cool, and we definitely want to get a review from the… I can't remember who I was originally proposing.
Marc Pichler (Dynatrace) 00:08:09 It was, ed was this person here, Where did I put the link? This… About… what's his name, I think?
Trent Mick 00:08:31 Okay.
Yeah.
Abdul Rahman.
Marc Pichler (Dynatrace) 00:08:33 I do…
Trent Mick 00:08:34 Okay.
Marc Pichler (Dynatrace) 00:08:34 Yeah, I did, put, comment here that I opened this PR, and they… reacted to it, so I think they're aware.
this PR is here.
Trent Mick 00:08:46 Okay.
Marc Pichler (Dynatrace) 00:08:50 Oh, most of the decisions that I made here, they are still open for discussion, so I'm not, Like… nothing of… none of these decisions that I made are completely set in stone. You can still change them. It's just what I've opted to do, in the first iteration, and, yeah, we can still… decide, what's best for the API shape there.
Right.
There's no immediate… Things, and we can… Move on to the next topic, which is the last one.
that I put on here.
Last week, we talked about, renaming the SDK log record to read-write log record to be more in line with the specification.
That is actually something that… it's not only the case in the logs SDK, but also in the Trace SDK.
There's, like, a read-write span.
That's defined here.
And we are now currently in a situation where we have not published the new SDK trace package yet, and we could rename it, in the new SDK trace package. Since the type stays the same.
will be compatible with previous versions, and we can export an AVS from the pre-existing packages. So that's SDK Trace Base.
and SDK Trace Node, and web.
But the window's closing, so I was just wondering if you have any… Preferences on that.
It would be good to have those aligned.
Trent Mick 00:11:02 No.
Is it actually called SDK Span right now?
Marc Pichler (Dynatrace) 00:11:08 I think it's called SDK Span, yeah, because it used to be called Span.
And we renamed it to SDK Span, because, when importing it, it was…
Trent Mick 00:11:21 Is it called Spend… Spend Impla?
I think.
Daniel Dyla (Dynatrace) 00:11:28 No, I think it's called SDK.
Marc Pichler (Dynatrace) 00:11:29 That's fantastic.
Daniel Dyla (Dynatrace) 00:11:30 Man.
Marc Pichler (Dynatrace) 00:11:31 I think Span implements Okay, prevent span, what?
I was completely confused there for a second.
When I wrote to Stone.
Trent Mick 00:11:48 I grew up in history.
Daniel Dyla (Dynatrace) 00:11:48 Zude.
If you look at the, Processor.
Sorry, I'm trying to pull it up quickly on my computer.
Marc Pichler (Dynatrace) 00:12:08 Yeah, here we're using the normal span interface, so it seems to be just… Court's abandoned.
Trent Mick 00:12:17 Well, that's the type.
From… oh.
Sorry, from…
Jamie Danielson 00:12:23 Yeah, I can't find…
Trent Mick 00:12:24 SDK.
Jamie Danielson 00:12:25 span.
Trent Mick 00:12:27 There is Span Impla, but I don't know if that's the one we're talking about or anything.
Jamie Danielson 00:12:31 Man, there's, like, readable span.
Marc Pichler (Dynatrace) 00:12:34 then I think what I was talking about was actually the span interface.
Jamie Danielson 00:12:40 There's SDK.
Trent Mick 00:12:42 Okay, so that's a union of… span from the API, and we don'.
Marc Pichler (Dynatrace) 00:12:48 pool space.
Trent Mick 00:12:48 I don't know what a readable spin is.
Marc Pichler (Dynatrace) 00:12:51 Yeah, so that's… that's the read-write span that I was thinking of.
I just had it wrong here, that it's called SDK Span.
Would be that, like, renaming that type here.
to SDK spend.
Trent Mick 00:13:12 And back to the spec, is that what the wording in the spec uses in the trace stuff? I know it does it for logs, the equivalent.
Marc Pichler (Dynatrace) 00:13:19 It has this read-write span.
Bing.
Trent Mick 00:13:29 Oh, I see. Stop that one. Okay.
Marc Pichler (Dynatrace) 00:13:33 Yeah.
But I think it's… Not completely necessary, too.
Rename it.
Yeah.
Daniel Dyla (Dynatrace) 00:13:44 I think it's not complete.
Marc Pichler (Dynatrace) 00:13:45 actually snow.
Daniel Dyla (Dynatrace) 00:13:46 necessary. It might avoid some confusion, since it's called span in the API as well. Like, avoids the rename we have to do in this file.
Trent Mick 00:13:58 Yeah, sure. Like, I mean, if you go to line 77 and, you know.
I agree, it would help with confusion. Because there I naively, without looking around too carefully, would just assume that's implementing.
the API spend. So… Yeah, if we can do it without breaking users, let's do it.
Marc Pichler (Dynatrace) 00:14:19 I can also look into that, since I brought it up, it should be fairly easy, I think, but might be some caveats. We have this nice situation where, like, if we just do a type alias, everything else will still be Compatible, even if the… thing is renamed, so nobody has to immediately switch from Span to the new one.
But we can encourage it by deprecating the old one.
Alright, then I'll, open the PR.
Jordette, that's weird.
Next topic.
Trent removing shim open senses.
Marylia Gutierrez 00:15:15 Okay, so there's.
Trent Mick 00:15:15 No rush.
Marylia Gutierrez 00:15:16 I do have a question about this one. Can we just, because it's experimental, just remove, although we have to mark as deprecated for a little while? Because this one is going straight from, like, having to, like, nope, not anymore. Do we have to mark as deprecated? Because the… I was looking at the guide, it's like.
Yeah, people, like, should, like, for example, the SPAC will still exist for a year, describing what it does, in case people still want to implement.
So yeah, that is my only question for this PR.
Trent Mick 00:15:47 So if you follow… right, so if you follow through that first link… So, yeah, I was gonna give some caveats here, so I don't… I don't know for sure either. I'm just going on reading what the language is. So, recently, that note was added at the top.
basically saying compatibility requirements from the point of view of the spec are now depicated. So, certainly, if we hadn't had a shim, we wouldn't implement it now.
I'm not sure whether this requires us, as people who have already implemented a shim, or a language group has already implemented a shim, to… Keep maintaining one until… The spec drops all mention of Open Census in June 2027?
And there's basically the same, situation for the open tracing shim, which was actually I had this equivalent node added a bit earlier.
Daniel Dyla (Dynatrace) 00:16:39 We're allowed some leeway here, I think, as maintainers. It was never released as a stable package. It gets… 150 to… like, it looks like the lowest week is 6.
like, downloads per week. I am just not at all worried about just removing this from the repo.
it can still obviously be installed from NPM, that doesn't delete it from NPM. So we'll mark it deprecated there, but it doesn't just go away.
I'm not convinced that anybody is actually using this.
Trent Mick 00:17:15 Okay, so part of your… okay, so thank you. One, part of your argument there was that it never made it to stable, so if we were to now also talk about the open tracing shim, it did make it to stable.
But would you still feel the same way? I hadn't looked at the NPM numbers for that either, but I suspect it's also low.
Daniel Dyla (Dynatrace) 00:17:34 It's, I mean, it's $5,000 a week for that one. It's definitely more.
Trent Mick 00:17:40 Okay.
Daniel Dyla (Dynatrace) 00:17:41 It is stable.
I think I would also say, though I'm… I'm not particularly Worried about it.
Is open tracing itself Like, it's been deprecated for a really long time. It's discontinued. Yeah, I'm just not… Overly worried about the.
Trent Mick 00:18:03 As of only March.
Sweet.
So then…
Daniel Dyla (Dynatrace) 00:18:08 It was only March. Interesting.
Trent Mick 00:18:10 Yeah.
Daniel Dyla (Dynatrace) 00:18:11 Yeah, and this one gets, you know, 20 times as many downloads, so maybe it's worth treating it a little bit differently?
But I mean, when was the last time we actually made a change to this shim?
Either of them.
Trent Mick 00:18:31 Yeah.
Marc Pichler (Dynatrace) 00:18:34 One… one thing that we could do is, we could… Mark them as deprecated, still publish them until we Go to 3.0, and then only provide security updates for a while.
But… Only for the previous version, so… There's no published version for, the OpenCensus shim.
in 3.0 and beyond.
Trent Mick 00:19:07 So, yeah, basically I could park this PR and put it on the 3.0 milestone.
Right.
Yeah.
Marc Pichler (Dynatrace) 00:19:15 And then we still, like… Yeah, people could still use it for a bit, if that's what they're actually doing.
And for 3 below, it will just go away, and it will be somewhat clear that, won't come back, and if there's actually somebody who needs it, they will probably open an issue.
I think, maybe.
So, there's…
Trent Mick 00:19:50 I'm going back 4 years, and there hasn't been a meaningful change to SHIM Open Tracing.
So…
Marc Pichler (Dynatrace) 00:19:57 I think the OpenCensus stream is in a similar port theirs, where it was added, and then… We only updated versions.
Because we have to version everything together.
Data and dependencies.
Trent Mick 00:20:17 Yeah.
Okay.
Yeah, I'm fine. We're close to 3.0, so I'm fine just… I suppose we can mark them… the packages deprecated now? I'm not even sure what the process is. Like, still releasing 2.xes, but they're… do you… do we bother marking them deprecated or not?
Jamie Danielson 00:20:39 If we still have another release, probably.
Is that the opposite?
Daniel Dyla (Dynatrace) 00:20:45 Is he markable?
Jamie Danielson 00:20:46 What does that.
Daniel Dyla (Dynatrace) 00:20:46 A package as deprecated?
In NPM.
I think if you release another version, that version does not get the deprecated tag. You'd then… we'd have to go, like, re-deprecate it every time.
Jamie Danielson 00:21:02 Oh.
Trent Mick 00:21:03 Okay, okay. So, I mean, maybe at most we get out a README note at the top of the README saying this 2.x is the end of the line for these things, and wanting to the… These notes in the spec, if that.
Okay, cool. I'll… I'll park this PR and put it on the 3.0 milestone.
Marc Pichler (Dynatrace) 00:21:25 I guess one question's still open.
or that's still open about. This is what we do with the OpenCensus.
Declarative config stuff.
because, if I recall correctly, the way that it was implemented is… Dynamically loading it, if it's there.
That's known to cause trouble for people that are using bundles and stuff.
So… Okay.
Trent Mick 00:21:57 I would like to now, and not even wait for it, just drop support for that, so remove that, because the… our declarative config stuff is all still experimental. And the current state in the declarative config spec is that Supporting this is… I'll get the language wrong, but it's optional, it's not required anymore, because OpenCensus compatibility has deprecated itself.
Marylia Gutierrez 00:22:22 Yeah, I would definitely say, like, that is the time to just, like, remove completely, like, nobody's still using this, that is the chance to… Kind of, like, break away, so, yeah.
Trent Mick 00:22:33 Yeah, okay, so, yeah, I can, or any one of us can go drop that from the current… configuration package.
Or SDK node, I think, actually.
That's where I'd be from.
Cool.
Marc Pichler (Dynatrace) 00:23:00 Random.
Topics you would like to discuss?
If not, then we can move on to… fact triage?
As always, if you have anything… That you would like to discuss, feel free to… Interrupt, and then we can, make use of the time here, and talk about your topic.
We got no new bugs in the corrible.
Let's check here if there's anything that looks like a bug that wasn't reported through… Template… Looks… Fine.
In contrip, there also doesn't seem to be anything new, And also looking for stuff that looks like a bug that wasn't reporting… reported through the template, Also looks like nothing there, so that's also fine.
And then we can look at old PRs.
Let's pick the one which has more PRs open.
That's the quarry Bull.
It seems like it's kind of not moving, it's been at 52, and I keep merging PRs, but more PRs are opened.
Trent Mick 00:25:09 It's a Hydra.
Marc Pichler (Dynatrace) 00:25:10 Yeah.
So, the first one here, not actionable yet, I guess we can take some time to look into the… logs, API, SDK, milestone, because that's… what we need to finish to actually move it there.
Thanks, Trent, for, opening the issues here of the stuff that we discussed last week.
Trent Mick 00:25:50 That's my guilt complex, because I haven't done the… The widening the attributes type thing.
Dan, Dan, you threw out that idea a few weeks ago of just, oh, just use unknown, but that runs into other problems, so that slowed me down a little bit. I have to get back on that.
Murse.
I can't remember what the issue was.
Daniel Dyla (Dynatrace) 00:26:13 Sorry, I was not intentionally trying to hold anything up.
Trent Mick 00:26:16 I, I'm sure, yeah.
Brilliantly done, if you were, though.
Marc Pichler (Dynatrace) 00:26:27 Oh, that's, wait, is that linked to this?
Pink?
Trent Mick 00:26:34 Actually, is it not on there, the PR… well, okay, because it was going to be a new PR. So I have… I had the PR sitting there that was… Widening the attributes type.
That'll be in draft. I guess I didn't add the PRs to this. I don't know which issue was the appropriate one there.
And then I have local work, I'm not even sure I made a PR yet for… Widening the attributes type, just setting any value to be unknown.
But, yeah, that's nothing to review yet.
Marc Pichler (Dynatrace) 00:27:12 Alright, Yeah, if, once it becomes ready, to review, I'd be happy to also have a look, so feel free to just reach out once, once it's there.
Trent Mick 00:27:29 Other side, general question, maybe people here would have an opinion. The… so there are a number of PRs that… Anna Rag, a colleague at Elastic, has been working on for the SDK metrics, the self-observability stuff.
And I've been helping review some of those, so some of them are in and some of them aren't yet.
Way back for the non-declarative config code path, so the current one using Node SDK, there's an environment variable that we use that would tell node underscore something.
for opting into SDK Metrics.
So I want to have a good sense of what the reasonable process would be for opting into those well… Because they're still experimental, so the idea is to opt into them.
How we would do that through declarative config.
I'm not sure where a good area to do that is, and whether we want to have a node-specific Part of the declarative config schema that's for opting into that, or… Or that there's something in play in the configurations discussion, so go ready.
Jamie Danielson 00:28:42 Actually, that's a good question, like, if another language has already added something.
Trent Mick 00:28:49 Because I think Jack… for Java, they'd had the internal SDK-like metrics, not according to the spec that predated… predated the spec based on micrometer or something, so just some Java-specific… technology there. So, I'd seen discussion from Jack Berg about having some declarative config option for selecting by name which type of internal metrics you wanted, which wasn't quite the Boolean that we would use, so I wasn't… but I wasn't sure if that had progressed at all.
I don't know if anyone has more data.
Okay.
Because as it stands, we'll probably get to the point where, you know.
The declarative config path and start… Node SDK rather than braiding the Node SDK class, so that the declarative config Path becomes the preferred way of starting.
on the SDK for Node.
But we won't have an option for someone to be able to opt into these SDK metrics. We're still a ways away, so this is not… A burning need, but… Okay.
Fun?
Marc Pichler (Dynatrace) 00:29:59 Discussed different, different options where to put it, a few SIG meetings ago.
on the car here, but I don't… I don't think we… Came to a conclusion.
Trent Mick 00:30:19 Okay.
I guess…
Marc Pichler (Dynatrace) 00:30:21 reaction.
Trent Mick 00:30:21 it to the configuration.
That repo.
Master.
Marc Pichler (Dynatrace) 00:30:28 I remember my, my idea was to just define it as if it was an instrumentation.
Trent Mick 00:30:40 Right.
Marc Pichler (Dynatrace) 00:30:41 But I'm not sure how the instrumentation config stuff currently looks like, I haven't… Played around with it.
Trent Mick 00:30:51 In declarative config, there isn't really.
there's… oh.
Yeah, it's…
Marc Pichler (Dynatrace) 00:30:56 That's obvious.
Trent Mick 00:30:57 Yeah, wide open.
Jamie Danielson 00:30:57 There's plans for it.
Yeah.
Trent Mick 00:31:00 are there plans for… because, I mean, inherently, it's language-specific, so I don't know what the…
Jamie Danielson 00:31:06 Yeah, but you'd have, like, language-specific sections, too. At least last I checked, it's been a little while since I've looked at it, too, but that way you might have, like, Java, and then, like, instrumentation.
something or other, and then… I think… so it's, like, infinitely extendable, I think.
If you add in the options.
Trent Mick 00:31:28 Okay.
it is… The top-level, wide-open thing is instrumentation. Isn't it? Slash development, whatever.
I'm trying to… Find the examples again. Yeah, okay, so it's a bit… if it's not an instrumentation-type thing, then as far as I know, in declarative config schema right now, there isn't a language-specific area for… Things that aren't really about instrumentation.
Or at least it feels like, I don't know if naively you would just put stuff in there anyway.
Right.
Okay.
Thanks.
Marc Pichler (Dynatrace) 00:32:18 Anyway, while we're talking about declarative config, I'm, also gonna say something. I had this draft PR here, About this plugin component provider spec.
If anybody's interested in taking that over, or building on top of that, or building something in parallel, please feel free to do so. I'm not sure if I will have time to Continue working on this.
Because I want to focus on the context-attached, detached stuff first.
So if that's something that, you're interested in, please feel free to just… Pick that.
Take that work, and adjust it as needed.
Trent Mick 00:33:05 Okay, thanks.
Yeah, the… I think the declarative config stuff… everything except the plugin component or provider stuff is moving along well, I think, and… at least for me, my focus will be on firming up the other stuff, and your PR was pretty useful to keep like, that in mind for what kind of API we want to have laid down to make it easy to add that later. But for now, I think… I think my expectation of where it'll go is if someone tries to use this custom thing, we, one, won't have a way to register a plugin component provider for a certain name, and we'll just error out, basically, saying, you know, you're trying to use a… a type of span processor that we don't know anything about. And I'll just error out on config for now, and then we can worry about that part later.
Like, I don't know of any, like… It's in the spec, and I understand how that's useful, but I don't know of any burning use cases right now where people have these kind of custom components.
That might help motivate.
Marc Pichler (Dynatrace) 00:34:11 I think one thing that I saw recently on… of PR.
was… I think Mike Gord Smith opened… this here.
The spec conformance matrix, and… Like, for example, for the resource detector… There's this… I probably didn't publish that.
Just do that so that it's… That it doesn't get lost.
So, there's this no-container detector in JS today, which actually The container detector is here, but it's in the contrib repo.
And I think that's, like, one of the first signs of… That might be useful later, to have something to load stuff from a different repo.
Oh,
Trent Mick 00:35:15 Yeah. Yeah, I see what you mean. Yeah.
Marc Pichler (Dynatrace) 00:35:18 So, there's nothing pressing right now, but I think as the rest of the features progress, these will be the ones that are left over.
And then it… Might be, interesting to start looking into that.
I think there was also.
Trent Mick 00:35:39 So it might… it might be that we need this… plugin comp… Component provider story answered before.
This code path is a viable alternative to the… Node SDK one.
Before, for example, auto-instrumentation, this node can switch over to using this. Okay.
Marc Pichler (Dynatrace) 00:35:58 Yeah, exactly, all the instrumentation's not, like, getting feature parity with that will be… I think for that, it will be required.
But for everything that we have now in Node SDK.
Probably moving over is… is fine. And also loading instrumentations.
Could be done via a second, like… require flag.
When you're starting up, you could, like, require and then use the thing that does declarative config, and then require something that loads your instrumentations.
So you can stack these together.
Trent Mick 00:36:40 Okay.
Marc Pichler (Dynatrace) 00:36:43 It's a bit hacky, but it works.
Trent Mick 00:36:46 dash dash import, though, you gotta be careful. If you want to use import, then you do… you probably have to use import if you're using top-level weight in the… but then I'm not sure, import in the middle has changed a little bit there.
And I think Node processes the dash dash requires before the dash dash imports, so if you're using import for one, you gotta use it for there.
No end of bug reports.
Marc Pichler (Dynatrace) 00:37:14 Right. How I distracted us from PR triage.
Successfully… I think it was a team effort, so…
Trent Mick 00:37:23 It was, it was.
Marylia Gutierrez 00:37:25 Part of the plan, like, yeah.
One thing… oh, one thing that I can bring by start helping with the PR situation, so, because in another SIG that I'm in, we do have, like, a lot of PRs who are trying to find ways to basically check the status and stuff like that, and we really like what was done on both, like, the Java and the Gen AI repos. Don't know if you ever saw this, but they have, like, an issue that is basically keep getting updated, showing the PRs that, like, oh, are waiting for us to review, and then they have the session, like, no, actually just waiting on the author, or just, like, waiting, so it's a little more easy to see what we actually… we should be paying attention. So I will… I was going to add to that other SIG, and also try it out on the JavaScript, but that… basically, it created, like, a whole thing, because it is, like, an action, but Renao is using a token from, like, one of the AIs, or whatever, I think it was Copilot, or whatever, but it was using, like, a personal one from somebody, so I cannot just use that to everybody.
So we are trying to get one per hotel in general, and at the same time, we do have a lot of workflows that make sense to have to a lot of people, so we are gonna have a new, repo that is just about shared workflows, and we're gonna basically create this as apps.
So this is a way that… so that is one of the ones that we are putting there, so we're just gonna put, like, it's called, like, just PR dashboards, and we can opt in, like, repos that want that. So that is something that will be coming in the following weeks. I can keep you guys up to date, and whenever we have that available, I can also opt in the JavaScript, and hopefully it would help with the… things like that. And if you also have any ideas of workflows, so I'm gonna be one of the maintainers on that repo, so you can also let me know.
Marc Pichler (Dynatrace) 00:39:26 So, that's… I think that's gonna be very helpful, to have some sort of, like, overview issue and going through these.
It's also very easy to lose track here, usually, on, like, where we stopped and stuff. So, I think that's gonna be really helpful.
Marylia Gutierrez 00:39:47 I can share here one example of the Java one.
Just how the issue itself looks.
And the other thing that we're also adding up, I don't think it's gonna affect… a lot of this repo, we don't have that much of a problem, but in a lot of other repos, we're having an issue of people just coming, like, using AI and opening, like, 10, 20 PRs, and expecting, like, review quick, so we're actually gonna limit the amount of PRs by… People that don't have right access, pretty much, so everyone that is not maintaining or approver, can… so the discussion is right now, it should be limited to, like, 3 or 5, or something like that, if you have an opinion.
I can also share the link, but I think we are… we're gonna start with 5, and then the repo itself can change the value if they need.
We don't have that much of a case here, I don't think I noticed. We do have a few, like, AI… submission that I'm adding comments, like, please make sure that you're actually reviewing stuff, because we have some AIs coming up with just the reply of the person that are not a real person, so that is something we also want to discourage.
Trent Mick 00:41:12 Yeah.
So… I… because we don't have the problem, I… I would hesitate having a limit on the number. Like, the best example I can think of is… is Anorag, who had been doing those, the SK metrics.
PRs, and I think at one time he had 5, maybe 6 PRs that were open, and they're, like, legitimate PRs from him. I wouldn't want some arbitrary barrier there to catch someone, if we don't need it. Like, if we get to a point where we do have this problem with a single Brando opening a whole bunch of PR cents, sure, let's put gates on that.
Daniel Dyla (Dynatrace) 00:41:47 I think…
Trent Mick 00:41:48 Anyway, agreed that we've had some one-offs from… from kind of just AI-generated ones, but… That's… that's a separate issue.
Go ahead, Dan.
Daniel Dyla (Dynatrace) 00:41:57 I think the GitHub feature is, like, limits on non-member PRs. Like, if you don't have right access to the repo.
Oh, I guess Anirot doesn't.
Trent Mick 00:42:09 Thanks for the reply.
Daniel Dyla (Dynatrace) 00:42:09 Yeah.
Trent Mick 00:42:10 That was the one… only example I had, yeah, either way. Okay.
But I mean, at least a member, that would be my opinion.
Yeah, yeah.
At least it hasn't been a problem for us. On the other issue of getting some AI-generated things, I've personally stopped using good first issue.
Has a label on things.
No.
Marc Pichler (Dynatrace) 00:42:33 I've used good first issue to get free tokens.
Trent Mick 00:42:38 That's what I've seen them in my neck, yeah.
Marc Pichler (Dynatrace) 00:42:40 Only chumps pay for.
Trent Mick 00:42:41 tokens, you just open rando PRs with good first issue and wait for people to reply.
Yeah.
Marc Pichler (Dynatrace) 00:42:52 Yeah, it's, also one of the… I think it's difficult with the good first issue thing, because in the past, it was a good way to Onboard new people, but, it's… A bit more difficult now, because it gets immediately picked up by, people using agents, so… I'm not sure upstairs.
Marylia Gutierrez 00:43:22 Yeah, the problem is, like, some of them that they don't use, so some of the repos, we created, like, agent files to tell the agent, like, okay, if the human is not reading, maybe the agent would actually read, so we have things, like, you have to send the PRR that was generated by stuff, but they are not actually reading the whole thing, so they are not copying the whole repo, so we still don't get that file being read. So I was like, oh, not even the agents are reading our stuff, but yeah.
Marc Pichler (Dynatrace) 00:43:55 Oh, I'm… I'm actually… Like, we still have the requirement for the disclosing, usage of LLMs and PRs, right?
That still exists.
Trent Mick 00:44:09 I don't think that's a requirement, is it?
Marc Pichler (Dynatrace) 00:44:13 That was the community repo, probably, right? .
Trent Mick 00:44:17 Yeah, I think the… I might be mixing up two things, but I do recall the… the AI usage discussion at the Node Summit. The Node Collaborator Summit.
there was… James… Jaznell is his… I can't remember.
I know is GitHub… I know people's GitHub handles, I don't know their actual names. Jasnal had mentioned that you can't necessarily require, because some people are using it to… using AI to assist with, like, personal disabilities or something like that, so it's kind of… doesn't always cross the line. I think our contribution policy was more about like, the human needs to be in control here, you can't just be blitting whatever rando stuff without reviewing from.
Marylia Gutierrez 00:45:04 Yeah, basically, that is what, like, our policy said, like, the… like, if you're creating something, yeah, you can use, but you have to review, and when we are replying to, like, the issue itself, a human has to be replying, not just, like, copying and… whatever the LLM said, and… because the amount of, like, you can… there are, like, some tales of just, like, the person doing the merge with main over and over, and just adding a comment, see, these are the updates, like, yeah, I don't care about merge with main, but yeah.
Trent Mick 00:45:33 Yeah.
Or some random updates, but they didn't actually answer any of the questions that were asked.
Marc Pichler (Dynatrace) 00:45:44 Push some updates, and what the comment says is different to what the actual updates were.
Trent Mick 00:45:53 Yeah.
Marc Pichler (Dynatrace) 00:46:03 Alright.
Dr. Ashton. This one we already talked about.
PR… I didn't assign myself… But… I still need to work on… my other PR, which… Probably linked here somewhere.
I might try to get to these, soon. I've just been… I wanted to get to this one first, and then work my way through.
Fair.
This one, I think we have said we're gonna merge with 3.0, so… You can leave that open.
There's… SPR here for the gRPC general options, Ike, trump has reviewed that, so… We can also still leave that open.
Good.
Already looked at… this was the PR that I need to finish, actually, like, the canceling retries and shutdown.
Which is what blocks the OTRP exporter base one.
Entity resource prototype.
Trent Mick 00:48:04 Yeah, I'm curious what the status on entity stuff. I'm pretty ignorant on entities. I think I read the spec a while ago, but it's changed. That was back when it was going to allow re… effectively, resource to be mutable, but that's not… parent state of things anymore, is it? Dan, do you know… Kind of what the current hopes and dreams are for entities.
Daniel Dyla (Dynatrace) 00:48:23 Well, it is going to allow resource to be mutable. Parts of the entity are still defined as immutable, but it… parts of the… the entity are mutable.
we call those identity and description, and they're just bags of attributes. So the identity is not like an ID or anything like that, it's a set of attributes that identify the entity.
And then the entities are attached to… resource as… references, but the attributes themselves are actually on the resource. So if a descriptive entity ID, or a descriptive entity attribute changes.
It also changes on the resource.
or, more likely, An entity is… Added or removed from the resource.
Trent Mick 00:49:25 And… Do you know if the current… spec.
for entities is something that the browser guys would be using for session ID and other stuff, because if I understand correctly, that was one of the main motivations.
Daniel Dyla (Dynatrace) 00:49:39 It was original.
Trent Mick 00:49:40 It was for mutable resources, but yeah.
Daniel Dyla (Dynatrace) 00:49:43 It was originally, they were not happy with it. They are going their own way with… session manager is what they're calling it, and I don't know exactly where they're storing the session ID. I believe it's on the resource Just as a mutable resource.
attribute.
Trent Mick 00:50:04 I thought it might have been a SPAN processor and log record processor that was just gonna add.
attributes.
Daniel Dyla (Dynatrace) 00:50:10 Yeah, that was the original… I think the prototype used that because resource is currently immutable.
Trent Mick 00:50:17 Because that was a thing at the time, sure, okay, so it could be.
Daniel Dyla (Dynatrace) 00:50:21 I think the long-term plan… like, the plan right now is to make resource mutable.
I'm not as familiar with the browser side of things, but I know that they were not happy with the… entity, like, concept.
Trent Mick 00:50:43 Okay.
Marc Pichler (Dynatrace) 00:50:47 But they're currently in pro… in… In the process of moving… whatever is in Webcommon to the… browser repo?
And they've had these… span processes.
Where you can, like, give a session provider, and it attaches that to the span, or to the log record.
So that's the latest, info that I have on how it works right now.
But yeah, no idea, how the entity, or… What they… what they will do with the entity stuff.
So, will the… Since there have been some changes, since this prototype was opened, will there be another prototype, soonish?
Daniel Dyla (Dynatrace) 00:51:52 maybe just because there's so many, like, changes since this, I haven't been keeping it up to date, and there's, like, conflicts and stuff like that, I might reopen it, but most of the spec changes… were motivated by these prototypes. I think the prototype Still is at least relatively close to, the… the specification.
Marc Pichler (Dynatrace) 00:52:24 Alright.
Then we'll keep that around, and yeah, looking forward to… that progress.
one thing… Just out of curiosity, was the… I don't know what the latest state is on entities. Is there going to be a separate exporter for entities? Or is…
Daniel Dyla (Dynatrace) 00:52:52 Eventually… so, no, there will not be a separate exporter for entities. I believe that the entity events are gonna go out as log records.
Marc Pichler (Dynatrace) 00:53:04 Okay.
Daniel Dyla (Dynatrace) 00:53:05 But eventually, it will be… events will be omitted. Right now, all we're defining is… The entities attached to the resource.
Marc Pichler (Dynatrace) 00:53:22 Alright, that's good to know. I was just wondering, because the, Would be interesting to see adding, like, a new signal to the exporters now that we do the, custom serialization. I'd be interested to see if it would be easy to add stuff or not.
Yep.
Daniel Dyla (Dynatrace) 00:53:46 Yeah, I don't think this will require that. There was some talk about potentially having it be its own signal.
But… I think… That's not the way that we're gonna go.
Marc Pichler (Dynatrace) 00:54:08 Hmm.
Moving on to the next one. We have… No changes requested by… Jared, I think I also… Mentioned that we… Would want to wait for this.
Until Fetch is actually available in all the supported runtimes that we have right now.
Did Surface assign this to me, so I'm hoping to also get to this then soon.
I think they made some changes to it since… The idea here is to have, like, a custom fetch that people can Give to the exporter, so if they have to do anything… With it before, or they have some special requirements, they can just replace whatever fetch instance is being used.
I haven't looked at that, So I'm done with the rest of these here.
this one here has the Up for Grabs label on it. I suppose this is because somebody has to actually try and see if the example still works, because I assume this is… Just updating the example here.
I guess it's somewhat unlikely that, anyone will pick that up, with that.
sit around for a few months, so I'll just close this for now.
there's also… Maybe a somewhat related question, if we want to… Keep the examples here around in the way that they are now, or if we want to move them.
as well.
This is essentially, that's a very simple Prometheless metrics.
example, and I'm wondering if we could just consolidate these, into… like, one… Example that, Just shows a general setup.
We probably don't have to figure that out now.
Daniel Dyla (Dynatrace) 00:57:01 The examples in general, are they, like… used by any… do we know if people look at them? Are they actually useful and up-to-date? And… or are they pointing people towards outdated…
Jamie Danielson 00:57:14 Some of them are outdated.
They were.
Trent Mick 00:57:18 ly out of date.
Daniel Dyla (Dynatrace) 00:57:19 Yeah.
Jamie Danielson 00:57:20 Some of them weren't, but… I was gonna.
Daniel Dyla (Dynatrace) 00:57:22 Should we just remove them?
Trent Mick 00:57:25 That is…
Daniel Dyla (Dynatrace) 00:57:25 Are we better served by improved documentation?
Jamie Danielson 00:57:30 both, I would say. But, yeah, there's, like, an issue out there that, like, I had started at some point, and Mark had started at some point, and then kind of fell off of cleaning up, like, getting rid of… a lot of those are too complex, right, with having, like, Jaeger and, like, having multiple ways of running things. That's… Like, we were gonna have, like, one kitchen sink example.
And then maybe, like, one or two other ones, but… Just haven't done it.
it might be worth it to take them all out and just add a couple of new ones instead of trying to clean up what's there, I wonder.
Trent Mick 00:58:05 Or pick a subset, like, we should have one that shows HTTP.
Jamie Danielson 00:58:08 Yeah.
Trent Mick 00:58:09 But… But otherwise.
Daniel Dyla (Dynatrace) 00:58:10 Yeah, or just, like, the basic setup, like, we… we can have one that shows setting up the SDK with You know, the expected high-value exporter, you know, instrumentations, and call it a day.
Jamie Danielson 00:58:23 Yeah.
Daniel Dyla (Dynatrace) 00:58:23 P.
I think…
Trent Mick 00:58:26 Okay, maybe so.
Daniel Dyla (Dynatrace) 00:58:28 Doesn't…
Marc Pichler (Dynatrace) 00:58:29 That's also…
Daniel Dyla (Dynatrace) 00:58:30 and… Go ahead.
Marc Pichler (Dynatrace) 00:58:33 I think I was about to say the same thing, there is this example spec that was recently published, and somebody was working on that. I think that was what you were trying to say earlier, right?
Daniel Dyla (Dynatrace) 00:58:46 No, actually, I was gonna say, there's… there's been somebody in Slack that's… was asking… Questions about, various, like, exporter configs that weren't documented.
And we went back and forth a few times, but the general… problem that The options for each package are not really documented in each package's README.
I think… this may be, like, the bread and butter use case for some AI PRs to go through and update the READMEs with you know, a basic getting started example and configuration options on every README, because… they're not really documented anywhere, you kind of have to dig through the code to figure out what any of the packages can do. And in order to do that, you have to know What you're looking for in the first place.
I think this may be a case where… somebody with… a couple of afternoons and access to a couple hundred dollars in Cloud tokens could crank through this and really improve the experience for a lot of people.
Marc Pichler (Dynatrace) 00:59:59 Yeah.
I agree.
Trent Mick 01:00:00 Maybe? I mean, certainly not opposed to getting the READMEs improved on some of the documentation. The… I don't know how much signal there was on… so that was James.
That had asked about the export… like, the exporter options are some of the hardest ones to suss out, because they're jumping through a whole bunch of different packages, and they still have to create legacy options, and they're super meta. So those ones are… could certainly be improved by having some docs there. The ongoing pain, then, is maintaining docs of options in the README while… when we make changes, I guess it just becomes another burden for review. But yeah.
I like the idea of stripping down what we have in examples, because I think some of those are counterproductive right now if they get out of date.
Marc Pichler (Dynatrace) 01:00:50 Yeah, maybe we can start by removing… like, the ones that are really out of date, that are for sure not going to be helpful. And then… we can start looking at the ones that are more up-to-date. But there's a few ones that use 0.something of the trace SDK, which, It's fairly old.
I think we have to, End the discussion here anyway, because we're out of time for today.
thank you, everybody, for joining and for the discussions. Have a nice week, and see you next week.
Trent Mick 01:01:33 Thanks.
Marylia Gutierrez 01:01:33 Pia.
Trent Mick 01:01:34 Still.
Marc Pichler (Dynatrace) 01:01:35 Thank you.
