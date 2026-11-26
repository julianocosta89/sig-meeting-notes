SIG: Go Compile Time Instrumentation SIG
Date: 2026-11-26
Duration: 83 minutes
============================================================

## Zoom Recording Transcript

**Kemal Akkoyun** 04:43 Hello, hello.
**Huxing Zhang** 04:46 Hi.
**Kemal Akkoyun** 04:49 Ed.
Okay, I think bunch of people in… is in another meeting.
**Huxing Zhang** 05:08 Yeah, I was, going in a different meeting, but I think last week… last time we are in this meeting.
I'm on…
**Kemal Akkoyun** 05:17 I think it's the calendar one, right? Yes.
**Huxing Zhang** 05:20 Yeah.
**Kemal Akkoyun** 05:28 I meet, like, All of this is different.
I thought he replaced that one, too.
I really don't understand.
It is the correct one.
Interesting.
Arvin, the… I mean, the same different one?
**Dario Castañé** 06:19 I don't know, but apparently.
**Kemal Akkoyun** 06:22 I mean…
**Dario Castañé** 06:22 And another one?
**Kemal Akkoyun** 06:24 I'm always using the calendar link, and then, like, use the Zoom one.
And that is the one in the document.
I just, like, copied that from the calendar, like… All this thing happened.
**Dario Castañé** 06:44 Oh, whoa.
That's weird.
**Kemal Akkoyun** 06:47 Yes.
**Huxing Zhang** 06:48 I think, there's… once upon the Azhar… OTL has migrated the meeting from, like, Linux, the, like, from… I don't know how to say it, just the…
**Kemal Akkoyun** 07:04 Yeah, it's the LFX platform, yes, and calendars are auto-upgraded to that.
And that's why the calendar is source of truth.
But, yeah, don't know why it's sad.
**Dario Castañé** 07:16 So… Let's do one thing. Let's remove the old one in the dock, keep the one that you pasted.
**Kemal Akkoyun** 07:23 But it's the same! Soft hop.
**Dario Castañé** 07:25 I know, it's usually the same, but maybe there is some difference, because, I mean, it's like an HTML page. You have the text, and then the link.
**Kemal Akkoyun** 07:35 That's true, that's true.
**Dario Castañé** 07:37 I'm going to just remove the format, and… Okay.
Cool. No, it didn't work.
So, yeah, let's go ahead with the meeting done. I will fix this.
**Kemal Akkoyun** 07:47 Yeah.
I will need Azhar for, like, these topics.
Let me pink him.
Okay, so… Today's meeting, or it's, I pinged him, let's see if he's going to turn up.
Okay, he said he's in the meeting right now.
Okay, Okay, is he here? Like, Azhar, are you here? No, you are not here.
**Huxing Zhang** 08:51 Is he in another meeting?
**Kemal Akkoyun** 08:55 Yeah, he's in the wrong one as well.
Oh, he said he joined the 1A poll, like, what's going on? Like…
**Huxing Zhang** 09:01 Yeah, I think we should ping him.
**Kemal Akkoyun** 09:03 So we are not… so… we are not in the one, in, like, in the link, like… Oh.
Okay, let me click this link.
I mean, it doesn't do anything for me, it says that we are in the correct meeting.
Okay.
Well… are… So confused now.
How come all of us ended up in this meeting then?
Yes.
**Dario Castañé** 10:27 The difference is… is just using the calendar or not.
That's different, because I actually used your link in Swag.
I landed on the same meeting as Azhar, and then I came back to this one through the calendar.
**Kemal Akkoyun** 10:42 Okay, then, as you suggested, like.
Something in the… something wrong with the calendar link.
**Dario Castañé** 10:51 Let me check Bonsai… Okay, gotcha.
So, the thing is that the calendar is the one that has, like, an HTML thing, you know, you have the text.
tags, and then you have the href value. That's the one, the calendar is showing a visual representation of the link that doesn't match the href value under it.
**Huxing Zhang** 11:20 Yeah, that's… I agree.
**Dario Castañé** 11:22 Change that.
**Kemal Akkoyun** 11:24 Can you fix that?
**Dario Castañé** 11:25 Yeah.
**Kemal Akkoyun** 11:26 You have the permission.
**Dario Castañé** 11:27 no, no, I don't have that kind of permission, apparently. I'm going to just change the link in the docs.
**Kemal Akkoyun** 11:36 No, no, let's, like, this could create, like.
But we need to make sure that the platform is correct, right? Because at some point, Linux Foundation gonna tear down the old links, probably.
**Dario Castañé** 11:50 But anyway, If somebody happens to join through the dock, they're landing on the old one, not the one in the calendar. So, we cannot change the calendar.
But we can change the doc, so at least we know both.
**Kemal Akkoyun** 12:03 I didn't… I will try to… I will try to change the calendar, I might have, like, permissions to do that.
**Dario Castañé** 12:13 Okay, let me try the link. I just pasted, just… I'll be good.
**Kemal Akkoyun** 12:18 I saw what you mean, okay, okay.
Okay. Attend I opened the page of one.
**Dario Castañé** 12:33 Definitely, that was the issue. So, and it's what, we were talking about, that they migrated from the Zoom LFX platform, yada yada, to just an account that is zoom.us, like the plain one.
**Kemal Akkoyun** 12:52 Okay.
Let's… I will try to find… figure it out how to fix this calendar thing. I am taking an action item for myself. Azhar, you can, like, take it over.
Or, for your topics?
**Azhar Momin** 13:11 Hello, everyone.
Oh… Let's see if I can enter it.
Alright, so I wanted to discuss about the upcoming release. We have Almost, completed our, release milestone for the release.
And… We also completed our, Contribu split. We have moved our instrumentations to the To the new repo, called… Open Telemetry Compile ConTrid.
Meaning that, also.
Yeah, so, all our instrumentations, we can, release the instrumentations directly from, the other repo, and we don't have to, update our tool every time, and we can keep the core compiler, OTLC within our main repo, so… Whenever we have a fix related to the instrumentation, we can push the release directly from the control group, and we don't have to wait for those releases, on the tool. We don't have to delay those releases because of the tool.
This would also allow us to, push releases faster, on the conflict side. And we also had this problematic, thing, the OTLC bundle.
Which was delaying, the pull request, so every time we had a pull request, it would always conflict on the bundle, because it was a binary, bundle of the instrumentations shipped with the tool.
I want to discuss about, how should we, do the releases, in one February posture. We started from V, 0.
So, for example, we can do V0.1 initially.
Or should we follow the same release as tool? We can start from?
V1.3 for it as well.
Cool.
**Kemal Akkoyun** 15:50 Okay.
just… I see some new faces in the meeting, so I will just… summarize, the previous work. So Azhar is, joined us for LFX, and his project was about introducing a registry to split the… tool from the country repos and the Instrumentations, because it was getting hard for us to maintain everything, and we would… we don't want to be in the business of maintaining all the integrations, so that's why we created the country repo.
which have, like, less barrier of entry. If anyone wants to, like, come and, like, add an integration and be a code owner for that integration, we will assign those code owners to those, like, people that would like to, maintain that. We haven't done the code owner work yet, but we will. For example, someone from the community wants to add, Qi support, they mentioned. Probably in that PR, we should just push for, like, do you want to, like, own this component, right? So, the contract people will be all about Adding instrumentations and integrations.
One advantage we gain from this is we, like, untangled the release cycle of the tool and the contra people, as Azhar mentioned. How do we do that?
There is another component in the Open Telemetry ecosystem called Open Telemetry Explorer, and Explorer has an API, and it scrapes the construct repo, check for all these OTLC YAML files, and generates a manifest, and our core OTLC binary reads that registry through the Open Telemetry Explorer, right?
Correct me if I'm wrong, anywhere in Azhar.
So with this way, we will be able to, like, release faster with the country people, with the security fixes, whatnot, and any, like, OTLC will pick it up.
I guess, like, The only problem will happen When we… change the minimally supported Go versions, or when we try to upgrade them, because now quantum repo and the tool repo needs to be in sync for that.
Yes, and we… yeah, we already committed to just, like, with each release, we were just gonna, like, push through the latest two supported version, so this is how are we going to iterate.
So for that, Azhar's point, how are we going to do the releases for country people?
I think this should be automated?
Right? Yes, yes,
**Azhar Momin** 18:36 I was working on that PR, we can use, OpenTelemetry already has multi-mode for that, so it automates almost most of the work for us, so we just have to update a versions.tml file, and it will then automatically create the release.
I was,
**Kemal Akkoyun** 18:53 almost sort of.
**Azhar Momin** 18:53 we start from V0 for contrab, or should we continue, the, V1.3, same as 2?
**Kemal Akkoyun** 19:02 we should start from V1. Like, we already give guarantees for the integrations. I don't… like, that's my opinion. I would like to hear others' opinion as well. Like, we already called ourselves V1 for the tool.
I don't know why I think we should do the same for the integrations as well.
Like, like, in an ideal world, I guess.
each integration should have a version, and depending on the maturity, the owners can decide whether it's a V1, or P0 or a V2, right?
But I think at this point, it's really hard to… Like, support this?
But, like… We can try.
That means submodules in Go, and submodules in Go is… just gives me creeps, so I don't know.
**Azhar Momin** 19:54 Sorry, I was… I didn't… I can go repeat what you meant.
**Kemal Akkoyun** 19:59 So, like, we can, in GoMode files for each module, we do this for DDTrace Go, for example, you can maintain different versions of all these integrations, right?
So, instead of, like, tagging the whole country repo, each integration can have its own version.
I think that's the best way to do that.
I don't know… we might have some tooling for this in Open Telemetry?
Right?
**Azhar Momin** 20:27 Right now, multimore can do that, actually. We can have these sets for it, and we can have a list of modules in that release set.
So we can also have a single release set for each module, so every integration will have its own version. We can do that.
**Kemal Akkoyun** 20:44 And… and each integration is a Go module with properly tagged version, and pushed to the proxy, or pulled by the proxy, okay? Then let's do that.
**Azhar Momin** 20:55 Okay.
**Kemal Akkoyun** 20:59 When it comes to deciding whether V1 or V1 or V0, again, I think it's per integration basis, supposed to be per integration basis.
we can… Yeah, again, like, if we trust that integration is, like, mature enough, we can go with V1. If it's not, or it's not contributed by us, maybe we can go with V0, and after assigning cod owners, they can decide.
**Azhar Momin** 21:31 I wanted to have a checklist first, on all the… on all our instrumentations, and I wanted to check if we, comply with the upstream semantic conventions correctly, and if we have all the attributes before V1. That's why I wanted to start from V0.
**Kemal Akkoyun** 21:47 Sounds great.
**Azhar Momin** 21:48 Some might be wrong. That's one.
I can create an issue for that to track, and then we can also have a README. So, for example, we don't have a metric SUNL in a lot of instrumentations. Most of our instrumentations are only traces.
So we can also add metrics to them, and then once we also have metrics and places in all of them, then we can, push them to E1.
So, we can start the year and then push them to even.
**Kemal Akkoyun** 22:20 Sounds good.
I don't know if it's necessary to py that, okay, this thing supports all the signals, then it's V1. I'm not sure of that.
But I like the checklist idea, if we can even, like, make it as part of CI, whatnot, or, like, having… I think, eventually, we had decided… We have a website, right?
about, like.
it discovers the registry, I don't know, we can check, like, what we have in the Explorer website. Maybe we can… Expose this information in that… There was a registry that opened?
**Azhar Momin** 23:02 That part is still pending, that part of it is still pending, though we don't… we currently hardcore the manifest in OTLC.
So, we don't have that registry in Ecosystem Explorer yet.
**Kemal Akkoyun** 23:15 Okay.
**Azhar Momin** 23:18 That's my next book.
After this.
**Kemal Akkoyun** 23:23 I meant this website, this is… I know this is different, but, like, when… if I say that, like, I write here Redis.
Oh, yeah, we already see that. Oh, maybe I should share my screen.
So we already see that, like, Open Telemetry or Compile Time, Auto Instrumentation, Redis V, Mine is here, there's also Go Redis Instrumentation, which is from the con trip.
I believe, and then, like, in this one.
If I click that… okay, it opens… yeah, file not found. And first of all, I think this is not good.
They didn't update the registry, and it's pointing the old thing. We should… we should fix that immediately.
And in, in here…
**Azhar Momin** 24:10 I've frozen the… frozen this registry, so they are moving to the new Ecosystem Explorer. This is the old one.
**Kemal Akkoyun** 24:17 Come on.
**Azhar Momin** 24:17 wasn't…
**Kemal Akkoyun** 24:18 And you should read the… read this command, okay.
This is the… Now, this is the new registry.
Isn't it the same?
**Azhar Momin** 24:34 In a sink, maybe.
No? Yeah, it's… I think it's ecosystem.opentelemetry.io.
**Kemal Akkoyun** 24:54 And did I do the typo?
**Azhar Momin** 24:56 Maybe, maybe Explorer.
Explorer.opentelemetry.io, so either one of those.
Okay. Yeah, this one.
**Kemal Akkoyun** 25:06 It looks fancier.
**Azhar Momin** 25:09 Yeah.
**Kemal Akkoyun** 25:09 But it's Java agent, open Telemetry, semantic corner, which is okay, where are the instrumentations?
They need to migrate.
**Azhar Momin** 25:18 Yeah, they need to be added to this file.
I can, start working on those now.
**Kemal Akkoyun** 25:27 Okay.
All right, oh, there's the… all right. Probably, yes, if it's the… if collector components has this Telemetry Signal section, it should be same for our instrumentation.
And yeah, there is a stability. I think we should use these conventions within the country people, or wherever we put that, it should just render for this one, right? So, in your… as you said, like, or V… if it's, like.
if we consider that it's better, like, V0 is, better, like, we can just use that one.
And the V1 stable ones can be stable.
I don't know how this distribution thing… it won't probably work for us. I have to check the Hotel Explorer and how these things work, to be honest.
But we should… this should be our documentation, or, like, how to discover our integrations. This should be the… way, then, if registries are not another thing anymore.
Anyone else?
**Azhar Momin** 26:37 This can also be… this would also be useful, for our, decorative conflict work. Aditya's working on that, but he's not in meeting right now, but… Those config options can be shown directly in the Ecosystem Explorer, so it would be very nice for people. They can simply generate the config directly from this tool.
**Kemal Akkoyun** 27:00 Yes.
I think so, too.
But I think we had… we also had… Where was it?
In the country, people.
Alright.
Okay, it's Compile time.
we used to have README files in certain Okay, do you hear Immortals.
I think we should at least also have some.
**Azhar Momin** 27:31 Yes, I think we're.
**Kemal Akkoyun** 27:32 closed this now.
Okay.
Maybe for these README files, we should also have a, like, convention to show, like, which signals are supported.
And which configs are supported as well?
And then, like… Yeah, these… that README section should be also gen… can be also generated.
especially for the config parts, right? If we change something in the source code.
For a config, maybe there needs to be a step that, like, generates a section.
For the README. I am… I am not following the config LFX project, to be honest. I don't know if this is within the scope or not.
**Azhar Momin** 28:19 I don't, I'm not, I think they're still pending that part.
But, yeah, we can definitely have that.
**Kemal Akkoyun** 28:29 Okay, so let's… let's take some action items here, so… you will… you can create an issue for this as well, like, I'm just gonna assign this to you, but you can create an issue in the country people, and we can check, right?
as, there will be someone maybe would like to tackle this one. So, we will make sure that… Explorer… is supported.
Right? This is one thing that we would like to do.
And the other one… We want to have… generated.
Indeed, miss.
It's configuration, and supported.
signals… Any other ideas?
He also said that you are exploring the… multi… Multimodule, versioning.
**Azhar Momin** 29:34 Yes.
**Kemal Akkoyun** 29:35 Right?
Okay.
**Azhar Momin** 29:37 Yes.
**Kemal Akkoyun** 29:38 What else?
Did we miss anything?
**Azhar Momin** 29:43 Now, if we can move… slowly move to the next topic?
I wanted to, discuss about the integration tests.
**Kemal Akkoyun** 29:54 Yes.
I actually have a subtopic of that.
the last thing… so… Yeah, you start. I have a lot of ideas, because I'm also, like, dealing with this on our side.
**Azhar Momin** 30:09 I was thinking that we could maybe group the integration tests to the instrumentations they belong. So, on pull requests, they only run on the integration, they only run the integration tests related to those instrumentations, or… A2A tests related to those instrumentations, so that would speed up our CI, I think, a lot.
Okay.
**Kemal Akkoyun** 30:33 So… My suggestion, you should check DD Trace Go and what we do, now. I will be, for example, pushing some updates, today, so… so the gist of it, now we are trying to migrate from Orchestrian to OTLC for DD Trace Go, and we run all these integration tests.
And we are facing a lot of issues, like… And we try to optimize them as well, how we run the tests, whatnot, and the same problems valid for the country repo as well, right? Since we are still experimenting, and we didn't find, like, the perfect way to run everything, I haven't, like, upstreamed these things yet, but you can have a look.
One of the things that Rodrigo, like, for example, found out yesterday, and this made significant improvements.
basically, this is something we have in our question already, whether to check, like, to run the, like, to check… try to manipulate the AST for that file or package at all, so this is… brings that out, and This actually, like, gave us, in some places, 10x improvements while running the integration tests.
I don't know when is the last time you checked the integration test. Maybe the integration test that runs today, because this just merged, like, yesterday, could be significantly faster.
And I think we have… yeah.
**Azhar Momin** 32:02 Yeah, but, we also have to update the OTLC in Contrib Repo for that, because if this is a new commit, the OTLC in Contrib Repo might be pinned to an older, commit of OTLC.
**Kemal Akkoyun** 32:15 Yes, this is another topic. I think one of the things, like, this… So, we are trying to automate dependency upgrades, for country people and OTLC, and we will have a cool-down period. That means Dependabot and the Renovate gonna have, like.
It will be merging a lot of, dependency upgrades in the modules, so… and then OTLC will be moving the tool part, and for the integration test and for this repo, we should decide how are we going to release, right? The automated release, and it ties to your multimodal versioning.
like… Shall we automate that? Let's say, like, every two weeks, release something for the contrips, every week, release something for the contrips, pull all these, like, sub-components, and create that file that you are mentioning, and take an automated release from Contrip? Do we want to do that? Like, we should decide.
And the same goes for Hotel Sea, for example. Like, this is merged.
And, like… on the PRs, at least, we should always run the OTLC from main, and also the latest stable, right?
So whatever, like, we should all know beforehand, before releasing anything for the contributions, that we break something for… for disintegration or that integration. So this should also, like, break the auto-releases of any contribos, right?
So that, like, whenever we cut the OTLC major one.
Yeah, so on and so forth. So that should be our strategy.
But still, I would like to hear from other people's opinion in the meeting. We have a lot of people, but it's like you and I having a one-on-one, but these are all ideas, so… I know, like, Romain is in the meeting, Dario is in the meeting, and if you have any ideas, because we have the… all of this experience with the orchestrian, and, like, let me know if I'm missing anything.
Morning once.
Only twice?
Nope. Okay.
Seems like they are all good.
Okay, that's it, I guess, right? Do we miss anything about that? We've, like, I, I, like… But, again, the running the contribution test, there's two problems with that. One is how we actually run the tests on the CI, and how we utilize the caching layer, right? We had some problems with how we generate the instrumentation JSON file, and then it was, like, not sorted, not stable, and we already merged that fixes, and that was creating a lot of, like, cache trashes on the CI, around the build cache. Those should be fixed, and I will… we can check if we missed anything from, like, DD Trace Go setup on the CI that we could have in the oral country repo, I can take that action, to be honest.
on running the integration test, that's… one thing, right?
stream the… Integration.
Pest.
Runner's tool.
Excellent.
Okay, right. So the second part, this is the first part that we need to improve. The second part, there are a lot of small things that we can improve in HotelC that could, like, make sure that the compile times are faster, right? And this is on our roadmap.
after we're, like, migrating all our integrations, we will be bashing on these improvements. And already we see this, and, like, Rodrigue already contributed that.
So, we will do that, alright?
Ugh.
And, yeah, Azhar, you have your actions, I have my actions. Please create issues for that, and, like, you don't need to do the whole work. We have other people who would like to support, and we can create issues and share that in the channel.
That we can help. So… okay.
Anything else on the topic?
**Azhar Momin** 37:09 Nope.
**Kemal Akkoyun** 37:13 Okay, about Busin, you have a topic, update with the hotel in Japan.
**Huxing Zhang** 37:17 I created…
**Kemal Akkoyun** 37:18 the.
**Huxing Zhang** 37:19 Yeah, sorry,
**Kemal Akkoyun** 37:21 Please go ahead. No, you will give that.
**Huxing Zhang** 37:23 I just, I want… wanted to know the update. I saw that you have a conversation with the auto-injector SIG, and, what are we gonna do, any collaborations with them, yeah.
**Kemal Akkoyun** 37:41 Right now, the injector SIG is working on adding all these auto-instrumentation components, for the distribution part, which means, like, if you are using a package manager on Debbie and Ubuntu, and you have… they already, like, publish these packages on Open Telemetry.
auto Instrumentation part.
And they are, like, working with the injector part, and I guess one of the things that we can do, make sure they use Autel C4 as, like, default Go Compiler, maybe, and everything auto-instrumented, that's one of the ideas. So we will discuss this, they're supposed to have a SIG meeting today, and I plan to attend that, but because of the US Thanksgiving holidays, they canceled that meeting, so I will try to attend the next one, which is next Thursday.
In US morning. The, the, like, you can see the Slack channel thread on the hotel injector, SIG channel.
And after the meeting, I will update.
Slack, on our Slack, I will let you know. I think this would be super hard for you to join, because of the time difference between, but if anyone else wants to join, you can check the Open Telemetry calendar and find the injector SIG, it's… We will try to do this next week.
**Huxing Zhang** 39:10 Oh, okay, good. I think I'm not able to join that because of the time zone issue, so… I will, comment if, any ideas I want to address.
**Kemal Akkoyun** 39:24 Okay.
**Huxing Zhang** 39:25 I know.
**Kemal Akkoyun** 39:25 I will keep you in the loop.
**Huxing Zhang** 39:27 You can't have a problem, you have to go.
**Kemal Akkoyun** 39:29 Okay, and I have this, I'm trying to find your repo.
**Huxing Zhang** 39:35 I have another article. Yeah.
**Kemal Akkoyun** 39:37 Oh, it's just, okay, I need my…
**Huxing Zhang** 39:40 Hold on.
**Kemal Akkoyun** 39:41 Let's do it auto… I think this should give me the… yeah. Is it pilot now?
**Huxing Zhang** 39:46 Or elocin, go. Go, go, go.
Both companies.
**Kemal Akkoyun** 39:49 Okay.
I remember there was an issue in here about, like, migration.
I'm looking for that, I haven't checked.
Oh, yeah.
Yes.
Do you have any update on this? Are you planning to do this? Is this in the works? That was my question, because we are doing this for orchestrian work.
I was wondering, have you ever attended to… Start the migration.
**Huxing Zhang** 40:17 Yeah, we're actually planning, planning to do that, but right now I, have some, another tasks for, Hai Bin, and he's quite busy, so I'm gonna, talk about this enough.
A few weeks, and we want to, like, to have some… comments, like, roadmap and speed into subtasks, and then we will… I think we definitely should move it forward.
In this couple of months, I think, yeah.
**Kemal Akkoyun** 40:57 Okay.
**Huxing Zhang** 40:57 Oh, Rhino.
**Kemal Akkoyun** 40:58 Do you… do you plan to, like, move all these integrations to the upstream, or, like, or maybe you haven't already, like, talked about it, I just wanna… I wonder, like, do you plan to move these, or, yeah, keep them here?
**Huxing Zhang** 41:15 Yeah, I think we, we, we should, contribute that, most of them, but I… I don't know if there's… or all of them, should be accepted by the, upstream. So, with that, we will keep some of them, maybe, which are not suitable for, like, upstreams. We will keep them.
And we, we won't actually put that, to the… Registry, or I think…
**Kemal Akkoyun** 41:45 as much.
**Huxing Zhang** 41:45 as possible, yes, from my side, yeah.
**Kemal Akkoyun** 41:48 Yeah, let's discuss that part. I think, like, if Open Telemetry governance accepts that… accept the long-suit Alibaba repo as a, like, a source of registry of integrations, I think Everything should… can stay here.
**Huxing Zhang** 42:05 But, you know.
**Kemal Akkoyun** 42:06 if there's a, like, I don't know, an issue with that, then we can decide to move everything to the country repo, and Alibaba can be co-owners of those integrations, which is, like, should be fine with the SIG leadership, I guess.
**Huxing Zhang** 42:22 How about…
**Kemal Akkoyun** 42:22 I don't…
**Huxing Zhang** 42:24 Did the Austrian project? How, how do you plan to do that? Your… your… Yeah, we are Instrumentation.
**Kemal Akkoyun** 42:31 Mr.
So, for our instrumentation, since we are not using Open Telemetry SDK, Right? It's a totally different SDK.
**Huxing Zhang** 42:40 Goodbye.
**Kemal Akkoyun** 42:40 It's… it doesn't make sense for us to, like.
use the DD Tracecore repo as a registry, but what we plan to do is, if we have a missing registry.
a missing integration, that it's not in the country repo, and somehow we implemented that for DD Tracecore, it should be easy to port those codes for… make it for Open Telemetry SDK, and which we will do.
So, yeah, you… the long-suit integration is already, like, Open Telemetry native, so it is… somewhat different than the DG Trace Gold story. You are, like.
It's really low-hanging fruit for you to upstream these.
**Huxing Zhang** 43:27 I got, I got it, okay. I will check that with having, and we'll work out a proposal or plan of how we're gonna do that.
**Kemal Akkoyun** 43:40 Okay, awesome.
Yeah, I'm mostly asking that for, like, we need to make sure that OTLC works perfectly, and I guess Alibaba and Datadog, they are the only production power users at this point, so if we can, yeah, start testing our tool more and more.
I would love to discover any edge cases that we have.
**Huxing Zhang** 44:03 Alright.
**Kemal Akkoyun** 44:05 Awesome.
Do we have any… Other agenda items.
Any last-minute additions?
Okay.
**Azhar Momin** 44:25 I wanted to discuss about the release cadence. I was thinking that, now that the instrumentations are more to counter the repo, we can have Maybe 4-week cadence for the contract repo, and for OTLC, we can have longer cadence, maybe 6 weeks or 2 months, so… We can do patch releases if there are… there are any critical bugs, but for major releases, we can… or minor releases, we can do them in 6 weeks or 2 months.
**Kemal Akkoyun** 44:55 I even, like, at this point, to be honest, if… we can commit to the 6-week cadence for the tool, core repo, but then if we don't have anything to update, because as at some point, I assume that we will, Achieve some sort of maturity, or the core tool itself, the injector part.
we don't even need to release that, right? So, I would say, like, let's say 6 weeks, but that 6-week thing should check, okay, is anything changed? Like, is there any, like, security fixes that I need to, like, sync? Whatever?
then it should, like, we should release. If we don't have anything, we should just skip.
But for Contrip, I'm sure, like, there are lots… there will be lots of things, security fixes, dependency upgrades, whatnot, we should even try to release every two weeks, yes.
That's my… my two cents on that.
**Xabier Martínez** 45:59 Yeah, I agree with that. Maybe we can… Document them in each report.
**Kemal Akkoyun** 46:05 Yes.
**Xabier Martínez** 46:05 The release flow will be different, so if we want to change, maybe in the future, again, we just change the document, but it's clear that How to proceed in each of, the reports.
**Kemal Akkoyun** 46:22 Okay, I'm taking some notes.
**Azhar Momin** 46:24 Right now, it's, actually needed for tool as well, because Currently, we hard-code the manifesting tool, but once we complete the registry integration with Ecosystem Explorer, so it can… it can dynamically fetch the release from config repo, then we can follow this.
cadence.
**Kemal Akkoyun** 46:45 Okay.
When do you think we can handle the Explorer support?
**Azhar Momin** 46:57 We need to, first complete, the registry support, and then we can Follow that up with the Explorer support.
**Kemal Akkoyun** 47:08 Okay, do you have issues for this already?
**Azhar Momin** 47:11 Yeah, they are already open. I already have some PRs as well, one PR on Explorer's side. I'll try to push them, next week.
**Kemal Akkoyun** 47:22 Okay.
Fine by me. But we will release 1.3 today, right? That was the plan.
**Azhar Momin** 47:29 Yes.
Yes.
**Kemal Akkoyun** 47:31 And this… this will still have the… embedded manifest file that pulls things from Alton Telemetry.
Awesome.
Yep.
Alright, we have another topic, the Maintainer Summit.
Roshin, do you want to talk about it?
I think he's… he… cousin?
**Huxing Zhang** 48:11 I, sorry, I just, I have a last-minute topic, so I just saw the email, and the maintainer summit of Group Count Europe.
Next year, and they are still calling for.
Proposals, and we'll be closing soon.
I think there's some interesting, like… session categories, like, how do we, grow in, like… project, like, undergoing the… contributors… how do we… maybe there's also a project meeting, I saw there. Yeah, I think.
**Kemal Akkoyun** 48:56 I was gonna say that, let's submit for a project meeting. It says that there won't be any, like, passes for that, but, like, I know, like, I will be there, Dario will be there, because this is practically his hometown, and Xabier maybe join…
**Xabier Martínez** 49:14 I'm planning to go, not sure, but I will try.
**Kemal Akkoyun** 49:19 Yeah, let's… let's at least have a project meeting submitted, and we can meet and talk in person for this one. I think we will have enough people in Barcelona, And yeah, that would be nice. And if… Anyone needs a ticket.
maybe they can sub something for the Maintainer Summit? And yeah, probably… And maybe Azhar, if you want to join us in KubeCon.
If you got a talk accepted.
You can even ask from CNCF to help, to, like, there's a scholarship, so they can pay everything for a maintainer.
So that would be ideal for… to have you, if you have time.
**Azhar Momin** 50:09 Yes.
I haven't tried to, explore it. I haven't been to a… con… conference before. I will take a look today.
**Kemal Akkoyun** 50:19 Yeah, that would be amazing for you, as well, and as an experience. So, yeah, I think you should, like, Azhar should be the one to… Like, maybe submit something for us.
to talk about our tool? What do you think?
And the rest of us can join to the project meeting.
Awesome. We have some hearts.
Okay.
Bam.
That would be nice, like… Huxing, do you want to submit something for the project meeting, then?
**Huxing Zhang** 50:57 Yeah, yeah.
You can't assign it to me.
I'll stop.
**Kemal Akkoyun** 51:01 This is Azhar… some Hotel C talk.
**Xabier Martínez** 51:06 Let us know if you have any doubt or problem with that.
I have time to help on that.
**Kemal Akkoyun** 51:19 Is this your meal?
Sure, okay.
project meetings.
Awesome.
We still have 12 minutes.
Apparently, we should have met earlier. We already have… We discussed a lot. We have a lot of action items.
**Azhar Momin** 51:44 Okay, one last thing from me. We have a CI failing on conreb right now. I haven't explored merge queues, much, but maybe, I think merge queues can… help us, minimize those problems. So, when we enable auto-merge, the CI is passing on that PR, but when it gets into main, the CI starts failing. Maybe merge queues can help us with that.
**Kemal Akkoyun** 52:12 how it would help, what I'm missing.
Right now, we have auto-merge enabled, but it's… if CI is red, I've seen that.
But it would be the same for the merge queue as well.
**Azhar Momin** 52:26 Yeah, but it would block the PR from melding. Right now, it gets, when the PR itself has passing CR, but when it, gets into main, it starts failing because, maybe because of some other things. I haven't looked at the recent…
**Kemal Akkoyun** 52:40 Okay, I…
**Azhar Momin** 52:41 Maybe it's related to that.
**Kemal Akkoyun** 52:44 I got it, I got it now. You mean, like, you, like… Or, like, but it's the same behavior, you know?
with the merge queues. We can explore the merge queues, but for this case, I don't… I don't understand what it would bring, right? Because, let's say you, Sea ice failing, it's red.
And then you marked… PRs for AutoMerge.
And then you've merged something to fix?
Things on the main.
do you need to click the update PR button, right? So with the merge queue, you said, it won't be the case, because it will be auto-viewed, and if this fix landed on the main, everything's gonna merge. Okay, yes, all right, now I got it.
Yeah, why not? Happy to enable that.
Any disagreements? Like, anyone objects?
Enabling the merge queues?
No? Fine by me.
**Azhar Momin** 54:01 Mr.
**Kemal Akkoyun** 54:02 Merge keys also help with the stack PRs and whatnot, so I'm all in for that.
Only maintainers can use the stacked PRs right now, but still, I think maintainers are also the ones that sends a lot of PRs anyway.
**Xabier Martínez** 54:21 Yeah, I was checking, going back to the previous point, the gift card, that the… if we register as a project meeting.
the meeting facilitator will not receive, like, the registration pass, so I'm not sure if we can make Azhar get that, Oh, okay.
**Kemal Akkoyun** 54:43 Sorry, if it's not clear, it was not clear, I think Huxing going to submit for the project meeting?
Because probably he already submitted some other talks, or, like, our companies can sponsor us to go Barcelona.
But there's other type of talks which we should, like, submit.
That was the idea for Azhar, not the project meeting, but some other form to… for KubeCon, or obs… there is, like, KubeCon Observability Day.
There's the Maintainer Summit, and if you have a Tolkien Maintainer Summit, you should get a ticket, I think.
**Xabier Martínez** 55:18 Oh, okay, okay, okay, great, I misunderstood. Thank you.
**Kemal Akkoyun** 55:22 Project, yeah, project meeting is just for us to make sure that we have a SYNC meeting, so it could be Huxing or someone else.
**Xabier Martínez** 55:34 And… clear.
**Kemal Akkoyun** 55:38 Cool!
Anything else?
Going once?
Going twice, Azhar? Any last-minute thoughts?
Alright, cool.
Then, thanks everyone for attending.
I guess we have a really good momentum. Thanks for all the contributions, so keep up the good work, please.
And see you in… yeah, maybe in Barcelona.
Bye-bye.
**Huxing Zhang** 56:09 Bye-bye.
**Azhar Momin** 56:09 Why not?
**Xabier Martínez** 56:10 Bye.
