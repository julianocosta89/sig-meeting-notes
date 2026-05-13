SIG: Android SIG
Date: 2026-05-12
Duration: 61 minutes
Zoom Recording URL: https://zoom.us/rec/share/UGSBa4jHWclQtaq_9q2TV2wSp7ZjPvzZDZJti16sNyy13RXhDdkaMwGsT0_yKTPe.rptsQI5zdoXh3Zwc
============================================================

## Zoom Recording Transcript

Jason Plumb 00:04:44 Let's give it another minute and see who shows up.
Cesar Munoz 00:05:16 Edo, good morning.
Jason Plumb 00:05:18 Hey, Cesar.
Sounds like Jamie won't make it, and if he's in the office, I don't know if that means other people are doing embrace stuff, but maybe Hanson won't make it. I don't know.
Cesar Munoz 00:05:35 Yeah I think he only mentioned… Himself, not handsome, but…
Jason Plumb 00:05:43 Yeah.
Cesar Munoz 00:05:44 Yeah.
Jason Plumb 00:05:45 We'll see where it goes. Yeah, we'll see who shows up.
Cesar Munoz 00:05:50 Yeah.
Jason Plumb 00:05:53 Cool. So, we can get started.
Oops.
Brain's still waking up.
Yeah, so I put this in here, I think, on Thursday, maybe after the Java SIG last week.
We borrow a lot of, kind of, prior art from their work, and one of the things they're doing… It's probably gonna take me a minute to find it, because I'm not really prepared, but let's see.
Cesar Munoz 00:06:39 Oh, it's the, AI… got it, the… for the release notes.
Jason Plumb 00:06:44 Yeah… I don't know how I'm gonna find this.
Cesar Munoz 00:06:52 I didn't know about it, to be honest, but I think it makes sense.
Jason Plumb 00:06:56 This one…
Cesar Munoz 00:06:57 Sounds handy.
Jason Plumb 00:07:01 Yeah, so they're using this classify.py… Oh, no, this is a different thing. Make draft release notes classified robust.
to multi-object LLM responses and slow agent runs. So I think this is already in place, but they're using this thing… they're using, like, a small model.
To help, you know, do the release notes, because… What we get when we run our automation is pretty basic, right? Like, we just get the titles of the pull requests, and we get all of them.
So, like, this one, right?
when we do a release, this is what we're looking at, and it comes out like this, and then I think we just… I think I just copy-paste it.
Cesar Munoz 00:07:44 Yeah, me too.
Jason Plumb 00:07:45 Yeah, so we can start with this, and it's pretty long, and it takes, I don't know, it takes me, like.
20 minutes, depending on the size of the change set, but, like.
being able to, like, go and decide, first of all, which ones we want to include, but then to basically, like, rewrite these titles from the PR titles, and give a little, you know, one or two sentence, like, actually helpful description of these, especially the important ones, like.
like this, I don't know, I'm just picking on this one because it's on my screen.
I don't know how that looks, like, alter how Android instrumentation is loaded. That's probably, like… there's probably more to be said about that, something more descriptive than, we changed it. Like, how did we change it? What's the impact, you know?
That's kind of stuff. And so they're doing that.
And we could maybe look to borrow some of that.
Cesar Munoz 00:08:33 Yeah, sounds good. So I'm guessing this tool will have to… all the PR's metadata, to see… actually, you know, try to infer a better description, I guess.
Jason Plumb 00:08:51 Yes, and I think it might require a token, maybe a co-pilot token or something, I forget, but we can… we can ask.
Cesar Munoz 00:08:58 Yeah, sounds good.
Jason Plumb 00:08:59 Yeah. Okay, well.
Cesar Munoz 00:09:01 I'm not sure how… Yeah, I'm all up for it.
Usually… what I've noticed with this kind of tools is that they're not free, so the.
Jason Plumb 00:09:13 I know.
Cesar Munoz 00:09:14 the, but I'm guessing… OpenTelementary has some tokens available, I guess? I'm not sure. If they did it, there should be.
Jason Plumb 00:09:25 Yeah, I think we do. I think we have a little bit of Copilot, but I think Trask was using something from himself, Let's see if… I think there might have been a link to this from last week's notes. Let's see.
No. Wait, is this coming up?
That was last week.
I thought we mentioned it, but, it wasn't this one.
No.
Well, I've lost track of it, but anyway, it's out there, we can look to borrow for some of that, but I'll create a tracking issue, how about that, and then I can start putting resources in there and do a little research.
Because right now, I don't have much to go on, but it sounds like you're open to it, I'm open to it.
Cesar Munoz 00:10:16 Yeah, yeah, definitely. I'm reading what David said.
So it sounds like it's, Trask's… personal tokens.
Jason Plumb 00:10:24 Okay.
Yeah, thanks, David. Yeah, appreciate that.
Yeah, I think he did. I think he was talking about adding it… I think they were talking about adding it to the Java repo, not the instrumentation repo, and Trask offered to put his token in there, so… Got it. I don't know what that looks like or what token, if it's Copilot or what, but… If it's… if it's some… there's, like, some mini models that are, like, free, and I think that's what they're using, but I think it still requires you to have… An auth token, even if it's not billed.
Cesar Munoz 00:10:55 Got it. Now that we're on the, on the topic, I've also, thought about… the… the co-pilot Reviews that they have in other repos.
Jason Plumb 00:11:09 Yeah.
Cesar Munoz 00:11:10 It could be something… that might be helpful. I know, it's not like… it's not something that we… It's not… it's not… it's not enough.
for those reviews to, you know, to get a PR merge, but sometimes I… you know.
Catch-up stuff that, that, that, you know… Annoying to… to… having to review manually, so… Probably that's another thing. And I think for that one to work.
It might be a bit easier.
Jason Plumb 00:11:46 Yeah, I think… I think there's… I think we will need to go through a process of, like, revising… the guidance on this stuff, because I think if you just turn it on right now, you get tons of comments, and a lot of them are often not that helpful. But I think through… instructions to the agents, you can kind of dial that in, and I think they've done a pretty good job in some other repos, too. I don't even know what it takes to turn that on, do you?
Cesar Munoz 00:12:12 No.
I think it's just… yeah, no, broadly.
Jason Plumb 00:12:16 Like, right now.
Cesar Munoz 00:12:17 Click this, it's like…
Jason Plumb 00:12:19 Yeah.
I don't know.
Cesar Munoz 00:12:24 I think something should be enabled in the GitHub folder, some file, I don't know which one.
Or maybe we can have a look at the… I think I've seen it a lot in the country one.
Jason Plumb 00:12:35 Okay, why don't you create an issue to track on that one?
Cesar Munoz 00:12:39 Yeah… Yeah, that sounds good. So it sounds like you're… open to that, Ryan, just wanted to confirm.
Jason Plumb 00:12:47 I am. I mean, it helps to have help, and that is a form of help. I don't… I don't love the idea, and we've definitely had some PRs where Copilot just clogs it up with stuff, so I want… I think we need to be a little bit careful with it, like any tool, I think we need to make sure it's configured to our liking, and that we have some policies, or some words drafted about how to close those out, or how to… How to keep it on… on track.
Cesar Munoz 00:13:18 Yeah?
Jason Plumb 00:13:19 Yeah.
Cesar Munoz 00:13:19 I'll have a look.
But I think it's… It's… it's probably… this is the file that's probably related to… That work?
But yeah, I'll take a…
Jason Plumb 00:13:33 I think it still has to be enabled, though. Like, this is cool.
But I think you… Yeah, this is great. Like, this is… this kind of stuff, yeah.
But I don't know, I still don't know how to enable it.
Cesar Munoz 00:13:52 Me neither, but I'll figure it out.
Jason Plumb 00:13:54 Okay, yeah, I don't think it's that. They're doing it everywhere, so I don't think it can be that bad.
No.
Alright, do we want to talk about Instrumentation API?
Cesar Munoz 00:14:06 Oh, the, yeah, there's… we're stabilizing it, yeah. I think it's… To me, it's ready to go.
Jason Plumb 00:14:16 So this release… next week, I think?
You know, if I'm curious about, I'm curious about when we're gonna do the next release. I've made this really ridiculous GitHub page that has this stuff.
And I can just choose OpenTelemetry Android. And so, next week.
Cesar Munoz 00:14:33 Oh, that's… this is pretty cool.
Jason Plumb 00:14:35 I can put a link to this in there. These questions come up all the time.
Cesar Munoz 00:14:42 Can probably leave it as a, you know, pin… Link at the top.
I think it's pretty cool.
Jason Plumb 00:14:49 It's just got Splunk stuff in here too, so I don't know.
Cesar Munoz 00:14:52 Okay, good guy.
Jason Plumb 00:14:56 And it's always the backtrack. I don't know if this happens with you and your distro, but, like, it's like… when is your distro coming out? And then you have to track back to the dependencies, so that's what I get all the time.
But, like, Java just released, they won't come out for a month. Instrumentation, end of this week, probably.
contrib… Javacontrib is not even on here, because we forget about it all the time.
So, instrumentation API, I think, is good. I think it's getting… I think we can do it this release.
It's in here, right? Is it this one?
Cesar Munoz 00:15:37 I forgot.
Jason Plumb 00:15:40 It's the one with the installer, right?
Cesar Munoz 00:15:43 Yeah, no, then it's the one… no, it's the Android.
Gosh.
Jason Plumb 00:15:48 This one.
Cesar Munoz 00:15:49 Yeah, instrumentation.
Jason Plumb 00:15:50 Yeah.
And that looks like this.
Yeah, so the install takes a RUM, the uninstall takes a RUM, and they each have a name. That seems like a pretty reasonable API. So, let's do that for this coming release. I think we should.
Cesar Munoz 00:16:17 Got it. Let me create a milestone, just to keep track of it.
Jason Plumb 00:16:25 Yeah, that's.
Cesar Munoz 00:16:25 have already won.
Jason Plumb 00:16:27 I don't think we do.
We can take a look, I don't think so.
Oh, we do.
Oh, look at what's in there!
As we do, never mind.
Cesar Munoz 00:16:55 Nice.
Jason Plumb 00:16:57 So the instrumentation config process needs to be documented.
Cesar Munoz 00:17:04 I don't even remember about this issue.
Jason Plumb 00:17:12 So this was part of the migrating of OKHTTP to the new API.
And… Yeah, just… so this was calling out that, like, if you're configuring an instrumentation, you should do it before calling the Install.
Or, sorry, yeah, sorry, you should do it before initializing RUM.
Because if you do it after the… after the rum is created, then it won't take those into account. Yeah, I'm like, that's an important thing for people to call out, for people to understand.
And so I was like… I want us to be able to have that, like, I want… I wish there were some higher level guidance for instrumentation authors to account for this kind of stuff.
I don't know that it's super high priority, because… I don't know how many people we have writing instrumentation yet.
Cesar Munoz 00:18:11 Yeah, and also, for the, built-in instrumentations, it, you know, the DSL takes care of that on behalf of the users, so… They don't have to think about it.
But, I think, yeah, I mean, it won't hurt having some dogs on it.
Jason Plumb 00:18:35 Yeah, and we could just throw in the docs directory for now, maybe. Let's see… I don't know if there's an existing place for it, but maybe, like.
Instrumentation, or writing instrumentation, something as, like, a placeholder?
Cesar Munoz 00:18:51 Yeah.
Let me create an issue for that. So, like, a guide.
Regarding. Yeah.
instrumentations and… Oh, yeah, which I've seen it in the, in the upstream repo, so… And you can… Take inspiration from that.
So… I'm creating issues right now.
Jason Plumb 00:19:16 Okay, cool.
The other thing that's in the milestone is… This one, which I have a PR for… I think it's gotten no traction.
I know that we talked about it.
We talked about it a lot last week, and then we decided to keep the name the same.
But I don't think there's any been any more… Reviews on it.
Cesar Munoz 00:19:43 Yeah, no, I mean, for me, it's good to go. It's just that… But, like, you added a comment on… Adding docs.
And… I… I think you still haven't added those dogs?
Last time I checked, at least.
Jason Plumb 00:19:59 Was it… okay, maybe that's just me.
Yes, okay, so that's on me. And also, I don't know that this needs to be in the milestone, does it?
This doesn't… I don't think that this touches anything on the API, does it?
Cesar Munoz 00:20:18 ATOS… well, on the, agent.
Yes.
Jason Plumb 00:20:24 On the agent, it does, but it's adding stuff, and the agent's already stable.
Cesar Munoz 00:20:29 Yeah.
Jason Plumb 00:20:30 It doesn't.
Cesar Munoz 00:20:31 Nothing out again.
Jason Plumb 00:20:32 Yeah, okay.
So, should I remove it from the milestone?
Cesar Munoz 00:20:42 I mean, if… I can… I can approve it right away, and we… like…
Jason Plumb 00:20:47 I'll add that Java doc. Let's just get these done this week. We'll leave them in here, even though if they're not maybe mandatory.
Cesar Munoz 00:20:54 Got it.
Jason Plumb 00:20:55 Sound good?
Cesar Munoz 00:20:57 Yep.
Jason Plumb 00:20:58 Okay.
Okay.
What do we think is next after Instrumentation API?
Cesar Munoz 00:21:25 Well, we will have the instrumentations.
themselves.
Jason Plumb 00:21:31 Yeah, but we have other stuff too, right? We have session… Session already is. Sorry.
Cesar Munoz 00:21:36 Yeah, it is.
Jason Plumb 00:21:37 We did stabilize session.
There's services, there's core, And what's in common again?
Cesar Munoz 00:21:51 Oh, Constance. Okay, and…
Jason Plumb 00:21:56 Oh, like every common module that ever existed, it's just a hodgepodge of mishmash.
of stuff.
Huh.
Cesar Munoz 00:22:06 Yeah, I'm not sure we even need that module. It's probably, you know, for historic reasons.
Jason Plumb 00:22:14 Yeah, it'd be…
Cesar Munoz 00:22:15 We have it there.
Jason Plumb 00:22:16 See how that comes into the dependency tree.
Cesar Munoz 00:22:20 Also, for services, They're kind of, They're kind of an internal thing.
I believe.
So…
Jason Plumb 00:22:34 If an instrumentation needs a service, what's the… does it just use the global right now? Is that what… is that the approach?
Can instrumentations use services?
Cesar Munoz 00:22:45 instrument, and yes, and I think they already do.
But… at least last… the last thing I remember was that Only our instrumentations were able to do so, or at least that was the intention.
Because then, if we do market public, then… We'll have to… maintain a lot of calls to the Andri SDK.
That we do there.
We're kind of like… grabbing a lot of Android SDK Golds.
Jason Plumb 00:23:24 Right, so maybe we need to split services into the API, and then an.
Cesar Munoz 00:23:30 Internally.
Jason Plumb 00:23:31 patient.
And we only stabilize the API ever?
Cesar Munoz 00:23:37 Yeah.
Yeah, it could be.
So…
Jason Plumb 00:23:45 Something to think about. Services…
Cesar Munoz 00:23:49 Yeah.
For both services and common.
I think we need to think through a bit what we want to do with them.
Because probably we don't need them as standalone artifacts.
Or… Yeah, let's see.
Jason Plumb 00:24:08 Yeah.
Okay, well that sounds like a problem for another time.
Cesar Munoz 00:24:19 I'll still create a couple of issues.
Jason Plumb 00:24:23 Cool.
I've been trying to create an issue to… Discussed declarative config and haven't done it.
But… We're going to need to support it at some point.
And at some point is probably soon.
Cesar Munoz 00:24:41 Oh, the credit config? Yeah.
To be honest, I'm not… I'm not in the loop of how is that, you know, what's the progress on it, but I've heard that it's already used in the upstream as a gay.
So… It's… it sounds like it's already stable.
Probably?
Kind of.
Jason Plumb 00:25:08 I think it is… I think the spec… I think the spec is stable.
I'm not sure if… Yeah, I'm not sure if it's considered stable in upstream Java yet.
But it's there, and people… people can use it. Like, it's… yeah, it's… There's been a lot of work on that recently, and I think Jack Berg had an announcement… Let's see, thought it was over here, this thing.
So back in March is when the spec got stable.
Let me just link to this.
Cesar Munoz 00:26:04 Thank you.
Jason Plumb 00:26:07 And… So that's the… that's the schema, YAML… the data model… YAML mapping… Other stuff, and then… what's the status of language implementations? They're available… But it doesn't talk about stability.
But, spec compliance, let's see what that says about it.
Cesar Munoz 00:26:41 My understanding… and please correct me if I'm wrong, is that whatever you do there in that YAML file will translate At runtime, into… an OpenTelemetry object that's created using those parameters from the YAML file.
So, I think it comes… it… it brings, it brings a challenge.
for Android.
Because… Of the runtime, of how Android Runtime works.
And what kind of configuration?
Like, where you want to provide it. Because if it's, like, in your project.
Then, you know, we're gonna do this reading at runtime, From the disk that… it's probably fine. I don't get… I don't think it will become a huge file, or something.
But, but, but, there's also the option of… somehow turning that YAML file at compile time into code.
That can be… Probably statically referenced.
At runtime, or something like that.
I mean, there's ways… to go about this, and I guess we don't have to make a decision right now, but I wanted to… mention it.
I guess the… The downside of the latter is that that configuration won't be dynamic. So whatever you put there in the project, it's… You know, it's fixed.
Jason Plumb 00:28:32 Right, right. Whereas if it's an actual file on the device, or a file that ships with the app, it potentially could be modified. Like, if your agent was talking op-amp to a server somewhere and getting config changes, it could modify them on disk, and then on app restart, and I'm saying disk, but on device, and then on app restart.
It gets new configuration, right?
Cesar Munoz 00:28:54 Yeah.
Jason Plumb 00:28:58 Yeah, that's… that's interesting. I mean, I think it might be worth also exploring Some benchmarks and get a realistic sense of, like, how much how much startup time are we talking about to load the file from the device, and to parse it, and to create the SDK?
Cesar Munoz 00:29:19 Yeah.
Jason Plumb 00:29:21 So we have that… we have that thing in Core that's still the pre-configured OTel SDK thing. That's one way for Android to go forward, right, is we could use declarative config to create this pre-configured OTel SDK that we then pass into our… our pre-configured OpenTelemetry Rum Builder, and then what we get back out is the… we can create the OTEL RUM instance with that. Well, what it doesn't account for are all of the custom Android pieces that aren't specced in the declarative config spec?
Cesar Munoz 00:29:54 Right.
Jason Plumb 00:29:55 So, the… that… spec mostly targets the SDKs.
So, core SDK behaviors, exporters, I think there's provisions for things like samplers, and probably propagators, baggage.
Cesar Munoz 00:30:13 That's a great point, because it's like… so, for example, one of the, thing, the stuff we do in core is… Setting up a disk buffering exporter.
Jason Plumb 00:30:25 Right.
Cesar Munoz 00:30:26 And there's no way to… I guess there's no way to declare that in the JAMA.
Jason Plumb 00:30:31 Oh, no.
No, it won't… it wouldn't be in the schema yet, no.
Cesar Munoz 00:30:37 And so… and if we go… the same path as the SDKs are going.
and just follow strictly what's in the YAML file.
Then users won't have… these features.
it wouldn't make sense. Unless… to… Add stuff on top.
Of what's in the YAML file?
the later.
Jason Plumb 00:31:08 Yeah, there's… so there's a way to… and maybe we need to see if… if we can piggyback on an existing one, but let's see.
If, if there's an example anywhere in instrumentation.
Oh, there's gonna be YAML files in every directory, I forgot.
There's, yeah, like, this one may be, let's see.
So, this is just as an example. So there's all the way to configure… there's a way to configure all of the common, like, SDK stuff is up here.
So here's what's in the resource, here's some attributes, here's the exporter… And then, you get into distribution. So this is where the customizations can happen.
Distribution, Java agent, instrumentation, enabled false, enabled Tomcat, right? Like, that's the kind of stuff we would also have, but we just wouldn't be Java Agent, we'd be, like, Android Agent.
Cesar Munoz 00:32:10 Does that distribution… Block needs to be defined somewhere, or we can just go with whatever we want.
Jason Plumb 00:32:19 I don't know that there's a formal schema for stuff that's underneath this. I think the keys here under distribution might be limited.
But let's look at the spec.
Cause I don't know the answer.
Let's see… Data Model API… Where is the schema?
You don't see it in there. Is it a part of the API?
No… I've been really trying to avoid looking at declarative configuration, but I think we're gonna need it.
Cesar Munoz 00:33:27 Yeah, I'm guessing… I mean, I've just seen it, that it's… it seems to be spreading across all languages.
So…
Jason Plumb 00:33:34 Totally.
Cesar Munoz 00:33:35 But what I… what I see… at least that we just found out, is that it's going to be slightly different for distributions.
Which…
Jason Plumb 00:33:45 It is. Yeah.
So I can show you how we do it in ours.
Because we've been doing a little bit of work around this, too.
Let's see… Do we have an example?
Yes, so here's, like, here's an example one in our distro. That's not helpful.
Let's see… No… Maybe we don't have an example checked in.
I think all of our tests just have this YAML hard-coded.
Cesar Munoz 00:34:35 One more thing, do you… regarding… It's okay, I mean, just… I'm just curious.
Jason Plumb 00:34:41 Yeah, yeah.
Cesar Munoz 00:34:41 Do you know if upstreams… current efforts with the Clarity config involve making it dynamic, or is it just one… one-off reading when the app is starting in, and that's it?
Jason Plumb 00:34:59 There's… I think there's nearly no work in the two upstream repos, the core Java repo and the instrumentation repo. I think there's almost no work to make parts dynamic, with a couple of caveats, one of them coming from Jack and the work he's doing.
I don't know if you're dialed into that. Are you dialed into that?
Cesar Munoz 00:35:19 Yeah, yeah.
Jason Plumb 00:35:20 Okay, so he's been doing a bunch of work around, this.
Cesar Munoz 00:35:26 Dynamic, yeah.
Jason Plumb 00:35:29 Yeah, so he's got this… he's got this checklist here, and this thing called Telemetry Policy, which is an OTEP, that's really where the work in OpenTelemetry is happening, as far as I can tell.
it's also at arm's… like, arm's distance for me, like, I don't know the ins and outs of it, because of… I'm just busy with other stuff.
But I'm aware of it, and I think that's where the real work is happening.
Cesar Munoz 00:35:53 Yeah.
It's just that I know that Jack… Sorry?
Jason Plumb 00:35:58 Go ahead.
Cesar Munoz 00:36:00 I was just gonna say that. I know that Jack's initial idea was to… Create some sort of… custom configuration.
file for the dynamic conflicts to happen. But then is that… then the… the… the issue is that You know, it would be custom, so it won't have anything to do with the clarity.
At least that was the initial idea.
But… Like, if we want to… Yeah, that's the thing. I guess there's, right now, at least not that I'm aware of, a… a path to… like, connect… or to make the clarity config dynamic. I know that Jax's idea was to make some config dynamic, but not using the clarity config.
Jason Plumb 00:36:54 Oh.
Cesar Munoz 00:36:55 Probably… probably he'll have to.
use the clarity config, and… It's, yeah, it's a very early stage.
Because… It's tricky, it's like, how do you tell exactly what you have to change?
You know, say that you only changed, you know, an exporter, and then should you, like, repeal the whole thing?
Jason Plumb 00:37:18 I know.
Cesar Munoz 00:37:18 So…
Jason Plumb 00:37:19 It's really, it's really, really complicated. I think… I've been stewing on this a lot because people keep asking for it, making parts of the agent… Highly dynamic, or just allowing huge portions of the thing to change in the middle of its run.
Feels like a pretty big step backward to me.
It feels counter… at least on the… maybe especially on the server side.
it feels… Kind of counter to the way that the… development cycle and the deployment model has been evolving, right? Like, people are getting comfortable with these orchestration systems and all of the tooling that's layered on top of Kubernetes to push out changes and to do very sophisticated control and configuration of your deployments. And then to go through all of that, and then to have something kind of Sidestep all of that and be able to change the runtime seems really, really like a step back to me.
I think… I probably will give some concessions to… mobile… Because it's much harder, and you really don't control your deployments on mobile.
Where you have a user that has installed an app, you know, from a year ago, and they've never installed an update, and maybe you do want to be able to tweak the configuration that was deployed with your APK, right?
I haven't quite figured that out, but I think that maybe mobile and client stuff should allow for it to be a little bit more dynamic because it's not controlled.
Cesar Munoz 00:39:00 it's more helpful. It's just that it would be very difficult to… Make it work with such a broad… Kind of config as the one.
Provided in the… in the clarity config, because it really… it literally covers everything, so… ideally, or at least what we've been doing at Elastic, is that we have a config with Some very specific parameters, let's say sampling rate, and that's it.
And then, when we receive that, we change whatever Processor or sampler implementation that we set.
Upfront.
to… to follow that new sampling rate. But it's not like we're gonna rebuild the whole thing, so… Which makes me think that probably… probably dynamic… sorry, declarative config will be only a thing of… Just for initializing.
an agent, and then the dynamic part will use something else, maybe? It's just that I was curious, but I know that it's not… It's probably not, still defined.
Upstream, yeah.
Jason Plumb 00:40:23 Yep.
Cesar Munoz 00:40:24 Yeah.
So, I guess, back to mobile.
Maybe if we start implementing this, we don't… maybe we don't have to think about dynamic stuff.
At least not at the beginning.
Jason Plumb 00:40:42 No, I think it's a first step, yeah, for sure. Having declared, like, a file, a YAML file that can be used to bootstrap the Android agent would be a step forward.
Cesar Munoz 00:40:51 Yeah.
Jason Plumb 00:40:52 And even, you know, even though it's primarily configuring details of the SDK, once we get our layers on there, people are going to want to have Configuration tools that generate these things.
And they're gonna pass the little snippets around, and they're gonna, you know, they're gonna reuse a bunch of that configuration.
I think that's the goal. But also, OpenTelemetry has stated that dynamic… Sorry, declarative configuration is really the future.
And… The goal, at least on the server side.
is to wind down the amount of fancy environment variable support. So, like, as new features come out, they're gonna be treating the configuration in YAML, the declarative stuff, as the first the first place to put that, and then maybe it gets backfilled with environment variables, but new stuff… Won't necessarily have an environment variable defined.
Cesar Munoz 00:41:49 Yeah. Yeah, that makes sense.
I guess in the meantime, again, at least you just have something that initializes an OTL instance.
Because once we start working on this, I know that a lot of questions will follow, such as, so… What are we gonna do with… I mean, I'm guessing that a user who provides a YAML file then that means that they won't have to use the DSL at all, probably, because you'll just have to follow what's in the YAML file.
And so, in that sense, what if a user does… both things.
Like, which one wins?
Things like that, you know?
Should we create statics for storing the… instance generated by the YAML file.
It's gonna be…
Jason Plumb 00:42:48 I remember…
Cesar Munoz 00:42:49 a phone.
Jason Plumb 00:42:49 I remember there was a time in the JavaSig, maybe in the middle of last year, where we kind of did this thought experiment, which was like, if you wanted to change I'm trying to remember the exact details, like, if you wanted to change… in its current state, if you wanted to change, like, the… I think it was, like, late… let's say you wanted to add a header to the exporter.
Just as a… as a for instance.
I… so, I think it would require changing… the… OTLP exporter's URL, or no, it's configuration, it has, like, some set of headers, so you have to re-change… you have to change that.
And that exporter is tied to the batch span processor, so you'd have to re-change that. And the batch span processor is tied into, like, the tracer provider, so you'd have to replace that. So you end up having this, like, this, like, tree, this object tree, this entire thing that needs to get replaced, just to change one little thing, and… It gets, it gets really unruly pretty quickly.
And especially in the case of Android, I think it also harkens back to some stuff that we were talking about last year with Mustafa, and the reason why we have the uninstall Because they were trying to change configuration. Like, they had stuff that they wanted to set up differently every time a user logged in, or whatever their use case was, but it was certainly having to rebootstrap everything.
To account for this, and that's, you know… It's a problem.
Cesar Munoz 00:44:18 Yeah, it sounds very complicated.
Jason Plumb 00:44:20 Yup.
Cesar Munoz 00:44:21 But it's just one of the problems, because of what I mentioned then.
Then there's gonna be, like, multiple ways to… Initialize hotel.
And, yeah.
Jason Plumb 00:44:33 Let's kick the dynamic can down the road as long as I can… as long as we possibly can. Let's do the simple thing first.
Yeah. By simple, I mean not simple at all, just building declar… we're talking about declarative config.
Hanson 00:44:46 Yeah…
Jason Plumb 00:44:47 To be able to have a YAML file on the phone, ship to the APK or whatever, and then it helps configure the SDK and the agent.
Hanson 00:44:54 Yeah, it totally makes sense. The YAML probably should be parsed at build time to turn into a build object that we could then… or, like, a class file that we can load so we don't have to do a disk read, on startup.
Jason Plumb 00:45:06 That was what Cesar was proposing. I've heard no one… Before today, talk about that idea.
And I do think that it is actually quite counter to having declarative config in the first place, because it's not even really declarative anymore if you're evaluating the configuration at build time. Is it still configuration? Like… It's very much intended to be runtime configuration.
Hanson 00:45:30 So the problem with runtime configuration with short-lived clients is the dynamic.
Jason Plumb 00:45:35 Yeah, this is what we've been talking about.
Hanson 00:45:37 Yeah, so, I mean, my opinion is that the client shouldn't try to dynamically apply config. It should wait till the next process, which actually is very fast. Like, it happens in no time.
You're not gonna be able to do, like, live pushes of things, but on a client app, you can't really guarantee that anyway. So it's almost like what the things you have to do to achieve that level of, like, basically server-controlled.
client apps is really high, and, I mean, I don't have to explain… y'all know this, so it's whether we have consistency and build towards that, or have nothing and build towards that, and have nothing until we get there, and… I always believe in the incremental approach, which is, let's just have something that's predictable right now, and then… and then if we could improve it, improve it, so…
Jason Plumb 00:46:30 Yep.
Cesar Munoz 00:46:31 Yeah, it makes sense. I mean, the… another thing that we mentioned was that, like, if we do… if we… there's really two ways to do this, which is generating classes at build time based on the YAML file, and then the other one is reading the JAML file at runtime.
The former, it's gonna be faster.
But it's gonna be fixed. So, if in the future, you know, you want to support that use case, even… even if it's not, like, dynamic config in the sense that It will change at runtime, but it's like, you want to wait for the next launch of the app to… to read the new file, then in that case, you will need the, like… like, the… whatever you generated at comfy… at compile time wouldn't… wouldn't be used. Anyway, so… But again, it's probably just trying to get ahead of ourselves.
If we go with the, We still haven't decided, but if we go with the, generate… Objects at build time.
path.
That would require adding a Gradle plugin.
to these projects.
Which, I know in the past, I think Jason has had, some ideas on it.
I don't know how, you know, where you stand on it.
Nowadays.
Jason Plumb 00:47:59 Oh, I think it's… I think it's really powerful, yeah, I think it's super cool. It seems to feel like the Android way, you know? There's plugins literally for everything, so… and we have a little… we have a little bit of that already with the OKHTP build time configuration, or build time instrumentation. We had talked about doing… Even some of the OpenTelemetry Rum Builder type stuff at… at build time?
now that we have the agent, maybe we do kind of the agent stuff, but whatever, it's like getting into the application's early setup and injecting our entry point based on some other DSL or some other configuration, so… that… it feels like a natural flow to me these days.
Hanson 00:48:44 Yeah, and also having that doesn't necessarily preclude us from updating things dynamically, so what this builds effectively is the default.
Right. And it'll be loaded at startup time, the defaults. And if we have runtime updates in the future, if the instrumentation on that stuff is able to do that, then we can apply the updates to some, you know, hot data model, which derives some of the default, but can then be modified and picked up. So these should be decoupled.
I think the important part about having the generation is that you're not going to take the penalty of having to deserialize or read from a file on startup, which, depending on your device, could be super painful and basically add to the long tail, so…
Cesar Munoz 00:49:30 Yep.
It's gonna be, fun.
Project.
We also mentioned, Hanson, if you… I'm just throwing questions, open questions.
In case anybody has an opinion. Probably we should create an issue for this.
Things like, you know, what's gonna happen if we implement this feature?
And then some user decides to initialize the SDK using the DSL.
and they also have a YAML file. Then in that case, what's gonna happen? Or if they only have the YAML file.
Then that would mean that we would automatically rate it.
and generate a ROM instance with it, then how users will be able to interact with it. So does that mean we're going to have to put statics Available for them, or something like that.
Things like that.
Jason Plumb 00:50:29 So I think that same question exists in the core Java repo as well, right? If someone uses declarative config.
can they also use the programmatic, SPIs to… and the service loader stuff to, like, override parts of the SDK configuration? I think… I think the answer is no, but I'm not sure… I certainly know that when you use declarative config, you cannot use environment variables separately from the environment. Like, if you use declarative config, environment variables are ignored unless they're literally inline in the strings in the YAML. All of the other external environment is ignored.
You cannot override parts of declarative config with environment. You just… that's not a thing.
You have to pick which… you have to pick which mode you're configuring your SDK with, and that's great.
But I'm not sure how that applies to programmatic. So… but that's why I said I assume that if you're choosing declarative config, you're choosing declarative config, and the programmatic stuff is also not used, but maybe it's still there as an override, I'm not sure. I don't know the answer.
Hanson 00:51:32 So the multiple YAML files can probably resolve itself just by precedence, like, you know, in various ways. And if that's what's taken at startup, programmatic could be seen as an alteration of dynamically, you know, changing stuff upon startup.
So, I think environment variables and declarative config probably do clash more. It's, like, hard to say, hey, what blows up which. But I feel programmatic is probably, programmatic feels as, aligned with environment variable declaration and… and… and the declarative config. So I don't think they're in contrast, but, you know, obviously the people who thought about this more probably has an opinion about this, and, Yeah.
Jason Plumb 00:52:18 Oh, there… yeah, so there is… huh, okay. So, David mentioned something, and I want to address that, so… Declarative config, so… inside of the YAML strings, like, inside of your file, you can reference, using, like, string interpolation, you can reference things from the environment, and they will be filled in.
But you can't have a YAML file with values, and then also expect separate, non-referenced environment variables that are… that are used for config today. You shouldn't expect those to apply.
They'll be ignored.
Hanson 00:52:56 So basically, YAML acts as, like, a different root default to the environment variables, and the YAML can get environment variables, but it's up to the YAML, whatever is in the YAML is truth. Yeah, that makes sense as, like, the startup default, but I think programmatic is… I'll go ahead.
Jason Plumb 00:53:16 I think… I think we're… I think what I'm showing right now is, like, part of the mechanism Through which you can customize parts of your distribution, or your SDK, or whatever, so you'll notice the package here is within declarative config, there is a package called auto-configure.
So, auto-configure is the… Auto-configure is the way to have… in Java, at least, the system properties, environment variables, and the SPIs for auto-configure.
Hanson 00:53:47 Oh.
Jason Plumb 00:53:48 evaluated. It's, like, all three. And… You'll notice that this is also… there is also auto-configure within declarative config, and one of the things you can do is you can implement this SPI, which is Declarative Configuration Customizer Provider.
And so, you implement one of these, and you will be invoked with a declarative configuration customizer, which I have no idea what that looks like, because I've been trying to avoid looking at all this stuff, but… You can customize the model, You can customize the span exporter and the metric and the log exporter.
Hanson 00:54:25 Extends ordered at that, that doesn't say…
Jason Plumb 00:54:27 Now, here's where it really gets interesting, right? Because this is gonna… this is gonna be almost exactly what's in the spec.
Alright, so you get a model in, you poop a model back out, and what that looks like… Somewhere.
I guess I can't find it, it's not smart enough to find it.
Come on.
Where is it?
Whoa.
Hanson 00:54:59 So, am I interpreting this correctly? In that… In that there… even if it's a claritive config, is wired up through these, These objects. So you can have multiple declarative configs being wired up, and if the order is applied differently, different… different results will happen.
Jason Plumb 00:55:24 Now, I don't think the expectation is that you can have multiples, I think that's one file.
Hanson 00:55:27 Okay, okay, okay, okay.
Jason Plumb 00:55:29 I don't know if you can do includes or anything like that, but I think the intention is, like, one file.
Cesar Munoz 00:55:37 Yeah, that's what I heard as well.
And so, from what we're seeing, the way to configure, like, to customize it is using SPIs, which… It makes sense, because you wouldn't be doing anything programmatically to initialize the instance.
Jason Plumb 00:55:57 It looks like this one might be the only one that exists, is the… this customizer.
At least in this package, which is, I think, the package where it would live, so…
Hanson 00:56:09 And is it… is it done per SDK instance, or is it done per instrumentation? Yeah. Okay.
Jason Plumb 00:56:15 No, per SDK, and we're only in the core repo, there's no instrumentation in here. This is all just, like, core SDK setup stuff.
Hanson 00:56:22 Okay.
But I believe…
Jason Plumb 00:56:25 I believe that this is the hook.
That allows you to do your custom stuff. So let me just see what ours looks like, because I haven't… It's not fresh in my brain.
Right, so we… do we have one of these? Yeah, we have the… declarative configuration interceptor. This is in our distro, and we do things like… I don't know, what are we even doing here? Nothing.
Hanson 00:56:53 Well, you pass in a function, and the function can modify in return.
By default, nothing.
Jason Plumb 00:56:59 Yeah, like, we have this… we have this snapshot profiler, so when we customize the model.
Yeah, so we have this as, like, custom Splunk-specific configuration stuff.
And so we can inject that into the model, is basically what's happening.
Hanson 00:57:16 It's doing stuff like adding span processors and stuff.
Jason Plumb 00:57:19 Exactly.
Cesar Munoz 00:57:20 So maybe in Otelandry, this is the way we could do stuff like adding, this buffering, exporter, and things like that, right? I guess.
Jason Plumb 00:57:30 Yeah, totally.
Cesar Munoz 00:57:30 something you will define in the YAML file.
Jason Plumb 00:57:34 Yup.
Hanson 00:57:35 Are we still on declarative config now? Because it seems like it's… It's not config as much as… Runtime customization.
Or…
Jason Plumb 00:57:47 I mean, this is after the… this is, like, after or while the YAML is being… it's after it's been parsed, but, like, while it's setting up the SDK. So you turn the YAML into a data model, right? You parse the YAML into a bunch of classes in a tree.
Hanson 00:58:00 gap.
Jason Plumb 00:58:00 structure, and then you allow these customization points, and then you build your SDK.
Hanson 00:58:09 Right. So, if we were to do this at… convert the YAML at build time, it would just replace the reading of the YAML at runtime.
We still have the order and precedence and all that fun stuff to deal with.
Jason Plumb 00:58:24 if declarative configuration is used, we don't have to worry about precedence for things like environment variables, or… or I guess there's no system properties, but… You know?
Hanson 00:58:34 Right.
Jason Plumb 00:58:38 With that in mind, I will share… go ahead.
Cesar Munoz 00:58:40 wouldn't be… it wouldn't be compatible also with the DSL, And probably the builder, ROM Builder, so it would be an.
Jason Plumb 00:58:48 Yeah.
Cesar Munoz 00:58:49 Separate thing.
Jason Plumb 00:58:50 Yeah, I think we'd probably need to not… have the DSL involved if we're using declarative config. That's my… that's my instinct, is that if you've chosen to use declarative config, you probably cannot also use the agent DSL.
Like, everything that you would have been representing in the agent DSL probably needs to be in YAML, and we will have to write that parsing or that binding.
Hanson 00:59:16 So, the…
Jason Plumb 00:59:18 We'll have a translation layer that knows how the YAML should be structured to accomplish the same things using the DSL, or the classes that underlie the DSL.
Hanson 00:59:27 maybe this is naive. I feel like because of, at least with the Android build process, the DSL could be applied on top of what is generated via the YAML, or even, like, reading the live YAML.
maybe I'm… being a bit naive, because right now, that's applied on top of any configure… environment config… variable configuration being read as well. So it… this is not so much replacing, this is… this is already kind of augmenting something that already exists, which is, like, you know, the default. This just provides a new default. But maybe, like, when we do this, we'll have to dig into it, but, Yeah, yeah, maybe I just don't know the nuances then.
Jason Plumb 01:00:16 Well, we are almost out of time. I think it's not important for us to talk about this last one, because, Cesar, I appreciate that you've… it looks like you've commented on this already, so that's good. I submitted a PR, like, kind of later last night, and it looks like you've already looked at it, so… we'll just… we'll take that off. We'll do that async.
Talking about declarative config, though, because we are basically at time, I did want to share this sticker that I picked up at the last KubeCon. We'll see if you can read that. It's gonna try and blur, but…
Hanson 01:00:43 Nope. Is that a honeycomb sticker?
Jason Plumb 01:00:46 Yeah.
Hanson 01:00:47 What is… I… I… this is too small for me, I can't…
Jason Plumb 01:00:49 Okay, here we go.
Hanson 01:00:50 Open to what you mean?
Jason Plumb 01:00:54 Dang it. There we go.
Hanson 01:00:55 the legs.
Task built, kernel task simple, okay.
Jason Plumb 01:01:04 Alright. Yeah, OpenTelemetry making the Linux kernel build look simple.
I just feel like that was relevant after looking at that declarative.
Hanson 01:01:13 This is fun.
Jason Plumb 01:01:14 It's very complicated, in my, in my opinion.
Hanson 01:01:16 Well, the speck and everything has to boil the ocean, so… this is the hard part. When you use it, you don't actually… Yeah, anyway.
Jason Plumb 01:01:24 No, that's… that should be the point, yeah.
Cesar Munoz 01:01:29 Well…
Jason Plumb 01:01:29 Great, everyone. Well, thank you for… thank you for being here, and I appreciate your input and your help on this project.
Cesar Munoz 01:01:35 Cheers. Talk to you next week.
Jason Plumb 01:01:38 Going.
