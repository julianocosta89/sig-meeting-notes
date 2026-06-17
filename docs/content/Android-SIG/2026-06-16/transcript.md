SIG: Android SIG
Date: 2026-06-16
Duration: 39 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb** 01:29 Let's see who shows up today!
Hi, Ben, Joseph.
**Ben Joseph** 01:42 Hi there.
**Jason Plumb** 01:45 How are you?
**Ben Joseph** 01:46 I'm good, how are you?
**Jason Plumb** 01:49 Good, is this your first time joining us?
**Ben Joseph** 01:51 Yes, it's actually my first time.
**Jason Plumb** 01:53 Nice.
I'm putting a link to the Google Doc that you might see in the chat.
**Ben Joseph** 01:59 Yes. Yeah, I.
**Jason Plumb** 02:00 We're just gonna… we're kind of just waiting for things to get started. Hopefully, a couple more people will show up, and then we can get into the agenda, but feel free to add yourself to the agenda and any items that you might have to discuss today.
**Ben Joseph** 02:12 Sure, no, I'm just here to, you know, see how you guys do this. So, honestly, it's my first time you know, participating in something open source. I'm… I recently joined Grafana, And, you know, that's how I got an interest in Autel, and I have some experience working with Android SDKs.
So, hopefully, I'm here, thinking I can, you know, contribute back here, yeah, so I'm here to, you know, watch and learn, I guess.
**Jason Plumb** 02:47 Okay, cool. Yeah, I've just added you to the agenda, just because then we have a record of, like, who was on what call when, and it's helpful to sort of track stuff down sometimes, but, yeah, welcome. Hopefully this is a pretty nice bunch, and feel free to pop in if you have… questions, concerns, and the way that we generally run… I mean, every SIG is slightly different, but at least for Android, we kind of follow the standard, which is we meet once a week, this is an hour-long meeting, We like to front-load the agenda, that way we have, you know, talking points, so during the week, as people are working, they throw stuff in here for SIG.
And then we go through it, and if we run out of topics, if we run out of time, then we usually revisit the repo and look at any new issues, any new PRs, any lingering PRs, and then we just sort of go through that. And that's usually enough. If we run out of agenda, that's usually enough to sort of, like.
Provoke some more discussion and get some action items out of it, so…
**Ben Joseph** 03:45 Understood.
Yeah, God, thank you.
**Jason Plumb** 03:48 I think it… so yeah, also at the top of the doc, we have a link to the repo itself, which you've probably already seen. There's a Google Calendar.
Yeah, we should probably put the Zoom meeting… There is a Zoom meeting on the calendar. Okay, so two clicks away. Anyway, I think we can… I think we can go ahead and get started. I have no idea about Cesar.
And a couple of these, it would be nice to have him around as our other maintainer, given that Jamie, our third maintainer, is out on leave, so… I am here kind of holding it down, I guess.
**Hanson Ho** 04:20 I think Satar has said he was out this week, right?
**Jason Plumb** 04:23 I don't remember that.
But, I believe you. It would appear so. He's been really quiet, so… I will be out next week, so… I'm just gonna leave it for y'all to run.
one of you can just run with it and organize and take care of the meeting. If Cesar's back, then hopefully he'll probably be a natural fit to do that, but I'm just making sure that everyone knows I'm out next week.
**Hanson Ho** 04:50 I can do it as Cesar's out, so…
**Jason Plumb** 04:52 Killer. Thank you. That's awesome.
Okay, so I think as I was reviewing a screen orientation thing, I found… or maybe it came up from another PR… There, and I didn't link to it, but in the orientation instrumentation.
There is a manifest… This thing.
Do we need this?
Is this just an artifact? Like, this is empty, so to me, it's telling me it provides almost nothing.
And I think it can be safely deleted.
Does anybody know any reason why this should be in here?
**JM Jason Morris** 05:41 Delete it and see if it still bolts.
**Jason Plumb** 05:45 Yeah.
**Hanson Ho** 05:48 sometimes when you generate a project, they generate files, but, I'm not sure if an Android project requires a manifest if it doesn't have Anything to merge it from, or… Anything it needs to merge.
Into the app manifest, so…
**Jason Plumb** 06:08 Yeah, but it could create it on first need, right? There are… I think there are other manifests in the project that are used, like…
**Hanson Ho** 06:16 Yeah, usually you'll put, like, permissions or whatever, things that that particular thing needs. Exactly. But, you know.
it's empty, so I don't know if it requires that, but, like, as Jason's… the other Jason said, if you delete it and it breaks, then, you know, then we'll know we need it.
**Jason Plumb** 06:34 Yeah, that's a good… that's a good… good way to test that, yeah. Okay.
That one's short, and pretty, unexciting.
Screen name.
**Hanson Ho** 06:46 So…
**Jason Plumb** 06:48 There is an upstream standard for app.screen.name, In the semantic conventions.
It's the name of an application screen. It's part of a device displayed drawn by the app.
pretty generic, but we kind of all have a mental model, at least on Android, probably what a screen is.
If you want to get into the nitty-gritty, that's when it starts to get complicated, but at a first glance.
we know… we think we know what a screen is, but all over the place, we have screen.name, and I think that we should be trying to normalize on semantic conventions, but, you know, we have… our own definition of screen.name. It seems to be redundant with app.screen.name.
And I think that we should probably… I'm suggesting that we probably should rename it.
**Hanson Ho** 07:38 Yep.
These are… these are… these are, by definition, not stable, because we haven't declared any of these instrumentation to be stable, I assume. So I think ripping that off is… is good.
Because we already have something already made in Semantic Adventures, as generic as it is.
**Jason Plumb** 08:00 Yep, so, not stable, but we still don't want to break people, so there's a few ways that we could go about doing this. Let's assume… Today… Still waking up over here. Let's assume today that there are at least one vendor that's using this, screen.name.
and not app.screen.name. If we do the next release with this change, then that breaks them, so I think… We probably want to either emit both and mark one of them as deprecated for some amount of time, or what we do in other projects is there's an opt-in flag, or an opt-out flag for the entire, kind of.
collection of… of… newer semantic conventions, and then when we bump to 2.0, that's when we can do that switch, right? So people can… that'll give… Users and vendors time to adjust to those changes.
And the… with my OpenTelemetry hat on, we should be attempting, or we should be striving for, you know, stable by default.
We don't want to be flip-flopping and breaking people with every release.
Go ahead.
**Hanson Ho** 09:12 Oh, so didn't we just flip the switch with crash, and just started calling it, app.crash, rather than device.crash?
**Jason Plumb** 09:23 We did, we haven't released that yet.
**Hanson Ho** 09:26 So, I think… I think whatever we do there, we should do here. Like, either we have a uniform policy to say, the attribute names could change at any time, or we basically say we deprecate, and then remove at the next major release. So, so… In that sense, Well, I guess the other one would be harder, because we… it's firing a whole last event, versus this is, just an attribute, I assume. Unless… Yeah, so… actually, if anything, the other one would be… would be, even more of a… potential issue if, you know, if we're changing the literal name of the event. This is just an attribute, so… Yeah, and I think you make a good point about not wanting to switch it up, in the middle on a minor release. At the same time, then we basically are saying, we're gonna keep the semantics, or semantic… yeah, the shape of the telemetry until, the next version.
So… I would prefer not to have another flag to opt-in, because then people will basically say, well, I'm just going to opt-in all the time. I'd rather do the duplication and deprecation and then removal in the next major version.
**Jason Plumb** 10:49 What do you…
**Hanson Ho** 10:50 Yeah.
**Jason Plumb** 10:50 Why do you say that people will always opt-in all the time?
**Hanson Ho** 10:53 Oh, they, they don't… they don't want to change… sorry, people will… will not opt in all the time. They will.
**Jason Plumb** 10:59 dangerous, right?
**Hanson Ho** 11:00 They will basically say, I'll just keep whatever I had old, I don't care.
**Jason Plumb** 11:03 Yeah, until we hit 2, and then they won't have a choice, right? If they want to upgrade to 2, then they have to bite the bullet, and if that's a bigger change by deferring Those things as they come along, which it would be, right?
Like, this… I think the way it's intended to work is that you have 6 months, or however long it is before we release 2.0, that people can… incrementally, kind of on their more relaxed schedule, take on these semantic changes as they appear. And then by the time 2.0 drops, there's just one flag, right?
**Hanson Ho** 11:36 So, where do we set the flag, and is it default on or off?
**Jason Plumb** 11:42 It's a fine question. We don't have the plumbing for that yet, and I think the default will be to not opt into the new ones.
**Hanson Ho** 11:53 So anybody who is new to the project, we would be getting the old ver- the deprecated version.
**Jason Plumb** 12:00 That's right, that's right.
**Hanson Ho** 12:02 Ehh… And then everybody basically has to switch, rather than just the people who need to.
Like, I'm… I'm… and maybe, you know, this… I'm thinking make the default to be opt into the new behavior, and then have the ability, in whatever, builder or whatever they use to start this to disable it. So, the change will be a one-line thing.
And I think for Android, that seems very reasonable, to ask for somebody to… to, on their start, set something, that… that says, hey, I want the deprecated behavior, or old behavior, and default to the new one. Because I think… I think it's important to… have everybody, by default, go to the new one, unless there's a really good… unless they have a really good reason to want the old one. I know, I know it may not be, Per convention, or… or expectedness, but… this is almost like something we should have done in the first place, and we're just kind of, like, you know, catching up. So, that's… I kind of prefer that.
**Jason Plumb** 13:10 Yeah, yeah, I know.
I mean, my instinct is to just keep with what the semantic conventions say, like, to treat them as law. That's my instinct, but I'm also trying to not… I'm trying to make it easier for adoption by not thrashing our users too much, so there's a balance there.
**Hanson Ho** 13:31 I'm…
**Jason Plumb** 13:33 I'm also looking at what Java does.
And there's this semantic convention for… or there's this configuration for opting into the semantic convention stability stuff, right? So… This is not quite the same thing, right? Because this is… Like, none… like, we're making a change from experimental to experimental, right? Or development to development.
**Hanson Ho** 14:00 Yep.
**Jason Plumb** 14:01 So it's not quite the same thing.
**Hanson Ho** 14:05 It's almost… it's almost, like, non… from, like, non-semantic conventions to semantic conventions, so it's… it's…
**Jason Plumb** 14:11 Right.
**Hanson Ho** 14:12 Yeah, it's… the other one's almost like, it's an implementation detail. Although, I don't think we… I don't know if we can say that, but it is effectively something that is not… Defined to be more than what it is, which is… what literally that instrumentation decides to output. So, we may have a little bit of a more wiggle room, but, you know, I guess… it still stands, like, it's the migration path. It's, do you have to opt into old behavior, or do you have to opt out of new behavior?
**Jason Plumb** 14:46 The only reason I'm looking this up is because… okay, so the next semantic invention is, is on Monday. We could potentially ask there… Or we could hit them up on… on… we could… we could ask what people think about this, and what the other… what the other SIGs are doing in these cases.
So I can take that on.
We could also just ask, I'll just ask on Slack, probably.
**Hanson Ho** 15:12 Yeah.
**Jason Plumb** 15:14 Okay.
**Hanson Ho** 15:15 I think, just in general, Android, this is… it's less of a problem to do this type of thing, especially if we make it clear that, hey, you need to do this, and the fix is one line. So, I'm hopeful that just because of… of… Android precedence, or expectation, and the fact that what we had before wasn't even semantic conventions, that we could at least default off. Or default? Default off? Well, whatever. Default new behavior.
**Jason Plumb** 15:51 So, I'm not hearing any pushback, though, around changing… screen name to app.screen.name. Like, to using the semantic. I don't think anybody's saying that we should hold off.
**Hanson Ho** 16:03 No.
**Jason Plumb** 16:08 Okay.
**Hanson Ho** 16:09 And we should, whatever we do, we should, we should back… back… backdo it, or, you know, make sure that… Per device.
**Jason Plumb** 16:17 I agree, we should do that, we should have the same handling.
**Hanson Ho** 16:25 And ideally, we could… we could put it in one place where, you know.
Have something that's, like, getEventName, and then… and then basically… have, like, the default one to be, like, whatever, and then… So, so basically, ideally, the code, when we add, when we change the device name, or when we change the event name, we don't have to change every, consumer, or whatever we use it to basically do an if check, but, like, have it all, like, you know.
centralize and, like, get device name, or get event name.
**Jason Plumb** 17:02 Yeah.
Okay, I think we have a path forward on that one.
This one is probably not worth talking about until… we have the other maintainers here. This is, like, an internal kind of CICD topic. There's a desire, I'll just give you the TLDR, there's a desire to switch over from using… just flat GitHub action secrets to using environmental… environment secrets, and that allows you to give a much narrower scope than any old, Any old branch, so you can declare which branches have access to which environments, and then through that, you can say, these secrets are only available on the main branch.
and on, release branches, so that when we do actual builds and releases, that's the only time that a build should ever have access to those secrets. So, we should switch. Anyway, we'll talk about that another time. I might just do it, I'm most of the way there, so I might just do it anyway.
And that's just, like, kind of maintainer housekeeping stuff.
And then the last topic for today, but I also want to make sure we talk about, and no one else has added anything yet, so I will… I don't know why this keeps happening to this bulleted list, but I have to keep doing that. Okay.
So, federated semantic conventions.
It's a thing now.
So I opened this issue yesterday, and maybe no one's read it, but I'll give you the breakdown. This allows us… so right now, we have… our own… and some of this is due to the, like, history of this project and its origins, but, like, we have a lot of, like, bespoke Android semantic conventions just littered throughout this repository.
And that comes in the form of… Event names that don't live anywhere else, and attributes that don't live anywhere else, that are of our own design.
Which is completely fine to do that, like, we're… you can use OpenTelemetry and just generate those things with any names that you want, right? The APIs allow for it.
But we want to… we need to adhere to the well-established semantic conventions when and where they exist. Like, device crash, right? So we have the new name in the semantic conventions repository, we need to be following that stuff.
But right now, it's… it's difficult… To see where we don't… Where we're not using established conventions, and where we're using bespoke conventions, and so… what this new OTEP that was merged… let me go back and do it this way… This was merged, I don't know.
like, a month or two ago. What does… what this allows you to do is to declare or have your own semantic inventions. Also, you could imagine, like, projects outside of OpenTelemetry that want to… that are not official projects might also want to establish their own semantic conventions, and this is a way for them to do that in a conformant way that can still leverage tooling like Weaver to do source code generation, et cetera, et cetera.
Document generation… And… I kind of describe what the problem is and what I think the approach might be. I'll just give you one example, right? So if you go into any of our… instrumentations, and look at the documentation for it. I'm just gonna pick… Fragment.
We've done… we've done a pretty good job now of, like, documenting what the shape of the telemetry is like.
But, you'll see things like span names here. These are all the span names. These exist nowhere else.
Right, they exist in the code, and they exist in the docs. And there's even been times where the code has changed, and we forgot to update the docs, and so those two things are out of sync.
If we have our own, YAML descriptors for the semantic conventions.
Then we can do code generation, then we can do doc template generation, and we can keep those two things in sync, and make it more official. Even in cases where we might hate the names, right? Like, this, like, uppercase, like, created is totally not a… is not a conformant OpenTelemptry name, but at least we can see them all in one place, right? So… That's what this is proposing, and I want to… before I talk through the, kind of, the phasing of it, does anybody have any thoughts or questions on this so far?
**Hanson Ho** 21:35 No, we do this in Embrace, too, so we can, you know, do things like share cross-platform, and things like that, and it… yeah, this makes total sense.
**Jason Plumb** 21:48 Cool. Are you using the SEMCOM V2 style, or is it your own design?
**Hanson Ho** 21:53 No, it's the old, the old way of recommendation, so before the OTEP, it's like, hey, this is how you can get your own semantic conventions.
Jamie did that, so… But this'll be nice. So…
**Jason Plumb** 22:10 Yeah.
And as we know, like, getting things into upstream, as much as we want to do that, that's often a process, and there will still always be things that are just Android-specific, so that gives us a path forward on that stuff.
Alright, so the first phase, I'm calling this, like, the phased approach, and this is largely just because these semantic conventions touch, like, every instrumentation, like, and I don't want to just, like, have a gazillion files change with a gazillion lines of code.
So, I think I opened the PR yesterday to create the new module.
And it will be a top-level project module called SEMCOM, and it will have in it our list of… our registry of attributes, our events, and the manifest. And I'll show you what that looks like.
this thing… So kind of late yesterday, I opened this, but yeah, please have a look and please review. Pretty manageable change set so far, right? So I'm trying to do this in little bite-sized increments. So here's the top-level project, and I do wire it up to, even though there's no, like, source code in here, I'm just, like, setting the… the groundwork for this stuff, and it is included in Settings Gradle. The README is pretty generic.
There is… A top-level registry of attributes, so if you look through this, this should be all of the attributes that we reference.
And so these are not duplicated, right? If you look across… like, when this lands, when this PR lands, hardware pointer type, that's duplicated now, right? It's in the registry, and it's still hard-coded somewhere.
That's… but that's… this is intentional, right? Because there's a phased approach here. So, first step, get all of the stuff defined in the registry, and then in the events.
And what's nice about this federated thing is that we can also just refer to existing upstream attributes as part of our event definition.
Alright, so this is just a ref over to the existing SEMCONF.
And that's declared, I believe, as a dependency through the manifest. Yeah, so look at this. So, we're saying that we depend on upstream semantic conventions.
**Hanson Ho** 24:31 A particular version, too. Okay, cool.
**Jason Plumb** 24:33 And the version, yeah. I don't know how we're gonna manage that long-term, but let's just go with it for now.
So, anyway, so that's phase one. You can imagine, then, what phase two might look like.
How to build stuff to do code generation.
Once that happens, there'll be a bunch of files, like .kt files, with these constants defined, and then… That'll be one PR, and then the third PR will be replacing usages of those hard-coded values with the constants that we've now generated from Weaver, through Weaver.
And then we do the same thing for events. So, add code to build the event files. If you haven't seen, I think we talked about this last time, but if you haven't seen… This PR, it's generating event classes that kind of look like this.
where you can make an instance of them and then emit it through a logger. So that would be, like, I think I call it a Phase 4? I've lost track, but, like, Phase 4.
And then, you know, finally swap in the events that right now we're hard-coding these event names, and we call emit, we would replace those with usages of the event classes.
And then that's kind of the… That's what I'm throwing out as a path forward. I know it's a lot of words.
What do you think?
**Hanson Ho** 25:54 Looks great. We should probably… I mean, we just talked about the deprecating, like, changing. We should build that infrastructure in with this as well, so we have, like, a canonical name, and then have, like, a fallback, and the canonical will get… something that is more semantic convention-y, and then the fallback will be, you know, basically coming from, well, I mean, we can decide, you know, how we want to shape that, but ideally, there'd be, like, a sixth phase, maybe 4.1 or whatever, that will… When we actually, like, the final state, the instrumentation should be asking some infrastructure for an event name, and built in to, that will be, you know, the adherence to the flag that we're going to propose.
To basically get the new one, or, like, the legacy one.
**Jason Plumb** 26:49 Yeah. Yeah.
**DavidGrath** 26:54 Amazing.
**Hanson Ho** 26:54 this could…
**DavidGrath** 26:56 Okay, yeah, I'm kind of… yeah, I'm kind of curious about the current state of span events as well. I can't remember exactly how… Well handled we are with it, and how it might tie with this.
**Jason Plumb** 27:10 At least in Android, I think there's only one place where we use them, but in general, span events are still around.
They are deprecated. I think they will continue to be deprecated for the foreseeable future. The intention is that you should generate event events, like true events, and give them a span context instead.
So… A separate signal, instead of it being events that hang off of a span, it's a separate event that can be correlated via span context.
**Hanson Ho** 27:43 the SDK, needs to support, logging events with span context, and also, using the deprecated, add span event API, to basically,
**Jason Plumb** 27:58 bridge.
**Hanson Ho** 27:58 wire it back, and I don't think that work is done yet. Span event is… the API is deprecated, the OTLP representation isn't, so you can still theoretically, in the SDK level.
put, spat events in… events in spans, but the very nature of spat events is that they're not as expressive as, as, regular events. So, you know, there… there is no… there is a name, but there isn't, you know, anything else.
there's, I guess, I guess, attributes and things like that. So, you could see how things get a bit dicey. But, you know, as Jason said, we don't really… we don't really use it here, so we don't have to worry too much about it.
And it's orthogonal to this, because I don't think we're using span events with an official, semantic invention event name, because… those… those came a lot after.
our usage of bad events, I'm sure.
**Jason Plumb** 29:04 So it looks like the upstream Java SDK incubator… brought in the event bridge, and I think what the event bridge does is that exact thing, where if you call span.ad event.
It uses the logging API, I think.
**Hanson Ho** 29:19 Yeah, because you'll know what… what span you're adding to, so that's the context. And then I think probably everything else just gets transformed into attributes.
**Jason Plumb** 29:29 Maybe I'm confusing it, though, because this reads event to span event… This reads the other way around.
Which… this is a log record processor which bridges events… as span events on the current span. So this is when you call… Yeah, so this is the other way around. This is, like, when you're calling log or emit event.
Patching back into a span event.
**Hanson Ho** 29:55 this is probably what they want to do first, because what they want to get rid of is usage of the ad span event API, so they would have to… they want people to switch to use the regular event API. So, I could see that this being first, but.
**Jason Plumb** 30:15 Yeah, I think I'm also confusing myself, though. Let's see.
**Hanson Ho** 30:19 At the same time, to, on… on Android, to say that every… a span event, which is pretty cheap, turns into a full-ass event, which is less cheap, is a decision that we have to make, whether we actually want to enable this, or, or, you know, basically have old behavior. Certainly, we have to, like, surface it, because some people will want that. But it's… it's… it's… there's a more of a pragmatic decision that needs to be made, for… for Android, as to how we want to encode these.
Canonically, as it goes out. So… Especially if our instrumentation isn't really… You know, we're not logging… like, events, events. We're just… Creating span events.
That makes sense.
**Jason Plumb** 31:14 It does. I was surprised to see that this is not deprecated. I thought it had been, and it looks like it isn't yet, but there's certainly talk about it in the spec.
**Hanson Ho** 31:26 It's separated in the API spec, right?
the add span event method.
**Jason Plumb** 31:31 I thought it was.
**Hanson Ho** 31:32 Yeah.
But I guess it isn't in the Java API itself.
**Jason Plumb** 31:45 Yeah, this event data is different than the… I believe it's different than the log event data. Yeah, trace event data. Anyway, I think… Does that help a little bit, David? I know it's confusing.
**DavidGrath** 31:58 Yes, it does. I forgot that there was actually a way to convert it Yeah, on the… behind the scenes, to make sure that it doesn't break things. So, yeah, it helps.
**Jason Plumb** 32:08 Yep.
**Hanson Ho** 32:10 It's also both ways, too, the conversion needs, too.
**Jason Plumb** 32:19 Cool, so we still are not showing up in this Google thing, Hansen?
**Hanson Ho** 32:22 As of yesterday, no. I can do another search today, but .
**Jason Plumb** 32:26 No, where is it? I thought we linked previously.
Can't find it now.
**Hanson Ho** 32:33 I can… I can flip this in the chat.
Technically, this is under the, analytics category, so they might… They potentially could, classify us differently, but I do a search and it's not there either, so…
**Jason Plumb** 32:53 Bummer.
Okay, so it's really just hurry up and wait?
**Hanson Ho** 32:58 Yep, I'll wait till next week, I'll get… oh, we'll ping them again.
**Jason Plumb** 33:02 Cool.
**Hanson Ho** 33:04 But yeah, oh, but now all the maintainers have been added, Severn's added all y'all to the, to the, SDK, the, the, the, the project. So if you, if you log into, your Google account, and point it to, Android Vitals, or whatever places that you see all the Android apps you have access to, this SDK should be available for you to see, and you'll be like, hey, you're part of this, but… at least for me, I can't do very much other than… you know.
**Jason Plumb** 33:39 There was no, like, time… hopefully there was, like, no time-limited invite or anything that I was supposed to be responding to.
**Hanson Ho** 33:45 No, I don't think so.
**Jason Plumb** 33:46 Okay, good, because I didn't.
**Hanson Ho** 33:49 That was just… I think he did it Monday, so… Okay.
**Jason Plumb** 33:54 Nice.
Alright, well, we still have this milestone for the next release, and we need to be releasing pretty soon, and that's because… We're a month now.
Which means, if I'm out next week, we either do it this week, or we wait 2 weeks, and I'm inclined to say we do it this week. The… The remaining stuff for this milestone is pretty small.
So… I think we can get that in, but I also was thinking that we should probably figure out this.
**Hanson Ho** 34:27 I was just gonna say.
We might want to just revert it… I know it took so long.
**Jason Plumb** 34:34 I can look at it today. I'll see what it looks like. I can maybe make progress on that next day or two, I hope.
**Hanson Ho** 34:40 Okay.
**Jason Plumb** 34:42 Is there anything else that anybody wants to have in the next release?
**Hanson Ho** 34:47 The, the thing, that I'm… just updated, but I haven't checked to see very, the… I forgot what it's called.
So when I updated a couple weeks ago, with the, disable logging stuff, I made the changes, you wanted.
**Jason Plumb** 35:13 I'm drawing a blank on it.
**Hanson Ho** 35:14 Oh.
**Jason Plumb** 35:15 already merged.
**Hanson Ho** 35:16 No, no, it's disabled tracing. The API to thoroughly disable tracing, logging, and metrics.
**Jason Plumb** 35:24 Yes.
I want that in there too, so I think that this is close.
**Hanson Ho** 35:30 Yep.
**Jason Plumb** 35:33 That's definitely in the milestone.
**Hanson Ho** 35:35 Cool.
**Jason Plumb** 35:39 There's just some comments, yeah.
**Hanson Ho** 35:42 I, yeah, I made those changes today. I need to go and close the comments. Please. I think I took them all.
**Jason Plumb** 35:49 Cool. Great.
Yep, so that issue will get closed by your PR, I think. You know, I think… I think what you did is, like, a superset, or it's the better approach than just exporters.
So I think we can resolve that one when yours goes in.
This needs to happen after the instrumentation releases, which it has not yet.
And they are dragging their feet intent… dragging their feet is not the right… It's not doing it justice. They're being slow and thorough because they expect to do a major version bump next month.
So it'll be Java 3.0 probably in July, and if not July, then, you know, August, September.
But… They're leading toward a 3.0, and so they're really being careful and packing stuff in, so that's why it's taking time.
But we can't merge this one until instrumentation, so if instrumentation doesn't happen, then we would just… we just won't release this week, and I'll leave it to Cesar or whoever to do it next week, and if it doesn't happen in those two weeks, then I'll do it when I come back.
I think this one is close as well.
It'd be cool to have this one in. I like that we're getting a bunch of new instrumentation, too.
Oh, I thought I reviewed this yesterday, I'm sorry. I think… I started looking at this, I think I didn't finish, but I think this can go in.
Cool.
Is there anything else new and exciting in here?
We got the truncation, that's great, we talked about that on Slack a little bit. Power save mode, I haven't looked… oh… Diane I look at this one?
Yes, I did.
Was there anything else remaining on this?
Cool, I think we can get this one in, too.
Awesome.
Well, with that, I think we've hit the end of our agenda. We do have 20 minutes if people have anything else they'd like to talk about.
Or dig into, or think about.
It's kind of a weird… a weirdly slow time with both Jamie and Cesar out this week.
I… there are a bunch of PRs that can use reviews, so David, thanks for helping out there.
Yeah, it just… These sort of projects, they ebb and flow, so… That's the nature of it.
**Hanson Ho** 38:48 We'll use this extra time to review PRs.
**Jason Plumb** 38:51 Sounds great. Yeah, do that. Please. All right, thanks everyone.
See you next time.
**JM Jason Morris** 38:58 mine.
**Jason Plumb** 38:59 Right.
