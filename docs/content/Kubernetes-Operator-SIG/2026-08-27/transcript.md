SIG: Kubernetes Operator SIG
Date: 2026-08-27
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Marc Schäfer (T&A SYSTEME)** 02:55 Hi.
**Tyler Helmuth** 03:00 Hello, Mark.
I'm just waiting for the other maintainers to show up.
I think the meeting's still happening today.
**Marc Schäfer (T&A SYSTEME)** 03:06 Okay, sounds good.
**Mikołaj Świątek** 04:34 Sorry for being late.
**Tyler Helmuth** 04:38 Hello.
**Mikołaj Świątek** 04:44 Drink Jacob is on… Are there right now?
**Tyler Helmuth** 04:48 Yeah, he said he wouldn't be at a meeting today.
**Mikołaj Świątek** 04:52 Pavol and I'm gonna… Something of a pity, because I wanted to talk about what you're doing, Tyler.
**Tyler Helmuth** 05:02 I know.
If it needs to push, It's not horrible, but… I'll be out next week.
At a off-site.
So I won't be adding… I won't be doing any coding next week.
**Mikołaj Świątek** 05:16 Wow, you don't call your offsite? What, what is it?
**Tyler Helmuth** 05:19 I don't… No, we just talk a lot, I think.
**Mikołaj Świątek** 05:24 Oh.
Hmm, so… I don't think this blocks what you've written. I think it's fine to merge it, it's just… because we haven't shipped anything, so it's okay.
**Tyler Helmuth** 05:36 Yeah.
**Mikołaj Świątek** 05:37 It's just that… looking at it made me realize that we're changing the behavior of the CRD in, like, a kind of a non-trivial way.
**Tyler Helmuth** 05:48 Whereas… Yes.
**Mikołaj Świątek** 05:49 it used to be the case… and I'm not just talking about the fact that you have to specify the image, I'm talking about the fact that you have to, like, it used to be that you could create the CRD, you would have all the images defaulted.
And then you could attach that to anything that is, to any, like, you could use any of those instrumentations, essentially.
**Tyler Helmuth** 06:09 Correct.
**Mikołaj Świątek** 06:10 annotate a pod, and it would get injected. Whereas right now, if you… you can create a CRD, which only has the Java image set.
And if you instrument a Java pod that way.
It will work, but if you instrument a Python application that way, it will not.
**Tyler Helmuth** 06:30 Correct. And you're saying CRD, but you mean CR, right? Create Custom Resource, like the instance of the object, not the definition.
**Mikołaj Świątek** 06:37 Yes, yeah, sorry, I'm a smoker.
**Tyler Helmuth** 06:40 Yeah, that's true.
So, like, we have… that can happen today. So today, in the Operator Command flags, you could disable Python, for example.
And you could create an instrumentation object, without specifying Python.
And instead of auto-injecting that default image, the operator just won't.
And so, we have the same situation where someone could go to a Python pod and say, annotate, they could do inject true or whatever, and then nothing would happen.
**Mikołaj Świątek** 07:15 Yeah, that's, like, it's probably also a problem that we don't surface that error anywhere in a, like, a discoverable way, I would say. Yeah.
Because what should actually… I think what should actually happen in that case is that there should be… either there should be something in the CR status itself.
About it?
Or there should be something like an additional annotation on that pod.
Telling you, hey, you asked for us to instrument this, but we couldn't.
**Tyler Helmuth** 07:49 Yeah.
**Mikołaj Świątek** 07:49 Do you think we could…
**Tyler Helmuth** 07:50 Can we get away with just a cluster event? Like, could the operator be like, hey, we saw this, and we rejected it because you didn't have a.
**Mikołaj Świątek** 07:57 Yeah, that, I would… I would accept, I would accept that, that as well, that's fine.
And we should probably… we should probably just fix that in the existing one, to be honest, and then that will also fix it in the new one.
By extension.
**Tyler Helmuth** 08:15 The other thing about my PR is that it does this… it nils out the language block, but then if you set the language block, it requires the image, so there's no more emit empty. There's nothing enforcing that yet, I'm pretty sure. Like, that's just struct work. I'm pretty sure… That there's, like.
once we start… like, we have nothing that installs the CR… like, that installs this anywhere yet. We have no tests that test B1 Beta 1, we have… no platform testing, like, nothing, so I'm pretty sure… there is a future, like, actual enforcement that will happen somewhere, like in the reconciliation, but I'm not totally sure yet. I need to look.
**Mikołaj Świątek** 08:58 I mean, no, no, it will happen, it will happen structurally, right? Because the field is required.
The field is required, so it's just going to be part of the CRD definition, the CRD definition.
**Tyler Helmuth** 09:11 I guess I'm wondering…
**Mikołaj Świątek** 09:12 our definition.
**Tyler Helmuth** 09:13 Yeah, yeah, yeah. I guess I'm wondering if the error message will be specific, if it'll be like, hey, you didn't specify an image for Java. You can't… do that. You must specify an image. Or if it'll be, like, a generic, like.
un-martial thing, where it was like, hey, you didn't.
**Mikołaj Świątek** 09:31 No.
**Tyler Helmuth** 09:31 We ain't on March.
**Mikołaj Świątek** 09:32 No, no, this is like an OP… this is like an OpenAPI spec thing.
**Tyler Helmuth** 09:37 Okay, so it's… we're… so we're good. This is… this is how we do this.
**Mikołaj Świątek** 09:41 Yes. Cool This is… you're gonna get, you know, spec java.image… spec.java.image is required.
**Tyler Helmuth** 09:49 Is real life. Okay, cool, cool. I wanted to add… some platform tests, but it seems like maybe we're not ready for that, so it'll be nice when… when those are there.
**Mikołaj Świątek** 10:02 I think… I think what you've… I think what you've done is correct. I actually, like, my brain… switched red with green, I think, reading that PR of yours, and thought that you were changing it in the other direction than you were.
**Tyler Helmuth** 10:16 It seems like Jacob had the same question, so I wonder if… Yeah, I don't know, it… Jacob also said, like, hey, are we nilling… or everything, and I was like, I don't think so. So I don't know if there's, like,
**Mikołaj Świątek** 10:32 No, no, that's what you are doing. The change you are making, right, is you're changing.
**Tyler Helmuth** 10:38 Knilling the language only.
**Mikołaj Świątek** 10:39 Yes, yes, yes. And so we are knilling things, yeah.
**Tyler Helmuth** 10:44 Yes, definitely, but only the language, not the image itself, on the common struct.
**Mikołaj Świątek** 10:49 Yeah, yeah, yeah. Otherwise, if you didn't do that, then we would be forced to… you would be forced to set all the images every time.
**Tyler Helmuth** 10:57 Yeah, which we don't want, yep.
**Mikołaj Świątek** 11:00 Nope.
**Tyler Helmuth** 11:00 Alright, well, I think I'm happy with it.
I'm happy where it is in the current state, then. And when I'm back from Grafana Fest, I'll keep working with Pavol to move instrumentation V1 Beta 1 through the paces.
**Mikołaj Świątek** 11:16 Oh, you're gonna… You're soon gonna run into the ultimate blocker of doom.
for that.
**Tyler Helmuth** 11:25 Yeah, is it the fact that we, like… is it the same problem we had for the collector?
The Collector Beta 1 image? Or, definition?
**Mikołaj Świątek** 11:33 No, no, no, no, no, no. The ultimate blocker of Zoom is the fact that Jacob is going to want to refactor the injection. He's not actually going to do it.
**Tyler Helmuth** 11:44 I'll do it, I guess.
Or maybe… maybe I'll continue to… maybe I'll continue to limp along with this messy code until we get V1 Beta 1 out, since it's an entirely internal… Like, non-user breaking refactor.
**Mikołaj Świątek** 12:01 Yeah, but it's… it's gonna be difficult, because… I… he… Jacob has good reasons to want to… to refer.
**Tyler Helmuth** 12:10 Oh, yeah.
**Mikołaj Świątek** 12:11 Because it's, like, it's really hard to understand.
**Tyler Helmuth** 12:14 It's so hard to understand.
**Mikołaj Świątek** 12:16 But also, you know… You have to actually do it.
**Tyler Helmuth** 12:22 Yeah. Yeah.
Well, I'll look through the RFC again and make sure I'm aware of, like, all the different… things we're trying to do with V1 Beta 1, because I've been really focused on just the… the image at the moment.
But yeah, I'll.
**Mikołaj Świątek** 12:38 I don't think we're doing… we're doing that much, other than wanting to use… Other than wanting to use, what's it called?
The label, a label instead of an annotation.
**Tyler Helmuth** 12:58 The label instead of annotation.
**Mikołaj Świątek** 13:00 Other than that, I'm not sure that we're doing really all that much.
**Tyler Helmuth** 13:08 If we wanted to, in the future, reverse the… the matching strategy, I think Jack came and talked about this in the past, and instead, like, automatically Instrument, like any pod that shows up in the namespace.
I'm pretty sure we could do that as a feature ad, like, as a setting that.
**Mikołaj Świątek** 13:27 We talked about this even explicitly. It can be… it can be added as a feature to…
**Tyler Helmuth** 13:33 Okay, cool.
**Mikołaj Świątek** 13:34 Current one, even, and even…
**Tyler Helmuth** 13:36 Yeah.
**Mikołaj Świątek** 13:36 There's even an issue about this with quite a lot of comments and even some consensus. It's just that, like, the contributor who pushed it stopped pushing it.
**Tyler Helmuth** 13:46 Yeah.
**Mikołaj Świątek** 13:47 And that would take…
**Tyler Helmuth** 13:47 Something?
**Mikołaj Świątek** 13:48 to pick it up.
**Tyler Helmuth** 13:49 I think that's something that I'm interested in, but I'm more interested in instrumentation, or in V1 Beta 1. Like, I don't really see a lot of value in throwing features onto Alpha right now, when we're trying to do beta, so…
**Mikołaj Świątek** 14:01 Yeah, it's like… So basically, it looks like the solution, and also Jack Berg wanted to do that, if I recall correctly. So, maybe it's worth… start talking about how it worked, because I recall that the contributor who originally did it wanted to do selectors, which I liked, because those are, like, a idiomatic mechanism in Kubernetes, whereas Jack.
**Tyler Helmuth** 14:23 Like, you put a selector in… you put a selector on the instrumentation.
**Mikołaj Świątek** 14:26 Yeah.
**Tyler Helmuth** 14:27 Yeah, yeah, yeah.
**Mikołaj Świątek** 14:28 Yes, what Jack wanted to do is something more elaborate, with, like, a full-on rule system, where you define a set of matching rules, and those change what gets matched and what doesn't get matched, and so on, and you can, like, select on all sorts of things that the selectors by themselves don't necessarily let you do it.
**Tyler Helmuth** 14:48 Even that feels like… a non-breaking change. Like, even if we started.
**Mikołaj Świątek** 14:52 It's not a braking trade. It's not a braking trade.
**Tyler Helmuth** 14:55 more, yeah.
**Mikołaj Świątek** 14:56 Yeah, it's not a breaking change, and you can even add it, start adding it, kind of, by…
**Tyler Helmuth** 15:00 Yeah.
**Mikołaj Świątek** 15:01 piecemeal, and then if you wanted a behavior of ma… instrument everything everywhere, then that's, like, there should be just, like, a question of adding a… the right matching rule.
Right? Or the right selector, and that's it.
Oh, it should be.
Should be reasonably, reasonably okay. There's only one, like.
There's only one caveat to this.
And that actually requires adding, perhaps, a completely new instrumentation image and path.
It's the… package everything into a single image, and just decide at runtime what we're instrumenting. Because instrument everything, to instrument everything, you still have to tell the operator what instrumentation you want.
**Tyler Helmuth** 15:50 Yeah, which one? So you still… you still have to… there has to be some sort of discovery where it's like, I know that this… Pod is running.
Python, and therefore I need to select the Python thing. Yeah, there's something to think about there.
**Mikołaj Świątek** 16:04 But this is, like, this is a solved problem in the sense that Dash Zero does it, and a lot of what they did to achieve this is already encoded into the injector.
After the vibrate.
**Tyler Helmuth** 16:16 Do it with, OB-2, with Bela.
**Mikołaj Świątek** 16:20 Yeah, but that's, like, a completely different path, like, the OB is, like, you know, a completely different mechanism and different data, whereas The dash zero mechanism is the same instrumentation package doing the same thing, it's just that you have an image which contains all of your supported instrumentations at the same time, and you just pick at runtime.
And you have to… and you have to have that image, or I guess you could mount all the images.
**Tyler Helmuth** 16:49 all of them, you could just mount all of them, yeah.
The only one that's gonna work.
**Mikołaj Świątek** 16:53 I like that idea that much, but essentially, you have to have the binary that you want ready, already mounted at the time that you run the injector to figure out what you're instrumenting, right?
Yeah. So… so that requires… that… that part requires, perhaps, a new instrumentation type, from my perspective. Or maybe it's… it requires a switch on existing instrumentation types. This is… this is not… not, spec'd out. Like, it's not… Yeah, we have to think…
**Tyler Helmuth** 17:26 Think about that before we started working on it, yeah?
Maybe we can get someone from Dash Zero to come… Contribute to this, because they've got, they've got people in the hotel.
I'm sure that…
**Mikołaj Świątek** 17:37 Michelle is already… Michelle is already contributing, like, or… but he will… he will just tell you to do the exact same thing Dash Zero does, and I am, yeah, I like Dash Zero as a company, but I… I don't trust their engineering quite that much.
To just uncritically accept what they've…
**Tyler Helmuth** 17:56 Yeah.
**Mikołaj Świątek** 17:57 in there.
**Tyler Helmuth** 17:59 Well, it's good that there's an issue so that… once… when I'm ready, I guess I could take a peek at it and start investigating.
**Mikołaj Świątek** 18:08 Yeah, it's called something like Instrumentation Support Selector, or something?
**Tyler Helmuth** 18:12 Okay.
**Mikołaj Świątek** 18:13 I don't sure what…
**Tyler Helmuth** 18:14 And opt out, too, like… we might want to have, like, a way for a pod to be like, hey, I know that you're supposed to be matching everything, but I have chosen not to be matched. That could be an interesting label.
I don't know.
**Mikołaj Świątek** 18:27 Oh, maybe, maybe, like, Prometheus doesn't have that, I think.
**Tyler Helmuth** 18:32 Okay.
**Mikołaj Świątek** 18:33 If you're not, if you're…
**Tyler Helmuth** 18:34 on Prometheus, like, at all.
**Mikołaj Świątek** 18:36 I mean, Prometheus… in Prometheus, you can have, like, a selector which tells you from which pods you're taking scrape targets in a service monitor or in a pod monitor, and those pods don't get to opt out.
**Tyler Helmuth** 18:48 Yeah, they don't get the But also, their opt-out.
**Mikołaj Świątek** 18:50 Yeah.
**Tyler Helmuth** 18:51 The opt-out is just not serving up metrics.
Right? So they can opt out in the sense that they could just not serve metrics. In the… in the push instrumentation world.
You can't… If you exist, you get it, and so maybe there's some situations where you don't want that, I don't know. Again, that would be another.
**Mikołaj Świątek** 19:10 Maybe, maybe, maybe it's enough. I'm okay with that. I would also be okay if there was, like, an environment variable you can set to say, I don't want anything.
That works as well.
That's equivalent to not serving the Prometheus metrics, essentially.
**Tyler Helmuth** 19:28 Yeah.
Because there's probably going to be times where it's like, well, I've already instrumented my pod, but it needs to run in this namespace, so, like, don't try to inject anything, because I've already got it. That feels like a real-life situation.
Yeah. But anyways, that's later work.
**Mikołaj Świątek** 19:45 I mean, you can, you can always, you can always come up with your own, too, right? You can come up with your own label, saying these are all…
**Tyler Helmuth** 19:52 Yeah, and then just not to select that, yeah. It could be handled by the selectors, yeah.
**Mikołaj Świątek** 19:58 Because if you hard-code that into the operator, you're gonna… You kind of get into the…
**Tyler Helmuth** 20:07 Yeah.
**Mikołaj Świątek** 20:09 Can it be disabled exactly, right? Like, how optional is it?
**Tyler Helmuth** 20:13 Plus, then you're adding a feature that you have to support, and if there's a story where it's like, well, just choose a selecting schema such that you can add a pod to the namespace that doesn't get selected, that feels like probably a reasonable answer.
**Marc Schäfer (T&A SYSTEME)** 20:30 just… just to add regarding Prometheus, if you… if your pod doesn't serve the metrics, but it's still selected through the label, then you're getting error messages, so it's still.
**Tyler Helmuth** 20:41 Oh, really? Yeah. Oh, interesting.
**Marc Schäfer (T&A SYSTEME)** 20:43 You'll see that in the… you'll see that in Prometheos.
**Mikołaj Świątek** 20:47 What if there is no part?
open. Do you still get errors?
**Marc Schäfer (T&A SYSTEME)** 20:53 Yeah, that you can't scrape it. You get… there's a general, so if you lose the, for example, the CubeStack Prometheus Helm chart.
Which comes with Alert Manager, so for alerting Prometheless, part.
there are basic, rules inside, like, like, hey, I can't scrape my target. That's one of the basic rules that comes with it, that almost every environment has, because it does make sense that you get an alert if scraping doesn't work, but that means that if You have, like, Selector of a service monitor.
And there are too many servers that match this label selector, and… many or some of them don't provide those metric ports, or can't be scraped. You get… you get in the UI of Prometheus, you get the error shown. So, you need to… maybe, for example, that's what we sometimes do, is we add multiple labels, like 2, 3, 4 labels, and then it's matching based on them.
Not one single, multiple labels at the same time, yeah.
**Mikołaj Świątek** 22:00 I think that might also depend on what What's it called?
Because by default, I think still Prometheus Operator doesn't use endpoint slices.
And whether you… but it does use endpoints, then. Correct. And if you appear in an endpoint as a pod, depends on whether you have No, no, it doesn't, right? It just depends on the service spec.
**Marc Schäfer (T&A SYSTEME)** 22:32 Correct. Just on the server spec, yeah. On the labels on the server spec, yeah.
based on that, it's discovered. And also, also you need to add, like, if you have multiple Promethos instances in the same cluster, that is managed either by separate Promethos operators, which, for example, I know a case at work, or one operator managing multiple Promethos instances, regardless, you have separate labels, for those Promethois instances.
custom resource, Promethos instance 1, custom resource, Prometheus Instance 2, and if you have, then, different services for those, like 5 services for Prometheus 1 and 5 other services for 2, then you also need to include the Promethos Server that you want to, because otherwise the operator is not able to discover, the service monitors.
**Mikołaj Świątek** 23:29 No.
**Marc Schäfer (T&A SYSTEME)** 23:30 It only discovers the certain service monitors that have the same label as set for the server, because he knows that, this label belongs to my Pubetha instance, I'm only allowed to, Look up those.
And work with those.
**Mikołaj Świątek** 23:48 Yeah, but if you're brave enough to run multiple instances of Prometheus Operator in the cluster, then you're brave enough to add some more labels, I guess.
**Marc Schäfer (T&A SYSTEME)** 23:57 Yeah, definitely. Definitely.
And that's different scale of Kubernetes cluster, then you're not talking about small, cluster.
**Mikołaj Świątek** 24:10 Hey, hey, Pavol?
**Pavol Loffay (Red Hat LLC)** 24:16 Hi guys, sorry for being late.
**Mikołaj Świątek** 24:18 No problem, we were waiting patiently. Oh, by the way, Mark, if you have a topic that you'd like to discuss, I'm sorry, but me and Tyler got into this discussion about something. If you have a topic that you'd like to discuss, this is, like, a, you know.
this is going to be a good time. There's not that much of us, but we have, like, enough deciding power between us to help you out.
**Marc Schäfer (T&A SYSTEME)** 24:45 Not at the moment. I just started. I started in January on some Go and Android OpenTelemetry projects, and last week I started on the Helm chart, and also wanted to contribute to the operator.
as I do many operator work on other non-CNCF-related open source projects, and also at work, so… Yeah.
**Mikołaj Świątek** 25:08 We have some issues tagged Help Wanted, if you'd like to help out, or you can just look at what was filed most recently, and if it seems straightforward, and there's a, you know, some kind of indication from a maintainer or approver that, yeah, we want to do it, then…
**Marc Schäfer (T&A SYSTEME)** 25:28 Sounds great.
**Mikołaj Świątek** 25:28 Feel free to ask to… for it to be assigned to you, and… Far away.
Cool.
Pavol, we talked a little bit with Tyler. I don't know if you've seen Tyler's PR about making the instrumentation images required.
No, it has…
**Pavol Loffay (Red Hat LLC)** 25:51 seen that.
**Mikołaj Świątek** 25:53 it has one consequence that I, at least, was not, like, I didn't know that this would be the case, but now it seems obvious. I don't think it was in your RFC as well, either, sorry. It was, it's the fact that if you make images required.
Right? Then you are forced to make the actual per-language sections optional, because if you don't, then you're going to require all the images every time.
Right?
Right? You have to make the Java section optional, if you want the Java image to be required, because if not, then if you just want to use Python, you'll be forced to set Java if the section is not optional, yeah?
**Pavol Loffay (Red Hat LLC)** 26:44 Because there is no way to figure out if it's… Provided, if it's omitted.
on purpose, or… like, why? I don't understand why.
**Mikołaj Świątek** 26:59 No, it's just a question of, It's just, like, required validation logic, essentially.
I'm pretty sure. Like, if your whole section is not marked as optional, then anything that's required in it just causes the whole thing to be required.
It's like, you have to have optional somewhere in the train along the way for it to, like, be optional, because we don't want these images to be unconditionally optional, right? We want only conditionally required. We want only them to be required only if you're actually, you know, using Java.
That's kind of, like, the idea of it.
Although that kind of causes a different problem, right? Maybe we have to have an explicit switch to enable instrumentations.
Because otherwise, you can create an instrumentation which doesn't have anything set, and it will do nothing.
I don't think we want that.
**Tyler Helmuth** 28:04 You could define… you're saying you could define the Java block, set an image… And no.
**Mikołaj Świątek** 28:10 No, no, no, I'm saying that you define absolutely nothing.
**Tyler Helmuth** 28:13 Oh.
**Mikołaj Świątek** 28:14 instrumentation with nothing.
**Tyler Helmuth** 28:15 Yeah, that's We can handle that with validations, though. We can… it's surely in the validations of the… of the CR, we can check Is at least one language block defined.
**Mikołaj Świątek** 28:30 We have…
**Pavol Loffay (Red Hat LLC)** 28:31 I think the bigger issue is, like, you define a Java agent image, and then you use the Python inject annotation.
And… the validation will go through, it's a valid CR, but the injection will fail.
**Tyler Helmuth** 28:46 So that's what Mikolaj was talking about, and we actually have this problem today. So today, because we have the feature flag… not feature flags, the command line args that can enable and disable instrumentation, you could disable Python instrumentation.
Create your CR in Alpha 1 that doesn't define any images.
The Operator will go through and default all the images for all the other languages, but will skip Python, because it's disabled.
then you'll have a CR, it'll be… it'll exist, it's in the cluster, you go to your Python pod, and you annotate it and say, give me instrumentation, and it just won't work. So that problem actually does exist today, also.
So we were talking about adding Maybe, like, a cluster event, or some sort of… Warning. That is like, hey, we noticed that you added a valid annotation to your pod.
this… your CR does not… Like, allow that particular language to be instrumented.
It didn't work.
It didn't work as planned, I guess.
**Mikołaj Świątek** 29:59 Yeah, because we don't really have any way of telling what the intent of the user is when they update or create the instrumentations here, right? We only have… know what they're trying to do after they try to inject something using the mutating webhook.
**Pavol Loffay (Red Hat LLC)** 30:14 We need to make it visible that it failed, and yeah, even maybe, like, on the status, on the instrumentation as well, like.
signal that, hey, there's a user that tries to inject Java, but you actually don't have Java, so…
**Tyler Helmuth** 30:30 Yeah.
**Mikołaj Świątek** 30:32 Yeah, but we have to be careful, because that can be, like, a lot of signals, potentially, so we have to be careful about aggregating them. Like, we can't just put stick, like, every single pod where it failed in the status, because there can be, like, thousands of those, right?
So it has to be something more… Like, maybe a number and an example, but also… like, it has to be a counter, so maybe we should have a metric that measures this. We already wanted to have a metric that measures this, like, the train… the PR adding it stalled.
And then just the value of that metric can be in the status, too.
Towing you, hey, this is non-zero.
But yeah, this is, like, a something that I don't think we discussed.
Do you agree?
**Pavol Loffay (Red Hat LLC)** 31:28 Absolutely.
**Mikołaj Świątek** 31:28 We have to deal with.
**Pavol Loffay (Red Hat LLC)** 31:30 I was… I thought that metric is overhead, like, what would be the… what would be enough to just signal that there was a Java failed injection, or Python failed injection.
But since you mentioned metric, I think we could as well then have metrics for the successful injections, and signal that as well. Like, hey, I injected 20 Python.
**Mikołaj Świątek** 31:55 Yeah.
**Pavol Loffay (Red Hat LLC)** 31:56 8 containers, or 20 char… I think that's useful for users as well, to kind of…
**Mikołaj Świątek** 32:00 Yeah, yeah, and we even have… the decision to add those already exists, it's just that when you try to add metrics, it starts being like, what should the name be? What should the unit be, right? What should the attributes be? Because whenever you want to change any of these things, you're essentially… you're not exactly making a breaking change when you add a an attribute, but if you can add an attribute that leads to, like, a, what's it called? What's the right? To a partitioning of the… of the… of the set of time series, right, to… that effectively creates more time series. It's kind of a breaking change-ish.
If your users wrote their, like, queries the wrong way.
**Tyler Helmuth** 32:46 Yeah.
**Mikołaj Świątek** 32:47 So it's like, adding new metrics is one of the most, most, difficult things to add to the project, right? Because it's like a public API surface that doesn't really have great ways of managing breaking changes.
**Tyler Helmuth** 33:04 Yeah, it's like this… it's like all the semantic problems, like when we change the auto-instementation name, it's like… How do you help users realize that we just changed the way you would interact with your data? Like, we just broke all of your alerts, sorry.
It's tough.
**Mikołaj Świątek** 33:19 No, whoopsie, whoopsie.
**Tyler Helmuth** 33:21 The Collector SIG has a pretty in-depth… Feature flag process that we're using for changing components to get to… Stable semantic conventions, we could maybe look into that if we needed it for us.
**Pavol Loffay (Red Hat LLC)** 33:40 Yeah, I have more questions about Tyler's PR.
**Mikołaj Świątek** 33:45 He's here.
**Pavol Loffay (Red Hat LLC)** 33:47 Yeah, exactly. So, are you… do intense then to, as well, like, clean up the… the other… Code related to the default images.
like, let's say the… I think the versions that takes the… could be cleaned up, and… That's one part, and then we talked about, as well.
Kind of improving the docs and the examples, so we.
**Tyler Helmuth** 34:18 Yay.
**Pavol Loffay (Red Hat LLC)** 34:19 those images.
**Tyler Helmuth** 34:20 So I want to take care of all of that. I want to be… I can definitely be responsible for all those changes.
Do you want me to do that as part of this PR, or, like, incrementally? Is it okay to do it incrementally?
**Pavol Loffay (Red Hat LLC)** 34:32 As you prefer, like, what is the easiest for you to…
**Tyler Helmuth** 34:36 I think it's… for me, it's easier to take it in small chunks, so I do it incrementally, since none of this is released yet. I'm also… it's not clear to me… So, like, this change, I'm making it to essentially just some Ghost trucks.
But since we don't do anything with the instrumentation V1, there's instrumentation V1, Beta 1, CR, like, there's no platform test for it or anything, like… This is just kind of essentially a struct change.
Where… And there's nothing in the Operator yet that uses… like, the operator has no idea how to reconcile this In this type yet, right?
Has that all…
**Pavol Loffay (Red Hat LLC)** 35:16 Yes, and even the.
**Tyler Helmuth** 35:17 been added.
**Pavol Loffay (Red Hat LLC)** 35:18 it doesn't reconcile any of the instrumentation objects. There is just the.
**Tyler Helmuth** 35:23 Tile is the wrong word, then.
**Pavol Loffay (Red Hat LLC)** 35:26 It just uses the webhook?
**Tyler Helmuth** 35:29 Yeah.
**Pavol Loffay (Red Hat LLC)** 35:29 Queries the instrumentation, and then there is the defaulting and validating the book.
**Tyler Helmuth** 35:34 Yeah, the… reconcile is the wrong word. The… because it's doing a… it's doing a mutating webhook, right?
**Pavol Loffay (Red Hat LLC)** 35:41 Yep.
**Tyler Helmuth** 35:41 Okay.
**Pavol Loffay (Red Hat LLC)** 35:42 I think the book.
**Tyler Helmuth** 35:44 Is this… is the V1 Beta 1 instrumentation hooked up to that at all inside our… Yeah, okay.
**Pavol Loffay (Red Hat LLC)** 35:51 Nordo.
**Tyler Helmuth** 35:51 So I was… I was imagining, once we start hooking that up.
like, this is just, like, the very beginning of these changes. I think once we start hooking it up, there's going to be additional changes that Are required in order to make Image a required field on a… Honestly, like you said, there's, like, code to clean up, there's… We have to figure out what we want to do with those… with those operator gates, and how those interact with this, theirs, all the docks and stuff, so… I think there's a lot still.
**Pavol Loffay (Red Hat LLC)** 36:22 I'm sorry, I… yeah, I thought that you want to do it as well for V1 Alpha 1, but I see the changes are in V1 Beta 1, so…
**Tyler Helmuth** 36:29 Yes, V1, Beta-1. This would be definitely a breaking change.
Right, this is a super breaking change, so it's… I scoped it just to be one beta-1.
**Pavol Loffay (Red Hat LLC)** 36:40 Okay, so let me think about it, how we'd actually… How the conversion will work from…
**Tyler Helmuth** 36:48 So we have a… there's a nice thing that's happening right now for the conversion.
Which is that… if you create a V1 Alpha-1 instrumentation CR right now.
And let's say you specified a Java image, but you didn't specify an image for any other language.
When that is created, the operator says, oh, I noticed you didn't specify an image.
Fored.
Here, let me give you one. And it takes that default image, and it, like, puts it into the object.
So when we… when that object then goes through the conversion webhook, it turns out that all the… all the images are set in the… in the object when it comes through the conversion webhook. That's my claim, at least, based on how I interpret the code.
So when we do the conversion from an alpha to a beta, we actually have every image set.
So we can take all those images and set them on the B1, Beta-1 instrumentation, and it will… it meets the requirement of Setting an image, because it turns out that the alpha 1 had an image set by the operator.
**Pavol Loffay (Red Hat LLC)** 38:04 Okay, and once we ship Operator that will support V1 Beta 1 as a storage version of to CRD, Then, the defaulting webhook, which sets the images right now.
We'll switch as well to V1 Beta 1.
And that's when you want to remove the defaulting.
of the…
**Tyler Helmuth** 38:31 Yeah, so my intention would be… When that… when that default is switched, Any new instrumentation.
like, if you create a brand new V1, Beta 1, CR, instrumentation CR, When it goes through the webhook, if it… is it the webhook, or is it just when you create it?
I don't know the right words. Yeah, I don't know the right word… Kubernetes words for this, but, like, you have… if you specify a language block, if you specify Java, you'll have to say the image.
But any existing Alpha 1, Beta 1, instrumentations that are… already exist on the cluster, they go through the conversion, right? And they get upgraded, and they get all of their images set automatically, which is technically how they exist today.
The operator is just the one setting them.
**Pavol Loffay (Red Hat LLC)** 39:21 Yeah, that's gonna… just one thing, it's… like, once we release this version of the Operator that will change the V1 beta one to storage version, and we'll use the defaulting on the V1 Beta one.
then if you create V1 Alpha 1, it will not get any default images, right? Because the defaulting will work only on V1 Beta 1.
But, yeah, the object… The cluster will have the images.
**Tyler Helmuth** 39:52 Yeah, that's true. If you… if you tried to create a V1 Beta 1, Hmm.
**Pavol Loffay (Red Hat LLC)** 40:01 So, so that version of the operator will simply… Switch off defaulting for both versions.
**Tyler Helmuth** 40:07 I guess… Didn't…
**Pavol Loffay (Red Hat LLC)** 40:09 Right.
**Tyler Helmuth** 40:09 Is that okay?
I don't know if that's okay… That feels like a break and change that V1 Alpha 1.
I don't have… I don't have a good answer for that right now. I feel like I want to explore… I want to explore that a bit more, but it's hard to do right now because There's no, like, plumbing hooked up.
So I don't have a good answer for that yet. This feels like a solvable problem.
like, it feels like the operator… can the operator not tell that it's making a V1 alpha 1 versus a V1 beta 1?
**Pavol Loffay (Red Hat LLC)** 40:52 I don't think so.
**Tyler Helmuth** 40:54 God, that's so annoying.
What's the point of versioning?
I don't have an answer for that yet. I'll have to explore that. I think I'll have to try to test that locally. Like, I'll have to go into the operator.
switch the plumbing around so that it's actually supporting B1, Beta 1, and C.
see what the impact is, and see what I could do.
because I want… I… convert… this is such a hard… This makes me not even want to have the conversion webhook. It's the same problem from the… from the… collector V1 Beta 1, where it's just like, I want to do, like, a straight-up breaking change, and it's just V1 Beta 1 now, but I know that we can't really do that. So, I'll just have to look into how to solve that. Hopefully there's a good solution.
**Pavol Loffay (Red Hat LLC)** 41:49 The issue is not with the conversion, but the issue is with the defaulting.
**Tyler Helmuth** 41:53 Yeah, with the defaulting, mutating webhook. Sure.
**Pavol Loffay (Red Hat LLC)** 41:57 Yeah.
**Tyler Helmuth** 41:57 So…
**Pavol Loffay (Red Hat LLC)** 41:57 double-check that defaulting is not perversion. I think it's just for the… Objects, and the version of the object you get is the storage version.
**Tyler Helmuth** 42:11 Hmm.
There's a good chance… Thursday. There's a good chance that I won't be able to focus on this particular problem much more this week, but once I get back from the company off-site.
So, like, starting in September, I'll be able to dig in deeper to… Into this.
Headache.
**Pavol Loffay (Red Hat LLC)** 42:31 I'm… I'm running way behind of the Leon, beta on… work I wanted to do.
But I will… I will get to it, and I… my highest priority right now is to fix the network policies.
I didn't have time to… to start working on it, but yeah, it's on my list as well. I'm… officially on… maternity leave next week, just for one week. But I will probably get to it and, And Lucy.
**Mikołaj Świątek** 43:04 Do you want to meet some…
**Pavol Loffay (Red Hat LLC)** 43:05 any…
**Mikołaj Świątek** 43:05 Do you want me to.
**Pavol Loffay (Red Hat LLC)** 43:06 If she…
**Mikołaj Świątek** 43:06 That's instead.
**Pavol Loffay (Red Hat LLC)** 43:07 If you want, you can go ahead, but…
**Mikołaj Świątek** 43:09 I don't want, but I can.
**Pavol Loffay (Red Hat LLC)** 43:13 I can… I can promise… I… well, I don't want to promise. I can try to look at it by Tuesday, and if I don't book.
by Tuesday, would you be fun taking a look?
**Mikołaj Świątek** 43:30 Yeah, that's fine with me. I'm actually on vacation from Tuesday as well, but I'll have a… I'll have my laptop with me.
**Marc Schäfer (T&A SYSTEME)** 43:37 If you want, I can also help.
**Mikołaj Świątek** 43:40 I don't… that's like… That's kind of a foreign issue. I don't know if you want to volunteer for it.
It's, it has to do with, like, feature flags and what environment variables they require.
**Marc Schäfer (T&A SYSTEME)** 43:54 I didn't understand, that's all, yeah.
**Mikołaj Świątek** 43:56 Okay.
**Marc Schäfer (T&A SYSTEME)** 43:57 I did follow.
**Mikołaj Świątek** 43:59 Alright, no, it's fine. Oh, either Pavol will do it. Pavol introduced this, and he broke it, so now he gets to fix it.
**Marc Schäfer (T&A SYSTEME)** 44:07 I knew…
**Pavol Loffay (Red Hat LLC)** 44:08 Need to look at that, yes.
**Mikołaj Świątek** 44:12 I actually have a question while we're here. Tyler.
Can you remind me what we ended up doing about, like, the changelogs for the instrumentation images? Are we gonna have them, or is it just gonna be, like, published, and it's in…
**Tyler Helmuth** 44:28 Yeah.
**Mikołaj Świątek** 44:29 in the listing.
**Tyler Helmuth** 44:31 So, right now… The current implementation is… We've got the revision, we've got all of the… Scripting to keep our… our examples up to date.
And someone else had already added Automatic publishing on any change to one of those folders.
**Mikołaj Świątek** 44:52 That was…
**Tyler Helmuth** 44:52 So right now…
**Mikołaj Świątek** 44:53 Okay, cool.
**Tyler Helmuth** 44:54 Cool. Yeah, so right now, anytime, like, we bump a busy box or whatever, we are releasing an image.
All of those image bumps end up through the automation in the Operator release, but yeah, we don't have an individual changelog yet for, each auto-instrumentation image. We… that's still discussed in the… In the issue we're working through. Like, we want to go update the… essentially, like, the GitHub package homepage for each one of those images to describe what they are, same with the Docker Hub one. I think we had landed at not wanting to make A release for every single image last time we talked, because it's quite noisy.
But if you'd like, that's not hard to… it's not hard to make an actual GitHub release for it, we could do that.
**Mikołaj Świątek** 45:42 I don't know, like, I kind of want to… I like to have some record of these releases actually happening.
**Tyler Helmuth** 45:52 More so than just, like, the tags. A record that's more than the tag.
**Mikołaj Świątek** 45:58 Maybe it's enough for them to just be in GHCR.
slash Docker Hub.
I'm not sure. Like, I would like to… I don't know, like, I would like to be able to… for the user to know what it means that he's, you know, has Node.js 093.0-3. Like, what's the difference between 2 and 3?
**Tyler Helmuth** 46:23 How would you feel about, like, a changelog file in each one of the folders, where it's like… Because that would prevent us from having to… busy.
**Mikołaj Świątek** 46:32 That's a good start.
**Tyler Helmuth** 46:33 page, but then there would be, like, a list of, hey, we went from this version of Java to this version of Java, here's a link to the Java release notes, this is what you're getting, something like that.
**Mikołaj Świątek** 46:43 You know, I think having a changelog per instrumentation just as a file in there would be, like, a very nice start for this.
And later, we can decide whether we want to do something like, you know, do an operator release. In the Operator release, there's already… the versions are pinned. We can also append a section in there later saying, this is what changed in the instrumentation images specifically, right? So that's maybe, like, Informat is enough without forcing us to publish literally everything as a release.
**Tyler Helmuth** 47:16 Yeah.
**Mikołaj Świątek** 47:16 top.
**Tyler Helmuth** 47:17 Yeah, because, like, the Helm chart releases, they're the way they are because they have to be that way. But it is kind of annoying to, like, look at the list and be like, oh, well, I just want to see the collector ones, because, like, GitHub's filtering is not good. If you put… if you put OpenTelemetry Collector in that list, it'll show you every OpenTelemetry one, and then anyone that came, like, before or after it. It's really annoying.
**Mikołaj Świątek** 47:37 I think GitHub recently did some feature that lets you filter releases, actually.
**Tyler Helmuth** 47:42 Oh, really?
**Mikołaj Świątek** 47:43 I recall seeing something like that.
Yeah.
**Tyler Helmuth** 47:47 I've always ever had to search by name.
**Mikołaj Świątek** 47:50 Look, at least there's, like, a little list to the side that lets.
**Tyler Helmuth** 47:54 There's a little.
**Mikołaj Świątek** 47:54 sort of a.
**Tyler Helmuth** 47:55 side. It looks like this on my screen.
it looks like this. It's very… It is… is a little useful.
**Mikołaj Świątek** 48:06 It's a little bit better.
**Tyler Helmuth** 48:08 Yeah.
**Mikołaj Świątek** 48:08 They're doing something. Maybe eventually they'll do something that will solve this problem properly.
**Tyler Helmuth** 48:13 I still can't… I still can't filter GitHub notifications by… Closed.
like.
you get a GitHub when, like, a PR… a GitHub notification when a PR is closed, right? I still can't filter all my notifications by things that are closed, so I can quickly mark.
**Mikołaj Świątek** 48:28 Let me give you, let me give you an incredible life hack for the new AI era we are in.
**Tyler Helmuth** 48:34 Yeah, spot to it.
**Mikołaj Świątek** 48:36 It's quite cheap. It's quite cheap to tell your LLM of choice to write you a little tool in Go, probably Go is easiest, because it's, like, a single binary, which will give you, like, a terminal UI that works exactly like you want for.
**Tyler Helmuth** 48:52 I'm looking at I should do this.
**Mikołaj Świątek** 48:55 I don'.
**Tyler Helmuth** 48:56 I know a lot of people are switching to.
**Mikołaj Świątek** 48:57 Surprisingly, I'm surprisingly more productive with my personal… with my personal stupid application that does this. Yeah. While we're here, I also wanted to discuss one more thing. I'm just gonna link the issue, I don't want to share my screen.
There's an issue opened by, apparently, an engineer from Datadog who wants to use the operator, but they have… Instrumentation images that require customization, and the customization they require, they want, is to be able to change the, init container command and arguments.
And that is easy for us to support, but also this is, like, kind of a nuclear option, in a way. This is an option that when you set this, you're kind of taking fates completely in your own hands, because there's no… Like, you… we might make some change in the operator, in the code that does this, and your stuff will just break.
And you will not know until you actually try, right? Because… and considering that we want to use the injector, and that we also don't want to use init containers, we want to use image volumes.
instead of having to run the stupid copy command, I wonder if it's, like, a good idea to actually allow this, and not just force them to say more specifically what they need, and try to support that in some way.
That's what I'm wondering.
Like, do we want to open this?
box, or two users.
As opposed to, like, defining some standard that has to be adhered to by these… by custom images, and just saying, here's what you have to do.
You know?
**Pavol Loffay (Red Hat LLC)** 50:50 I would rather define the standard.
How the images should be built, and what we expect.
**Mikołaj Świątek** 50:57 Yes, but also defining the standards is going to be a lot of work, whereas adding the ability to customize these would be really easy and simple.
like, defining the standard realistically is going to depend on the injector work, right? Because we want the standards to be related to the injector, and there's even, like, these things Michelle is saying where they just want to solve this in the OpenTelemetry packaging.
Project?
Where they want to have, like, a container image for injection specified.
Defined in some way, and then we would just… consume that, right? So maybe they will just define this standard for us.
And we'll just adapt to use it. I would also be happy with that. But that also means that it's not… you know, it's not gonna happen very quickly, probably, which means that the, you know, what I'm good, the reply to this, to this, The author of this issue is going to be, sorry, we're not going to do it because we're waiting on this thing that we don't know when it's gonna happen, and it's not even properly defined yet.
Which is, like, another great answer.
And there's also the fact that we, again, we don't want to… we want to use image volumes.
So, in the future, this init container field will not just actually just do nothing.
on, like, sufficiently recent versions of Kubernetes, because there won't be an init container.
**Pavol Loffay (Red Hat LLC)** 53:04 I would be curious what he actually needs to set in the command and arcs.
**Mikołaj Świątek** 53:12 Yeah, so maybe, maybe we should… maybe I'm gonna ask for… I'm just gonna ask for more detail.
About this, so we can decide whether, like, what it is that they're actually trying to customize, and, like, do they need Do they actually need to run the program in there? Right?
Of some sort, that they… a custom program that they've written.
Because that's the case, then… maybe even in the image volume world, there's gonna be an option to define an init container for your instrumentation. I would rather not do that.
To be honest. I'd rather not give anyone the option to do that.
That kind of depends.
All right, oh, that's how I'll reply, and we'll… we'll see. But I… I get the… I get the sense that you're… that you and me, Pavola are kind of aligned.
On this, in that we would rather just define the standard and then tell them, you follow the standard and it works, even if you don't, then it doesn't.
Okay, cool. Do we have anything else?
Is that correct?
**Marc Schäfer (T&A SYSTEME)** 54:28 I have one general question. Do we have any meeting notes?
Or is there no Google Docs? As in the meeting.
Invite, there's no link to Google Docs.
I know from most… Yep.
**Tyler Helmuth** 54:44 I see in my invite a link to the doc, to the notes.
I can post them here for you.
**Marc Schäfer (T&A SYSTEME)** 54:52 Could this one?
**Mikołaj Świątek** 54:54 It is in the… it is in the… in the calendar.
**Marc Schäfer (T&A SYSTEME)** 55:00 Interesting, I see one for the Go Sick.
This is the next call in a few minutes, but I can't see one in the Kubernetes Operator SIG.
**Tyler Helmuth** 55:09 I wonder… are you looking at the general…
**Marc Schäfer (T&A SYSTEME)** 55:12 Oh, I'm looking inside, inside, inside, inside Zoom, the calendar.
**Mikołaj Świątek** 55:18 In Zoom, I don't know, but on Google, in Google Calendar.
**Marc Schäfer (T&A SYSTEME)** 55:23 It's the same on Google. It's the same on Google.
**Tyler Helmuth** 55:26 Hmm. I see it on our… I see it on the general OpenTelemetry calendar I'm subscribed to.
They did make a lot of changes recently with the… the new Zoom links. Maybe… Try re-adding the calendar, or rejoining the Google group to get the new… to get a new invite.
**Marc Schäfer (T&A SYSTEME)** 55:45 Just as an example, I just sent it, or will send, two pictures.
For comparison.
Well, there they are.
**Mikołaj Świątek** 56:07 As you can see on the floor.
**Marc Schäfer (T&A SYSTEME)** 56:08 This one, there's the meeting notes, and the other ones, even if I scroll down, there are no, so, I was wondering, maybe, maybe due to the transition, they were not added there?
Because I joined through the, Well, those, those are from the LFX portal, or from the Zoom portal itself.
Not from the Google Calendars.
Because there you can see… There you can see how many people are participating in other features.
Which are not available in… the Google one.
Okay.
But thanks for the answer.
**Mikołaj Świątek** 56:51 There isn't that much in here. But…
**Tyler Helmuth** 56:56 We talked a lot and didn't take any notes today. Whoops. I did post something on the… on the instrumentation image issue for the takeaways we discussed, though.
**Mikołaj Świątek** 57:05 That's… that's fine.
I don't, like, all these, all these notes, I think, like… Yeah, it should go into the instrumentation… it should go into the V1 beta one.
Discussion.
I was like… That it should be explicit that we're kind of changing the semantics.
How this is going to work, due to the fact that it's not… With the fact that it is required now to set the images.
Right, anyway, we're… we're at time, so… We should wrap it up, unless either of you has anything else you'd like to talk about.
Okay then, have a nice rest of your day.
**Tyler Helmuth** 57:53 Been two weeks.
**Marc Schäfer (T&A SYSTEME)** 57:56 Bye.
**Pavol Loffay (Red Hat LLC)** 57:58 Thank you, bye.
