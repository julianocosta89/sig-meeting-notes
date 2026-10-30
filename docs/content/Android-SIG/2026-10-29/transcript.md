SIG: Android SIG
Date: 2026-10-29
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Cesar Munoz** 06:58 Hello, David.
**Jason** 07:22 Hello.
These are the wrong glasses.
Okay, that's better.
**Cesar Munoz** 07:35 You know, I don't know what's the background you have, Jason, but it seems… Like, it may come from a horror movie, I don't know why.
**Jason** 07:44 Yeah, yeah, lucky, lucky guess.
It's from The Shining.
**Cesar Munoz** 07:48 Oh… Right.
**Jason** 07:52 Yep.
One of the classics.
**Cesar Munoz** 07:56 I see.
**Jason** 07:58 It's the season.
**Cesar Munoz** 08:02 Oh, that's true.
**Jason** 08:09 Do you… do people in Spain celebrate or do anything for Halloween?
**Cesar Munoz** 08:16 Well, I… I mean, I've seen some stores that are decorated, but… Like, the same way… They seem to do so there, in the States? No, I don't think. Yeah. No.
**Jason** 08:33 Well, yeah, it might be, like, a… pretty uniquely American thing, maybe?
**Cesar Munoz** 08:40 Well, I mean, they do celebrate other places, but I think in America, it's the biggest.
Probably… Yeah.
**Jason** 08:49 Yeah, and I mean also, like, just, like, trick-or-treating on the night of Halloween.
I know they have similar stuff elsewhere, but yeah. Okay, pretty light agenda today.
Let's give it one more minute, just because I'm gonna have a sip of coffee.
**Cesar Munoz** 09:09 Sounds good.
**Jason** 09:32 Alright, let's talk about this, PR.
**Cesar Munoz** 09:37 Right.
That's my PR, so…
**Jason** 09:44 It's the only thing on the agenda.
**Cesar Munoz** 09:47 I think… I didn't add it.
My guess, it's… that's probably Jamie.
Added it there.
**Jamie Lynch (Palo Alto Networks)** 10:02 Didn't either.
**Cesar Munoz** 10:03 because I think.
**Jamie Lynch (Palo Alto Networks)** 10:03 But we can discuss it.
**Cesar Munoz** 10:05 Right.
Yeah, I didn't say you're there, Jamie.
**Jamie Lynch (Palo Alto Networks)** 10:10 Yeah, just dropped in.
**Cesar Munoz** 10:13 Nice, so… so yeah, it's… it's just that there's… there's some feedback that I think… Jamie wanted to… cover in the… in the SIG, so… I don't know if you wanna… Explain it, Jamie, or should I…
**Jamie Lynch (Palo Alto Networks)** 10:34 Yeah, so I just wasn't sure on the need for a dedicated API extension interface, rather than just defining an extension function.
**Cesar Munoz** 10:50 about the linkage. Thanks.
**Jamie Lynch (Palo Alto Networks)** 10:51 Yeah, I call it an extension function. So… I'm trying to remember the… Exacts.
**Cesar Munoz** 11:02 That's a while ago.
**Jamie Lynch (Palo Alto Networks)** 11:04 Yeah, it was a while ago now, but… Yeah, I, Yeah, I think… Part of me was just wondering why we needed the interface, particularly as it's just a marker interface right now.
**Cesar Munoz** 11:30 Yeah.
**Jamie Lynch (Palo Alto Networks)** 11:33 Is the intention that we'd, like, add extra things onto that interface, or…
**Cesar Munoz** 11:41 Well, well, right. So… Okay, just to put… to put the… Things in perspective.
So… Because of the… comments that I've seen going on regarding maybe adding some manual APIs to… set what the current screen name is, for example, or… Start… well, start a new session.
And, and, and… And even, I think, at some point, we even discussed maybe adding a method so that users can tell the SDK that some Android permission was granted, or something like that.
Or things like that. Like, like, like small… like, manual.
Ways for users to tell us something.
that… I guess… Ideally.
should all be part of the one thing that we give users, which is OpenDelemetry ROM.
But we cannot add everything.
There, like a, you know, bucket of… Yeah. Anything?
So… I was trying to find this kind of, like, I guess, middle ground, where… We still allow for some optional APIs to get accessed via the OpenTelemetry ROM instance, but without having to be part of the OpenTelemetry ROM API itself.
And so… the use case right now that I'm… the reason why I created the PR, Because at the beginning, it was just, A proposal?
is because there is a PR from Vish, Is this one here?
**Jason** 13:54 No, it doesn't look like it.
**Cesar Munoz** 13:57 I think I linked the PR in the description, but essentially.
So it was trying to create a way for users of the agent To allow… to create a new session.
Or to kind of force our session manager to start a new session.
The thing is that our session manager is private.
And it's the way that we decide to handle sessions only in the AIS itself, or opinionated session provider.
So… like… This is some kind of, like.
Pinch of flexibility that we could provide to users.
So that they don't have to… Create their whole session manager from scratch, but still use what we provide, and then tweak some things, And that's why I created this. EssentialLink.
the thing is that… Based on that example, and also the example for the current screen name.
It seems to me that we might need these kind of optional extensions, A lot in the future, at least I know of these two right now.
And I wanted to have, just like with… instrumentations.
Like a… like a structure to it. Something that is easy to… I guess.
even ask an agent and say, I want to add this extension, and then it knows that, okay, there's this API, there's this process, there's… He provides for some sort of… structure, I guess, order. There's a lot of things that we can control about this.
maybe even the future, we want to extend this API, To allow for, like, a hook that tells when the underlying… Agent instance gets closed.
So that it no longer does whatever it's supposed to do as an extension.
Things like that. I mean, we can… we can kind of control and… and… Yeah, I guess control is a big part of why I like the idea of having our own thing. I mean, there are other, in my comments.
There are other reasons that it might be nice to have something like this, one of them Which probably doesn't have much weight, I know, but that it's, like, easier to use this kind of stuff from within a Java source.
and other stuff. But the point is that, to me.
well, actually, the case of, which I… which I think is actually a bit reason to have our own thing.
the case that Ishwan is trying to address.
Is something that requires the extension to hold the session manager, in this sense, in it. So, some kind of state that The thing about conflict extensions, is that the way I see them is that they… allow you to do, in a much more convenient way, what you can already do with the public API.
So it's not like it enables stuff that the public API cannot.
It just makes it, like, puts it in a nicer package.
Because at the end of the day.
My understanding is that really what it does is create this… it's really… it's essentially syntactic sugar. It creates this… static function.
That has the instance As the first argument to it.
So you can only access the public stuff that that instance already provides, so this also provides a bit more of a flexibility, like a real extension of the API itself.
So, I guess these are the reasons.
But yeah, I also, after thinking about it, This week.
Like, I don't see these two things as… Overlapping, or… I guess, clashing with each other.
I mean, we can… this could be, like, the underlying mechanism That we use.
From a coupling extension, if we want to make things, like, even more… nicer, I guess.
But, like, just extensions alone.
To me, it's like… it's really just intact, sure. And in this case.
I… I don't know. I mean, of course, it's possible you can probably put the session manager instance into a static, I don't know, cache, something.
So that you can access it via, you know, the catering function, but… but… I wouldn't be… Yeah, I would be worried about, you know, using that as a system to anything that we add on top. So, yeah, I guess those are my reasons.
And sorry, Marius, I see that you've been… Maybe around there for a while.
**Marius Constantin** 19:13 I'm just looking at your code, because I never looked into this PR, because for me, Kotlin extensions are new, so that's… I've been… I've been resting in Kotlin.
But… Well, I have a question, because we kind of had the same problems in Datadog realm a long time ago, and we had to introduce things like this, decorators. What you want in the end is decorators for things that you want to decorate, in a way.
But my question is, like, where do you want it to happen? Because there's two… options, and two solutions for these options. Like, do you want to happen at the runtime? Meaning, in a way, like, runtime, like, when you create the event?
When the event is already created and sent into the pipeline.
Because in data, what we propose, in order to decorate your event, it's a mapper, like you have for, for spans, if I think correctly, where you have a decorator, so you intercept the pipeline.
If you want, with a mapper, and you add your own data on top, or you… Replace some of the data in the event.
If you want to. So, for example, for a view name, if you want to change it from the one that we propose automatically, you'll have to intercept the event, figure out the view name that you want to, like, with a regex or something, and change it just in there.
It's not very nice, but more flexible, because you can actually decorate any type of property in the event, but yeah, this is the question, where do you want it to happen? Sometimes you want.
**Jason** 20:45 Yeah, I think… hopefully I can provide a little bit of clarity. It's like, I think this… these two approaches and these two PRs that we've been looking at are at a higher level of abstraction than actual dealing with telemetry. Like, they are… they're more concerned with the machinery of the agent internals, and how it operates, versus just, like, patching up or mapping telemetry on the way.
**Marius Constantin** 21:07 Yeah, yeah, that means… that makes sense in that case, because you want to control the instrumentation part.
**Jason** 21:13 Yeah.
I mean, coming back to Jamie's original question of why do we need, or what's the purpose of… I think you were questioning the existence of this interface.
**Jamie Lynch (Palo Alto Networks)** 21:24 Yeah, basically, I think… Currently, where… Service loading, an empty interface.
**Jason** 21:33 Yeah, exactly. So this serves only for implementations which are extensions to have a shared common interface that can be loaded uniformly. But it looks like, and I hadn't reviewed this PR, but it looks like there aren't any examples of this yet, are there? Maybe in the test?
**Cesar Munoz** 21:52 There's some tests, but yeah, I would say the really… real example is the PR from… from each one.
**Jason** 21:58 Okay, and what, Jamie, without this interface, would you… is something that you're proposing or thinking as an alternative not include service loading?
**Jamie Lynch (Palo Alto Networks)** 22:09 So… I would suggest… Maybe we just… base it on OpenTelemetry one for now, like the interface. I think if we need to… access internals, one pattern we could use is have the underlying SDK instance.
implement some… Like… internal API that's in a separate module, and then we could cast to that within Like a session… Yeah, within my procession example.
Potentially.
**Jason** 22:48 Yeah, which is not… it's not dissimilar to what Java does.
And upstream.
I will… so I don't wanna… I don't wanna derail this, I think this is really good work. I will just share my, two cents, little bit of a hot take.
I think… Extension functions are very… convenient, and they can make things kind of nice, but I think they're also very… dangerous in that they muddy clean interfaces, and you can see someone's code, and then you go and look at the implementation, and you can't build it yourself, and you have to track down where these things came from, right? If you see an example.
With this code that you don't realize has extensions applied to it somewhere else, no one knows where, or how they get sourced, or how they get applied.
And you see this thing with all this, like, extra functionality, and you just… it's really… it makes it really unclear where all of that stuff came from.
So I would like to encourage us to try and use them somewhat sparingly. If there is, you know, if the intent is for these extensions to be short-lived and eventually make their way, like, graduate or mature into proper interfaces, then that's great, but… what I don't want us to have is, Just a pile of extensions that… Make our interfaces no longer opinionated or kind of uniform?
**Marius Constantin** 24:24 What do you think about providing plugins? One of the ways we do it is, like, whenever… so, for example, take an example when you're in ROM and you're trying to… I don't know, record your screen events, or stuff like that. You have… you extract that part in a, you know, let's say a component for which you can provide an entry in your SDK it's in the ROM SDK Builder configuration, and you're allowed to actually plug in your own implementation, and Which is going to replace the default. So, this way, you identify the places where you need to actually plug in your own implementation, and you allow flexibility from outside.
That could be an idea.
**Jason** 25:08 I think that that approach is pretty well aligned with some of what we already have.
In the air.
**Cesar Munoz** 25:14 Gotcha.
**Jason** 25:15 API.
**Cesar Munoz** 25:16 Athen, Athena, actually, the blogging idea is kind of like what I'm trying to propose with this PR.
Yeah. The… the… Yeah, yeah, and I just wanted to add on what you said, Jason, about Kotlin extensions.
**Jason** 25:34 Sure.
**Cesar Munoz** 25:35 I do… I do find them very… Nice.
But yeah, also kind of like a double-edged sword.
**Jason** 25:44 Yeah.
**Cesar Munoz** 25:44 So, for example, and this is a… this is a real example, I remember once I was taking a look at a code, where… they had… it's an Android app, and they had a single screen.
Where they have a registration form.
And part of the registration form, you have to set a password for your new account.
And they wanted to validate that the password Had a right format.
And I remember saying that somebody created an extension for the string class.
that read, is this a password, or is this a valid password? Yeah. So every time you created a screen.
Anywhere else in that project, and you press, you know, the dots to see what's available for that.
**Jason** 26:39 You wanna see that?
**Cesar Munoz** 26:40 this is a valid password function, and it's like…
**Jason** 26:42 hamburgers.
**Cesar Munoz** 26:43 incredibly silly.
And it, it, it's, it's… again, but it's so easy, so it's, it's, it's, it's easy to… to… it kind of reminds me of the, the old, kind of, like, utility… utilities pocket, anti-pattern that… I know that I felt poor when it was starting to program.
where everything that I wanted to help me with the code, I will add into this single utilities class.
And that will grow up to the point where other developers will… will miss that there were some alternatives already there, and they will re-add them in another way, so it was… all over the place, so I kind of see… That kind of issues.
to be possible with Kotlin extensions, if not, If not used, you know, I guess, correctly.
So… so yeah.
I wouldn't say it's a hot take. Well, probably.
But at least to me, it makes sense.
**Jason** 27:51 So, I think we've identified… so, your PR here is somewhat generic, meaning it's providing a… scaffolding upon which other things can be built, right? Like, you're providing a foundation here where anyone can build extensions, and the two extensions that I think have been kicked around a little bit so far is… one is, like, dealing with sessions, and one is dealing with, maybe, screens, right? Those are the two that we've identified.
And I would say… where my mind goes is, wouldn't it be better for us to have like, very explicit, opinionated APIs for those two concerns, because they are such core concerns to a lot of implementations. Like, why not have those two things be first class.
Customizable, configurable components.
**Cesar Munoz** 28:40 Yeah.
**Jason** 28:41 kind of… and we are kind of, like, halfway there already. Like, we have a bunch of stuff around sessions, we have a bunch of stuff around screens, it's like, we're just missing a little bit of extra customization, it sounds like.
**Cesar Munoz** 28:54 You mean, like, just to make sure I understand, to, like, add… to open sedimentary ROM?
like a start a new session function, and then setScreenName function. Something like that.
**Jason** 29:09 So this is… this is our… this is our main interface, right? And we're… we're a little bit precious with it, and I think we need to be, like, delicate with it, and not treat it like a kitchen sink.
But maybe through the builder, there can be some… ways of customizing those components, yeah. I don't know that the methods for setting the screen name or, like, rolling the session over, I don't know that those necessarily need to be on this interface.
But when building it, perhaps there's still a way to add customizations that don't expose it on its interface.
**Cesar Munoz** 29:45 Holo.
Probably. I mean, the thing is that when it comes to public API, I think… I mean, it's fair, and probably we can go this direction.
By the way, this is an option, again, as I mentioned in the previous proposal PR.
one option.
Probably address issue.
But now you're mentioning another one. I think it's fair. I… I see the public API around OpenTelemetry wrong.
in my mind, as… in two different… like, two different categories. One is… the public API to configure it, like, to… to build it.
And then the public API after it's built, which gives you, like, triggers to do something about telemetry at the moment. So, so, it's not about configuring stuff, it's about, you know, actioning stuff.
At runtime.
And in the case of these two… like, I see it… Possible that you may… At configuration time, at build time.
Probably set, an object that Like, you will have to… by the way, for starters, it's an object that you will have to… Like, keep it yourself somewhere accessible to you.
that… After everything gets built, you can, like, interact with it.
to provide something.
That's possible.
I will argue that's less… Nice.
if you will, than just having some sort of method available from the OpenTronometer ROM object itself.
So, so… But it's… but it, yeah, it could work.
That's an alternative.
**Jason** 31:54 Yeah, I'll respond to that real quick before… having Marius chime in, just because we're on… we're riffing on the same… same topic.
So, with those two things in mind, right, you could… like, we've talked about maybe instead of just exposing the getter for the session, which is effectively what this is, we could also instead relax this, and next to it also provide the session manager, or the session controller, I don't… I mean, we have a session manager, but something that will allow you to both get and roll over the session.
Right? We don't… that interface doesn't exist, but if it did, you know, we could put that on here and deprecate provider, like, that's fine.
And then, as far as screen name, it would be maybe one other method on here, which is, like, setCurrentScreenName.
And those… that doesn't seem like a… like an unreasonable expansion of API surface to me.
In fact, we've been hemming and hawing around these for so long that I think adding them… I think the fact that we've talked about these and they've been on our radar for such a long time means they probably weren't… Now, kill…
**Cesar Munoz** 32:56 They don't consider it.
**Jason** 32:57 but consideration for adding. Go ahead.
**Cesar Munoz** 33:00 That's true.
And for these use cases, that's something that we could do. Actually, with Session Provider.
I would argue that… just by turning our session manager implementation public, That will already… enable the use case that you mentioned without having to touch this interface, because people essentially can just cast.
the session provider to it, and then get all the extra functionality, which I think is similar to what Jamie was mentioning, Arden. So, I don't want to be left out.
**Jason** 33:36 on a public interface, but I do see what you're saying, yes.
**Cesar Munoz** 33:39 Yeah, but I mean, at the end of the day, it's… it's like, there's no free lunch, right? So… so…
**Jason** 33:44 That's true.
**Cesar Munoz** 33:45 we can… I mean, there are these alternatives. I'm glad that we are talking about this.
I do see that… This thing of… keep on adding stuff to OpenTrames ROM.
it's probably not something that we can do forever. I mean, we can do it for this too, because I say it's arguably… like, reasonably, you know, core to everything in mobile or Android to have session control and screen control.
But, like, I don't know, maybe in the future there could be… and I'm not saying that we should merge this because of this hypothetical future situation, but maybe in the future, there could be an instrumentation I don't know, for… for… We have, we have one for, Logs that automatically create logs.
OpenTermetry logs, based on the Android logs. We do have it somewhere here.
**Jason** 34:50 Yeah.
**Cesar Munoz** 34:50 Maybe let's say that at some point, we want, to provide some sort of manual interaction with that code at runtime, because we want to either, I don't know, change dynamically at runtime the log level.
Or something.
And then… I mean, we wouldn't add… well, logs are very generic, so probably that would also fit in the main API, but I guess my point is that…
**Jason** 35:20 I'm trying to come up with a straw man example of something that shouldn't be on the interface, right?
**Cesar Munoz** 35:25 I mean… I know that for all of the use cases that we might get asked for, there will be something that we don't want to put in the main interface.
**Jason** 35:35 Totally.
**Cesar Munoz** 35:36 This is, an option to… Not having… it's kind of like a… is the freest lunch that I could find, if we can put it that way.
Where we can… we can say to users, okay, well, if you have that module.
in your dependencies. You can just get its extension.
from the OpenTelemetry ROM instance, and then you can Toy around with it.
But, like, you know, but we won't add it in the main interface.
Yeah. And sorry, Marius.
**Jason** 36:13 Marius, you're being very patient.
**Cesar Munoz** 36:15 by long.
**Marius Constantin** 36:15 I mean, it's an interesting discussion, because I kind of… I see the value in the extensions, exactly what you said.
It's like, how long you… how much further you can go with this ex… with these extra methods, the extra plugins that you're going to provide.
Through the builder, One thing I wanted to mention is, like.
we have the same things that you proposed first time, like methods in the OpenTelemetry ROM instance, like startView, StartAction, sendViewName, setVueName, anything, but… I wanted to make sure that you don't get into the same problems as us, where… Think about multi-active scopes. When I say view scopes, I say, like, you have multi-view screens, sometimes, where you have, like, 2 or 3, maybe, active screens in the same time. If you provide a method that says, said to you name, you will not know At which… so you need to add a lot of things in that method in order to make sure that this view name goes in this screen, so it's like a race condition, if you want, in a way, with this method. So, these methods are good, but in this new world where we're gonna have more and more multi-active views, is… I'm not seeing it well, whereas the plugins, I see it better. And even the extension, I would see it better.
Than that one.
**Jason** 37:43 Cool, and I think extensions, like, using them as a way to, like, vet ideas or to add functionality to the OpenTelemetry Roam interface, like, via extension, is a nice way to test stuff out, right? Like, try it. Maybe these, like, kind of two things we're talking about, we can add as extensions without breaking the interface.
Right? If we decide, oh, you know, we were short-sighted, we said set screen… set screen name, but it really needs to be, like, set screen names, because there can be more than one. Like, if we decide that down the road, then if these extensions themselves are… experimental or under development, not stable yet, then I think that affords us a little bit of flexibility of changing them without changing the main stable interface.
It's a bit of a cheat, it feels… it feels like cheating, but… I think it's okay, it might be a nice way to try this stuff.
**Marius Constantin** 38:36 On the other hand, I think it's a nice idea to expose the OpenTelemetry, say, like, Cesar Manager, to allow me to actually manage that myself.
Or parts of that.
that's also… so yeah, it's… it's your decision here, but I'm just giving you, like, my… I mean, when I build a ROM from Datadog, I'm kind of reacting the same problems more and more.
And, yeah, the more you expose, the better.
But you need to know how much to expose, because you don't want to expose too much.
**Jason** 39:12 You're gonna have a hard time convincing Cesar of that.
**Marius Constantin** 39:14 Yeah.
**Cesar Munoz** 39:14 The users, of course, the more they have… exposed for them, the better.
**Marius Constantin** 39:20 Yeah, but you know that… we know that users can screw it up, so yeah, you need to make sure you expose as much… as little as possible for them to not screw it up.
**Cesar Munoz** 39:31 Yeah.
Well, so… Where does that leave… with Vishwan's use case.
Should we tell him to just add this functionality to the main API? That probably… that could actually solve this particular problem.
Yo.
**Jason** 39:54 It would, and it feels like the least complicated thing right now, to me.
is to put a method on OpenTelemetry Realm that says, I don't… I gotta get the… like, it's like new session, like, or… or… Yeah, like session rollover, something like, rollover session, something like that.
**Cesar Munoz** 40:16 Right.
**Jason** 40:17 Yeah.
**Jamie Lynch (Palo Alto Networks)** 40:17 Yeah, that feels like… It would be… Fairly straightforward to implement.
And… Yeah I think one option as well is we could also, like, mark that as, like, incubating or experimental in some way.
Sorry, but…
**Jason** 40:37 Someone's at my front door, sorry, I gotta go. I gotta… sorry, I'll be right back.
**Cesar Munoz** 40:41 Yeah, take your time.
Yeah, I mean, I think we have dogs that say that experimental, or incubating, I forgot which noun we use, Are not tied to any stability.
Promises, so… Should be fine.
**Marius Constantin** 41:04 If it's a boiler session, I would say it's fine. Session is session. We don't have any rates, any problems.
So, just our decision.
**Cesar Munoz** 41:15 Yeah.
But now that we're discussing this, I'm wondering… Would it be better to add a function to just do this particular use thing, like, this particular use case thing of starting a new session, or maybe add a function that actually gives you an object?
That can control different things.
Related to the session.
**Marius Constantin** 41:49 Like the session criteria, or session start criteria, or something, like a rule set?
**Cesar Munoz** 41:58 Yeah.
or like, or a session, I don't like to use the word manager, but something like that, that you can then… keep on adding stuff, not just start a new session, but then, I don't know, things that… I don't have another example for it.
Because then… I mean, we don't have a use case for it now, and if we put it incubating.
We can always remove it, so…
**Jamie Lynch (Palo Alto Networks)** 42:28 Yeah, I guess that would be… the session provider, or maybe an interface for what supersedes.
Like, the session provider.
I think you've approached your book.
**Cesar Munoz** 42:46 Yeah.
I would like just to confirm with Jason, once he's back, because to me, it's fine.
To have this incubating stuff And then remove them later, if we don't want them anymore.
But I've seen Jason complaining about removing stuff that has never been marked stable before.
And I don't know why. So, before going in this direction, I just wanted to confirm You know, what's his stance on that?
Because I really wouldn't like to get to a point where then we realize that we don't like this New method, and then we have a better shape for it, and then… We can't remove it, because… you know.
Jason doesn't want to, because probably some users already using it, or something like that, so… I want to confirm that first.
But yeah, I mean… It sounds good.
And… and… And I agree that this… at least these two use cases make sense as a… as a… like, main use case for, you know, that are… that grant… its own thing.
in the major, I don't know, let's say.
canonical API interface, if you will, so…
**Jason Morris** 44:16 Is it worth maybe having an incubating, sort of, OpenTelemetry Rum extensions, or incubating interface that implements the OpenTelemetry RUM interface, so it's a sub-interface.
And then the implementation actually implements the incubating one. So all the incubating stuff goes on there. It's more… it's easier to iterate, add, and remove, and things can always migrate up into the main interface. If you want those extensions, if you want the incubating stuff, you have to downcast your interface.
But it maybe provides a bit more freedom.
**Cesar Munoz** 44:55 Right, like, I think like they do in Upstream, right?
then they…
**Jason Morris** 44:59 Yeah.
**Cesar Munoz** 45:01 Yeah, I think they have, like, OpenTelemetry… Incubating some… they start with incubating something, and then that would be the… implementation for… Yeah, they did it with events, now that I remember.
That's another option.
And… I guess the nice thing about it is that you would only have to… Do the cast ones, right?
for the whole…
**Jason Morris** 45:30 Yep.
**Cesar Munoz** 45:31 Instance, yeah.
**Jason Morris** 45:35 And it's also a nice, clear opt-in.
**Cesar Munoz** 45:39 Yeah.
Well, that sounds good.
So… while Jason is away.
Let me see if there's something else on the agenda, and then we can go back to… Please.
There's nothing else in the agenda?
Well, there's nothing else in vision.
Is this a bit awkward?
So… Yeah, in Spain, we don't celebrate Halloween as big as in America.
It sounds fun in America, I don't know.
Probably will… I will… probably will want to see it at some point.
**Marius Constantin** 46:33 It's weird, because in France, we do celebrate.
**Cesar Munoz** 46:37 Like, really big, like.
**Marius Constantin** 46:38 I mean, not…
**Cesar Munoz** 46:39 we're going…
**Marius Constantin** 46:40 We're borrowing it from US, basically. Okay. It's like, it's not that big as in U.S, because I've been in New York two weeks ago, and it already started 2 weeks ago, so… People were already starting celebrating this, so it's not that big, but still, like, I mean, people are… they do, like.
himself, and yeah.
**Jamie Lynch (Palo Alto Networks)** 47:02 Yeah, it's becoming a big thing here as well.
**Marius Constantin** 47:05 It's a funny one.
I like it. It's one of the funniest things.
**Cesar Munoz** 47:15 The funny thing is that where I live.
I've already seen, this month, some… Christmas decoration going on around the city, so… I guess that tells you how much, or how little, I guess, Halloween.
Ace, like, here.
**Marius Constantin** 47:36 Yeah.
**Cesar Munoz** 47:37 decorating for Christmas.
**Marius Constantin** 47:39 Where I live right now, there was already… I was… In the snow up to the knees already last week.
So, the snow is still… it's already here, so yeah.
makes more sense for Christmas than Halloween right now.
**Cesar Munoz** 47:56 Let's see… Well… I really don't know what else to do. I mean, if you guys have any questions… I'm here for it.
Gonna keep… I'm gonna start adding notes into the… the dog.
**Marius Constantin** 48:22 I have one thing to say, I really enjoy these SIGs. I didn't expect that, to be honest, but I really enjoyed it. I learned a lot.
So… Good job.
**Cesar Munoz** 48:33 Nice.
**Marius Constantin** 48:33 sequence.
**Cesar Munoz** 48:35 Well, thank you. Well, it's good to hear.
**Marius Constantin** 48:40 Yeah.
**Cesar Munoz** 48:42 By the way, I took a look at your PR earlier today.
**Marius Constantin** 48:45 Oh, okay.
**Cesar Munoz** 48:47 And… and I think it's… I think it's pretty nice, to be honest. I thought it was gonna be… I was a bit concerned about how big it is.
You know, based on what it tries to solve, and… And then I realized that it's, like, it's just big because, well, it has to, but it really doesn't add, like, any, like, you know, threads or, you know.
Complicated stuff, so… It looks good. I just left a small comment, but otherwise…
**Marius Constantin** 49:18 Thanks. I had David, looking over, actually. I tried to address all the comments he had this morning.
I will look over your comments also. I don't know how you plan, how do you manage these things, like… You decide when to merge, then you close yourself the issue? How is this happening?
Basically.
**Cesar Munoz** 49:40 Well, we have a… we have a policy of types of PRs.
where… they have… we have tiers, and so, depending on the type of PR, Well, it looks like Jason's back.
**Jamie Lynch (Palo Alto Networks)** 49:57 Thank you.
**Jason** 49:58 Sorry about that.
**Jamie Lynch (Palo Alto Networks)** 49:59 I'm a chat.
**Cesar Munoz** 50:02 Yeah, we have, we have… we have a set of tiers, and then, you know, if your PR doesn't touch too much stuff, then with a single approval, we can merge it, but if it does, then two approvals are needed, things like that.
**Marius Constantin** 50:16 Okay.
**Cesar Munoz** 50:17 Yeah, but only, only maintainers can merge VRs.
That's the thing.
**Marius Constantin** 50:24 Yep.
which I find it fair.
I can't… I mean, as an external, you cannot merge PR if you don't really know what's going to affect Above and below the thing that you're touching.
So yeah, you need to know all the infrastructure.
**Jason** 50:47 And to be honest, I mean, I feel like we're probably a little bit slow right now in terms of reviewing and merging pull requests, just because I think… There's a lot of activity right now, like, just the number of pull requests is pretty high.
The number of, like, AI-assisted PRs that come in is, like, increasing, and then we're all working on multiple projects, right? Like, this is no one's full-time job. I think many of us are maintainers on other open-source projects as well, including those for the companies we work for, so it's like, there's a lot going on.
**Cesar Munoz** 51:17 So… I would like to add that sometimes.
I hope I don't regret saying it, but sometimes we… we… we get, You know, carry away with other work.
And maybe you added some… updates to your PR, and we haven't taken a look at it yet, but maybe it's because it just fell you know, inside the gigantic pool of PRs that we have to check, and… And sometimes it helps a lot if you… tag us in the Slack channel, or things like, you know, hey guys, I already have this ready for… and second review, things like that. I would say that that's… that's helpful.
**Marius Constantin** 52:02 Okay, good.
**Cesar Munoz** 52:03 Yeah.
**Jason** 52:04 If we're… yeah, if you feel like it's being unreasonable and you're getting impatient, that's totally fine. Feel free to mention us directly in the PR, ping the Slack channel. If you're not in the Slack channel, it's OpenTelemetry Android.
**Marius Constantin** 52:15 And then…
**Jason** 52:16 And then also just showing up to SIG and put it on the agenda, and, like, force us on SIG Meeting to look at it if it's important to you, and we're dragging our feet.
**Marius Constantin** 52:25 Okay, I got it. I mean, it's fine, I'm not in a hurry either, you know, like you said, I have, like, 4 or 5 projects already… with AI agents right now, it's hard to keep focus, at least for me.
**Jason** 52:42 Yeah.
There's a lot of plates, a lot of plates being spun.
**Marius Constantin** 52:47 Yeah.
By the way, do you plan to add a… it's just a question, because I have it on all my projects, like, do you have… do you plan to have an agent overviewing a… I mean.
Bringer…
**Jason** 52:58 We have that enabled right now, so, like, this is the last PR that came in, I haven't seen this yet, and it automatically should get a… oh, it doesn't automatically get… oh yeah, it does get a co-pilot review.
**Marius Constantin** 53:09 Hmm, Copilot is fine, but not that great.
Yeah.
**Jason** 53:13 That's what we have.
**Marius Constantin** 53:13 This is the only thing you can have as by default, yeah.
**Jason** 53:17 Yeah.
**Cesar Munoz** 53:18 Yeah.
**Marius Constantin** 53:20 I don't know what's your experience with Copilot, by the way, but for me, it's not that great, to be honest.
**Jason** 53:24 It's mixed. I've… I think it's annoying sometimes, but it's also fine.
**Cesar Munoz** 53:32 Yeah, I would say that reviewing PRs, it's… it's fine.
Most of the time.
**Marius Constantin** 53:37 It's catching.
**Cesar Munoz** 53:37 Writing… writing code? Probably not so much, but, you know…
**Marius Constantin** 53:42 I've never wrote code with Copilot, maybe just in the beginnings, like, 2 years ago.
**Jason** 53:46 The other thing to keep in mind is we can make this better, right? Like, do we… don't we have an agent's MD in here somewhere?
**Cesar Munoz** 53:53 the co-pilot instructions.
**Jason** 53:57 Yeah, this one.
So we can make this better, right? If it's not doing a good job, we have plenty of room to throw a bunch more words in here and make it do different stuff.
**Marius Constantin** 54:07 Maybe some skills to know how to run the tests and everything, like, things like that.
**Jason** 54:11 Yeah, it doesn't run them because we have CI, and hopefully it's aware of the CI and can incorporate some of that, but if it's not, yeah, we can always improve it.
**Cesar Munoz** 54:22 Yes.
Yeah. Okay, Jason, just to wrap up the topic.
I added a couple of notes. I think… Regarding this particular issue.
It seems like, okay, we're not going with this… plugin extension API.
We're gonna use… An incubating method.
to add a way to address this issue, to start a new session?
**Jason** 54:49 like this.
**Cesar Munoz** 54:51 Yeah, I forgot if it's incubating or, whatever noun we use to…
**Jason** 54:56 Yeah, okay, but… Like, annotated, okay.
**Cesar Munoz** 55:00 Makes sense. Now, two things that I wanted to confirm. First.
If, in the future, let's say… let's say we had an incubating method today, and then 3 years from now, we decide that we want to get rid of it.
are you gonna be okay with removing it? And I'm asking because sometimes… I know that sometimes you have this, you know, it's not stable, but maybe a lot of users are using it, so… So, you know… Yeah. And…
**Jason** 55:30 No.
**Cesar Munoz** 55:32 And I guess the second…
**Jason** 55:33 I think that's the whole purpose of incubating, right? Otherwise, we just wouldn't use it. It sends that signal, and you have to opt into it, right?
**Cesar Munoz** 55:41 And the second thing is… that… Jason… provided an, Like, there's two alternatives… there's two options to go with this approach. One is… Adding the incubating method into the, Interface.
Or… Creating, another interface that is incubating.
And then extends… From the original interface, and adds all of the incubating stuff.
Which I think is…
**Jason** 56:16 And then as stuff matures, we can move it to the… to the… yeah. And so people would use, or we would give them access, or they could cast.
To the extended? Yeah. Like, what's the…
**Cesar Munoz** 56:26 They'll… they will cast the whole… ROM instance.
**Jason** 56:31 Okay, I think I like this idea.
I might like that.
better. I might like that better.
**Cesar Munoz** 56:38 I think I've seen that approach upstream, so…
**Jason** 56:41 I think so, too. Yeah.
**Cesar Munoz** 56:44 Okay, so… I guess I'll just add… the… the comments in… in… in this one's PR.
**Jason** 56:56 Yeah, it's a bummer that he's not here today, but that's fine. Yeah, I think that's good. Yeah, I like this approach.
I mean, this is a class example, it's not quite the same thing, but they have an extended tracer, which is the interface.
Yeah.
So it'd be very similar to this, yeah.
Cool.
**Cesar Munoz** 57:21 Yeah.
**Jason** 57:22 I'd like to see… yeah, I can't wait to see what it looks like. I think that's a good approach.
**Cesar Munoz** 57:28 Sounds good. Okay, I think that… I think that was it for that… that topic.
**Jason** 57:32 Nice.
Well, we spend most of an hour on one topic, that's pretty good.
**Cesar Munoz** 57:39 Oh, yeah.
**Jason** 57:41 Okay, and I haven't looked at the issues in a couple of days since the release. I assume there's nothing crazy with it.
This thing, yeah, this is… I remember this thing.
**Cesar Munoz** 57:57 Oh, yeah.
I grew up here for it.
**Jason** 58:00 You did?
**Cesar Munoz** 58:00 in country.
**Jason** 58:02 That's cool. Awesome.
So it was reproducible.
**Cesar Munoz** 58:07 Yeah.
**Jason** 58:07 It was a genuine bug.
**Cesar Munoz** 58:09 It is, it is.
**Jason** 58:10 Okay.
**Cesar Munoz** 58:10 Luckily, it was… was easy to fix, but yeah.
**Jason** 58:14 Cool.
Nice, I'll review this.
**Cesar Munoz** 58:18 Cute.
**Jason** 58:22 Looks like Jay already looked at it. Cool. Awesome.
**Cesar Munoz** 58:25 Okay?
**Jason** 58:28 Happy Halloween!
**Cesar Munoz** 58:29 I've seen.
Happy Halloween!
**Jason Morris** 58:31 Happy Halloween!
**Cesar Munoz** 58:32 Bye.
**Jason** 58:33 Bye.
