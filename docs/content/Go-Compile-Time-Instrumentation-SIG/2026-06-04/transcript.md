SIG: Go Compile Time Instrumentation SIG
Date: 2026-06-04
Duration: 89 minutes
============================================================

## Zoom Recording Transcript

Kemal Akkoyun 00:08:02 Hello, everyone.
Everyone is so silent.
vyagh 00:08:15 Hello.
Kemal Akkoyun 00:08:17 Hello. Thanks for breaking the silence!
Okay.
Okay, we have some AI things now.
Taking notes.
Interesting.
Shall we wait for it in the wild?
Xabier Martínez 00:09:17 Nope.
Kemal Akkoyun 00:09:19 Hello?
Juraci Paixão Kröhling 00:09:21 Mmm.
Huxing Zhang 00:09:24 Hello.
Kemal Akkoyun 00:09:24 Okay.
People are showing up.
Juraci Paixão Kröhling 00:09:30 hear you all.
Kemal Akkoyun 00:09:33 Nice.
Okay, I guess I will be the facilitator, I don't know.
was… Who's turn it is. So, just… Assuming the role, or no?
Oh, this is the wrong meeting.
I don't know what's going on. Okay, too many meetings. Please add your names, and you can just copy over one of the attendees.
This looks… Representative.
Okay… Right, yes, yes… Yeah, I think, more or less, but please add your names.
If you want to be documented.
So, do we have any agenda items? Like, I remember something on the Slack… from… I think… Xavier, I wanna talk about this.
We can add that.
Xabier Martínez 00:11:04 Yes.
Kemal Akkoyun 00:11:06 And we also… I think… You wanna talk about observability today?
That's KubeCon… Fair enough.
Okay.
And I want to talk about… V1, okay.
Remaining room, 4 rule… B1.
So, okay, welcome, everyone. This is another, SIG meeting of, OpenTelemetry Go Compile Instrumentation, SIG.
So, we have a couple of agenda items. First one from… Shall we ourselves, you can take it over.
Xabier Martínez 00:11:52 Yeah, okay, let me open… basically, my point, or I wanted to open some discussions Regarding what to do after the V1, Release.
We have, two projects, lots of instrumentation there that we need to migrate, and some of the instrumentation is already in repositories like OpenTrift.
There is, OpenTelemetry ZenConf, so we need to decide if we are going to reduce those instrumentations, if we are going to push everything to our own repository, we are going to maintain everything, if not.
My idea is not to decide right now, but… Just to get to an agreement to the direction, so we can continue working async.
I wanted to bring this discussion now, before the V1 release.
Just because, if we just wait too much, maybe we end up in, like, a blocked state.
where we need to discuss all this again. So, these are, like, discussions that we can push right now in a sync.
But we need to agree, if we are going to like the direction, if we are going to try to contribute to OpenTelemetry Go Country for repository, for example, or we're going to push everything in Oprah. So, I wanted to know your opinions about this.
Kemal Akkoyun 00:13:41 Okay, can I start?
Xabier Martínez 00:13:44 Sure.
Kemal Akkoyun 00:13:45 So I've been, thinking about this as well. I actually, like, checked the GoCountry repo recently, So, what I see from OpenTelemetry Go… so, this is the repo that we are talking about. Let's being made sure about it, so… Good, yes.
So… I checked what are the instrumentations that are actually, like, available through this repo, and you can immediately see that they say, like, there are a lot of instrumentations, but the following are included because they are so popular, right? The, like, this repo itself, they don't want to have a lot of instrumentations, so… and the rest is in the OpenTelemetry registry.
I think… I don't know how this works, but Jurassi in the call, maybe he can, like, enlighten us, but I think you can just, like, register your instrumentation in this website, right? So, my two cents is… we can follow the same footsteps. So the two things, right? We don't need to put all of the instrumentation in our repo, which we already agreed on, right? We maybe said that there will be another repo for all these instrumentations. But if we want to follow these footsteps, I mean, this could be another repo that we wrote most of the instrumentation, which is fine.
It could be also that, let's say, that since, like, the long suite has a lot of instrumentations, so I believe they can stay in the long suite, and then we can just register them in OpenTelemetry, as long as, like, the hotel C supports them.
They are discoverable for the community, it's also open source, it should be fine, right?
If we have additional, like, instrumentations that we would like to provide, we can have Either talk to the, OpenTelemagical country repo owners, right? Can we have a dedicated directory in here and put something? Because this is, like, more discoverable, compared to having yet another repo for instrumentation.
But there could be some, like, pushback, because they also don't have a lot of instrumentations here, right?
That's one… one idea. Like, this is two ideas, right? Sorry. So, one, keep everything where it is. The second one, have a repo for, like, our promoted instrumentation.
The third one, actually.
for example, there's also another issue, like, I think our tool supports everything here as is, should support everything here as is, right? We should be able to inject all these libraries, and we should have the patterns, and we should just provide, maybe.
single files to here, right? Just an itelic.yaml file, so we can directly use the country people. I think that would be ideal.
to support the existing integrations, like instrumentations here, but that means a lot of work in our OTLC repo, which is fine.
And yeah, the… and then, like, we can discuss the same thing. Do we really want to provide a lot of instrumentations for community? Do we really want to maintain those, right? We had this discussion… yeah, this is the discussions that… these are my… was my point here, right?
I don't think we really should be in the business of maintaining instrumentations, right? After a while, we should stop. This is endless, right? We can't… we don't have enough work, power to keep, like, these instrumentations up to date, right? We should just maintain the tool available, all possible patterns, so that instrumentation library providers can use this.
Xabier Martínez 00:17:54 Mmm… Yes, totally agree. For me, the main discussion is not… if we need to… like, where we need to put it, like, I agree… That we can use the auto registry, or contriv, wherever.
But when we do it, like, are we going to start migrating all of this first to a repo, and then migrate it to Vulcan 3 for registry, or just straight to it?
My second question is… In order to do that.
We will need to refactor, the long, sweet, and orchestrian instrumentation, because some of them, for example, the gene instrumentation is not based in a middle world, for example, so it's hard to use as an independent library.
So, it's like the raw runtime that can be used like an independent library, so you can just use that instrumentation manually in your service.
And then the wrapper over that, that it's what we should maintain in your site.
So… This is my point.
Kemal Akkoyun 00:19:15 Yeah.
Xabier Martínez 00:19:16 So, for example, for Gene, I see that we weren't, or Ensuite, or Chestion weren't using the middleware approach, I don't remember.
So we need to force this way, that all of the instrumentation that we are using are based on libraries that could be added manually to the services. So we just own the wrappers for the rules.
Kemal Akkoyun 00:19:42 origin.
Or, like, anything in this repo?
the hotel contract core repo. I think OTLC should support this. So we need… we just need a single file.
We need to be able… all the features.
And these integrations should work with our tool. That is my, like, goal.
And then we can just contribute a single file for all these integrations to do the OpenTelemetry GoCon trip. It's just single file, there is no hard dependency. Whenever they would like to use.
if they point to our tool, to this core country people, it would just, like, grab that file and inject it, right? For these, this should be our array, right?
Your second question.
the orchestrian instrumentations are not… they are not using OpenTelemetry SDKs, right? They are using DD Tracecore.
So… I don't think we… And, like.
So we… we can't just, like, support them, right? We need to rewrite them, so that you can use… they can use OpenTelemetry SDK.
So… That's why I don't think there's any migration, like, direct migration path for orchestrian. What we're gonna do, we will convert all these instrumentation that it would use OTLC, but then it would inject DDTrace go, right? So, we will… we will have all the patterns that needed in the OTLC, but it's there not, like, highlighted up, they are not, like, coupled, right? They are decoupled. They don't need to be in sync whatnot.
The long suitcase is different. Please chime in, Alibaba people, because they are already exposing OpenTelemetry, and they are using OpenTelemetry SDKs and whatnot, right? They are closer to be supported. But I think we still don't need to bring everything over to our repo.
If they started to, like, refactor.
their instrumentation to support OTLC with the same file, same interface, they can live in the long suite, right? And then we can register into the open telemetry. Long Suite itself is open source, right? We don't need to maintain those.
You don't need to duplicate the work, right? They… if they provide an Open Hotel C-compatible file in those instrumentations, this is just called a module system, this is what we agreed upon. If someone use… want to use everything from longswit this should just work, because it's already OpenTelemetry compliant.
What was it? Blogs?
Is it in here?
Haibin Zhang 00:22:33 Yes.
Kemal Akkoyun 00:22:35 Okay.
So, then probably packages… yeah.
Yeah.
So… I mean, they have already everything, Where's… The rules, yes. So all these rules, right? We don't need to rewrite them. Like, we need to rewrite them, but we don't need to migrate them, right? This is open source. One thing we need to check is, like, the license, I think.
So, I don't remember the license, and whether they are compatible. This is Apache 2.
And…
Huxing Zhang 00:23:12 Yes, it's Apache 2 license.
It's completely compatible, I think.
Kemal Akkoyun 00:23:18 Yeah, this is also a project. Like, these are completely compatible, so anything in this repo, everyone can use. It's the same community thing. I think, like, we just need to, like.
this is already done, right? Where is the rules? I think that we just need to have the OTLC YAML files in upstream Long Suit, and then I don't know how registry works, like, the same question, Jurassi in the call, I don't know if he's listening.
But we can just use the registry and register all the long suit instrumentations here, and make them discoverable for the community.
Juraci Paixão Kröhling 00:23:55 I think you just answered your question. It is a YAML file that you can just add to the… I think it is a community repository. So you can just add a YAML pointing to the right places.
Kemal Akkoyun 00:24:08 Okay, so you said community repository.
Juraci Paixão Kröhling 00:24:11 Sorry, OpenTrump 2.io.
Kemal Akkoyun 00:24:14 Okay, open to another trial.
What was the name of that people? I don't remember.
Juraci Paixão Kröhling 00:24:21 io, it's up there, like, to reposter is up.
No, no, at the pinned repositories.
Kemal Akkoyun 00:24:29 Okay, here. All right. This is… this is even easier then. Okay, so there… there is a file here for the registry.
Juraci Paixão Kröhling 00:24:36 Yeah, I know that they changed a little bit over the past, I don't know, Yeah, there you go.
Kemal Akkoyun 00:24:42 link to a registry. Yeah, amazing. We have the documentation. So, instrumentations. We… probably we will need to have a special tag.
I know there's auto-instrumentation, but maybe also auto-instrumentation plus, like, compile time instrumentation, and then we can register the long suit agent instrumentations here.
But then we need to provide, like, all the itelic files for them, and then boom, like, everything is, like, available for the community.
And it's already maintained by Alibaba, and they can iterate faster, right?
Let's say that we found another way that is, like.
somehow different, and we want to, like, support that. Again, like, we can talk about having a dedicated repository, or, like, as the GoCon trip does, maybe we can have, like, a limited, limited amount of, instrumentations here.
Yeah, that depends, like, what do you think? This is my, like, my two cents, and I think it's, like, this is also the easiest to implement. But I… yeah, I want to hear from Xavier or, like, Alibaba, like, what do you think about this?
Haibin Zhang 00:25:58 I'm hyping for the Alibaba.
Okay.
I have, straight comment in the issue.
About, use, OT configure for the implementation PKZ.
And, the first is, like, interface, invalidation is not limited to the hiring package, like the NetEP. I'm always thinking, in the new version of the Go, some interface is changed, but, in the country, I… I'm… I have no… No time to change the implementation, where… Where Arrow. And I'll just… Like, the dual repo about, an end-to-end test is, is not a good idea for the Full report. And, And always, I think the OTC can implementation the loss rate and the DDTrace or others is a good idea, but in our our country… our RIP.
I think we will have, NetHP and other, implementation in our report.
It can… Improve our, Whoa, whoa.
Okay.
Kemal Akkoyun 00:27:40 Okay, so let me rephrase if I… if I understand correctly, you said that Do you want to have the net HTTP in here? Or you don't want it.
You wanna… you wanna have it.
Haibin Zhang 00:27:59 I haven't too.
Kemal Akkoyun 00:28:02 Yeah, I think it's okay, like, as the GoCon trip does, right? There are selections of instrumentations here.
which is, like, supported by default, right? And which is, like, runtimeNet HTTP, gRPC, Mongo, and some other, like, repos, which is… I think we should… have the same, right? Some basic SQL, GRP, CNET, HTTPN, we are close to that, right? I think we can have some of them.
as first-order citizens, like, first-order instrumentations in our repo.
Haibin Zhang 00:28:41 this could trip, the… like, gRPC, like the Mongol, I don't know who maintained this, about if the SDK is changed or updated, and the others.
Kemal Akkoyun 00:28:57 I think this is the Go SDK SIG.
So, yeah, there's the goal SDK sync.
we can… like, this is just a code owner question, right? If we put those files here, we can just assign ourselves as code owners, and also add some end-to-end tests here.
And then if something happens with those files, or like, or those tests that break, we can be responsible and maintain those and fix those.
Haibin Zhang 00:29:35 Okay.
Kemal Akkoyun 00:29:35 Of course, we need to talk to the… we also need… sorry to cut you, just to add, we need to talk to the Go SDK SIG first, of course, if they are open to… be adding those files and assigning our SIG as code owners. We need to have that conversation.
Haibin Zhang 00:29:58 I think we need to have a comprehensive implication within our report to ensure a better user experience.
Naturally, it can always also be utilized to inject other ripples, like… like long swings or the DD trees.
is mine.
Kemal Akkoyun 00:30:21 I agree.
Haibin Zhang 00:30:21 option.
Kemal Akkoyun 00:30:24 I totally agree, but… But it should be, like, limited amount of integrations, right?
like, not HTT, whatnot. You are not saying… Or, like, if you're saying that let's move all the long-suit integrations to the main repo, is this what you want, or is just… do you want limited amount of integrations?
Haibin Zhang 00:30:55 In the contrib… now is how the DRPC or other gene, like the mongrel. If we have other estates that need to, implement… implemented, we will contribute to our rep, or all the contrib.
I… I simply… I think in a country built to our roof is the… is a good idea for this.
Kemal Akkoyun 00:31:26 Okay.
I get it, but, like, Which instrumentations?
like… just a selected number of instrumentations, like gRPC, NetHTP, Or, like, all of them.
Haibin Zhang 00:31:45 Okay, you.
Kemal Akkoyun 00:31:55 My gut feeling tells me that we can have a limited amount of instrumentations in the upstream, right? The critical ones, like the most commonly used ones.
But not everything, right? We can't maintain all of these things.
Haibin Zhang 00:32:13 Yeah, and now in my RIP, it always have the HP or GIPC or others.
I think we were… Focus on keeping a stable, like, related, working.
I, I always post, and yeah, and other, and then now, and next, we… we… They, update the new SDK, to the… our rip all of the con cheap. I think, It's, user option, and what… We sh… We can't we not decide.
Kemal Akkoyun 00:33:01 Yes, this is… we are exactly on the same page, I guess. We are not, like, conflicting here. We should have limited amount of instrumentation in the main repo to guarantee level of service.
But the rest of the things can live somewhere else. It can live in Long Suit, it can live in any other repo. We can use registry to discover that, so they will be available to the community.
And that's it.
Haibin Zhang 00:33:29 Yes.
Okay. Okay.
Kemal Akkoyun 00:33:32 Maybe you should document this, right? Let's document this, like a consensus call.
Xabier Martínez 00:33:39 The idea is to… use directly the instrumentation that's currently redefined in all countries.
No, sir, we are going to add that instrumentation.
to autopsy.
And…
Kemal Akkoyun 00:33:56 I think…
Xabier Martínez 00:33:57 Right? They will live in the other repositories.
Kemal Akkoyun 00:34:00 Yes, I think, that is what, like, Hobbin wants to have, like, have a limited number of instrumentation in, our repo.
for… Quality assurance, basically.
Haibin Zhang 00:34:17 Yes.
Kemal Akkoyun 00:34:17 gRPC, HC… NetHTP…
Haibin Zhang 00:34:22 with DB.
Kemal Akkoyun 00:34:24 DB. DB.
And… the most popular one. It's most popular. We can even say that, like, the standard, library…
Haibin Zhang 00:34:36 our package.
Kemal Akkoyun 00:34:37 Yeah, standard library instrumentation.
Plus some, and the most popular I don't know, tree? .
Haibin Zhang 00:34:49 Yeah.
Kemal Akkoyun 00:34:49 I don't know.
It's hard to… Find these numbers, let's say that.
I'm fine with that. Like… We can also, like, the similar approach, the alternative would be like, alternative… is… So, support… These instrumentations in here.
So… Okay.
buys.
Adding hotels, see files, and assigning… files and E2E tests, probably. I don't know the testing infrastructure in that.
and, assign… our SIG… Can't type today. Let's called owners.
Xabier Martínez 00:35:54 will those files be in GoConrieve, or in Otenshi?
Kemal Akkoyun 00:35:58 Yeah. Yes, it should… they should be… so, one of our agreements previously, the target modules should have the files, right? So, in this part, it should be GoCon Trip. But, like, this is… this is long-term, right? Alternative and long-term. We should definitely.
Haibin Zhang 00:36:16 Yeah.
Kemal Akkoyun 00:36:17 go into this after we are… we have stable APIs, whatnot, and we know that we can support all these, frictionless, right? It's just a single file that we need to maintain, maybe some tests. Then we can ask to see, right?
But for this, you need… We need to talk.
For the Google SDKC.
Xabier Martínez 00:36:40 So we will start out in our repo, directly the instrumentation over that.
Like, we'll use local trig, for example, 14.
Kemal Akkoyun 00:36:50 Eventually, I think we should.
Xabier Martínez 00:36:52 Okay.
Kemal Akkoyun 00:36:53 I was like, why do we… why do we confuse the community, right? There are some instrumentations in this compile time, there are some instrumentations for, like, which one I'm going to use, like.
for them, it should be frictionless, right? We should just support, like… and eventually, I believe, like, this is probably already… these are quite popular.
And this is… these are not, like, these are quite popular among open telemetry, probably, because this is the, like, the official instrumentation, so… Yeah, I think, it should be… It should be the way to go.
Also, also, okay, the other one. About the long foot, instrumentations, are you, are, like, Do we have a consensus on keeping them in your repo, making them OTRC compatible, and then using registry to make them available to the community?
Haibin Zhang 00:37:55 Yes.
Xabier Martínez 00:37:57 Cool. Maybe… I like that idea, like, let's make a long suite, compatible with OTLC.
We should also document that in OTLC repo, that you have this based instrumentation, but you also have these other instrumentation from LaunchSuite that are already compatible, and maybe in the future, community just try to move some of those instrumentation to, GoCon 3, for example.
Kemal Akkoyun 00:38:28 Yeah, I think, like, technically.
the long-fit instrumentations, they are already compatible, because they are always… they always use, the trampoline approach. I think only missing thing, I don't… oh, these are also Go module files. I think… we need the YAML files in these modules, if I'm… yeah, this was our design.
We need to have the YAML files in these modules, and then we point to the OTLC to this module. It should download that file, and just do the injection. You don't have to go some files in here, is this by design?
Haibin Zhang 00:39:07 Yeah, if the OTSA were to the stable, Listen, we were treated.
Kemal Akkoyun 00:39:14 Okay.
You have some files here, okay. Anyway, this is detail. So, you… if you, like, if we have, like, hotelc.tyaml files in these, and they are already compatible, right? And then…
Haibin Zhang 00:39:30 Yeah, we'll update it.
Kemal Akkoyun 00:39:33 Okay, cool. Then, yeah, provide files in the modules, so let's say… what else? Here are the YAML files in the modules, and then… Use the registry… to Edward… Or is, where did I find that?
Okay, adding the registry, I think this is the… Okay. This makes easier than, like, long suits that you are already maintaining all the instrumentations anyway, should be fine, right? Then if someone else wants to, Maintain, like, maintain other instrumentations and make them available for the community should be no-brainer, right?
maybe, like, for orchestrian, for example, if we think that we have a better approach for whatever reason, and we would like to expose the OpenTelemetry SDK using that version, we can just, like, put a file, and that's it, right?
Xabier Martínez 00:40:46 Cool, what about?
Another question, what about your instrumentation from Datador?
Kemal Akkoyun 00:40:53 we will convert… we will provide OTA YAMLs to inject DD traccope.
Xabier Martínez 00:40:59 Oh, also. So, you can choose.
Kemal Akkoyun 00:41:01 Yeah, we will decommission the orchestrian, right?
we will use Autelic to inject DDRE scope.
Okay.
Xabier Martínez 00:41:13 I like that, as an extra step, but it could be maybe confusing for the community, having those two independent repos, like…
Kemal Akkoyun 00:41:23 They're completely different. They're not even competing, right? Because, like, DDTresco, by default, it's a completely different path, different SDK, it's not using… it can technically expose all TLP, right? But it's different, right? So… it shouldn't create any confusion, and we won't register them to the OpenTelemetry registry, because they are not OpenTelemetry by default.
So, there won't be confusion, like, most of the integrations will be coming from Longsuit.
Xabier Martínez 00:41:54 Okay.
Kemal Akkoyun 00:41:58 Okay.
So… What else?
Did we miss anything?
Xabier Martínez 00:42:11 No, sounds like a solid next steps. This should be part of V2, no?
Kemal Akkoyun 00:42:19 I don't think… you know?
Xabier Martínez 00:42:20 It's the…
Kemal Akkoyun 00:42:21 This is… this is not related to the V2, like, this can eventually happen. This is independent of the OTLC features. Like, this is… these are already supported. I don't remember the latest stage of that module support. I think there was an issue, but yeah, let's check that.
Has anyone, like, does anyone remember that? So… He had this summer.
Now, this is already in V1.
This is something else… yeah, this is the… this can be done after, like, V1.
I totally had an issue about this, like, having complete, removed… maybe we already implemented that.
Guillan, do you remember if we implemented, like, complete module support, remote module support? Which means, like, point to me any Go module, and if there is an OTLC YAML file, we will just inject that did fee, and actually, that's a perk.
I think we did, right?
I don't know if it ever tested that.
But yeah, like, this is the basic structure that should work. I think we added that. So, there's no blocker.
Apparently, we need to test that, but yeah, there is no blocker.
Okay, any other things that we have… we need to address?
Xabier Martínez 00:44:11 I think we can move on with the next point.
Azhar Momin 00:44:15 I had one question, regarding this. So… Our goal with this was to, decouple the integrations from the tool, right?
Yes. So, will we be able to support a wide range of versions, or are we still going to support two major releases for each liability?
Kemal Akkoyun 00:44:35 A good question. So, let's add that, version support.
So… like… For the third-party integrations that live somewhere else, Integrations providers can decide that.
Meaning, aka Longstreet in this case. But for our… tool, it should be last… the last major tool versions.
we don't… we don't care, like, we did… we didn't even release the tool, right? After we, like, the point that we released V1, we should only support 125 and 126.
Azhar Momin 00:45:20 Okay.
Kemal Akkoyun 00:45:21 And then, for rolling each version, we can improve that, right?
And if someone wants to use, use an instrumentation for older version of code, they can just use an older version of R2.
Azhar Momin 00:45:39 That sounds important.
Kemal Akkoyun 00:45:40 But I… yeah, sorry.
Azhar Momin 00:45:44 Oh, please continue.
Kemal Akkoyun 00:45:46 The… in an ideal world, we should decouple from Hotel C from any of the instrumentation, but it's in an ideal world, it wouldn't work because of the Go module systems, because whenever a Go module declares the minimum supported Go version, then you need to upgrade everything.
So, we can, like, be sensitive and not, like, bump the OTLC minimum supported version.
for a long time, unless we use a specific API from Go, and then we can… like, the… support range for OTLC can be as large as possible, but in practice, there's always a feature that you want, and you pump that minimum version, so let's officially, let's just support the last major.
two versions.
Any other comments?
Do we agree on that.
Haibin Zhang 00:46:47 No cousin.
Kemal Akkoyun 00:46:49 Okay. I'm gonna, like, officially call for consensus here, to just mark this, so… Do we have consensus on all these three points?
Please do a thumbs up, thumbs down, okay?
Cool.
I don't see any thumbs downs, okay?
Alright, on the recording, I'm officially sealing it.
Of course, this is not Git, so someone can tamper with this, but we will have the recording.
So, okay.
Cool! Any, any other topics on this? Like, did you get your answers, Xavier?
Xabier Martínez 00:47:33 Yes, I will update the issue with all these comments.
Kemal Akkoyun 00:47:38 Awesome, thank you, thank you for that. Okay.
So, we have still 19 minutes left, so we have enough time to discuss the observability today.
So… Do you want to take it over, Roshin?
Huxing Zhang 00:47:55 Yeah, yeah, we actually… we have missed the deadline for the KubeCon main conference, I think, but we still have a chance to submit to the Observability Day in… I… I guess, we'll still have, like, Deadline will have… Hmm, over… maybe…
Kemal Akkoyun 00:48:15 Correct.
Huxing Zhang 00:48:15 Several days left.
Kemal Akkoyun 00:48:17 Yeah.
Huxing Zhang 00:48:17 I'm not… I don't remember the detail, the exact date of the deadline, but we still have it.
Kemal Akkoyun 00:48:24 21st of June.
Huxing Zhang 00:48:27 Or do you know about that?
Kemal Akkoyun 00:48:29 Yeah, I think it was 21st of June, I will double check.
Huxing Zhang 00:48:35 Yeah.
Kemal Akkoyun 00:48:35 Observability Day, CubeCon… Yes.
To any… nope, this is the old one.
Oh, this is for the Euro. Okay, XIQ.
Colon NA26.
Yes, and events, events, co-located events… observing today.
Sponsored event? Yeah, 21st of June.
Okay, so…
Huxing Zhang 00:49:20 Yeah.
Kemal Akkoyun 00:49:23 Yeah, what are your thoughts? Like, so far, we couldn't get any talks accepted to either Observability Day or KubeCon. We are trying for the past year.
Huxing Zhang 00:49:35 Yeah, we, we actually have submitted, one proposal to the KubeCon China this year, but we are still waiting for the… notifications, but it doesn't mean that we don't have to submit to Kukan North America, because I think it's a big event for the whole year, and we should… definitely, advocate our project towards SEEK.
So, given the… given the, result that we have, or past the experience, I'm proposing some proposal that we… maybe we should… like, cooperation, have some cooperation with other states, in order to increase the chance that we get a, would get an accept, but I think maybe to Rusty, have some advice for us, and,
Kemal Akkoyun 00:50:40 He already raised his hand, so…
Juraci Paixão Kröhling 00:50:43 Yeah, so, yeah, my camera is not very bad, I'm trying to change my sensor. But, so… In any case… please send the proposal to me, and I can give some feedback before you actually send it over.
I've reviewed literally, like, hundreds of proposals. I can help you see… Find the blind spots in the proposals.
So this is one thing, right? So no matter what happens, send it to me, and I can give you some advice there.
But in general.
what I… what I really suggest to you all is don't focus on… too much on the engineering side, focus on the problem-solving piece. Like, what is the problem that you're solving there?
what are the people that are your… what is your audience? Why do they… why do they care about what you're doing?
So, go for a, from an end-user perspective, like, that's the audience for the conference. The people there are the platform engineers, they are the software engineers, they are the people who are using the tools, so don't focus too much on the… what is cool about GoAuth instrumentation, but focus more on, here's the problem, and here's the solution.
Right, so don't try to… make an introduction to the project, go with a problem, like, oh, we had so many, Go projects internally at Alibaba.
And we… and we were not having visibility into those, and we saw the Java folks having this cool stuff called Java optimization that gave us a… I don't know.
But I… Talk about the problem, and then the solution.
And typically, the way that I structure proposals is a three-paragraph Proposal, like, one is… the first one is, A… a problem statement?
So, what is the problem that I'm solving? What is the thing that I'm covering on the call, or on the talk?
Second is a short description of the solution.
And then the third is, what is the takeaway for the community members? Like, what is… what is the audience taking from that talk? If you structure in those three paragraphs, then it's already A very good proposal for somebody who's reviewing, so that people know Why this stock deserves Twitter.
Of course, catch titles. Most of the people, they choose their talks based on the title, so they look at the titles, oh, this is cool, I'm gonna go there, I'm gonna watch this one. They don't even read the abstract. But abstract is very important for the people who are reviewing The proposals for the conference.
Yeah. Again, more than happy to brainstorm with you all.
On, on, on the… On the talk itself, on the proposal itself.
I know you… you probably want both to be there, like Datadog and Alibaba.
But what I really, really encourage you all is, get an end user. Get somebody who's using the tool. I know that Alibaba is an end user in that scenario, but try to get somebody else as well to go there on stage with y'all.
Right, so I… I see a, Somebody here is also from an end user company?
Can we find a figure song?
Kemal Akkoyun 00:54:17 Yeah, Sharia, are you using this tool, in New York.
Huxing Zhang 00:54:24 Company.
Kemal Akkoyun 00:54:25 Yeah, recovery.
Xabier Martínez 00:54:25 Not yet.
Kemal Akkoyun 00:54:28 Okay.
Juraci Paixão Kröhling 00:54:29 Yeah, I'll really encourage to get end users, to go there and see, so this is the problem that we had, and so on, and then, and then talk about the solution.
Kemal Akkoyun 00:54:40 Actually, we have a community member, from Victoria Metrics, and I think Victoria Metrics is using this. Maybe not as a vendor, as a user, they are using this. So, we can talk to them and reach out, maybe they would be happy to Go to the stage with us and talk. What do you think is the good idea?
Juraci Paixão Kröhling 00:55:04 Honestly, I don't know.
I would… I would say that a true end user, like, somebody who… Without any… any red flags in terms of… vendor pitches and so on, like, that would be ideal. Like, somebody who… So, if I'm reviewing the proposal, and I see the name of Victoria Metrics there, or any other names, like any other vendors, then the first question that I'm going to ask is, is this a product pitch? Is it a… is it trying to sell anything to the people there?
If I have any questions at least.
then I'm gonna revisit the proposal, perhaps with different eyes. So the proposal has to be extremely clear that she's not trying to sell anything that's not very specific to parametrics or data dialogue.
And then… and then you'd have to convince me, but that's… that's way harder.
I would find a true end user, like somebody who is not selling shovels there, who's not selling tools.
Somebody who says, you know, I have this problem, I'm using this to solve this specific issue.
If you don't have that, that's fine. I think Alibaba fits the situation there. But if you are there.
machine for Alibaba, then you don't, you don't sell the tool that you have internally at Alibaba. The same with Kemau. Chemau is not gonna sell our orchestral, right? So it is really about to go compiler time instrumentation. It is really, this is the problem, this is the solution, and if you are not using what you are showing.
Then this is not true anymore.
So, this is not a true user, end user, for that case. And then it becomes, I'm building tools on top of this tool.
Which then kind of dilutes the value of the tool that you are displaying there, because then the image that it passes… it is not… useful, On its own, on the current stage.
And it should be.
And if you think that it's not useful right now, at its current stage, then wait a little bit. It's better to go there with the full-fledged, or not full-fledged, but with a… something that the audience can take away and play Right after the talk, then to get some noise and get some excitement, and then people get disappointed by not being able to use Right now.
Kemal Akkoyun 00:57:25 Okay.
These are great advices. Who wants to draft the, like, the… First initial draft for the proposal?
Huxing Zhang 00:57:38 I'd like to, and actually, I want to respond to what Jurassi says, is… Actually, the problem here is, our OTLC tool, or this project, it's not reached the stable version yet, so we can… may not be… find a very good end user that's already using it in production or, in massive scale. But actually, if you are looking at the Alibaba one, actually, there's a lot of… open source end users, or whether open source or, their UR product.
there's a lot of customers, but they… I think they don't… one, they don't have… they don't… have time to go to, you know, North America in this conference. I mean, they maybe go to China, but they don't have the time or to… Second, they, they don't use the, just as they… they don't use the Open Telemetry project, but the… maybe using Long Suite from Alibaba. That's not a, proper, proper choice for now. So, what I'm thinking is to, like, if we want, maybe we could do some, from, flash, like, lightning talk, or some other, format of the proposal. We want to make sure that there is some… some chance for us to showcase this, project, and let more people know, because we… I think at that time, we… we… we have… have reached the stable state.
And, to make more people know about this project, then it, will help us to, like, to have more end users, maybe for next year, we'll get, get a real… and the user can Talk about that.
Yeah, I can have a proposal, but I'm thinking of different formats this year, maybe letting talk, maybe some cooperation with other stake, and be part of that, or be part of the OTL community update.
proposal. That's one of… that's another choice, I think.
we can have one or two slides in, if we have… time and space, we can have one or two slides to the hotel community update.
Proposal to, to, to advocate for that.
Yeah, that's what I'm thinking currently, yeah.
Juraci Paixão Kröhling 01:00:29 Yeah.
I would suggest then to… How about we target a proper… a highlight session with, end users for… for Barcelona next year, so for KubeCon Europe next year. That's in, what, April, perhaps? So we have time To wrap up the important things that you have in the project right now, and then get end users, and then get a good story.
For… for Europe. In the meantime, I'm here for you all. I can help you make noise, I can help you make connections, and what… what I can… what I can suggest then is.
First.
You can definitely submit a proposal. I would refrain. Instead of talking about the tool, I would talk about the technique.
I would perhaps talk about, like, create a proposal, perhaps not even for observability Day, but perhaps for some, some event closer, or close to Observability Day.
on… on the cool algorithms that you have there. I submitted a similar one for KubeCon, hopefully it gets selected, but so it might not be a perfect fit for Observability Day, but even if there's no better track, you can try.
But they're not focusing on the tool, not focusing on… people use, HotelC.
It's really gonna be… the quirks of Alto instrumentation, and then you can pair up with the folks from the Java Alto instrumentation, for instance, as well. So that, half of the talk is about the quirks for Go, half of it could be the quirks for for Java, for the Java agent. You could perhaps even talk to the Bela folks or to Obi folks, because they have, some, some querits at that level as well, that kind of, like, how to map memories and blah, blah, blah. That could be a nice talk between the three of you.
But very technical and very on the instrumentation side of things, like, how instrumentation works under the hood, what are the quirks, why is it so hard, why is it so interesting, and so on.
This could be one angle. I think that could work a lot.
Better than just focusing on the goal of the instrumentation for the moment.
And then… We can also focus on making noise to acquire your first end users.
So let's make noise on YouTube, on the open country YouTube channels.
I can also give you all some space. I know this is a community, so we can talk later about other channels that I can help to promote you, but I can help promote you all.
In other channels as well.
The idea being, let's focus on acquiring the first end users for the project, and then nurture them for CubeCon next year, for Europe.
You were on mute, Colon.
Kemal Akkoyun 01:03:32 Okay, sorry about that. So it's a great plan, thanks for, like, fleshing that out. Okay, so we will release V1, try to acquire our first end user.
For doing that, we need to do a lot of marketing, so we can take any offer that you can give us. Like, we would be happy to participate in any YouTube channel or, like, podcast. I don't know, maybe we can… After we won, we can publish an official OpenTelemetry blog post that could also… super useful, and maybe with some tutorials.
For V1, we already have this roadmap of, like, having official documentation in the official OpenTelemetry website, so after that, I think it would be easier for us to talk about it broadly.
Okay, duh…
Juraci Paixão Kröhling 01:04:22 Don't forget the community members, the community managers, sorry. We have a group called Community Managers, that's, Adliana Vilela, that's Risley, and that's Julia Morgado.
They are also dev rails at their companies, they can also help make noise, but, you can let that with me, so I can, I can search for them.
You know, whenever time's ready. I just need you all then to ping me whenever you are ready, so that we can make noise.
Kemal Akkoyun 01:04:48 Okay, thank you so much.
Juraci Paixão Kröhling 01:04:50 Of course.
Kemal Akkoyun 01:04:53 Any other questions to Jurassi, or on this topic?
Huxing Zhang 01:05:00 Yeah, I would try to draft some ideas, and maybe we can collaborate.
After this meeting.
Kemal Akkoyun 01:05:09 Sounds good. Yeah, ping… feel free to ping us, yeah, on the review.
So we have only one minute left. We have the V1 work. I just want to quickly talk about it. I think this issue is already, like, sound. We just need to make sure that we have everything done as soon as possible, because we said that June And, I mean, I know Yiyan has some plans for the website pages.
If he's busy, he can, like, hand it over to someone else.
Because we have, like, the web UI, like, we said that this is V1, and a web UI for code exploration. This was from Premierk, but he is silent lately. We can… I think we can drop this one, because it's already in the stretch goal, so it's not a big deal. It's, like, a nice-to-have developer tool.
we can drop that, but the rest of the things I think we should have. And for reaching out to feature parity, this is what I'm working on, especially OP4 things. I already have PRs, and I have some issues. I will be sending PRs for those. I think that's the big chunk of work, and I'm on it.
The rest of these, I think we already, like, reflect the website and quality assurance infrastructure.
Yeah, like, documentation, whatnot.
This can be… Yeah.
I will revisit those, like, external configuration sources, this can wait for V1, the configuration loader validator interpreter. These are additional tooling that eventually can get there.
Meaning we want to have a linter, for example, to check our rules, whatnot. But yeah, it's really nice to have. May… I will update, carry some of these issues, like, directly to the upstream release V1.
So we are in the, like, last, last corner of this, so, if anyone wants to assign themselves into these issues, like, please engage in two comments, and let's get this over with. We can still do it in June, I have high hopes, so let's push for it.
Any questions?
Any concerns about the roadmap?
Xabier Martínez 01:07:36 No, I… just one question. I just remember reading in our testion that, you can… Select or skip the instrumentations that you want.
It's something that we are planning to add here also.
Or maybe for the future?
Kemal Akkoyun 01:07:59 And then skip, what do you mean by that? Like…
Xabier Martínez 01:08:03 I remember reading that you can enable or disable some instrumentation, like the DPEs or…
Kemal Akkoyun 01:08:13 It is per instrumentation, right? There are, like, we usually have this, Guards, with environment variables to disable them on the runtime.
Right? So, that's one level we have. The second one is just, like, simple Go module support, right? Like, you are adding this by default. You say that, okay, I want to have this instrumentation, just so you point that into your Go module, which we already have.
It's editive, right? So it should be working.
Xabier Martínez 01:08:48 maybe we need to document all that, like, I'm just thinking that, okay, we have all the long suite instrumentation.
If a user doesn't want to use all that instrumentation, it should be able to decide easily.
Kemal Akkoyun 01:09:02 Oh yeah, yeah, like, this should be one by one. We are not going to, like, I don't know, I don't think this is the case. Habin, maybe you can correct me, but these are also by rule basis, so you don't just get the whole thing at once.
This whole package, you don't get them at once.
Just, like, at them one by one.
It should be like that, so it should be selective from the beginning. I just want to have this more, like, instrumentation, not the whole thing.
Xabier Martínez 01:09:33 Okay, because right now we are adding all of them at the same time.
Kemal Akkoyun 01:09:37 Okay, that's something that we need to fix, like, if you have any, like, if it's the case, please open an issue. It should be, like, yeah, that's the thing that I was, like, getting at, like, it should be… I should be able to say that, like, this is my instrumentation. I just want to have this module.
Right? In our… so yeah, okay, I now remember this. So in Orchestrian, we have this, like, orchestrian.tool.go file, which is, like, a Mugo module file, and in that, we have the imports, right? And we actually want that for the V1.
this one was the thing that I was, like, getting at. I thought we had this.
Do we have it? We don't have it.
Xabier Martínez 01:10:20 I don't think so… But yeah, I was talking about it. I think it's an interesting feature.
Kemal Akkoyun 01:10:28 Yeah, let's, like… let's create an issue for that, and it should be in the V1. That's definitely one thing that we have, that, like, import file module, so that you can add your imports, and then we can discuss that. That is critical, actually.
I will create that, okay? So… Pause this.
Yeah… something like OTLC runtimeGo file, but otelc.tool.go file, we need to have that, so, we can actually… I can… yeah, if anyone wants to drop in from the meeting, yeah, please do so.
Okay, add… Hotel C, tool… That's cool.
File support.
This file should help us to… Definder required dependencies for the instrumentations.
Too many titles… Okay, this is the… I have this… I will add a… An example from here… You should have it… Yes. This is… One example do I have?
About an example.
Yes.
So, this is what we need.
Nope.
Similar logic to… This… this… like, there's two things that we do. We… sometimes we auto-generate this, depending on the instrumentation, or if there is, already an orchestration.tool.co, we just support that. So… Okay, I am creating this, And adding this to V1, I will populate, for the rest… no, here's our milestone.
Xabier Martínez 01:13:09 Yeah, I know you.
how it's done in Longshuite, or if they had this problem.
Kemal Akkoyun 01:13:17 maybe one of the Alibaba people can comment on that. I don't also… I don't remember seeing a similar file for… Or dark.
Blocked.
Why I see different things here.
Cheers.
Okay, so… This is… this is gone.
Define an overhead SLO injection. Yeah, I think we need an issue for this.
You were working on this… Shabbra, can you maybe create an issue for this one?
Xabier Martínez 01:14:30 Yes.
Kemal Akkoyun 01:14:31 Thank you.
So, let's check, reach the feature parity, I will create some of the, like, move some of these things from there. Yeah, we can move this thing to the top-level instrumentation, should… It's, like, a bit of a cold turn, but it should be supported.
Test capital to check the current, yes.
I think we should work on it.
Yeah, we need some sort of a documentation page, we need to update that.
Okay, I forget to add this issue.
To the tool, this is… an important one.
Okay.
So, for the feature parity… Not just the GitHub pages, open… Official documentation.
Oops, for documentation, yeah, let's say that, we actually have… Respawn… I will… Create issues for this, these things.
Are we already hiding?
We already have some issues for this as well.
He can create dedicated issues.
In the roadmap.
Good choice.
I think we are not using to track the… I'll leave all about things for here.
I think what I'm gonna do is, like, instead of putting these here, like… This can be dropped from V1.
maybe 10… Instead, directly these.
Was it Long 64? Yes.
In a format that is more compatible to here.
I think this should be… Way better. I already have these.
Do you have any other issues you would like to add this?
Yeah, to this one.
Xabier Martínez 01:17:49 Nope.
Kemal Akkoyun 01:17:58 Okay. Yeah, much more clear.
Yeah, this is a big issue. These, like, these are redundant. I'm gonna address these after a while.
Clean these things out.
Okay, yeah.
Okay, do we have now… I'm working on this, we need someone to work on this. If there's no takers, I can take that afterwards.
Azhar Momin 01:18:34 I had one question regarding OTLC.tool.go, I wanted to make sure I understand it correctly. So, we already defined in Go.nod, what package we have, so rules can then detect what implementations we want. So, will this file be, like, what rules to match against? Did I understand that correctly?
Kemal Akkoyun 01:18:55 These files would be, like.
this is, like, you can see here that what this tool does, you create this file, you can check the orchestration on how it works, but you say that, okay, all the instrumentations in the DDTrace code, I would like to include, and then these are all modules, right? We can just go there.
And… there's our country people, contributes, and we have a bunch of instrumentations here, and each of these are, like, modules.
Right? And we have Orchestral YAML in here. So, this is just Go module system, right? If you give a Go module to it, it will just, like, download everything.
And what we are, like, piggybagging on this issue, like, on this tool, basically, you are just doing a blank import statement. That means go module system downloads that, and then the whole file is discoverable, and you use it, right? So this is our way of, like, managing our dependencies. So.
Ideally, when you say hotel.c in a project, and if that project specifies an otel.c.co, it will just, like, download all those dependencies, discover their hotelC, yaml.files.
parse that and start injecting the code. And if those OTLC modules, OTL-C YAML files have other modules that they import, it would also get them inside.
Azhar Momin 01:20:27 Okay, I'll try to push this one.
Kemal Akkoyun 01:20:30 Okay, I'm happy to assign this to you, and if you have any, like, more questions, like, feel free to ask.
I can… I don't like this… Completion.
Azar, what was your handle? Amazing?
Azhar Momin 01:20:47 Yes, it was amazing. I don't know why it's not showing.
Kemal Akkoyun 01:20:51 What an amazing sound, right?
amazing Akai, but somehow I can't assign this to you. I don't know. Okay.
If I do this, can I assign now?
Anyways, okay, like, let's… but I think it's a big chunk of work, like, I don't want to fight on GitHub on recording. So, please, like, feel free to ask more questions. I will try to populate it more.
We have this, so… Okay.
Xabier Martínez 01:21:33 Are we planning to test in… in Datadoc or Alibaba before the big one, or after the big one.
Kemal Akkoyun 01:21:43 Yeah, we are, like, we are also trying to… During our migration, we're gonna, like, start adding the OTLC, YAML files, and we are, like, we're about to start that, and then we will see, like, how we are… if we are missing any features during this month, we are trying to contribute back, and while also doing that, we will do some, like, performance comparison and whatnot.
But… if we discover it is, there's a performance regression and hotel orchestron is faster, I don't think this should be a blocker for V1. We should just, like, go for, move forward, and then… we will, try to contribute back some performance improvements, so…
Xabier Martínez 01:22:31 Okay, yeah, that sounds great. So, you will work on parallel.
Kemal Akkoyun 01:22:36 yeah, we will work on parallel, migrating all our integrations, and bringing back all the discovered issues to the upstream. Yeah.
Xabier Martínez 01:22:46 That's right. Thank you.
Kemal Akkoyun 01:22:49 I… Hope, like, probably that will be also long suits, like… progression and their experience. So, the upstream tool, in the end, will be the perfect one that can exchange all the downstream tools.
Xabier Martínez 01:23:09 Right?
Kemal Akkoyun 01:23:10 Robin?
Habin, I think he's our, instrumentation expert, so…
Haibin Zhang 01:23:16 Yeah. Yeah.
Kemal Akkoyun 01:23:18 Okay.
Yeah… okay, I'm gonna try to… Put more context on this.
I will… Try to make sure that every… we have issues for all these things, and they are, like, committed, like, sing to the… This umbrella issue.
Yup.
Any questions?
Haibin Zhang 01:23:51 Oh, okay.
No, no question.
Kemal Akkoyun 01:23:55 Awesome.
Thanks, everyone. This was a long session, but we have been skipping a lot of meetings lately, so, it's good… it's good that we have that. I won't be, here for the next two weeks. There's GopherCon Europe, and I have a team meeting, so I won't be able to attend to meetings, but feel free to have them.
Right, if you have any questions, we can talk on Slack.
Xabier Martínez 01:24:27 Yes, I will be also out next week.
At the bottom, I will be… Pushing, the user I have assigned, so…
Kemal Akkoyun 01:24:38 Awesome.
Alright, see you, see everyone around. Bye-bye.
Xabier Martínez 01:24:44 Thank you all. Bye-bye.
Azhar Momin 01:24:46 Thank you, anyone.
Yi Yang 01:24:48 Oh, bye-bye.
