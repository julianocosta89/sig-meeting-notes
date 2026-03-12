SIG: Kubernetes Operator SIG
Date: 2026-01-29
Duration: 67 minutes
Zoom Recording URL: https://zoom.us/rec/share/pCo6UHKktFZHcctx56MuptEk66q4vG5QXN-9ahvXTO3XHHbVs80-w-dAQT_v0jCY.7JAspSXMPbmUFNrB
============================================================

## Zoom Recording Transcript

Mikołaj Świątek 00:01:49 Hey, Israel.
Israel Blancas 00:01:51 Hey, how are you doing?
Mikołaj Świątek 00:01:57 I'm recovering from a cold.
Israel Blancas 00:02:00 Oh… Victoria off.
Mikołaj Świątek 00:02:03 It's also cold outside.
Israel Blancas 00:02:06 Yeah. Yeah.
Yeah, so usually we don't see, like, there's no… I mean… We have the mountains, like, 45 minutes driving, right, from where I live.
Usually there is snow, or even a ski station or everything, right? But, like, you see the… the snow in the mountains, right? But now, like.
intermittance, I can arrive to the snow, right? So it's, yeah, it's pretty cold. And usually, it's not like that, right? So…
Mikołaj Świątek 00:02:38 Well, we're having one of, like, the… first real winters, I think, in a good couple years.
Like, right now, I think it's, like… well, right now, you know, it's already dark outside, so it's probably, like, minus 8 Celsius or something. Wow.
I mean, that's not so bad, like… So bad, in my opinion, starts at around minus 20. At minus 20, I start, like, you know, this is… this is a level of cold that… that is actually detrimental.
to serious things. Like, if it's minus 20, I have to go outside and, like, make sure… make sure there's no ice under my heat pump, because… Because it starts becoming dangerous to its operation.
Quality.
Right now, it's not too bad, it's just, like, it's like… During the day, if it's sunny, the top of the snow just melts, and then it refreezes, so you get these, like, really unpleasant, icy surfaces everywhere.
Hey, Benet, I see that you're, you are a topic on the agenda.
Benedikt Bongartz 00:04:02 I started typing.
Mikołaj Świątek 00:04:04 It's true.
Benedikt Bongartz 00:04:05 Then my browser froze.
Mikołaj Świątek 00:04:08 What… do you want us to discuss you, Benny? You know, we can do that if you're really interested.
Benedikt Bongartz 00:04:14 No, so I was actually curious… give me one second, I will close the door.
I was curious on this breaking change with the semantic conventions and the orchard cementation.
I wanted to bring up this topic and just discuss some thoughts, Give me a second…
Mikołaj Świątek 00:04:35 And let's, I don't know, that… that's… Jacob say anything?
I'm sorry, but I'm laughing, but I just looked at my company Slack, and we are now at build candidate number 12 for the most recent stack release, so… It's been a long journey for this one.
Benedikt Bongartz 00:05:08 Yeah.
maybe start with something else, because it takes a while until I'm able to open…
Mikołaj Świątek 00:05:14 Okay, let's do… let's do the… Those are the feature gates.
I'm gonna… I'm gonna try and share my screen. I am feeling adventurous today.
Let's see.
Benedikt Bongartz 00:05:27 I think Pavel added also something to the list.
PL Pavol Loffay 00:05:32 I'm below your phone.
What's that?
Mikołaj Świątek 00:05:34 Yes, shit.
PL Pavol Loffay 00:05:34 Discuss it as well.
Mikołaj Świątek 00:05:36 Yeah, do this?
Benedikt Bongartz 00:05:37 first? Alright, yeah.
What if…
Mikołaj Świątek 00:05:40 I wanted to do… I wanted to do this, I wanted to do the future gate stability before, because that's, like, a fixed point If there's anything here that we should be doing anything about.
The Golang flags is… this is Jacob's, but… It could probably… it could probably become, like, stable reasonably fast, like, it's safe, it's been in beta for a while.
Benedikt Bongartz 00:06:12 Didn't we last time just already agree that this might be stable?
Mikołaj Świątek 00:06:17 I think we agreed to make it beta. I don't recall agreeing it to be stable, but maybe it's in the notes.
Hmm… Yeah, we agreed to enable it by default, but we haven't… Agreed to make it.
And this is even an issue by yourself.
Benedikt Bongartz 00:06:46 Yep. That's a problem.
Mikołaj Świątek 00:06:47 In order to stable.
It is not assigned to you, but it is by you.
Okay, so this already exists, so now you know, now you know that you have the power to make it stable. I think there's no disagreement about this one.
Benedikt Bongartz 00:07:03 Alright, yeah, we'll then follow up with this.
Mikołaj Świątek 00:07:07 Yeah. The MTLS one, no.
Because I keep seeing bugs being fixed around this.
And if we enable it and it has bugs, it will affect literally everyone.
This, no, because this one's probably gonna go… gonna be removed after this is configurable.
Hey, Antoine?
atoulme 00:07:31 Hey, buddy.
Mikołaj Świątek 00:07:34 Yeah. Default config should have already been deleted, according to this.
thing here.
Now, let's see who did this and didn't follow up.
Who was it?
Where is this?
Oh, it was actually an external contributor, not one of us, so I guess now I feel bad?
And we only had an issue to promote it to stable, we didn't have an issue to actually, like… Yeah, I did say this, and… Oh, there is a pull request doing it, we just ignored it? No, there's an issue.
I'm… I'm sorry, I'm jumping through this, like, list of… things being done. This isn't really a big deal, I just want to make sure that we're, like.
Yeah, and so this person simply forgot to reopen this later, oh well.
I'll take care of it. So this is… this is fine, it's actually kind of tracked, so that's okay.
Do we have anything else?
The network policy… stuff.
Bravo.
Should this go… should this go to beta at some point?
PL Pavol Loffay 00:09:14 Remind me, the beta enables it by default, right?
Mikołaj Świątek 00:09:19 Yes, yes.
PL Pavol Loffay 00:09:20 I think there might be one more issue related to the Kubernetes API server.
Which I need to solve, because… before we enable it for the operator.
Mikołaj Świątek 00:09:34 Okay.
That's fine. I'm just… we're doing…
PL Pavol Loffay 00:09:38 I can take a look, yeah.
Mikołaj Świątek 00:09:40 I mean, there's not really any rush, it's just that I want to do this review every time, or every month, at least, to make sure that we're not forgetting to handle any of these future gates. I don't want to have too many.
in the application.
Oh yeah, that's it. Okay, so Benet.
It's your topic.
Are you ready, or should we do the next one first?
You're muted right now.
Benedikt Bongartz 00:10:17 I'm opening, but do the next one first, and then I will… Then I'm ready.
Mikołaj Świątek 00:10:23 So, bravo?
PL Pavol Loffay 00:10:26 Yeah, I… One item on the agenda is to talk about the instrumentation V1 Beta 1 CR, so there is a pull request opened. What it does, essentially, it… exposes the entire declarative config, in the… in the CR.
What I find out is that the declarative config is only supported for a couple of languages.
I think it supports… Java supports it, I think Golang and C++.
And we support more in the operator, so… I'm not exactly sure what we should do at this point.
I was talking to Jack, Jack Barrett, he's working on the config. He mentioned something in the lines, like, we can start and kind of support the only languages that really support declarative config.
In the V1 Beta one.
Honestly, I'm not sure if I like that approach, That's one point, and second point… It feels kind of… complicated the declarative conflict to me. I'm not sure if you played with it.
But it's… it's not trivial. I think, like, the configuration via environment variables feels… feels easier.
It's definitely more powerful, and… And flexible, but, yeah, it's… it's a bit more work for end users.
Israel Blancas 00:12:13 Yeah, so… Go ahead, go ahead.
Mikołaj Świątek 00:12:17 I just want to say that, and I also posted… wrote this in the… in the issue Jack opened, is that there's… from our perspective, there's a difference between the interface and the implementation, right? What we're talking about here is the interface, like, what is… in the CR that we're exposing to let users configure their instrumentation, right?
that's different from the implementation, which is how do we configure the instrumentation to do that? And these are not necessarily the same things. From what I understand, even among the instrumentations that do support declarative config, they don't all support the same stuff.
In the declarative config. So, this is already the case, right? That somebody can write something here, and some of it will simply not be supported, because it's not supported by the instrumentation, and we don't really have AU way of checking.
Ahead of time, right? Which goes where. Like, we would have to track every single version, like, what supports where, how, and I'm not sure that we are, like, very excited to do something like that.
We're already not excited to do it for the collector, right?
PL Pavol Loffay 00:13:29 So, maybe the way how we could approach it is to think about it as, like.
a way to configure the SDK, not, like, the D way, but, like, a way So, like, give users maybe, like, flexibility to use it, but not use it as kind of the default thing.
Mikołaj Świątek 00:13:50 Well, so right now, the way instrumentations are configured is that we basically exposed some fields. We added some fields to the instrumentations here, right? And those fields are sometimes passed down via environment variable, And that's the way… that's just the way it happens. So… It is technically maybe possible, I'm very sorry, by the way, I am being attacked by… by my dogs right now.
I don't know why they're so excited right now.
Thankfully, they're not… they're not excited enough to show up in my camera earlier part.
The point I'm trying to make here is that maybe there… it is, like, an alternative.
of a configuration, let's say. But, like, the… our front end, as it exists right now, is already kind of arbitrary. Like, we have some fields that let you set, like, I think… propagators they let you set, or something like that, and this already exists, and why does it let you set this and not something else? It's kind of arbitrary, right? I don't… at least I'm not aware of, like, any…
PL Pavol Loffay 00:15:08 I mean, I created the CR, I can talk about the principle that we took. I think at the time, we looked at the environment variables that were supported by the SDKs, and we took all of them, I think, pretty much. So the… the propagator… sampler and exporter, I think only that, and we made those fields as, kind of, the… the… the… we made them… we expose them directly on the CR, and everything else could be then, kind of.
Additionally configured through environment variables.
jea 00:15:48 Oh.
Mikołaj Świątek 00:15:49 So I'm wondering if it's not like… Should this be an alternative? As in, should being able to use the declar… because you… have you, like, manually mirrored this, or have you taken the spec and generated from the spec via some…
PL Pavol Loffay 00:16:09 I generated it from the spec.
Mikołaj Świątek 00:16:11 Okay, so that at least is nice. That works, that's nice.
So, in principle, if you have an instrumentation that supports the spec.
Then we can just let the user Put it in the spec.
Maybe they want to, maybe they don't, right? But let's say they put in the spec, then we just write the spec to a file on disk inside a container, and that's it, right?
And we don't really care.
We're not involved in the question of which of these features are actually supported or not for the given, like, instrumentation, for the given version, and so on, right? That's the idea, it's the idea of the declarative config, for us to do this.
And this will work.
PL Pavol Loffay 00:17:02 I think what we should mention is that the… in the SDK, you either use the declarative config, or you use the environment variables, and you can't override the declarative config with environment variables.
that doesn't work. I know it sounds crazy, but it's… I think that's how it's implemented. So if we decide to support the declarative config.
than if users… opts in to use it, then we would… just use that config, nothing else, pretty much. So maybe what we could do is… in the instrumentation CR, Have the… embeds the config as an alternative to the config that we already have.
Actually, it gets more complicated because it's alternative to only some fields of the instrumentation CL, right? It's the alternative to injectors, not injectors, the EV sampler.
Propagator, exporter.
Mikołaj Świątek 00:18:11 So…
PL Pavol Loffay 00:18:11 more fields there. So maybe I was thinking, like, okay, we will have it as an alternative. If user sets it, then we… don't propagate those The exporter, and so on.
Or maybe we could have, like.
Maybe user could specify it as well, maybe as a config method.
And it will just propagate it to the… To the final workload.
Mikołaj Świątek 00:18:37 I hate config maps because they're namespace.
PL Pavol Loffay 00:18:42 Yeah, we would need to do the cleanup and propagation.
Mikołaj Świątek 00:18:47 Excellent.
PL Pavol Loffay 00:18:48 Different.
Mikołaj Świątek 00:18:49 Yum.
PL Pavol Loffay 00:18:50 Actually, no, we could, like, load it in the operator, and then just put it on the file system on the workload.
Mikołaj Świątek 00:18:57 I guess, I guess we could, we could just manually read it. But I like the idea of, like, since this is a spec, I like the idea of having it be actually properly declarative for us.
As well, like, it's a nice benefit that we can actually statically guarantee that the format is correct.
So I wouldn't want to lose that, necessarily. But, The question is kind of like this.
So the… Config is… Over… overarching, in the sense that it's an alternative to literally every other field that we have on instrumentation, pretty much, right?
PL Pavol Loffay 00:19:47 Not every other, because we have more stuff, we have stuff related to this, to Kubernetes.
Mikołaj Świątek 00:19:52 Okay, but I mean, like, in terms of… in terms of the, like, the configuring the… the instrumentation.
Yeah. Right.
Right, so you… you're not… we're not going… if somebody… if somebody wants to set an endpoint, and they want to set an endpoint, right, they either set the endpoint through… at the endpoint field, or they have to set it through the… in the declarative config. Like, these are the… like, there's no option where one really, like.
goes to the other. So maybe, in that sense… in that case, the question is.
do we want to keep the older config? Because we can… if somebody puts in the, like… or rather, maybe the question is this.
Let's say… let's say we… do this. Let's say we use the spec, the declarative config. Are we able to take it and extract the environment variables that we currently set from it, like, extract the values.
And just set those as environment variables, if it's an instrumentation without support for the declarative config.
PL Pavol Loffay 00:21:02 Most likely, I would say.
Mikołaj Świątek 00:21:06 Because that's what I mean when…
PL Pavol Loffay 00:21:07 It should contain… it should contain everything that we… we have, right?
Mikołaj Świątek 00:21:11 Yeah, yeah.
PL Pavol Loffay 00:21:11 But maybe… but maybe, like, if you express your configuration in a declarative config, we will not be able to replicate it via environment variables. We will.
Mikołaj Świątek 00:21:23 Well, not all of it. Kind of. All of it, right? Not all of it, yeah.
So, the question is then…
PL Pavol Loffay 00:21:32 We have just subset, that's it. We have subset at the moment, and declarative config offers you much more flexibility.
Mikołaj Świątek 00:21:40 Yeah.
PL Pavol Loffay 00:21:41 So then people could complain, like, hey, I said this kind of custom thingy in my decorative config, and it's not kind of… Reflected in the instrumentation in my work.
Mikołaj Świątek 00:21:53 Yeah, it would be, it would be, misleading.
But you didn't want to do this… to do the… to… to have… Some instrumentations support this, and others support the current state, right?
PL Pavol Loffay 00:22:11 Ideally, no, but the situation is different, like, the… as I mentioned, declarative config is not, supported for all the instrumentation, so I think we should think about… either… being alright with that fact, and only support the next version of CRD for subsidy languages, or have a hybrid approach where we kind of keep what we had, but as well enable declarative conflict in some way.
Mikołaj Świątek 00:22:40 Well, the hybrid approach would have the advantage that it wouldn't be a braking change at all, right?
PL Pavol Loffay 00:22:46 No, but yeah, at the same time, I would take that opportunity to kind of clean up our CR. Like, there is confusion around, like, export or endpoint, it can be said as gRPC and HTTP and… some instrumentation libraries default to HTTP, some gRPC, and I think it's a bit confusing.
So I would definitely change something in the structure that we have right now.
Mikołaj Świątek 00:23:11 So I would… I would… I suppose the question I would like to have answered, and I don't think we're gonna answer it right now here.
is… what is our intended end state? Because we're talking about this in the context of making instrumentation beta, right?
If the end state is the… is that we only have the declarative config in, like, V1 in the stable version, if we only have declarative config there, and we want to get rid of the attributes that we have right now.
then we probably shouldn't make this beta, then we should make it, like, alpha, alpha 2, right? Because the intent is to make another breaking change when we drop the existing.
the existing attributes, and only leave the clarity config once all the instrumentations that we support support the clarity config. And in that case, we would do something like alpha 2, and in alpha 2, we would have both.
And you could do either or. If you tried to do both, we would error.
And, you know, it's up to you, and we would, if somebody… we could even make, you know, we could put it everywhere and just say that, okay, for this instrumentation, it's not supported, so if you try to set it, we will, you know, reject you at admission and stuff like that. But it would be understood to be a… transitory period, and the moment we can switch to only declarative config, we would. So that's, like, one option I see. And the other option is that both is the intended end state, in which case we can go to beta and just kind of evolve them separately, but I'm not sure that's something we actually want to do.
Does that make sense?
PL Pavol Loffay 00:24:54 I think it makes sense, but it's still alpha, beta, there's no much difference, so we are not moving to B1, right? If we were to move to B1, then we should kind of have a clear understanding what is the end state, right?
Mikołaj Świątek 00:25:10 Yeah, yeah, but… but what I… I don't know, like, to me, to me, going to beta would imply that we think we are feature complete, as in… and we think that we're not going to be making… a lot of breaking changes anymore. If we know we are making… going to make a big breaking change, I think we should keep… keep ourselves at alpha and just, like, document this somewhere. Like, if we… if this is, like… the plan is to do this, then there should be, like, a pinned issue on top of the repository saying, this is the plan, these things are gonna go away eventually once we can. You know, that's why we're at alpha.
And they're gonna go away when we move to beta. That's how I would imagine this process. If that's… If that's what we want to do. I am… if that's what we want to do.
It's not necessarily what we, like, have to do, right?
PL Pavol Loffay 00:26:00 I want to do two things. I want to clean up the existing instrumentation, especially the endpoint problem.
And… introduced the declarative conflict.
Mikołaj Świątek 00:26:12 So you would like to do both?
PL Pavol Loffay 00:26:14 Yeah. Do some… do some braking change.
Some simplification for the learnings that we… we had.
Because it's been a long time since we released the instrumentation, and we can make it better.
And introduce the declarative component.
So I think since we can't use only the declarative config, the only way forward is the hybrid approach.
Mikołaj Świątek 00:26:43 That's… that's okay with me. So… so then the only question is, do we… Do we eventually only want the collaborative config, or not?
are we able to answer that question right now, or do we… or are we not able? Do we need to, like, actually try it out and release it and see… see how it works for everyone? I think… I kind of think the latter is the answer.
Like, I don't… I can't tell right now, personally, whether this is completely the right call or not.
Like, is it better to only have the clarity config, or… or is it better to have, like, a simpler way of configuring the instrumentation? Maybe the clarity config is gonna be… the implementation part, like, maybe eventually, once… like, it might be the case, for example, that eventually, if we decide to have both.
Then, eventually, the current attributes, which are right now implemented by environment variables, maybe they will eventually also be implemented via config file that we'll just, you know, generate internally for those values.
That's also something that can eventually happen, right?
PL Pavol Loffay 00:27:57 Yeah, but it's implementation detail for us.
Mikołaj Świątek 00:28:00 This is an implementation… but it is an implementation detail that will help us, because environment variables suck.
Right? We already have a bunch of problems where users are like, I wanted to set this, but these variables that you set are screwing things up for me, right? We have a bunch of issues like that.
PL Pavol Loffay 00:28:19 Yeah, there is one more thing I can talk about related to this. I was in the injector call, and… I was just curious, like, what is the current state, and… It supports a couple of languages, it's a subset of what we have in the operator.
And they… they're using this LDC load where they can manipulate the environment variables before the process, and… So, what's… I was curious, like, what environment variables they actually configure, and that's… it's only the, like, Java tool option, and… the one for Python, And… something else, like… like, only environment variables for the runtimes, I think.
Mikołaj Świątek 00:29:08 Honestly, that would solve a lot of problems for us already.
PL Pavol Loffay 00:29:13 It would solve only for the, for configuring the runtime. It wouldn't solve the problem for, like, if someone encodes the… the exporter endpoint in the docker file.
That issue would be still there.
Mikołaj Świątek 00:29:30 Yes, but, like, that issue would be solved if we support… properly supported the, Or, I, I, I guess, I guess maybe it wouldn't. Like… maybe it wouldn't matter at the end. Like, if we properly support the declarative config.
And if the instrumentation supports declarative config, then the user can do whatever they want. Like, maybe they can't do per-pod overrides of stuff, but, I mean… A.
for that, maybe a different feature is needed. And it's something I kind of also wanted to talk about if we're talking about V1 Beta 1, is whether we want to do the…
jea 00:30:10 Rule-based selectors.
Mikołaj Świątek 00:30:13 As well, in this version.
Or if we want to add those selectors to alpha first, before going there. Does everyone know what I'm talking about?
PL Pavol Loffay 00:30:25 Maybe you can show the.
jea 00:30:26 Yeah, do you want to share a screen?
Mikołaj Świątek 00:30:28 I don't actually… I'm not actually looking at this shadow, give me a sec.
I don't have this open.
Oh my gosh.
Because I linked to it in the… in the issue Jack opened.
There we go.
Give me a sec.
Alright, let me know if you can see it.
No. I can see that the answer is no.
Unfortunately, I am cursed, because I'm on Linux, so I can only share a screen once during a given Zoom session.
But I can link… the… Issue.
That I think some of us are already… familiar with.
It's basically the issue where we want to do centralized selection. So right now, if you want a pod to be instrumented, what you need to do is annotate it, and the ask is to do it the other way. So put some rules in an instrumentation object which pods to select.
jea 00:31:48 Yeah, the, the, labels.
Mikołaj Świątek 00:31:52 I mean, it's not necessarily… Maybe… it might be labels, it might just, like, the syntax might also just be, like, cell, right?
jea 00:32:01 So would be great, I mean, as long as we can do, cell-based selection in the, in the webhook for subscribing. I know that you can do it with the label selectors. I guess you could probably do it with cell, but, that's why we don't want to do, annotations.
Mikołaj Świątek 00:32:24 Yep.
But basically, like, the ask… the feature here is fundamentally just… you know, write some rules in an instrumentation CR, saying which pods should be selected.
And then we would actually apply those rules to every pod that we get in the stream.
I don't really need anything here. I don't know what the status of it is, necessarily. I just wanted to know if, like, this is something that should also, like, be around the instrumentation beta.
PL Pavol Loffay 00:33:09 I think we definitely want to migrate from the annotation.
Or the… reasons Jacob mentioned, and this is one of the viable solutions.
I don't have this strong opinion. I think… looking back at my comments, I kind of… what I don't like about this is that, like, then if you want to apply the instrumentation, you need to… Restart the bot.
Right, with the label on the part, usually people, like, you put label on the part.
Get… gets restarted, and the instrumentation is injected.
With this selector, you add it, you add it on the instrumentation, and then you need to explicitly, kind of, redeplog.
Mikołaj Świątek 00:34:10 But I think… I think that's fine. This is already the case when you, like, upgrade the operator, or restart it, or do, like, any amount of things that, like, impact. It's already… Like, for example, if you change your instrumentation configuration, it's already the case that you have to restart all of your pods before that whatever change you've made, like, applies, so this isn't… out of the ordinary, either for instrumentation or for, like, Kubernetes operators which work this way.
Like, anything that does… You know, webhook.
PL Pavol Loffay 00:34:46 Yeah, I think from…
Mikołaj Świątek 00:34:47 The webhook doesn't work like this.
PL Pavol Loffay 00:34:49 from this standpoint, it unifies, when the update is propagated, so I think that's… that's a good… Good approach.
Mikołaj Świątek 00:35:04 Do you have, Pavel, do you have, like, because this, this is… you have a PR for this… Hmm… For the declarative configuration.
We do have, like, we do have an issue for it to open by David Ashpole.
So I guess the question now is… how to apply it. And I think the only possible answer, it sounds like, is to do both.
Just, like, keep what we currently have.
And… and add the declarative config as an… as an option.
PL Pavol Loffay 00:35:48 Yeah, yeah, exactly.
And we like… To be time-safe, so… we would probably expose it directly in the CRD, not as a comfort map.
Mikołaj Świątek 00:36:01 Assuming it's stable, right? Because there's… if…
PL Pavol Loffay 00:36:05 It's not, actually. It's not all the parts that you are stably.
Mikołaj Świątek 00:36:10 Because there is this problem, right? This problem is… the problem is that if we're… if you're generating it straight from the OpenAPI spec.
then… Like, it's enshrined in our CRD. They make a breaking change, we have to make a braking change.
Maybe we don't really have a choice.
And the other option is not even about breaking changes, but it's the same question as what we had with the managed CRD.
for… For exporter configuration.
It's like, let's say they add a new feature to the spec.
Right?
Like, there's gonna be… a… like, either we'll have to be quick adopting the new spec version in our CRDs, or we're gonna have users yelling at us to update what we have in our CRD if we're gonna fall behind.
And the question is kind of, are we okay with that? Does that spec change very often? If it doesn't change very often, then maybe that's not a problem.
jea 00:37:26 I think, I believe declarative config is, 1.0, right?
So ideally, it shouldn't be changing that often.
PL Pavol Loffay 00:37:38 I'm actually not sure, but I'll double check.
I think it's, like, a candidate, maybe, no?
jea 00:37:44 Oh, if it's at candidate…
PL Pavol Loffay 00:37:47 RC3.
Yeah, C++ supports RC3.
Mikołaj Świątek 00:37:59 I would say that it should be stable before we, like, release a CRD with it.
But that doesn't stop us from actually, like, implementing it.
Right?
PL Pavol Loffay 00:38:14 Yeah, in December, it was released, the RC3.
So I think it's not far from… from being a stable.
jea 00:38:24 Well, yeah, but Collector's been close to a V1 for 3 years, so… I don't want… I don't want to put too much weight on, on an RC.
Mikołaj Świątek 00:38:36 I would say, like, that doesn't actually stop us, but we, as long as, in my opinion, as long as the… As long as it's not stable, then our field should be explicitly marked with, like, big warnings that this is not stable.
So use at your own risk.
PL Pavol Loffay 00:39:01 I mean, we would spin it to RC, and then if there is a new version, we would need to kind of deal with that change, like, maybe release new API version.
Which is probably a lot of work.
Mikołaj Świątek 00:39:12 I would really like to avoid doing that.
Like, unlike, you know, the spec can do whatever it wants, we are kind of bound to the Kubernetes conventions for API stability.
Right? So we're not actually allowed to break things, even if we, like… nicely document that we're doing it. Like, we're only allowed to break things by releasing a new CRD version.
Which would be a… pay.
To do, indeed.
And anytime there's, like, a new release of this in the future, we would also have to do a new release of… If there's, like, breaking changes in it, right, then we would have to do the same dance, Again. Which, if there's not a lot of them, then maybe that's acceptable.
Right? But… I wouldn't… But I don't… I also don't know what the alternative is. The alternative is the same thing that we did for Collector, right?
For the collector, we used to have just a string field, and it kind of sucked.
PL Pavol Loffay 00:40:31 Yeah, I mean, if we go with the string field, maybe it's better to, like, source it from a config map, and then, at the injection time, just dump it into the pod file system, so we don't have to deal with the cleanups.
And maybe this is fine for the, like, V1, Alpha 1, and C until it's stable, and then once it's stable, we would kind of embed it in the CR.
maybe this could be a good path forward, like, I want to do the cleanup of the current version, so maybe we should bump to the B1 Beta 1, do the cleanup on the endpoint, and other stuff that we can do.
And introduce the… the config, source the declarative config from the config map, and once it's stable, we would deprecate that field and have it embedded directly in the CR.
Mikołaj Świątek 00:41:22 Yeah, in that case, we would start, like, we should name the field appropriately from the start, right? It should be named, like, you know, declarative config raw, or something, right?
I don't like config maps around instrumentation because of the namespacing problems, and even if you, like, read it and then, you know, write it directly into the pod, you still have to have, like, permission to read a config map in some… Namespace somewhere, which may or may not be, like, an ideal thing to do.
So, I would rather avoid that. I am not… I'm okay having a text field, personally. I'm okay having a text field with, like… I'm also maybe okay having a config map, but I don't like… Promoting that as the… That's the only way of doing it. I am perfectly fine having, like, a text field where… which is called, again, like, declarative config raw, where you can stick the config, and if you do, we're going to ignore everything else and just use that.
And once it's stable, then we can add declarative config.
without raw, which is gonna be structured as it should be. We can even do an automatic conversion for people at that point.
But we can… we can add it, and we deprecate the raw field then, but we can do that without, without, like, having to do a new CRD version.
PL Pavol Loffay 00:42:56 Yeah. We're just adding things.
Yeah, I like this. I think it makes sense. It's the most sensible thing that we can do now.
So, maybe to move this forwards, I would… Open a new pull request to… DB1 data1 that will have the cleanup without the declarative conflict, because it's going to be easy to review and merge, because we are familiar with the structure. And then… Add the declarative config as a raw field on the CR.
And work on the reconciliation, and it's… Yeah, and the kind of…
Mikołaj Świątek 00:43:42 We can, we can even… We can even do… we can even add the declarative config to V1 Alpha 1 if we really want to, but I don't think we want to.
just remember that the main thing… one of the main things we want to do in V1 Beta 1 is to switch from annotations to… to labels, like, that's, like, the big… the big ticket item.
Read this. Okay.
So, anyone else have opinions about this? Because it's mostly, like, me and Abel talking thus far.
jea 00:44:15 I think, right now this feels a little abstract, and once you… once there's more written out, I'll review, but nothing that's been said has been… uncontroversial… has been… nothing that's been said has been controversial to me.
I think that anything that we do to bring us closer to a world where, you know, we kind of just wrap the declarative config and the injector is going to be good no matter what. Implementation… is gonna be sort of side… like, an aside to that, right? I think as long as we move to a labels approach and then give people, like, a good exit hatch, which has always been our strategy, you know, I think that that's… that's the right way forward. But I think without, like, re… I haven't been able to read too much on this right now, but… what's that?
Nothing that's been said so far is anything I disagree with, so… Definitely, I think once we come together… are we all going to KubeCon? Is all five of us?
Yeah?
Paul, will you be there? Yeah.
PL Pavol Loffay 00:45:21 Yeah.
jea 00:45:22 We should definitely book some time, at the, like, observatory for, like, a real in-person SIG, and we should come prepared with this as sort of, like, the main event for our discussion, and come with, like, some YAML files to touch and look at.
I think that'd be a good use of time. So it's tactical, and we can kind of get together on review.
For what that should be.
Yeah.
That's all… that's… that's all I got.
Benedikt Bongartz 00:46:09 If we have some time left, I would like to… jump on the other one, about semantic convention and basically how we want to upgrade those libraries.
The thing is… I was reading this… I guess it's not a third issue or something that was opened up, and it seems like everything goes in circles.
how to overcome this issue. There was this proposal with this, Environment variable, which might be implemented to… Stay on something, on a semantic version that is supported, but as far as I understood, it's not supported by every SDK, so it's just a few.
Somewhere here it was mentioned that JavaScript didn't have a breaking change.
Well, I wonder, because they should also follow the semantic conventions of HTTP, and if HTTP has a breaking change, I would expect that JavaScript has it too.
And one guy…
Mikołaj Świątek 00:47:07 Sorry, even if there was an environment variable for it, I don't think that would help us very much. Like, would that make anything simpler for us?
Benedikt Bongartz 00:47:18 partially, so we could give the user the option on the CRD to set a specific semantic convention version.
So, like, you would go and say, stay on one.
to X, basically the semantic conversion version that is used in 1.2x, so you don't upgrade, you can go further with your library, use the new instrumentation, maybe a new framework that got picked up, or… Some new version of a framework, so technically your instrumentation would work, but you transmit the old semantic convention versioning.
Mikołaj Świątek 00:47:50 Yeah, but that's, like, I would imagine… I would imagine the instrumentations wouldn't want to maintain that variable forever and ever, so at some point, you would get back to the same problem of, like, some version just basically breaking stuff.
Benedikt Bongartz 00:48:03 Yes, and there is another thing that you mentioned, for example, which… let me share… Which was here.
Is it this one? Could we simply automatically upgrade users?
No, it was here somewhere. So that, at least, you mentioned that, With the auto-instementation, not all your workload will be upgraded, which means you do this somehow.
And then there's chaos.
It depends when the workload gets reconciled.
Mikołaj Świątek 00:48:38 Yes.
Benedikt Bongartz 00:48:39 And, So I was wondering if it could make sense to add some kind of component, I think I mentioned this in the other issue, in one of them.
to provide a collector instance which can do the upgrade path for you. I think currently the schema processor is in development, I looked into this a bit.
But in the long run, that you can specify the semantic convention versioning that you would like to export, and we can do an upgrade or a downgrade for the user, and we don't really… Care much about this one.
It's, like, just, we need to provide the semantic… the YAML to upgrade and downgrade.
And an extra service, that's the downside.
Mikołaj Świątek 00:49:24 This is something that I would expose as some kind of… either I would put this, because this is a, like, the fact that we're blocking upgrades doesn't help anyone to actually deal with the breakage, necessarily. Like, it just informs them that there is breakage.
And this, I feel like, is a way to try and tell them how to deal with the breakage, because this potentially deals with it. Like, you put a schema processor somewhere along the way, and And it does the thing for you, at least until you're actually ready to deal with the change to the shape of the data that comes from the semantic convention break, right?
I… maybe it's… it would even be reasonable for us to, like.
Offer some kind of attribute on the instrumentation, which would do… spawn an auto collector for them, and do this.
I would not do this automatically without, like, any indication that it happened. I am not in favor of spawning hotel collectors for people, like, without any say-so.
on them.
Benedikt Bongartz 00:50:39 No, it was more like, if you go to the CR and you pin this to a specific version, we will transform this into the… Specific version, if you don't pin it to a specific version.
to go on your own, but then we can go forward with breaking changes, so if you want to avoid a breaking change, use this option. If you don't want to.
This would also help with migration, so if I don't want to upgrade now, I could switch this on.
And then just upgrade my instrumentation.
And at some point, I can change this, remove this container again.
Mikołaj Świątek 00:51:15 Yes, that… that's re… I think that's very useful.
It also sounds difficult, at least to me.
So this… this is, like, like, this is not a solution, necessarily, I would say. It's, like, part of… a solution, because… If you just add this field that lets users do it.
it… that doesn't, like… that doesn't let us just bump those versions, right? We will bump those versions, the field will default to off, and they will have breakage.
Because of something we did. So… it… it has to be something… either way, they have to do something. It's just a question of, like, how complex the thing they have to do is.
Benedikt Bongartz 00:52:01 Then there is another thing, so here we are super concerned in moving forward, because we break, potentially, the odd transmutation of people already semantic convention.
But with the collector, I think we never cared, right? So if, for example, they renamed…
Mikołaj Świątek 00:52:16 We care somewhat. Like, there's some breaking changes in the collector that we've, acted to automatically resolve.
For example, when there was this change going from, like, the… telemetry endpoint to the metrics reader. There was a lot of pain involved in that, but we actually did something.
Benedikt Bongartz 00:52:34 Yes, no, but what I meant was more with the semantic convention, so if you use, for example, the, not node exporter, what's the equivalent, the receiver to collect CPU metrics, system metrics, and so on.
Mikołaj Świątek 00:52:54 I know what you mean, I understand, yeah. So the collector, from its receivers, emit different data, and we don't care about that.
Benedikt Bongartz 00:53:02 We had also semantic, versioning changes. And I know that there is now, but this seems to be recently.
some… Can I share this here?
Mikołaj Świątek 00:53:15 This is almost recently, so that they started with semantic conversion migration in the collector itself.
Benedikt Bongartz 00:53:21 This is end of December 2025. So until now, when we upgraded there, we also eventually broke a dashboard, because we didn't really care much.
Mikołaj Świątek 00:53:31 Yes, but I think that's fine, in the sense that Collectors are easy to roll back.
If you want to.
You can have some… you upgrade, and you will immediately see that something broke for you, like, because the collector will just get, you know, there's gonna be a rollout of the new version. And you'll immediately… something breaks, and you say, whoops, rollback.
And then you can try and figure out what the hell happened.
So I am vaguely okay doing that.
like, with instrumentation, I'm especially… Careful, because with instrumentation, you can deploy, right? And then nothing happens, nothing happens, absolutely nothing has happened. Three hours later, some application, some pod gets recreated for some whatever reason. It can happen for all sorts of reasons in Kubernetes.
And suddenly, you have breakage, and you have no idea how that's related to anything you've done recently. So that's, like, the… the pain that I wanted to save. Like, if it was obvious, if it was obvious immediately upon operator upgrade that something's broken, I wouldn't care that much.
Does that make sense?
Benedikt Bongartz 00:54:45 Yep.
Does it make sense, then, to… Just create events when workload gets upgraded, so that you get somehow informed.
Mikołaj Świątek 00:55:01 M… among other things, like, what I wanted to do was to do this, like, or rather, I wanted to create events about the upgrade being blocked, but we… we can… we can create events about… about upgrades. I'm not sure if that's gonna help, though.
Benedikt Bongartz 00:55:19 No, just in case of a breaking change, so, and then your workload gets upgraded.
So that you are aware, so that if something breaks, you can see at least, the recent event is that some auto transmit mutation got upgraded, because it was rolled out.
In another way.
Mikołaj Świątek 00:55:37 Are we able to do that, technically?
Benedikt Bongartz 00:55:41 Good question, we have no registry which tells us which workload, which part is instrumented where.
Mikołaj Świątek 00:55:51 we don't have a way of knowing… right, we don't have a… we don't have a way of connecting what the instrumentation that's injected to the revision of the instrumentation that it's used, right? And we probably should.
Benedikt Bongartz 00:56:05 Technically, it's something which is just something we can put into the webhook and then have some kind of registry.
The question is how to persist it, but we could just use a config map or something.
Mikołaj Świątek 00:56:19 We could just put, like, an annotation on the pod, I think, that's, like… That's what annotations are for, I think, origin.
Yeah, so this is something that we could do, if it's… sufficient I'm not 100% sure at the top of my head.
But it would help.
Benedikt Bongartz 00:56:41 Because I was really, like, depending on the receivers that we have.
we break this right now, so you just jump from one version to another, and then CPU system metric was renamed.
And also there, it's… They had an option to enable and disable the old naming or the new naming, and there was some phase to make this change.
But from our end, we didn't really care. It's… Similar to, like, you can set an environment variable in the RTransmitation to remain on the old semantic convention.
And we would just mention it and go ahead.
Mikołaj Świątek 00:57:22 Yeah, but for… currently… currently the instrumentations where this is a problem are Java and .NET, and Java and .NET don't let you do that, I don't think. Java actually has a major version… a major version change, like, there's a V2 out there.
of Java.
And .NET doesn't let you change that, I don't think.
So, and in any case, like, if you actually have a problem with this, like, if you know it's going to be a problem for you, then it's like, you can just mitigate it by manually setting the version you want to be on.
Right?
Benedikt Bongartz 00:57:59 Yeah, I was curious, because, yeah, we discussed this at the observability, and we have multiple options how to resolve this, so one would be, for example, something like the schema processor or something, and you just do it afterwards, and you don't really care much what version is reported.
And that's, for example, one thing that we… Had with the instrumentation itself.
Seems like there's also an option to do this in the backend, so I was looking into PremiToys.
So they have here… this proposal, which came out of this talk, which more or less, mentioned how that you don't really need to care or take much care, but your alerts will still work. So what they do is basically they transfer.
Mikołaj Świątek 00:58:46 Or do some aliasing in the database, which… Yeah, I know.
Benedikt Bongartz 00:58:50 Will not work if you do… Something like this, this unit change from milliseconds to seconds.
Oh, that's not supported.
And, that's why you end up then with technically something like this in your ferries, which is, again.
Not what you would like to do.
Mikołaj Świątek 00:59:11 I still think that what I'm proposing to do is, like, an easy way to kind of at least unblock the new instrumentation versions for users, like, to set the defaults. I guess we could also do what Jack said in that issue, and just, like, don't set the default at all.
and just say, user, figure it out for yourself, which I have… I don't like. I don't like doing that. I don't like doing that for the auto collector either.
Just because… But that's what we do with the collector by today.
Benedikt Bongartz 00:59:42 So that's…
Mikołaj Świątek 00:59:44 No, we don't. We have a default image.
Benedikt Bongartz 00:59:48 Yes, but what I meant was, if I go from one operator to the other one, we take the default image.
We completely ignore if there is a breaking change in the.
Mikołaj Świątek 00:59:57 No, no, no, no.
I meant something different. I meant that, like, in the issue about this, Jack Berg said that maybe we can just, like, stop setting default instrumentation images at all, and, like, require users to set it explicitly. And I don't want to do it for the same reason that we already talked about doing this for the collector, and I also didn't like doing it there for, like… similar reasons, basically. Like, I feel like that is… I am… maybe that is the right call at the end of the day, but I don't like doing things that are just, like, convenient for us, but, like.
force users to know a lot more about OpenTelemetry than they, like, maybe should.
care, right? Like, we are the experts on this stuff.
So, like, if we can't resolve certain problems, I think we should, is, like, my position, even though… even if it's not necessarily easy.
Anyway, just write a comment in the issue, Benny, and, like, let's talk it through. I like this solution that I wrote down, because it's really simple. It's actually, like, simple to implement, and it will unblock… it doesn't prevent us from doing any of the other things later, necessarily.
But it solves the problem right now, it's simple to implement, and it'll, like, it's, like, screams, it screams, like, hey, you need to do something.
at users, which I think… which I think is a good thing. So that's why I like it. I am not, like… so I'm kind of in favor of doing this just because it's easy to do, and it will resolve the problem. I don't think that's necessarily, like.
the end of the problem altogether, right? We should still kind of pursue better solutions. Like, I like your solution with the schema processor, it's just, like, more complicated and, like, more… involved to actually do that. But it would… it would also, like, it would also help, I think.
PL Pavol Loffay 01:02:01 Maybe… well, like, one issue that I see is… I think we are… Failing on delivering break free updates, because the instrumentation can break users anytime if they change semantic conventions, and we have no We have no CI at the moment, or no validation on what we actually ship in the instrumentation images.
it doesn't exist. Maybe we get hints that there is a breaking change, and we don't update the image?
But that's pretty much all about it, so we can't guarantee it.
So it can happen that we will ship something that will break users.
And if we… I don't like… Either that we delegate this Completely to the end users, but maybe it's the same thing to do, because it then clearly communicates that, hey, our responsibility is of injecting the image what you choose to inject? It's your responsibility. And if something breaks.
You should fix it. You should then upgrade, and you should keep the upgrades.
You should be careful about the upgrades.
Mikołaj Świątek 01:03:21 Okay, but A, that's… I accept that argument, and it's not like I am completely opposed. I think it's, like, a valid solution to the problem. But it's like a solution that if we decide, okay, this is the solution, we're still gonna take a bunch of time to, like, get there, just because it's a breaking change to make that field required.
Rather not have a default.
It's also a big, like, it's… right now, we essentially own the instrumentation images. Like, the instrumentation images don't really even have a release process in this traditional way, right? Whenever there's a change, and there's a bump to the versions, we just make a new image. But the only way you can discover the images is by looking at the packages we publish.
On GitHub. So, if we want to say that, if we want to say, hey, user, this is up to you, then we have to make all of that stuff much more discoverable and, like, much easier to understand what it means that something has this version or not that version. And that's, like… my point is that this is a bigger problem.
It's, like, a much, much bigger, more serious problem to make these instrumentation images into, like, their own releasable artifacts.
I, I suppose.
PL Pavol Loffay 01:04:37 I, I, I think they, they, they follow the… The auto-instrumentation version.
And then… If we publish the default CR with images into README, we could perhaps set up the GitHub action to update the version when there is a new image version.
And have maybe better links in the README that will point to our package for given instrumentation image.
Mikołaj Świątek 01:05:07 There is, the auto-updates already exist. Renovate does it? So… that's already in. The problem is that there's no, like… We release a new ver- the only thing we do is we say, hey, this operator release has this version by default.
But… There isn't, like… There isn't any real documentation for it.
like, what they… okay, which… what Node.js instrumentation versions are.
PL Pavol Loffay 01:05:36 Yeah, excellent.
Right, exactly.
Mikołaj Świątek 01:05:38 It basically doesn't exist. Like, what… let's say I want to make my own.
Node.js instrumentation image. How do I do that? Like, what are the requirements for it to work? Like, that's not actually published. I know users have done… some users have done this anyway, right? They basically took our images and modified them, but, like, we don't publish anything. So if we want to make these images into… if we want to tell users pick and be responsible for your own fate, then we have to make it possible for them to, like, actually know what's published, like, what is, what are the promises given for, like, any given image, and so on, so that's, like, a bunch of work.
PL Pavol Loffay 01:06:22 I think those are two different… issues. One is issue, like, how users discover those images.
that we build, and the other issue is… For other use cases, do we… Supports.
Users building their own images.
I think.
Mikołaj Świątek 01:06:42 Right now, we don't.
PL Pavol Loffay 01:06:44 We don't, yeah, it's sort of, like, implementation detail. I think what we should improve, if we go this route, is Actually, one step further, like, we build new image that is based on the auto-instrumentation.
And make it easy for users to, kind of.
Jump into the release notes for that package that is, you know, bundled in our image, so they can find out what has been changed there.
Because that's ultimately what people might want, right? They are not… They're interested in, like.
What has changed in the instrumentation?
Nope.
Mikołaj Świątek 01:07:25 Yes.
PL Pavol Loffay 01:07:26 Anyways, I need to drop as well.
Mikołaj Świątek 01:07:28 Yeah, yeah. I would, I was gonna say, even go further.
We shouldn't build these images, but we are right now, so that's kind of.
PL Pavol Loffay 01:07:34 I agree.
Mikołaj Świątek 01:07:35 An imperfect world we live in. All right, let's continue the conversation in the issue, okay, that I opened, or under the HTTP breaking change, okay?
PL Pavol Loffay 01:07:44 Alright, see you, have a nice…
Mikołaj Świątek 01:07:46 See you.
PL Pavol Loffay 01:07:47 You mean goodbye.
Israel Blancas 01:07:48 I'm…
