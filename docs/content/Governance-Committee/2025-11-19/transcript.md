SIG: Governance Committee
Date: 2025-11-19
Duration: 62 minutes
============================================================

## Zoom Recording Transcript

Pablo Baeyens 00:00:19 Hey!
Marylia Gutierrez 00:00:20 Hello!
Pablo Baeyens 00:00:22 Good morning, I guess?
Marylia Gutierrez 00:00:26 Good afternoon to you.
Pablo Baeyens 00:00:29 Yeah, thanks.
Austin Parker 00:00:37 Yo.
Marylia Gutierrez 00:00:38 Hello?
Pablo Baeyens 00:00:42 How was Cube going?
Austin Parker 00:00:47 Not bad.
Pablo Baeyens 00:00:55 You don't sound too excited.
Austin Parker 00:00:59 It's another KubeCon. I mean, it's good to see everyone, it's just, like, it's four 16-hour days in a row, you know?
Pablo Baeyens 00:01:11 Meal.
Austin Parker 00:01:15 And by the time I… I calculated it, I literally had… 3 hours of, like…
Do something at the show that wasn't, like, scheduled or planned or whatever.
Trask Stalnaker 00:01:33 Yeek.
Austin Parker 00:01:34 Which was fun, though, because I got this from.
Pablo Baeyens 00:01:37 It's a flipper Zero?
Austin Parker 00:01:39 Yeah, there was… one of the companies was giving it away, and I won the, like… The little thingy?
Trask Stalnaker 00:01:46 What is that?
Austin Parker 00:01:48 The Flipper Zero?
It's basically a… It's basically an Arduino…
slash Raspberry Pi, kind of in a box with, like, IR… A bunch of, like…
Shorten your field, and, communication stuff, and, like, door tags, so you can, like, you know.
you can, like, clone amiibos with it, right? You can, like, copy your hotel key. It's got GPIO pins on it, so you can use it as, like, a signal analyzer, like, it has, like, a logic analyzer, so you can, you know.
Just, like, a little, like, hacker tool.
Where do you get it? But it's fun, and it's cute, but it's also, like, super cute-shaped. Very fun shaped.
Which I like. I appreciate friend-shaped electronics.
Alolita Sharma 00:02:43 Where did you get it? Black Friday?
Austin Parker 00:02:45 No, KubeCon.
There was a company that was…
There was, like, it was, like, I forget the name.
I did post about them, so they did get some free advertising off of it, but I forget the name of it. But it was some security company, and they had a fun, like, I will say, like, the thing they did at the booth was fun. They had them in, like, a little…
a little cage.
Alolita Sharma 00:03:07 Oh, very cool. Like mice?
Austin Parker 00:03:10 Yeah, well, it's like, there was, like, one in the little cage, and then…
you had to, like, go… you, like, scanned a QR code and went to a website.
And… put in your information, and then, like, it would spit a bag of code at you, and there was, like, a padlock, a little padlock on the cage.
And so, you had to… you could go once a day.
Get a code, and then try the code.
And if it was the wrong code, then you…
Alolita Sharma 00:03:37 You didn't get one.
Austin Parker 00:03:38 Yeah, you didn't get And the next day.
Alolita Sharma 00:03:40 I see. Okay. It's pretty cool.
Austin Parker 00:03:43 But it was a… I thought it was a fun, I thought it was a really, like…
Fun way to, like, get people coming to the booth over and over.
Alolita Sharma 00:03:52 Totally.
Austin Parker 00:03:55 Oh, missed… we missed you, Alita.
Alolita Sharma 00:03:58 I know, I was… I was very sad by telling you.
Austin Parker 00:04:02 Yeah, you can use it.
Alolita Sharma 00:04:04 What a travel disaster. Terrible. My whole team was.
Austin Parker 00:04:07 You and everyone…
Trask Stalnaker 00:04:09 Right? Yeah. Like, yeah, it was just…
Alolita Sharma 00:04:13 We, you know, we waited, like, almost 9 hours, and then they delayed the flight again for another 4, and we were like, oh gosh, this is never going to go.
Austin Parker 00:04:22 I don't… I mean, I don't blame you.
Alolita Sharma 00:04:25 So…
And my whole… my… half my team was there on the same flight, so we were like, oh my gosh.
And the stew, guys.
I was like, gosh, I was gonna come and meet you guys, but hey, we're gonna do Fostem now.
Then we get to see Marilla also.
Pablo Baeyens 00:04:49 So, are we going to do GC only today, or GC plus TC? Because there was a… there was a thread last week on…
Armin (Dynatrace) 00:04:58 Wait, did I hi-check your meeting now? I'm sorry.
Pablo Baeyens 00:05:03 I mean, no, like, we did discuss this last week, so.
Austin Parker 00:05:07 Maybe we are.
Armin (Dynatrace) 00:05:08 Wait, let me check what.
Juraci Paixão Kröhling 00:05:11 The calendar says it's TCAGC today.
That's what my calendar says.
Armin (Dynatrace) 00:05:18 See, mine does.
Austin Parker 00:05:19 No, mine says…
Alolita Sharma 00:05:21 She doesn't. Yeah.
Mine will… You see?
Juraci Paixão Kröhling 00:05:26 I see a technical committee meeting, and I see a governance committee meeting. Yeah. I see two invitations.
Austin Parker 00:05:34 Last week was supposed to be GCTC, but it was KubeCon.
Alolita Sharma 00:05:38 Yeah.
Pablo Baeyens 00:05:39 Right. So…
Trask Stalnaker 00:05:40 Oh… Are we going to do a demo?
Pablo Baeyens 00:05:41 SGC, should we…
Austin Parker 00:05:44 I mean, I think we have a bunch of GC-specific stuff.
Alolita Sharma 00:05:48 Yeah.
Pablo Baeyens 00:05:49 Okay Yeah.
Alolita Sharma 00:05:52 I mean, since Armin is here… Armin, did you want to raise anything?
Armin (Dynatrace) 00:05:56 I could either try to summon the other TC folks, or I leave you on your TC-only call, and then we just do the TC-TC one next time.
Guess we'll have to do the new GCTC member inauguration next time, then.
So unless there's any… TC-specific topics, I… I'll drop off.
Austin Parker 00:06:23 No, the next… so the next current GCTC is scheduled, I think, for December 10th, and we are going to have a guest presentation from Jeremy Morrell at Cloudflare, talking about
their new… How they implemented, their new…
tracing for workers, and I know there was some discussion in the channel about if that should be, like, a spec thing, but…
I thought it would be… we can certainly record and clip out that section if we… Jeremy doesn't want to have, like.
multiple presentations, but I figured it would be good, because they did do some interesting stuff, and I thought it'd be really good feedback for the TC, especially, to hear from people that were doing interesting things at that scale, so…
Armin (Dynatrace) 00:07:11 Yeah, so maybe.
Alolita Sharma 00:07:12 Maybe the TC can join in then, because I think that would be…
Austin Parker 00:07:15 Yeah, that's the next one on the calendar, so it's December 10th.
Armin (Dynatrace) 00:07:19 In the regular, cadence. Alright, sounds good. Yeah. Yeah, I think that the other TC folks are also not…
not prepped for GCTC today, looks like they didn't get… Yeah, it's fine, we had KubeCon, KubeCon messed everyone's stuff up, so…
Austin Parker 00:07:32 Then, catch up with you another time. Bye-bye.
Alolita Sharma 00:07:35 Yeah, Ivan.
Pablo Baeyens 00:07:35 Right?
Alolita Sharma 00:07:35 I.
Trask Stalnaker 00:07:41 Hey, look at this, we got the Brady Bunch.
Austin Parker 00:07:44 thing going. I know, first time in a while, I feel like.
Alolita Sharma 00:07:50 Yes, totally.
Okay, Pablo, do you want to share the… what's on the agenda?
Pablo Baeyens 00:08:02 Right, is there any…
I mean, so I had a very short one, which is, we did a two-week break last year.
For the end of the year, do we want to do the same thing this year? Yeah, absolutely.
Trask Stalnaker 00:08:16 Absolutely.
Alolita Sharma 00:08:17 Yeah.
Morgan McLean 00:08:19 I think it was very effective.
Pablo Baeyens 00:08:20 an issue.
Austin Parker 00:08:20 Everyone loves it.
Pablo Baeyens 00:08:24 Cool.
Alolita Sharma 00:08:24 No, it really helps everybody.
It's actually our main dinners.
Pablo Baeyens 00:08:31 Okay, then…
I don't know, I… did you discuss anything at KubeCon relevant for the graduation, OTEPs, etc?
Austin Parker 00:08:45 I think, yeah, like… So, I will give my, like, general…
summarized readout of, sort of, the various discussions that I had with people outside of the GC.
And it's mostly that… From, like, a due diligence perspective, they feel like what…
That we're doing the right things, and that this should not…
Wind up being an impediment to… The maturity discussions.
And they seemed… TOC seemed…
Happy.
with the, result of…
the feedback and the decisions. I think probably, if I had to summarize even more, what people… what I think people are looking to see, generally, from hotel is more quickly becoming boring.
as a project.
Morgan McLean 00:10:01 We haven't already done that?
Alolita Sharma 00:10:02 Apparently not. I thought it became mainstream.
Morgan McLean 00:10:10 We don't have enough. Let's go home.
Ted Young 00:10:12 Heartbreak.
Trask Stalnaker 00:10:13 I don't have enough stable stuff.
Ted Young 00:10:14 We already are.
Austin Parker 00:10:15 I think that's my… that's the point, right? Like, that's… The point is… You should…
I don't want to say should or get off the pot, but certainly I think there's, you know… that's a fairly crude way of saying it, but I think there's definitely a, like, hey, come on, it's been…
9, 10, 11, 12…
Morgan McLean 00:10:38 Cheers.
Austin Parker 00:10:39 6 years? Six years. Yeah, it's been 6 years now, 7…
you know, if we count from when this whole thing really started and earned…
Morgan McLean 00:10:49 Open Census, all that, yeah.
Austin Parker 00:10:52 Right, when we had those first meetings back in the fall of 2018, wasn't it?
Morgan McLean 00:10:58 I think so, yeah.
Austin Parker 00:10:59 Yeah, Ted Morgan…
Alolita Sharma 00:11:01 Yep.
Morgan McLean 00:11:02 That really fancy office building near the Golden Gate Bridge.
Austin Parker 00:11:05 Yeah, like… Six, seven years being a counted, like…
Ted Young 00:11:09 Is that where Brian Cantrell asked, Bogdan if he'd ever read the SRE? Yeah.
Morgan McLean 00:11:16 Yes!
Alolita Sharma 00:11:17 Yes.
Austin Parker 00:11:20 Yeah, I don't recall Sparrows being there. But either way…
I think there's just a general sense of, like, okay, you know.
you need to have a glide path to some of this, and I do think that that's kind of what this…
Ted Young 00:11:37 Right.
Austin Parker 00:11:38 is all meant to be, and so I think there's probably, you know.
Ted Young 00:11:43 Yes.
Austin Parker 00:11:44 Generic agreement that, yes, we can get there from here.
Pablo Baeyens 00:11:48 Okay.
Austin Parker 00:11:48 I think in terms of specifics around, sort of, the OTEPs, the only thing… the biggest conversations I had…
And I'd be fascinated if anyone else had
feedback on this, but Trask and I talked for a while about instrumentation and telemetry stability.
And I think we kind of came to a consensus about how…
the short version of that, that we can encode into the OTEP is that…
Instrumentation packages can declare themselves stable, assuming they meet stability requirements, even if their telemetry is unstable. All that means is that if the telemetry updates, that's a major version bump.
for them.
Ted Young 00:12:33 Yeah.
Austin Parker 00:12:34 And they are not required to, you know, if it's like, hey, you're depending on an experimental, something that's, like, not gonna be stabilized for years, okay, cool, right? Like, you…
All you're saying is we're not gonna break the out… we're not gonna change the outputs without a major version bump.
You don't have to take every single update of SEMCOM That comes your way.
Right? You can choose to stay where you are, until… and we would recommend, actually, I think… I think the actual recommendation would be, like, you should stabil… you know, if you meet these other criteria, then you should stabilize with what you have today, irrespective of the stability.
Of the underlying… telemetry. At least in…
Trask Stalnaker 00:13:19 underlying…
Austin Parker 00:13:19 and being, like.
Trask Stalnaker 00:13:20 Right. I would just rephrase that to say the telemet…
Austin Parker 00:13:24 conventions.
Ted Young 00:13:25 You emit is stable.
Yeah.
Austin Parker 00:13:29 Right, but like… If you're in… if your instrumentation library is somehow, like, in the middle of
stabilizing. If you're… if you're, like, in RCs right now, right? Or it's, like, actively being… maybe… maybe you could wait until you hit stable semantic conventions.
But if you're not, like, if you're some… some other thing, then go ahead and you meet all these other criteria, then go ahead and say, like, okay.
We're, you know, we're one dot whatever now, and… The telemetry emitted
Is going to stay at this until… and it won't change unless we do a major version bump.
And that's really the…
Ted Young 00:14:19 He'll make 3 changes for a major version bump, I think.
Austin Parker 00:14:21 Right, that's the simplest way to put it. Like, if you're… if the outputs change, that's a major version bump, but don't let the fact that
They may change in the future.
Don't let that stop you from stabilizing.
Ted Young 00:14:36 Yeah. I mean, there's a support problem they will run into.
Right? Where the underlying framework or whatever is being targeted is just gonna move on on versions, and they will hit some version at some point where their old telemetry is not supported by the newest version of the framework they're trying to target, or whatever, but…
That we can leave that for another day.
Like, like…
Trask Stalnaker 00:15:00 really run into that practically in the Java space, at least.
Ted Young 00:15:06 If things move very slowly, it's not… it's not, like, a huge problem, but…
Austin Parker 00:15:11 The… the thing that I… the question I had in my mind was, like.
Because the goal, you know, in an ideal world, it's like, okay, at some point in the future.
let's say… let's take OKHTTP, just to pick a random example. And let's say OKHTTP, in its next major version, has native OTEL API, or, like, natively integrates OTEL.
like…
I guess there's some questions there. Like, I would imagine that the goal should be that, yes, we want you to do this, okay, HTTP, we don't want to do this for you forever.
Obviously, we would continue to… unless they backportered it to…
again, I don't know how all their support matrix works, but if they backported OTEL into their older releases, then I guess we wouldn't have to distribute a…
Instrumentation library.
But, I mean, that also feels like something that's gonna be so case-by-case.
Morgan McLean 00:16:21 Yeah, it seems unlikely, yeah.
Ted Young 00:16:23 Jurassic.
Austin Parker 00:16:24 I'm not thinking that they would natively integrate it, or that they would.
Morgan McLean 00:16:26 Then they would backport it.
Austin Parker 00:16:28 Yeah.
Morgan McLean 00:16:29 Yep.
Native integration seems… well, I don't know, okay, HTTP, but, like, seems likely, and that is our desired.
Austin Parker 00:16:36 I mean, that was just…
Morgan McLean 00:16:36 All instrumentation.
Austin Parker 00:16:38 Right, I was just throwing a dart for that, like, I don't… Amy Drossi?
Juraci Paixão Kröhling 00:16:43 I think, I was working today on a case very similar to that one, not native, but, OTLC, so there is a, like, an external library, but somebody who cares about OTLC and, OpenTelemetry, and, turns out that is not following the semantic conventions, so…
changing that would break the dashboards of people using the telemetry generated by that library. But if I…
So, this is a concrete case, right? So, a case where people would move from one to another, and that would break people. I like the way that Java handled that in the past. I guess what I was trying to say with Otoshi is that requires a major version bump on their side, if they were… if they were to follow the strategy commissions.
I like the way that Java handled that in the past, AA emitting the same telemetry under different names, and, you know, attributes under different names as well.
One concern I think we had right after Java had a 2.0 was people were saying, well, I mean, it's then easy to just break again and just release a 3.0.
But I guess that didn't happen, right? So Java set the tone there, and I think it is… the way that it was handled can be used as a model for the future, for the other libraries as well.
The only concern that I have is… like…
the concern that we had before with Java that didn't concretize.
But it might be…
done in the future by other languages, like, okay, it's fine to break compatibility, I just, bumped the version. Like, the majors become… or minors become majors in the future, and I think that's the wrong…
Kind of approach.
It didn't happen with Java, but I feel like if that's an official position that we want to adopt in any place.
Then we should establish a kind of, like.
6 months or 1-year, ripe period, where…
People would not be bitten by, like, 2 major versions in 6 months.
And that's it, like, you know, you have to move.
Ted Young 00:18:57 I mean, I would suggest… I think I like the idea of having…
Like, in our long-term support doc clarifying support for outdated telemetry.
I don't know that they couldn't move fast, if they had to for some dumb reason, but they definitely have to support
The old stuff.
And that includes if the underlying framework does some major version bump, right? That's where I see people getting stuck.
Austin Parker 00:19:22 I do also want to point out that I…
I would like to think that some of this gets kind of solved by the Epoch release stuff, where…
Right now, so right now, what we say, we say that we give anything that hits stable 3 years?
of… Before we remove it?
From the point we deprecate it? When…
Ted Young 00:19:51 a year.
Trask Stalnaker 00:19:52 One.
Austin Parker 00:19:53 One year.
I mean, we could…
Trask Stalnaker 00:19:56 can…
Austin Parker 00:19:57 No, go on.
Trask Stalnaker 00:19:59 Yeah, I just wanted to cover a couple of things that, add some more color to what Jossie was saying, and I can, address that one also.
the migration that Java did, that was actually defined by semantic conventions.
So that was for all languages.
But that… it was only for within OpenTelemetry community.
Right, for native instrumentations, it's…
guidance, but there's… I mean, they could choose to do what they want. I don't…
Know if we have much say over that.
Yeah, and then for the major, I don't think we have to worry about the major version bumps coming very often because of what was raised about the support. We do have to support, I think, the old major version, CDEs on the old major version for a year, so that would become
really painful.
Austin Parker 00:21:10 I did cap… try to capture this in the notes by saying, like.
Whatever we do is not binding on third parties that choose to integrate OTEL.
But… I would like to think, at least, that we're setting guidance.
Ted Young 00:21:28 Yeah.
Austin Parker 00:21:29 Pablo, then Maria.
Ted Young 00:21:31 just a little bit of color, that double instrumentation, the reason why you only see it in Java, though, is we got feedback from the other language communities that it was too much work.
Right, so in Python and in other places, they're like, we don't have…
We don't have the capacity to do all of that.
Pablo?
Austin Parker 00:21:52 Yeah. Well, I think we'll probably end up hashing out those details in the OTAB.
Pablo Baeyens 00:21:58 Yeah, so…
Switching gears a little bit, are we going to have a single OTEM for this? It seems like this,
More than the epochs or anything else is the topic where…
We have more ideas right now? Should we start with an OTEP for that?
If so, who's going to be… I think that's the thought, yeah.
Ted Young 00:22:21 This seems totally orthogonal to everything else we're doing, it's worth its own OTEP, in my opinion.
Austin Parker 00:22:27 Well, yeah, I thought the idea was that the stability… instrumentation, telemet stability thing would probably be the first one.
Pablo Baeyens 00:22:35 True.
Austin Parker 00:22:35 That's green.
I guess the one question I have…
is that… and Trask and I talked about this, so just correct me if I'm getting the details wrong here, Trask.
But part of the idea is that…
We would expand the definition of stability a little bit to include more specifics around, like, documentation, having benchmarks…
Stuff like that.
maybe we'd not be specific about, like, oh, you have to publish the benchmarks in exactly this way, but, like, it's about, you know… I think a good example would be, like.
when you…
For an instrumentation library to become stable, it must have, like, usage documentation, like, available on the website, so that there's a, like, here's how you actually use this thing.
And… that… definition of stability…
Does feel a little orthogonal from some of the issues that we were just talking about, about, like.
How do libraries and maintainers and everyone cope with
this split of instrumentation and telemetry stability, which feels, again, orthogonal to… and then how do we release all these things as some big unit? So that… that's sort of…
maybe these first two go hand in hand, and we say, like, okay, here's the, like, expanded stability OTEP, and here's the instrumentation and telemetry stability OTEP, and then once we get those two dealt with, we move on to the EPOC release OTEP.
Ted Young 00:24:30 Wait, so, sorry, could you… what are the other two OTEPs?
Austin Parker 00:24:34 Th-th-there's… the first OTEP, or the two OTEPs that kind of happened at the same time.
But are, are necessary One is…
More… changing the, like, updating the stability requirements, and saying, like, stability also means… to be stable, you need…
here's more requirements around documentation, and usage documentation, and blueprint, you know, all that stuff, right? Like, it's not enough to just have a README, you have to have, like, usage documentation for your library, it has to be in the website docs.
You have to have a benchmark that can be run automatically
for your instrumentation, or SDK, or whatever.
You know, and those have to be published, but maybe, you know, or they have to be something that can be run on a regular cadence.
like, stuff like that, right? Like, that sort of bundle of usability… Guidelines, or not guidelines.
Ted Young 00:25:41 User experience stability?
That's one, yeah.
Austin Parker 00:25:45 Right. And then the other one would be the
If you're an instrumentation library… if you have an instrumentation library, here's how you decouple
telemetry stability from… like, here's… here's the guidance on, like, oh, you don't have to…
You could have a stable version of your thing as long as… You…
Commit to, like, not changing the telemetry outputs without a major version bump.
Ted Young 00:26:17 Really has had her hand up for a long time.
Austin Parker 00:26:20 Yeah, sorry.
Marylia Gutierrez 00:26:22 Yeah, so…
Austin Parker 00:26:23 In that case, I'm gonna bring a little back, because it was just a reply for another comment.
Marylia Gutierrez 00:26:27 That it was saying about, like, the sending of two things, that Java is the only one. Actually, JavaScript does that. We do the duplication for HTTP, we do for database semantic conventions. We do major bumps, so we did, like, the 2.0, this year. We got, basically.
no, like, negative feedback. We got no people, like, complaining about, like, I still want those things from one… like, not a single issue was open related to that. We're gonna…
Ted Young 00:26:57 Right? Sorry? When you said you went to 2.0, you're talking about the SDK.
Marylia Gutierrez 00:27:02 Yeah, the SDK. Yeah, the SDK. And we are gonna do the 3.0 beginning of next year, when we're gonna try to stable logs. So, we have been doing major bumps, and people seem to like it, and we have the duplication, and the idea is to
Like, so for example, we added the duplication for, like, HTTP and the database, and we're probably gonna remove the old ones when we do a major bump.
Ted Young 00:27:29 Honestly, JavaScript's kind of a poster child for what I'd love to see in some of the other SIGs.
But just to put a bow on what you were saying earlier, Austin, I totally agree in separating those into two separate OTEPs, because one of them, I think, around, like, hey, let's change our versioning requirements around telemetry, that feels, like, very cut and dry.
And I think people mostly just get that rubber stamped. The rest of this stuff, I think, is a rat's nest.
Because it's all, like, good ideas that communities don't feel like they have the capacity to deal with, so I think we're gonna get a lot of bike shed
Around that stuff. So, for the…
Austin Parker 00:28:09 Yeah.
Ted Young 00:28:10 I think go for it, but I just want to clarify Let's, like…
I don't want us to put so many requirements on this that we don't see movement, when all we're trying to do is, like, rubber stamp these existing…
things. To say, no, really, these things are stable, stop… stop being weird about installing them.
Austin Parker 00:28:32 Yeah, I think we could…
I feel like the, the stability one is probably, like, or the stability requirements one is the one that could get shaved down more. I would rather we start a little bigger on that, and then walk it back.
Ted Young 00:28:53 So, I think… but this gets to, like…
how are we gonna run this stability session in general, right? Like, we have an issue of, like, we've got a bunch of different SIGs, they all have different…
Capacities in terms of, like, How much effort they can put into anything.
And it seems like there's some benefit to having everyone perform a motion at the same time. We're all gonna look at X together.
Right? Like, so one of these motions could be, we're all gonna look at instrumentation, or we're all gonna look at contribib, and we're gonna go in, and to the best of our ability, we're gonna try to add in all of this stuff to the stable things, right? That could be one motion, right? Like, let's add in benchmarks and other things. Another motion could be, like.
the other stuff that JavaScript did, which is, like, we're just irritated by a bunch of crap in our SDK that we would totally just change if everyone would shut up and leave us alone for a minute. And so the JavaScript community took that upon themselves to just do.
And I think some other SIGs would probably benefit from
like, going through that effort. But we can't do all of these things all… we can't tell everyone, do everything at once, right? Like, that'll be…
Austin Parker 00:30:11 Right, right.
I… maybe a better way… or maybe…
How… try this on for size.
instead of casting, sort of, the stability OTEP as stability, what if we, sort of, recharacterize it as re…
productizing… hotel more.
Ted Young 00:30:41 Yeah.
But it's, like, a bunch of bite-sized initiatives, that's all I'm saying. Not one big.
Austin Parker 00:30:47 Sure, but, like, I'm… I want us to have, like…
Maybe I'm wrong. Maybe this is gonna go completely terribly.
Highly likely. I think… but… I feel… and you know, I… I… I tend to feel like…
the… the idea of productizing OTEL is actually a lot of small things that are in service of one big thing. And what we… and from an OTEP perspective, we should present it as, like.
the whole enchilada, right? Like, we should… we shouldn't necessarily have 20 different…
Like, there's… I don't… I don't… I don't know.
if the right approach is having a piecemeal, sort of like, okay, well, here's the improved documentation, OTEP, that is very precise about, like.
here's the exact documentation requirements. Versus, here's the productizing OTEL OTEP, and it has the Four pillars, or whatever.
of what does it mean to have a productized OTEL distribution
And one of those pillars is around documentation.
Like… What, you know…
Feel free to… I feel like different SIGs are gonna take this in completely different ways.
But…
And I think the people on this call are gonna take it in completely different ways, but I think, you know, if there's a tension here, it is that there are some of us that think that
The way to sort of move for… to get alignment on this and move forward is to have… is to…
is to re-point the ship, right? Is to say, like, okay, our North Star was over here before, as this very spec-driven, ticky-tacky.
compliance matrix-y, 300 different checkbox thing, and our new North Star is over here, and it's…
These fairly straightforward goals of
I should be able to, as a consumer, like, download a thing, and click install, and have it work, and get me useful stuff, and be able to have it really clearly documented about what I get.
And how to use it.
Like, that is a big shift. That's a community-wide shift.
And I tend to be on the camp of.
If we try to get people, if we try to move that star, or re-point the ship with a lot…
Like, the fundamental thing we're changing here is that we're trying to move away from being ticky-tacky 300 checkboxes and towards…
slightly more of a vibes-based approach, where we're talking about, like, fitness for purpose, and, more consumer-y, product-oriented things. Like…
trying to do that, try to get there the old way, doesn't feel like it's gonna be as successful. Again, could be wrong, and I'm sure people are gonna have different opinions about it.
And maybe the idea is we do a hybrid, right? We have the OTEP that says, hey, here's the direction, and then we're gonna have smaller OTEPs, or projects, or something that tack to that?
Mainly Jurassi.
Juraci Paixão Kröhling 00:34:12 I'd like to call time on that. I think we had 10 minutes allocated for this one here. I think it is important. I think we have to discuss that.
I… I think we're going too deep into the details for this call here.
One idea that, was circulated last week was…
I like the idea of…
like, us, GC, creating a press release, like, doing the Amazon AWS kind of,
Thing, like, create the press release that you'd like to see published by the time that you complete, and then you work backwards.
Like, if we are changing it, you know, where… or what we are…
supposed to do, like changing the… the,
from the original We Are Only a spec part, to now being the holding Shilada, apparently.
Then perhaps we can start with this press release, and then go back and see, you know, what are the one… what are the things that we need to make this a huge success? Like, is it Java and Go and blah blah blah, and then we go there and do whatever we need to get this press release done.
Austin Parker 00:35:20 I… I will point out that that was… the blog was the press release, right?
Juraci Paixão Kröhling 00:35:25 I don't think it was. Like, it's… I mean, it's not the press release. Like, the press release is… we are… we're very happy to announce that we now have support for Go and Java and blah blah blah and those, main… so people.
Morgan McLean 00:35:38 Are you saying starting in 6 months, or whenever this is implemented.
Juraci Paixão Kröhling 00:35:42 Right, exactly, yeah, so what we're gonna publish in the future, like, start with the future, and then we work towards the future.
Austin Parker 00:35:48 I… I hate ideating exercises.
I mean…
Juraci Paixão Kröhling 00:35:53 I'm having trouble… I mean, I'm having trouble in seeing… like, we have so many paths to go from here. Like, what you suggested is one of them.
There's so many more. Like, Pablo just mentioned another one here in the comments. We are going to have 500 comment discussions, just to get an alignment on that. And it is open telemetry, I see that happening, right? So, we've been trying to get to view one for the collector for 4 years now.
we talked about stabilizing OpenTelemetry in Seattle, and that was, what, 2 years ago? Yeah. So, I think…
What I'm saying is, there's so many ways of achieving that, and we haven't been able to do that right now, or so far.
Austin Parker 00:36:36 Yes, with respect to, like, you did call time, and we should move on, I want to point.
Juraci Paixão Kröhling 00:36:40 Right, yeah. Yes.
Austin Parker 00:36:41 There's a very straightforward way to solve this problem. It is to simply say, okay, it's 1.0 now.
Right? Like, we… Some of this isn't… I think it is a little…
disfavor… I think we need to be very clear that we have had… that we control the buttons we press, and at any point in the past however many years, we had the option of saying, like, okay, we're… we're done. We have hit 1.0 on whatever.
We have chosen not to do that for a variety of reasons, many of which are good.
Some of which are less good.
But I… I will take, as an action item, I will… I will be responsible for the first drafts, at least, of,
the OTEP's coming off of this, and we'll endeavor to have them post-reinvent.
Ted Young 00:37:37 My only strong suggestion is just byte size, right? Like, we know we have, like, a concrete need to change, you know, telemetry versus major version bumps. The collector 1.0 can be its own thing, right? Like, what the collector needs to do to get to 1.0 is totally independent from.
Austin Parker 00:37:57 Yeah.
Ted Young 00:37:57 SDKs have to do.
And then for the rest of the stuff, for the rest of the stuff that affects the SDKs, the main thing I want to point out is…
we do work through a spec, and then people implement it, and that's a very feature-focused way of working. I think the thing we're trying to figure out now is how do we have some cadence of work that's more around
like, installation and usability and cleaning things up, and it feels like stuff that… some of it can go in the spec, but it's, like, harder to, like, drive by, we wrote this in the spec, and now you go do it. And that's why we actually have to figure out what is our…
on a long time scale, like, what's our process for, like, having the SDK SIGs.
Austin Parker 00:38:43 Yes, exactly. 100%.
Ted Young 00:38:45 Yep.
Where they're gonna do this for the rest of time, right? They're not gonna ship features for the rest of time. Hopefully we run out of features.
Right, but, like, if we don't want the sigs to just kind of, like, slowly die on the vine, there needs to be some kind of, like, motion that's always happening there.
Austin Parker 00:39:03 Alright, we gotta give people a goal.
Yeah.
Ted Young 00:39:07 That's a great way to put it.
Alolita Sharma 00:39:09 Yes.
Austin Parker 00:39:10 Or we have to see.
Alolita Sharma 00:39:10 Don't give…
Austin Parker 00:39:11 finish line.
Alolita Sharma 00:39:12 Yes. Pablo.
Austin Parker 00:39:13 You have the next item.
Pablo Baeyens 00:39:15 Right, so we talked about this before KubeCon. I wanted to suggest creating a Code of Conduct Committee. I wrote a proposal. I think today what I want to know is…
First, whether this feels like a good idea to everybody that maybe wasn't there last time. And second, what are the things we need to do?
to move forward, like, what are the… what is the information you would like to know to decide, stuff like that.
I don't know if everybody has read it, or if you want a quick summary of the… Proposal.
Ted Young 00:40:01 I'd like to make a…
Pablo Baeyens 00:40:02 It'll take a minute or two.
Austin Parker 00:40:03 I think it's a good idea. I feel like we should do…
I feel like we should move on to step one.
with the… caveat that, like… It might not happen.
But I think we should at least put the call out there and say, like, hey…
We think this is something that we need to do.
you know, like… Start doing interviews, basically.
Pablo Baeyens 00:40:35 Right.
So, I think one…
One thing that could be positive is there are people that are not from OpenTelemetry, necessarily, within the Code of Conduct Committee. Like, it could be…
people from Kubernetes or some other community within the CNCF, to have the more, like, impartial external voice.
How do people feel about that, and if so, like, how would we get… People to know about this.
Alolita Sharma 00:41:07 I mean, Pablo, the issue is that even Kubernetes, as if, has,
I mean, it's possible, technically, but it's actually a very slow-moving ship when you're in the CNCF doing cross… cross-project, you know, kind of work groups, which review…
Pablo Baeyens 00:41:28 And we are not asking, like, Kubernetes as a project to come here, it's just, like, somebody that is not typically contributing to OpenTelemetry, but rather typically contributing to Kubernetes to join this committee.
Severin Neumann 00:41:39 I mean, we can ask former or existing members of their COC committee, like, for the bootstrapping, to say, like, hey, it would be great to have people
Or maybe one or two that have experience with doing something like that already.
That would be, let's say, a targeted outreach to specific people, if we would be interested.
Austin Parker 00:42:01 I do want to point out that, like, yes, CoopKates has a provisio to say you don't have to be part of
Kubernetes or CNCF, but it also says that you should be, like, Not part of the community.
I think the…
does not have to be part of the Kubernetes community, it's probably more of, like, you don't have to be an active contributor, but you do have to be, like, in the space.
Ted Young 00:42:33 and…
I feel like I've done so much community organizing and, like, affinity groups and things like that, that I'm, like, innately nervous about…
outsourcing that.
Alolita Sharma 00:42:43 Yeah, me too, me too, because I've not seen that.
Ted Young 00:42:47 When these things go sideways, they go sideways so hard. I'm just curious, what's the motivation here? Is it that we don't feel like we're doing a good job with COC stuff, or we don't want to do it?
Alolita Sharma 00:43:00 Yeah, I mean, that was my question, too.
Juraci Paixão Kröhling 00:43:03 I think the key point there is it is elected, or selected by the steering committee, like, in our case would be perhaps the GC. So people would apply, and people would be invited, perhaps, but the decision to who forms the committee would be on us.
Ted Young 00:43:19 Anyone who applies is automatically not allowed on it.
Austin Parker 00:43:23 So…
Juraci Paixão Kröhling 00:43:24 No, I'm good.
Austin Parker 00:43:25 Hmm.
Juraci Paixão Kröhling 00:43:25 No, it's…
Austin Parker 00:43:26 So.
Ted Young 00:43:26 So, the.
Austin Parker 00:43:27 Can you clarify the first part of this, Ted?
There's kind of two big things that…
led to this discussion originally, and one is that I think there's…
an internal percept… like, when we talked about this in the past, there was, like, an internal perception that, like, having the GC…
In certain cases that have come before us on COC, there's…
Hard to talk about this on a recorded call. Right.
Ted Young 00:44:00 Some stuff could.
Austin Parker 00:44:01 Right, but, like, you get… there's… there's… I don't want to say confidence of interest, but there's certainly the, like, oh, the GC is, like, very intimately… like, there's a power imbalance there that is…
challenging.
Like, both for reporters and people being reported, and there are certain intersections of all this stuff that maybe make it harder than it should be to…
Because the point of the COC… I would say the point of the COC is not to, like.
you know, do this to people, it's to actually genuinely
try to make this a more welcoming place, and to sort of help correct these not-great situations that happen. And… I don't know how successful we've been at that second part because of the first part, right? Because…
we're very…
intimately connected in many cases, like, as a project and as employers and whatever, right, to the… some of the circumstances… some of the situations that come up to us. And so there's that idea of, like, okay, if this is something that is, like, outside the GC,
Maybe that helps that.
Ted Young 00:45:10 But you could see it a transitive problem, right? Like, I would have been fine talking to the GC members, but these… I actually have a beef with this jackass over here on…
Alolita Sharma 00:45:19 This year.
Austin Parker 00:45:20 Right, and…
Alolita Sharma 00:45:23 That's exciting.
Austin Parker 00:45:24 Well, you're gonna run into that no matter what. I, I, I, by the way, I agree with you, Ted. Like, fundamentally, I have seen this.
Ted Young 00:45:30 I don't…
Austin Parker 00:45:31 Way too many fucking times.
Alolita Sharma 00:45:33 Many times.
Ted Young 00:45:34 It's not a lot, that's why I'm, like.
Austin Parker 00:45:36 Yes.
Ted Young 00:45:36 Whoa.
Like…
Austin Parker 00:45:39 I, I, I do agree with you there. However, I do also think that…
We should at least explore this enough.
Ted Young 00:45:47 Yes.
Austin Parker 00:45:48 like, I think there is probably value in having
some sort of COC body that is not us directly, although I strongly… I do believe that it should prob…
Ted Young 00:46:06 breathe.
Austin Parker 00:46:07 when I say people that are, like, not…
member, like, people that are part of the observability community, or the open source observability community, or whatever, like… I don't fucking know.
Alolita Sharma 00:46:20 Yes.
Ted Young 00:46:21 How about this?
Austin Parker 00:46:21 Like Henry!
Ted Young 00:46:23 One of… he's…
Austin Parker 00:46:24 part of Otel, but he's not, like…
Ted Young 00:46:27 So there's one approach to taking this forwards, is, like, what Pablo is saying in the comments, which is just that, like.
there are reasons why people, individuals, may need to recuse themselves from individual cases, right? I don't think we've actually written down, like, what the hell do we do when someone needs to recuse themselves, because generally we've got enough…
Alolita Sharma 00:46:48 members to cover it, but… Yeah.
Ted Young 00:46:51 Like, if we need to swap people out, it would be great to have that written down, how we do it, like, before we need to do it.
So in, like, that sense, I would be… Be interested in this?
Pablo?
Pablo Baeyens 00:47:06 So, to try to close this topic,
I can ask, just within auto channels, like, I don't know, the maintainer channel, or, like, different Slack channels where this could be interesting, to see if there are people that, would be…
willing, interested to be on the Code of Conduct Committee, if it were to be formed, and we can continue discussing once we have the list of people, or the…
Pinterest.
Ted Young 00:47:36 watch out for the flame war that comes from the people who said they were interested, and then when they don't…
Alolita Sharma 00:47:41 Exactly.
Ted Young 00:47:42 Conspiracy theory, they're gonna run around generating.
Morgan McLean 00:47:45 Yeah.
Alolita Sharma 00:47:45 Oh, gosh.
Juraci Paixão Kröhling 00:47:46 So, we are quite good.
We are quite good at generating conspiracy theories.
Austin Parker 00:47:54 People… People Select it, or whatever.
Alolita Sharma 00:47:58 And not for GC.
Ted Young 00:48:00 Sure.
Alolita Sharma 00:48:00 Right? I mean, Jurassi, you're saying in general…
Pablo Baeyens 00:48:03 I don't…
Alolita Sharma 00:48:04 V. Who's V?
Juraci Paixão Kröhling 00:48:05 Specifically, like.
Pablo Baeyens 00:48:06 Other projects have code of conduct committees.
Austin Parker 00:48:09 Right, and other projects also have.
Pablo Baeyens 00:48:10 I'm…
Austin Parker 00:48:11 No problem, Pablo.
Ted Young 00:48:12 Yeah, other projects! Hello.
Pablo Baeyens 00:48:15 I don't think the level of drama that you are, envisioning is what we see in other projects, at least not publicly.
Ted Young 00:48:23 Yeah.
Pablo Baeyens 00:48:23 I'm not saying there won't be any drama, but I think it won't be as big as you think it would be.
Juraci Paixão Kröhling 00:48:30 That's what I think.
Austin Parker 00:48:30 Ted and I are both a little on the, like… Ted and I are probably coming at this from a position where we have both seen and experienced these things, how these things go along in a different way.
Alolita Sharma 00:48:41 than maybe some other people on the juicy? Yeah, I mean, I have worked in Wikipedia's COC discussions, so I can tell you they are very complex.
Austin Parker 00:48:53 Yeah, I don't want…
I'm not saying it's a bad idea, Pablo, and I really appreciate everything you're doing through here, and I appreciate your optimism.
Like, I really do?
Alolita Sharma 00:49:04 But I'd like the GC to actually have a group, a sub-team to do this, right?
Juraci Paixão Kröhling 00:49:10 No, I think one way that we can handle that is, we could have different positions in the CLC committee for different parts of the community, so one seat for maintainers, two seats for PC, one for TC, one for the CNCF, and that's.
Alolita Sharma 00:49:24 Yep.
Juraci Paixão Kröhling 00:49:25 Like, it's the CNCF… by CNCF, we trust them. And, that person from the CNCF could be somebody who does a CLC for Kubernetes, or whatever.
Alolita Sharma 00:49:33 I mean, the CO… so, Jurassi, to your point, just interrupting, the TOC does have a COC committee, right, internally, and you can actually take a person from that committee to actually help.
Juraci Paixão Kröhling 00:49:47 So, that requires people knowing, like, very intrinsically, like, very…
Alolita Sharma 00:49:53 Yes. So many details about the hotel and how we work, to go there, to complain about us.
Juraci Paixão Kröhling 00:49:58 And I think the point is, if somebody has a problem with a GC, who do they complain to? To the GC? Like, the COC committee would be, like, that… that…
that body, and that body could have a couple of people from the GC, and people from GC could refuse themselves, but then also TC, and and maintainers, and the CNCF, right?
Morgan McLean 00:50:21 So, I don't think any of that is different, though, if we have a COC committee, right?
Alolita Sharma 00:50:25 Yeah, exactly.
Morgan McLean 00:50:26 the complaint might be about someone on that. Like, I share Ted and Austin's concern here that, like, just to be clear, COC stuff on the GC is my absolute least favorite thing on this committee. Like, I really… it stresses me out, it's always scary, I don't like it, I don't like that kind of conflict. I suspect that's true for a lot of us.
That's probably actually a good thing, that we don't enjoy this, and it makes
relatively good at this. Like Ted and Austin, I really worry if we create a COC committee, the people who will be attracted to it are the ones who enjoy drama and friction and.
Alolita Sharma 00:50:58 Yes.
Morgan McLean 00:50:58 And I've seen that, like Ted and Austin have, in other open source communities, where it gets just out of control.
And I worry about it. Like, the GC has the one pressure valve of being elected by contributors, right? Like, a committee and others do not have that relief valve, and I… I just… I worry about the path that that will take us down.
Ted Young 00:51:19 Yay.
Pablo Baeyens 00:51:24 So… I could… I don't…
there's other topics on the agenda. I can write something down that is vague enough to
possibly appeal to you all, post it on the GC channel. If that works, I can post it and see if there is interest. I don't need to, like… we have not decided anything on this meeting, and it's just, like…
Knowing whether there are people other than this group interested in Code of Conduct that we could, like…
Ted Young 00:51:54 What is here.
Yep.
Austin Parker 00:51:57 I'm… I am gonna call time on this one. I… I do think we should move forward in exploring this more, although, like, I…
Alolita Sharma 00:52:05 Truck.
Austin Parker 00:52:07 I do not… I'm certainly not trying to shit on it. I think…
We all come to this from different places. I do think it's a…
generally a good idea for us to continually improve this, so I would be interested to see, like, some next steps, and for us to, like, move it forward somewhat.
But yeah, let's, let's work on the details.
I have a quick one.
I think Trask will probably be most interested in this, but, I've been approached by…
Minimus.io, who is a… competitor, I believe, to ChainGuard? But they're in the open source…
base image security, whatever space. They're looking into starting an open source program to provide
validated secure base images to OSS projects.
I don't actually… like, my understanding is most of the images that we actually distribute are Scratch.
Images? Is that… is that mostly true?
Juraci Paixão Kröhling 00:53:18 Yes.
Pablo Baeyens 00:53:18 for the collector are?
Juraci Paixão Kröhling 00:53:21 Nick, operator as well, as far as I remember, yeah.
Austin Parker 00:53:23 Yeah, and we don't distribute a ton of other images, other than maybe… out of the operator?
Pablo Baeyens 00:53:31 The eBPF Profiler 1 is based on Go.
Austin Parker 00:53:34 Okay.
Pablo Baeyens 00:53:35 Third one.
Austin Parker 00:53:36 So…
But we also have… but there are a lot of places where we use container images in our toolchains, so…
This is mostly a project infra thing, but just with people's, like, I just, you know, quick blessing of, are we cool if I continue to have discussions with them about,
you know, they're developing this program. They would like for us to be a initial partner type of thing.
But I think supply chain security… Is, increasingly important.
So, good thing for us to give a shit about.
Morgan McLean 00:54:18 It's also a reasonable.
Juraci Paixão Kröhling 00:54:19 Alrighty.
Morgan McLean 00:54:19 use OTEL. And so, if we can get even better at it, I think that's very positive.
Juraci Paixão Kröhling 00:54:25 Are they gonna fix the problems that they find?
Because, the.
Austin Parker 00:54:30 So this would just be, they would provide these tested, FIPS-compliant, whatever, base images that we could use in our container builds.
This isn't, like, security scanning or whatever.
But this would be, so, like, hypothetical…
Someone… we used some image in our builds that got hijacked.
by a malicious actor to, like, insert rogue code or something that makes it to the next stage. Like, these images would be certified to not be bad.
And they would be.
Juraci Paixão Kröhling 00:55:05 So it's…
It's not about our images using their base images, it's about our builders using their images to build our software.
Austin Parker 00:55:15 It would be… I think it would be for everything, yeah. So, like, for stuff that… for stuff where we actually distribute a base image, but yeah, I think it would be… you just have a license to use all of these across the project. Again, I don't know all the specifics, I feel like it would probably be a simple matter of, like, oh, now we… instead of using the upstream…
Go builder image, we could now use the minimus one that is certified to not have…
Ted Young 00:55:42 It's just reducing surface area, right? All they're doing.
Austin Parker 00:55:45 Producing attack surface.
Ted Young 00:55:47 All of these libraries and packages and stuff that come standard, you don't need any of that crap, so we don't ship it, so there's just fewer things.
Fewer.
Austin Parker 00:55:56 This is just about hardening the supply chain.
Ted Young 00:55:58 Deleted everything else off the box.
Juraci Paixão Kröhling 00:56:00 I mean…
it's still not clear to me, like, our… the images that we distribute, they are scratch images, as you pointed out. Like, are we gonna change anything on those images?
Austin Parker 00:56:12 I don't think for the scratch ones, no, but I think what we would pro- like, I think what we could do is we could use these, like.
certify… these… these… Like, we could use them as… like, where we're not… where we're pulling…
not Scratch, and we're pulling, like, a builder image.
like, I think we could use these, like, certified images for the builder instead.
And then we have… you know, Supply chain guarantees.
Juraci Paixão Kröhling 00:56:42 So, I'm a little bit uneasy about that.
Pablo Baeyens 00:56:45 I was…
going to say the same Severin said on the Zoom chat. Let's maybe have 5 minutes to talk through a project.
Austin Parker 00:56:51 Jurassi, if you want to talk… if we want to talk about this async, we can. We're not agreeing to anything yet. I don't know the exact shape of this, and, but this is mostly a, hey, they reached out to me, I want to get a, like…
thumbs up that… We're cool to continue talking with them.
And it sounds like we have a thumbs up to continue talking, so… I will come back with more details.
Ted Young 00:57:17 Project proposal?
Severin Neumann 00:57:18 Yeah, we have two of them still. I don't know if we need to talk once again about the Ecosystem Explorer. Just as a background, like, a lot of the work is happening already, so Jay is really active on that one, and a few other people as well. I don't know if people just can take a look and give their thumbs up, thumbs down on that one.
I think maybe we should spend a few more minutes on the MCP one. 3 minutes is not a lot of time, but I thought it would be good.
Trask Stalnaker 00:57:45 For the Ecosystem Explorer, I'm just waiting for your approval first.
Severin Neumann 00:57:49 Okay, okay, so you want me to take the lead there. Yeah, I think there's a few outstanding, issues on the proposal as well, so then let's do it that way.
Austin Parker 00:57:59 Oh, as the person who has subjected this community with the registry, I will read through Ecosystem Explorer.
Severin Neumann 00:58:07 Yeah, please do.
Trask Stalnaker 00:58:09 Yes, I'm happy to approve it after you do, Severin.
Severin Neumann 00:58:13 Yeah, that would be…
Trask Stalnaker 00:58:14 support it.
Severin Neumann 00:58:15 I will make sure that Jay and I maybe spend some time on, like, getting it into… into a shape I'm happy with, and then hopefully everybody else is happy with it, right? On the MCP server, I don't know if we have, like…
Enough time to get into that.
So I'm not sure if you saw that.
Pavel opened a proposal to have
a working group, a SIG, whatever, to work on a MCP server. I think it was mainly about, like, a tool helping to configure the collector, if I understand him correctly, but of course…
Can we…
Austin Parker 00:58:52 I'll push this to next week.
Alolita Sharma 00:58:53 Yeah, let's discuss that.
Austin Parker 00:58:55 This is a.
Alolita Sharma 00:58:56 What do you do?
Austin Parker 00:58:56 There's… there's a lot here.
Severin Neumann 00:58:57 There was my thing I was worried about with the time that we have, that maybe it's another big, big topic, so… but maybe…
Austin Parker 00:59:04 I would… Did you block off, like, 30 minutes on that?
Ted Young 00:59:06 Yes. Not him.
Severin Neumann 00:59:09 30 minutes.
Austin Parker 00:59:10 No, because, I mean, there's, like, I have… I want to go through and read through it and, like, give… I will actually, like.
Severin Neumann 00:59:16 Yeah, yeah, I think that's the best thing, like, read through that, please, and make up your mind on that, and then we can talk about it next week.
Austin Parker 00:59:25 Yeah, I would… well, I want us to… because there's a lot of ways this discussion can go.
Alolita Sharma 00:59:29 Yes, yes.
Austin Parker 00:59:31 So, I think we should have a…
Alolita Sharma 00:59:33 Yeah, it's.
Austin Parker 00:59:34 about.
Alolita Sharma 00:59:34 It has lots of different ways of…
You know, doing things and also the need for guardrails.
So…
Severin Neumann 00:59:45 Just as a last piece on that, like, he also opened, like.
blog post, or proposed a blog post to the website. And my feeling is, like, this highly depends on the direction, like, this proposal is going.
I told him that already, I just wanted to let you know, like, depending on, like… because if we accept this proposal, I don't, I think this should be, like, a call for contributors. If it's not accepted, this could also take a different route, where we say, like, oh.
here's a group of people working on that outside of the community, whatever, something like that. So, just to… to have you all in the loop for that. But yeah.
Ted Young 01:00:22 Thanks.
Austin Parker 01:00:23 Thank you.
Alolita Sharma 01:00:24 We're at time, but, couple of things.
Juraci Paixão Kröhling 01:00:27 Super fun.
Alolita Sharma 01:00:28 Please read the questions I raised. They are important and coming from the community. So, can we push this next week? Yeah, let's do that.
Austin Parker 01:00:38 Okay. Sounds good.
Severin Neumann 01:00:40 Okay.
Austin Parker 01:00:40 Okay, who keeps… who am I writing to about reInvent on this?
Alolita Sharma 01:00:44 Me.
Austin Parker 01:00:45 Okay, yeah.
Alolita Sharma 01:00:46 Sorry, I didn't run in.
Austin Parker 01:00:48 No, it's cool, it's just like, we're fucking texting in the GC notes. Yeah, just hit me up.
Alolita Sharma 01:00:54 Yes, yes, okay, awesome.
Austin Parker 01:00:56 Will do. See you in Vegas.
Alolita Sharma 01:00:57 The idea.
Morgan McLean 01:00:58 Hey, folks.
Trask Stalnaker 01:00:59 Right.
Pablo Baeyens 01:00:59 Right?
