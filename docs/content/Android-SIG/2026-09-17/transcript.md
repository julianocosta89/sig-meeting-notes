SIG: Android SIG
Date: 2026-09-17
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb** 01:52 Hey, everyone.
**Jason Morris** 01:57 Huh.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 01:59 Yeah, I was…
**Jason Plumb** 02:23 So many Jasons now.
We'll give it one more minute.
Get some Embrace folks in here, in addition to Jason.
And we'll see what else shows up.
**Hanson Ho** 03:03 Hello.
**Jason Plumb** 03:07 Hello!
Okay, please feel free to add anything to the agenda that you'd like to talk about today, but we will start with, Ben's topic.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 03:31 Hey guys, yeah, so this… Basically, I saw there was an open issue for this already.
And, basically the premise is that, with our current HTTP instrumentation, every… every HTTP call in the, app gets instrumented. So, you have… if you have any third-party, SDKs, any other third-party SDKs, like, say, analytics or… you know, payments or whatever, you… you are going to instrument those, network calls, and your dashboards are gonna be, properly, like.
You'll see traces coming in for those network requests.
Which is not ideal. So this is why we put, we want to have an ignore URL, or a whitelist, or an allow list, or a deny list.
And so there was an idea proposed, to have a sampler, to do this.
But on further investigation, I found that, like, it has some limitations and, like, how it does, the filtering.
So I think we will need to do this at an instrument level, instrumentation level.
And I have a proposal that details the plan on how to do this.
I also have a first PR up, which just, provides an interface on, like, how the configuration would look like.
And, the rest of the actual instrumentation later changes are going to come up in the next PR.
**Jason Plumb** 05:14 Yeah, this table is really good. I think that's helpful.
**Hanson Ho** 05:22 Where did you read that the sampl… you're supposed to use a sampler? Because that doesn't sound like sampling at all.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 05:29 I think, like, this… it was discussed in this issue.
In some comments. I think it was one of the original ideas proposed.
**Hanson Ho** 05:43 Just to pinpoint… for it to be… well, I guess it's a different type of sampling.
But…
**Jason Plumb** 05:52 Yeah, I mean, it depends on what the goal is, right? The goal is… I mean, the whole intent of the sampler is just to not do a thing, right? Like, oh, we're making spans, oh, not this time, I don't want a span. Like, that's… Seems… smells like sampling, but if the goal is to also not include Propagation sometimes, which is what's in this table.
And metrics, right? If you also don't want to include that in your metrics, for some reason.
But that also makes it harder to reason about, maybe?
**Hanson Ho** 06:24 Is the instrumentation just too heavy-handed? Basically, you install it on a, on a, on a particular client, specific HTTP client, OKTP client, and it just does everything. Like, does the instrumentation need to be configurable?
Or… Is the proposal… kind of, like, adjacent to that, but effectively looks at the internals? Or does it look by semantic conventions and then deals with it that way?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 06:58 Sorry, are you asking, like, why we need this, Altogether, instead of, like, having, configuring something per HTTP client or something like that?
**Hanson Ho** 07:12 No, I'm wondering if the instrumentation itself is just too blunt in the way it's applied, and whether there should be a configuration for the instrumentation itself that basically narrows its application.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 07:29 That is what this is trying to do. I, I think how we have it is, is… Because this is auto-instrumentation, it's, it's, it works really well, it's, it's easy to… integrate. There's not a lot of developer effort required.
And this sort of configuration, Would be the minimum… like, would provide a better developer experience in terms of… in terms of minimal integration work, and, like.
Minimal configuration.
So, so we have the auto-instrumentation, and this is the other side that would, you know, provide some sort of configuration and allows certain host only to be instrumented.
**Hanson Ho** 08:14 Okay. Let me maybe read this first. I was expecting the change to be in the actual instrumentation itself in Contribs, and not in the Android. So, yeah, let me take a look at… sorry, I should have… Before commenting, I should have read the whole thing first.
**Cesar Munoz** 08:32 Sorry, man.
**Jason Plumb** 08:32 So the…
**Cesar Munoz** 08:33 Ravian.
**Jason Plumb** 08:34 Go ahead, Cesar.
**Cesar Munoz** 08:35 Does I have a question, so that you're, you're… that… Ideal scenario that you're mentioning is for the solution?
would be targeted per instrumentation. Is that… is that correct?
Or, like, phase that affects HTTP-related instrumentations within OTA Android.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 08:57 That is correct.
The latter, like, just pure.
**Cesar Munoz** 09:01 Got it.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 09:01 related instrumentation in Android.
**Cesar Munoz** 09:05 So, any other, like, You know, custom instrumentation of… other HTTP clients or things like that, that will be ignored by these, functionality.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 09:20 Yes.
That is a call. We just want, or OKHTTP instrumentation. This targets both OKTTP instrumentation and the HTTP URL.
Connection.
**Cesar Munoz** 09:34 exit. Got it.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 09:35 Yeah, so, that's… those are the only targets.
**Cesar Munoz** 09:41 Well, I guess it's fair to say that those are probably the only targets in most apps as well.
So… Yeah… Bathing is fine. Usually, I… I… I… I… I would like to have a, like, a… global… tool agnostic.
Knob for this kind of things, but… it also depends on the… on what's needed, right? So…
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 10:12 I guess it's because, like, this is the existing instrumentation that we have, and if we have more instrumentation, I think, like, we need to add support for each instrumentation on a case-by-case basis to respect this configuration. This configuration can be global.
But each instrumentation would need to read the configuration and, like, respect that, and that is a per-instrumentation work.
**Cesar Munoz** 10:44 Got it.
By the way.
**Jason Plumb** 10:46 Yeah, the original…
**Cesar Munoz** 10:48 Just wanted to say one last thing. The API that you mentioned looks quite similar to the instrumentation API from from upstream, which is… I think it's used under… underneath the, For, at least for the OKHCCP… instrumentation.
So, I don't know, just in case that can help. But yeah.
Sorry, go ahead, Jace.
**Jason Plumb** 11:14 Yeah, I wanted to kind of come back to the original description and the use case, because this says kind of two things, right?
Ignore URLs matching a pattern from being traced. So, really, I think this means, like, prevent the URLs mentioning a pattern from being traced by HTTP, like, don't generate a span for those.
But it also sounds like we've interpreted that to mean, also, don't pass… trace context. Like, don't… don't propagate.
And then there's also this, if the URL is ignored on the client side, the server should also get the knowledge that it was ignored on the client, which is weird, because if you're not tracing, and you're not propagating.
you still want the server to know that you did those things? To me, that's… that's a very strange use case.
I think I know what that's born out of, but I… it's weird to me.
**Cesar Munoz** 12:10 Matrix?
**Jason Plumb** 12:13 I mean, metrics aren't mentioned in here at all, but they are mentioned in Ben's table.
**Cesar Munoz** 12:18 Because I guess that's one way to still let the server know that there were some ignored.
Traces.
**Jason Plumb** 12:25 How would the server know about the metrics?
**Jason Morris** 12:28 Well, you're assuming that they're talking about the same server in both instances.
**Jason Plumb** 12:36 Help me understand that.
**Jason Morris** 12:37 So you want to block the instrumentation happening, or the telemetry being generated for requests going to your analytics service, but you still want to know that you dropped those on the floor. You want to know how many of those happened on your own, you know, internal services.
**Jason Plumb** 12:56 I see what you're saying. Yeah.
Yeah, so, I mean, that… that could… we… I mean, you could… the naive approach might be to just make a counter that has some attribute on it, right? Yeah.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 13:12 Yeah, that, I… I've ignored that second, point for this change. I think that can be… A separate independent chains, So that's… that's why it's not in scope for this, the proposal I've made.
But, like, story, was there a question regarding, like, if… We want to maintain the trace injection, but not, not, like, have more fine-grained control on what we do here.
Rather than, like, completely excluding a certain host, or, like, including certain hosts.
**Jason Plumb** 13:53 Yeah, my question is whether it's important to not do trace context injection.
Our propagation. Which, in the case of a client-side app, is usually pretty weird already, right? Like, we're not in the middle of a call chain. We're usually the originator of a call chain.
Right? So, by sending, trace context, that's saying, hey, here's the trace that we're part of, and it's almost always the root is going to be in the client somewhere, like in the Android app somewhere. It's gonna be the root span. But if we're inhibiting or not sampling those the way it's supposed to work.
Is that you're supposed to propagate and set the sampled flag.
Or not set the sampled flag, I forgot the… The terminology is sometimes backwards.
But I think that's the way it's intended to work, so that the server side could say.
Cool, there's a trace, and there is a span, but it has not been sampled, meaning it's not going to be included in the trace.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 14:57 Right. So, why… why this?
feature in the first place, because there could be network calls that you do not own. Even if it's your own application, it could be a third-party SDK or third-party provider making that, API calls, and You do not want to inject or trace context into that, because it's not your service.
**Jason Plumb** 15:24 But that wasn't stated as one of… I don't think that was stated as one of the original goals, was it? It was just to not…
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 15:30 H… yeah.
It was not.
**Jason Plumb** 15:33 Yeah.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 15:34 That is… that is an additional scope I'm proposing. I feel like there is a use case for that.
we… we can certainly… so that's why I asked, like, do you, stay a recent to… If we want to keep the trace context propagation, we can certainly do that, and Find, like, add more configuration that would allow, you know, okay, we can have metrics, but, like, disable metrics, but, like, trace context propagations can still continue.
If that's the case. But I would definitely… I think there's definitely a use case for You know, I, as a developer instrumenting my application, I do not want to have my dashboard polluted with metrics for a third-party, you know, service that I do not control or have no visibility into.
**Jason Plumb** 16:30 The metrics for your client-side app.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 16:34 metrics for… certain services that I… I am not responsible for, or it's a third-party service.
**Jason Plumb** 16:45 So you don't want to… you don't want to store metrics about how long the client calls take to that service, is that what you're saying?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 16:52 Yes.
**Jason Plumb** 16:57 Even if it's… I mean, it's part of your app, you're calling it, but you just want to be able to ignore those completely.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 17:02 Yeah, for example, say, some sort of analytics SDK is present in my application. I really do not want to see all the network calls that's being made. Those are not mission critical. Those do not, you know, affect my user's experience, so I do not care about them. They are more passive.
And not, not critical for my, issues.
**Jason Plumb** 17:27 Got it.
Okay.
**Cesar Munoz** 17:32 Well, what if we start with… A behavior that we can later expand.
So that, you know… otherwise, if we start with something that we cannot later take back, then that will be a problem. So maybe… I don't know, because I haven't checked. I know that this is a common use case for backend services to… keep the trace context, and… and also they… I think they also generate a lot of metrics Around this stuff that it's ignore.
And as you said, Jason, it's… It's probably not as useful for a client, since stuff is generated there.
So… I don't know how easy or difficult it is to add the, context propagation, or remove it later, I don't know, you know, which of the two, so… But yeah.
For now…
**Jason Plumb** 18:33 It kind of seems like we're talking about three things, I think. It's like.
**Cesar Munoz** 18:36 Everything's fair.
**Jason Plumb** 18:37 from being created, inhibiting trace propagation from happening, and then inhibiting metrics from being created. Like, there's kind of, like, three things.
If there's a… if there's a way to sort of tease those apart and implement them as different use cases, that's cool, I think that would be helpful.
To think about those as three separate things.
**Cesar Munoz** 18:57 And it sounds to me that the main goal is really just avoid turning spams for some HTTP calls.
And, Really, my only comment on that is that I don't know why I kind of like the idea of having a one-for-all.
not needing to maintain later, or to remember that it exists for any new instrumentation option.
**Jason Plumb** 19:27 I mean, that's… I think that is though, right, is to put it in this instrumentation common?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 19:33 Yes.
**Jason Plumb** 19:35 So what that says, I think it would be shared across multiple implementations.
**Cesar Munoz** 19:40 Well, I mean, you still have to use that API.
**Jason Plumb** 19:42 True. Yeah, you still have to do work, you still have to do this, right?
**Cesar Munoz** 19:46 But, I mean, yeah, it's… I mean, it's… I don't have the thing… the thing is, I don't have a… valid reason why, like, we need it, like, in a processor, for example. And then we, like, that's essentially… central to anything, so that… that way we don't have to remember about APIs or anything like that. I don't have a use case for that, but essentially, that's usually why… what I prefer.
But if this is needed right now, I think that's fine.
**Hanson Ho** 20:15 So this seems like an agent-level configuration that can be applied to anything the agent touches, as long as it's got a configuration surface area. Because looking at the proposal, you're… you're not proposing to mod… other than the WebSocket one, you're not proposing to modify the internals, you're just using the existing configuration Options on top.
And having a single point of entry for configuring this. And then… in how the Android agent, configures those instrumentation. You apply, these, these, these settings, basically. So you have to add, you have to change the code for OKHTTP, you know, or at least in how Android configures it, and, and, URL, HTTPR connection, etc, etc. So all of the features, with With respect to propagation, those are added one by one.
So, like, the first part you have to do is add the API. So we agree on the API surface. And then, basically, there's, like, n number of things that individually will total up to the feature. So I think we could maybe just figure out the API first.
And whether this is a good idea. And then, you know, talk about each specific point, whether or not we want to do it, how we want to do it. But the idea is that you're… you're leveraging what is already there for configuration. You're not adding new configuration. So I think, given that, you're only using existing instrumentation, configuration services.
You know, if you're allowed to do that, then… The instrumentation. Or rather, if the instrumentation lets you do that, then you should be allowed to do that.
**Cesar Munoz** 21:56 Yep. Well, Ben already suggested an API.
shape, and, and… I think as long as… I'm guessing we're not… like, I'm guessing this is supposed to be used only by our own instrumentations already, at least initially?
I would prefer that.
So that we can then… I mean, it doesn't have to be, like, the final shape of the API up front.
That would be ideal for me.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 22:32 Yeah, so, why I went with this API shape? A typical use case, I assume, would be, as a developer, instrumenting my application, I have one backend That I primarily interact with, or a base host that all my app communication, goes through, right? So, in that case, I am interested in everything, any… all sort of instrumentation for that host.
And for any other host that I do not control, I do not care about any sort of instrumentation at all.
So that's… that's why it's a very limited API surface, or a config surface with just the host. But if… if we… if you feel that, okay, more fine-grained control in terms of, okay, certain posts might require face context propagation, but not metrics and spans, then I can, You know, rework this configuration to have that kind of control.
**Cesar Munoz** 23:36 Correct me if I'm wrong, this API that you proposed here will be… Intended for instrumentations to Become aware of the config, so that they don't… Create spans based on what it's… Comes from here.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 23:57 That is the idea. So, now the next step is to, to modify the instrumentations, so that, like, these, if, if, say, for example, we… we add API.example.com as one of the, allowed hosts, only allow those hosts. So, I… I want to update the instrumentation to, look at this configuration, and if we are, if, if we are, like.
Encountering some other domain, then… or some other post, then we did not instrument it.
**Cesar Munoz** 24:34 Got it.
Guys.
Handsome. But, like, aside from that, just wanted to try to connect the dots end-to-end.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 24:45 Huh.
**Cesar Munoz** 24:45 If this API would be the one that delivers, let's say, the filter configuration to the existing instrumentations.
Then, where will users… provide… those filters. I'm guessing the DSL?
Somewhere, or, or… or they always have to do this… instrumentation or other URL filter or something manually elsewhere.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 25:15 So, I mean, this would be the row API, I think, like, we can… maybe, in, as a nice add-on, we can, add some sort of DSL config in the agent, maybe?
for easier use… usage.
**Cesar Munoz** 25:33 I like the DSL, In the… in… in a way that… I wouldn't like users to… manually use this API, At least until we know What it should have.
Before, you know, making stable.
At least on that side, I would prefer the DSL.
As, the only way users Or at least the exposed wave for users to… Add these filters.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 26:03 Yeah, this, this, I mean, I… I don't know if I, mentioned this in the plan, that was, like, the fifth, PR in my, plan, to have a easy-to-use, API. So this is… More for internal, you know, how we design.
The configuration, or how this would be passed on to the individual instrumentations.
**Hanson Ho** 26:33 Yeah, that's… that's what I was tripping on. I thought you were leveraging existing configuration, but you're adding layers of configuration so that this could be applied generically. So that API might… might be more, harder to come up with. So… like, yeah, I thought… I thought the existing information would already have that, and we're just applying configuration, but this is both. We're applying configuration that we need to build first.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 27:05 Right. Do we… I don't think we have any sort of configuration that we can use, with instrumentation today, right?
**Jason Plumb** 27:12 Not for this stuff.
**Hanson Ho** 27:13 I don't know, that's what I'm aware of.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 27:15 No. So, the only thing that we do is, like, we, I think it uses some sort of context-based suppression, so that, like, we do not instrument the instrumentation, or, or, you know… Exporters. Yeah, exporters.
But, like, I couldn't find any other way, so that's why we have to build out this… configuration.
**Jason Plumb** 27:37 Yeah, the suppression context key is the thing that I think inhibits the… Stuff for the exporters themselves.
**Cesar Munoz** 27:46 Yeah.
**Jason Plumb** 27:46 So, there's something that's put into the context and then checked later.
I think Cesar built that.
**Cesar Munoz** 27:53 Yes.
**Hanson Ho** 27:54 So the Android API looks fine, but I don't think we're gonna be making the instrumentation aware of that.
Right? So, the API that we probably should be talking more about is how you intend to modify the instrumentation itself to take the configuration generically, without taking a dependency on Android.
That seems like the more, The one that needs a bit more thought on.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 28:24 Okay.
yeah, makes sense. That I can work on, but, like, so I… for that, I think, I think if we can agree on, like, what kind of user configuration we allow.
Then based on that, I can work on how I can, like, use a generic configuration for the instrumentation so that, like, doesn't have an Android dependency.
**Hanson Ho** 28:54 Sounds good.
Again, knowing the first PR to just, like, the surface area, that we're expected to configure on Android would… Kind of put the other stuff into a different conversation.
with different people, too, because, the instrumentation isn't owned by, you know, the Android folks, but, you know, others.
**Jason Plumb** 29:17 Yeah, what I'm… what I'm thinking about is… the addition of, like, new APIs to do tracing stuff… That are kind of outside of the main way that OpenTelemetry does tracing stuff.
So that's why I keep thinking about the sampler.
as being a natural fit, but it doesn't do all of the three things that we were talking about, right? It inhibits spans.
I don't think it breaks trace context propagation.
And I don't think it would change your metrics.
I think you'd still have the regular HTTP client metrics, so I was like, well… maybe we just drop those, if there's a way to drop those, but I don't… There might be a way to put, like, a metric view in place.
to… I mean, whatever, metrics on the client side are spicy already, but… Like, maybe we could put a metric view… I bet there is a way to use a metric view that drops them. Like, you could probably… I don't think we have any DSL around metrics at all, let alone metric views.
But I'm just… my… where I'm going with my 8 o'clock first cup of coffee brain is, like, I want to see if there's a kind of a more natural OpenTelemetry API-type way of doing this, rather than inventing a new API that sits, like, next to OpenTelemetry.
If that… like, the OpenTelemetry core use cases. And maybe because we're client-side, we have different use cases that haven't been considered, but… This is a pretty mature project at this point, and I'm sure that someone has thought of this use case by now, and so I still question whether or not there isn't an existing way of doing it that is good enough.
If that makes sense.
**Hanson Ho** 31:10 I think the utility… I think the…
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 31:12 Sorry, go ahead.
**Hanson Ho** 31:13 So I think the utility this brings is the single point of configuration for n number of things. So I think if we agree that that in and of itself is useful, then what that could do is apply existing OpenTelemetry filtering and limiting options.
**Jason Plumb** 31:33 Yeah, yeah, yeah, so I think what you're saying, I think what I'm hearing is that, like, this ends up being not… this ends up just kind of being a configuration interface, and then… when the OpenTelemetry SDK is getting created, we leverage this to create those specific things, like to create a sampler, to create a metric view, and to create… I don't know what you do with propagation, but something.
Right? I think that's what you're saying, Hanson.
**Hanson Ho** 31:58 Yeah. You can do this via, via, like, programmatically with this, you can do this with YAML config, you know, any other way.
**Jason Plumb** 32:06 It sounds like… it sounds like that's not quite what Ben was suggesting originally, if I'm reading this correctly. It's like we would have implementation changes that are then specifically aware of the config, and have to respect this.
**Hanson Ho** 32:20 Yes.
**Jason Plumb** 32:22 Jim's… Jim's HTTP client gets popular in 2 years, then the instrumentation for Jim's client has to also then implement this, rather than the kind of doing it the core way, or the kind of the OpenTelemetry fundamental way, would cover all of those use cases, right?
**Hanson Ho** 32:38 Definitely.
**Jason Plumb** 32:38 PDP, you know, it would be for other possible instrumentations, too. But it sounds like, Ben, it sounds like you've gone down this route.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 32:46 So, why… okay, let me… I understand, like, we have to change instrumentation, and why we are in this position is, I think, like, these instrumentations were designed to, you know, you use with, like, manual instrumentation, like, you instrument your OKHTTP client.
But what we are doing is, like, auto-instrumentation, which just, like, patches all the OK HTTP clients within the application, and that's So, with how the original instrumentations were built, like, there was no need for this kind of configuration. Like, you attach it to whichever okay, street client, you wanted to instrument, right? But now… now we are doing a blind patch on everything, and that's… that's where this, you know, unique situation comes up, and, like, I… I think this is unique to Android at this point, like.
Probably doesn't apply anywhere.
And that's why, You know, it does not exist in the instrumentation itself.
So, yeah, I…
**Jason Plumb** 33:44 The instrumentation is at this level, right? And it sits on top of the SDK.
Like, the core implementation, right? And that core implementation is based on the specification, and the specification includes a lot of ways of doing these kinds of things, like not sampling. I mean, not… not including spans by sampling.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 34:05 Okay.
**Cesar Munoz** 34:05 Or, like, or, like, dropping stuff in the processor.
Exactly. Expands. Things like that.
**Jason Plumb** 34:12 But if you've gone down this route, it would be cool to see, like, where… I know you have this cool table that shows why the sampler isn't enough.
But maybe the sampler combined with, like, maybe a metric view for this, and maybe something else, I don't know, but if it… I haven't… I haven't scratched at this enough to know, but I suspect there's some ways to handle this in the SDK, is what I'm getting at.
**Cesar Munoz** 34:37 It kind of…
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 34:37 Understood.
**Cesar Munoz** 34:38 to me that we were talking about several things at the same time.
You know, metrics and things like that.
But if, if, if I'm trying to focus on not creating spams for HTTP.
Requests, and there's definitely Many ways within the… OpenTelemetry core APIs to do it. I really don't know if metrics All the other stuff needs to be also avoided.
But at least on that front, there could be some, as you say, natural open telemetry ways to do it.
And I guess right now, Really, my biggest concern is what will be the user interface to provide this filters.
So, and I would like it to be the DSL, like, in the simplest way, like, an array of hosts, and that would be it, at least the beginning, and then we can… expanded. Now, how this array, or whatever config we put in the DSL gets actually executed.
Yeah, I guess it's… I would like to… I agree with Jason, it would be nice if we didn't have to add new APIs to carry over that work.
So, it would be nice to see that path.
Unless, you know, there's a… Clear use case where, you know, you know, at least having the metrics or something like that would be… Incredibly annoying, or… Cause too much problems, or… so that we must get rid of those two things like that.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 36:25 So, okay, so on the use case, So, you do not see a situation where we would want to avoid metrics for a certain post, or, like, certain… the API calls made by a third-party SDK, is that… what are you saying, like, that's not a strong, use case?
**Cesar Munoz** 36:49 Well, the thing is that so far, metrics really haven't been a topic.
in… Overall, in this SIG. Usually we… actually, overall client stuff in OpenTelemetry, my understanding is that the… the feeling is that metrics aren't needed for clients. I think today.
just because we're using OKTP's upstream instrumentation, I think it already creates metrics, I haven't checked.
But for the… for the large part of it, we… I think we could just ignore it. So… so that question that you just asked, it's really… we haven't… Talked about metrics that much.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 37:33 Okay. Makes sense.
**Hanson Ho** 37:36 We could almost talk about this as four separate things. One is, how do we configure what is the general configuration API that we have? That's topic one. And then… supporting each of the features, could be a separate topic on its own. Looking at, like, what you're trying to do, it… it might be hard to do it with OpenTelemetry API, simply because some of this is literally about configuring how an instrumentation does things. So the trace parent injection and the, the WebSocket stuff is… It does… it's… it's configuring not the… what hotel stuff happens, it's in… it's how the thing… That gets to know how it's produced and what it includes.
So, I could see all the separate features, some of them having open telemetry ways of dropping, like, with the sampler and traces, but the others maybe not. So, it's hard to, I think, talk about it, like, in one general thing, because, you know, as somebody said, we are talking about multiple things, so it would be good to separate the things that we're talking about. So, whether we're okay with the current API or prefer a DSL, That's topic one. Topic two is how we prevent traces from being propagated. Topic three is how we stop metrics from propagating.
Etc, et cetera, et cetera.
These are all different.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 38:58 Yes, I think, like, I kind of, did not, like, the instrumentation-related changes, I think, that I… I need to take another look at, that. I did not give so much thought. I think that's why we have a, I think that's important to have… to have that clarity before we go further, so I'll go back to the drawing board and see how we can do this.
you know, what kind of SDKs or APIs, like, at the SDK level, or API level, what is available, rather than, like, changing the instrumentation as such.
**Hanson Ho** 39:42 Yeah, some of them is maybe possible, through existing means. Others may not be, and we have to make a decision whether we want to go down that route, or it's something we actually need to support, like metrics. It's theoretically possible, but no one… not a lot of people are, configuring metrics we set from Android devices, probably.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 40:02 Okay.
Got it.
**Jason Plumb** 40:04 I kind of alluded to some of this earlier, and I didn't… haven't scratched around very much, but I did find this issue… That's related to the trace context propagation stuff.
You'll note that it's from 2023, so this is not new. There was someone who wanted to conditionally disable propagation.
for whatever reason, they have some pros here, and then… yeah, so Ted… Ted makes a point, like, down here, like.
How about it?
Being designed just to be able to be interoperable with whatever's downstream from that, and… And it seems like no one's actually done… I mean, at least according to this one issue, and there could be similar ones, but I haven't seen… I haven't seen this in… I don't think I've seen this implementation yet, so I question… How important it is?
But we could… we could provide… there is a propagator… like, a interface, and so we might be able to customize the propagator in such a way that it knows to filter based on host. So there… that might be the mechanism by which we could implement this. So, assuming that, like, this is configuration, when we go to create the SDK, if we can provide… if we can make the sampler, the metric view, and then a custom propagator that's, like, host-aware. And that might get us there. And then we don't have to touch the instrumentation implementations.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 41:32 Right.
**Jason Plumb** 41:33 Okay.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 41:34 Yeah, I'll, yeah, I think the initial design was based on, like, modifying the instrumentation. I understand the challenges with that.
Either.
It's like…
**Jason Plumb** 41:44 Certainly a viable approach. I mean, it's kind of the most direct and most straightforward, but we are sitting on a stack of other code that has considered this kind of thing previously, and so… It's nice when we can fit within those existing use cases, right?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 41:58 Absolutely.
**Jason Plumb** 41:58 I think we've probably talked this to death. I think there's still… Some work to be done there. Do you have, next steps, Ben? Like, is this okay?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 42:08 Yeah, I, I think, I've, Yeah, I would, you know, appreciate some feedback on the configuration, or, like, how it should, you know, look like at the DSL layer, or, like.
**Jason Plumb** 42:21 This is a good first start. Just, if you convert this to look more like DSL, I think this is a great start. With one exception, is that this glob is starting to give me hives a little bit already, so maybe we don't do that in the first pass.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 42:35 Yeah, I, I actually, in the initial implementation, I, literal ITV6 blocks, I dropped because of…
**Jason Plumb** 42:42 You know…
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 42:43 complications. But yeah, maybe regex as well. Makes sense.
**Hanson Ho** 42:47 I said a bunch of regex, good time.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 42:51 Yeah.
**Jason Plumb** 42:51 Yeah. Yeah. Okay, cool. I think we should probably move on in the interest of time. We've got about less than 20 minutes left.
Cool. Hanson…
**Hanson Ho** 43:01 Yeah, I'll touch on this quickly. The Federated semantic convention for client-side has been created. I'm working on, first commit. We're going to talk about it next week in the client, instrumentation SIG, about how to proceed. Basically getting a structure in, getting some, existing, Things in so we can populate the repo and do some tests to make sure, you know, the manifest published properly.
And then deciding, how to move stuff around and put stuff in there. There's a way for deprecating existing semantic conventions, and then moving them to this new repo. And the idea is to have a handful of namespaces that we own, and then do the deprecation for. But at the same time, we could add new ones.
you know, without having to do deprecation, because they don't exist. And finding out a process to do that is also, you know, something that we need to tackle. The Android manifest, or the Android project, we have a science convention. It's not V2.
And it doesn't publish a version that manifests out. The artifacts go out, but there's no manifest status. Like, it's always version 0.10, and it changes whatever made is. So, work on the Android project will include, figuring out how we want to use this, and where we want to put our, semantic conventions, especially ones that… that we aren't… we aren't… gonna publish out. The ones that we want to move out, we can move out, and deprecate and do all that. But the ones, that, that we want to, kind of just keep private, we can do that as well with the manifest. You don't… you'll… with V2 of Weaver, you specify what public interface you have, so we could basically have none, and then internally, we could still have semantic conventions that this project owns, uses.
But it's not a public API, so we don't have to worry about, you know, changing.
At least, you know, not… not with other consumers of the semantic conventions. We do with the instrumentation itself, obviously. So, that's a path forward.
So I had a…
**Jason Plumb** 45:25 And since you brought up… I think on Tuesday, you brought up a good point about what it means for Android to be publishing its semantic conventions, and… I think it's a legitimate problem, like, so… I think I just did, like, Maven… Like, Android semantic conventions.
Yeah.
Like, we can get to, like, this, right? So we do publish jars, right?
**Hanson Ho** 45:53 Yes.
**Jason Plumb** 45:54 like, a person could take a dependency on our latest version of the semantic conventions, and what they get out of that are those two things, right? It's the constant classes and the event classes, and they could go crazy with those if they so choose. These are not really intended to be consumed.
But that's the thing we publish. What we don't really publish in our repo, if you go to a given release, is We don't publish any ER files or R files, or whatever, we just have the source code bundled up, because it's expected that people will consume it through Maven, but the semantic conventions are interesting because, they get versioned along with Our artifacts, and if you go into the repo and you look at our federated semantic conventions.
They are versioned by… schema URL… I haven't looked at this in a while, it's probably this.
Right, so we've declared a version here. This version is not in lockstep.
with our… main SDK version.
**Hanson Ho** 47:00 Yep.
**Jason Plumb** 47:01 So if we make a PR, like, say, today, to change this to 0.2, how do people become aware of that? And I guess one way is maybe you point directly to this file, but the question is, should we publish these, Is there a way, or should we be thinking about how to publish these as a more permanent artifact that is, like, a point-in-time version, rather than just the file sitting here on the tip of the head branch, or main branch, or whatever?
So…
**Hanson Ho** 47:31 Yeah, that's kind of, like, the main thing we need to figure out is, structurally, what is the open tree Android semantic conventions? Right now.
there is that URL, and there's that version, but the version is… is not, as you said, in lockstep with our version. And when we publish it, it does… we don't have to cut artifacts in order to publish it. We just have to basically declare it and say, hey, this is… this is the file, this is the version. So it's almost like there's, like, two different versions happening.
the actual artifacts we generate aren't even necessarily mapped one-to-one to the manifest. It is… it just happens to be what we pull in and, you know, run the code generation for. So, there could be an implicit dependency on, like, you know, a third, like, the core. There definitely is.
Because a lot of that stuff is coming from there. So… The version of the artifacts.
That is versioned along with… the… the project. This is something a little bit different. So, figuring out How we want to do it is probably the important thing.
doing that is almost secondary. So, I don't know if folks have already had some opinions or thoughts about it, but, I just want to seed this, and we can talk about it probably at a later time.
My current opinion is that, we should not publish.
We should not be… we should not be a full federated semantic convention.
repo that publishes a versioned manifest that others would want to consume, because.
**Jason Plumb** 49:18 We Android.
**Hanson Ho** 49:19 We Android.
**Jason Plumb** 49:21 Yeah, the client-side stuff, I think, is the place for that now. Exactly. I think I agree with that, yeah.
**Hanson Ho** 49:27 if we start having, like, app.android. You know, AEI or whatever, that shouldn't live here. That should live… or that shouldn't live here, as a public-facing thing.
in the long term. We may want to put it in our, repo, consume it, but have it internal.
And then when we're ready, we promote it to the real repo.
And basically have it live there. Because… I don't want… It doesn't make sense to manage yet another, manifest, yet another version, if we could help it, since the client-side one seems to be a reasonable place to put it.
That's not good thinking, so…
**Cesar Munoz** 50:11 So… So, essentially, the current semantic conventions that we have in Auto Android will Eventually just have… Either, you know, experimental stuff, Or stuff that we know… will never be needed outside of Android. That's pretty much it.
**Hanson Ho** 50:30 outside of, this project specifically, yeah. So, even if we move it to V2, we could have, like, a stub, manifest, but nothing public.
I don't know if Weaver supports that use case or whatever, because we still want to structure it as if it were a regular semantic convention. Oh, yeah. Like, put it in the YAML file, have it generated, so that when we actually promote it, it becomes easy. So we basically do all the work of putting it in place in our repo, and when we promote it, it's hopefully pretty mechanical.
**Cesar Munoz** 51:04 Sounds good.
Yeah.
**Jason Plumb** 51:07 Okay, so we… go ahead.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 51:10 Sorry, yeah, I, I, I feel like… So, what is the actual purpose of having something published? I would imagine it's for somebody who's building a consumer to reference, like, for this SDK version, there's this semantic convention That… that is fined against for this, SDK version, right? Like, for Android. So, even if it's just Android only, or, something that's, used only by the Android project, I think it's still… there is still value in publishing that.
So that, like, there is that pinning against SMAD convention, versioning against the SDK, when you're… when you're building on the consumer side. So, yeah, that's that.
**Hanson Ho** 51:48 No, that's true. Yeah, true.
**Jason Plumb** 51:50 I mean, I wrote this, I'm like, does it matter, like, who consumes these, or who cares about any sort of published semantic conventions? And I, you know, I have to think that it's probably vendors or tooling that wants to look at this and say.
what attributes are available on what things, because they want to pre-populate a drop-down, or, you know, there's, like, something in a vendor's tool, probably. Or to help out… something to help, maybe, application developers with new conventions, I guess. I don't know. I don't know why people care, but…
**Hanson Ho** 52:22 if the Android project publishes a semantic convention manifests, it should be tied to the, the project versions. And that is different than, I think, the semantic conventions for federated repos, which… it'll be somebody like us taking that version and then generating artifacts from it to consume. So, yeah, I think it is a useful thing to publish, but for a different purpose.
And also, the versions should be tied. It shouldn't be… semantic convention 1.5, for Android, and then our project is a 2.1, or something like that. Like, you do want the match between, hey, I'm using this version of the Android agent, what semantic conventions does it use? And then if we… there's a link to it that I can programmatically get, parse, and understand, I think that's useful.
But I don't want them to say, I'm depending on, you know, Android client version 2.5, the spansing engine that it publishes. Because, well, I guess they could.
If they want, but, there's no guarantee that in 2.6, that certain things aren't removed, if it's internal declared. So, maybe that's a way of getting out of this, but, I think it'll be easier to talk about it with a proposal in PR form. So, you know, we can talk about it next week. Hopefully by then there'll be a PR that I can point to, at least update the one I have right now, which is out of date.
**Jason Plumb** 53:52 So, we're rapidly running out of time. I want to make sure we just cover quickly these last few things. So, I wanted to bring up… are we cool to move on?
**Hanson Ho** 54:00 Yep. Yep.
**Jason Plumb** 54:01 Okay. I wanted to bring up this thing, which was recently mentioned in Slack and over on our side. Not necessarily a new issue, and you'll notice that this is against the instrumentation repo, but this is coming from some folks working on Android, and it… what happens is, you know, we have a policy right now about strict mode, but this is a strict mode violation that was discovered. It was pretty significant. I forget, it was, like.
it was non… I don't know if it's stated in here, but it was, like, a non-trivial thing, but… oh, 80 milliseconds, right? So, what happens is that during the creation of the HTTP instrumentation, the instrumentation API in upstream Java.
has an SPI for having these customizers, and so it walks the class path looking for customizers, and does a service loader thing which hits strict mode and causes somebody some grief.
And Lori has been looking at it or responding a little bit on… on this… on this issue, but I just wanted people to be aware of it, and maybe we should think about what we might… could do for that. Like, maybe it's a change in upstream that… Allows us to configure the suppression of any customization for a given instrumentation, but I don't know what that looks like yet, or even if it's possible. But just know that this is, like, a hit, so if, like, your users turn on strict mode and hit this, don't be surprised, I guess is what I'm saying. And we should think about ways of making this better, right? Like, because in most cases, there's not a customizer, or a customizer's not needed, so doing the service letter thing is, like… A little unnecessary.
**Cesar Munoz** 55:45 Thanks for bringing it up.
Yeah, I think if there was a way for us to disable this.
Like, because it seems like an extra configuration layer.
that… I guess we don't have to have, if we don't need it yet, until somebody complains or something.
**Jason Plumb** 56:06 Yeah, I mean, it would be nice just to not block startup, right? Like, that's also, like, should be a goal of ours, is to not make apps considerably slower, just because we're walking the class path looking for things that don't exist. Like, that, you know, ideally we wouldn't be doing that, but I don't know that there's a mechanism yet to do that, so… Anyway…
**Cesar Munoz** 56:25 I know that Jamie… Jamie added some changes.
not too long ago that enhanced the SPI loading.
But I don't know if those take this into account, because they seem to be even more deep inside the implementation.
**Jason Plumb** 56:43 Yeah.
**Jamie Lynch** 56:43 I think I ported over a fix that Hanson originally did when we first integrated the Java SDK into the embrace SDK, and I think it was effectively switching I think, yeah, it set some sort of property which basically avoided the context, storage from hanging disk by default, so I don't know whether… It's possible to do that for this, or whether it just always Runs, and it's not, like, a configuration option.
**Jason Plumb** 57:16 I don't think there is one yet for this. I think it's… I think it's just baked in. I was… I was scratching at this. I spent all of, like, 4 minutes looking at this yesterday, and I think there's nothing yet, but maybe we need to add it.
**Jamie Lynch** 57:27 Yeah.
**Jason Plumb** 57:27 So…
**Hanson Ho** 57:28 it's a bit of a whack-a-mole, basically. Anybody can introduce a discrete, so anytime there's a discrete.
Yeah. We need to try to avoid it, so… if there's a mole up… It's whack it.
**Jason Plumb** 57:41 Yep.
Okay, and then just real quickly, I know we're about at time, Jamie, has a couple of PRs. Please review them. They are what we talked about previously, about integrating the Kotlin API into some places in Android.
And Ben is now an approver, and when Vishwan returns from vacation, I guess, we will, get him set up as well.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 58:05 Alright, thank you guys so much.
**Jason Plumb** 58:08 Yeah, thanks for all the help, thank you.
**Hanson Ho** 58:09 You're pushing all the right buttons, this is great.
**Jason Plumb** 58:14 Alright, everyone, thanks for the help, we'll see you soon.
**Cesar Munoz** 58:17 Mode.
