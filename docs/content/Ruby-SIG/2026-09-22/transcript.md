SIG: Ruby SIG
Date: 2026-09-22
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 01:04 Oh, there's one.
It might just be you and me?
**Xuan Cao** 01:09 Hi, I guess so, if, if messages, not gonna shut off, shut up.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 01:16 Bill.
I'm not in a place where I can do a lot of screen sharing.
We might just have to… Talk to each other.
**Xuan Cao** 01:36 Yeah, I, I didn't attend this, SPAC Sue.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 01:42 did not.
**Xuan Cao** 01:42 Yeah, I do not. Actually, I never attend, attend this specific, so… I appreciate it started.
Attend them in the future.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 01:55 I think I did once, and… Didn't, again.
September 22nd, looks like… I'm looking at the spec SIG notes, at least.
I don't see any of the Ruby people there.
In the attendees list.
So I guess we're gonna have to… Do what we can with looking at notes.
**Ted Young (Raintank, Inc. – Grafana Labs)** 02:28 Hello!
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 02:30 Aye.
Actually, I saw that guy's name in it.
**Ted Young (Raintank, Inc. – Grafana Labs)** 02:34 Yeah, I was there.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 02:35 I was talking about Spec SIG. We usually have somebody go to Spec SIG and bring over interest, pertinent items, and I was skimming the Spec SIG notes to see If any of our people had gone and… They hadn't.
**Ted Young (Raintank, Inc. – Grafana Labs)** 02:47 Yeah.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 02:47 I was like, I guess we're on our own with notes, but no, you're here!
**Ted Young (Raintank, Inc. – Grafana Labs)** 02:50 Yeah, I'm here. I'm gonna say hi to you guys.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 02:53 Well, welcome.
**Ted Young (Raintank, Inc. – Grafana Labs)** 02:55 Let's see, what did happen?
Spec SIG was so long ago, that it was hours ago.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 03:01 Right? Who can remember? I barely remember breakfast.
**Ted Young (Raintank, Inc. – Grafana Labs)** 03:04 Yeah.
I think the most interesting thing for this SIG was around, language injectability.
Right, so we're trying to get everything stood up with the packaging SIG and the hotel injector.
to be able to make OpenTelemetry easy for, like, a central operator to, like, roll out at scale, right? This is traditionally the weak spot that OpenTelemetry has relative to, like, traditional you know, proprietary agents is… it's, the… the metaphor… I found a metaphor in Japan, which is there's all these automatic doors, but you have to push a button for the door to open, and I'm like, that's open telemetry. It's like… and literally the doors say auto on it, and they do automatically open.
After you push the button, and that's like OpenTelemetry. It's like, it is automated, you're not manually…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 04:06 It's like the…
**Ted Young (Raintank, Inc. – Grafana Labs)** 04:07 libraries together.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 04:08 It's like, what do you mean when you say dynamic scaling versus auto-scaling? There's, like, you could… do you have to turn a knob, or does the knob get turned for you? Yes, I,
**Ted Young (Raintank, Inc. – Grafana Labs)** 04:17 It's a good.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 04:18 metaphor.
**Ted Young (Raintank, Inc. – Grafana Labs)** 04:19 It's like, like, the Ruby Auto instrumentation is magic, you know, it works very well, but you still have to, like, boop every single app on the nose to install it, and we wanna, like… lift that up a level so that through the Kubernetes operator and through, like, Linux package management, there's a way to just be, like, you know, apt install telemetry, and just… everything has it by default. And one of the…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 04:49 I'm sorry?
**Ted Young (Raintank, Inc. – Grafana Labs)** 04:50 Oh, I was gonna say, and that works, but one of the things we're bumping into now is, like, in different languages, OpenTelemetry's a little unsafe due to dependency conflicts. gRPC being the most pernicious bastard dependency that shows up, and in some languages, it's very easy to shade things, or vendor them, and kind of, like, restrict the damage, and then there's other languages, like Python, where this is just a disaster, and it's, like, actually not safe to auto-inject OpenTelemetry Python SDK right now, due to some of its dependencies.
potentially having conflicts and blowing up. So, we wanna… the question was, like, can we just go around, and in every language, like… like, Protobuff in particular, but just in general, can we, like… Make sure that our dependencies are safe.
In a way where the chances that they're gonna blow something up if we auto-inject things, you know, can we, like, minimize that? So, I was actually showing up here to just sort of… ask the Ruby SIG, like, hey, like, what… what is the current state of that in Ruby?
you know, like… like, does gRPC cause problems? Is there, like, gotchas around dependency conflicts, or is that, like, kind of a non.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 06:11 One gRBC and Ruby's just sort of… unpleasant to… to begin with.
**Ted Young (Raintank, Inc. – Grafana Labs)** 06:16 it everywhere. It's a terrible dependency.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 06:19 And then on top of that, Ruby's dependency resolution can get weird, where if you… if a particular process tries to load two different versions, weird things can happen.
Yeah.
My… from my personal experience doing just about any open telemetry in just about any language, I'm like, HTTP protobuf is, like.
you get most of the advantages of GRPC, and none of it's…
**Ted Young (Raintank, Inc. – Grafana Labs)** 06:47 Money.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 06:47 gratefulness.
**Ted Young (Raintank, Inc. – Grafana Labs)** 06:48 So, the request was that for every language, we switch to hand-tooled… hand-rolled proto.
Because this is the last, usually where it's like, yes, don't use gRPC, use HTTP Proto, most people just have that as the default. Again, Python, bastard language, chose gRPC as the default, for whatever reason, you know, decisions.
Many years ago, but… and so, like, they have it more rough. But still, if you're… like, Proto can have, like, some weird gRPC-ish dependencies in some languages.
But, generally speaking… that was kind of the, like, do we have those problems in Ruby? Like, how bad is it over here?
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 07:34 I am… I don't have an answer for that right now.
**Ted Young (Raintank, Inc. – Grafana Labs)** 07:38 Yeah.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 07:39 But we can… we can find out.
**Ted Young (Raintank, Inc. – Grafana Labs)** 07:42 Yep. And I know this SIG, you know, is… has got… is pretty lean on staff.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 07:46 Yeah.
**Ted Young (Raintank, Inc. – Grafana Labs)** 07:46 So I don't want to be like, hey, here's a mandate to go do a birth.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 07:50 more work!
**Ted Young (Raintank, Inc. – Grafana Labs)** 07:51 But, but that's one option, is hand-rolled proto. The other intriguing thing, Alex Bowen, who I'm sure you know, was working on, you know, upstreaming the C++ bindings, kind of starting with Python, that.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 08:08 Yeah, the, what if we all, what if we all in the background, just to see? Yeah.
**Ted Young (Raintank, Inc. – Grafana Labs)** 08:14 Yeah, and that was the other, you know, potential… you know, I am nervous about saying that's the only solution we provide in the language, because I suspect there are many places where having that kind of dependency makes it hard for people.
And again, vendors that have done that in the past have just said, well, we just don't… bother with those customers, right? But OpenTelemetry wants to be standard, we want to work for everybody, so we want to have a native language option, but to what degree does, like, do, like, our Ruby problems and staffing shortages maybe get solved by, like.
switching over to that? Or, like, how bad… how easy is it to take on that dependency in Ruby versus, like, how awful is it to take on a… C++ dependency in Ruby?
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 09:07 I also don't… well, it is… possible.
to wrap.
C++.
**Ted Young (Raintank, Inc. – Grafana Labs)** 09:14 It is definitely possible.
normal thing to do in Ruby is to like Python to, like, take… have, like, your… the stuff that needs to be really efficient be down there in.
But also, you know, it can, you know, be awful looking at you, YAML. Like, so…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 09:35 And then there's the compile step at install, because,
**Ted Young (Raintank, Inc. – Grafana Labs)** 09:40 Right.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 09:42 Which is a thing.
**Ted Young (Raintank, Inc. – Grafana Labs)** 09:45 I just presume it's something that would be great for some users, and for other users, they'd be like, we cannot… We cannot inject this.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 09:54 If you care about performance, here's an option, but the trade-off is you gotta… You gotta…
**Ted Young (Raintank, Inc. – Grafana Labs)** 10:00 Yeah.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 10:00 compile it.
**Ted Young (Raintank, Inc. – Grafana Labs)** 10:02 But we're looking at C++ and Python, and I was just kind of curious how much Ruby could be maybe the other SIG that would be interested in kind of running with that ball quickly.
Because, again, it's a very common thing to do in Ruby, and I suspect also that the bindings would not be too hard to set up in Ruby, again, because it's, like, pretty normal, and I think this stuff already exists in Honeycomb, like, you all… have… These bindings may be for Ruby, maybe not.
Maybe not. But…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 10:34 The experiment started in Python, and it was a twinkle in my eye to do it for Ruby, too.
Yeah. And it never went beyond a twinkle.
**Ted Young (Raintank, Inc. – Grafana Labs)** 10:44 Right, but that could potentially be… be some awesome sauce that, you know, we could really benefit from. So that was why I was showing up.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 10:53 Okay.
**Ted Young (Raintank, Inc. – Grafana Labs)** 10:53 just to be like, hey, how are things going over here? I'm your GC liaison, and I will talk to the maintainers sometimes, but I was like, oh, I actually have time in my schedule to come to the SIG, so I thought.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 11:03 Wait, well, welcome. As you can see, we're a bit lean.
**Ted Young (Raintank, Inc. – Grafana Labs)** 11:06 I know, Ruby's always a bit lean, that's…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 11:10 Most of the folks didn't make it today.
**Ted Young (Raintank, Inc. – Grafana Labs)** 11:13 Yeah.
Yeah, I know that Matt Weir came back, whom I love yearly, but… Not today.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 11:21 Was happy to see his face again.
Yep.
Hannah and… and… Ayla from New Relic have been spearheading getting the logs and metrics signals stable, since we still have, like, a punch list of stuff to do to get spec coverage.
**Ted Young (Raintank, Inc. – Grafana Labs)** 11:37 Right. So, logs and metrics are still kind of in the works.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 11:42 They are in development status, and I… I… you… they, you can… Talk about the auto button. They will automatically wire themselves in if you choose to pick those libraries up in your own dependency graph. So, in addition to, depending on the standard, like, hotel gems, you can add hotel logs and hotel metrics and get… And if instrumentation uses them.
We're working on ways to make them automatically light up.
Parallel to, what if we just got them stable, and… then everything can depend on them. It's a… it's a bit of a… list. There are milestones in the GitHub project. The core Ruby project has a milestone for both signals and the punch list of issues to work on for spec compliance.
**Ted Young (Raintank, Inc. – Grafana Labs)** 12:33 So there's still… there's still, like, a pretty long… pretty… pretty big schlep left to… to get those things done.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 12:40 Yeah, I think having it written down very clearly like that might help the schlep, because, with as understaffed as we are, if we at least know what the next work is, it's not us wondering what to do next.
**Ted Young (Raintank, Inc. – Grafana Labs)** 12:52 That kind of, like, circles back to, C++, in a sense of, like… you know.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 13:00 What if we just did wrappers around C?
**Ted Young (Raintank, Inc. – Grafana Labs)** 13:03 Well, I don't know, in terms of, like, again, I don't think we should only do that, but it, like, that meant the effort could just be, like, finish up the APIs and get some instrumentation working and bind to an existing SDK that, like, how much… time does that… how much effort does that save at this juncture? Versus, like, oh, no, the SDK is, like, pretty much done, so not much time.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 13:31 That is a good question. I can take to the rest of the group, because I don't know the answer to that yet.
Here in the moment.
**Ted Young (Raintank, Inc. – Grafana Labs)** 13:37 Yeah.
So, let me put some stuff in the notes here, just before we forget.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 13:45 Come on.
**Ted Young (Raintank, Inc. – Grafana Labs)** 13:54 Plus, plus…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 14:01 What have we delegated?
It seems so promising. It's a promising idea.
Like, how far along are metrics?
Or are they coming along, and would… and would pivoting to, what if we just did the wrapper?
**Ted Young (Raintank, Inc. – Grafana Labs)** 14:19 Yeah.
And then the other one is…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 14:40 Grpc and the proto… Genesis.
Or, yeah, that's right, hotel dependencies in general. We tried, like, most languages tried to reduce the number of dependencies we actually demand.
**Ted Young (Raintank, Inc. – Grafana Labs)** 15:01 up.
Can we… Vendor…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 15:17 Rendering's an interesting idea.
**Ted Young (Raintank, Inc. – Grafana Labs)** 15:19 I don't know…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 15:21 There's some namespace issues with.
**Ted Young (Raintank, Inc. – Grafana Labs)** 15:23 I… Yeah.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 15:27 I mean, it's just… that's a… that's a path I had personally considered.
**Ted Young (Raintank, Inc. – Grafana Labs)** 15:32 I don't… it has been so long since I've done Ruby development, I don't know what vendor, shading, blah blah blah. There's always.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 15:39 Yeah.
**Ted Young (Raintank, Inc. – Grafana Labs)** 15:40 Copy and paste, you know, but… And we hand roll… our proto-deepad.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 15:59 Do you know that other places that have hand-rolled protocol.
**Ted Young (Raintank, Inc. – Grafana Labs)** 16:03 Oop, you roboted there.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 16:06 Yeah, so I guess that might be me.
**Ted Young (Raintank, Inc. – Grafana Labs)** 16:10 Could… could be me.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 16:12 Let me… let me drop and come back.
Or did that just clear? And we just cleared up. Okay, so my question was, that last point about, hand rolling.
Yeah. Proto. How… has anybody… has any of the other SIGH done something like that, and what was that experience?
**Ted Young (Raintank, Inc. – Grafana Labs)** 16:31 Lots of them are doing it, and they're experiencing.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 16:33 Interesting.
**Ted Young (Raintank, Inc. – Grafana Labs)** 16:34 Awesome. Two things. Awesome, okay. One, like, so, they're doing this in Python, they've already done it in Node, they did it in Java, I'm not sure what other languages, but… One, it… again, the proto… non-hand rolled proto is usually bundled up with gRPC in some way that sucks, right? So, it gets that SIG out from under that, you know, aversion conflict nonsense. The other thing is it usually comes with a pretty big speed boost, and for languages that are, like, global threadlocked and things like that, like, that speed boost is great.
So that's something they saw in Node, and they're seeing in Python, is, you know.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 17:21 Okay, so nodes in this list, too.
**Ted Young (Raintank, Inc. – Grafana Labs)** 17:23 Yeah, so people have generally been liking it, and it's one of those things that, in the past, was potentially a really onerous task, but these days, you know, with AI coding and other things.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 17:36 Can get ground out.
**Ted Young (Raintank, Inc. – Grafana Labs)** 17:38 Less work than it used to be to get it, you know, bite-perfect, hand-rolled proto-stuff.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 17:44 Going.
**Ted Young (Raintank, Inc. – Grafana Labs)** 17:45 Again, not like this SIG has just spare capacity lying around, but… That… that… when we looked through, like, what blows up, the answer generally came back is, like, just GRPC Proto, right? In every language, it's like, our dependencies are mostly fine, except… you know, gRPC and proto that depends on GRPC.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 18:10 I'm gonna cautiously… I'm gonna cautiously… set out the theory is, like, that's generally the only real external dependencies most of the SDKs take, because.
**Ted Young (Raintank, Inc. – Grafana Labs)** 18:19 Right.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 18:19 like, Everything else is just… I'm implementing spec in the language.
**Ted Young (Raintank, Inc. – Grafana Labs)** 18:24 Yeah, we don't ship a lot of plugins that require external dependencies, generally speaking. We just don't. I mean, like…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 18:32 instrumentation.
**Ted Young (Raintank, Inc. – Grafana Labs)** 18:33 Maybe a language takes a dependency on some weird HTTP client or some bullshit, but, like…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 18:37 Sure.
**Ted Young (Raintank, Inc. – Grafana Labs)** 18:37 Yeah, most of the other plugins we ship are things like samplers and whatever that don't…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 18:42 Yeah.
**Ted Young (Raintank, Inc. – Grafana Labs)** 18:43 Don't. So that's… that's… that's the bugbear, and also just GRPC is toxic, in the sense of, like, they have never done… put effort into… They make a lot of breaking changes, and major version releases, in a way that's, like.
super not…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 19:02 It hurts.
**Ted Young (Raintank, Inc. – Grafana Labs)** 19:02 Yeah, it's not a good dependency for us to have. But it's one that the spec requires us to have, right? Because it's a protocol.
And then the… and then proto… so that's just the one, yeah, that… and… and the answer has been, like, for every language that isn't Python.
just be like, don't choose GRPC!
That's not a default, but then also, like, for people who do want to use it, the answer is, like, we do want to vendor that, because we don't want people… It's auto-instrumentation that's driving this, right? Because we don't want to be in a situation where someone makes a little config change, and suddenly OpenTelemetry's blowing their deployment up, right? Like, that's, like, super bad for us.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 19:48 Yes.
**Ted Young (Raintank, Inc. – Grafana Labs)** 19:49 And when you're deploying OpenTelemetry in that manner, you don't… it's like you don't have the ability to get in there and twiddle with stuff, right?
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 20:01 That's the point. You didn't even want to push the auto button.
**Ted Young (Raintank, Inc. – Grafana Labs)** 20:04 The whole point is you don'.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 20:05 Like, the whole point is that you don't tweak a bunch of dogs.
**Ted Young (Raintank, Inc. – Grafana Labs)** 20:08 You probably don't even have access to that, right? You are some operator who does not have access to this stuff. You are not the application team. So, that's why it's like.
you know, what… if we are gonna offer GRPC, can we vendor it, or shade it, or something something in a way where it's not going to be creating… dependency conflicts for people. And we also learned that… Nobody offers JSON, but that was the other funny one. It's like… Most languages don't even offer that as an option.
But that's the other place where you could have problems.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 20:47 Yes.
And again, my personal experience has been, just HTTP protobuf. Stop it with the gRPC, Right. Half the people who… half the people who are an operator who can't control the application that they want to just inject instrumentation in also can't control the forward proxy that they're sending their telemetry through that doesn't really speak to your PC well, so just use HTTP and you'll be fine.
**Ted Young (Raintank, Inc. – Grafana Labs)** 21:08 But there's a difference between shouldn't and can't, and if we're offering it as an option in Ruby, and it's an option that can blow things up, then that's like a foot gun we're handing out.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 21:19 Sure.
**Ted Young (Raintank, Inc. – Grafana Labs)** 21:19 the… the question…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 21:21 You know, I could see that if you want the… We could… I… I could see where… where in the, in the menu of options, you've got, if you want to use gRPC, you don't get to auto-inject it. Like, auto-injection is only in this safe path.
And if you want a gRPC, I'm sorry, you're gonna have to learn how to push the buttons and turn some knobs.
**Ted Young (Raintank, Inc. – Grafana Labs)** 21:43 Well, yeah, but how do you… anyways.
Unclear how we… as someone who's working as a member of the packaging SIG, this is just… we're kind of just going around and reaching out. We wanna… we wanna bundle every language up, but as part of that bundling up, we're coming to the SIGs and being like, we don't wanna… we wanna have some ground rules, and this was actually getting… so there is a spec issue, let me link to this.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 22:07 Okay.
**Ted Young (Raintank, Inc. – Grafana Labs)** 22:08 But that is what kind of triggered this.
So there's a spec issue to go look at. We're trying to add some… some language into the spec, specifically about… about this stuff.
Because we wanna… we wanna have, like, a… just, like, in the spec, a list of criteria that… that an implementation needs to meet for us to… to bundle it up.
we want to have, like, a contract with the different SIGs about, like, what… like, let's all agree on, like, what that list of thing is, and then… Once a SIG meets that list, then the packaging SIG will come in and bundle it up.
You know, in partnership.
But we don't want to be bundling up things that can blow up, and we don't want to be handing out footguns, because we think that will be just very bad for the project's reputation.
If we do that.
So, just trying to get that list, so this is also, yeah, would be helpful for the Ruby maintainers. Just have a look at this PR.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 23:19 Yeah.
That was in the… that's in the notes.
**Ted Young (Raintank, Inc. – Grafana Labs)** 23:22 Yeah, I added it to the notes.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 23:24 Sweet.
I don't, so Ted, I don't have a whole lot of answers today, since I am just starting to re-engage with the SIG, not unlike Matt.
Having been… Great. Having been away for a bit, so,
**Ted Young (Raintank, Inc. – Grafana Labs)** 23:42 Oh, good.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 23:43 added opportunities to make it, but… I'm sorry, right? There's also, like, personal life and stuff, too, but…
**Ted Young (Raintank, Inc. – Grafana Labs)** 23:51 Well, cool. I mean, it seems like I missed the meeting where Kayla and Matt show up, but they generally show up.
Maybe?
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 23:59 They do.
**Ted Young (Raintank, Inc. – Grafana Labs)** 24:00 looking back, somebody usually shows up.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 24:02 Yeah, we'll chat.
**Ted Young (Raintank, Inc. – Grafana Labs)** 24:04 Really holding it down.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 24:05 Kayla's been the one holding us together, recently, yeah.
**Ted Young (Raintank, Inc. – Grafana Labs)** 24:08 Yeah.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 24:10 So we could chat with them in CNCF Slack, and we'll do some reading and some catch-up, and we'll chat Certainly the… we'll chat… amongst us, ruby chickens. We'll chat about it next week.
**Ted Young (Raintank, Inc. – Grafana Labs)** 24:23 Great, that's super helpful. But yeah, I'm… yeah, but also, just, yeah, just saying hi, I'm also the GC liaison, so I do talk to the maintainers, but also, like, just to let all of y'all know, if there's ever any, like, we're having some fucking issue, or we're confused about something, you can always just, DM me.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 24:43 Oh, don't open that door, I'm confused about all sorts of stuff, Ted.
**Ted Young (Raintank, Inc. – Grafana Labs)** 24:46 No, yeah, just saying, like…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 24:47 in your DMs.
**Ted Young (Raintank, Inc. – Grafana Labs)** 24:48 There's always the usual, try to go through the regular public channels, but if you have some question, you're like, I don't want to post this in public, you can always DM me and be like, yo, what, you know… help me navigate this. They're happy to do it.
Cool bean. Yeah. I had other questions, but they're really down the line. Like, Ruby on Rails, like, you know, where are we with that support? But it sounds like logs and metrics are, like, the answer. We need to get those done.
I think the tracing support's pretty good.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 25:21 Tracing support's pretty solid. the maintainers… Of your word.
super interested in traces, got traces stable, and… and…
**Ted Young (Raintank, Inc. – Grafana Labs)** 25:32 Yes, and that was that.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 25:34 And are, by and large, like, why metrics and logs? But,
**Ted Young (Raintank, Inc. – Grafana Labs)** 25:37 Yeah.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 25:39 The instrumentation for Rails is… is present. There are maybe some… new components added to newer versions of Rails that… I don't run rails at Honeycomb, so my day-to-day experience with what's changed is,
**Ted Young (Raintank, Inc. – Grafana Labs)** 25:58 Yet.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 25:59 has atrophied.
**Ted Young (Raintank, Inc. – Grafana Labs)** 26:01 Well, I think that's something to revisit on the other side of…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 26:05 Sure.
**Ted Young (Raintank, Inc. – Grafana Labs)** 26:05 Very stable.
But… My longer-term hope for OpenTelemetry, now that we've graduated and the spec has stabilized, around, like, the major signals, is, like, to then get the instrumentation stable.
And then once we've gotten the instrumentation stable, potentially, it's also if we've got maybe better tooling with Weaver, this is also something we're experimenting with in Python, the GenAI SIG.
Is experimenting with, and maybe we can export it. But just, like… Better tooling for writing and maintaining instrumentation. Right now, you know, actually using semantic conventions correctly is tricky, right? Like, it's like, you just have the fucking docs open, and you try to not screw it up, and that's…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 27:03 I have gone through a couple cycles of… Alex would probably even tell you, like, I would go through some… some… some loops of, yeah, we ought to have a library for this, with a whole bunch of constants, or something, with all of the submitted conventions, and then it hurts, and then it hurts every time you use it. And I'm like, what if we just use strings, folks?
And that means, yeah, having docs up, and whoever's doing the instrumenting is…
**Ted Young (Raintank, Inc. – Grafana Labs)** 27:27 Right. And some hope that a Weaver could help with this, right? Because Weaver is a code gen tool, you know, and there's some interesting patterns in, like, Java, for example, on creating these, like, instrumenter Like, like, semantic APIs, right, where they have, like, an HTTP client instrumenter object.
That, you know, so, like, we're… but again, they've got more people around, but the idea is they have, like, 50… they've got a whole bunch of HTTP instrumentation That they have to maintain. And rather than copy-paste stuff, you have an instrument or object, so now the API that you have to fulfill is not, traces, metrics, logs, the API you have to fulfill is, give me this data. Like, give me an object…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 28:21 The client is making a request.
**Ted Young (Raintank, Inc. – Grafana Labs)** 28:23 Give me an object that… that I need this information off of you, give me that information, and then I will, under the hood, do all the right things with it, and my API is like, you give me this thing.
and then I have a start and a stop, you know, method, and that's it. And then internally, that thing handles… All the stuff, tracing metrics, logs.
And that just makes it a lot easier to… To maintain a bunch of these things.
And so, like… and then if you're like, how could Weaver potentially spit out these things, right? Like, like, or then, like, if something changes to spec, you know, the semantic conventions, can Weaver update this thing?
And then, of course, that thing also gives you tests.
to prove that you're… you're spitting out the right stuff. And if you've got tests, and you've got objects like that.
how then easy is it to get, you know, AI coding to kind of help Write the code for you and not be a total idiot, because you've actually given it.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 29:32 You've got deterministic output.
**Ted Young (Raintank, Inc. – Grafana Labs)** 29:34 You've given it enough of a constraint that it doesn't have a lot of wiggle room to totally mess.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 29:40 Well, we, I know that, others have attempted to make, what we would have called helper libraries for, making… instrumenting HTTP, something… So, yeah, everybody sort of… Multiple people in parallel have found that going in that direction to be enticing, so that's intriguing to us, yes.
Speaking on behalf of people who aren't here, that does sound interesting.
**Ted Young (Raintank, Inc. – Grafana Labs)** 30:11 I could see that being maybe interesting on the other side of getting metrics and logs stable, right? Because that's when you'd want to sweep back through instrumentation and kind of.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 30:22 Because we'd have all of the signals ready, and now we can make the instrumentation produce the signal that you want.
**Ted Young (Raintank, Inc. – Grafana Labs)** 30:27 Produce the stuff that you want, add a specific version of semantic conventions, and.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 30:33 You know?
**Ted Young (Raintank, Inc. – Grafana Labs)** 30:33 stable and kind of get all that done. But that's, like, down below. And then, and then, you know.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 30:41 Wait, but wait, there's more!
**Ted Young (Raintank, Inc. – Grafana Labs)** 30:43 that would be then the point where we could maybe start sniffing around at trying to upstream some of this instrumentation, like going to Rails and other library communities, being like.
Would you like to just bake this in and own this, now that we have made it not suck to, like… deal with, you know? If we can make it, like, easy to under… comprehend and deal with, and very stable, and, you know, the APIs are decoupled from everything and blah blah blah, would they… Have more inter… potential interest in… Native instrumentation at that point.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 31:19 What if you framework authors didn't have to reinvent instrumentation?
But…
**Ted Young (Raintank, Inc. – Grafana Labs)** 31:24 I have always…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 31:25 For the frameworks who already have it, they'll probably go, but…
**Ted Young (Raintank, Inc. – Grafana Labs)** 31:30 Yeah, I don't know how much they care. This has always been an interesting… Conundrum to me, but, You know, to some degree, they're probably gonna be like, well, we just provide hooks, and that's all we care about, but… I've always felt that if they had these primitives, like, if they were maintaining runtime instrumentation more directly? Would that open the door to… providing playbooks, right? Like, like, caring a bit more about runtime observability, and being, like.
When you run our library, you should make these dashboards, and you should make these alerts, and when these things do this, you should tune these knobs in the configuration.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 32:16 Because we know we're emitting this information, we know that we could point you at how to interpret it.
**Ted Young (Raintank, Inc. – Grafana Labs)** 32:23 Yeah, and I don't know how many people are gonna care about that, but I've certainly seen some people care about it. CouchDB was an early adopter of this with open tracing, where they… embedded open tracing, and then they were like, yeah, here's how… here's how you run CouchDB, like, and like… Here, we provide you these weird knobs around, like, cache size, and, you know, buffer this or that, and whatever, and what should you… when should you.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 32:50 And how do you know when to turn one? Yeah.
**Ted Young (Raintank, Inc. – Grafana Labs)** 32:52 How do you know when to turn any of these knobs that we give you? And, like, being able to be like, here's a playbook for, like.
like, look at this information that comes out of this thing, and when it does this, turn this knob. So, but that's a long-term dream, and we're miles away from that. It sounds like trying to get more help involved.
But maybe also getting a C++ dependency could take some of this.
But again, I don't know how… how far… how helpful that is.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 33:29 Well, it… it… conversations I've had with Alex when he was doing the, the experiment with adding it to Python was it works when you're in an environment where the, what Ruby would call C extensions, and compile.
Right.
And in a world where we're trying to not even make the automatic door open, don't make them even have to push the auto button.
like… I foresee that the, any of the dynamic libraries, depending on the C extensions, That's gonna be… Very big speed bump, if not a block or two.
injecting.
**Ted Young (Raintank, Inc. – Grafana Labs)** 34:13 Yeah, yeah, I mean, I know Python.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 34:16 Maybe…
**Ted Young (Raintank, Inc. – Grafana Labs)** 34:16 Python on Python in environments where that doesn't work, but I feel like there's… there are ways of shipping these things.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 34:23 Well, with the packaging and, and, like, producing… like, Linux distribution packages, RPMs or devs, that are gonna run on a host of a particular architecture, that can have pre-built binaries in there, and that's cool, but the Kubernetes operator… maybe? Maybe.
**Ted Young (Raintank, Inc. – Grafana Labs)** 34:43 Well, we want the Kubernetes operator to be using the same primitives, right? So, it should hopefully… be able to grab the right thing. But again, yeah, my knowledge is a little thin, but the operator should frickin' know what architecture is.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 35:01 Yeah, as I said all that out loud, yeah, it's true. You know a target that it's gonna get attached to, so it's just a complicated build process for us.
**Ted Young (Raintank, Inc. – Grafana Labs)** 35:10 I should.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 35:10 produce the thing.
**Ted Young (Raintank, Inc. – Grafana Labs)** 35:12 Right, but it's also a world where people sometimes run really weird shit, like Rancher and stuff like that, that maybe we're like.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 35:21 But then… and that's where… that's where, certainly there's… there are patterns. I haven't done an extensive C extending in Ruby, but there are patterns for being able to choose between, C extensions for performance or pure Ruby for Not needing a compiler. Compatibility, yeah. Yeah. So, fair enough.
**Ted Young (Raintank, Inc. – Grafana Labs)** 35:42 I have a feeling it would help.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 35:43 work.
**Ted Young (Raintank, Inc. – Grafana Labs)** 35:45 Like, the three languages where I think it would help the most are Python, Ruby, and Node.js, just, again, because these are the languages that tend to have like… threads getting blocked and things like that. It's, like, harder. Maybe Ruby is a little more multi-threaded than Python and Node, but, you know, those have been more the problems, is, like, getting the exporter out of the way of the application is just hard.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 36:14 I think we've… we've managed… Hotel Ruby is thread-safe.
**Ted Young (Raintank, Inc. – Grafana Labs)** 36:19 Yeah.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 36:19 There's… there's hijinks when the application being instrumented is doing async stuff, and… context prop between, but…
**Ted Young (Raintank, Inc. – Grafana Labs)** 36:30 Yeah, I don't know how much of a performance boost you get, but it's usually.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 36:35 Performance boost we would… performance boost we would probably get just because we're not Ruby's slower than C, generally.
**Ted Young (Raintank, Inc. – Grafana Labs)** 36:42 And use a memory hog. Like, that's the other thing about Ruby, is, like, the more Ruby you load up, the more memory it takes. So, I would guess you would see, like, a memory overhead reduction, but the biggest help, I think, where people notice it the most is, like, where the exporters were somehow blocking or getting in the way of the application code performance, right?
install OpenTelemetry, and then you're seeing You know, your latency go up.
Significantly, or your latency variants start to go up significantly, because some of…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 37:18 I really see that, I can see that in, And if you're blocking on queuing.
**Ted Young (Raintank, Inc. – Grafana Labs)** 37:26 Yeah, yeah, and I don't…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 37:27 Which, again, is a knob. In Python, it's a prop.
**Ted Young (Raintank, Inc. – Grafana Labs)** 37:31 Right, because they're single-threaded. And Node.js is the same deal. It's asynchronous, but it's… it's… you're still… just only have one thread and coroutines. And Ruby is a little more genuinely multi-threaded, so I don't know, maybe it's not a problem.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 37:47 We have multi-threaded, but I think there are opportunities for contention where if your queue size is for export.
Aren't big enough for your volume of traffic, and you've chosen to.
**Ted Young (Raintank, Inc. – Grafana Labs)** 37:58 Oh, so young.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 37:59 Exactly.
**Ted Young (Raintank, Inc. – Grafana Labs)** 37:59 Blocking on some handoff or something like that.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 38:02 So… so if somebody goes, I shall not lose telemetry, but the queues aren't big enough for their for the throughput that they need, for the volume of telemetry that they're generating, they're gonna have the application process hang, waiting for the span to get queued.
And then you're out of the… the door opens automatically for me, because you've got to go turn it on for queue sizes, or let the drop spans on the floor when it can't queue.
**Ted Young (Raintank, Inc. – Grafana Labs)** 38:30 Yeah.
But that's…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 38:31 It's not a, it's not a single-threaded issue, that's just queues. They rule everything around us.
**Ted Young (Raintank, Inc. – Grafana Labs)** 38:37 Right, right, yeah, but I don't know how much that then turns into application performance issues versus just… Well, you're dropping stuff on the floor, or your… your memory's ballooning.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 38:47 It could… well, it could be in an auto-injection world, in the… in that… hesitate to use the word context. In that situation.
Where you're auto-injecting Ruby, the default configuration for auto-injected Ruby, or anything really, could be, I'm gonna drop stuff on the floor if your queues aren't big enough.
log it. I'll make you aware that you're losing telemetry, but I won't take your app down.
**Ted Young (Raintank, Inc. – Grafana Labs)** 39:13 Yeah, which is the other thing. OpenTelemetry is ironically not as observable.
as it could be, and I don't know the state of that in Ruby, but that's another.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 39:25 How do you observe the observer? There was a… there continues to be a little, clever hack.
an abstract that someone could choose to implement. Could emit metrics or emit logs, it'll say, I had an issue, and you can choose to log it, you could choose to Add a metric,
**Ted Young (Raintank, Inc. – Grafana Labs)** 39:49 Yeah.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 39:50 But it's not… there's not a default.
output for that, it's just this, like, abstract class.
**Ted Young (Raintank, Inc. – Grafana Labs)** 40:00 I don't even think… I don't know how much we have, even in terms of semantic conventions around… what… what we should be outputting. And I do… I have received feedback from people, I don't know about Ruby specifically, but yeah, it can be hard to tell… When you're dropping data, and, like, where it's getting dropped, and why it's getting dropped, like… like…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 40:21 So far, what I've seen people do is they've picked up that abstract class that will… if you give an instance of this thing to the SDK when you configure it.
you get to choose where it goes. So people, like, implement a stats D and send it somewhere, or Prometheus, or just a logger, where… where a metric is going to get incremented and just log it to the console, so it's not… Getting routed anywhere fancy, it's just… A structured event sent to the standard out.
And, last line of defense, right? When everything else is broken, go look at the console.
Yeah, because if you're… if the export of your telemetry is broken, I don't know how you export your telemetry about that being broken.
**Ted Young (Raintank, Inc. – Grafana Labs)** 41:11 I mean, at least… Blog it locally.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 41:14 Log it, is the… yeah, that's…
**Ted Young (Raintank, Inc. – Grafana Labs)** 41:16 Fit app somewhere, but I think we don't even have… conventions around, like, saying we should do this, right? Like, I don't know how much we've even written down in the spec that… Hey, like… We give you… we say there's an option to define queue size, but we don't say, like, emit this somewhere if the queue overflows.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 41:38 Right.
**Ted Young (Raintank, Inc. – Grafana Labs)** 41:39 Huh.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 41:41 And you should probably tell somebody when it's full, type of thing.
**Ted Young (Raintank, Inc. – Grafana Labs)** 41:44 Yeah, people want to know.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 41:47 It doesn't need to be said, but we should probably say it. Yeah.
**Ted Young (Raintank, Inc. – Grafana Labs)** 41:50 Like, it kind of sucks to be like, we're not getting data out of this thing, and it's not telling us why we're not getting data.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 41:59 And the, the, the, the, how do you tell it to tell you that?
midstream. I would like to not have to restart the process to… Tell it to tell me it's having problems.
**Ted Young (Raintank, Inc. – Grafana Labs)** 42:11 Yeah.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 42:12 Tyrons around that.
**Ted Young (Raintank, Inc. – Grafana Labs)** 42:14 infinite piles of work. But, yeah, that's why I wanted to pop over. Okay.
Yeah, maybe we can move some of this to the… to Slack, hit people up there, but I'll try to come back next week as well, to have some of these things.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 42:33 Sweet.
**Ted Young (Raintank, Inc. – Grafana Labs)** 42:34 Oh, man.
Well, I might sign off early then, because we're just chewing the fat.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 42:40 Sure.
Thanks for coming.
**Ted Young (Raintank, Inc. – Grafana Labs)** 42:43 Yeah, man. Good talking to you, Rob.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 42:45 See you.
**Ted Young (Raintank, Inc. – Grafana Labs)** 42:46 Bye.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 42:51 So, Xuan, do you have anything pressing?
**Xuan Cao** 42:54 No. No? Yep.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 42:59 I'm gonna jump back to the spec SIG.
Notes, just to double check.
Oh, yep, I see the bullet point there, language around injectability of SDKs.
Component name… for SDK components.
I don't know what this means.
Well, I don't know that main, so I don't know if it's important. So, looking on… Well, nothing's jumping out at me. So, I guess if it's important, it'll… Come back up.
And, and you don't know… you don't have anything pressing in core contrib, PRs you want reviewed, or… Issues opened.
**Xuan Cao** 44:24 Yeah, I have some PRs, but they're not very urgent to review. I'd like to, Just open all… all the things I have for the metrics, then, I mean… Then people can go one by one.
that I can, like, focus on them.
So, yeah, they're not… they're not urgent.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 44:48 Okay, so maybe bring them up in Slack when you're ready for review, or…
**Xuan Cao** 44:54 Yeah, one thing… one thing I think is more interesting for people to review, Because this, this issue… well, I, I shouldn't call it issue, it is… This one has been for a long time. I think a lot of people are chiming about what they're thinking about this.
For, for spec, I mean, we're not doing.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 45:18 Oh, yeah, unfinishing.
**Xuan Cao** 45:21 I think this is more, well, more interesting to… to review, yeah, this one.
I mean, even though it's written by AI, but I think it still is, will be… Yeah.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 45:41 It's… AI's not an immediate blocker.
**Xuan Cao** 45:44 Yeah.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 45:45 Excellent.
Interesting.
Private synchronized method.
Alright, I got my second screen up, I can… I can share this.
Is this something you want to look at together, or just pointing it out as a, as a thing to review soon?
**Xuan Cao** 46:43 Yeah, I think this is something should be reviewed soon. I guess a lot of people is blocked by this kind of behavior.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 46:50 Okay.
**Xuan Cao** 46:52 Yeah, especially if they wanted to change something before our finish.
They want, they have one… they want to do something unfinishing.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 47:02 Yeah.
unfinished Yeah, okay. I'll put it on my list. If we're not gonna review it, like, synchronously here together, I can… I'll put it on my list of things to review this week.
**Xuan Cao** 47:12 I can… I can put into the… I'll just put it into the notes here.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 47:22 Okay.
**Xuan Cao** 47:23 Yeah, so I think the main… argument before is Aria wanted to use different, spread lock.
To allow reentry.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 47:36 Okay.
**Xuan Cao** 47:37 Yeah, but, I think they want to… do you want to use the fiber?
Which I don't really know, I don't have any, experience with that.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 47:50 Yeah, I haven't used fibers and anger, so…
**Xuan Cao** 47:55 Oh… I guess, I think the decision is to use the fiber, or we… Change the behavior of this mutex.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 48:09 Was there… it looks like this… I'm sorry, you pers… go ahead.
**Xuan Cao** 48:13 Sorry, sorry, I mean, I personally prefer to use this new mute text, I'm not sure.
Okay.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 48:20 My quick read of this is the attempt to fix reentry is the private synchronized method in spam.
Where if the mutex is already owned, it yields And if it's not owned.
It takes the… whatever's being synchronized within a spam, method.
is using a… I'll share my screen.
My very quick read is that this is the attempt at Fixing re-entry within, actions that a span is taking.
Because instead of, mutex Synchronized, and then something else gets called, and Mutex synchronized gets called again.
And we're blocked.
It's, this new private method.
Matt.
If the mutex is already owned, yield.
to allow it. Continue mutating state, because The mutex is already taken.
They're locked.
and then, if it's not, Do the… do the usual.
For whatever block.
**Xuan Cao** 49:49 Excellent, okay.
Yeah, I think, I think this looks…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 49:53 Which as a… which as a code read, I'm like, makes sense, but I've only looked at it for… 2 minutes.
**Xuan Cao** 50:01 Yeah, so anyway, yeah, I think this is, And it is related to trace?
Which is, something, like, weird.
It's stable, so…
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 50:13 What was that?
**Xuan Cao** 50:14 I mean, this is… this isn't a related trace.
Will be more… even more important.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 50:26 The review, yes, unfinishing is a… is a thing that is wanted.
It unlocks all sorts of good stuff.
Oh, there's lots of tests.
But evaluated.
Goodness, but… Good to see.
Okay, it's on the list. I will review this this week.
Anything else?
**Xuan Cao** 50:59 That's everything in my mind.
**Robb Kidd (Hound Technology Inc. dba Honeycomb)** 51:02 Okay.
I guess we can call it early venom.
See you next week.
And in Slack.
**Xuan Cao** 51:09 See you.
