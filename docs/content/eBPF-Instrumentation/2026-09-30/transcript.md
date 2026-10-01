SIG: eBPF Instrumentation
Date: 2026-09-30
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Giuseppe Ognibene (Coralogix)** 00:34 Hey, how about it?
**Tyler Yahn (Splunk)** 00:36 How you doing?
**Giuseppe Ognibene (Coralogix)** 00:38 Good, how are you?
Doing well.
**Tyler Yahn (Splunk)** 00:41 Yeah.
Doing well.
Just, moving along, excited about this upcoming release, so… We'll see. See how it goes.
**Giuseppe Ognibene (Coralogix)** 00:53 Yeah.
**Mario Macias** 00:56 Hello.
**Tyler Yahn (Splunk)** 00:58 Hey.
**Giuseppe Ognibene (Coralogix)** 00:59 Mario.
**Tyler Yahn (Splunk)** 01:03 dannyda: Mario, were you doing a hackathon as well? Nicola was telling me he was working on a hackathon.
You're muted, by the way.
**Mario Macias** 01:15 No, this week I'm focusing on some missing tasks in OV.
**Tyler Yahn (Splunk)** 01:23 Oh, okay, yeah.
**Mario Macias** 01:24 Yeah, concretely improving the metadata support, when, when running in some Kubernetes services… in Kubernetes, sorry, in Amazon Cloud Services.
**Tyler Yahn (Splunk)** 01:36 Oh, I gotcha. Yeah, yeah, cool.
No.
Well, cool, looks like we're actually getting quorum, I don't think… Any Canadians are going to make it today, so I think we could probably get started here in just a second. If you haven't yet, go ahead and add your name to the attendees list.
And if you have agenda items you wanted to talk about, go ahead and add them there as well, and yeah, we can jump in here.
Cool. Alright, so Nicola did want to start us off. I know he's not going to be here with his Dynamic Instrumentation Probes. This is something we had talked about last time, as something that's a 1.1, feature. It looks like he's created an issue for this.
I know he was playing around with this as well, so he's got a, yeah, POC.
Last I heard, it supports Node and Java as well, so… super exciting about this.
Yeah, so I think that there's, like, a lot of really great, work going on here. I'm super excited about this. But yeah, if you have thoughts on it, please go ahead and add it as well, or add your thoughts here.
But yeah, let's jump into this after the 1.0. I'm really excited about it.
Speaking of the 1.0, so, next up is the V014 release. There is, I think I created one issue… It's, nope, it's not in there, but okay.
I think all of the issues actually are done. The releases, or the, the milestone is technically done, but there's kind of a question around, like, what we want to actually include in the, the 1.0.
And I guess it kind of, like, goes to say, like, what do we want to stage here as well?
So, one of the things was, brought up in our limitations, documentation, is if we want to decide for this.
Enforcement of SysCap, or system, Yeah, syscaps, default, currently it's false.
Which means that it's just gonna log an error, and continue… Borkin? It was talked about, maybe we want to switch this to true, being the default.
And, yeah, I guess that's just kind of an open question, if we want to do that, but then the other thing is, is, like.
when, do we want to do that, is kind of the main question. Like, is this something we wanted to try to change prior to the 1.0? Just to, you know.
timeline-wise, we were trying to get the 1.0 out today, so, like, this is gonna delay that… I'm sorry, not the 1.0, the, the V014 out, today, which means that we're gonna have to delay our schedule, if we start including these things. There's a few other things as well we want to talk about, but just kind of a heads up on that. But yeah, I'd love to hear people's thoughts on this.
**Mario Macias** 04:41 Oh, I find it reasonable, otherwise.
Having something that… keeps working, but it's not really working. Sometimes… will provide telemetry that is not expected, users will need to look at the logs, so… Yeah, I think the easier way is just let failing by default, and then the users will realize that something is is not failing.
So I will be in favor.
**Matt** 05:15 Nicola made a good point that, right now, I think some.
Some stuff which, which should not be working is working on their… or the other way around.
is working, so I, I don't think we, we can, like, Make it default right now, altogether.
So we should go a little bit more cautiously and see what breaks and where So, I don't know, maybe we can, we can do this before the V1.0.
But for V014, I think we can, we can just… I'll keep it.
In general, we should, I think we should audit all the config options and see what we can drop from there.
Well, we can simplify it.
**Tyler Yahn (Splunk)** 06:13 Yeah, so… Let's talk a little bit about timing here, because, the V014 goal is, is.
Today or tomorrow, get it out, and the… The idea was to get the RC out the next day.
within the RC, like, we're not trying to change the fundamental, like, nature of the project, meaning that, like, if you want to get configuration changes done, like.
We need to have done it in the past 6 months.
At this point.
**Matt** 06:46 Yeah, yeah, I'm saying that we can just… I think that we can proceed as it is right now, and eventually… change it for V100, not GERC.
**Tyler Yahn (Splunk)** 07:00 Yeah, I don't… like, that's… that's actually, like, not what we want to do, right? Because the… the 1.0 RC is meant for a release candidate, meaning that folks are going to be trying it out.
And they're going to be.
**Matt** 07:14 Oh, okay, we can.
**Tyler Yahn (Splunk)** 07:14 Okay.
**Matt** 07:15 see.
**Tyler Yahn (Splunk)** 07:16 So making a dramatic change in a release candidate is definitely not what we want to be doing.
**Matt** 07:23 So, so we should commit by everything that we have by today.
**Tyler Yahn (Splunk)** 07:28 I mean, I think we need a plan today, absolutely. I can understand if we want to delay the V014 and try to get a few more things in.
We did have, like, a buffer of, like, a week or two. This will be the buffer, meaning that, like, our… if there is a second RC, we're not gonna make our timeline for the KubeCon, release.
But… yeah, like, I… we need a plan today. Like, if we're going to do it, we need to make a plan, hopefully in the next day or two, we can get that implemented.
If it's a deep cutting plan, like .
That's just not gonna happen, right? Like, if it's gonna take weeks to do this, like, we're definitely not gonna be able to make that happen.
**Matt** 08:10 Yeah.
**Tyler Yahn (Splunk)** 08:12 So, yeah, like.
**Matt** 08:13 Well, I don't think it's that urgent that we need to do this.
Right now, I think it can wait. I mean, we've been like this for a year, so…
**Tyler Yahn (Splunk)** 08:24 You meaning the default here?
**Matt** 08:27 Yeah.
**Tyler Yahn (Splunk)** 08:28 Yeah, I, I, like… .
I agree. Like, I agree. Like, I definitely, like, think that.
This is something that could wait. There's also, like.
you know, just to kind of, like, frame the conversation, also, like, there's nothing saying that, like, we're not going to get a 2.0 out next year. Like, stopping the major evolution of this thing is not, like… I don't think it's as critical as, say, something like the OpenTelemetry API, where adoption of a major version is, like, very hard to get off of.
Rolling upgrades, or something like that, like, you know, as long as we're very clear about that.
I do think we want to be very careful about changing behavior In the middle of a major version, though, just to kind of, like, throw that out there, because it could be… it could be… You know.
I don't know, on one hand, you're like, okay, it was working before, it was just logging a bunch, and then all of a sudden it starts crashing when you do an upgrade in the middle of the major version. I guess there's an argument to be said that it wasn't actually working beforehand as well, but… I mean, I don't know, like, it's, it's one of those horrible things where people start relying on, features like this. So, yeah, we want to, I think, be a little bit cautious about that.
So… Yeah, like, if we want to change this, it does sound like, based on what Nicola's saying, like, there are some.
edge cases that are happening right now, maybe we need to take a look at this? Like, I'm happy to take a deeper look, but I definitely want to get more of a… a consensus, I guess, today is kind of the goal.
If that makes sense.
So, yeah, I guess… I guess I am a little hesitant just based on, like, what you just said, Mattia, or reiterated from Nicholas, saying that, like, you know, maybe there are edge cases where this is actually, like, saving us in a few places.
I was trying to look at Nicola's comment really quick, but, Yeah, he says he left a comment on the CheckOS capabilities issue.
But I… Is that a different issue? Oh, no, sorry, I didn't scroll down.
Sorry.
Hmm.
Yeah, so…
**Matt** 11:20 Yeah, so depending on, on the system, oh.
On the mounts, basically, there are some capabilities that might be needed or not.
Yeah, and that's why we can't, like, we can't be sure of what to enforce.
**Mario Macias** 11:40 I think one option will be build the… a list of required capabilities from the configuration. I think it shouldn't be difficult to do just something that scans some configuration options and say, okay, for this kind of activations.
the following capabilities are required. And then you can check only the capabilities you need.
**Matt** 12:08 But I think config is not enough, because on some systems, you have the mount that comes from the daemon set spec.
And if you don't have a certain mount, you need another capability. On certain kernel versions, you will attach the UPROPS via TraceFS.
And you need certain capabilities and not some others, so it's a little bit… For safety, I would leave it as is right now. We don't have to rush it, I think.
**Tyler Yahn (Splunk)** 12:46 Okay.
So, because if we change this to true.
That means we may end up in situations where we're failing, where we don't need to fail? Is that… is that the takeaway from this? Yeah.
Yeah, okay, okay, I think, I think that's a good point. I think I definitely need some more… More testing.
Okay, that's… then let's… yeah, let's leave this out of the milestone.
I'm gonna put this… I'm just gonna leave this out. I don't know how we're gonna get it in at a later time, but… I was looking for a decision, let's go with that decision. Cool. Okay, cool.
So next up, also Mattia asked the question of, what's the plan for deprecating the config options? Should those be dropped for the 1.0?
So, That's a good question. I kind of was thinking the same thing about the ConfigV1 entirely, but, like.
Do you specifically have, like, specific config options? Like, are these, like, the override, the environment variable overrides you're talking about?
Sorry.
Losing context, maybe I can pull up the Slack channel.
**Matt** 13:59 No, no, in general, I… I was wondering if we did an audit of all the config options and the Decided that, okay, this makes sense to stay as a config option, this is deprecated, we should remove it.
Like, for example, in Discovery.
There is, services, and there is.
The other one with the globe and the one with the.
**Mario Macias** 14:27 Richard?
**Matt** 14:28 you I think one of those should be dropped, I think it was with the one with the regex.
So, I don't know if we should commit to drop it before, before the ERC, or if we can keep it there as deprecated, because… Most users, anyway, are using this, As a feature, and… Don't care about the deprecate options.
**Mario Macias** 14:59 Yeah, yeah, I think that as long as the deprecated options are kept undocumented.
Inovi.
I think if someone uses them, it's at their own risk.
Most of those deprecated options come from… Bayla, legacy… legacy Bayla stuff. So, yeah, probably there's no real reason To… to keep them.
We can…
**Matt** 15:32 the.
**Mario Macias** 15:33 them yeah.
**Matt** 15:35 Should we remove them before the 0140 as well?
As I understood.
**Tyler Yahn (Splunk)** 15:43 So, You're talking… are you talking about… you're talking about Config V2, or V1?
**Matt** 15:49 V1.
**Tyler Yahn (Splunk)** 15:51 Yeah.
Yeah, so I'm… Why don't we just drop V1 support for the 1.0?
**Matt** 16:02 Because I think, So, did we, like, officially deprecate Configui 1?
**Tyler Yahn (Splunk)** 16:13 No.
**Matt** 16:14 I don't think so. But yeah.
**Tyler Yahn (Splunk)** 16:16 Can… So this seems a little rushed to me, but, like, I'm just gonna run it past you, so this may just be a bad idea, just preference it. But, like, what if we, in this next release, deprecate it, and then in the RC, or the V1, like, essentially we say, like, we're going to deprecate it in the V014.
And then saying that it will be dropped in the next release, and then in the 1.0, it just will… support for that will be dropped.
**Matt** 16:43 We have to… Is that tested, like, thoroughly? Thoroughly? Because I think we have to run all the integration tests, both with V1 and V2.
**Tyler Yahn (Splunk)** 16:56 It's not, you're right.
That is true. All of our integration tests, we put that off until after the…
**Matt** 17:04 The first time that I used the config v2 was there for the LoginRicher blog post, and there was something that was not working, so I needed to fix it.
I'm not sure that every feature is completely covered, or is working as expected. I think we should take our time there.
**Tyler Yahn (Splunk)** 17:27 I don't know if that's ever gonna happen, though, is the problem. Is, like, the only way you're ever gonna get people to actually test it is to, like, make them use it.
Like, there's no reason… They would start using the V2 if they're not going to already use the V2.
Like.
**Matt** 17:42 But we can start testing in CI. For example, the login research test right now runs both with V1 and V2, to make sure… To make sure every, every, everything is, is covered.
**Tyler Yahn (Splunk)** 17:57 Yeah, and like, that was a big part of the testing idea, was to just move everything over to the V2.
And I get that.
the thing is, is though, that, like.
Until, until you're telling people that, like they need to start using the V2, or they are using the V2, you're not going to get any of the bugs. And I see it as, like, just one of those things that we just need to move forward on. Like, when you start finding bugs, we need to fix the config, right?
**Matt** 18:26 Yeah.
**Tyler Yahn (Splunk)** 18:28 LB Helm chart uses V2.
**Mario Macias** 18:33 Maybe we can… market, the V2… I don't know, do some kind of… announcement that V1 is going to be deprecated, maybe in V2, or something like that, or mark V2 as experimental, and… I don't know, and something that motivates people to start moving from V1 to V2, even ourselves, as a… As other developers.
**Tyler Yahn (Splunk)** 19:04 I mean, that is another option, right? Like, we could just have it so that we deprecate it while… after the V1.0, right?
And then in V2, we drop it completely.
That would give us, you know, a runway of… Months or a year to do this validation stuff, and it would give us time.
**Mario Macias** 19:26 Yeah.
**Tyler Yahn (Splunk)** 19:27 Get all of our stuff switched over.
**Mario Macias** 19:31 Yeah.
We should probably start keeping in mind every new integration test we add.
Well.
**Tyler Yahn (Splunk)** 19:39 instead of, like.
**Mario Macias** 19:40 Copying.
**Tyler Yahn (Splunk)** 19:42 Yeah. Yeah, the goal was to just get, like, we… yeah, I've got a big tracking issue. I just, like, there was no way I was gonna get it done before this release got out, to do the whole.
**Mario Macias** 19:50 migration.
**Tyler Yahn (Splunk)** 19:50 But yeah, like, the goal is to not have any config V1 anymore. It's just to support the V2 going forward and just standardize on that, yeah.
**Mario Macias** 19:59 Yeah.
I guess shouldn't be difficult to create.
a converter tool, right? That creates a base… It already exists.
Already exist, okay, okay.
**Tyler Yahn (Splunk)** 20:13 That was part of the migration.
**Mario Macias** 20:14 version.
**Tyler Yahn (Splunk)** 20:14 Stuff, yeah.
Yeah, that… so that already exists, and then, Yeah. So maybe, maybe that's just the plan, as we go forward with the V1 still there.
I would… I would try to say, though, that, like.
Yeah, I think… I think we need to halt work on it, though, is the thing.
So, taking options that are deprecated, trying to manipulate the config V1, like, I think we need to just stop, and we need to start, like, focusing all of our development efforts on V2.
And.
if there are bugs in V1, like, I think that's just what it is. Like, I think we need to move on to the V2.
**Mario Macias** 20:54 try to, like…
**Tyler Yahn (Splunk)** 20:55 put effort there, so that it consolidates that. So, like.
**Mario Macias** 20:59 I, yeah.
**Tyler Yahn (Splunk)** 21:00 these deprecated fields are, like, the restructuring of the V1, I think we need to just leave it as it is.
**Mario Macias** 21:06 Yeah.
**Matt** 21:07 Okay.
**Mario Macias** 21:09 Some crazy idea. At some point, maybe we could even… all the code we have that handles V1, remove it and replace it by this V1 to V2 converter embedded into OV. So people… we have some time that for people providing V1, they will still get it supported. Internally, it's transformed to V2. And for us.
Any new feature we add?
we will be forced to add it in V2, or to add the configuration in V2.
**Tyler Yahn (Splunk)** 21:42 Yeah, we're kind of already doing that. Like, it's actually, because we actually… There's a separate config, it's called the internal Go structure data representation, right? Like, that's the actual.
**Mario Macias** 21:53 configure.
**Tyler Yahn (Splunk)** 21:54 Right, and so, yeah, we're kind of.
**Mario Macias** 21:55 Yeah.
**Tyler Yahn (Splunk)** 21:55 This in our, like… ingestion pipeline, like, we take V1 and we take V2, and, like, we convert them into that standardized format, but yeah, like…
**Mario Macias** 22:03 Okay.
**Tyler Yahn (Splunk)** 22:05 There is like a, that's actually the true config is like that data struct.
Which is where, like, Mattia's bug that he found with the log and richer stuff, that's where that came in, because it's more about, like, those conversions into the internal data struct is, like, kind of the key thing here. But yeah, we… I mean, we definitely should keep doing that. Like, we could, to your point, like, maybe even stop supporting the V1 and just, like, go… instead of… V1 to the internal data struct, go V1 to V2 to internal data struct, or something like that.
**Mario Macias** 22:35 Yes.
**Tyler Yahn (Splunk)** 22:36 But I don't see us adding any more features to the V1, so, like, I'm not sure why we would need to do that either, I guess.
Okay.
**Mario Macias** 22:45 Okay.
**Tyler Yahn (Splunk)** 22:49 But maybe…
**Matt** 22:50 We could do one crazy thing. We can go to V1 to internal, and we can also do V1 to V2 to internal, make a diff, and print it.
Please report this.
**Mario Macias** 23:01 Zoom.
**Tyler Yahn (Splunk)** 23:03 Yeah, and then they say.
**Mario Macias** 23:04 I don't think it's crazy, yeah.
**Tyler Yahn (Splunk)** 23:06 Ha ha ha.
**Mario Macias** 23:07 It's very good, it's a very good idea, yes.
**Tyler Yahn (Splunk)** 23:10 Yeah, yeah, actually, I think you're right.
Yeah, I mean, we definitely have integration tests on that compatibility, but I think that's, like, even more, like… because, like, we were just saying, like, that's the important representation is the internal one, so I don't know if we're validating that.
**Mario Macias** 23:25 can.
**Tyler Yahn (Splunk)** 23:25 Like, fully. Like, that's more of an integration style.
Yeah, I agree, I think that's a good idea.
I think maybe the takeaway from this, though, is that, like, maybe we also want to make it clear that, like.
in either this release, or maybe the 1.0 release, the V1 config is sealed, or whatever we want to call, like, sealed, in the sense that, like, it's not… we don't plan to iterate on it anymore, it's no longer… You know, growing. I don't know if we want to, like, deprecate it at that point, I think it's just, we need to say that, like, it's frozen? Maybe frozen is the better word? I don't know.
**Mario Macias** 23:59 Yeah. Yeah.
**Matt** 24:00 Yeah, I think it makes sense, yeah.
**Tyler Yahn (Splunk)** 24:02 Okay.
What about… which release candidate do you think is better to do that in? The 1.0 or the, the V014?
**Matt** 24:15 Good question.
**Mario Macias** 24:19 If there's nothing else to do, we can do it for 14. If we need to do some extra stuff that could delay 014 that 1.0 where C is okay.
**Tyler Yahn (Splunk)** 24:36 I mean, I don't think there is like I think we've gone through.
**Mario Macias** 24:38 Okay.
**Tyler Yahn (Splunk)** 24:39 Pretty substantially, so maybe we just do it in the V-Zero 14, yeah.
**Mario Macias** 24:42 Okay, okay.
**Tyler Yahn (Splunk)** 24:44 Yeah, okay.
Maybe, yeah, maybe it's just… more, like, saying in the release notes is one thing, maybe putting it in docs somewhere as well is also a better idea.
Yeah, maybe there is a PR still, but okay, we can do that.
Okay, and Mattia, you also had another issue. Let me start sharing my screen again.
**Matt** 25:15 Oh yeah, this is a bug with the UPROPS.
There was a comment from Nicola that says that this should be in the V014.
So, I have a PR for this one. I'm running some tests right now in the background. It looks like it's good, so… Maybe I can, I can open a PR today as well.
**Tyler Yahn (Splunk)** 25:42 Okay.
Yeah, alright, cool. Then let's… yeah, if this is a… yeah.
That sounds good.
Let's add that, that's definitely added, alright.
Yeah, alright, so then I guess that also means, everyone, please be on the lookout and, take a look for this.
PR from, Mattia. And then, yeah, we can… I agree, let's try to fix this.
The only other thing… that I'm thinking is maybe that PR we just talked about, like, by updating docs, but otherwise, yeah, let's try to… I'll draft a PR for the V014.
Release… hopefully we can get it out… tomorrow, but if not, like, Friday or early next week, seems totally reasonable, and then let's… yeah, I'll try to get the RC out, like, the day after, whenever we get this out. And then, Yeah, I think that that's it.
I just got really excited, if that's it. Maybe… maybe it's a little premature. Any other things… That come to mind for folks on this?
Okay.
Awesome. Alright, well then we can move on. Giuseppe, you want to talk about pinning the Clang format and the Clang tidy, for local, and CI?
**Giuseppe Ognibene (Coralogix)** 27:01 Yeah, I just noticed that we were using… we are using Slang Tidy 19.
And actually, we are building in Silang 22.
Hello!
So…
**Tyler Yahn (Splunk)** 27:16 I think there was like some.
**Giuseppe Ognibene (Coralogix)** 27:17 Both.
**Tyler Yahn (Splunk)** 27:19 With 22, right? Like, I think there was, like… yeah, like, I thought… Rafael would know more, but, like, 22 actually contained, like, certain fixes that we didn't want to do, because they introduced things into, like, the eBPF code that were, like, not optimal for… Some of these backwards compatible kernels, but…
**Giuseppe Ognibene (Coralogix)** 27:36 I'm like…
**Tyler Yahn (Splunk)** 27:37 Little fuzzy on that, so don't take it, like, with, like, authority on that, but, like, yeah, if… because I… I'm running 22 locally, and I would, like, I'd be, like, doing things, and it would just, like, crash once I actually submitted it, so, like, it was a problem for me. And so, like, yeah, like, if you're… if you're running into issues where, like, it's not pinned for you, like, we definitely should pin it, like, agreed 100%.
**Giuseppe Ognibene (Coralogix)** 28:01 Yeah, I think that I run it, and there are only 3 files that change between Silang TID19. My only question is that I have two possible solutions. One is to… to add the Silang tide inside the OB generator, where there is the Silang.
But another one is to using Python directly and but this will add Python.
As a prerequisite.
And also, for the first idea, I don't think that I can, publish the image. So I don't know which is the best practice, or if you guys have any… Any opinion?
**Tyler Yahn (Splunk)** 28:40 The generator image?
**Giuseppe Ognibene (Coralogix)** 28:42 Yeah, I mean, we have the original radar image that is inside Celang. We can add the Celang tidy and Celang format inside.
Or…
**Tyler Yahn (Splunk)** 28:55 Yeah, like.
**Giuseppe Ognibene (Coralogix)** 28:56 Okay.
**Mario Macias** 28:57 Yeah, I like.
**Tyler Yahn (Splunk)** 28:57 We can… we can do that, yeah.
**Giuseppe Ognibene (Coralogix)** 28:59 Okay.
**Mario Macias** 29:00 Yeah.
**Tyler Yahn (Splunk)** 29:01 Generator image, if I'm not mistaken, is just, it's just a action that we run. In fact, I think it's run every night as well, if there's changes.
**Giuseppe Ognibene (Coralogix)** 29:08 Okay.
**Tyler Yahn (Splunk)** 29:09 Don't quote me.
**Giuseppe Ognibene (Coralogix)** 29:10 I, I thought that I, I.
Okay, I didn't know that.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 29:15 It only publishes from Maine.
**Tyler Yahn (Splunk)** 29:18 Oh, okay, is that what it is? Okay.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 29:19 Yeah, so if you've got a full PR, and you've got some changes to the generator image, and you want to try and publish it off your branch. It won't work.
It's not until you merge into main, or you use a source branch directly off the Oh, the origin repo.
**Giuseppe Ognibene (Coralogix)** 29:38 Okay.
**Tyler Yahn (Splunk)** 29:38 Giuseppe's just gonna need to make a PR, get it merged, and then it should work, right?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 29:42 Yeah, then you can… I don't know if this, like you said, if there's a nightly or something, but you can… there's the action that you can run at any time. Yeah, yeah. Which you can select a branch, main being one of them, or any other source branch, and then you can publish it from there.
**Tyler Yahn (Splunk)** 29:56 Well, if I can just select a branch, I mean, I could also just… yeah, okay, alright.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 29:59 As long as it's an origin branch, you can't select a branch off a fork.
**Tyler Yahn (Splunk)** 30:01 Oh, I see what you're saying, off of a fork. Sorry, yeah, I missed that part. Yeah, I gotcha. I see. I see. Okay.
**Giuseppe Ognibene (Coralogix)** 30:07 So I just need to do the PR when it's merged, the image is just published.
**Tyler Yahn (Splunk)** 30:12 I'll make sure it's published. Yeah, I'll make sure the actions run right after the PR merges, yeah.
**Giuseppe Ognibene (Coralogix)** 30:18 Okay, bye bye.
**Tyler Yahn (Splunk)** 30:20 Yeah, if I'm not… and then I'll double check. If it's not run every night, then I'll… Try to fix that, because I probably want it to. So, yeah.
Yeah, that sounds good.
**Giuseppe Ognibene (Coralogix)** 30:29 Okay.
Thank you.
**Tyler Yahn (Splunk)** 30:32 Yeah, well, thanks for bringing it up.
Yeah, the thing kind of bites me all the time, so I'm happy somebody's actually gonna fix it, that'd be great.
Okay, cool. So, if that's the end of that, I don't see any other agenda items on the list.
Any other topics folks need to talk about, or things they're working on?
**Giuseppe Ognibene (Coralogix)** 31:02 I'm working on the bit filter cache.
Is the PR open?
You reviewed with Rafael?
I'm working on that, it's… There are some edge cases that I didn't consider, and I'm testing it probably because the, you know, the valid speed is used by many, many probes, so I don't want to fix something and break everything else.
But that's…
**Tyler Yahn (Splunk)** 31:30 Doing great work on that, so yeah, I appreciate it. That's… it's, like you said, it's spicy, so, yeah.
**Giuseppe Ognibene (Coralogix)** 31:36 Yeah, I need to test it also on REL.
And that's the hard part.
But I did it.
**Tyler Yahn (Splunk)** 31:44 Oh, nice, okay, yeah.
I heard Mike Dame is pretty good at Red Hat Enterprise Linux stuff.
**Mike Dame (Odigos)** 31:54 I learned a lot of that from Andre.
But… at least as far as eBPF goes, he helped us with a lot of stuff. But, yeah, REL's fun. SE Linux is… It's on… Little beast.
**Tyler Yahn (Splunk)** 32:11 Yeah.
I just assume that SELinux has saved my butt a million times, that I just don't know about it, because it's bit me so many other times that it otherwise can't be worth it.
**Mike Dame (Odigos)** 32:21 Yeah.
The guy who wrote it is pretty cool, Dan Walsh. He was in the.
Red Hat office I worked in.
Nice. Very Boston-y.
They did, he's, lead on, like, Podman, or he was, I think he just retired recently, so Podman and Cryo was also… You have SELinux to thank for that.
**Tyler Yahn (Splunk)** 32:41 Hmm.
That's interesting, actually.
It's cool.
Awesome.
Anybody else have any updates?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 32:57 So I'm coming to Kubecon now. I wasn't originally, but that's a last minute thing, so I'll be there if anybody else is going to be there.
**Tyler Yahn (Splunk)** 33:06 Yeah, Nicola and I will be there. I'm trying to think of other folks that are…
**Endre Sara** 33:11 I'll be there.
**Tyler Yahn (Splunk)** 33:11 Andre.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 33:12 cool.
**Tyler Yahn (Splunk)** 33:13 Yeah.
Cool. Yeah.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 33:15 Is that… is anyone going to the Maintainer Summit on the Sunday?
**Tyler Yahn (Splunk)** 33:19 I'll be there as well.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 33:21 Awesome. So I will, I will see you there. I got an invite.
**Mike Dame (Odigos)** 33:25 Yeah, I had a ques… is the Maintainer Summit… I'm looking at that, and it looks like it has, like, the same, like, maintainer requirement, is that… Because, like, what the CNCF considers a maintainer is, like, the TC and GC.
And…
**Tyler Yahn (Splunk)** 33:43 Oh.
**Mike Dame (Odigos)** 33:43 like.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 33:44 No, there's a big CSV file.
Yeah.
**Mike Dame (Odigos)** 33:48 Yeah, that CSV file has, like… it doesn't list SIG leads for OTEL. That's the same thing, because we were trying to do a, a maintainer track talk. Me and, Rafael, we were trying to submit on maintainer track, and we talked to, Drassy.
Or, not Draft, Severin about it, and Austin Parker, too, and we were trying to figure out, and it's like, yeah, the CNCF for Kate's.
All the SIG leads are considered maintainers, like all the maintainers, but for OTEL, they just keep it at the TC and GC. So we couldn't submit a maintainer track talk because we're not actually in that CSV of maintainers. So I would look in that CSV and see if you're actually listed in there.
Because… That is the…
**Tyler Yahn (Splunk)** 34:30 gave a maintainer talk. So, okay. I mean, like that must have changed. I'm guessing.
**Mike Dame (Odigos)** 34:35 Yeah, we couldn't… we couldn't submit ourselves. One of the maintainer… one of the, like, TC or GC could submit for us.
**Tyler Yahn (Splunk)** 34:41 Really?
**Mike Dame (Odigos)** 34:42 Like there's a whole, yeah, I'll show, I'll send you guys the Slack thread, but if that's what I'm asking, cause I looked at the maintainer thing and it's like, you have to be in the CSV and like.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 34:49 Yeah.
**Mike Dame (Odigos)** 34:49 I'm not in the CSV.
Huh.
So yeah, I'll send you that because like, yeah, we couldn't just submit it on our own. It could have like Severin could have submitted the maintainer talk for us, and that's the way that you know you can do it.
But it has to be, like, it's really… I was talking to Austin a lot about it, like, this is so dumb that it's, like, just TC and GC that the CNCF sees as OTEL maintainers, where every Kubernetes SIG gets their own, like, the SIG leads, right? They're maintainers, but… So that was my… I don't know if I can go to the maintainer talk or not, and I can… I feel like bringing it up is gonna be, like, the same… argument that I had. I mean, Austin's on our side, at least, but…
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 35:36 If, if you have a KubeCon registration, it's free to register for the maintainer summit, and it's just like it sends a request.
And it goes for review.
**Mike Dame (Odigos)** 35:47 Okay.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 35:49 So you can… there's some space to, like, write a little bit. There's some text boxes, so you could try and… Argue the case, and then if, if it gets rejected, you can appeal it as well on.
**Mike Dame (Odigos)** 36:01 Okay.
Yeah.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 36:02 Slack.
**Mike Dame (Odigos)** 36:03 I wasn't trying to argue with you guys about what I'd seen or not. Like, I was…
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 36:08 No, no, I…
**Mike Dame (Odigos)** 36:09 Oh, you had done it, yeah.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 36:11 So, so, no, it turns out I got nominated for an award for SIG Instrumentation. Oh, cool. That's how I got in, but then I was stressing out about it, because I wasn't in this CSV file, and I'm like.
They want me to go, but am I allowed to go?
So they, yeah.
**Mike Dame (Odigos)** 36:29 Yeah, you should check that CSV. It's interesting.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 36:32 Yeah, so it turns out, so I donated a repo to SIG Instrumentation, which I was a maintainer of, the Kubernetes mixing, and apparently that classes me as a maintainer.
Yeah.
**Mike Dame (Odigos)** 36:45 Kubernetes maintainers for every SIG are listed in there. You look, it's like Kubernetes has like 140 like maintainers.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 36:51 years.
**Mike Dame (Odigos)** 36:51 The CSV in OTEL has, like, 25.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 36:54 Right.
**Tyler Yahn (Splunk)** 36:57 Yeah, so there's a…
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 36:58 Yeah.
**Tyler Yahn (Splunk)** 36:58 There's a community PR for the profile itself that's actually actively changing that mic as well. I don't know if you noticed it.
**Mike Dame (Odigos)** 37:05 Yeah, that's… I've been trying to… there was a thread that I was following, if you have that, PR, or, like, that link, because I've been trying to follow that, too, because I'm totally on the side of, like.
This is… silly. Like, we've got, you know, your second biggest project, and you're not letting any of the, like, SIG leads be, considered maintainers. It's just…
**Tyler Yahn (Splunk)** 37:28 Yeah, I mean, I don't…
**Mike Dame (Odigos)** 37:29 keep.
**Tyler Yahn (Splunk)** 37:30 like I said, like, I gave a talk at it last year, and so it wasn't… like, I didn't have any of these problems. So, like, unless you got, like, new management that's coming in and saying, like.
We're gonna be really strict about this, but, like, yeah.
Also, like, I've gone to the Summit, like, multiple years now, and, like, I've never had any issues of just getting excited.
**Mike Dame (Odigos)** 37:48 and.
**Tyler Yahn (Splunk)** 37:49 So, yeah.
**Mike Dame (Odigos)** 37:49 I guess I'll try to submit it, and maybe… maybe I'm just, like, following, like, trying to find rules to follow, and if I just submit, it won't be a problem, but that was… that was my question, was if… if I… can I just, like, apply to this? Because I just stopped when I saw that there, and knew that I'd had these problems this year already, so kind of gave up.
**Tyler Yahn (Splunk)** 38:08 No, yeah, I think if you just submit, you'll get accepted. Also, it's like… .
it's kind of poorly attended, because it's on Sunday already, so I don't know why they would turn people away, to be honest, especially people who are interested in, like, the CNCF, so… yeah.
**Mike Dame (Odigos)** 38:25 Yeah.
Oh, cool. Thanks.
**Tyler Yahn (Splunk)** 38:27 Yep.
**Mike Dame (Odigos)** 38:28 I'll try, and hopefully it'll be good, but…
**Tyler Yahn (Splunk)** 38:32 Yeah.
**Mike Dame (Odigos)** 38:33 on CNCF stuff.
**Tyler Yahn (Splunk)** 38:36 Contributor Summit, okay, yeah.
Looks like there's a Slack channel for it. Cool.
On that note, also, anybody submit a talk yet to the KubeCon EU?
I'm thinking there's an idea there, too, but I haven't submitted yet either myself, but yeah.
I think the Cfp, actually, let's see.
Maybe I'll look it up really quick, maybe I won't.
computer.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 39:06 They extend it, maybe, I think I saw the other day.
**Tyler Yahn (Splunk)** 39:09 Oh, did they? Oh, nice. I just remember it being, like, in, October, but
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 39:16 It says 11th of October on the website.
**Tyler Yahn (Splunk)** 39:19 Okay, yeah, that's what I was looking for. Cool, okay, so 11th of October, so I think that's another, 2 weeks, I think? So yeah.
If folks have talks.
I want to go hang out with Mario in Barcelona. That's the way to do it.
**Mario Macias** 39:34 Yeah.
Yeah.
**Tyler Yahn (Splunk)** 39:40 Well, cool. Alright, well, we can end this meeting here. I don't think there's any other topics, unless I'm wrong.
But yeah, it was good seeing you all, really excited, look forward to Matias' PR, try to get a review on that if you can, please, and then the release PR coming out, tomorrow or the next day, yeah. But yeah, really excited. Coming up on a big milestone, so yeah.
Thanks, everyone.
Talk to y'all.
**Giuseppe Ognibene (Coralogix)** 40:06 Right.
