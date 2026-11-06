SIG: Swift SIG
Date: 2026-11-05
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Marius Ciocanel 00:01:58 Hey, Vishwan.
Vishwan aranha 00:02:00 Hey Marius, how are you doing?
Marius Ciocanel 00:02:03 Yeah, good, good.
here for the meeting, but I can only stay for about half an hour, so hopefully it's, We can address things quickly.
Vishwan aranha 00:02:13 Yeah, I'm gonna drop in, like, 30 minutes. I have another meeting, so… it seems like we don't have many topics today.
Marius Ciocanel 00:02:20 Yeah, no, I don't think so.
I have a question myself, about how to handle those things, but
Vishwan aranha 00:02:30 Did you add it to the dock, or…
Marius Ciocanel 00:02:33 Yes, it's, it's the last one with, Let me see. So, yeah, it's… it's about… this, semantic convert… conventions, there was a script.
That basically pulled, all these semantic conventions, and the question is how about handling deprecated attributes. I'll explain a bit.
there's a draft out, PR.
That explains it, that I've opened.
Vishwan aranha 00:03:08 Yeah, we can… we can wait till everybody joins in, then, as we go through it. Yeah, yeah.
Marius Ciocanel 00:03:19 Hey, everyone.
Ben Joseph 00:03:24 Hey, guys.
Marius Ciocanel 00:04:31 How's the weather where you guys are? Because today we had the first negative… Temperature.
Of the year.
Minus 1.
So, I don't know how,
Vishwan aranha 00:04:49 It's warmer for us, like, 70 degree Fahrenheit, which is, like, 19 or 20 degrees Celsius, so…
Marius Ciocanel 00:04:56 Well, this is minus 1 Celsius, so it's, like, below freezing.
It was… it wasn't… it wasn't great when I had to scrape the windshield in the morning to…
Ben Joseph 00:05:08 Peace.
Marius Ciocanel 00:05:08 To drive away.
But,
Ben Joseph 00:05:11 We're gonna have a light winter this time, hopefully.
Marius Ciocanel 00:05:16 Yeah, with fuel prices.
Fair enough.
Billy Billy 00:05:20 Yeah, it's still ideal fall in the States, for most places.
Marius Ciocanel 00:05:33 Did… Oh, hey, Nacho.
It's so weird, I'm not used to, Zoom hiding people. I only saw 4 people, I was like, we're still waiting.
Nacho Bonafonte 00:05:47 Hello?
Marius Ciocanel 00:05:48 Hello?
Nacho Bonafonte 00:05:56 We already created the document.
Okay, yeah, I think we are all again. Let me share the document.
Mmm… So… topics from… last week… Yeah, we talked about the device ID requiring privacy disclosure.
We… we… we got to the threshold that we thought it needed.
And we talked about… duplicating the device ID into the app, right, Ben?
Ben Joseph 00:06:51 Yes, so, yeah, I think, I raised a PR last week for… Adding it to app.installationID, and that's merged now.
Nacho Bonafonte 00:07:12 It was app ID? Just no, it was… App…
Ben Joseph 00:07:14 app.installation.id.
install.id, sorry, I don't call it.
Nacho Bonafonte 00:07:20 Yeah, no, no worries, I mean… Okay,
Ben Joseph 00:07:32 installation, yeah.
Nacho Bonafonte 00:07:34 Oh.
Installation, okay, yeah.
Sorry.
Okay, the other topic was about the, Parkgate Straits.
There were some questions about it. We… yeah, I pinged Vladimir, because as you… yeah.
I just… I don't know who remembered. Yeah, it was there, so I… Pinned him into the… into the thread?
Marius Ciocanel 00:08:06 I mean, Vladimir is here, he can maybe…
Nacho Bonafonte 00:08:09 Yeah, that's right.
So, yeah, yeah, he answered here.
So the… the… the user who was proposing it Ask, for some ideas.
And the proposed trades.
I don't know if you have followed it, but yeah, basically he proposed this trade.
And he also… Yeah, he also asked… Moving to GRPC Swift.
2?
Which, apart from that, which I said that… Yeah, as next version is a major version, we saw that everything as a single step is possible, better than having several steps. That was one of the things he Was asking here.
Next version is a 3.0. It will be 3.0. So, yeah, we… I think it's better. I don't know your opinion, but maybe, if you have… please raise your hand, or just speak outright, basically. No raising hands, please.
cut my, cut, cut me talking. And I, and I think it's better Just doing it in one step, everything just working, without having different setups in the future.
But I also said that about gRPC Swift 2, I think that's orthogonal to… This, trades thing, but I think… I'm not sure if… it will be possible to support this conditionally, depending on trades for different platforms. I don't know if that if… Apart from the different versions, if… It could… if trades can handle different versions Of the same dependency.
I don't know if that's possible, but… we cannot drop gRPC, not… Swift, the year PC.
Swift 1 version still, because we still need some Super for older versions.
So I think we should move… that's what I said, move to trades.
But they still not changed to ERPC Swift 2.
And evaluate that.
after moving. But I don't know if maybe Vladimir or any of you have more experience with trades, and if… Supporting that.
in the same platform is possible, or just will be needed for Linux, for example, because Linux will never use Swift 1, or something like that, right? That can be probably supported on… on trades, but I don't know if, for the same platform, the same dependency, depending on your trades, having two different versions will work.
Vladimir Kukushkin 00:11:18 That's a very good question. So… Having… definitely having to… Different versions have the same dependency in the… in the dependencies.
Depending on trees isn't possible, but having different dependencies based on traits, horse chicken, I don't know.
might work, might not work, but that will be SwiftPM in the patient.
Nacho Bonafonte 00:11:46 Sorry, I didn't… I think I didn't catch the last…
Vladimir Kukushkin 00:11:50 So, if it doesn't work, it's gonna be blocked by SwiftPM, so… Not something that we could easily…
Nacho Bonafonte 00:12:01 Okay, so yeah, that's something we must try later, right?
See if that's possible.
Okay.
Okay, so then, I don't know if any of you have a different take on this, if… That please raise here now, or raise later in the thread.
I… maybe I… I'm thinking that I didn't say that the proposed trades, I am… If they are okay. So maybe he's missing that information for the… For starting the PR?
So, do you… all of you, agree that Trades are… Makes sense?
For a production point of view?
Billy Billy 00:12:57 Yeah, are there any, like, backwards compatibility issues, or is it… I haven't… Implemented it before.
Seems fine otherwise, yeah.
Nacho Bonafonte 00:13:17 Sorry, what, I was writing, sorry.
Billy Billy 00:13:22 I was just asking if there are any backwards compatibility issues for this. I know that if you said it's, like, additive only, so… If not, then it seems totally good.
Nacho Bonafonte 00:13:33 Yeah, I mean, the only dependency is on Swift 6.2, So, as we already have the minimum 6.2 version, you could… at all trades and have all the libraries that we have now. That… I think that… that's supported.
Billy Billy 00:13:50 Okay.
Nacho Bonafonte 00:13:51 Yeah.
Yeah, if I am wrong, please, someone just say the opposite, But I think that that's, like, that… doesn't limit you, or doesn't… and students have, I mean… Only on SwimPersia is the limitation.
Marius Ciocanel 00:14:12 I think there was also, a bug.
With traits that was fixed in a slightly… higher version of Swift.
I don't remember exactly what the details were, but I remember when I was looking into it, trying to figure out what… how traits worked.
There was an open issue, but I guess people could… Bump the… The version of a bit if they want to.
Yeah, I think… I would say, if they want to create a draft PR, so we can see how it works.
Nacho Bonafonte 00:14:53 Yeah, that's right. Yeah, if we have even… not Nadrat, right, you can still download the branch and test that.
Local, so yeah, that… Yeah, that sounds perfect for the dependencies thing, and the problem with downloading everything, and probably also will… will help with, some Linux support for some libraries that… Yeah, currently I'm not.
version-friendly. So this one, Okay, yeah, update the README with 6 mentioned and new instrumentation. Yeah, that… yeah.
Yeah… oh, sorry, one minute.
OEM. Yeah, basically, yeah, we… I created the issue, and yeah, this one was really fast, and took it. So, have you taken a look on that, PR?
I think Marius said he was gonna try to…
Marius Ciocanel 00:16:41 No, I think a bit Vishwan did it, but it's fine. It looks good.
Vishwan aranha 00:16:45 It was a small change, yeah, it was not, like, major, so…
Marius Ciocanel 00:16:50 Yeah, no, it looks good, I think. Can be merged.
Nacho Bonafonte 00:16:53 Okay, yeah, then… I… as no one more had approved, I just waited for today, but if you have taken a look, it looks good.
I will address… I will… Yes, Merchief. Yeah.
If you have any other change you want to add, just another PR, so that's great.
Vishwan aranha 00:17:14 I might have a couple of them coming up, but, yeah, I got busy with some work, so I will look at them next.
Nacho Bonafonte 00:17:21 Okay, yeah, great.
Okay, and the other topic was the automatic semantic conventions creation?
Marius Ciocanel 00:17:33 Yeah, so I had a look at that. There's a draft PR that I put in the new topics, it's the second link at 1274.
Nacho Bonafonte 00:17:43 In the PRs, you created one?
Marius Ciocanel 00:17:45 Yeah, it's, it's a… That's new, right? It is, literally, half an hour ago. Just because I was testing… I was trying to understand what Weaver did, and, like, seeing very… like, I ran various, runs, so it, fixes… There was an issue with the script, where… Just trying to find a version, and… but nothing matched, so that was fixed.
Also, Weaver, was a very old version, so I tried to bump that first.
Basically what Weaver does is… Takes the semantic conversions and and uses a template to generate, code, like Swift code.
So I made sure that I went to the latent version of Weaver, and had to make a small fix.
Which is mentioned at point 2, where it kind of generated weird-looking code.
But made sure that I kept the semantic conventions version the same, and just upgraded… updated Weaver.
And with that fixed, it basically generates… well, generates the same thing, which is exactly what we have in Maine, so,
Nacho Bonafonte 00:19:12 Okay.
Marius Ciocanel 00:19:12 it works fine. But there is a question about this one, because the next step would be to… actually update the semantic version com… some semantic conventions version.
We're at one… 38.0, and I think the latest is 144 or 45, I don't remember exactly.
But what happens is… Weaver is set to… Delete… deprecated.
attributes.
Which means… Code gets deleted, so if someone uses Like, some old, attributes, they will have breaking changes. It's, like, basically like a code-breaking change. Okay. We could make a change so that we declare them with, like, a deprecated attribute, rather than deleting them completely.
So I think that the decision is now, are we… I guess if you scroll down a bit to the third one, is, like, do we want to… half-breaking, or, you know, not in this PR, the bit in… that says not in this PR at the end.
do we want to, I guess… Keep the deprecated attributes and just mark them as just deprecated.
Or do we want to delete them and say that they're going away, and, like, when people… I don't think people will appreciate it very much, like, if they started using something, if it goes away, and with a… with a version of the library. I think that my proposal would be to mark them as deprecated, and that will show up as a warning in Xcode, rather than actually break So I think that this is kind of the decision, like.
I would like us to… to take. Would it be okay if, like, the next PR For this would… would change the… What we do, rather than delete the… The deprecated attributes, we just mark them as deprecated instead?
Or are we okay with brew, with breaking changes?
Billy Billy 00:21:45 Yeah, I remember there's, like, all these, like, hidden, tech debts inside this, like, outdated, SEMConf that's, like, referenced, so, like… Yeah, I'm concerned if we, like, fix it, it'll just, like, change the schema for everybody, and then, it might even break builds.
It's, like, so it's, like, not an easy fix from what I recall.
We might have to, like, do this in a new major version, I'm also curious if, like, you know, CI, like, passes for, like, this fix as well. So, yeah, I think it's, like, kind of a…
Marius Ciocanel 00:22:21 Technically.
Billy Billy 00:22:22 I'm hitting this…
Marius Ciocanel 00:22:23 At the moment, this… sorry, but at the moment, this won't change anything, because this is a script that only runs manually, so nothing actually changes.
Billy Billy 00:22:32 It's just…
Marius Ciocanel 00:22:32 a bit of tooling… tooling change, so I am waiting for CI… I was waiting for CI before I kind of… Made it available for review, but, like, on my own, kind of.
work, but yeah, like, nothing really changes. There's no… no file changes. I did run it locally, and, at the moment.
If you run the script from this branch, it will not generate anything new.
Because I haven't changed the semantic convert, like, conventions version, just the tool that performs the… Template generation, like, code generation. This is why I wanted to have a conversation, because, like, changing the semantic conventions version will generate, like, some new files, and, like, we'll have a proper diff with things being removed.
Billy Billy 00:23:25 Yeah, that makes complete sense.
Marius Ciocanel 00:23:27 So I wanted to keep it separate.
Billy Billy 00:23:29 We… I think if we do this, we should just do it complete from beginning to end.
And, like, create a plan for, like, major version bump, just so we're actually, like, you know, up-to-date, and… If there's any, like, weird… we don't have that many instrumentations yet, so this is, like, a really good time to do it.
And if there's any, like, breaking change to the schema, like, we'll have to, like, you know, go through and review that. Yeah, so I think we should… I think we should do, like, everything together, and not just, like, update the script. Otherwise, we're in this weird partial state.
Yeah.
Nacho Bonafonte 00:24:05 Yeah, yeah, yeah, that's a… Brilliant, brilliant.
Yeah, good question about, yeah, the preparating or breaking, right?
This is probably, probably a good moment to do that break-in.
Because we are going to a major version, but we are not usually going to major versions, and updates will happen.
I don't know if they removed values, very, very usual. But, yeah… I think having them deprecated is probably… The, the, the way to do it, safely.
So we don't break it in the future if the semantic conventions get new, and a new session thing appears that we are using, but on the other side, something on, you know… to say… Tafka… instrumentation just changed the name, so we… and we can break something if something changes that we are using, and we don't really realize about that. So, if it were… if it was possible to Have a parameter on the script?
To just remove or not remove, and use the deprecation by default, that will be great.
And we can think so the user can think if they want to remove or not.
For this 3.0, my take would be breaking, because it has been a long time since we changed, so it's a good time for everyone to update their things.
But, yeah, I don't know.
Would they be able to… I mean, if we break that to users, would they be able to create an extension?
On that type, and create the old version of their code.
Because we are not breaking it, right? They can extend with an extension any type that we create. So they could add the break. If they don't want to update their things, could they…
Billy Billy 00:26:08 I think that we We have the, the schema, don't we? So, like, they could be using… like, you know, consumers could be using the schema.
Right.
Nacho Bonafonte 00:26:18 Yeah. Another option would be, maybe, Hiding that in an extension?
Instead of, putting them as deprecated, adding extension, To the namespace that say… Deprecated.
You know what I mean?
if you add the deprecated type, you have access to the old ones? I don't know, just thinking for your use cases,
Marius Ciocanel 00:26:47 My…
Nacho Bonafonte 00:26:48 Yeah.
Marius Ciocanel 00:26:50 So I ran… I ran this, like, locally to… I basically bumped the semantic conventions. I bumped it to the next version just to see, you know, from like, a minor, minor, bump, what would that change? And… from what I've seen, like, the diffs are… basically… like, some strings that are used as, as keys. Like, leaving them as deprecated won't really break anything?
And it's up to the… you know, if someone… Right now, takes the, you know, would take the library and wanted to use them.
they would look and say, oh, this is deprecated, what, you know, they would probably look at something else. Having… I think having them in there.
woods… I guess, maintain backwards compatibility for a very long time. It's just… but if we do want to… Have, like, breaking changes with version 3.
This is the time to do it, as well.
If we're gonna have any other breaking changes, then it kind of makes the decision easier.
Nacho Bonafonte 00:28:09 Yeah.
Marius Ciocanel 00:28:09 Like, delete everything that was deprecated anyway.
But if this is the only breaking change, I would choose… To mark them as deprecated instead.
Does that make sense? Yeah.
Do we have any other breaking changes that… Perfect.
Nacho Bonafonte 00:28:28 Consido, yes.
Right, yeah.
Ben Joseph 00:28:31 Yeah.
Stop this.
Nacho Bonafonte 00:28:33 Yeah, of course.
Ben Joseph 00:28:35 Yeah, I just want to add my two cents. I think, like.
If we are going to 3.0, as a major version, I think now is the time to just, get rid of all. Yeah. Because, Nacho, it's not just, like, typically, you know, anybody who is using Autel, right? Like, they have multiple, platforms, it's just not… Swift or iOS, right? Like, so every other, project is using the latest version of semantic convention, so when you're building a pipeline that consumes this telemetry, if we are on the oldest and, like, sending the older data, it just makes it difficult for the consumer to manage it, like.
Every, every other, just for SIFT, they will have to maintain the oldest version. So, I don't think we are doing anybody a favor by, you know, not breaking things. It's… it's… because, like, there are so many OpenTelemetry projects, and all of them consume the same semantic conventions. I think it's in the best interest of all of us to have the latest version.
If there are, like, specific circumstances that we want to, you know, maintain both, I think, HTTP is a good example. We maintain… we have a flag which says, use stable or latest.
And, based on that flag, we send the semantic conventions, that is the newer version or the older version. Like, so if there are, like, specific items that we want to maintain, I… I'm not in favor of that, like, if the semantic conventions have moved to a new Newer label, I think it's best that we all adopt it. There is no reason Just thus maintaining or holding onto this older version is not in the wider interest, in my opinion.
Marius Ciocanel 00:30:22 Aye.
Yeah, I think I agree with the sentiment. This is the best time to break. Like, if there's going to be breaking changes, let's make all the breaking changes we can.
Nacho Bonafonte 00:30:33 Yeah, the…
Marius Ciocanel 00:30:34 I can do that. Yeah.
Nacho Bonafonte 00:30:35 How about adding the parameter to the… to the script, so we can break or not break? So, break or deprecate? Because… If we have some minor update, and we need some new Thing we don't want to break existing.
Because if it doesn't build, you know, it's a breaking change, so it should change a major… If we keep the philosophy we have tried to keep, so… So I think breaking today is great.
We can break now?
But in the future, maybe when we release version 4, then we run it with a break, right? And we… everything that was deprecated in the 3.1, 3.2, whatever we release in between.
can be kept deprecated, and break… Right, so.
Marius Ciocanel 00:31:27 Let me see if I understand what you're saying. So you're saying, for 3, we can run the script And, run it with the parameter that says you can make breaking changes, which means delete everything that's deprecated, so that we take it as an opportunity to you know, since we're breaking stuff, might as well delete old code, which I think is a good idea. But then, if you do, like, a 3. I don't know, 3, 3.1, 3. And then we, like, there's new semantic conversions, we mark them as deprecated in the same major version, rather than Deleting, which would be a breaking change, which we don't really want to do, unless it's a major… Semantic version, yeah? Okay, I think I got it.
Nacho Bonafonte 00:32:13 Yeah, for example, if we, you know, for example, I say sessions, for example, that's something that's more or less updated, now more than other, other areas, and a new parameter attribute appears there that we just want to report. If we just update to the new semantic conventions for that parameter because we need, or we want to support it new, and we are breaking other code.
That's a problem for our users, right? Those who use the old things will get the deprecated warning, so they can act and have the new one, but we are not breaking them if they are not really using that, right? Or if they don't care about that, or if they are not updating the collector at the same time that they update the library.
So yeah, I think… That's the best way to go.
Just having a parameter. Breaking, so run it now for this… For the main now, run with a break and delete all things, but have the option when we update between major versions to have that deprecated.
Marius Ciocanel 00:33:25 Okay, yeah, I think I… I just wrote a comment… To that.
If you refresh, with what? Yeah, there.
So, add a parameter to that script, so that we can run it with… Either delete for a version like 3.0, or make deprecation, or mark them with… with that, or… Yeah, okay. I'll, I'll… yeah, I'll look into this.
Nacho Bonafonte 00:33:54 Yeah, I think that's the best. Oh, sorry, yeah.
Ben Joseph 00:33:57 Yeah, so I, I, I wanna, so now, now the semantic conventions, follow something called schema 2.
Which is federated, which means that it's not just one single semantic convention repo. There's a client-side repo that aggregates, you know, anything that's used across Android.
iOS or Swift and browser, so that, like, the semantic conventions are, like, defined in multiple places.
just… I'm trying to give a reason why it's in our best interest, or for the wider community, why we should be on the latest version. So before this, when the semantic convention was defined in just one place, there used to be something called, a schema, which would help with the translations for consumers. So, every consumer would refer to the schema. Say, for example, from… we are… we are on 138 and, moving to 144. Something got renamed. So, the schema when they released the schema, they also release a… I think it was a YAML file or something.
that would tell the consumer how to handle this rename. So, if something from http.request code to http request.code, then it would… it would tell you how to handle that rename. So, if somebody… if we are always on the latest version, and they refer to the schema, the consumers do not have to manually handle this, rename, or any of the duplications, or… You know, additions that happen, so… That… that schema existed before. With the federated, conventions, I think the… how… how the schema change will be handled, I think that is still being discussed. I think, for each layer or hierarchy of the schema that's being defined, it will have its own schema file, and it will define, how this should be handled. The problem is that, like, if we should pin a release, like, for example, 3.0 of Swift.
it should use a specific version of schema. Say, for example, 145, the newest that's available. If that's the case, then the consumer knows, okay, for this schema.
this is the, for this Swift release version, which we send in our metadata, right? It can identify which is the SDK version that's being used. Okay, this has 1.45 pinned, and this is the, schema, how I should handle the schema. What… what… The complication on the consumer side is when we… when we vary from this pinned schema version. For example, we allow users to manually, even if this is the pinned version, and we allow to use an older schema, then the consumer doesn't know what to expect. Like, it knows the SDK version.
From that, it can infer the schema version, and then if we are sending telemetry that does not match either of them, then the consumer has to just handle all the cases, which… which is difficult on the consumer side.
So that's… that's why I have a slight preference to always keep updating. This is not so much a problem on the consumer side, I think, And, like, the general community guidelines is also to use the latest semantic convention version.
I think, like, if we look across the other projects, we might be the one that's… the only project that's holding on to 138 at this point, which is, like, maybe a year or two old at this point.
Yeah, just wanna make my case for updating to the latest.
Nacho Bonafonte 00:37:40 Okay.
Marius Ciocanel 00:37:42 I don't think that's… I don't think updated to the latest was necessarily, like.
contested here. I think everyone wants that.
Yeah, that'd be, yeah, the first…
Nacho Bonafonte 00:37:53 is that someone had to take the role of updating the tools and the schema. Yeah, but then we need… If we are going that route.
We then must remove the, the types.
of the attributes. We must use just strings.
Because we cannot break the build.
Just because you update to a newer, minimum version.
Do you know what I mean?
You cannot release, I mean, or update and break a build.
Billy Billy 00:38:28 Yeah, so I think…
Nacho Bonafonte 00:38:29 something we should do. So…
Billy Billy 00:38:32 Yeah.
Nacho Bonafonte 00:38:33 If we want to always support the latest one, we need To remove the… the… the compiled check.
Ben Joseph 00:38:43 So, yeah, I understand…
Nacho Bonafonte 00:38:45 Another way of… Adding those values.
Not with the current.
Yeah.
Ben Joseph 00:38:53 I… I… Yeah, so, Okay, I think we are confusing schema changes with API changes. I understand API changes, like, if you're introducing a new API, if you're changing a class type, that definitely means that we should, it should not happen in a minor release. But these are schema changes. These do not show up on the client. Like, your SDK can integrate on the… inside the app without any breaking changes. These matter only for a consumer. Even if we generate these new semantic conventions from the latest version, these are internal classes, and no consumer is expect… consumer, as in a client consumer is not expected to handle these clients direct, classes directly that they generate… these are only meant for internal use within the SDK. So the string changes happen on the consumer side, right?
Billy Billy 00:39:45 It's also for the client side. Client side can be writing custom, like, attributes and telemetries based on the, the struct, because it's exported to whatever Swift runtime.
So, not just in the, like, whatever collector, like, that they're receiving, but, yeah, it can definitely break CI, if we just, bump the version in a minor release.
Ben Joseph 00:40:10 My concern is that, like, major release is too slow to be updating to the latest.
later semantic convention.
Billy Billy 00:40:18 Why is it slow?
Why can't we just do it.
Ben Joseph 00:40:21 How often… I mean, like, how often do we bump major release, major version?
Billy Billy 00:40:27 I mean, we don't release much at all. We can just do it. I think it's fine.
Ben Joseph 00:40:32 No, my concern is, like, if we decide semantic conventions are a breaking change, and it should only happen with major releases, then.
Billy Billy 00:40:40 Oh, I see what you mean.
Ben Joseph 00:40:41 Semini conventions come out every month or two, yeah.
Nacho Bonafonte 00:40:44 The thing is that currently they are a breaking change.
The way they are handled now, they are a breaking change.
Billy Billy 00:40:53 Yeah, and especially because we're bumping so many versions on this time, Yeah, ideally, just bumping the version shouldn't be a breaking change, but I think in this case, it's a little different, because we're bumping so many versions, and like Nacho said, there's a few bad cases.
I'm not afraid of just doing major version bump in this release, I think it's not a big deal, but… Yeah.
Nacho Bonafonte 00:41:19 Yeah, that… I mean, we can release more major versions, that's not a problem. We can do that. I mean, I'm not against doing major versions.
But… Yeah, we… but we cannot… do breaking changes on non-major versions, that's the point that I want.
Billy Billy 00:41:39 Fantastic.
Nacho Bonafonte 00:41:40 That's why I mentioned about the deprecation.
Ben Joseph 00:41:43 Understood.
Nacho Bonafonte 00:41:43 It's true that if we are… Yeah, if we say we are supporting some version, we shouldn't be adding all their attributes, or all their things in the semantic conventions that's not part of the new I speak. Yeah, that's… So, in order to support both things, we need to change how semantic conventions are now, but now I… Somehow they are nice because they are… compile check.
And they, they are, and they are nice to write. If not, we will probably have to You know, make… string… Binding or strings replacement, somehow, Or use another name, that's not what is in the attribute, and change that later.
Oof, I don't know, we could move to something like that.
Ben Joseph 00:42:41 Yeah, I think, we can… let's… let's do this breaking change for the 3.0 version, and then let's update… if there are no breaking changes, if there are no public API changes to…
Nacho Bonafonte 00:42:55 If they don't remove attributes, if all the changes they do are additive, that's okay, we can update as much as we want.
We will only have the problem if they remove something, but probably… I can imagine that if we remove something, and we keep it deprecated, and we still report that, we won't be the only platform reporting that old one, at least for a long time, right? You will still have clients in apps that are using the old version. You don't update all the apps of all your users.
Ben Joseph 00:43:28 But the SDK version there indicates that it's an old version, like, but the newer SDK version sending… that's where it gets complicated.
Nacho Bonafonte 00:43:37 So they can use the new version to know that the… that, yeah, that we are supporting the new one, but maybe… Yeah, that's… that's true. I don't know how to solve it, to be honest.
Ben Joseph 00:43:48 It's a, it's a…
Nacho Bonafonte 00:43:50 It's a nice problem.
Ben Joseph 00:43:52 Yeah, it is.
Nacho Bonafonte 00:43:53 Yeah.
Marius Ciocanel 00:43:55 But this… like, I'm just open semantic conventions, and I see that they're, like, string enums, which we're basically using the raw value for.
From, sorry. Yeah. So… If we declare…
Nacho Bonafonte 00:44:11 That's why I say that.
We should change everything. Do not use that, right?
Marius Ciocanel 00:44:17 I think it needs a nice… yes, I think it needs a nice developer experience to be able to kind of get autocomplete, and then…
Nacho Bonafonte 00:44:28 Yeah, it's a nice.
Marius Ciocanel 00:44:29 And if someone writes the code manually, and they get a deprecation, I would expect that they go, oh, it's deprecated, okay, what's replacing this? And they look, and, you know, we take the opportunity at every major version to kind of clean up the… the deprecated versions, but if… I think the point with this generate script being able to either delete the deprecated stuff completely, or just mark it as deprecated and leaving it, I mean, you kind of have to choose, like, but I guess, Ben, I see your point, you want people to be on the latest.
But then, you know, like, if you update something and then… I was like, I haven't changed anything, what, you know, I just bumped up a library. We made the… we break the SEM… version, semantic versioning of the library itself, so I don't.
Nacho Bonafonte 00:45:27 You update to a miner version because it fixes one of your bugs, and it stops building and reports something that, you know, that maybe your backend is not expecting, because it uses a new semantic convention.
For example.
Ben Joseph 00:45:41 If it breaks the bullet, I think that that is something we need to decide on a case-by-case basis, so…
Nacho Bonafonte 00:45:48 Yep.
Ben Joseph 00:45:48 Until that, I think we can go ahead and keep updating.
That's helpful.
Nacho Bonafonte 00:45:53 Okay, yeah, great.
Marius Ciocanel 00:45:55 So… I guess we're breaking three.
For now, just to get it to the latest, and then we'll… Decide later on what we do.
Nacho Bonafonte 00:46:06 Yep.
Marius Ciocanel 00:46:06 So, you know, how we handle things. Okay, cool.
Ben Joseph 00:46:09 Sounds good.
Nacho Bonafonte 00:46:13 Okay.
Billy Billy 00:46:23 Okay, yeah.
Marius Ciocanel 00:46:26 I'll actually mark it as draft, because it's not done, based on these conversations.
Nacho Bonafonte 00:46:32 Okay.
Marius Ciocanel 00:46:32 Can I mark it as draft, I guess?
Ben Joseph 00:46:34 I think that is safe to merge assets, right? Like, this is just.
Marius Ciocanel 00:46:37 Yeah, yeah, yeah, it is. It is, it's just… this is why I wanted to keep it separate a bit, just because…
Ben Joseph 00:46:44 Absolutely.
Marius Ciocanel 00:46:44 What's in here makes it easy to… to look at, whereas, like, if you change 80 files, because it is about 80 files when… when we moved… when we moved the… the versioning.
I've tried it, just out of curiosity, and it's… it was a lot, of changes.
Nacho Bonafonte 00:47:04 Yeah, definitely having two steps here is the… is the way to go. You know, like, we update the tools, and we… Later update, Samanth.
Marius Ciocanel 00:47:13 I mean, in that case, I guess.
But you can review this and have a look and… Yeah. The changes aren't… super… Longer.
And then I'll follow up with another PR, where we move to the latest.
Ben Joseph 00:47:33 Sounds good.
Nacho Bonafonte 00:47:36 Okay, so yeah, we are.
We are short on time. Maybe we cannot review much PRs, but I think all of them are here once, more or less. So, new topics, how to handle the deprecated attributes, that's the topic we talked, right? This is exactly these PR.
Marius Ciocanel 00:47:56 Okay.
Billy Billy 00:47:57 Yeah, I just have two quick topics. I created a new app launch instrumentation, after I was reviewing, like, all of the, like, implementation I wrote last year, and then Datadog, Sentry, Embrace, like, Honeycomb as well, I, I realized that, like, there's actually, like.
I think a pretty big gap in, like, monitoring, at least in these public SDKs, so… I was wondering what, like, the Apple engineers are doing internally, because I'm aware they also have, like, their own, observability SDKs, but… Specifically for, like, warm detection… detection of warm launches, so, like, that's when you start a new process, and you launch the app.
But the, app is not cached in memory still, like, A cold launch has almost none, but, And everything has to be paged in, and then a warm launch, everything's already there, so, there's, like, lower latency there. The other SDKs all, infer it based on, like, previous launch history.
But I realized that through, like, various, like, sys… system calls, like, you can actually calculate, like, the number of page-ins at various stages of, like, the app launch sequence. And I compared this against, like, the lab tool that, Apple provides. It's called, Instruments.
There's also, like, a command line tool called XC Trace. And it compared the, the data from, like, runtime versus, like, the lab tool, and it seems to be doing pretty good. But, Yeah, I was curious about, like, how, like, Apple wants… captures this, like, I don't know if Vladimir has, like.
I don't… I think… I don't know if the metric team, like, metric kit team is, like, you know, also doing the internal SDK for Apple monitoring.
But, yeah, so this is already, like, in the draft PR. I've only tested it on an iPhone 16 Pro Max, because that's the only device I have. I think Marius has, like, some other devices for some reason, so that'd be good if you could help me out there.
Another thing is I added, federated, semantic conventions here, and I added a W3C-like, schema for, like, breaking down the app launch sequence.
I try to, like, keep it, like, similar to, like, what, Instruments is doing, and also, like, base it on, like, the performance navigation timing schema that's, like, used in web.
Anyways, just take a look and tell me what you think. For now, I, like, figured out, like, a generic way to, like, count pagans before and after, the app launch, and then during the app launch, I figured out a way to sample, like, one segment of, like, the app binary, which is, like, the text segment that's, like.
typically where all the, like, the constant data is. I learned this all, like, very recently, so I really don't know what I'm talking about, like, but, like, for those that know, like, the differences between, like, text, image, sorry, text, data, and link edit.
I only sampled text at runtime via, like, the MinCore system tool, and that seems to be performing pretty well when compared head-to-head against, XC Trace. So anyways, please take a look and see what you think. I think it's, like.
pretty interesting what you can discover with AI compared to, like, what was written, like, 3 years ago or more.
So that's number one, and then the second thing is, yesterday, I met with the, the founders of the… and maintainers of our web also reached out to me and had a quick meeting with them.
They're also, like, interested in, like, you know, getting a session replay, like.
into web and, like, into the semantic conventions for OTEL. They don't have any presence in mobile, so maybe this is, like, the wrong space for it, but, like… They're also interested in, expanding to, like, mobile at some point, and they're, like, the number one open source framework that does this right now, like, that everyone depends on. I think all the other implementations are totally private, so… If anyone has any interest in, like, doing an open source, like, mobile session replays, particularly for iOS or Android, you know, and if you want to add that into ROWeb, which is, like, a good place for it, yeah, you can reach out to me, I can connect you to the founders there.
But I haven't done any work on that, that was just a discussion. So, yeah, those are the two quick points I wanted to add.
Any, any comments, or anything?
Vladimir Kukushkin 00:52:44 As you mentioned the name, I can chip in. So, obviously, neither I nor any other Apple engineer can comment how things are happening inside Apple. Okay, sure, even if we knew, even if we wish to share it.
But are you looking for some specific CIS calls, or are you looking… so, are you looking… How to identify specific syscalls, or are you looking what kind of cycles or other signals I need to look for to identify a warm startup.
Billy Billy 00:53:20 basically, like, I'd want to know, like, if this is the correct approach, because I'm pretty new to this, and I only have, you know.
AI to help me, and this is not very well documented either, like, I think you guys stopped, like, documenting things publicly, like, you know, some years ago.
Nacho Bonafonte 00:53:38 80s, probably, yeah, sorry, yes.
Billy Billy 00:53:40 In the 80s?
Yeah, I think there were some, docs, like, from 10 years ago that were out, but, there's just, like, the WWDC conference talks that I have to reference on, because, like, Metricit is obviously, like, not open source either, so I just want to know if this is, like, the correct approach, and if this is, like, useful, because the only indicator I have right now is, like.
just, like, reading about stuff and comparing the data against, like, XC Trace. So, like, do you think… like, what do you think about this latency breakdown and, like, the different, like, ways of measuring, pagans,
Vladimir Kukushkin 00:54:18 Yeah, so I don't know the answer, but if we want to find an answer, could you please file a feedback?
Okay. Through the feedback assistant. I see. Basically, asking how you would ask an Adapt MDC lab, hey, is this the right approach? Is this expected to work? Is this a reasonable way to do things?
Maybe link that last .dc, where things have been mentioned, maybe linked this, proof of concept PR, draft PR, And send me the feedback.
in a CNCS cycle next time we meet here.
I can try to find Roland people to answer it.
Billy Billy 00:55:03 Okay, that'd be amazing. Where do I cut that ticket?
Vladimir Kukushkin 00:55:07 So the Feedback Assistant, it's available either on the web, or if you happen to have a beta version of Either of us, basically, it's there.
Billy Billy 00:55:20 Oh, like, on support to Apple.com.
That, that one.
Vladimir Kukushkin 00:55:24 Okay.
Nacho Bonafonte 00:55:24 Yeah, it's a search for it.
Billy Billy 00:55:27 Okay.
Oh, you know, could an internal ticket, not like a GitHub ticket, that thing? Okay.
Okay, I can look into this.
Vladimir Kukushkin 00:55:35 Yes, this, yes, Liz, yes, please.
Billy Billy 00:55:39 I'll reach out to you. Thank you. And then, another quick question, do you know if the active pre-worm flag is still, like, being used?
Vladimir Kukushkin 00:55:49 I don't know. I'm unfortunately from that part of Apple who's not… who's working.
Billy Billy 00:55:53 Okay.
Vladimir Kukushkin 00:55:55 Yeah.
Billy Billy 00:55:57 Yeah, because somebody stumbled upon it years ago and posted it, and everybody copied it, but I have no idea. There's no way to reproduce Freeworm either, so…
Vladimir Kukushkin 00:56:05 That's… that's exactly a good question to ask.
Billy Billy 00:56:09 Okay, cool.
Vladimir Kukushkin 00:56:10 Damn.
Billy Billy 00:56:10 Yeah, those are my only two questions. Thanks so much for letting me.
Nacho Bonafonte 00:56:13 I think I remember that parameter was… outdated already. I mean, that… that doesn't do anything more now.
Billy Billy 00:56:20 Okay, that's okay.
Nacho Bonafonte 00:56:21 To remember, but yeah, might, might be wrong.
Billy Billy 00:56:27 Okay, I'll ask them. Thanks, those are all my questions.
Ben Joseph 00:56:37 And Billy, on the RR web, I'm definitely interested in, seeing how, how we can, you know, support mobile, If, if, yeah, if maybe we can discuss.
Separate.
Billy Billy 00:56:53 Yeah, sure, you have my Slack, and…
Ben Joseph 00:56:56 Yep.
Billy Billy 00:56:56 Oh, you can do my email or anything, or phone number or something, just let me know, yeah.
Ben Joseph 00:57:00 Yep.
Billy Billy 00:57:03 Okay, thanks guys, see you next week.
Nacho Bonafonte 00:57:07 Yeah, last topic here was already the…
Ben Joseph 00:57:12 Yeah, I…
Nacho Bonafonte 00:57:13 we marked.
Ben Joseph 00:57:14 I had added it. I understand, like, there is Swift-specific docs, but the example it gives is for Swift Server, so I was thinking this might be a good opportunity to have, like, iOS-specific docs, if you open that link, that's… the examples in there are for Swift Server. So since we… OpenTelemetry has a page for iOS, I was thinking we could… we could do that.
I'm not sure how to, like.
Should we just, open a PR to this, repo? But,
Nacho Bonafonte 00:57:53 Yes, that's handled in the repo, or the documentation repo, yes. When we created this, yeah, it was our PR there.
With the changes. Yeah, we have this documentation.
That's only for, yeah, for the language itself, but… the… Oh, sorry.
Marius Ciocanel 00:58:14 I can… I can have a look at… doing some, like, having a plan for this, it just… I got contacted by, one of the people from that chain.
to contribute to the Romanian localization. And… yeah, like, I think they were offering to… to help me, like, if I want to do that, and, like, if it's documentation, it's on the same… it's on the same page, so I could do both English and… Romanian. I'll ask for feedback first, from everyone.
And even if it's just a basic, like, just… Couple of steps, I think it still helps. What's in iOS at the moment?
Ben Joseph 00:59:00 Ios is empty.
Marius Ciocanel 00:59:02 Oh, right, okay, so anything is better than nothing, okay.
Nacho Bonafonte 00:59:05 I mean, we have the sweet thing that… that talks about how to install, basically, mainly on iOS also.
and the instrumentation, and I think most of that information is already here.
But, yeah, maybe… Focusing more on the user.
perspective, I don't know. But yeah, I think most of it I think we documented it as if it was for a clean user when we did.
Ben Joseph 00:59:39 Yeah, definitely, it's clear, but, like, it is a little bit more wide, and it's not talking about iOS-specific use cases, I think. Definitely for iOS, we have to implement it slightly differently.
You know, so that aspect can definitely help. I think the issue came from some user who was trying to find I.O. specific documentation, and they couldn't. It was only Swift.
Even, even looking at these, examples, right? Like, I feel like, if, if I were to implement or integrate, this SDK into an iOS app, I would definitely… I could definitely use a iOS-specific example here, so I think it definitely adds value.
Nacho Bonafonte 01:00:26 Yeah, but probably it's also as outdated as the rhythmia, right? So probably having something about the session instrumentation and things like that will be really useful, and probably that's what Yeah, what the platform documentation should specify more.
Ben Joseph 01:00:46 Marius, if you're opening up PR, I think, like, you can open a PR to that repo, and then… Add, the people in this call to the reviewers.
Marius Ciocanel 01:00:55 Yeah, yeah, just for feedback, yeah. For review. Yeah, I'll have a look, see if I get a chance to do that before next week. Yeah, okay.
Ben Joseph 01:01:05 Yeah, thank you.
Marius Ciocanel 01:01:07 Cool.
Nacho Bonafonte 01:01:08 Okay, then, those are all the topics. We didn't review the issues or the new PRs today.
But yeah, we are on time.
Thanks a lot.
For joining the call, and for all the, all the feedback.
Marius Ciocanel 01:01:27 Thanks, everyone. See you next week.
Vladimir Kukushkin 01:01:29 Am I?
Nacho Bonafonte 01:01:30 weekend.
Marius Ciocanel 01:01:31 Take care, have a nice weekend.
