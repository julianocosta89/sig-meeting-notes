SIG: Client SIG
Date: 2026-08-04
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb** 00:17 Well, that was fun, chasing that down.
**Martin Kuba** 00:22 I don't know what happened.
**Jason Plumb** 00:25 Is the link being wrong?
**Martin Kuba** 00:29 The link in the… in the meeting invite, yeah.
**Jason Plumb** 00:32 Yeah, like, links to the one for next week.
**Martin Kuba** 00:38 I think, I think I can fix that.
**Jason Plumb** 01:19 Well, Martin, nice job giving an update on web.
In the spec meeting. Thought that was good stuff.
**Martin Kuba** 01:28 Yeah, thanks.
I just, I just decided to just go for it.
I think… I don't know, like, if Ted wanted us to do an update, like, a combined update on… Together with mobile, but it's, I think, you know…
**Jason Plumb** 01:45 No, I think it's cool, I think it's per SIG is probably great.
**Martin Kuba** 01:48 Yeah.
**Jason Plumb** 01:49 Like, more granularity, more specificity, probably the better.
**Martin Kuba** 01:53 Yeah.
**Jason Plumb** 01:55 I'd also like to commend your choice of shirt today, it's the proper one, Cleo, nice job, yep.
**Hanson Ho** 02:02 I missed the memo, or at least.
**Jason Plumb** 02:03 Yeah.
**Hanson Ho** 02:04 Part of me missed the memo.
**Jason Plumb** 02:05 We're not getting you out of that shirt anyway, Hanson.
**Hanson Ho** 02:08 I have, like, I would say 60% of the wardrobe are black t-shirts, but they're just from shows, so… So I signed in to the Zoom as a guest, because I don't have a Linux Foundation account, is that the right thing to do? Like, or do I have.
**Jason Plumb** 02:26 You can make one, and you can link it to your Gmail account.
**Hanson Ho** 02:29 Okay, cool, alright, cool. Do that next time.
**Cleo Schneider** 02:32 Is it… Kosher to just… Keep signing in as a guest?
**Jason Plumb** 02:38 I think so.
**Cleo Schneider** 02:40 Sweet.
**Hanson Ho** 02:41 Alright.
**Jason Plumb** 02:46 I'd rather people show up as guests than not show up.
So, you know, eliminate, like, like, let's get the smoothest path.
You know, whatever's easiest.
**Cleo Schneider** 02:57 Yeah, I… we just have… I don't know what restrictions we have around linking stuff to our account.
**Jason Plumb** 03:04 Yes.
**Cleo Schneider** 03:05 It's a nightmare.
**Martin Kuba** 03:28 Okay, does anyone have anything they want to talk about today?
**Hanson Ho** 03:38 Just an update that I haven't gone to the, SEMCOM meeting yet, because yesterday was a holiday, so I haven't had a chance to propose this, but no one has commented, or liked… I'm just gonna ping, like, Lamila and Trask, like, hey, is this a thing, before I show up, because I was hoping to get some acknowledgement before I show up, but… I would have shown up yesterday anyway, were it not holiday, but… It is what it is. I'll show up on Monday.
**Martin Kuba** 04:09 Cool. Yeah, I think, I would like to… start making progress on… on some other conventions for browser.
Seems like this may take some time to bootstrap. I'm kind of leaning towards just following your example and adding it… adding our semantic conventions to the browser repo, and then, you know, getting it set up there, and then maybe once we have this new repository.
we can… Talk about, like, what overlaps, and then move things from… But I think… Is it also your understanding that you will have your own, like, Android or mobile schema?
that will be based on, like, this shared, shared one that will have a dependency on it. So we will not have, like, a single, single, like, client… client.
side schema, we will have, like, browser schema, the Android schema.
**Jason Plumb** 05:02 No, I hope it's both.
**Hanson Ho** 05:04 Yeah, it's gonna be, like, a three-tier, at least, approach, where we have the core one, and then we have, like, a common Client one, where a session really should go, other things like that. And then the browser, like, you know, soft navigation is not a natural concept. Although, one could argue that… anyway, let's not get… there would be ones that are platform-specific, and there will be ones that are not. Android already has, we already have our own, and, you know.
exists because we declare it as existing, so browsers do the same. And then I think the process of actually creating a new one is just… Having… moving things from the core one down, perhaps, or moving common ones that we have, up.
So if there are things that are truly browser-specific, as long as you, in the browser SIG, decide it's good to go, you know, it's good to go, and I think ditto for Android, iOS, and other SIGs that spin up, I would imagine.
But this was all we're gonna be talking about when this spins up, but but yeah, as a preview, this is… this is what I think is an approachable model.
**Martin Kuba** 06:12 Sounds good to me, yeah.
**Jason Plumb** 06:14 So, since we're light on agenda.
I will just share what… some of the progress we've made on Android, and, like, it might help for people to, like, see some of this, like, actually look at some characters in the YAML, so… We have this… module called SemConv.
And in it, we have our definition of the Android attributes and events.
And… the… kind of the new thing that we're doing is importing specific events from upstream. So, like, all of these… are defined in Upstream?
And actually, now that I'm… now that I'm thinking about this, why… Are these imported into the registry and not into the events?
**Hanson Ho** 06:59 The events are where you define.
**Jason Plumb** 07:01 14.
**Hanson Ho** 07:02 Yeah, where you define the ones that are accustomed to this one, and the registry is where everything comes together.
**Jason Plumb** 07:09 In any case, we have tons of events and attributes. I mean, tons, I'm overstating it. We have quite a number of attributes and events that are custom to Android right now, there's probably some commonality with other platforms, and once we can reach that commonality, then we can define it in the client semantic conventions for all of us to kind of use and share. But for now, the ones that we've kind of agreed upon, because they're an upstream.
are these, and we're able to bring these in and actually do code generation based on those upstream, examples, so… see if I can find… find an example of this. So, like, there's, like, a Cenk… I think we have a jank reporter Yeah, there's an imp… yeah, so here's the one that generates events.
When jank happens, and… where's the actual thing? Yeah, so this is generated code.
Alright, so we… we're like, oh, we detected jank, let's generate a jank event, and we do that just using these event classes that are generated Kotlin classes that are coming, like, from the upstream spec.
So with just that import, it becomes really nice to be able to reference these in code, and you know, this enforces, like, attributes that are required or not.
Our parameters to the constructor.
**Hanson Ho** 08:30 Actually, the fun thing is that this is actually not the one generated from the Kotlin repo, this is generated from Android.
**Jason Plumb** 08:36 Yeah, sorry, it's generated Kotlin classes, yeah, not generated from the Kotlin repo. And we're getting rid of that dependency slowly.
**Hanson Ho** 08:44 Yeah, the… I think the templating is so flexible that repos really are depending on… or repos that consume, OTEL, semantic conventions really only need to depend on the registry, and based on that, you can use Weaver, to generate everything, and Weaver is available as a binary. So, you could generate… so… the event class that we generate includes the API that we use to actually record the stuff.
So we could shape it to however we want. Now, you'll probably want to do that for the JavaScript repo that, or the instrumentation that you set that consumes the browser constants as well, because they're just not going to be defined upstream, so you're going to have to get it from somewhere. And, There's no place better than to get it from your own repo.
Or generate it, I should say.
**Jason Plumb** 09:36 And circling back to the question of, like, are we expecting to have just 3, like, at least 3 separate, you know, like, browser, Android, iOS, like, only separate semantic conventions, or is there a common one for all client? I think, like, something like activity is probably a good example, like, that's very Android-specific.
We'll probably always have some users that want to do activity tracking, and so I don't see that going away, but it also wouldn't make sense to necessarily have that in a common area, because it's not going to be applicable across all of the client space. But there's likely to be other stuff in here that is, like, I don't know, battery percent, right?
Maybe that doesn't apply to the web, I don't know.
Maybe it doesn't hurt, but those are the… those are… that's like the bike shedding that we'll need to do when that time comes.
And there's also a bunch of stuff in here that is ugly and needs to change, but…
**Hanson Ho** 10:30 And the good thing…
**Jason Plumb** 10:31 Yeah.
**Hanson Ho** 10:32 the good thing about Android having its own, is we could actually move, all the things that are not good but are defined within the actual instrumentation into this place, and we could declare it as not good and deprecate, and then have, like, a migration reason and say, this is the good one, you know, deprecate, go to this one. So it could be a transitionary step to basically, at least strip out the hard-coded constants and putting it somewhere that at least can be shared, and then have a reasonable path to deprecation. We'll probably need to do, like, a dev release, and then, like, a, you know, bring forth, you know, the stable semantic convention release, things like that.
Yeah, and you'll be able to do that, control your own, even without the, the common repo.
**Martin Kuba** 11:28 Hey, Jason, thanks for sharing the code. I'm curious how the code generation works.
I don't know what you had to do to make it work for Kotlin, so I might… I might be.
**Jason Plumb** 11:39 Yeah, let's just… let me just walk through it, since our agenda's so light. I mean, why not? So,
**Martin Kuba** 11:46 I'm just trying to figure out, like, what we need to… do we need to do something?
**Jason Plumb** 11:49 You do, yeah, you'll have to do a little bit of swizzling to make that happen, but we have some… Gradle, that's our build system, right, for Android and Java. And so we have some tasks that are defined, but the main… the main thing is that you… you will end up running the Weaver binary.
And there's a lot of supporting stuff in here, so we're… we're downloading the Weaver binary based on what platform you're running on. There's also Docker images if you wanted to do it that way, but somehow you're gonna have to have Weaver on your build system, or your dev box, or both, likely both.
we have a bunch of, you know, generated code that helps do this thing, but at the end of the day, you get Weaver, and Weaver will consume these templates. So it speaks Jinja, and we have one for events, and one for… semantic conventions, then we kind of have, like, a base. I think this is, like, a base class. So our Weaver config file is here. This kind of tells… Weaver where to look for ginger… like, what ginger files to consume.
And then where to do outputs, and there's some other fancy, you know, processing of the YAML before Weaver gets it, right? Like, you can do a filter.
So, like, when we process events, we only want to look at events, like, for example.
And then some type mappings, right? And then our Jinja templates is where it gets exciting, I think. So for our generated event classes, get ready.
You know, it kind of looks like Kotlin. There's some stuff in here that's familiar, but there's also, like, you know, template stuff everywhere.
Because there's one template for all events.
I wish I… maybe I can do this. Let me… I might have to share my whole screen, but let me… let me show you what one of these generated event classes look like, because I think that'll be more impactful.
Let's see… Is this one of the generated ones? Yeah.
**Hanson Ho** 13:58 So, LLMs are really good at getting you started, with a boilerplate, and you can tweak as you want.
**Jason Plumb** 14:11 Let's see… Alright, this is Android Studio.
And… so for that jank event that we were kind of looking at the definition of earlier, this is generated code. So, like, we put a little disclaimer in here, like, don't… And also, we don't… currently, we're not committing the source code into our repo, so this is just a purely… that's why it's, like, orange up here. It's a build artifact, and we're able to… because it's in a module, we're able to compile against it, and we create the, you know, generated bytecode for it.
And… as part of the constructor, we include the attributes that are required and optional or nullable or not. That's what this question mark in Kotlin means. And then… So these are all optional. You can just indicate that a jank event happened, there's no required attributes, and then we also have the constants now def… That PR may not… oh yeah, it did get merged. So we also have these constants defined, so if you want to refer to this elsewhere, you can. So we have… we have that event name available.
And then, when you call emit, it just… it stitches up these attributes if they're there, puts it into the event, sets the name, and then emits it.
So that's what's generated from the template.
Like, this thing.
Right.
Which is even uglier to look at in IntelliJ, because I don't have the plugin installed.
But anyway, that's… yeah, was there anything else on this that you wanted to look at, Martin?
**Martin Kuba** 15:49 No, I think this helps me, like, actually have an… Like, some idea how it works, so…
**Jason Plumb** 15:54 Cool. Yeah, I mean, there's kind of a lot of moving pieces, but it came together really quickly, and like… I didn't… have to do a lot of iteration on this to get it… to get it going. It felt like it just kind of comes together. And that's also my experience doing the Weaver stuff that we use in the… this IBM MQ monitoring stuff that we do for, over in Java Contrib. We have a module that will, like.
send events… send messages on an IBM MQ system and get back responses and parse those into metrics, and, like, do measurements that way. Like, it's basically a metrics bridge.
for the internals of IBM MQ.
And we used Weaver for all of those definitions as well, and that also came together kind of… kind of nicely. Like, it wasn't a lot of thrashing, like, Weaver… as long… you know, Weaver will complain loudly if your YAML's not formatted right, but, like, when it is, it just… it kind of just works now. It's… it's really good.
**Martin Kuba** 16:50 Nice.
**Hanson Ho** 16:52 I threw up the links in the, in the doc. Kotlin actually, generates and checks the files in the repo, so you can actually, you know, look at, like, that model if you want. Yeah, that's a good call.
And, like, running it is just fetching a binary. You don't need to, you know, load up, like, an image or anything like that. It's… you could, you know, have a shared script to run it locally as well, as well as, doing it with the GitHub workflow. You could… set this up however you want. It's fairly lightweight.
**Jason Plumb** 17:25 So, Hanson, you have an issue open for the creation of this new repo and SIG?
**Hanson Ho** 17:31 Yeah, I created… I created a repo initially.
**Jason Plumb** 17:33 Is that linked? Can we link to that somewhere?
**Hanson Ho** 17:36 Yeah, oh, yeah, yeah, yeah, I thought we did. If we didn't, I will… We'll send that,
**Jason Plumb** 17:43 Probably in community.
**Hanson Ho** 17:45 I created two, actually. I created one in SEMCONS and one in Community, so… I'll link to those…
**Jason Plumb** 17:58 I fell in one of community.
**Hanson Ho** 18:00 Yep.
**Martin Kuba** 18:10 Yeah, I've seen that there's been no… No activity on that.
**Hanson Ho** 18:17 Yep.
I'll ping. Everybody's busy, so…
**Martin Kuba** 18:20 You know.
It's also August, so…
**Hanson Ho** 18:26 It's a very European-centric network, or organization, so you're… August is just, like, holiday, so…
**Martin Kuba** 18:33 So I appreciate that you've done this, and kind of set example for us. It makes it a lot easier for us to follow what you've done.
Yeah.
I had one question about, schema?
schemas, like, are you planning? I don't know what exactly that involves, I haven't been following that, the new model.
Are you, are you planning to add schema? Is it, is it, like, is the… This is kind of ready? It's like the… the Federate… federated some conf… approach, like, does… do they provide us, like, with instructions how to do that, or… Not quite there yet, or how does that work?
**Hanson Ho** 19:15 So, if you're talking about, like, the OTEP 8715 or whatever, the V2, the V2 definition, so… oh, I forgot which one. The Embrace repo is definitely on 2.0. I think the, I think Android, I might have changed it to 2.0 as well.
Do you remember, Jason? If it's not…
**Jason Plumb** 19:36 I don't.
**Hanson Ho** 19:37 Okay, the sample I threw up, in my personal one is 2.0. The conversion's pretty easy, it's just about moving some stuff around, and it allows you to do a lot more, interesting… well, not interesting, but, like, better ways of specifying and addressing. So, if you have… if you don't have one already, starting at V2 is fine. It's technically marked as development, but as everything is, and… and since we consume this stuff by version anyway, if the version works for you, then who cares?
And it's all… it's not runtime, right? It's just build time. So you… you generate the stuff, you use it, da-da-da.
So, it's ready, basically. A lot of the tooling, I think, may not be… if we go further down the line, but for what you need right now, just defining a registry, pulling in additional registries as sources.
and then specifying what you want to generate from that. You could do, with fancy filters, explicitly import, events like we do.
you know, however you… however you want to define this, you could define it that way, so it's pretty flexible, so it's actually really, really good that way.
**Jason Plumb** 20:54 Yeah, Martin, I want to make sure I understand what you meant by schema.
**Martin Kuba** 20:57 Yeah, I… so, your SDK right now, when it sends payloads.
with telemetry. Do you… do you send… schema URL along with that.
**Jason Plumb** 21:11 I don't know the answer to that. I think we don't.
Because I think Java also doesn't.
**Hanson Ho** 21:19 We shouldn't…
**Jason Plumb** 21:20 I could be wrong. I don't think we do, though.
**Hanson Ho** 21:23 it's not stable anyway, so, like, even if we send a schema, it's gonna be like, yay, this is what it is. I don't… no, I… I… at least I haven't touched any code that would have changed that if… either we've done it all always, or we still don't do it.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 21:37 I don't think we do it, and I think the reason is that, like, not all of our labels are part of the semantic convention, so… You cannot really apply a schema there.
**Jason Plumb** 21:49 Yeah.
There's…
**Hanson Ho** 21:53 If Java hasn't done it, then it… you know, what chance do we have? We're not even… the instrumentation even isn't even stable, so…
**Martin Kuba** 22:04 Yeah, but I mean, does it need to be stable?
**Hanson Ho** 22:10 No, but I think, like, for me, it's… I think if we spend time on semantic conventions, there are other things to do, and adding an unstable schema is probably, like, further down the list for me. I don't know, we haven't even talked about it, I don't think, Jason. Have we?
**Jason Plumb** 22:24 We haven't, no. And we haven't had anybody ask for it, but it, I mean, the… the reason why schema exists is helpful, and I could see people wanting that. I just had… I haven't heard it being asked for yet.
Ben, you've looked into it, so is that something you want?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 22:42 Yes, actually, yeah, I think, we would, we would appreciate having something like that. I think the first step is to have all the… so I was waiting for the rate at some handy conventions to be up and running, so that we have all the labels, in a single place, and then… then we can go about the schema. But, like, yeah, this is something, when you're building the consumer side of things, it would really come in handy.
**Hanson Ho** 23:07 Schemas tied to telemetry scope?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 23:14 What do you mean, scope?
**Hanson Ho** 23:16 telemetry scope, like, like a tracer scope, or, like, what does a schema version tie to?
**Jason Plumb** 23:23 There's definitely one on the resource, but there might also be one on the scope, I'm not sure.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 23:30 Yeah, I… I'm not sure what the exact standard is.
**Martin Kuba** 23:38 I, I think this is, this is, like, very important, because… for client SDKs, you will have all, like, all sorts of different versions out there sending you different data, and so it'd be really nice, like, to know, like, what you're getting in the consumer. And especially in mobile applications, I expect.
**Hanson Ho** 23:58 Oh, I think it's definitely important, it's just, like, amongst the things that… having stabilized, like, the names, defined somewhere would be a first step. Second step would be to say, hey, what is being defined? What does this represent? So, I think it's something we want to do, but… you know, in the order of things, I think there's still a couple of things that I would consider higher priority.
But if, if, if the browser folks are ready, Great to demonstrate how it could be done.
Let's copy it.
**Martin Kuba** 24:31 Okay, but it doesn't sound like anyone's doing it. Yeah, okay.
**Jason Plumb** 24:37 No, and it's… I think that the Federation actually makes it more complicated, because we do declare… so, like, when you do Federation, you have to declare your own… kind of schema, like, version. Like, you have to declare a version that you're emitting.
And… I'm sure that we don't have any practices about when we might rev that. I'll just share my screen again. We're almost out of time, I think, but… Just so that we see this and we're talking about the same thing, like, in the manifest for your schema, like, one of the things you have to do, in addition to declaring, like, what you depend on from upstream, is you have to declare.
your own schema URL, and that's a way to version this?
**Martin Kuba** 25:17 Yep.
Yep.
**Jason Plumb** 25:18 I just… I made this number up, and there's nothing there if you go to that URL, I'm sure it just is nothing, yeah.
So, I don't, you know, I don't know what this fully entails.
Other than just being, like… right now, you could treat this as an opaque identifier that has some kind of version information on the end.
But I don't think that… that's… that's probably not the design. The design is probably to actually be able to fetch Something meaningful, and to use that.
But that's a gap. We should probably have an issue to track this in Android.
And I can take that as an issue, I can take that, let's see.
**Martin Kuba** 26:00 Yeah, no, like, you have… you don't have, like, in the schema version that you have there, Jason, like, you don't.
**Jason Plumb** 26:05 Yeah.
**Martin Kuba** 26:06 It's just, like, minor version, like 0.x, right? So, I kind of imagined that it wouldn't have to stay stabilized to have a schema version.
Like, you could just, like, we could just, like, you know, whatever our instrumentations are generating right now, we could add it, we could, like, call it, you know, not major, like, not stable, but have some kind of identifiers to say, you know.
This is what it is right now, and it has a version.
**Jason Plumb** 26:33 Yeah. Shouldn't it?
Go ahead.
**Hanson Ho** 26:35 So by definition, I think we do have… have that, and in fact, because it's development, the artifacts that get marked, you know, the actual, URL has, like, dev and all that stuff around it, so we can address, like, versions of registries, and therefore define a schema based on that. I thought you were talking about, like, sending the actual URL in the telemetry. And if… if… if that is defined at an SDK implementation level, we can always just send that as, you know, as an attribute. Like, that probably would be doable.
Like, if that's all it is.
**Martin Kuba** 27:18 Yeah, I don't know, like, where exactly to put it, I'm just saying, like.
I would like to be able to send some… something that defines, like, what we're… what the data that we're sending is, right? So…
**Hanson Ho** 27:31 Yep.
**Martin Kuba** 27:32 Yeah, that's all.
**Hanson Ho** 27:33 Yeah, there are fields in telemetry scope, for telemetry version, and then one of the URLs is schema URL. When I was doing…
**Jason Plumb** 27:44 I just linked to the spec in the doc, and in OTLP, that URL field exists on resource spans, resource metrics, resource logs.
And applies to the things within them, so, like… It's at that grouping level, it's the container for your telemetry. There's also… Instrumentation library spans, instrumentation library metrics, instrumentation library logs, so I think it's also scoped at the instrumentation scope.
So it's both.
**Hanson Ho** 28:16 So it's probably defined within, like, OT.
**Jason Plumb** 28:19 It's resource and instrumentation. Scope.
Cool.
**Martin Kuba** 28:25 That helps, yeah.
Thank you.
We are out of time, so… I appreciate the discussion.
**Jason Plumb** 28:37 Feel free to add stuff to the agenda for next time.
**Martin Kuba** 28:41 Sounds good, right? See you rolling.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 28:43 Thanks.
