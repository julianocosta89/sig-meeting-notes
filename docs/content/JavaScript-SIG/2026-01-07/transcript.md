SIG: JavaScript SIG
Date: 2026-01-07
Duration: 60 minutes
Zoom Recording URL: https://zoom.us/rec/share/iEgGXatsM47N3LaEF1msPWEZ3w2TngrKFT7_MTe_R3Of9X5kgX3nIBMOXiLwhw8b.QG0_9SnnwKBQ1bTG
============================================================

## Zoom Recording Transcript

Marc Pichler (Dynatrace) 00:01:57 Hello?
Marylia Gutierrez 00:02:00 Ew.
Marc Pichler (Dynatrace) 00:02:01 Happy New Year.
Alright, let's get started here.
Or share my screen.
Too many windows.
Alright.
Welcome, everybody.
Let's get started with Marilla's topic.
Marylia Gutierrez 00:02:45 Yeah, sure. So, I just put it here in case people don't know. There is an Hotel Unplug happening February 2nd in Brussels, right after Fosden.
The idea is to be an unconference, so if you want to bring topics, to kind of, like, shape the roadmap of hotel, or if you have topics, basically a day that people can talk about it. So I just want to bring it up in case people didn't know about it.
Marc Pichler (Dynatrace) 00:03:16 Thank you.
alright, any questions?
comments about water unplugged.
If not, then I guess we can move on to the next topic, I just wanted to say thanks to everybody who worked on the HTTP and database SEMCOM stabilization efforts, so that was mostly Trent and Jamie working on it. So, special thanks to those two.
There.
I guess the next steps for this is, enabling the stable semconf, by default.
Let's, plan for around June. Thank you, Trent. I think you opened the issue there.
2.
Make sure we follow up on that.
And, yeah, I guess.
new focus topics we will, define in the coming weeks, to make sure that we don't Run out of work there.
And… yeah.
Trent Mick 00:04:29 Made sure we don't run down to work. Thanks.
Marc Pichler (Dynatrace) 00:04:36 Alright.
Any questions about, HTTP or, database CENCOM stabilization?
If not, then, - I guess let's move on to the next topic. I put this here.
Before, the holidays, last year, we didn't do a release, so I was looking into, cutting a release, this week, and I found that there were quite a few changes in the API package right now.
So, one of the things I was considering is doing a feature release for the API package, since there's one change in particular that, Also… oh, that's actually not the correct ER I think I linked here.
No, it is actually the right one. So this PR changes the public API slightly. The component logger type is changed from Any to accept unknown shouldn't affect anybody, really.
So, what I'm wondering of… what I'm wondering is if you think it would be acceptable to release this as a bug fix release instead. So instead of doing 1.10.0, we would do 1.9.1.
And the benefit of that is that, people who are still using SDK1.x, won't get any com- won't get any, install errors, if they install the latest, OpenTelemetry API version.
The SDK packages, right now.
have a upper limit of which API is acceptable.
So, obviously the older ones, they… Use 1.9, or 1.8, or something like that.
And if we bump that to 1 to 10, then, on in-star, people might get errors if they try to use the latest API.
Then.
Daniel Dyla (Dynatrace) 00:07:06 Yeah, so In my opinion, I… I would… Say, instead of releasing it as a bug fix, it's not a bug fix.
like… You know, if you look at the change, it's not fixing, like.
It's not fixing a bug. It is a compatible change.
I think… Like, keeping the… The honesty of the release is important.
I would rather release I… you know, I… A backport fix.
to the 1.X SDK.
Like, release set, A patch version of that.
That just increases the API that it can install with and move on.
Marc Pichler (Dynatrace) 00:08:09 Yeah, that's.
Trent Mick 00:08:10 I'm assuming the pause there is because that's a pain in the ass for us right now, right?
Marc Pichler (Dynatrace) 00:08:13 Yeah.
Daniel Dyla (Dynatrace) 00:08:14 Yeah, it's a pain in the ass, I know. So I realize that, it's certainly a harder way to do it.
And it's fine if you go the other way, I just… You know, if… if we had… perfect tooling that would allow us to do anything, I think that that would be… my preferred solution. If you say, I don't want to do that because the tooling doesn't support it, that's also fine.
Marc Pichler (Dynatrace) 00:08:42 It's also a thing of, if you just do a one-off release, that's probably also fine.
To do it manually.
Daniel Dyla (Dynatrace) 00:08:54 Yeah, I was wondering… What are the… Like, requirements and promises of the… the 1.X line… Like, did we say it will continue to work for a year, or… And does that include with new API versions?
Marc Pichler (Dynatrace) 00:09:20 I think… so, the… I'm not sure if we gave any guarantees in that sense.
Trent Mick 00:09:31 Oh, I don't know…
Daniel Dyla (Dynatrace) 00:09:32 necessarily did, but the spec might in the stability dock.
Trent Mick 00:09:36 So, at the top of the upgrade to 2.x, we said, per open telemetry guidelines, the 1.X versions of stable SDK packages will be supported for 1 year from the 2.0 release.
And we did the release in late February, so we're still inside the year.
Marc Pichler (Dynatrace) 00:10:04 I guess one of the options could always would be to just wait.
We can cut… we can cut an SDK and experimental package release, without having to release the API, since it is just internal changes, mostly.
We've done that.
For the past few… months where these changes have been slowly trickling in. So, that is one of the options that we can take there.
I don't think it's necessarily super urgent to release the API package, so… That's a slow option.
Daniel Dyla (Dynatrace) 00:10:45 have any… Actual new features, or is it just the type changes?
Marc Pichler (Dynatrace) 00:10:51 It's… it's just this type change here that stuck out to me.
Because type changes can be finicky. I don't think… This change in particular would cause any trouble?
There is… let me see here…
Daniel Dyla (Dynatrace) 00:11:09 Right, it's just the way that the package JSON declared the maximum, right?
Marc Pichler (Dynatrace) 00:11:16 Yeah, exactly. So, we have here, improved performance.
There's a change in the ESNext, export condition thing, where, I think if you used ESM, and you wanted to have ESNext, you would always get ESM, and that's kind of fixed now.
And the rest is… Yeah, internal changes. Like, internally removing the export star, or, I think that's also in the top-level package, in the top-level index.
That changed the export star there. And then a few, tsconfig changes that shouldn't affect the compiled output.
And then again, refactors. So… I think the people that are waiting for it are mostly looking for the performance improvements there.
And the rest is, yeah.
Internal changes that shouldn't affect too much.
Daniel Dyla (Dynatrace) 00:12:30 You know, up to you.
Given that we only have a month and a half before… Our promised end of support.
You know, waiting seems reasonable. A month and a half is, like, kind of on the edge of… Kind of a long time, but given that there's no… like… actual, you know, if we're delaying, like, I don't know.
the profiling API by a month and a half for this, I think it'd be different, but… It's something… Fairly minor.
Marc Pichler (Dynatrace) 00:13:12 Yeah, so… I guess one of the options could also be to… Leave it now, and then… see if we get any features that actually add API to, API package, like the integrating the logs API, for example, is one of these cases where We definitely need a new, feature release.
And we could do it then.
Does that sound okay to everybody?
delaying it, to February, I'd say.
And then we can re-discuss, ways forward for releasing the API.
I never, update this PR to, exclude the API funnel, and, Yeah, we'll go ahead with the… Released tomorrow, then.
If any questions come up, or you have any other ideas, please feel free to just reach out to me, and then we can discuss.
Alright.
Any questions?
If not, then, hand it over to Jackson.
Oh, I think you're muted.
Nope, still can't hear you.
Still continuing, unfortunately.
Alright, sounds good. See you then.
yeah, I guess this is mostly a call for reviews here. It's updating OpenTelemetry resources, Changing the N for parsing logic… aligning with, other SDK's behavior.
I guess, I guess, definitely put that on my list of PRs to review.
Jackson-iPhone15 00:16:26 Hey, Mark, sorry, I just joined from my phone. Can you guys hear me all right now?
Marc Pichler (Dynatrace) 00:16:30 Yes, we can hear you.
Jackson-iPhone15 00:16:32 Perfect, thank you. Yeah, so this PR in particular is really just to get us in line with the other OpenTelemetry SDKs. The problematic behavior in the JS SDK at the moment, is that Not only do we, so, for example, if you passed a set of attributes in the hotel resource, attributes, NVAR. If you hit an invalid attribute in there, attribute value specifically, something that might contain, like, an unencoded space, basically anything that's not a baggage octet, valid value.
Not only does it drop that specific attribute, it drops every attribute after.
So I, modified this to bring us in line with what the other SDKs have been doing, which is basically just to percent encode those values, in the cases where it makes sense.
Marc Pichler (Dynatrace) 00:17:30 Yeah, thanks for working on that, that sounds, Sounds great. I wasn't aware of this issue, but guess it must have, under the radar there.
jeremyvoss 00:17:44 And for a bit of… for a bit of spec context on this, basically the spec does say that all the values in that environment variable should be encoded, but it does not say what SDKs should do when those values aren't encoded, and so all the other languages, looks like they have just said… well, I mean, we still know that a space is a space, so we'll encode it.
So there was a bit of… The spec left room for interpretation, and Node appears to be the one that, had the, you know, interpreted it, or rather.
Was sort of the strictest.
Yeah.
Marc Pichler (Dynatrace) 00:18:23 Yeah, I was, I was actually under the impression that we did exactly the opposite, so this is interesting to see.
Because I seem to remember running into this in the Python SDK at some point, and was confused that it wouldn't work, but I wasn't aware that this was also a problem in our SDK. So I think I have, bit of context on this, and I will take a look at that.
Hopefully. Or maybe we could get it in before the release.
Because this seems to be… actually more of a bug fix, rather than a feature.
jeremyvoss 00:19:03 Nice.
Daniel Dyla (Dynatrace) 00:19:08 Is there a, a spec issue to clarify it or anything like that? We should probably… I don't know, at least open an issue, just so that they're aware that It's not clear.
Carlos Alberto Cortez 00:19:21 Yeah, actually, that's what I wanted to say. I can take that on me. I'm curious about this part. I remember some complaints in the long past regarding coding, so I can take a look at that one.
Marc Pichler (Dynatrace) 00:19:33 Thank you for picking that up. Very much appreciated.
the, would be good to have some, sort of clarification here, so that every, every SDK behaves the same way, in these sorts of cases.
Alright, does anybody have any questions or comments around this topic right here?
Daniel Dyla (Dynatrace) 00:20:03 just to be clear, to make sure that I understood it correctly, it's actually… encoding, it's percent encoding values that it hits that are not typically allowed? Is that… It's not that it's… Like, decoding percent-encoded strings.
It's actually encoding invalid characters as percent encoded values.
Yeah, that's the…
Jackson-iPhone15 00:20:28 The new behavior.
Daniel Dyla (Dynatrace) 00:20:29 Okay.
Yeah. Or it feels…
jeremyvoss 00:20:32 Yeah, I mean, it doesn't… it's not like it even skips those characters, it just kind of crashes. Like, it… or rather, it just completely invalidates the entire attribute and everything that comes after it. That's the current behavior.
Like, all.
Daniel Dyla (Dynatrace) 00:20:46 Yeah, got it.
jeremyvoss 00:20:47 attributes, too.
that come out.
Daniel Dyla (Dynatrace) 00:20:48 That… There used to be a version of the baggage specification that said to do that.
jeremyvoss 00:20:57 Oh, interesting.
Daniel Dyla (Dynatrace) 00:20:58 Because the idea being… If you hit something… a character that's not allowed, like some… some sequence of bytes that's not allowed.
There is no way to know how to… like… you know, how to… how to interpret that. It could mean anything. Like, the… it could be that it was trying to, end the current value and insert a new one, and, you know, if you don't know What it means, then everything is invalid.
It's… it's just a much more strict way to view that. Like, there… In baggage, you know, it should be, under… You know, the happy path and everything. Should be impossible to ever see.
A baggage header with… impossible values. So, if you get them, you know something's gone wrong.
And it's not, like, an intended behavior.
And that was, at least… at some point, the baggage… I believe the recommendation was to drop the whole header.
Then it became drop everything after.
I think that might be the current state of the baggage specification, which, given that the formats are shared, may be where this came from.
jeremyvoss 00:22:29 Yeah, is there… is there, like, consensus on whether OpenTelemetry should follow all of the rules in the baggage specification itself? Because that would make sense why… why languages sort of reach different conclusions about how to handle the quote-unquote invalid scenario.
Daniel Dyla (Dynatrace) 00:22:48 Yeah, so I think the answer's no. I think if you look at the environment value or the environment variable specification. I don't think it mentions baggage at all. It just happens to share the format, right?
Carlos Alberto Cortez 00:23:03 Yeah, that's correct, I think…
jeremyvoss 00:23:04 Yeah.
Daniel Dyla (Dynatrace) 00:23:05 Yeah, so… so following the back…
jeremyvoss 00:23:07 It says that everything in it… all it says is that everything in it should, that everything outside of that range should be encoded. It doesn't say what happens if it isn't. So, yeah.
Daniel Dyla (Dynatrace) 00:23:23 Yeah, I mean, it's undefined behavior at the end of the day, but, like, you shouldn't ever… get those characters. The problem is, with the environment variable thing, now you're relying on like, user input, which is a lot less controlled. People are just probably copy-pasting things into, like, their AWS console, and it might contain, you know, frickin' whatever.
So you're more likely to get bad data in an environment variable.
jeremyvoss 00:23:54 Gotcha.
Marc Pichler (Dynatrace) 00:23:58 I think the reason why it's shared here is, At some point, we started using the baggage, I started reusing the package code for environment variable stuff, and it kind of stuck around in a bunch of different places in the repo.
so… I'm not sure if that is.
completely changed. I guess it's not using the shared code anymore.
But it might.
Daniel Dyla (Dynatrace) 00:24:30 Yeah, it's not.
Marc Pichler (Dynatrace) 00:24:31 Something we did in the past.
Daniel Dyla (Dynatrace) 00:24:32 detector, like, the resources package to depend on the… the… baggage.
Marc Pichler (Dynatrace) 00:24:41 Yeah, that makes sense.
So I guess, changing it is… probably the best way forward here. And there might be some other places as well, where we do some… weird things, that we might have to look into at some point.
I guess that should be… Everywhere where we read key-value pairs.
I think that's where we use the baggage stuff.
Daniel Dyla (Dynatrace) 00:25:14 The other… the environment variable configs may also reuse, but I don't… Know if there are any configs that accept A key-value pair list, so maybe it doesn't matter.
In any case, the only reason I even spoke up was to provide historical context. There's no… There's no reason that we shouldn't, do this. It's just in case anybody is wondering how we got here.
Marc Pichler (Dynatrace) 00:25:41 That's how we got here.
jeremyvoss 00:25:43 Well, should we, if we're going to create a spec issue, should we hold off and create a spec issue first to see what people say? Because it… it, like… I don't think the other languages could start doing what Node does, because that would sort of be a breaking change, to, like, suddenly not allow these values to be encoded by the SDK.
So, we weren't quite sure if this… if it, like, is worth making a spec issue about it, but, if we are making a spec issue.
would that mean we should hold off on this PR?
Daniel Dyla (Dynatrace) 00:26:18 I think… Given that it's… I mean, yeah, I see the logic there. I think… Given that all of the other SDKs are doing the same thing, which I guess I haven't verified, but I… that sounds like what you were saying. Maybe you haven't verified that either?
If all of the other SDKs are doing the same thing.
I think it'd be easier for us to follow them and create the spec issue and just document, you know, this is what all the SDKs did, because… I think, unless there's a major problem with it, the spec isn't going to… You know.
impose a requirement that breaks every SDK except JavaScript.
It's more likely to be the other way around.
jeremyvoss 00:27:09 Just clarifying my comment, I realize I said all other SDKs, but that's really just all that were relevant to our, like, actual team, which was…
Daniel Dyla (Dynatrace) 00:27:17 Yeah.
jeremyvoss 00:27:18 Python, Java, and .NET.
I don't actually know about the others.
Carlos Alberto Cortez 00:27:22 Actually, I would like to ask, is that a problem if we hold this PR for a week? I would like to spend a, you know, a couple days checking. Worst case, we come and discuss that in the next spec call next Tuesday.
So it depends on how, urgent this PR is.
jeremyvoss 00:27:38 Yeah, Jackson, how's that sound?
Jackson-iPhone15 00:27:39 Yeah, I think that's completely fine. Would rather have a good check over this than just rush it out.
Carlos Alberto Cortez 00:27:47 Okay, so what they don't mean?
Daniel Dyla (Dynatrace) 00:27:50 Yeah, so I guess hold off on this for now, we'll… and create a spec issue.
I join the spec issue every week, so I'm happy to talk about it, or obviously Carlos is usually there too, so… If you don't have time to join that meeting, that's fine.
and we'll go from there. I don't imagine that this change will be a problem, though.
Marc Pichler (Dynatrace) 00:28:18 Awesome. Thank you, R. Sounds like good way forward there. And then we can include that in the next release, after the one that's pending right now. So, should still… We would still be able to get it out fairly soon.
Alright.
There's no additional comments on this.
I guess we could move on to… But triage.
Carlos Alberto Cortez 00:28:55 Actually, sorry, since you are asking, and we are talking about specification, I think it's worth mentioning that yesterday at the spec call, Ted Young, from the GC mentioned that there are… they're having some conversations and, about trying to share goals between Sikhs, like, you know, currently each Sikh defines what is most important for them, you know? What we are considering, or at least the GC is considering, that we have, like.
some roadmap.
Like, for the next year, let's say for 2026, each SIG, and they present that to the GC at DC, and you get some feedback. And the idea is that, there are some… there's a mix between what each SIG needs to… to do, you know, that they think is very specific for them, and some shared goals. Like, for example, we want to finish this, or that signal, or wrap up with configuration support.
Stuff like that.
And, so yeah, it would be great to have, especially maintainers, but also provers could be great in the next spec call, which is every Tuesday at 8 in the morning, Pacific time. Otherwise, feel free to, to talk to Ted Young, directly in Slack, but it could be great to have, you know, maintainers there.
Marylia Gutierrez 00:30:14 Well, on that case, I can point out, because I'm… yeah, I'm also part of the GC, so what this SIG is doing is already kind of aligned, because the… one of the goals that we have is graduation, and for that, it's just making sure things are stable. So there are a few things, just, like.
as we are doing here, the stabilization of logs, of the database, HTTP, all of that are very aligned with what we are telling the SIGs in general to work on, usually to avoid things that are featured that are very, like, different from all other SIGs, like, completely, like, new features that only one SIG is doing, is the type of thing we say, like, try to hold on for a little while, but I think those are things already, like.
I already brought to this group, so they're already aligned with… and one of the other things, like.
We are hoping, like, even the event, like, Hotel Unplug is when people want to bring different things, that they want to change the roadmap, they can also have the chance to bring those topics.
Carlos Alberto Cortez 00:31:19 Yeah, it would be still nice in cold cases, in case there's some bigger discussion there. So, in theory, we will get more maintainers in the next spec call.
So, in case there's some, further feedback step there, it could be great to have you there.
Just in case, unless it's hard, yeah. Otherwise, yes, I think it's, it's fine. And in all cases, I think that whatever the result is will be communicated. Yeah, so… the shoe phone.
Marc Pichler (Dynatrace) 00:31:52 Sounds good. I will definitely join the spec car then, next week, and I will encourage others to do the same.
One question around this discussion in the spec car next week, is there an expectation that we have a list of topics ready already that we as SIG want to work on, or is that, like, basically a starting point for figuring that out?
Carlos Alberto Cortez 00:32:21 Yeah, I think it's more of a general discussion.
For now, yeah. Yeah, I mean, this is something that it's been discussed, as Marilla said, and, You seem to be in a good citizen So no need to, for now at least, to prepare anything. Just come and participate in the general conversation.
It could be nice, especially for other SIGs that may not be aligned.
As much as you, you know, for example. So yeah, just general conversation, I would say.
Daniel Dyla (Dynatrace) 00:32:51 Yeah, I've been talking with Ted about this a little bit, which is kind of, I think, where some of this is coming from, and I showed him our, like, focus topics thing that we already have, like, our… the way that we communicate the JIS roadmap.
And I think he's kind of trying to get other SIGs to do… a similar thing, and ideally, all SIGs would do the same thing, whether they're not… not necessarily that they're working on the exact same topics, but that they'd be communicated in the same way.
So that if you're like, what is Python working on? You don't have to figure out, oh, Python communicates that by pinning a Slack message, and then Java communicates it by having, like.
a priorities.md file in their docs directory, or, you know, I made those up, but… I think the idea is to unify how we're messaging Roadmap And then also to try to unify the roadmap topics, but those are kind of… they're two separate but related ideas.
Marc Pichler (Dynatrace) 00:33:54 I think that makes sense. The communication part, is… one of the more difficult things, I guess is something that everybody has run into, whenever I go to some other repo, I'm also not sure exactly what's going on at the moment, and I guess people are having the same, experience with us, daughter.js, to some extent as well.
Daniel Dyla (Dynatrace) 00:34:21 Yeah, one of the other, or there's a lot of other challenges, but, one of the big ones is when end users come to OpenTelemetry, and they're like, I want to use Configuration, declarative configuration.
And it's like, oh, well, that's not implemented here yet, and then they're like, well, it's been, you know, it says it's done, why can I not use it? And it's like, oh, well, this language has it, this language doesn't, it works slightly differently here, it's beta there, and like, the messaging to end users is a total mess.
So I think the idea long-term is to clear that up, and there was even some discussion about, like, project releases, rather than individual SIG releases.
But I think that that's… years off, if we ever get to there, but it's as a goal, as, like, a north star to point to, and say, this is what we want to do. I think that's kind of the goal, to move Towards a more unified type of, roadmap and release schedule.
Marylia Gutierrez 00:35:29 Yeah, and there… I don't know if you also know there's the Ecosystem project, Explorer project, that is ongoing, so that is one that would also help with things like that. So, for the ones that don't always… it's pretty much… exactly that, like, I have this SDK, and I want to know, like, is this following the semantic convention? Is, like, which one is following? What do I have?
And it kind of, like, shows what exactly is the state for current one. It started with Java, just because Jay is the one working on it, and he's in Java. But he aims to then add this to other languages, so I've been talking with him on also doing this for JavaScript. Might take a little while to actually reach other languages, but just something to keep in mind that might help users as well.
Marc Pichler (Dynatrace) 00:36:24 Alright.
Weird stuff.
One thing that I was just thinking about is there also, an idea of… defining process at some point, on how to do road mapping in SIGS, and stuff like that, because I think that's also been one of the… challenges that Sikhs have run into, that, you know, the process of like, defining a process of how to get to a roadmap has been kind of bumpy. That's also something that's not, well-defined for us, at least. We have the focus topics thing, and we… Decide on what we are going to do, to a certain extent, but there's no, like, formalized way of doing it.
is anybody aware of such an effort?
Daniel Dyla (Dynatrace) 00:37:22 That's what Ted's working on.
Marc Pichler (Dynatrace) 00:37:24 Oh, okay.
Daniel Dyla (Dynatrace) 00:37:25 At a high level.
It's to be determined if we, like.
How far that actually gets, because… A roadmap kind of implies… you know, we're gonna release this feature in April, and this feature in June.
and as an open source project, we… it's tough to make guarantees like that, right? Because you… it depends on… Contributors and reviews and all kinds of stuff like that.
So… what Ted and I talked about, and this is not… this is not decided or anything, so don't take it as, like, a final decision, but what Ted and I had talked about is the idea of… the individual SIGs having charters that they would renew every year. So, you would have a document that says, we are the JS SIG, we maintain these packages, and in the next year, we hope to accomplish these things.
And then you take that to the TC, they approve it, which, you know, gives… means that they are happy with the priorities you've decided on for the next year.
Or they say, you know, we think this is higher priority than that, kick this out, or add this, or whatever.
You know, come to a consensus, approve the charter, And then… a year later.
you go back and you say, what did we fulfill from the charter? You make a new charter and, you know, kind of have more communication with project leadership that way.
Cause one of the problems we're trying to… Address is the… To sort of… limited communication between implementation SIGs and project leadership.
Marc Pichler (Dynatrace) 00:39:21 Sounds actually like a really good way of going about things.
Daniel Dyla (Dynatrace) 00:39:26 Yeah, Ted was worried that the SIGs wouldn't want to do that, because it sounds like a lot of work, and I was like.
I… as a maintainer of a SEG, I would be super happy to have, like.
any feedback at all. Right.
Carlos Alberto Cortez 00:39:41 But, you know, this is… but this is why it would be great to have maintainers come and, you know, provide their feedback, even before we, you know, decide yes or no. You know, like, I think maintainers know better, so it would be great to have that point of view.
Daniel Dyla (Dynatrace) 00:39:57 Yeah, and I don't think the charters are gonna be, like, you know, 10-page documents, you know, we don't work at, you know.
I won't call out any specific companies. But, you know, just like a one-page of, like, you know, this is the general… what we're working on.
Marc Pichler (Dynatrace) 00:40:14 And it's one of the things that you have to do anyway, to some extent, so might as well just do the same across all the six. I think that makes sense, yeah.
Daniel Dyla (Dynatrace) 00:40:25 Yeah, not only that, but actually, The governance documents say we do that.
We just don't. So, there's that part of it, too.
Marc Pichler (Dynatrace) 00:40:41 Right?
Thanks for, bringing that up. Excited to see what, What we can decide on there.
Yes, let's move on to… park triage. As always, if you have any topics, or want to discuss something else, please feel free to just interrupt me while we do park triage, or PR review, or whatever we're going to do.
And then we can go back to talk about the other topics there.
Let's get started with bugs in the corrido.
The first thing here is, Zone Context Manager.
causes infinite task scheduling loop when used with RCLN.
It doesn't sound great.
There's a red click to crash repro button, that's… Seems that browser tab immediately freezes, CPU user spikes to 100%.
Some chairs, his munchies.
Daniel Dyla (Dynatrace) 00:42:14 RC Align is constantly calling clear timeout. That gets intercepted by ZoneJS.
and the Zone.js Context Manager is… Causing it to lock.
Because Zone.js Monkey patched clear timeout, and then we… Monkey patch zone.
Yeah, the workaround of replacing the zone context manager with a stack context manager works, because the stack context manager doesn't do anything.
Marc Pichler (Dynatrace) 00:42:57 Yeah.
Daniel Dyla (Dynatrace) 00:43:04 I don't know…
Marc Pichler (Dynatrace) 00:43:07 Hmm.
Daniel Dyla (Dynatrace) 00:43:08 This is gonna be a really hard one to track down.
Marc Pichler (Dynatrace) 00:43:14 Yeah.
Daniel Dyla (Dynatrace) 00:43:14 Is, does anyone know what the current state of Zone.js is? I know it was, like, deprecated, but then I think kind of revived because the deprecation was, you know, it's used by too many things.
Marc Pichler (Dynatrace) 00:43:28 There was recently a new version that was released, I think, so… There was supposed to be a… I think there was supposed to be one last release of it, but there was another one.
So I guess it's somewhat alive still?
Daniel Dyla (Dynatrace) 00:43:54 Yeah, I mean… I guess it's also… Kind of to be determined whether this is a bug.
with us, or… you know, I… I… I don't know whether this is RC Align abusing something and it just shows up now. You know, it's not like… You know, if you put… diesel… fuel in a gas car. The car's not broken.
or incorrectly designed, I guess it is broken now.
But, Yeah, I don't know if that's this situ- if that's what this situation is, or whether we actually are doing something wrong.
Hard to say.
Marc Pichler (Dynatrace) 00:44:50 No.
Daniel Dyla (Dynatrace) 00:44:51 This is on his choice.
Marc Pichler (Dynatrace) 00:44:52 More investigation here.
Daniel Dyla (Dynatrace) 00:44:57 I think we can ask Legendicus to look into this, though, because as far as I know, he, is the most… has the most context about the way that Zone actually works.
It probably would be the best to track something down.
Trent Mick 00:45:15 I'm pretty far from authoritative on anything around this, but, the Zone.js readme at the top says, while still a supported part of Angular, the Angular team strongly discourages using Zone.js outside of an Angular application.
So… I don't know if that's… something that we would want to move towards suggesting that don't use Zone for context management unless you're using an Angular app, because… weird stuff will happen, and it's basically not a supported path. I mean…
Daniel Dyla (Dynatrace) 00:45:44 Yeah.
Trent Mick 00:45:44 Sorry, there's no replacement, but…
Daniel Dyla (Dynatrace) 00:45:47 Yeah, that's the hardest part. Sorry, there's… Yeah, sorry there's no replacement, it's the hardest part. I don't know.
Marc Pichler (Dynatrace) 00:45:56 I wonder if this is something that would be interesting for the browser sig to have a look into as well.
the context manager… I'm… I keep forgetting what the plan will be for, browser instrumentation.
But I suppose context management is still a part of that.
Daniel Dyla (Dynatrace) 00:46:22 Yeah, so I think… Right now, they're focusing on the instrumentation part of it, with the underlying assumption that everything in the API and the SDK works and works well.
They know that that's a flawed assumption, but that's… You have to start somewhere.
I think… we could… Tell them… like, they're probably aware of the problems with context management in the browser.
So we could probably tell them, like, hey, we would prefer to move away from ZoneJS entirely and see what they think, because all it would mean is that the instrumentations would have to do manual context management.
Probably all of the instrumentations would have to, which complicates the instrumentations, but… Might be worth it if we could drop the zone dependency.
Marc Pichler (Dynatrace) 00:47:22 Yeah, I think, one of the things people have been asking about is to not have the zone context manager, though I'm not sure if they know what that entails, not having it,
Daniel Dyla (Dynatrace) 00:47:40 I'm quite certain they don't enough.
Marc Pichler (Dynatrace) 00:47:42 I will, note down an action item for myself, to… I'll reach out to folks and see what they think.
Trent Mick 00:48:00 Unfortunately, the OpenTelemetry I.O. Getting Started doc for… Browsers.
shows using Zone Context Manager.
Marc Pichler (Dynatrace) 00:48:10 Yeah.
I think the reason that it does is, because without it, won't get, You won't be able to, track context across, promises.
Daniel Dyla (Dynatrace) 00:48:29 Rc Align is also archived.
It's not supported. Last release, December of 2022.
The repository is public archive.
So… Yeah, I guess… I'm not saying we shouldn't look into this, but it's probably… Not something we need to get too bent out of shape about, either.
Marc Pichler (Dynatrace) 00:49:01 Alright, I guess, I will follow up on that, and then we can see, Where that leads us.
Right, another browser thing… Browser detector does not accurately detect browsers. There was, pull request here.
checks if Navigate, let's define… Compass returns the empty resource.
Daniel Dyla (Dynatrace) 00:49:57 It says the test suite uses a more accurate check. Would you click on that link?
Yeah.
So it's just a different way to determine if it's a browser.
I guess that's the opposite. This is detecting if it's node, but… .
Marc Pichler (Dynatrace) 00:50:20 Could be flipped.
Daniel Dyla (Dynatrace) 00:50:26 Well, Node is not the only non-browser runtime.
Marc Pichler (Dynatrace) 00:50:34 I wonder why I use the browser detector, denote anybody?
Daniel Dyla (Dynatrace) 00:50:42 Bet I know, but if we… if we use that detector.
and say, if this fails, then we're in a browser, then potentially it's wrong in other runtimes, like, I don't know, Deno or something like that.
Trent, I didn't mean to cut you off there.
Trent Mick 00:51:04 I just put a link in chat, this tickled a memory. We had an issue Assuming almost exactly like this, so now I'm wondering what this… Code is. Is this referring to a really old… Version of browser detector?
Did you see the link that I had in chat?
Marc Pichler (Dynatrace) 00:51:22 Let me pronounce it kind of…
Trent Mick 00:51:26 And then go to the PR that changed this.
And the diff.
So, here's Brazo Injector.
I don't know if this is ancient and maybe got lost when we did all the resource.
detector changes?
But there we were not just relying on Navigator anymore, but also following back… falling back to… Process versions node.
And something for Bun, and… You got it.
Yada yada yada.
No, I don't know what the current state is.
Daniel Dyla (Dynatrace) 00:52:05 Yeah, part of the problem is, like, it's an endless game of whack-a-mole trying to determine what.
Trent Mick 00:52:12 Yeah, that code's basically acknowledging, like, we don't have a way to do it from just browser APIs, because everyone's trying to emulate the browser, so you have to.
Daniel Dyla (Dynatrace) 00:52:20 I'm not.
Marc Pichler (Dynatrace) 00:52:30 So…
Trent Mick 00:52:30 I wonder if that change just got lost in the browser detector changes, because that ER showed a diff on browser detector sync, which we dropped.
All the sync ones.
Daniel Dyla (Dynatrace) 00:52:40 Yeah, so I wonder if this fix was not applied to the async one.
When it was applied last year, 2 years ago?
Marc Pichler (Dynatrace) 00:52:51 Exactly.
Or, I think, what happened?
Trent Mick 00:52:57 We had the browser to demonstrate…
Marc Pichler (Dynatrace) 00:52:59 Yeah, we had the browser detector package, and then we had a browser detector that was not stable in the resource package, and we were thinking, why have both?
There should only be one browser detector, and that's the one that we chose.
So probably the fix was…
Trent Mick 00:53:20 And it's Dan's fault he removed it.
Good afternoon.
Daniel Dyla (Dynatrace) 00:53:25 Most of the problems in this project are my fault in one way or another.
Marc Pichler (Dynatrace) 00:53:29 No, I… no, I think I'm… I'm…
Trent Mick 00:53:31 Three of us.
Marc Pichler (Dynatrace) 00:53:32 Way up there?
Trent Mick 00:53:34 Distributed faults. No, Mark's the only one with clean hands on this one. You didn't touch this, PR.
Daniel Dyla (Dynatrace) 00:53:38 Yeah.
Marc Pichler (Dynatrace) 00:53:39 I… I did approve it.
Daniel Dyla (Dynatrace) 00:53:41 Problems caused by maintainers, is that, like, something I can look up in the CNCF dev stats, I think?
Trent Mick 00:53:47 better resolution.
Daniel Dyla (Dynatrace) 00:53:49 Gotta be top 10.
Trent Mick 00:53:53 Okay.
Marc Pichler (Dynatrace) 00:53:54 Right, so I guess we were just…
Daniel Dyla (Dynatrace) 00:53:56 So we just probably imply the same fix.
Marc Pichler (Dynatrace) 00:53:59 Yeah.
Trent Mick 00:54:01 Brick.
Daniel Dyla (Dynatrace) 00:54:01 So, we could probably even just mark this as, like, a good first issue or something like that. Like, this could be most likely solved by anybody in… Very easily.
Marc Pichler (Dynatrace) 00:54:13 Hmm.
I'm not gonna add a lot of context to the, Thing why it's not there anymore.
Or follow up on that after the meeting tomorrow.
Trent Mick 00:54:32 I can.
For that now, while you move on, if you like.
Marc Pichler (Dynatrace) 00:54:35 Yeah, thank you.
I put, good first issue.
our outcome.
Or both. Let's do both.
Alright.
The next one is Instrumentation fetch. Lots of browser stuff today.
loses response to the URL and response.type.
Competice.
Original response… I suppose this was one of the recent changes around, streaming responses, I was trying to fix another bug there.
It's caused by wrapping the original response.
object here.
Yep.
That's… Fairly recent, 4 months ago.
That is a P1 bug, because it causes… problems.
With stuff getting lost.
And wet.
Cause different behavior based on whether the instrumentation is installed or not.
I won't have time to look into this one.
Maybe we couldn't.
Let's see here, is that the person that's around? Not sure.
In any case, this shouldn't happen.
Trent Mick 00:57:00 maybe I'm learning here, you marked this as a P1?
Thought that was for crashers, but…
Marc Pichler (Dynatrace) 00:57:06 I also see that it says data inconsistencies in the name.
Yeah, it's essentially… like, it could lead to a crash, because you expect something to be there that wasn't there.
Yeah, it's essentially anything that changes the behavior of the underlying library that you're using, or the underlying concept that you're using.
From… The original behavior, other than just emitting telemetry.
Trent Mick 00:57:39 Oh, sorry, I missed the impact here. I thought it was just one tree, but okay, cool.
Marc Pichler (Dynatrace) 00:57:47 I guess, we can leave that as P1 if somebody wants to pick that up, that's, Appreciate it, but, Like, other than just wrapping these two and making sure that it's up-to-date, or just forwarding these two things.
Making sure that all the other, properties are also forwarded, I don't think there's any other way to do this.
I feel like we've been going back and forth on… that… part of code for… at least 2 years now.
The streaming response thing, and then a few other… Things that cost… Do you want Fox, Seems to be very difficult to get right.
Anyway, I think that's it for the core repo, and then we can move on to Country.
The first one is… And then we'll do P.
Races split with other services after instrumented.
By a self-building video.
Two trace IDs, context not successfully propagated during the lambda to lambda implication process.
I wonder if this is, Come with, context manager missing, or something, or propagator not being defined.
In any case, I think we have run out of time for today.
So, that's… Stop it here, and we can continue.
Another time on this.
Also have a look.
Daniel Dyla (Dynatrace) 01:00:32 Thanks, Mark.
Marc Pichler (Dynatrace) 01:00:35 Thank you, everybody.
Thanks for joining, have a nice day, and see you next week.
Thanks for our friend.
