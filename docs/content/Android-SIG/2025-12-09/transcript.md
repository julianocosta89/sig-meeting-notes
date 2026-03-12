SIG: Android SIG
Date: 2025-12-09
Duration: 54 minutes
Zoom Recording URL: https://zoom.us/rec/share/SAOn4Lv9D5k7LFKmhK4niUQlvO91NzoU7EI9GkLm16s9k0BvJMRh58E5sC54-OCJ.W48yoQmUY-0RWOCZ
============================================================

## Zoom Recording Transcript

**JP Jason Plumb** 00:26 Good morning.
**Mustafa Haddara** 00:29 Good morning.
Is it just me and you today?
**JP Jason Plumb** 00:38 Let's find out.
Hopefully a couple of people will straggle in.
Jamie had something on the agenda, so that's a good sign.
In the meantime, I'm gonna have a first sip of coffee.
**Hanson Ho** 01:18 Yellow!
**JP Jason Plumb** 01:20 Yo-ho.
**Mustafa Haddara** 01:22 Hello.
**Hanson Ho** 01:26 I tried to move your tab, Jason, on the Zoom screen. It didn't work because it's a screen share, not an actual tab.
**JP Jason Plumb** 01:36 Yeah, sorry. That doesn't work like that. Yeah, I know, I know. I've done it, I've done it.
Here's the one that keeps getting me, is this new feature, because what I will do, I'll find myself, like, I'll be reading, and I'm like, oh, I probably want to follow this, and I start pressing down… on a link, and then I'm like, no, actually, I don't want to follow that before I release the mouse button.
And what I've always done is to just, like, move my mouse away, but there's this new thing now, and it's not gonna do it because I'm in Google Docs.
It's gonna try and format it. Well, no, so that's a bad example. But, like, on the rest of the web.
I don't know, let's just give an example. This is a new feature. So, like, I'm like, I probably want to click this. Oh, wait, maybe I don't, and if I release my mouse now, it's gonna go to that link, but if I don't want to, because I'm being phished or whatever, I can just, like, go over… there it goes. Okay, wait, how did it… It did it for a second, let's see.
Man.
Now I can't even do it because I want to. It was like, oh, there's a way to split tabs now in Chrome. There it is.
**Hanson Ho** 02:46 Oh, no.
**JP Jason Plumb** 02:47 And I was doing this by accident, like, all day yesterday, and I'm like, who wants this?
**Hanson Ho** 02:53 That's what happens on my iPad, when my fingers are slow or something.
Yeah, so… apologize for the ads, but I was just trying… like, that, like, like, trying not to release a link is, like, ridiculous.
**JP Jason Plumb** 03:09 Whew! Okay, so I have one item on the agenda, and then not too much else, Was this the same… because there might be another one with the same… No, but there is another one, so I want to pull these up, because I think it's worth talking about, and I did have a comment that maybe we wait until Cesar is back, and like.
adding additional support, like adding features, expanding our API footprint, will always be allowed without having to bump a major?
So, we just… I think we want to be careful about it, and methodical, and not just, like, take every single request and put it in the main API. But there was also this.
**Hanson Ho** 03:52 Well, the thing is, if we put it in the main API, we can't pull it out, right? Unless…
**JP Jason Plumb** 03:59 That's right, yeah, yeah.
**Hanson Ho** 03:59 Unless we have a facility to say, these are draft APIs, or these are alpha APIs.
**JP Jason Plumb** 04:04 Right.
**Hanson Ho** 04:05 That would be nice, because I don't… it'd be hard to, like, hard commit to something that seems useful, but we don't have time to, like, do we want to support this forever and ever and ever? Right. So, almost like a beta within our, you know, like, with instrumentation, we can probably use the existing, alpha stable, whatever, but, like, with API, that's… that's where it's like, hey, this one, we're putting it in here, but be aware that it's not.
**JP Jason Plumb** 04:33 that we… it may change. It's an alpha… it's like a beta API or something like that. But the act of adding it, is not breaking. That's my… that's my main point.
**Hanson Ho** 04:42 Yes, yes, yeah, yeah, definitely.
**JP Jason Plumb** 04:44 So, these are really what this whole topic is about, is additional customizations.
And core. So there's… maybe I'm blending a couple of things, but that was one example. So this person's like, hey… I really wanted to be able to… add these… these… I want to be able to customize these two… 3 span, metrics and log.
components.
And the way that they've done that is by adding API surface.
Yeah, adding API surface to the OpenTelemetry Roam Builder… Which, you know, is not the thing we're taking stable. I'm hesitant to rush into this yet, because I don't know if we want to keep or how much we want to keep adding convenience stuff into OTRB, because it's, like, already pretty sizable. So I'm intentionally being a little bit slow on this pull request.
But what they're doing makes perfect sense to me. So, they want to be able to add a batch span processor customizer. This is the kind of stuff that exists all day long over in the Java world. Well, maybe not to this degree, but close. Because… right, so we, like, this gets called later during the build process, We can see where… Okay, we make our batch span processor, there's a builder, which is what we were using before, but we were just calling builderBuild, and now that builder… Gets passed through the customizers, right?
And they can do whatever they want with that span processor builder.
And in this person's case, what they wanted to do was to… did they give an example? They don't, but they want to be able to add stuff to it and customize it. Completely reasonable thing to do, I just want us to be thinking about it. I'm curious what folks think about this by expanding, because I think you can already get to this.
Right? I think you can already do this, but you have to then go through… the true… Maybe we don't expose this. I think you'd have to create the SDK yourself.
**Hanson Ho** 07:00 So, I thought, like, the theory was that, the… the… the short… I forgot, the OpenTelemetry… Rum Builder, is the, where everything… you could do everything on there. So, theoretically, on the OpenTree Drum Builder.
anything is possible, short of, like, super unsupported SDK creation, which you have to do yourself. And the shortcut API is where most… where we have APIs for what most people want to do.
does this rise up to the level of what most people want to do? Is… is the… is the question of where we're actually at this. So if it's not in Rum Builder, then that… that almost, like, we should definitely… like, Run Builder should be the one that's got everything.
maybe not convenience methods, if there's already a way of doing it, just do it in the not-convenient way, maybe? But if it's… if it goes to the level of, hey, we should Allow this, because everybody wants to do it.
With processors and exporters, it probably does rise to that level, because we already do that for exporter customization. So, if we can't do that for processors, we should probably allow that.
**JP Jason Plumb** 08:18 Yeah.
Yeah, that's why I think this is probably a good, pull request. I just want us to think about it a little bit.
Curious what Jamie… Jamie and Mustafa, what do you think?
Would you… do you think it's good for people?
**Jamie Lynch** 08:34 I… Personally, would prefer just to be able to, like, set a processor or exporter.
And not deal with, like, another abstraction.
So, yeah, I think I was looking at trying to do that for BioV OpenTelemetry, initializer API, and there isn't a way to do that right now, so that feels… Like, it's probably something we want to support.
**JP Jason Plumb** 09:06 Yep.
Okay.
**Hanson Ho** 09:08 Yeah, the customizer abstraction, I'm not… I don't know if I'm 100%, like, Like it?
**JP Jason Plumb** 09:14 I was full of that stuff.
**Hanson Ho** 09:17 Yeah, it's… maybe I'm just not familiar with it, but it… it's… It feels really awkward to use. But if, if that's… I mean, if our API right now is still kind of based on Java, then that's what we should do.
then I guess the question is, when can we start… stop doing that? But that's a… that's a much later question.
**JP Jason Plumb** 09:40 It is.
Yeah.
I… well, then, I think that's a good segue to bring up something else. Which is related.
And that is that I think in the initializer.
So, similar to how Java handles this, and similarly to how a bunch of the OpenTelemetry Rum Builder stuff is set up today, I think there's an opportunity for us, and this could be somewhat controversial, but I think there is room for us to also Between this builder and its things, between this builder and the build.
if we use the DSL to allow the initializer to have builder customizers, and we don't have to use that name.
But something that then gets this builder instance, right? Because this is the OpenTelemetry Rum Builder.
And then they can poke all of the APIs that exist on that thing. I'm not showing it anymore, but you know, that's the… that's kind of… that's our baby kitchen sink. If you call the underlying Java SDK the auto-configuration, like the real kitchen sink, we're like a baby kitchen sink, and that would allow us to expose the baby kitchen sink to… People using the initializer, and it's only one… Probably only one additional API. But I want us to be thinking about it.
**Hanson Ho** 11:05 I thought this was what we tried to do initially, like, I think my first suggestion was basically, expose the baby kitchen sink, and then have, like, convenience methods on top of that that provide default to the baby kitchen sink, but something about that didn't work, I remember.
Okay. Because, you know, we foresaw this problem, like, I think we're like, well, people had it, and then we're like, well, let me expose the whole thing. It's like, oh, we can, but then some… for some reason or another, it didn't work.
I don't remember what that was.
But yeah, that would be nice, to basically say, this is the breakout point, and you can have the entire thing. I mean, maybe we just, we need to expose that API, of the builder, maybe that was what we're hesitant on, and that will become stable by proxy, because it's, you know, it's public.
So maybe the baby sink could be something that we call, like, beta or something like that?
**JP Jason Plumb** 12:00 also a dependency problem, right? Because then… Oh, yeah, now, like, your change that pulls the OpenTelementary Rum instance, when you use the initializer, you don't get core by default.
Yeah. Yeah, so that would change that, or we would need an additional interface.
**Hanson Ho** 12:16 Yeah.
**JP Jason Plumb** 12:17 Okay.
**Hanson Ho** 12:18 And I don't think we had the abstractions well enough to pull parts of that out without pulling the entire core out, I think.
**JP Jason Plumb** 12:25 I think that was the hesitation. I think we didn't want to make that stable, and if it's… if it's a… if that is a… if the builder then is a parameter to one of the methods, then we can't do breaking changes on that parameter. I think that was the problem.
**Hanson Ho** 12:38 Unless we have a way of declaring that to be, like, the baby sync is in beta.
**JP Jason Plumb** 12:44 Yeah, I don't think you can do that, though. I don't think you can have a stable API that takes unstable parameters or whatever.
**Hanson Ho** 12:50 Optional. Optional.
So I… yeah, I… I think that's the hangout. You're right.
**JP Jason Plumb** 12:57 Okay, okay.
And then, I think I also linked to this one, which was a comment on the developer feedback issue, the call for call for feedback as we're going stable. Someone responded on Friday and said, hey, I'm using the new version, and what I need to do is to customize the resource. And they were saying, I used to be able to do that, and I can't do it anymore. You guys broke it. And I think that's not accurate.
I think it's still there. This merge resource, though, is not on the Roam config, and I responded, and I pointed this out, but like…
**Hanson Ho** 13:32 The merge resources on the Rum Builder.
**JP Jason Plumb** 13:35 So I think they just have it in the wrong place.
I think they need a parentheses here, and that would fix their problem, but, The point being, people are looking for a way to customize the resource, and we don't expose that at all through the initializer yet, so… that's probably worth filing an issue about.
**Hanson Ho** 13:54 Yeah, that would be extremely common. Yeah.
**JP Jason Plumb** 13:56 I think we should just do that.
**Hanson Ho** 13:58 Yeah. Let me link to…
**JP Jason Plumb** 14:00 Wait, where was I?
Oh, yeah.
**Hanson Ho** 14:03 Pass in these attributes, and we'll merge it.
**JP Jason Plumb** 14:06 By default.
I'm clearly using the dumbest lingo on this. I'm sorry, not sorry.
**Hanson Ho** 14:26 No, baby kitchen sink works well because it is pretty meaningless, but also conveys some generic meaning.
**JP Jason Plumb** 14:34 Which…
**Hanson Ho** 14:36 The worst thing is we pick something that means something to people.
**JP Jason Plumb** 14:40 Yeah.
**Hanson Ho** 14:41 Someone doesn't call things marshmallows. Everything's a marshmallow. What is that? Well, read the definition.
**JP Jason Plumb** 14:45 Widget, it's a widget.
**Hanson Ho** 14:50 The obscurity is by design.
**JP Jason Plumb** 15:14 I'll open an issue on this.
I see Cleverchuck's joined us. Hello!
Okay, let's move on to Jamie's topic.
Which is around Google Play SDK console registration.
**Jamie Lynch** 15:39 Yup.
**JP Jason Plumb** 15:40 Very interesting.
**Jamie Lynch** 15:40 I just spotted this old issue.
Which… Well, I guess the question is, are we still interested in doing that? And… If so, I think it's out of beta now, so it's…
**JP Jason Plumb** 15:56 Reasonably straightforward to…
**Jamie Lynch** 15:58 register.
**JP Jason Plumb** 16:01 I don't know what this is.
**Jamie Lynch** 16:04 Oh, can you give a bit of context? Yeah.
It basically gives you insight into crashes and ANRs that can be, well, associated with an SDK out in the wild, so it's kind of anomalized from Google Play data.
So, it could be useful to see if, like, we're getting crash reports, That originate from the OpenTelemetry Android library.
**JP Jason Plumb** 16:37 Oh, interesting, so this would… this would be a tool for us, it would not be a tool for end user… for… for developers, it would be a tool for us.
**Jamie Lynch** 16:44 It's primarily a tool for us, I think.
developers… can… kind of give some additional context, if I remember correctly.
**JP Jason Plumb** 16:58 Interesting, so…
**Jamie Lynch** 16:59 a way to, like, communicate with developers and suggest what they use, different versions, and…
**JP Jason Plumb** 17:05 Cool.
So in addition to, like, knowing if and when crashes happen in our… in our library, like, in the OpenTelemetry Android code.
We would also be able to find out version usage.
**Jamie Lynch** 17:20 I think it's got some… Yeah, it's got some stats on that.
**JP Jason Plumb** 17:26 Yeah, like, this would be super cool to know.
well, I don't know, maybe this is higher level than I'm thinking, but to know which versions are being… Deployed. What versions are out there in the wild doing stuff would be really helpful.
**Hanson Ho** 17:45 The… the data is kinda spotty, especially with the attribution.
But it is some data. And if it shows that someone's using it, you know that someone's using it. If it doesn't show, it doesn't mean no one's using… it doesn't mean no one's using it. So, it's… it's… having nothing.
Versus having something that's kinda… ugh? Something kinda ewh is… is better.
I think it needs, like, an email address for contacting and things like that, so, if there's, like, a generic address, we can send it so that, you know, it's not gonna be, like, on a maintainer account. It'd be rather, like, it'd be, like, the maintainers and approvers or something like that. So just set your filters. It's not that noisy at all, like… In fact, I wish it were a bit more noisy, maybe.
But, yeah, I think if we can do it, we should do it.
**JP Jason Plumb** 18:42 I think there's probably a way to get us somebody in the OpenTelemetry org. I mean, we're all in the org, but, like, to get somebody in leadership for OpenTelemetry to maybe help us do this, I mean, I could just do it, but then if something happened to me, I don't want that to be… a thing. Most of the setup and all of the tooling is not tied to specific people.
Which I think is a… it's a… it's a benefit for the project to not be tied into one person, because it distributes control and also, like, it eliminates a single point of failure. I think there was… I think there was a case where… I think some publishing secrets or some secrets were shared through, like, 1Password or another tool like that, but that was, like.
That… and that was individual-based, but it was, like, me and Cesar, and I think that was the only thing I remember being tied to a specific email address… one or more email addresses.
This looks cool.
do we have a sense of, like, how much effort it is to set this up? Like, are there instructions on how to integrate this with your… I'm assuming there are.
**Jamie Lynch** 19:54 Yeah, I… I can't remember exactly what it was.
I think… you… there's several methods. It kind of involves basically claiming ownership of a Maven Central namespace.
**JP Jason Plumb** 20:11 Okay. On tweet.
**Jamie Lynch** 20:13 eventually… Yeah, but I don't know, it might have changed since we did it.
**JP Jason Plumb** 20:21 So, I still like this idea. I think it's… I think it's smart. I think having this… I think having this data could help us make some better informed decisions about project direction.
My gut right now is I want to push pause on this for 3 months. Like, honestly, just like, can we revisit it maybe in February or March? That's kind of my initial gut reaction at 8am.
What made you think about it? Did you just come across this and you were like, oh, that would be cool?
**Jamie Lynch** 20:51 Yeah, I just kind of did a run through all the issues, went through the old ones and… thought that would be reasonably straightforward to pick off compared to some of the other ones. But there's no pressing need, really.
**Hanson Ho** 21:07 We want to spend… we might want to spend, like, an hour on this and see… see what's necessary, because if… I just imagine if we… if we said, like, look at this in 3 months, we're just not gonna do it.
One of those things that's, like, not super important, but if we don't do it, we're not gonna do it.
**JP Jason Plumb** 21:22 I mean, it's been a year, right? Like, how long has this been sitting out there? Yeah, a year and a half.
**Hanson Ho** 21:25 year and a half.
**JP Jason Plumb** 21:25 I mean, we… yes, I agree with that sentiment, so… .
**Hanson Ho** 21:33 Like, does one of us want to just take half an hour or something like that, just to see how far it goes? .
**Jamie Lynch** 21:46 Yeah, I'd be happy to take a look, but I think, I'm not too sure on how the… Getting into it.
non-individual email address and all that sort of thing will work. But I could take a look and see what instructions are needed, and maybe post them a Slack group.
**Hanson Ho** 22:05 Yeah, I mean, maybe…
**JP Jason Plumb** 22:07 I can take an action item to ask some of the TCGC people in OpenTelemetry how they handle this for other things, because this can't be the first time this kind of thing has come up.
And then we at least know how it's typically handled, and then we can decide how we want to handle it.
**Hanson Ho** 22:24 Yeah, if it just takes, like, 5 minutes to get to a block to say, hey, we need, like, you know, we need this type of… we just need an email address to log in, and we're like, oh, we don't have that, so we can't… like, if it's tied to, like, a Google Play account or something like that.
**JP Jason Plumb** 22:38 And you have to… if somebody has a Google Play account, then the first thing we have to say is, hey.
**Hanson Ho** 22:42 Does OpenTelemetry want to just create a Google Play account and have that be managed by something that's not a person?
**JP Jason Plumb** 22:49 Yeah, like, by default, even just the sign-up button just defaults to my… my corporate identity, so…
**Hanson Ho** 22:56 There you go. So, we need a Google account that has… that is an SDK, that is an Android or Play Store, eligible account.
So…
**JP Jason Plumb** 23:08 I mean, so this is pretty clear, like, we do, yeah, we own that, and then contact…
**Hanson Ho** 23:12 I didn't understand.
**JP Jason Plumb** 23:14 Oh.
Oh, somebody's got the… the robo… robo voice.
**Hanson Ho** 23:19 Google Home tried to… I said… I said the word G-O-O-G-L-E-O.
**JP Jason Plumb** 23:23 Huh.
**Hanson Ho** 23:24 It tried to… yeah.
**JP Jason Plumb** 23:30 So that Seems fine. So, yeah, these are the steps, okay.
**Hanson Ho** 23:38 So we need that.
So maybe before Jamie can even do any investigation, we need a way to create a contact that is not anonymized, but, like, decoupled from individual developers.
**JP Jason Plumb** 23:53 So, are we entirely under, I think we are, right?
**Hanson Ho** 24:01 Yes. Oh.
**JP Jason Plumb** 24:02 without that extra A.
I wanted just to make sure… I think this is everything.
**Hanson Ho** 24:13 Might be OpenTelemetry Android, is it? It's just Android, okay. Yeah?
**JP Jason Plumb** 24:18 Yeah.
I… the reason I'm hesitating is because I think we screwed this up way back when, but I think it's been Okay, and then they need the package name. Okay, so we would have to pick one of those.
**Hanson Ho** 24:39 Well, the main one is… is… is the one people… it's Agent, right? It's Android Agent is the one that people…
**JP Jason Plumb** 24:44 this one.
Yeah.
**Mustafa Haddara** 24:50 We could probably claim a couple, right? Like, if the first one turns out to be quick.
**Hanson Ho** 24:56 Well, then we'll get pinged every time, like, that module is used and stuff, so, excellent.
**JP Jason Plumb** 25:05 I'm gonna… I'm gonna click this and see.
Hey! So all that's doing is saying, nobody's claimed this one yet, okay?
Don't let me finalize this.
I'm not trying to finalize this.
Okay, so you need this.
With a verification file included.
I'm just gonna screenshot this.
Okay.
And if other people have agenda stuff, feel free to jump in and tell me to stop this silly exercise, but it's kind of exciting. So, there is a verification file. Okay, we get that into our artifact, and then we publish the next version.
**Hanson Ho** 25:56 Makes sense.
**JP Jason Plumb** 25:57 Or they… they create a verification file, and we download it. Is that… what that is?
**Hanson Ho** 26:03 Yeah.
**JP Jason Plumb** 26:03 Okay.
Then we unzip it into the SDK parent folder, it goes like that… Build, publish… Make sure it gets out into here, okay?
wrong repository, kind of, after the Maven Central… Sonotype Central snafu stuff, but okay. And then check your email, and they will… Verify ownership within 7 days. Okay, well, that seems to definitely be tied to a Google account.
You know, we use… we, OpenTelemetry, uses Google stuff all over the place, like, for the calendaring, so someone, somewhere has an account that may not… be tied… you know, to their personal or corporate identity, so… I'll take that as an action item to ask about.
**Hanson Ho** 26:53 Yeah, if we use, like, GCP and stuff like that, surely it's not tied to, like, an, like, you know, someone's personal account.
**JP Jason Plumb** 26:58 Yeah.
**Hanson Ho** 26:59 Or corporate account, even. Especially not corporate account.
**JP Jason Plumb** 27:11 Yeah, the answer might just be, no, you're a maintainer, you do it, but it would be cool to not be the only one. And if I claim it, and something happens to me, you know, what… like, that green checkmark for verify ownership, or eligibility, rather, will no longer be there, presumably, right? Like, if… If I claim it and something happens to me, I don't want it to get stuck.
Great.
**Hanson Ho** 27:34 Yeah.
**JP Jason Plumb** 27:39 I can't go backwards in this workflow. I don't think so.
Anyway, okay, that's cool.
Yeah, it seems useful.
I'm definitely curious.
Have people used this on other projects?
**Jamie Lynch** 28:03 We've used it on embrace a little bit.
**JP Jason Plumb** 28:05 Yeah.
**Jamie Lynch** 28:06 But, you know… Data we didn't find helpful at all, but it was useful for crashes.
In that, I guess, it alerts you when there's a new one over a threshold.
And… You can see the known ones as well.
But in practice, we don't tend to see that many.
**JP Jason Plumb** 28:32 And do you get a sense of how they determined that the crash was in your code?
**Jamie Lynch** 28:40 I think it's basically introspecting stat traces.
Okay.
**JP Jason Plumb** 28:46 And looking for packages.
**Jamie Lynch** 28:47 Yeah.
**JP Jason Plumb** 28:48 James, okay.
**Hanson Ho** 28:50 And that's where the data becomes a bit, you know, hey, this is technically in our code, but it's a wrapper and pass-through, and… it's actually… the original call is some stupid network call that decided to do some stupid things in handling the response, and it crashed, so yeah, but it's wrapped around your interceptor, so… Good thing it's not THAT noisy, like, it's not so, you know, we're not, like… Getting things that we ignore all the time, so…
**JP Jason Plumb** 29:19 And then interfacing with the console, is it mostly, like, you go there and read stuff, or do they push you emails as well? They give you alerts as well when stuff happens?
Like, is input versus pull, or is it hybrid?
**Jamie Lynch** 29:34 A bit of both.
So, you could proactively go to the console and, like, check All the metrics and see what version usage is like, or you could just get emailed when new crashes occur.
**JP Jason Plumb** 29:47 And then, because I am learning about this in real time, what's the developer experience with this? Like, do they have to enable it or allow it?
**Jamie Lynch** 30:00 I think… The government… from the perspective of a developer who's included an SDK into their app, any stat trace is kind of anonymized, well, to the best effort they can have, so… So, basically, it'll just, kind of… They'll try and anonymize, like.
Stack frames that are specific to, like, a given app.
But common, like, libraries or Android framework codes, they'll still show up as static frames.
I guess what I'm asking is, do… do developers that are, building and releasing apps, when they… if…
**JP Jason Plumb** 30:43 If we did this, and they were incorporating open telemetry.
Is there a way for them to opt out of us being able to see their data? And by their data, I mean our data, but from their app.
For whatever concerns. If somebody's, like, super, privacy or security, focused.
Can they opt out of it, and… or do they have to opt into it?
**Jamie Lynch** 31:11 That is a good point. I'm not… entirely sure. I would have thought that it's related… to, whether you opt into diagnostics to Google Play, and kind of based off that, but I wouldn't take my word for that, we should check that.
**Hanson Ho** 31:31 Yeah. Also, similar caveat. I don't think this collects new data, so this… Google just gets this data from… from, from their various backdoor means. I think, this… and so… and the consumer… it's up to the consumer to opt in or opt-out. And when… when the data is received, I think it just… it just gets exposed in our developer console. So if… like, I'm not sure if apps have the ability to blanket, say, don't report this stuff to Google. If there is, then it is outside it… there are other SDKs that they're using that are getting this data, probably, so it would be… you know, unless there's something about specifically us, like, I don't know if the granularity of opt-out goes down to, like, SDK, an app and user, like, an instance.
So, it might be good to do a cursory check, but, I don't know if they'll provide this information, but we certainly can look.
**JP Jason Plumb** 32:38 Okay.
Cool, yeah, that's all… that's really helpful to me. I think this is, I think it's worth… worth trying.
I still want to stay focused on our 1O release.
But I can take an action item to do that.
And also, Jamie, you mentioned that you came across it as you were going through the old issues. That's been super helpful, thank you. I've definitely noticed that. It's been awesome.
There are a bunch now that have, I think, needs author feedback. It's great.
Awesome.
Good triaging, helpful, thank you.
We have kind of fallen off the end of the agenda. I will add one, though. What's… Because I think this is… I saw this yesterday, and I wanted people's opinion.
Let me find the change, because there's a… somebody submitted a PR for this.
This one.
So the issue that they themselves filed Is that when you are not connected to your carrier's network, You don't get this information.
And they were saying, that information is always there when you have a SIM card plugged in, and why are we not including this data? It's very valuable, useful tracking data, when they're, like, on Wi-Fi, for example.
And then they submitted a PR to make that change. It's a pretty small change.
And I… it's… I… I can't remember why we did it this way originally.
Other than it's some extra data that's not super relevant. In other words, like, knowing who the carrier for the SIM card is at the time that you're doing random stuff on Wi-Fi may not be that helpful.
But I guess this person finds it helpful, so I'm curious, first of all, have people looked at this PR? And if you haven't, please do. And then if you have, or if you're understanding, like, in this very brief description what this is about, do you think it's like, potentially a good idea. Should we always do this, or should we make the user opt into it?
**Hanson Ho** 35:00 So, I think right now, this information is… Is on network instrumentation, right?
**JP Jason Plumb** 35:06 It is.
**Hanson Ho** 35:06 If you're, if you're, you know… so that particular connection, it's going through this carrier.
**JP Jason Plumb** 35:12 Yes, by way of services, though, right? We have the… Yes. Yeah, okay.
**Hanson Ho** 35:17 But, I mean, our service is just… our abstraction of getting this data into the network,
**JP Jason Plumb** 35:25 I think the only… oh, actually, that is… hold on.
Is it part of the global attributes appender?
I think it's part of the global attributes appender, but you only get this data if you've opted into the network instrumentation.
**Hanson Ho** 35:43 Okay. Think, I think.
Okay, so if it's global, then it's even, I think, more… even weirder, to say our network connection is Wi-Fi, but somehow we're putting carry information on there, because what are we supposed to actually understand that we're making network requests right now, and there's carry information, but we're going through Wi-Fi. What does… the network, or the SIM card you're attached to that is not active, have anything to do with anything.
**JP Jason Plumb** 36:15 So they, they somehow managed to write their use case about this, so they think that it's useful.
For mobile apps that primarily use Wi-Fi, but need carrier information for analytics. That, to me, just smells like tracking.
Enterprise applications, tracking device context across different network types, I'm not… it's a little bit vague.
Because this is not really device context, it's network context.
**Hanson Ho** 36:45 Nope. Yep.
**JP Jason Plumb** 36:46 Consistent telemetry data regardless of connection type.
**Hanson Ho** 36:50 That's… this is consistent. The carriers know. So the…
**JP Jason Plumb** 36:55 Well, it'd be missing, yeah, but… so the fact that it shows up on some spans and not on others, I think, might be confusing, but…
**Hanson Ho** 37:01 But it's an optional, right? Yeah. You know, so I think by the semantic conventions, that is correct. The second one, it's not the responsibility of the applicat… or of the agent to report previous connections. You can also switch SIM cards. You can have dual SIM. So what happens if you have dual SIM? Like, do we track, like, a list of, last active, you know, carriers?
And, and for the first one, What this would be, would be, previously connected, connections, or, or, or networks. And if… And there is a privacy thing here, because if you're… only going through VPN to access some corporate data, and then previously, on your… when you're not using that VPN, you have some information that is effectively not about the session. If your app wants to track it and say, hey.
Cool, I want to track my last 10 carriers.
And then you want to report that, that's your prerogative. But I think as the agent.
we shouldn't do that. And if they care about that for their telemetry and want to track it for their use case, they could certainly, get this information. And now, if the question is, can they get the service information in their code.
The answer is probably no, in a public API.
But they can probably still get it by including the relevant modules and things like that.
So, like, I… My… my first kind of reaction is… This is stuff they could do themselves, and… to do it at the agent level feels a bit icky, especially of the privacy implications and utility, or general utility.
Yeah, that's crazy.
**JP Jason Plumb** 39:02 Yeah.
**Hanson Ho** 39:03 I can comment on this as well.
**JP Jason Plumb** 39:05 Yeah, that's always helpful.
Curious about other folks.
And that, I mean, it's cool if this is new to you and you haven't thought about it, but…
**Jamie Lynch** 39:24 I can't see myself wanting to capture this level of detail, just due to… Yeah, the potential privacy.
Like, implications.
**JP Jason Plumb** 39:36 Yep.
**Jamie Lynch** 39:37 At least not by default.
**JP Jason Plumb** 39:39 I'm also trying to put my rum hat on pretty tight, and be like, how does this help the rum experience to have this information? And it kind of doesn't.
It definitely seems way more for tracking, and I can kind of see the consistency argument, but it's at the expense of just more data.
**Hanson Ho** 39:58 do they want us to write an attribute with null ? Like…
**JP Jason Plumb** 40:02 No, OpenTelemetry will not allow that.
**Hanson Ho** 40:06 Yeah, so… I, I… I think… I think the data is correct. There is no… there is no carrier. It's a Wi-Fi. And I think there's also an abstraction problem, like, what are they tying this to? It's… it's effectively past connections. By definition, it's not the current connection.
And how many… how many past connections do we want to track in terms of carrier? And do they want, you know.
**JP Jason Plumb** 40:30 Yeah, like, we don't… we don't report, like, Wi-Fi hotspot name or anything like that.
**Hanson Ho** 40:35 No.
**JP Jason Plumb** 40:35 I don't even know if that's available, but we don't report it.
And I kind of see your point. There's, like, maybe some weird… asymmetry there. Like, you're reporting stuff about… like, these are network-based, I mean, network carrier… Okay, yeah…
**Hanson Ho** 40:53 they can get all this information themselves, is the thing. Like, if they really care about this, they can get this information themselves, stash it, and report it as a, you know, in a global attribute appender. Nothing's stopping them from doing that. It's just the agent is… it's not the right place to do this information, because.
**JP Jason Plumb** 41:12 Yeah.
**Hanson Ho** 41:13 We don't want a history of connections of this instance.
**JP Jason Plumb** 41:18 Okay.
**Hanson Ho** 41:19 I'll comment, I'll put all that, like, directly.
**JP Jason Plumb** 41:22 I mean, I'm happy to comment too, I was just… I saw this late yesterday, and I was like, I wonder what people think about this, like, am I the only one that thinks this is maybe a weird idea?
And… I'm not convinced that we want this yet.
**Hanson Ho** 41:36 I'm convinced we don't want this. Okay. At the agent level.
If they have a use case, go right ahead and do this.
Like, are they trying to, like, track… I mean, I think the reason the use case is fairly generic, they must have a specific use case.
If they want to find oscillation, or network drops, or transitions, and they should detect transitions, like, there's… Yeah.
**JP Jason Plumb** 42:14 Yeah, I mean, I appreciate that they took the time to put this use case in here.
Yeah, they're describing how we go about it.
No additional permissions… Okay.
Well, no, if there's no other opinions on that, we'll just kind of assume right now that we don't think it's super compelling, and maybe they can give us some additional… Information about why it's helpful.
**Hanson Ho** 42:44 Honestly, it would be confusing, but anyway, we've talked enough about it.
**JP Jason Plumb** 42:48 Yeah, as a maintainer, I'm, like, always a little hesitant to just say no, and as the project grows, I mean, there has to be more of that. Sadly, it's just the reality, like, there's gonna be ideas that don't fit in with what we want to build, and it's gonna have to be okay.
**cleverchuk** 43:07 Question.
**JP Jason Plumb** 43:09 Yeah, Cleverchuck.
**cleverchuk** 43:11 So, does the API allow them to, like.
Have that data in there without putting it in the agent, so can they write a code?
That the agent can grab and add that for them, without having to add the code into the agent.
**JP Jason Plumb** 43:30 I'm not sure I followed your question.
**cleverchuk** 43:33 It's like an extension, and they extend the agent without having to put the code in the agent.
**JP Jason Plumb** 43:39 Yeah, I mean, I think that's Hansen's point, is that they should be able to gather this stuff themselves manually if they want to, through the telephony manager.
**Hanson Ho** 43:47 And they could use a global attribute appender, or put it in their specific, you know, span or log or whatever. So, as if it's custom. I mean, it is custom. This is kind of like, you know, the thing that they want, so…
**cleverchuk** 44:02 So maybe we should probably just add that, tell them to, like, take that approach.
**JP Jason Plumb** 44:07 Yeah, like, a response that gives them specific guidance on how to do it might help on this.
**Hanson Ho** 44:12 That's huge.
**JP Jason Plumb** 44:12 I mean, it doesn't resolve the PR, but, like, on this issue, you could say, hey.
you can… you yourself can provide a global attribute supplier, I think, and the supplier could source this stuff from the telephony manager.
**cleverchuk** 44:29 Yeah. True.
**JP Jason Plumb** 44:30 I think that's true.
Yeah, I think that's smart to, like, the response including.
specifics on how they could do it, and not necessarily rely on the app to do it. On the agent to do it.
Okay, I have another topic, and oh, holy crap, it's already 45.
Alright, so this happened in instrumentation.
Recently.
And I'm curious what people think.
Let's see, is it… The pull request template… Oh, I don't have any… let's see, I'm just… It's not that template, maybe it's an issue template.
Maybe it didn't get merged yet, or maybe I'm just… Completely confused, let's see. So, what I'm getting at is there was a pull request that… When and I thought yesterday… Instead of merged.
I thought it was an instrumentation.
Okay, I'll find the… I'll find a way to get there instead.
We'll go to… here… So, I have a PR that's open in the community repo that, supplements some of the existing language around the guidance for using Gen AI to submit issues and pull requests, and if I can summarize the whole conversation happening over here is that I think, we should set an expectation that people submitting issues and pull requests disclose openly, that they use these tools to create a large amount of content for our repo, and there's some pushback, and the pushback is reasonable, but I disagree with it. The pushback is, I think developers don't… this is not me speaking, this is someone else speaking, That developers don't, or won't have the expectation that they should disclose it, and that we should ask them, and then they should respond with a yes or no.
And… One of the ways to handle that asking for this is with, here it is.
**Hanson Ho** 47:17 Templates.
**JP Jason Plumb** 47:17 an issue template, yeah, so I'm curious if we want to, if we think it would be a good idea to adopt this kind of thing.
The… the… the… I… I balk a little bit because… To me, this puts a wall of text in front of every person who's trying to submit a pull request.
And it looks like it had not been merged, which is why I was confused. I thought it has a bunch of approvals.
So, it's something to consider. I'm just gonna put it in the notes so that we can think about it.
**Hanson Ho** 47:51 I think a PR template is actually a good idea, Because it gives an idea of what we want folks to put in, in terms of, you know, the reason for this, etc, etc.
If we want to reduce the wall of textness, we just reduce the number of things that we ask, or perhaps, you know, have it fairly open-ended, so maybe just a couple of sections. And if we have that, then having a disclosed Gen AI yes or no would be fairly reasonable, I think.
**JP Jason Plumb** 48:25 Okay.
I mean, one of the things that prompted this, some of you have probably already seen this interaction, I think… yeah, so this thing… I added… I added this, this pretty cheeky label that you might have seen, and it's because of this, PR. So… And this PR did not mention the issue that it was resolving. So, like.
I don't know, a year ago.
I file an issue that was very brief, it's just like, we're using an old version of Jaeger, and for some reason it's not being bumped up by Renovate.
We should address this. And this person, decided to tackle that issue, and I'm like, great, help wanted, we love it. But for what I thought was a pretty, small change, there was a lot of content, in addition, like, there were also these, like, extra markdown files being committed about this stuff, and like… You know, clearly not something that we would want to maintain, and it's just like… like… tons of, like, descriptions, like, this is, like, a maintainer's burden, right? And so… If this was disclosed, or if this label comes up automatically, or if there's a template or something that sort of helps, the curators of a repository to know in advance that this is gonna take some additional handholding or some additional work, then at least we know that up front.
And, I mean, they're cool, like, they disclosed that they used some sort of tooling, they used Copilot to help create that, but really, it was… more than 600 lines of code that got submitted originally, and it ended up being distilled down, and what got merged was a single removal and a single addition, so one line of code changed.
And that kind of stuff is probably going to continue happening.
So, that's why I wanted to bring up this PR and what we think about it.
I don't love it, because of the reasons I said.
But it might be necessary.
**Hanson Ho** 50:35 You don't love the template, but you love…
**JP Jason Plumb** 50:37 I don't love… I don't love the template, because… I don't have a contrived example, but, like, when you go to create a pull request, being able to just, like.
give your nice little description is so much… so much better than having, like, this form to fill out. Like, we've all submitted PRs on repos where it's like.
there's a form, and it's like, did you update the changelog? Did you do XY? And it's like, you're… you have to go… like, even in SEMCOMF, like, you have to go through so many steps to even get that PR submitted. And… I mean, some of that's intentional, I assume. Some of that is to, like… Slow it down because it's too wild.
But I don't think we have that problem yet. But if we continue getting like, huge… AI-generated PRs that provide, you know.
Questionable… questionable benefit, then we… we might need something.
**Hanson Ho** 51:31 What… what if we just had… a block for description, another for Gen AI, disclosure.
**JP Jason Plumb** 51:40 Yeah, like, maybe take this and distill it down, like, something about…
**Hanson Ho** 51:44 literally just what we had before, like, a blank text box, put that in description, and then second section is, did you use GenAI to create the bulk of this? Or have some sort of, you know, because if you use Grammarly to, like.
you know, rewrite a block of text, that's not the problem.
**JP Jason Plumb** 52:07 I know, that's, like, some of that, philosophical comment stream happening in my other PR.
**Hanson Ho** 52:15 It's like, PR's… like, AI is everywhere, you're not gonna… everyone's not gonna disclose it, because it's always yes, and it's like, that's kind of not…
**JP Jason Plumb** 52:23 what we're talking about. We're talking about… Did you… did you use tooling to write the bulk of this PR? And you think you reviewed it, but did you really? That's… that's what I want to just ask every PR submitter.
Okay, so what I think I'm… what I think I hear you saying is, like, maybe there's a way to distill it a little bit.
**Hanson Ho** 52:44 Just have two boxes, you know, right? Anyway, and the other one is… I don't know, I have to word it somehow.
Like, the code itself, I, like, that's the part I trust AI to do.
you know, better. It's… it's that… that… all those markdown files that you created, that was created, and all the… all the fluff, clearly, they're not useful, or it's not useful enough to commit, and you, as the person submitting it, should have deleted that before submitting it.
**JP Jason Plumb** 53:18 Yeah, like this, for example. Like, it's a markdown file that describes.
**Hanson Ho** 53:23 Oh, yeah.
**JP Jason Plumb** 53:24 Yeah, like, no one wants this.
**Hanson Ho** 53:26 Oh my god.
**JP Jason Plumb** 53:28 Yeah.
**Hanson Ho** 53:29 Although, no, the…
**JP Jason Plumb** 53:31 I know.
**Hanson Ho** 53:32 Holy crap.
**JP Jason Plumb** 53:35 Yo.
So…
**Hanson Ho** 53:41 Just… edit.
**JP Jason Plumb** 53:43 what your AI generates, right?
Yeah, I know. Okay. Well, we're basically at time.
And once again, it got away from me.
Looking at the calendar, so I'm also taking some time off for the holidays, which you can't see my calendar, but I can.
So today's the 9th, next week is the 16th.
I am volunteering that day, but I will come and run the SIG that morning, so… should be fine for us to meet then.
And then the 23rd… I'm not sure what the community is doing that week.
I'm off, but I can also, if people want to show up, on the 23rd, let's decide that next week.
**Hanson Ho** 54:33 I feel like there's gonna be a ramp down of activities.
**JP Jason Plumb** 54:37 I feel ya, it's already happening.
**Hanson Ho** 54:39 Yeah.
**JP Jason Plumb** 54:41 Cool. Alright, everyone, well, I appreciate you.
Thanks.
And I'll see you next week.
**Mustafa Haddara** 54:49 But…
**Hanson Ho** 54:49 Bye.
**JP Jason Plumb** 54:49 Baby.
