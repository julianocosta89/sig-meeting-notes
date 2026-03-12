SIG: CI/CD SemConv SIG
Date: 2026-01-13
Duration: 32 minutes
============================================================

## Zoom Recording Transcript

**Christophe Kamphaus** 00:32 Oh.
**Alan Clucas** 00:33 Hello!
How are you doing?
**Christophe Kamphaus** 00:37 Why not you?
**Alan Clucas** 00:40 Yeah, right.
**Adriel Perkins** 01:04 Good day.
**Alan Clucas** 01:07 I am.
**Christophe Kamphaus** 01:08 boom.
**Adriel Perkins** 01:11 So, Alan, I can see my face in the reflection on the screen door in the background. It's wild.
**Alan Clucas** 01:23 I should probably do something about that, angle the camera some way.
**Adriel Perkins** 01:27 Yeah, no worries.
**Alan Clucas** 01:28 Like… Well, no, it's probably not a good idea, generally. I mean…
**Adriel Perkins** 01:32 Well, at first, I was like, wait, am I on the TV in the background?
**Alan Clucas** 01:35 What is that? Yeah. I've got quite a big monitor, so…
**Adriel Perkins** 01:39 Yeah, that's awesome.
Cool, cool.
Alright, let's see… Reorganize my tabs real quick.
Y'all can't hear the dogs whining in the background, can you?
**Alan Clucas** 02:09 Neither.
**Christophe Kamphaus** 02:10 No.
**Adriel Perkins** 02:12 Cool.
I'll go ahead and share my screen.
Give everyone a minute to add whatever topics they have.
**Christophe Kamphaus** 04:02 Sean, we get started?
**Adriel Perkins** 04:07 Yep, sure can.
Alright, we'll spend the first few minutes talking about the board as usual.
I haven't… haven't heard on this one, yet.
So… the same status, I think, as probably last week, which is… I don't know.
We'll see.
I don't know that I… was I supposed to… I probably was supposed to reach out to him last week, wasn't I?
I did not have an action item that I wrote down, so maybe… maybe… okay.
Or maybe I just forgot to write down the action item.
Whoa, whoa.
I'll see if I can reach out this week, though, and let me just write that down.
See, which one was it?
On the support for SDKs.
Aspect. We've got a couple things, in flight.
So, my PR for Python… Did get, did get reviewed, finally.
And there were some… some comments and questions that I'm kind of going through right now. Right now, I'm working on the type checking and rinsing, because those are red, but there were some other ones that were like, let's make this, because the… the spec is not considered stable yet.
Let's make this, private, opt-in in the API, so that it's not, like, implicitly… it's not, public.
API that we might break in the future. Let's just keep it private for now. That means people can still use it. It's just they have to explicitly opt in to use it instead of implicitly, have it available to them when using the Python SDK. So, that's one of the changes that I made.
But it is making… making good progress, and I was actually working right before this call to… to get some of those additional changes made. So hopefully, hopefully this can get merged soon, pending more… more feedback and comments.
The other one that, I think there's two other ones that are, I think, you know, warrant some… some comments.
The Go one and the JavaScript one.
Hold on.
So, on the go… no, this is the JavaScript one.
On the go one, it looked like this was added to the 140 and 1.40 milestone.
I don't know that… like, I'm not… I haven't picked it up.
So my question…
**Alan Clucas** 07:28 I was intending to pick this up this week, if you still want it doing.
So…
**Adriel Perkins** 07:34 Yeah, that was actually what I commented on.
**Alan Clucas** 07:37 Yeah.
**Adriel Perkins** 07:37 About… because I know you were going to pick it up from our conversations last week, but then I noticed when I came back that it was, like, set to the milestone, so my ask was, like, has someone already pick this up, and they go, Sig, I haven't heard back. If I don't hear back by, I mean, I'd say just open the PR, and… Yeah, if you've got time to open the PR, that'd be great.
But we can go to the GoSig, too, and just, like, ask if we haven't heard… heard back.
**Alan Clucas** 08:06 Yeah.
**Adriel Perkins** 08:07 So… But I just wanted to bring that up, because it was added to the 140 milestone, which is literally the next release, so…
**Alan Clucas** 08:14 Yeah.
**Adriel Perkins** 08:15 It's cool.
I just don't know if someone's working on it. Or, like, not us, it was someone, someone from their side.
On the…
**Christophe Kamphaus** 08:24 NPR, what was the, opt-in that you had to implement?
**Adriel Perkins** 08:34 So… Let me go back to this PR… oh, actually, I have it up here. So basically, in Python, when you have a library, the way you do opt-in is you change the file name to be underscore, and when you do a import, you know, opentelemetry.sdk.
that file.
And it's, you know, class don't get automatically, like, brought in. You have to explicitly say, from this import underscore ENV carrier. And so that essentially makes it private, by what they call it.
But it just means that it's not, like, a stable public-facing API, and you have to explicitly opt in. So that was the request that they had made, was because the spec isn't, you know, stable. Let's keep this.
**Christophe Kamphaus** 09:23 Yep.
One thought I had was, for the stretch goals in the parent issue.
Why don't we already create issues in those repositories?
And I guess someone from… Those… would already implement some.
**Alan Clucas** 09:48 Feels like a good call, especially as they're likely to be quite an easy, kind of, good first issue thing for… for people that might get… well get done.
They're not complicated to implement, I don't imagine.
**Adriel Perkins** 10:21 Alright, we'll add that action item there.
Yeah, good shout.
The other note… Is the JavaScript one?
Oh, wrong, PR.
I haven't responded to this yet, but Because this just got opened a couple days ago, and I haven't had time. But basically.
We've got someone who's willing to pick it up in JavaScript, which is awesome.
So I'm gonna respond to this, feel free to take a look.
But, basically, Yeah, that's cool, and I think that, you know, a list goes to the point you just made, too, Christoph, which is, like, why don't we just open them in the other repos, because somebody might pick them up, and that's exactly what's happening in JavaScript, so… Just wanted to shout that out, thought that was… that was pretty cool, if someone's willing to, to do it.
**Alan Clucas** 11:24 Nice.
**Adriel Perkins** 11:28 Let's see. Back to the board. So this is making good progress, I think, with the E&V stuff.
The other stuff, I think, has stayed where it currently is. No, no one's picked this one up yet, I haven't heard.
**Christophe Kamphaus** 11:47 I opened an issue.
**Adriel Perkins** 11:49 Okay. I think it's at the bottom.
**Christophe Kamphaus** 11:52 It was for giving guidance, if someone wants to opt in to the CICD SUMConf.
the question was asked in Jenkins, because… in the Jenkins OpenTelemetry plugin, because they wanted some migration paths from the old funder-specific conventions to the new OpenTelemetry conventions.
And I asked, yesterday in the sumconfig.
How to go about it, and the feedback was basically… We don't need it yet, because we are still experimental.
There's no de facto stable with us like there was for HTTP and RPC.
So, we don't need it. Or at least… Maybe we can ask, are there any vendors where We already broke something where they need such a flag.
I don't think so. If you scroll down, there was someone Looking into it, and apparently he found yeah, that… No vendor already, uses.
adhered.
**Alan Clucas** 13:06 This is kind of a question I was probably going to ask at some point, but from a different angle, in other workflows is used for Lots of different things, including CI.
So, in some cases, I should… the… so I think it would have to be on a controller, on her controller.
But I don't know, we could configure it however we wanted, but… For CI jobs, you would like to get CICD, SEMCOM tracing.
for non-CI jobs, you probably don't want it, because it doesn't quite fit the model.
So, should we… well, I don't know what to implement there. Should I implement something different?
for non-CICD use cases, which is what I've done at the moment. I've got… I haven't tried to follow CICD, because I haven't tried to adopt it yet. Just getting the rest of it all working was enough.
But, hmm.
**Adriel Perkins** 14:12 Yeah, I think part of that conversation… so, on the non-CI-CD-specific workflows.
part of that goes, I think, to, like, the original proposal we had was, like, pipelines are agnostic of CICD. Like, they're just flows of things that occur in a system, right? You can call it a workflow, too, but the… they're basically interchangeable, right? It's a pipeline of things that are occurring in stages and steps.
the… original statement was it should be agnostic, and then the request was made, if you make it agnostic today on your first pass, what you are going to get is a lot of feedback from a lot of different people, and no… make no progress. So, the ask was to put it under the CICD namespace.
For now, but this issue, there actually is an issue about this, where it's like, can we just have semantic, like, unified conventions for task workflows and pipelines and jobs? So that it's, like, consistent across the board, and it's not specific to CICD. So feel free to take a look at this one.
**Alan Clucas** 15:18 Yeah. It's gone.
**Adriel Perkins** 15:19 Fairly decent thread on it.
But yeah.
**Christophe Kamphaus** 15:24 Yeah, and I think at the moment, it's a bit…
**Adriel Perkins** 15:27 Stuck.
**Christophe Kamphaus** 15:28 Because I would also ask, then, for there to be a working group around workflow.
like, we have one for CICD.
And I don't think there's any candidates yet, or enough candidates.
Because they would not want just CICD to implement it, but also other workflow engines.
Business processing entrance, to implement.
**Alan Clucas** 15:56 Indeed. Yeah. All right.
Well, at least it's being considered. Thank you.
**Adriel Perkins** 16:02 You're welcome. Good question.
The other thing… On… this one.
So… It's been a while, but when I… when I remember using, like, the Weaver-generated semantic conventions for… Actually, for both Go and Python, essentially anything that's experimental and not considered stable has to be explicitly opted into anyway.
So it's like… you don't just get them for free, as stable, because they… they are generated as experimental, in the actual source code. Like, I think in… I think it was in Python. I think they were considered private, so, like, I had to actually underscore import, to explicitly opt in. I don't know if that was the same for Go, but… Yeah, I mean, these are experimental, so that kind of tracks with me in terms of that statement. We don't have to try to provide some type of environment variable.
**Christophe Kamphaus** 17:07 in Java, so you have experimental packages, so if you import something from that, and it's also a different, dependency. If you import from that, you know that you are importing experimental.
So yeah, coming back to the vendor-specific, opt-ins.
Here, it's an up to the vendor how they want to do this with a feature flag, or… Some parameter.
**Adriel Perkins** 17:44 Yeah.
Makes sense.
**Christophe Kamphaus** 17:48 So, yeah.
My thought here is just closing this issue.
And if we have breaking changes later.
Create a new one, or reopen this one.
Yeah, I said, or if we add breaking changes after we change the ability.
That's a use case for these flags.
**Adriel Perkins** 20:10 Alright.
Rock on.
**Christophe Kamphaus** 20:14 And white.
**Adriel Perkins** 20:16 Cool.
Well, it was a little bit more than… 7 minutes, but it's okay, it was useful. Christoph, I think you have… oh, that was… That one.
**Christophe Kamphaus** 20:27 Yeah, we didn't use a time box. The next one, yeah, I got in contact with Cyril from Jenkins, Open Telemetry Plugin.
We had some handover on his work-in-progress PR, so I will take it over, and hopefully get it to the finish line.
And there, the question was also asked, how would they use the feature flag for… opting into the Hotel SAMCOM.
**Adriel Perkins** 21:05 Cool.
Awesome. That was a good update.
Looking forward to seeing that in there.
Anything else on this one?
**Christophe Kamphaus** 21:21 There's some other refactoring I might pick up later in that plugin, but yeah, it's… maybe I will just wait for spec.
Some development of multiple resources.
might be useful, Saran says also we see long-running span issues that I might take a look at.
In the context of Jenkins.
**Adriel Perkins** 21:46 Okay.
Okay, cool.
There's nothing else on that one. I think, Alan, the next one's yours.
You're… you're muted, or you're unmuted. Are you double muted?
**Alan Clucas** 22:25 I'm mechanically muted.
Yeah, sorry. I should have probably typed it out in Slack, but, I never got around to it, so here we are. I'm gonna talk through it. Last week we were talking about, RWX and, Christoph raised that, the idea with CICD was that the top-level trace had a resource associated with the… With the particular run, whatever it was, which… is sort of fine, I believe, if you're doing it the way RWX would do it, or GitHub would do it, or something, but it's… problematic in the Argo workplace case, where we've got a controller, and my current resource that I'm emitting with the spans and the metrics is to do with the controller that's running. It's about that, it's not about the specific workflow that's being executed. And it would be lovely if I could tie some external object, like a resource, to the particular trace that propagates, you know, that somehow magically got added to all the spans that got emitted, so that, you know, easy lookup of URL for that would happen.
But, that involves creating a tracer provider for every single individual workflow and maintain… it's got the same problem as long-running traces. We've got to have these… a trace of provider per… per workflow that lives for a very long period, and therefore uses up quite a lot of memory, I'm imagining, because we're no longer getting the, you know, the deduplication and Of traces and attributes and all of that stuff that must be magically happening behind the scenes, with a single trace provider for the entire executable.
Which is what I'm currently doing.
And so, I'm really bringing it up here as just, like, this is probably not something we've really thought about as a group, and… Wondered if you had any thoughts.
**Christophe Kamphaus** 24:41 Yeah, it's the same issue I just mentioned also for Jenkins.
I'm just looking up the… I think there's a PR in spec.
I would share it here. Maybe we can create an issue, just to track this.
Goes, indeed, for… collector receivers, we can just Assembles resource on the fly.
What for… anyone using the SDK, it's a pain.
**Adriel Perkins** 25:18 Can I ask the stupid question here?
when we're talking about resource, do we mean, like, the actual resource attributes that are attached? Are we saying that in the SDKs, we can only attach one resource attribute?
**Christophe Kamphaus** 25:33 Now you can use multiple resource attributes, but the resource will always be the same. It's defined once in the SDK.
at industrialization.
**Alan Clucas** 25:42 Yeah.
**Carlos Alberto Cortez** 25:45 By the way, have you considered using instrumentation scope for that?
I mean, in the past, it used to be a build-time concept, now it's a runtime concept.
So, I don't know how elegant that could be, but that would work, because basically, you could be creating, A different instrumentation scope instead of creating multiple trace providers, you know?
**Alan Clucas** 26:08 I didn't find a way of doing that, but I didn't look too hard, so…
**Christophe Kamphaus** 26:13 No, I saw.
**Carlos Alberto Cortez** 26:14 Actually, you know what? The problem there is that some SDKs don't implement this yet.
as a runtime concept. I don't know, do you remember which SDK were you looking into?
**Alan Clucas** 26:26 Let's go, so that's…
**Christophe Kamphaus** 26:28 For me, it's each other one.
**Carlos Alberto Cortez** 26:30 They… yeah, Go has it for sure, but, it's relatively new.
**Christophe Kamphaus** 26:38 And for sure, SamConf has not defined it, so… There's no concept of, instrumentation scope in some conv.
**Carlos Alberto Cortez** 26:49 Yeah, actually, I do remember seeing a PR. I honestly don't remember which one was by you, Christoph, and I remember this one about creating multiple risk providers.
In the same column from our side.
And then when we had the change in the spec, I think it was by September, probably, making this remediation scope.
dynamic, let's say. I remember thinking about that. So maybe I can… spend some time outside of the call looking for that, and see whether that… that's something we can discuss. Because relying on multiple resources, like, even if we… I mean.
I am, like, on the side working on the loan… long, long span traces.
**Alan Clucas** 27:32 Yeah.
**Carlos Alberto Cortez** 27:33 Even with that, the problem is that resource cannot be recreated. I mean, there's these new concept called entities.
which will try to address that, but, I'm not sure that will work for us, you know?
**Alan Clucas** 27:47 But do you think an instrumentation scope would work?
**Carlos Alberto Cortez** 27:50 I would say, yes, try, yes. Somebody would have to, you know, let me actually look for that.
We're parties that ingo, and I would say it's worth trying.
**Alan Clucas** 28:04 I can certainly have a… have a look. I wasn't aware it existed at all, so, I will have a play.
And report back next week if I've got time.
**Christophe Kamphaus** 28:14 Yeah, I remember that we discussed using instrumentation scope, But I don't remember… Probably it's because it was not defined in SAMconf, and not every SDK implemented it.
**Carlos Alberto Cortez** 28:28 And yeah, and as I mentioned before, it used to be a compiled time concept.
So, basically, what you, what you had… it was, it was like the… resource, at the time.
**Alan Clucas** 28:41 I mean, resource… You can add stuff dynamically at… Runtime, but only at startup time, basically.
**Carlos Alberto Cortez** 28:50 That's correct, yes.
**Alan Clucas** 28:51 Yeah.
Okay.
Cool, thank you.
I'll get back with what I find and… what I make work.
Cool, thank you, Carlos.
**Carlos Alberto Cortez** 29:06 Yeah, let's see how that goes, yeah, keep us posted.
**Adriel Perkins** 29:15 Cool, on that note… Oh, okay, Carlos, do you have any update on the, long burning traces stuff?
**Carlos Alberto Cortez** 29:23 Not yet, yeah. Just… slow start of the year.
**Adriel Perkins** 29:28 real quick. Do you need any support from us? Is there anything we can… we can do?
**Carlos Alberto Cortez** 29:32 Nothing for now, yeah.
**Alan Clucas** 29:36 I'm the person who originally raised the CICD issue around this, so, if there is anything you want to get in contact with me about trying out or whatever.
in Workplace Go, then I can do it.
**Carlos Alberto Cortez** 29:50 Yeah, so to be honest, I think that probably next week, but most likely in two weeks, I will have an update from, you know, going over the stuff and trying some ideas and some brainstorming here.
**Alan Clucas** 30:02 Yeah, thank you.
**Christophe Kamphaus** 30:05 Yeah, I shared the PR in spec, where Josh was looking into it.
along multiple resources in an SDK.
**Alan Clucas** 30:15 Thank you.
**Carlos Alberto Cortez** 30:24 Yeah, yeah, I remember this PR. I think it's a good PR, but… Hasn't received enough attention In part because of the… of the Christmas break, you know, but yeah.
**Adriel Perkins** 30:44 Mmm, interesting.
Well, maybe this is something we can… we can look at and provide feedback on to help get some additional eyes on it.
**Carlos Alberto Cortez** 30:56 So, honestly, I would prefer that we try in the instrumentation scope, and only if that doesn't work, when we can… Jumping.
I mean, instrumentation scope is something that already exists, you know? Diesel tap may not be accepted, for example, you know?
So you… so we can… really rely on instrumentation scope, let's go. If that works well, I'm fine, without feeling like a hack. Otherwise, yes, let's… let's push for this.
**Christophe Kamphaus** 31:33 Yeah, and for sure, it would need to be implemented in SDKs before it's… we could use it.
**Carlos Alberto Cortez** 31:42 Yep.
**Adriel Perkins** 31:50 Cool.
Good to know. But you stop it. It's enough.
Sorry, dogs, I meant to mute myself.
Cool. Well, anything else?
Anyone wants to chat about?
**Christophe Kamphaus** 32:08 from my side.
**Alan Clucas** 32:09 No, I'm good. Thank you.
**Adriel Perkins** 32:11 Awesome.
All right, well, we'll get some time back to the day. It's good seeing y'all. Have a good week. We'll see you next week.
**Christophe Kamphaus** 32:18 You too?
**Alan Clucas** 32:18 Dude.
**Christophe Kamphaus** 32:19 Steal.
