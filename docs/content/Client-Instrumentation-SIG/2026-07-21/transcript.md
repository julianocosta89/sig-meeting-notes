SIG: Client Instrumentation SIG
Date: 2026-07-21
Duration: 36 minutes
============================================================

## Zoom Recording Transcript

**Ted Young** 00:50 Hello, y'alloo!
**Hanson Ho** 00:55 Hello?
**Jason Plumb** 01:01 Hi, hi.
**Ted Young** 02:00 Three to add things to the agenda?
Hanson, I know you've been working on semantic convention stuff, I'd love to… Dear how that's been going.
**Jason Plumb** 02:19 Yeah, we have federated semantic conventions in Android now.
We're generating event classes.
**Ted Young** 03:06 My stuff after that. That's more concrete.
**Jason Plumb** 03:20 Whoever's in a conference room, it would be cool if we knew who you were.
Just sayin'.
**Bryan Atkinson** 03:36 Sorry, I think that was me, but I dropped off and put a.
**Jason Plumb** 03:39 Oh, okay.
**Bryan Atkinson** 03:41 So it hasn't removed itself from it yet.
**Jason Plumb** 03:44 I'm familiar with that, yeah, okay.
**Ted Young** 03:46 Yeah. Recess, you know, they're playing wall ball, and, you know… Cool.
Alright, well, we got a couple things in the agenda, we got people, could probably kick it off.
Short meeting, 30 minutes.
Hanson, how are things going with, semantic conventions?
**Hanson Ho** 04:15 Yeah, so, add some questions on the semantic conventions Slack, ask some questions here. Basically, I have a existing… or I created, just in my GitHub, a sample federated, convention, a federated semantic conventions repo. I have changes on various other semantic convention repos to depend on it, so I have basically a three-level dependency.
you know, in somewhere else. I think Android, I have a sample, a PR for Android that does it.
Basically, this is a location where we could push, our, common semantic conventions, as we discussed last time. And I just wanted to, to get some more feedback, and… well, I should ask for feedback, but, really, I wanted to, like.
get the go-ahead, say, hey, I want to request this, be created in, Open Telemetry org, have something set up there, and then figure out The process by which we admit events, or a semantic convention in here.
get that going. The first step is we need to be okay with, hey, we're cool with this, and then create the repo, and then, you know, further discuss, the details of maintaining this. We need to talk about it a little bit before we do this, so that, you know, we're actually going to be here to… we're not going to, like, create something and no one is there to maintain it, but we don't have to iron out every little detail before requesting, because requesting, will take a while as well. So, yeah, I don't know if anybody has a chance to take a look at the repo, it's… it's… it defines a registry only, and generates, using Weaver, the READMEs, and the description MD files, for the, for the spats conventions. I put some… some sample ones in there, but it doesn't do any code generation. Code generation is done by the consumer downstream, so, Android, OTEL Android.
have draft PR up for that, that basically takes that stuff and does the generation and consumes it.
So it… the thread is pulled through. So I think mechanically, this is fine. we'll need to figure out some governance and… and checks, and make sure who can merge, and… and what checks we have, and… how we express our dependencies upstream, because, you know, implicitly, if folks are taking us, they're taking whatever we take from. And how does that work? If downstream they have a different, you know, core OTEL semantic convention dependency, how does that, you know, all that stuff?
It's not that it's figured out, but, you know, at least the thread can be pulled through and it works.
**Ted Young** 07:05 You're muted, Jason.
**Jason Plumb** 07:07 Yep Do you feel like there's anything, preventing you from opening that PR, just saying, hey, we're ready to go forward? Like, do you have… Maintainers and improvers identified?
To help with that?
**Hanson Ho** 07:18 No, which is what… I think that's the most important thing, is… is… is what… because the process of getting things, reviewed and merged into the, core semantic convention repo is quite arduous.
I don't know if we want that quite the same way here, but we should have some level of governance so that we're not like anybody who measures… we still want to make sure that everybody, you know, maintainers, approvers in the client space agree that this is good before we actually do it, right? So, determining that, will be important, and identifying people, as you said, would be, would be important. I'll put my name up there as, you know.
To… to be involved with this.
**Ted Young** 08:00 And even though we're federating, I feel like it's important that some core semantic conventions maintainer people be paying attention to this and are involved, because I… I feel like we want to… we're still learning, you know, how to make client stuff be commiserate with, you know, the rest of the semantic conventions.
And also, like.
educating them on what's different about our systems. Like, one thing I think I've seen come up is, we sometimes define things that look similar to, say, like, span-based conventions, but we're defining them as events because we're getting the data asynchronously as, like, a dump.
From, you know, the underlying system.
And just making sure everyone is on the same page about, like, how that should work.
**Hanson Ho** 08:54 So would there be a sponsor from, like, the core semantic convention, or, like, a… yeah, how does that…
**Ted Young** 09:01 Talk to them about how they want to do that, like Lyudmila and Trask and all of them, right? Like, because… it feels like, you know, part of Federated is, like, go off and, like, do your own thing, right? But… but at the same time, we don't want… we don't want there to just be, like, a mismatch, and I think we're all new to federating this out and, like, you know, working more in parallel, but I think it's just something we should just clarify with them and kind of ask how they would like it to work.
**Jason Plumb** 09:32 There was an issue to track this somewhere, right?
I feel like I saw one.
**Hanson Ho** 09:37 I might have created something.
somewhere, I don't know if Android or is it in this repo? Well, actually, there's no repo here, it would be…
**Ted Young** 09:46 Okay.
Yeah, maybe that's the next step, is to create an issue about this in the core semantic convention repo.
**Hanson Ho** 09:55 Okay, I can do that.
**Jason Plumb** 10:03 Yeah, I can't find it right off. I don't remember where it was.
**Ted Young** 10:10 And as a practical matter, I think also, like, attending their SIG meetings and being just kind of, like.
like, the same… the same way in the spec meeting, we found it… it helpful for there to be, like, regular kind of, like, report backs for the projects coming in, so there isn't, you know, there's some overlap between the groups. I think being kind of present there Will, will help a lot.
**Jason Plumb** 10:38 Yeah, the problem still being that I think it conflicts with Android.
**Ted Young** 10:42 Well, the spec meeting conflicts with Android, but, I mean…
**Jason Plumb** 10:46 When is STEMCOF?
**Ted Young** 10:47 I think they have a meeting on Monday… I think it's Mondays.
Yes.
**Jason Plumb** 10:53 AM.
**Hanson Ho** 10:54 Is it 8 AM?
**Ted Young** 10:56 Yeah, 8 a.m. Pacific time on Mondays is the main setting out.
**Jason Plumb** 11:00 Cruel… that's cruelty, Ted.
**Ted Young** 11:01 No, I don't go to it.
**Hanson Ho** 11:03 I'm technically…
**Jason Plumb** 11:05 I wonder why.
**Hanson Ho** 11:06 I start at 7.30, so, I can pop in next time, next week. Especially after… if I create the issues, it'd be good to, like, talk about it.
**Ted Young** 11:14 Yeah. I actually don't go to it just because Monday is, like, internal meeting hell, so… yeah.
**Jason Plumb** 11:20 Yeah.
**Ted Young** 11:29 Great.
But yeah, especially at the beginning, just oversharing, I think, is our friend, for starters.
**Hanson Ho** 11:45 Cool, I think Android would… if we, once we get the things approved, and we get the structure around it, I think Android would be the first one to actually use it. I think I have some sample events and stuff in there. We won't obviously merge those in, like, if we have the repo, we'll probably start with a blank registry or something like that? Or… or… or… or have… Get one in there that we could just, like, you know, fast track to approval, try the new process out, and, and, and see where we get there. But just… Creating a repo, creating a registry, with nothing in there.
**Jason Plumb** 12:22 Let's not get too far ahead of ourselves, yeah, and there are some Android conventions that are embarrassing that I don't want anywhere else yet.
**Hanson Ho** 12:29 Oh, no, no, no, I'm not saying move the Android stuff up, I'm saying Android pull in, and then add things that are less embarrassing, we can move…
**Jason Plumb** 12:36 Okay, okay.
**Hanson Ho** 12:38 I think Martin talked about wanting to… having lots of browser stuff that he wants to kind of get up there, so…
**Jason Plumb** 12:45 Yeah.
**Hanson Ho** 12:48 Cool.
**Martin Kuba** 12:49 Hanson, I'm curious, like, long-term… Are you… are you planning to keep some… some other conventions in the Android? Android? Yeah.
**Hanson Ho** 12:59 The ones that are purely Android, perhaps, but we would basically need to get off the existing name, anyway. So if it makes sense to get it up to a commonplace, we'll probably end up doing that and proposing going through the review stage.
Ideally, the… the platform-specific ones are really very obviously platform-specific. Like.
application not respo- A&R stuff, you know, very specific to the Android, you know, OS, that kind of stuff. But if there's, like, an equivalent that's, like, you know, a freezes or whatever, that's more generic and conceptual, that could be up in, you know, the higher one. I think… Defining a taxonomy and where things live, it's going to be an ongoing, you know, process.
**Martin Kuba** 13:46 Okay.
**Ted Young** 13:48 Yeah, I kind of have a feeling that, like, maybe… I mean, we're just dipping our toes in this, but maybe getting even all the platform-specific stuff up there would be helpful. I'm thinking about people trying to use Weaver and other, like, SEMCON tooling things, and… Someone trying to get their head wrapped around on, like, how Client works, and… I just wonder if having everything in one spot would… would… would be beneficial.
**Hanson Ho** 14:15 So basically, you just have, like, an Android namespace, if… for platform-specific stuff.
**Ted Young** 14:20 Yeah, yeah, I think we should figure out how that should look. But, I mean, the same thing's gonna happen in iOS, same thing's gonna happen in… in browser, and… and then we have, like, cross-platform things, which is, like, one thing I want to talk about, right? Like, Flutter's coming online, and they have to figure out what the heck… They're gonna do.
So, when you add all… stack all of that up, I don't know, it seems maybe, like, less crazy-making for everyone, if there's, like, one place we can all look to… to figure out what the landscape looks like.
**Hanson Ho** 14:54 Yeah, and.
**Jason Plumb** 14:56 Sorry, does that Flutter dude know about this meeting?
**Ted Young** 14:59 Well, they haven't kicked off yet, but you're right, I should reach out to him and look.
**Jason Plumb** 15:06 It'd be good to have him show up here, yeah.
**Ted Young** 15:08 Yeah, for sure.
They haven't started yet, but that's also, like, yeah, we need to… We need to help them, and not have them be, like, starting off in a vacuum.
**Jason Plumb** 15:22 Yeah.
**Ted Young** 15:23 For sure.
**Hanson Ho** 15:26 And one quick thing is, I think the name we're gonna go with is Client Side, after a lot of discussion. If someone goes and says, hey, that's not specific enough, then we'll revert back to… End user Client. They're all gonna be whatever. Part of me is like, let's just fucking call it marshmallows, so that it'll be obviously, you have to look it up, but…
**Ted Young** 15:47 Yeah, just don't call it DEM, I'm sick of that shit.
**Hanson Ho** 15:51 DEM?
**Ted Young** 15:54 Yeah, isn't that the new rum?
**Jason Plumb** 15:56 It is, yeah.
**Hanson Ho** 15:57 What?
**Ted Young** 15:58 Exactly, exactly.
**Hanson Ho** 16:01 No, no three-letter acronyms, or TLAs.
**Jason Plumb** 16:04 Digital experience is less creepy than people monitoring users, I think is the motivation. Even though it's the same thing.
**Ted Young** 16:14 Also, the real user monitoring, like, the real parts probably dropping… the floor's dropping out from that, so… Anyways… Anyways, moving on… Cool, that's awesome. Thank you so much for holding all that down, Hanson.
Okay, so next up, it would be great to kind of… I feel like we're at a stage of, like, doing a report back to, you know, the main… a spec group about, like, kind of state of client-side stuff. Jason, I think you were… you were hacking on that?
I was just curious if, where any of that was, and do we need to get a little more organized around presenting that?
**Jason Plumb** 17:04 I have not been hacking on that, except for we do have a roadmap now for Android. Okay, great. So, I think that would help. I can link to that here. It got merged, so let me… let me find it.
**Hanson Ho** 17:21 I'd be interested in helping out with that, if it's… if it's just, like, you know, talking to the, to the, to the, spec SIG or…
**Ted Young** 17:29 Yeah.
**Hanson Ho** 17:30 Appropractice.
**Ted Young** 17:30 I think it's getting, you know, maybe a roadmap for browser, and a roadmap for iOS put together, and then, yeah, having some collection of maintainers from those SIGs just give a… presentation of, like, hey, this is, like, generally where we're at. We're making, you know, federated semantic conventions, this is kind of where… Like, in terms of, like.
End users can use this, or there's something to demo, or whatever, just letting people know.
Know where things are at.
But I think maybe, Martin, for making sure browser has a roadmap that's consumable, maybe that's, like, the next there.
And… I don't… is there anyone from the iOS SIG here?
Maybe that's… that's a thing we should follow up with. I can follow up with the iOS SIG about doing the same thing over there.
**Jason Plumb** 18:29 I wonder if we should move the Android meeting.
**Ted Young** 18:34 This is gonna be my next question, like, how convenient would that be to maybe not have it overlap with the spec SIG?
**Jason Plumb** 18:42 I mean, I should have asked an hour ago, but I guess we can ask next week, and then follow up, but Thursday at 8am, maybe? Because, like, we do have a ton of people in Europe, so I think that would, you know…
**Ted Young** 18:56 Yeah, the OTO EU Pacific, you know, Meeting band is, like, very graphic, so I know it is hard to find something that works with everybody's schedule, but… might be good to have it be easier for Android to show up to the regular maintainer call. This is actually a request from people, other maintainers, was like, hey, we don't really see, like, client maintainers around much in the…
**Jason Plumb** 19:28 Yeah.
**Ted Young** 19:29 General maintainer spaces.
**Jason Plumb** 19:32 We have a meeting conflict, we… Today!
Okay, I will take an action item for… to bring up a time change next week, and in the meantime, I'll ask in Slack so that we can get a head start on that.
**Ted Young** 19:44 Great.
Okay.
Okay, so next up, so, Flutter, right, this crop, Dart and Flutter, the kind of last thing that SIG needs in order to get started is, like, TC sponsorship, which is, like, taking a minute, because Nobody there has expertise in this field.
I think Carlos is interested in doing it, so they're gonna sort it all out tomorrow. I think longer term, they want to get someone onto the TC who does have this experience, but We don't want to hold… the show up, for… for that. But… hopefully the TC sorts its shit out tomorrow about how they wanna keep track of this SIG, and I do think it's an important… it's important for this SIG to have some attention, because it… it… it's… we're moving in, code from existing, external sources, it's a lot of people who are excited, but who are new to Open Telemetry.
And then on top of it all, it's going from, like.
you know, 3 separate client domains to now adding, like, a cross-domain thing. So I do think it's a SIG that needs a lot of, like, tender, loving care from the rest of us if they're gonna be successful.
So… and because they'll probably kick off as soon as they get a TC sponsor, I think it's a good time For us to think about, like, how do we want to… One, you know, who… might be interested in… in joining that SIG and at least paying attention to them.
From this group. And also, I think it begs the question of, like, do we want to get more organized as… as, like, the client collective within Open Telemetry? Beyond just, you know, kind of, like.
Right now, it's kind of like a flat hierarchy, right? We just have a handful of SIGs working on this stuff.
Do we… is there, like, some more structure that would be helpful, other than getting a client-side person onto the TC?
So, I'm just curious what you all think about about all of that. Maybe the first question, is there anybody interested in Flutter?
sort of looking side-eye at the Firebase people.
**Cleo Schneider** 22:24 I did ping the Flutter team, so I'm hoping that we can get somebody from their… their team to actually get involved here, because I am certainly not a Flutter expert, but but yeah, I'll keep working that angle.
**Ted Young** 22:40 Yeah.
I feel like semantic conventions is, like, that's sort of the… like, it's, like, good timing to be getting that rolling.
Because that's… that's honestly where the most confusing questions come up, right?
And I think as long as there's… there's a lot of open conversation there, and they're not kind of off in a corner on that stuff, that's… that's probably maybe where we can organize all of this, so it's good timing that you're setting all of that up, Hanson.
**Hanson Ho** 23:15 Yeah, I think we had the client concern be a bit bigger, and then we kind of contracted as things that are common, there are fewer things that we have active cycles to work on.
But there's always something, something there. And I feel like when there are projects that kind of emerge, things can then expand. But, like, putting something you know, it's just another level of having to, like, you know, meetings to go to and things like that, and I think making things project-based, so, like, semantic conventions, for instance, you know, that would be good. so I don't think we need to do anything proactive, to, to… Other than, like, you know, try to bring them in and talking to them. But in terms of structure, I… I think what we have right now is okay, for now.
**Ted Young** 24:01 Great. Yeah, I think, where I think it gets confusing is, like, right now we have some common set of conventions, and then we have some platform-specific ones. But what does Flutter do about the platform-specific stuff? Is it just that there's also Flutter-specific conventions for these things? Maybe that's… that's the way it's done. I have… I am also not a Flutter expert, so I don't know how these existing implementations do it. I'm sure it's not, like, a new problem for them to sort that out, but…
**Hanson Ho** 24:38 So, so definitely talking to the Flutter folks with respect to semantic conventions is super important. That has to be done. I think I was just talking about, like.
everything else, yeah, definitely Savannah's conventions, for sure.
**Ted Young** 24:49 Maybe that's… that's all we need for now, is just getting this federated semantic convention reboasted up, and making sure, you know, maintainers from all the different things are paying attention, and we're making sure we get the Flutter people in their, write quick. As long as… I think that's… as long as we're really coordinating around that, I probably… we don't need to coordinate too much around… much else.
**Cleo Schneider** 25:15 Well, I am… I am a little curious as to how we feel about having a similar sort of interface that folks are using across these different clients.
you know, like, how much do we care about the modeling of some of these life cycles across these different… because you're going to have folks that are gonna want to be able to compare between these things. We are certainly thinking about that, and so I do think that's a concern, and we should think about how those semantic conventions translate into both the SDK feel and some of the observability side of it, the UX side of it, of how are people actually consuming this data. So I would like to have that conversation.
**Hanson Ho** 26:01 So we had this idea of an agent's API. Before, the word agent was basically repurposed for other uses, in the tech world in the last year, couple years, that unites, semantic behavior, things like sessions, which, you know, Martin will talk about later, and, startup and, termination, things, things that are common to all, apps. Because the interfaces for individual platforms are quite different, but, you know, abstractly, they… provide similar information, so is there a way to… there's always a desire to do that, but the cycles being what they are, we couldn't even get anything or rather, the things that we want to do with sessions, even, didn't reach where we wanted to be at, like, a year ago. So I think, starting… so we definitely need that, but starting with something concrete, like sessions, would be, I think.
Would be a good, a good thing.
**Ted Young** 27:05 Yeah, so I think, like, this really makes the case for, like, all the platform-specific stuff as, like, a next step as soon as we stand this repo up, to just, like, have every SIG just dump their existing stuff.
that's platform-specific into an area there, right? So we can just… it'll make it so much easier to figure out, like, and talk about these things.
But speaking of sessions, we only have a few minutes left, so Martin, do you want to lead us on that?
**Martin Kuba** 27:38 Yeah, so just really quick, we are in the browser SIG.
we are at a place where we want to start integrating sessions into the SDK. Right now, we have some implementation, but it's essentially just kind of like a side thing that you have to wire in. It's adding… it would be adding, session ID as an attribute on all the signals.
Which is, I think, what Android is doing right now, correct?
So, like, we're trying to decide, since we don't have that integrated yet, should we go with that approach?
like, kind of like what Android has done, or should we be kind of forward-looking and, and implemented, as, as, resource attributes, right, and, and, and maybe entities?
I was just one… I was just wondering to, to hear from Android, if you have any, any, Yeah, any plans of doing the same thing? Or, like, what the next steps should be? Like, do we need to align on this? Do we need to, like, write some spec or something?
**Hanson Ho** 28:43 So, I was looking at… oh, Jason, you're gonna ask.
**Jason Plumb** 28:46 Yeah, it's… we've kicked that can down the road for a while, as far as just slapping session ID, on all telemetry, and indicating what the current session is and when it changes. You know, there's… we generate an event that shows the current session and the previous session, but that state is just… like, the previous is not maintained past the event.
It's been… I'm chuckling because it's been on my to-do list to explore entities and to do this, at least, research and prototype. It feels like the right thing to do. We've put the work into creating entities, but haven't had… haven't had time yet, and I haven't seen anybody else pick it up yet, so, as far as a recommendation for you, I'm inclined to say do the right thing, and let the platforms differ, and Android will have to play catch-up, but… That's one opinion.
**Hanson Ho** 29:37 So, I was looking at the entity stuff with respect to session. I do see, a session entity, I think.
What we need, though, is a mutable, non-identifying attribute that represents the session ID. And looking at the state of the APIs and SDKs, they… we can define it in the semantic convention.
But none of the SDKs have support for it, and none of the APIs, or there's no… API way of even saying, I want to mutate a resource attribute. So, I think at the data model layer, we can define it, but we lack the plumbing.
So if in JS you've… you have defined API, you have defined mutator for attributes, or for resource attributes, and you can, you know, do the proper thing, you cut a new, you know, envelope, blah blah blah, resource object, and do all that update, then I think that's the way to go, because I think session ID belongs as a non-identifying attribute of the session entity, so you just have to force the rest of us to kind of, you know, get on board. We already have session ID as an attribute, so, you know, at least you don't have to get that in. But… That way, people on the client.
we could point to them, say, hey, you should look for ID in the attribute, or in the resource. And the other clients are not doing that yet, or the other… yeah, but eventually we should.
**Ted Young** 31:12 Yeah, so we're at time, but I totally agree with you, like, you know, the short path is you make a resource provider. We've sketched out what this thing should look like a million times.
But then you're stuck with this resource provider API, and if that's about to change into, like, an entity provider API, because we want more full support for entities. I think that's the bridge we have to cross.
**Jason Plumb** 31:37 I think we need a short-lived session, SIG, to be honest.
I hate to do it, but I think we need it.
**Ted Young** 31:43 Yep.
**Jason Plumb** 31:44 Yep.
**Ted Young** 31:44 Okay. Well, see y'all.
**Hanson Ho** 31:49 Bye.
