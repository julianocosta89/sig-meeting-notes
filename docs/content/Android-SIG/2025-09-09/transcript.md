SIG: Android SIG
Date: 2025-09-09
Duration: 61 minutes
============================================================

## Zoom Recording Transcript

GZ Gregor Zeitlinger 00:01:17 Hello?
Hanson Ho 00:01:19 Hello?
Jason Plumb 00:01:22 Hello.
How's everyone doing?
GZ Gregor Zeitlinger 00:01:37 Good.
Hanson Ho 00:01:40 Not bad.
Surbhi 00:01:43 Doing good as well.
Jason Plumb 00:01:45 Hey, stranger!
Surbhi 00:01:47 Sorry about that.
Jason Plumb 00:01:49 How you been?
Surbhi 00:01:51 Yeah, all good.
Jason Plumb 00:01:53 Good.
Surbhi 00:01:56 Now that we have done the GA release, hopefully we'll have bandwidth to look into things, and I'll… Come here often, hopefully.
Jason Plumb 00:02:05 Great, that's awesome, that's good news.
Alright, looks like we've got people adding stuff to the agenda, this is wonderful.
Give it another 30 seconds to settle down.
Hey, Cesar.
Cesar Munoz 00:02:24 Hello?
Hanson Ho 00:02:25 8?
Cesar Munoz 00:02:29 8.
Jason Plumb 00:02:38 Well, look, I'm the first one. Okay, so I think I put this in last week, just as a thought, as I was reviewing stuff.
The question is, is our use of detect making small PRs harder to review? And maybe I'm just overstating things, maybe I'm over-inflating it right now?
But, like, here… here was a pretty… what should be normally a pretty small PR.
That's just converting a constants file to Kotlin, and in doing that, 12 files changed.
And, you know, here's the real change, but look at all this other stuff that had to change, or did change as part of this, and I'm wondering… if we… if this is fine, am I just, like, getting too concerned about all of the XML, and it's a good tool and we like it, or… Is there a way to improve it? And will it just, like, steady state? Like, is it… is this still, like, the initial kind of bump, or do we expect there to be this much thrash on the detect stuff overall?
Hanson Ho 00:03:42 So I think we need to… We actually settle on a list of, rules that we want to actually have and adhere to.
Because what we're doing is basically adding exceptions to every violation, which is… which is not… the goal is for baselines to be empty, and that we fix pretty much everything. So, I think what we should do is… get a set of rules that we're okay with, do a massive refactor to basically reset the state, and then this wouldn't… like, the fact that these are in here is because they are A violations that may or may not be valid, and B.
Jason Plumb 00:04:19 Yeah.
Hanson Ho 00:04:19 They are from a file that we touched. So these files should all be touched by detect, outside of any of these, and then I think it'll be a lot smoother. Adding to the baseline should be an exception.
The idea is to fix, things that are addressed, or that are picked up.
Jason Plumb 00:04:40 Got it. And, I mean, we've made exceptions by having baselines for each of the modules, but really, we think that we should be able to reduce it down to one baseline that's pretty thin at the top.
Hanson Ho 00:04:52 I don't know where the baselines have to live, whether it's in the specific project or, like, that part, I don't know. But the baseline should be a steady state. It should, you know, even if there's, like, 20 baseline files, it should contain what it should contain, unless new violations are added and need to be, added to the exception.
Jason Plumb 00:05:16 Right.
Hanson Ho 00:05:16 That really shouldn't happen. Unless, oh, you know, for some reason, this rule we should have, but for this case, there is an exception, for whatever reason.
Jason Plumb 00:05:26 Okay, so if we had a, But, like, okay, so for example, just to pick one here, like, to pick… this instrumentation, whatever the hell this is, like this one, okay? So, we have a baseline here, which is max line length.
But it then also has to call out the specific instance of that line length, I think?
And then, like, the next one, like, in the compose instrumentation, we have line length. So, if we had an issue to, like, get rid of these bass lines and all the instrumentations, that would also help, wouldn't it?
Hanson Ho 00:06:01 Yeah.
Jason Plumb 00:06:02 Yeah.
Hanson Ho 00:06:02 Yeah, basically, the entire codebase should have… we should, like, you know, go through it once with this.
Jason Plumb 00:06:11 Okay.
Jamie Lynch 00:06:13 I'd also add that Detect is pretty configurable. Yeah, and base we don't use for defaults. We've disabled a few things, but we find too annoying, like, I think we've got an increased max line length, and… Like, we don't check for magic numbers and things like that. So, it may be we take a look through These baselines see if there's, like, two or three that are taking out Taking up, like.
The majority of the warnings, and we could suppress those.
Jason Plumb 00:06:43 Okay.
That sounds good.
Hanson Ho 00:06:47 I think you already created an issue for that, right, Jason? To basically have someone take a look? Or I did, maybe? Or somebody did?
Jason Plumb 00:06:53 I don't recall this, but maybe, maybe.
Mustafa Haddara 00:06:57 finishing sector.
There is a detect issue out there.
Jason Plumb 00:07:00 Hmm… Alright, thanks, Hanson.
Hanson Ho 00:07:03 Oh yeah, I did that.
Jason Plumb 00:07:06 Okay. We probably don't need to talk about it much more.
Okay.
Hanson Ho 00:07:25 I'll get to that today, because that's gonna be one of those annoying things that… We'll continue to annoy, but, you know, it's not breaking.
Jason Plumb 00:07:33 Yeah, huh.
Hanson Ho 00:07:33 So…
Jason Plumb 00:07:34 Okay. Yeah, that's kind of why I bring it up, is just, like, I was looking, I was like, I just want to review this thing, there's all this other stuff, so yeah, I get it, it's cool.
Hanson Ho 00:07:42 The friction is completely real.
Jason Plumb 00:07:44 Yeah Yeah.
Okay, Serbi, you're up next.
Surbhi 00:07:51 Yes, so, like, in the network detection logic.
So when our SDK is initialized in application.onCreate is when the current network provider is initialized as well, and the first network set of attributes is gathered, but when an app can ask for a permission is only in the main activity, the earliest. So… The details that require the permission, they are captured as permission denied, like, the first time the app is installed.
And in the main activity, let's say the permission is granted, but the status… the network doesn't change, right? So we never get those details, even though the permission is granted. The reruns of the app or the network change events will have those details.
But the very first span won't have it. So it's, like, not a big issue, but, like, if we can the agent can't keep calling, that would be a bad design, so instead, if we can provide the app, API that they can call, like, we do have the refresh network status API, If the, if that can be called, then it would refresh the network status, and we would get the correct span once the permission is granted.
But right now, it's marked internal, like, it's in the internal folder.
Jason Plumb 00:09:18 Right, so your thought is to expose this and allow the application user, the application developer, rather, to call this manually in their activity.
Surbhi 00:09:30 Once the permission is granted, yeah.
Jason Plumb 00:09:34 Are there any way to… do we know if there's any way to register listeners for permission changes?
Surbhi 00:09:42 That's… I did not check that, but I will check it.
Jason Plumb 00:09:46 It would be cool if we could just attempt that when the permissions change, because they don't change very often, but… yeah, I don't know, This doesn't seem… I mean, it's in an internal class, right, and this is designed not to be exposed, but it doesn't seem like… the worst thing… I do wish it was more automatic, though. I hate to… Hate is a strong word. It's a shame to maybe burden the application developer with needing to do this, right?
Surbhi 00:10:13 Yeah.
Okay. But what if there is no listener for the permission change?
Jason Plumb 00:10:20 Yeah, I don't… I don't know. We do have activity… we do have activity listeners, though.
So, can we hook that into the application… the activity state, and then do it, like, once?
Surbhi 00:10:35 Okay, when the first activity is initialized.
uncreated or something.
Jason Plumb 00:10:42 Yeah, I'm just… I'm riffing here, because I don't know what the right approach is.
Surbhi 00:10:47 that… I think it would be difficult, because they can, ask for permission anywhere, right?
So, like, in the first activity on create also, we can't do that.
Jason Plumb 00:11:03 Like, that there would be… there could be a timing mismatch. So listener is the best, if that is available, I'll check that. Okay.
Hanson Ho 00:11:12 So, is it so bad that we require a restart for the new… information to be added.
mobile apps start up fairly frequently, like, or rather, you know, cold starts happen fairly frequently. So if we have to put a bunch of logic here just to kind of take care of that one case, it may be okay to not, to not, explicitly handle this use case, especially if folks that really want this will probably… either ask it for it to be opt-in, or ask for it by default, and I think it'd be much more, reasonable for them to ask for the light version of that permission. And, you know, for those that don't have that, and they want to ask for the big one, and, you know, this requires, like, a reset, or not reset, but, like, you know.
The next iteration, the next instance will capture.
I think it's okay to avoid complication and extra craft. Not craft, but extra, like, you know, code.
I'm always trying to prevent.
Jason Plumb 00:12:19 I hear that for sure, Hanson. Did you have a… Serbi, did you have a specific use case where this was problematic?
Surbhi 00:12:25 Yeah, so, like, API 33 onwards, there is a default permission, the basic phone state, that would be granted, but between API 24 to 33 is… and the first install would be a problem.
Jason Plumb 00:12:43 Okay, but… and that's only on the first launch, and presuming that they give it the permission on the second launch, it would be fine?
Surbhi 00:12:50 It would be fine.
Jason Plumb 00:12:51 Okay.
Surbhi 00:12:51 But also, usually, they don't change the customer ones, like, they don't toggle the permissions as often.
toggle the permission, then also there is no refreshing of status. So if there would be a listener, that would be the best, I think.
Jason Plumb 00:13:10 But to burn just the network information on the first session on some older APIs, I'm gonna reiterate Hanson's question, is that so much of a problem?
Surbhi 00:13:20 That makes sense, yeah. It is not. Like, the subtype would be null , and the older carrier APIs would be used.
Jason Plumb 00:13:27 Right.
Surbhi 00:13:29 Yeah, that is not a problem, as big of a problem.
Jason Plumb 00:13:32 Yeah, okay. Mustafa, did you have something?
Mustafa Haddara 00:13:38 basically the same question of, like, oh, is a Java problem if we just… first session's not accurate?
Jason Plumb 00:13:43 Yeah.
Hanson Ho 00:13:44 We should definitely document it in the docs and say, hey, you know, permissions are granted,
Jason Plumb 00:13:50 Yeah.
Hanson Ho 00:13:51 at different times. So, it may require a restart before the extra information is added. And really, we're talking about, like, the network, I think the carrier name, and some details, so… The request will still be, or the change will still be tracked, you know. So, the important information is there, so…
Jason Plumb 00:14:12 Yeah, but…
Surbhi 00:14:13 fence.
Jason Plumb 00:14:13 But circling back on this idea, so maybe not… maybe we wrap this with something that's not in an internal package, right? Where am I?
if we expose this in some form, it's a pretty small API surface, and we wouldn't even need to return this, right? The application developer doesn't need that result.
But we could, we could, you know… basically, we want to put a wrapper around this, is what you're suggesting.
Surbhi 00:14:42 Yaw.
Jason Plumb 00:14:43 I mean, we do need to store it, obviously, but whatever.
That doesn't seem too bad to me either, and then if there are cases where an application developer absolutely needs to get this information earlier in the process, then they could do that, right?
Mustafa Haddara 00:14:59 Are there any other things that we have to request permissions for that have the same problem?
Jason Plumb 00:15:08 I'm not aware of it. What about DISC?
I don't know if that… I don't think that gets requested.
Cesar Munoz 00:15:16 I think this is the only use case where we require permission. Yeah. But I guess… I think I'm fine as long as it's done in a way that And maybe that's… Not sure if Mustafa was trying to… talk about… probably it's fine to expose some sort of API, as long as it's extendable, you know, if in the future we need Maybe add more stuff, it's not, like, all over the place.
Mustafa Haddara 00:15:40 Yeah, like, I wouldn't want to call it refresh network status, more like refresh permissions or something.
Jason Plumb 00:15:46 Okay, yeah, make it more generic, and then the instrumentations can provide a hook to that or something?
Hanson Ho 00:15:52 If necessary, in the future. If necessary, yeah.
Jason Plumb 00:15:55 Yeah.
Cesar Munoz 00:15:56 Yeah.
Hanson Ho 00:15:56 Refresh state, or, like, you know, something about, like, basically, hey, maybe check the stuff again, and, you know, we can put more than this.
Do we have a place like that? Like, does, like, the agent instance or something expose?
Something similar?
Jason Plumb 00:16:14 No, I don't think so.
Hanson Ho 00:16:19 Where would this be? Because I prefer it not to be, like, a global thing that gets hooked in. But if… I guess if that's all we do, then…
Jason Plumb 00:16:29 I mean…
Hanson Ho 00:16:30 do.
Jason Plumb 00:16:31 You mean, like… like, permission change refresh, like, manually called from the application. You don't want that to be kind of global.
Hanson Ho 00:16:39 Well, right now, like, if we were to kind of expose this API, would it be, like, a static thing? Like, where would it… where would it be attached to?
Jason Plumb 00:16:48 I mean, I think it would have to be on OpenTelemetry Rum, wouldn't it?
Hanson Ho 00:16:52 Yeah, okay, if there's always access to, like, an object that represents, like, the SDK.
Jason Plumb 00:16:57 That's… that's kind of the main API.
Hanson Ho 00:17:01 Yep.
Jason Plumb 00:17:03 I know Cesar's getting twitchy. Every time we bring that up, he's gonna get nervous.
Cesar Munoz 00:17:09 That's the place for adding stuff to interact with ROM after it's initialized, yeah.
Jason Plumb 00:17:17 Yeah, I mean, it's pretty light. There's, like, a bunch of overloaded event methods, but then it's like, get the session, get the OTEL instance, and that's kind of it.
Hanson Ho 00:17:25 I think a refresh, just have, like, a void refresh, and, and, you know, be fairly nebulous in the definition.
Jason Plumb 00:17:33 Well, people are gonna get the wrong impression… I worry about people getting the wrong impression.
Hanson Ho 00:17:38 Okay.
Jason Plumb 00:17:39 Yeah, like, they want to change their config on the fly or something, but…
Hanson Ho 00:17:44 Oh, yeah, yeah, yeah.
Mustafa Haddara 00:17:45 We call it, like, refresh attribute detectors or something like that, because that's what it is, right? We're detecting network attributes.
Jason Plumb 00:17:52 Yeah…
Cesar Munoz 00:17:54 I'm refreshing the entire SDK.
Jason Plumb 00:17:59 Yeah.
Cesar Munoz 00:18:02 So I need… I need… I think we should… be careful that some people… I mean, there are also attributes that are part of the resource, that there's no way that we can change them afterwards.
Jason Plumb 00:18:16 Right.
Cesar Munoz 00:18:16 At least not right now, so…
Jason Plumb 00:18:19 And that's… is that true of network? It's not, right?
Cesar Munoz 00:18:23 I'm not… I think network is not in… I think these attributes are not in… in the.
Mustafa Haddara 00:18:27 Brilliant.
It can't be true of network, because network stuff changes all the time.
Jason Plumb 00:18:33 Yeah.
Cesar Munoz 00:18:34 M.
Jason Plumb 00:18:35 And, at least for now, the resource is still immutable. That may change, I don't know.
Cool.
Hanson Ho 00:18:44 Non-identifying, mutable.
Mustafa Haddara 00:18:48 So then maybe I was wrong, maybe it should just be called Refresh Network Attributes, and we just… we tie ourselves to the fact that You have to do that manually.
Hanson Ho 00:19:02 We're not GA, we can always remove it.
Jason Plumb 00:19:04 It's true. Okay, Derby, is there a tracking issue for this?
Surbhi 00:19:08 There isn't, I will create one.
Jason Plumb 00:19:11 You are the best, thank you.
Surbhi 00:19:13 And I will try to look into these things that we discussed, if there can be an API. I'll try to propose a smaller footprint API, but yeah, if there is a list… if there is a listener, that would be also something. So I'll look into these things and get back to you guys.
Jason Plumb 00:19:32 Great, thank you.
Cesar Munoz 00:19:33 Thank you.
Surbhi 00:19:34 I can add a documentation to the README as well, to call it out right now.
Jason Plumb 00:19:40 So, we might… yeah, oh, this is so weird, because, This is a situation where this behavior is kind of buried in the services, but you would only ever have this problem if you're using the instrumentation, I think, right?
Surbhi 00:19:54 No.
Jason Plumb 00:19:55 No.
Surbhi 00:19:56 So, OpenTelemetry RAM itself initializes.
Jason Plumb 00:19:59 during the SDK initialization, we add these attributes to all spans.
Surbhi 00:20:04 And there isn't a flag that the customer is given to turn it off.
I'm not sure. Even if you're not using this instrumentation, you still get those network?
Yo.
Jason Plumb 00:20:14 Oh, interesting.
Surbhi 00:20:15 This instrumentation is, like, giving the change events for the network, but the attributes we want for every span.
Jason Plumb 00:20:23 That's interesting. We… I wonder if we should change that.
I wonder if… I wonder if you should have to opt into the instrumentation to get those event… to get those attributes as well.
Hanson Ho 00:20:33 It's a lot of attributes adding, to everything.
Surbhi 00:20:38 I think they should be independent, but there should be a flag to get the… to enable… I'm not sure if there is already, but there should be a flag whether they want the network attributes in all spans or not.
Jason Plumb 00:20:50 Yeah, it's default by now, and you can't opt out.
Surbhi 00:20:54 I am thinking that I'll check…
Jason Plumb 00:20:57 Okay.
Surbhi 00:20:58 Yo.
Jason Plumb 00:20:59 That could be a separate issue as well, if you want to file that. I think it's totally fine.
Surbhi 00:21:03 That makes sense, yes, I will do that.
Jason Plumb 00:21:05 Okay, thanks.
Surbhi 00:21:22 Cool.
Jason Plumb 00:21:25 Are we ready to move on to the next topic?
Surbhi 00:21:27 Yes, thank you.
Jason Plumb 00:21:28 Awesome, thank you. Yeah, Leo.
Leonardo Serrano 00:21:31 Hey, everyone. Yeah, I brought this up before, a couple of weeks ago, I believe. It's this issue of client tracing, where… I'll just kind of restate the problem so we're all on the same page. So, out of the box, OpenTelemetry, Android.
it will, and I think this is just gonna be the default, in general for tracing, but… You can take, for example, a scenario where I've opened up an activity, and… then that activity, I don't know, after it creates, does some networked call to some API or whatever, I think logically, you would expect these two things to be in the same trace, but that ends up not being the case currently. You have a application create, onCreate, not application, well, you would have an app, the application startup span.
And… As a child of that, you would have the activity created span.
Which… is good. You want that, You want those two things to be in the same trace ID, but… then you don't have the, get in the same trace, because I believe it's… I'm not sure exactly how… context is being propagated here, or maybe it's not a context propagation issue, actually.
Jason Plumb 00:23:04 Yeah, so you're looking… you're hoping, or your idea is that, there could be, or maybe you're asserting that there should be.
context, that should be using the same context for the activity.
telemetry spans, specifically, and any HTTP calls or whatever child spans get created during that con… during that context.
Leonardo Serrano 00:23:26 Sort of. I mean, that's just one use case. There's also a use case where you'd actually want spans across different activities to actually be in the same trace.
So… you could kind of solve for half of the problem with, Like, an activity span context? Or… there's some other way to do it, and I think we briefly talked about other ways, like creating, like, a… a session parent span, like a long-running span for sessions. Maybe establishing a new type of, like, user interaction, wrapper span, you know, when… when the real user, like, clicks on something, or taps, or scrolls, or whatever, that starts to span, and then ends it when the interaction stops. I mean, one seems kind of really difficult to implement. Okay.
So, unless… Concern…
Jason Plumb 00:24:22 Sorry to jump in, but what it sounds like to me is that you've kind of got two… two operations happening that are not really related, that you're trying to force a trace relation to. Like, I imagine an HTTP call on one activity, and then you switch to a different activity, and you do a second HTTP call. You're trying to parent those in the same trace, right? Is what it sounds like?
Leonardo Serrano 00:24:47 Yeah, yeah. That's one of the use cases.
Jason Plumb 00:24:50 But those two things are kind of unrelated. They're, like, not necessarily, or maybe I'm missing how they're related for the same trace, trace being…
Leonardo Serrano 00:24:59 Like, typically a trace is, like, a single operation. Yeah. And then the spans within those, distributed or not, are part… they're, like, the components of that operation.
Jason Plumb 00:25:09 And when we've gone, like, a higher level of abstraction above trace, what we have is session. Like, that is the thing that ties all of those together. And it sounds like you are… opposed to using session in that way, or that you want There to be a way to use a trace as a proxy for the session.
Yeah, yeah, basically. Yeah, you've kind of, predicted where this discussion was gonna go. Yeah, yeah, yeah.
Well, cause I think we've had it before.
Leonardo Serrano 00:25:36 Yeah.
Cesar Munoz 00:25:37 If I remember correctly, the thing about Leonardo's use case was that, and correct me if I'm wrong, is that You, you would like to use, Jaeger to… to visualize data, which only works with It spans, so that's why… I'm guessing you would like to have everything as a spam.
If… is that correct?
Leonardo Serrano 00:25:59 Yeah, yeah, well, Jaeger, or some other, like, third-party thing, honestly, I just use some special thing that I, like, built quickly, so it's just, like, a really specific thing that, like, ties, spans and logs together.
Jason Plumb 00:26:16 Through the session, right?
Leonardo Serrano 00:26:18 Yeah, yeah.
Jason Plumb 00:26:21 That's what every vendor does, I think.
Leonardo Serrano 00:26:22 Yeah, pretty much.
Hanson Ho 00:26:24 So… so I think the… this is, I think, one of the key differences between a client user-facing app versus a backend.
is that, to model the execution of backend service, you basically need to model how the process executes. So a trace, that spawns, you know, child spans and things like that, and connects to other traces make total sense.
Because what you need to know about the execution is basically the distributed trace, or the local trace at least.
Versus, that modeling for client apps is not that helpful, because, the interesting things happen Generally as, effectively events, or short bursts things that, can, be parallel, unrelated, and or overlap.
So, to take the same model as kind of the back-end traces, and to model, kind of, the execution of the process, you basically get this, what we used to call Uber Trace, which models, like, the span, or rather, the process, or a session, and then you have everything kind of being children of it. But some of them are unrelated, and some of them are you know, started by other things. Like a background job kicks off and, you know, starts uploading a file. The user taps a button, which, you know, does a bunch of things. Those can happen concurrently. Network requests you know, who knows who triggered it? So there isn't this niceness of, oh, whatever happens in this process belongs to this kind of flow, because the flows are kind of, you know, potentially unrelated, triggered by who knows who.
So, this is why the session ID is useful, because it effectively is a cross-cutting thing, where, you know, anything happening during that time is declared part of the session, and it doesn't have a parent-child relationship, necessarily, with anything, it just is associated with it.
So if you can think of it as not a… tree, where most, traces, you know, effectively can be that.
The client execution, or the session of a client-facing app, is effectively a bunch of potentially unrelated, events and traces.
So, in that case, it really doesn't, by default, it makes sense, by default, to say, hey, there's an uber trace. Now, what can make sense is for specific apps to model their execution that way.
And in that case, if an app wants to… yeah, I was just gonna, reference that. If the app wants to use, some sort of trace ID, as, like, the Uber Trace, you can provide your own session ID and, you know, effectively tie this up together. And Jason is showing the API that allows that to happen.
Jason Plumb 00:29:19 Yeah, if you wanted to manually create a long-running trace on whatever time boundaries you wanted, or whatever event activity you wanted. You could start a long-running trace, you could get that trace ID, and you could… create your own implementation of the session provider and plug it in at creation time, and then that session ID that's returned could be the same as your trace ID. Like, so you could tie it all together that way. It's kind of a lot of plumbing.
But it's possible. It's just not a standard use case that we think that most developers or most RUM implementers are really interested in, I think.
Leonardo Serrano 00:29:58 I see, okay. Yeah, I'm interested also in, like, the… the semantic way of, like… opinions on the semantic way of how to think of, like, a root operation, because I think the two camps are, you know, you can think of it as a session, or you can think of it as a… like, I think, Jason, kind of what you were saying, like, thinking about it maybe as an activity, since… Things that happen inside of an activity kind of, like, make sense to be grouped logically, but things outside maybe not quite as logical to group them together.
Jason Plumb 00:30:27 So, for me, my answer to this is, what is the root operation? It's the session. It's when you've launched the app and the duration for which you use it. Like, that is the session.
We… it comes back, once again, to us also not having a concise definition of what a session is.
Leonardo Serrano 00:30:46 Yeah.
Jason Plumb 00:30:47 And I think that would also help somewhat here, but it's… It's challenging.
Hanson Ho 00:30:53 October, maybe for October to get this stuff up and down.
How could you…
Jason Plumb 00:30:57 How could you even tell I was looking at your avatar? Or your video?
Hanson Ho 00:31:02 I look at myself when people mention Session.
Jason Plumb 00:31:05 I haven't documented this, because it's been in the back of my head for… I mean, it's also just not all on you. I mean, anyone could… could start this work, and we could talk about it and figure it out, but… Yeah, I know. Yeah, having… having, words written down that we could point to and say, you know, this is the route operation, or we've described it over here, and this is why or how it represents a launch and activity, like.
That would maybe be to help.
to reduce some of this frustration, but I also… I totally understand the need to be able to see these things associated in a tool, and there's just no good off-the-shelf tool to do this.
Hanson Ho 00:31:40 Well, yeah, I think that's the other part of the equation, is that the existing tooling, especially, you know, for visualization, still assumes a very back-end-centric way of looking at distributed traces. Yeah. It would be… Amazing for there to be, like, something fairly generic, even simple, to basically say, oh yeah, look at this attribute as, like, a session, and visualize, in a timeline kind of sort of way, you know, stuff that happens, associated with this.
I don't really think that's that difficult to build, given the existing, you know, stuff that's out there, but it's just, like, a mentality shift.
Concession ID is already a semantic convention. So to, to basically… we're not saying, hey, build off something random. We're basically saying, hey, build a UI visualization that understands telemetry, you know, with session ID as its, you know, singular thing that ties together.
But, you know, back-end traces is still how commands and traces are being visualized, so until that changes, it's gonna be hard. But hey, be the change that you want to be, kind of, you want to see.
Jason Plumb 00:32:54 Yeah, I mean, I think we floated this idea of even approaching the Jaeger people to see if they're open to helping with this.
Like, by having some sort of other… correlation or grouping ID that you could… leverage in the UI, whether it be session or arbitrary or whatever.
like a, I don't know, like a rum mode? That would be so cool. Like, launch Jaeger in rum mode? Oh… We have the same problem with the sample app, even. Like, our demo app, when you launch the demo app, you have to have these two disjoint back-ends. You have Jaeger, and then you have… well, we haven't wired up OpenSearch yet, but that's what it would be for your logs, and they just don't share data. It's like, it sucks.
So, yeah.
Hanson Ho 00:33:37 you'll get there.
Jason Plumb 00:33:38 I respect that pain, Leo.
Leonardo Serrano 00:33:41 Yeah, I think this is an issue of, so, my instinct, and I think the incorrect instinct, is to solve this with data and not, like, a different visualization, right? So my instinct was, how… you know, Okay, I'll just tell you what my instinct is.
it might be a silly thing. Sure. My instinct was to just literally overwrite, somehow, the trace ID as session ID. Basically, you could imagine for every session, generate, basically that the trace ID is generated as… with the session provider.
That is, like, the ultra, super, super naive way to reason about this. And this kind of, like, you know, within existing tooling, this gives you that… grouping out of the box. Of course, just solely on session ID, and I think, you know, you'd want to be able to group off of different attributes as well, but this is… you know.
Just the most naive way to think about it.
Jason Plumb 00:34:42 Yeah.
Hanson Ho 00:34:43 I think it's an interesting thing to build, because what this is describing is, like, you know, as I said, like an Uber Trace that basically uses the process as a route, and everything is, by definition, you know, coming from the process.
So, while your kind of disparate workflows within the app may not be related, they can all be rolled up to the process span. And the process span, could then, I guess, if you want to kind of chop that down further, is have session spans below the process spans, and those ones are the ones that effectively, you know, change every time. So I think this would be an interesting implementation of the session provider.
which is, like, the UberTrace provider, which I think, would be useful to some people. But, I definitely wouldn't want that to be a default, because I think there… There's a bit of, like, modeling and kind of conceptual mismatches, for the general use case, but there is a use case for which this makes sense.
So I would encourage you to actually, use a session ID provider and make an implementation, that effectively, does what you want. I think it's doable, and I think it's… it's going to be useful. I think a lot of this stuff is… is… Android is… can be used in so many different, you know, places.
having different implementations that do different things. Like, for auto manufacturers, for instance, if you use Android Auto, like, I think this makes a lot of sense, because there's not a ton of stuff that, that, that you don't want kind of tied together. Kiosks, things like that. So if, if your use case Would benefit from, you know, having this, or at least you want to try it out.
Go right ahead, I'd love to see it.
Cesar Munoz 00:36:29 Yeah, and also, like, I think it's fine, because you're just trying to work with The tools that are available right now, which are not great for displaying session predator stuff.
So… one way that, if it helps, probably you're already aware of this, but if it helps, the… at least the Java SDK, the way that it propagates context is via threads, thread locals, so… I haven't tried this, but probably one way to create an Uber… Trays?
Could be by starting it… starting a span in the application, on create, setting it as current, that should attach it to the main thread.
And then every other span that you create on… in activities, she'll get… she'll become children.
of this… of this application span. It's just that you have to make sure that the application span is ended.
You know, when the app is closed, otherwise we'll lose everything.
That could be, a way to work around it, I think.
Hanson Ho 00:37:38 That's also an issue with long-running spans, is if there's a crash, then what happens? So…
Cesar Munoz 00:37:47 Yeah.
Leonardo Serrano 00:37:49 Yeah, I'd love to see something like that, and I have hesitated to try to build something like an activity span, solely for that reason, the reason that you're mentioning, Hansen.
With long-running spans, you introduce a lot more risk of data loss, you introduce more state management. It would be nice, though, to have, like, long-running spans for activities, even for sessions as, like, a configurable, optional thing in the default, OpenTelemetry REM configuration, but…
Hanson Ho 00:38:25 Yeah, the idea of supporting a long-running span, I think, is very much in, I think, many of our heads.
I think there's a whole bunch of small things that need to happen in order for that to happen. Embrace has a solution called Span Snapshots.
Basically, at the end of a session, we take all the snapshots of running spans and send it, you know, it can effectively treat it as, like, logs, because there's not… those are not real spans, it's not done, but they contain state that, you know, could be useful. We persist it, and we resurrect it, if… if there's a crash, But, you know, that's kind of all outside of hotel. And, you know, once… to push it back into OTEL, you know, it has to be… it has to be one span. It cannot… it has to be, like, done. So it's almost like we do a bunch of buffering and caching, on… on the client side. And then, you know, when we know that span is done, we send it over, which, you know, ideally is not what we do, because it is a bunch of work.
But it is something that kind of can work, in the meantime.
Jason Plumb 00:39:35 And I will add that in the APM world, at least, a long-running span is often a sign of an instrumentation bug.
like, a long-running trace, like, if you have a trace that's running for more than several minutes, like, that's almost always, like, you've got… you've got instrumentation that, like, didn't properly close scope, so it ends up being, like, a bug, at least in the APM world. And when you see these long-running traces that have thousands of child's bands, like, that's… it's like a smell. It's like, you know that there's something wrong with the instrumentation when you see that, so… I also added that, just, this is, like, stupid, but, like, the original question was about, like, IDs, and I wanted to be clear that we're not actually talking about IDs, we're talking about more of, like, the concept. And the reason I want to make that clarification is because our current default implementation for the session ID, like, the actual ID value.
is a trace ID. Like, and that's just out of convenience, right? Like, there's some benefits you get from reusing that, but, you know, it wouldn't have to be.
Leonardo Serrano 00:40:37 Yeah.
Jason Plumb 00:40:38 Yeah.
Leonardo Serrano 00:40:38 No, no, I totally get that. We're talking about the concept. Actually.
In the thing I'm building, I just decided to go with, UUIDs.
Jason Plumb 00:40:47 Yeah.
Totally.
Hanson Ho 00:40:50 Whatever's unique, whatever's fast, ideally, if we have a bunch of them, it stores really well, and compacts really well on the back end as well, so…
Jason Plumb 00:40:59 Alright, in the interest of time, are we ready to move on?
Leonardo Serrano 00:41:02 Yeah, yeah, thanks for the thoughts, guys.
Jason Plumb 00:41:04 Yeah, yeah, cool, Leo, thanks.
Alright, Jamie and Hanson talking about the Kotlin API, oh my gosh!
It's happening.
Jamie Lynch 00:41:14 It's happening.
Yeah, so a bit of context for everyone. Base, we've been working on a Kotlin multiplatform implementation of OpenTelemetry. We started off with, just an API, but… wrapped the OpenTelemetry Java SDK.
We've been working on a Kotlin implementation as well, so you can kind of choose which one you want to move between. And yeah, we basically got it to the point where we feel comfortable Basically opening up a donation proposal.
So, yeah, like, we're hoping to kind of, like, get a bit more community involvement at this stage, Yeah, Hanson, anything to add, though?
Hanson Ho 00:42:07 So I've been converting Android to basically use this, and I basically have it, like, on a branch somewhere. It works, all the tests pass, The main difference is that, scope?
And managing contacts, by thread local is explicitly taken away for very explicit reasons, but they could be worked around, and, you know.
So, I think the goal for us is to get this in, get this… So the first thing is the API, because right now, the API says I owe.embrace.O.Telemetry. We don't want to pollute the namespace until we actually get in.
So once the API becomes official, it would be nice to start, on the Embrace side, exposing it, officially under… not under experiment, and also for, the, the Android open the LG ADR2, use this somehow. So, the interface doesn't have to change, initially. So, internally, like, like Embrace right now, we've exposed Java interfaces, but we use the… Internally, we use the Kotlin API with the adapter implementation, so it's basically Java SDK in the backend, so everything kind of works as it is. So I think that'd be a good first step to kind of, you know, introduce this, to, to OpenTeLP Android. And then eventually, as we Can build out the support.
you know, figure out, flesh out the instrumentation, you know, convert everything to Kotlin.
Then… then I think there's a lot of, potential in the future to, you know, get rid of de-sugaring, because it's gonna be all Kotlin and, you know.
A lot of interesting things, and we can start, like, thinking, What we could do to improve.
usability, and all that. So it's… it gives us control, because the SDK not only… not only is the Kotlin API, like, the idiomatic way of Android development, but also we can start doing, things, And adding things that are in the API that is, I think, more client-friendly.
So I… the… so hopefully the donation, if it gets accepted, will create a separate SIG, like the OpenTelemetry Android sig… or, Kotlin SIG, similar to the relationship, the JavaScript SIG and the browser SIG, where, like, one kind of hopefully uses the other. They're closely related, but have different goals, because multiplatform is… is explicitly something that we wanna… we wanna do, and, and Android is just a platform.
probably the platform. So, you know, it's a privileged, first-class citizen kind of thing.
But yeah, we want people to be involved, so please go in and look. We are looking for contributors and maintainers, Right now, the… the three that we have are, you know, the three people at Embrace working on it. But that's… that's a… very much a, a for-now state. We definitely want people to kind of jump in.
demonstrate that they're going to be long-term, you know, working on this project, and, yeah, get them to maintainers. So, if you or somebody you know, might be interested in this, especially somebody you know that may be just using the Java SDK right now, not the Android package, because they want to do something different. This may be a good alternative for them, to take a look at.
Cesar Munoz 00:45:51 I… I would also like to add one more benefit that I think it… we might get.
From this new implementation.
Which, it's probably a bit subtle, but I think it's huge.
Which is that… If we swap, hotel Java with… Hotel Kotling, We might be able to get rid of the, the, a minimum API stuff, Corely, the sugaring requirement.
Jason Plumb 00:46:27 Oh, yeah.
Cesar Munoz 00:46:29 that we have inherited from… from AutoJava, so… I think that's huge. So, you know, thank you for this, for this. This is great.
Hanson Ho 00:46:40 Yeah, for the embrace SDK, we had to add the sugar ring stuff, because we pulled in the, what is it? The, the semantic convention repo, because that had… that used, default, interface implementation.
Jason Plumb 00:46:56 Yeah.
Hanson Ho 00:46:58 Which is, like, so weird, and it seems so unnecessary to force that, but, you know, it is what it is.
Jason Plumb 00:47:05 Yeah, that's, something that could also be part of this. I mean, we could generate those constants in a more Kotlin-friendly way as well, right?
But nothing to prevent consuming that metadata and generating Kotlin classes.
Hanson Ho 00:47:20 Oh, boy.
Jason Plumb 00:47:20 work, you know?
Hanson Ho 00:47:21 we are… we are explicitly part of, you know, I think, hopefully you have a ticket for this, is to create an OpenTelemetry Kotlin semantic convention. I mean, it's all generated from the same metadata, right?
Jason Plumb 00:47:31 So, dude.
Hanson Ho 00:47:31 there's gonna be a bit of, you know, maintenance, kind of keep… when the builds break, you're like, oh, I gotta figure out how to do that. But, you know, to use it in multiplatform, it has to kind of be called anyway, so that's definitely, you know, on the roadmap.
Jason Plumb 00:47:43 Yeah.
Mustafa Haddara 00:47:46 Can you, you mentioned earlier that there were some… changes to context propagation? Can you go into more detail on that?
Hanson Ho 00:47:55 Yeah, explicitly, we've… So I think we're gonna come up with a doc to basically say, these are the differences in terms of API, but that is actually an SDK, kind of, you know, behavior change. So previously, context is stored in, thread local context storage, and there is, in the SDK, a current And also a bunch of methods, this is, like, setCurrent, you know, things like that. All that is gotten rid of in the, in the API.
if you use a compat implementation, it is, we… we emulate the same behavior. So you basically, you know, we expose the, because obviously using the Java API, so you have access to the, you know, all that stuff. There's no… I don't think there's a scope… is there a scope object, Jamie?
I don't think there is, right?
Jamie Lynch 00:48:49 So, yeah, I think basically, if you want context right now, you set it explicitly on a span or a log. I think in the future, we'd probably be interested in coming up with some sort of solution for setting implicit context, but we want it to work across Like, various different platforms.
Hanson Ho 00:49:12 Yeah, we're thinking of… one thing we're thinking of is… is an explicit named context, so you can basically declare the context you are… the route, because we do want the… we do want… we want… we want the convenience of having something that you could say, hey.
I am part of this context. If there's a parent, stick me under that, or something like that. But make it somewhat explicit. But I think the first step in the SDK and the API is to just not have that as a concept of default, which, you know, implicitly is what JavaScript is doing as well. So this is not going to be like, you know, we're so out there. JavaScript also doesn't have the concept of… or doesn't have a durable concept of current.
So, you basically manage your own context, everything's created from root.
But you can… you can force a… a current route if you want.
Mustafa Haddara 00:50:12 I mean, JavaScript doesn't have it on by default, but they have a context manager implementation the… can be… I'm not gonna say everybody uses, but it's very common, right?
Like, I think the, the, like, I'm gonna create a span, and I need it to be under whatever current active span exists is… A very important use case.
And it's like a pretty big foot gun if people are able to create spans, and then they don't see them nested under the parent spans that they would expect.
Hanson Ho 00:50:51 Yep. So that's a next step, is to make an API, that is, I think, client-friendly that does that, because it's also a foot gun.
To basically say, you know, hey, whatever threat local, we're cool. If you have instrumentations, that are competing, or you have even, like, you know, two teams in the same company working in the same app.
who see context differently, or who, you know, make a mistake, you know, then instrumentation could be also, you know, fucked up by default. So, I think the JavaScript one, it works sometimes, it doesn't work other times, is what I've been told. So, even that is… using that is a bit fraught.
But we understand how important this is, and certainly if you use the API with the Kotlin, with the Java SDK, everything works as expected as previous.
And we are looking for an API solution, to this that would be easy to use and amenable to those who want this behavior.
Cesar Munoz 00:51:58 Broly!
You already saw this, but I'm aware that I think that even the creators of Java don't like thread locals, I think.
And I think they have worked on a replacement for the latest versions of Java.
I think it's called Scope Values. I haven't never used those.
But I'm not sure, I'm just mentioning in case… whatever abstraction they have come up with, I'm not sure if… it might be… A good inspiration, probably, to… use.
In this SDK, maybe, I'm not sure.
mentioning something that I think might… might help.
Hanson Ho 00:52:46 Cool, take a look at it. Scope… scope values is what it's called?
Cesar Munoz 00:52:50 Yeah, scope values.
Let's scope.
values.
Jason Plumb 00:53:00 Yeah, there's a bunch of that stuff. I think that's interesting. I want to make sure we have enough time to at least start talking about this. I think that, this is awesome work, and I think the community will definitely appreciate this. I think getting… people to help out might be a bit of a challenge. I… I hope… I hope this happens, though. It's really awesome, especially for Android.
I also hope that there's a way to maybe… bring stuff in, like, assuming it gets approved and we get maintainers, like, I hope there's a way we can start bringing stuff over piecemeal, and it's not just, like, like, all of… like, here's the entire API, here's the entire… like, if we could bring over, like.
Bits at a time, you know, bring over context, bring over spans, bring over metrics, bring over logs, like, you know, as, like, units that can be… reviewed more easily, handled more bite size, and by bite size, I mean it's still a large sandwich, but, you know, it's not… It's not a warehouse of sandwiches.
Okay.
We have 7 minutes left, I want to make sure we allow time for this one.
Mustafa Haddara 00:54:05 Yeah. Open-ended question, like… where are we going? What's our… do we have a path to 1.0? What's the roadmap like? Are we gonna be stable? Are, like… what does that look like? Are we just gonna sit in… in unstable? Oh, we're not… we're not 1.0 yet, we can make breaking changes whenever we like mode forever? Like, what's the… I'm sorry if this is coming off as a… this is not supposed to be aggressive, I'm just trying to get a sense of, like, what the roadmap is and stuff, you know? Hands and smiling.
Hanson Ho 00:54:40 If that's aggressive, then…
Jason Plumb 00:54:46 No, I think it's a great question. If we scroll down here, I'm sure that we can find, cases going all the way back to March 12th of 2024, when we're thinking about the 1.0 roadmap. So, it's not, you know, not necessarily a new concept. I… understand why you're bringing this up, because I have heard from the same source, that there is some… some fear in the industry from, users who want to adopt OpenTelemetry, specifically on Android, but they're… they… like, the perception right now is that this, project is not… Not yet mature enough, not yet stable enough.
And frankly, that does not seem entirely inaccurate, because we don't have a roadmap published, and we haven't made a 1-0 yet.
But there is also this chicken and egg problem, right, where we are looking for users who are actively using this, contributing feedback so that we can improve it and have robust, stable, extensible APIs.
That address users' needs, and figuring, like, and having that circular feedback loop to really make stuff stable, so… Without that, you know, it's a little bit difficult. I'm curious, from other vendors, are you yet using, OpenTelemetry Android? Not Java, are you using OpenTelemetry Android in your distro at all?
It sounds like, no, it sounds like Splunk might be the only one.
Cesar Munoz 00:56:17 No.
Leonardo Serrano 00:56:17 Question?
Jason Plumb 00:56:18 Yeah, the question is, are you using OpenTelemetry Android or any pieces of it in your distro distribution?
Leonardo Serrano 00:56:24 Oh, yes, yes, I am directly… for the distro that we're building, we are directly consuming it.
Jason Plumb 00:56:31 That's AWS, right?
Leonardo Serrano 00:56:32 Yep.
Jason Plumb 00:56:33 Boop.
Mustafa Haddara 00:56:34 And I'm from Honeycomb.
Jason Plumb 00:56:36 Are you using it?
Mustafa Haddara 00:56:38 We're using it, yeah.
Jason Plumb 00:56:39 Oh, I didn't know that, okay, cool.
Hanson Ho 00:56:43 I feel like in the Android world, we're less… we're less, what's the word? Reticent to use, quote-unquote, not 1.0 stuff. If it's demonstrated to be okay, our tests are passing, things look okay, we tend to use it. So maybe this is one of the reasons why, you know, there hasn't been a huge push to kind of stabilize, externally, I should say, and declare 1.0.
But I can certainly see some other folks who are… who are new, coming from back-end world say, hey, we want this to be declared stable before we could.
use it. I mean, API changes, a lot of times are fairly trivial to kind of change and fix on a client app. It's not that way in the backend, so I definitely understand the consternation.
So, to be honest, I mean, you're searched March 2024, that's… it's a long-ass time.
Jason Plumb 00:57:39 Yeah. Yeah.
Hanson Ho 00:57:40 and we have a bunch of stuff here that we've labeled 1.0 required. Maybe we should just see if these are truly 1.0 required, and… and… because if… if we have four companies, and I think there's probably more, who are using it in production, it is de facto, assumed to be fairly stable.
So, what, what, what is to say that we can't just declare our next release 1.0? .
Jason Plumb 00:58:10 It's true, that's a really good question, and that is the main gating factor. It's up to us. Like, if we choose the next release to be 1-0, we have that… I mean, there's probably, like, some, you know, thumbs up, thumbs down we want to hear from the TC, but, like, we… I think we have that autonomy to declare something 1-0, for the most part, and… We certainly could do it on the next release. I think I would be hesitant to do that yet.
But, go ahead, Cesar.
Cesar Munoz 00:58:38 For me, I was gonna say, I think if… I would be happy with going with version 1.
Thoro, if we for… just by feeling confident about the initializer API, which I think is what… You know, most end users, she'll, she'll use.
I think it's… I mean, I haven't heard much, complaints about it yet, yet, at least.
The one that I remember is that somebody wanted to provide their service name through it, which is not possible right now. Probably, you can just add those.
that parameter, and I created recently a PR to make the instrumentation config a bit that's painful.
Jason Plumb 00:59:21 Yep.
Cesar Munoz 00:59:21 So, I'm really not… I don't think we're far away from… from 1.0, and probably next, SIG meeting, we can go through this list of issues and see if they're still required.
And maybe before that, Mustafa and anybody else, if you think there's something missing, maybe we can… I mean, if you could create an issue and tag it with this label.
Probably they'll… that'll help too.
Jason Plumb 00:59:52 Yeah, totally, for discussion, yeah, I mean, and if you don't have the ability to label, just holler at me or someone else to put the label on it and discuss it. Like, if there's… we have 95 issues, and if some of those you think are mandatory, like, we've talked about NTP, I think… that was not super contentious, but there was some other stuff that, like, do we really need that? Is that required? Like, we should continue having that discussion. Cesar, that's a great idea. I love it, and I want to just… I'll front-load that for next time as well.
Cool.
Cesar Munoz 01:00:22 the two.
Hanson Ho 01:00:23 the two things that we need really to be, you know, doubly sure of is the API surface area that we expose, and any, like, you know, killer bugs.
I think the killer bugs we would have, we would know by now.
Jason Plumb 01:00:38 Yep.
Hanson Ho 01:00:39 So, really, it's about whether or not the APIs we've exposed as something that we will break. We want… we may want to break in the short you know, in the short term. And if we do that, if we have those, let's just break that now. I think adding APIs is okay, in 1.1. It's just like, hey, we changed our mind about the initializer, as you said. That's the kind of stuff that we don't want to do, so… Yeah, and on that document, too.
Jason Plumb 01:01:06 I'm gonna throw that on the pile, too, because no one wants to do it, but we need it so bad.
Hanson Ho 01:01:11 What kind of documentation? So, so I think there's, there's, like, API documentation, and there's also, like, you know, usage, you know, example-type documentation.
Jason Plumb 01:01:19 Yeah, yeah. I mean, I think that's a huge detractor from adoption, and we're at time, sorry. Okay, let's continue this discussion next time, I think it's great. So we've got to bump to the top, and we can spend a bunch of time, hopefully, hashing that out, but in the meantime.
Everyone, thank you. It's been awesome.
Mustafa Haddara 01:01:39 Thanks.
Cesar Munoz 01:01:40 Thank you.
Jason Plumb 01:01:41 Okay.
Leonardo Serrano 01:01:42 Thank you.
Mustafa Haddara 01:01:43 Yep.
