SIG: PHP SIG
Date: 2026-03-18
Duration: 59 minutes
============================================================

## Zoom Recording Transcript

**Bob Strecansky** 01:01 Means?
**Chris Lightfoot-Wild** 01:03 Hey, Bob.
**Bob Strecansky** 01:05 Period.
**Chris Lightfoot-Wild** 01:07 Sorry, turn the volume right down.
**Bob Strecansky** 01:10 Yay.
**Chris Lightfoot-Wild** 01:13 Double-check the, calendar today, just to make sure it's at the right time.
**Bob Strecansky** 01:18 Stupid daylight savings time.
Gets you every time.
**Sergey** 01:24 Alright.
**Bob Strecansky** 01:26 Blue.
**Sergey** 01:29 I like them. I done?
**Chris Lightfoot-Wild** 01:35 How you doing?
**Sergey** 01:36 Dwell.
All things considered.
**Chris Lightfoot-Wild** 01:42 Hmm.
**Sergey** 01:44 what, Do you have any effects on price of, gas? How do you call, do you call it petroleum?
How do you call it in UK?
**Chris Lightfoot-Wild** 01:56 We've got either petrol or diesel.
**Sergey** 01:57 Petrol. Okay.
**Chris Lightfoot-Wild** 01:59 Yeah, so, yeah, I refueled last night, actually. Yeah, it's gone up.
A little bit. Awesome.
**Yeah, it's… Bob Strecansky** 02:07 What did it cost last night?
**Chris Lightfoot-Wild** 02:10 Is that £1.58 per liter or something?
**We put Polita rather than going here, so… Sergey** 02:17 What was the jumbo?
Relative to the last time.
**Chris Lightfoot-Wild** 02:20 I think it was 1… 138 or 139 something, so 20, so, I don't know, 15% something?
Quick mental… mental maths, but yeah, it's been up a little bit.
**Bob Strecansky** 02:34 Yeah, it's gone from, like.
$2.29 a gallon here to, like, 4… I think it was $4.30, or sorry, $3.49 this morning when I drove past the station.
**Chris Lightfoot-Wild** 02:45 Hmm.
**Bob Strecansky** 02:47 Big changes.
It's, I drive an electric car, and my wife drives a gas car, so we, like, have to pay attention to it.
**Sergey** 02:57 Mmm, good.
**Chris Lightfoot-Wild** 02:58 There's not very much you can do about it. If you don't… I guess if I don't have an EV car, then I'm stuck.
**Bob Strecansky** 03:04 Say it again?
**Chris Lightfoot-Wild** 03:05 kind of at the mercy of whatever the market price is, because I've got no alternative. I mean… Bob Strecansky 03:11 Go ahead.
**Sergey** 03:12 hedge your bets, right?
You could have bought oil futures, right?
**Bob Strecansky** 03:17 That's right.
**Sergey** 03:18 Maybe even with, you know, I think there are different kinds of features, but you can buy features where they will… they will supply you oil, right?
**If you have your own, kind of, like, what those factories are called, where you… Bob Strecansky** 03:32 Refiner. Refiners.
**Sergey** 03:34 refiners, yeah.
That's beautiful.
**Chris Lightfoot-Wild** 03:37 I was in the back garden, and I'm Market.
**Bob Strecansky** 03:39 They just keep… Chris is just stacking barrels of crude in his backyard.
**Sergey** 03:44 I thought that you can read those stories, people obviously… I think it's 10 times the market, paper market on oil, like, most people obviously speculate on it.
But sometimes people, like, new, they don't understand what they're doing, so some people buy future… futures with supply, so they eventually got to… somebody calls them, okay, where do you want that, half a ton per oil that you bought?
**Chris Lightfoot-Wild** 04:04 Oops.
**Bob Strecansky** 04:07 It'll all fit in my gas tank, right?
**Sergey** 04:13 Actually, it's not fun, like, because in COVID, it was, you paid people just to hold off that oil, right? It was kind of, like, negative in the sense that People didn't have anywhere to store it, so… You got paid, you got paid, essentially, to sell, so the seller was, also kind of, like, had to pay the buyer just to get rid of that oil.
**Bob Strecansky** 04:36 true. I remember… my daughter was born, like, a couple weeks before COVID lockdown. I remember going for walks.
past the gas… like, we, you know, we aren't driving that much, and I remember going walks past the gas station and seeing, like, $1.19, or… it was just… it felt, like, prehistoric, you know? It felt like I was a little… when I was a little kid.
**Sergey** 04:58 Should have stuck up, should have filled all the canisters.
**Bob Strecansky** 05:01 I know, I should have just, like, yeah, I should've got, like, a big swimming pool in my backyard.
**Sergey** 05:05 Although, I think petrol has, expiration, right? I don't know.
**Bob Strecansky** 05:08 It does.
**Sergey** 05:09 Yes, man.
**Bob Strecansky** 05:10 It's funny that you mention that. I was actually just reading about that the other day. I think, like, sitting idle, it has, like, a shelf life of, like, 3 months, but like you said, it probably, like, it can be 5 to 10 years, but I think, like, its useful… like, its usefulness and degradation is, like, a pretty goofy curve.
Alright, we're 5 after. I don't think we expect anybody else to come.
So, let's open the floor. Chris, looks like you had something on the agenda for SEMCOM and instrumentation?
**Chris Lightfoot-Wild** 05:43 Yeah, I guess a discussion point, maybe to help my own clarity, or maybe just… Document what we should be doing about this.
I think… It changed, so the… There's a dependency on the SEMCOM there, which obviously feels quite dangerous just to bump up, generally without any kind of consideration that… the previous schema URL there, does it match the new semantics? Because… they can change, obviously. That's the point of versioning the semantics.
So, if people just come along and say, oh, I'm just gonna bump this number.
Without, like, actually checking that all the attributes align, and… Correct. Only that we've seen it in the past, obviously, with the messaging instrumentation, where the order of, the way the payload was built out had changed around a little bit.
I don't know if there's any, like, safeguards in place for it or not, or… because I imagine, certainly with, like, again, Laravel instrumentation, obviously I'm more familiar with, there's several components to that, and each of them may in future remit different versions of the schema telemetry, I guess, well, the sort of… You know, you can't… if there's a new version out, you'll probably update little bits and pieces as and when you've checked that they adhere to the The stipulated version.
**Bob Strecansky** 07:12 Yeah.
**Chris Lightfoot-Wild** 07:13 So, yeah, I don't know… in this instance, I think I… did I leave a comment on this one? Yeah.
**Sergey** 07:18 By the way, when you say that the different pieces on Laravel can emit different versions of the schema, but schema, you place it, like, per span, right? You don't have, like, finer… final resolution that you can… it's not like per attribute, right? You… so the whole span should… should be conforming to one particular schema, right? This is how the… or even per resource. Where do we place the schema URL?
**Chris Lightfoot-Wild** 07:42 When you're building a tracer, you can specify the version… Sergey 07:45 But eventually, in the output data, I think it's placed in the resource, and then on the resource, you can have, like, a bunch of spawns that came from that resource, right?
So it's… what I'm trying to say is that at least it's per spun, right? So it's not possible to… so that's why I was wondering, when you said that Laravel can emit different versions of, it would not be possible to do it just for one span, I mean, different pieces with different schemas, right?
**Chris Lightfoot-Wild** 08:09 No, I don't think it's for… I think you're right. So, like… but different parts of… different components in the overall viral instrumentation.
Could be emitting different versions, and that's, like, you know, different spans.
**Sergey** 08:24 So somehow you're saying per span, then it somehow output data kind of, like, sorts them out, and you can identify which span was emitted under which schema.
**Chris Lightfoot-Wild** 08:35 But my understanding of… semantic conventions, and omitting them in that way as well, is that certain things like upstream, like the hotel collector.
Might want to help migrate from, like, an older format into a newer one, or… To handle that kind of process.
It was more like, should we be… the PR template, or an issue template, or something, should it mention?
There's some, like, caution to take with… you know, you can't just… I don't think you should just blindly bump it up without… Necessarily understanding what the… The differences in the version you're.
**Bob Strecansky** 09:12 That's interesting.
**That, and I think, like, I don't love this hard… like, this hard coding of this version here. I think that this was probably done for a particular reason. Like, using… Sergey** 09:23 That's always the latest one that we support. That's one on the top that, the old one.
**Chris Lightfoot-Wild** 09:30 that resource attributes, and it got moved into that.
**Sergey** 09:36 That comes from SDK, right? Or API? Like, which package? API?
**Chris Lightfoot-Wild** 09:41 on the package.
**Sergey** 09:43 Weird.
**Bob Strecansky** 09:43 That's from Simcoe.
**Sergey** 09:45 But that's gonna be the latest version, right? So it will not care, like, if you actually… so essentially, if you go and just, so it doesn't even depend on this… so if some other… so what I'm trying to say is that if some other dependency goes and takes dependency on higher level… higher version of the… whatever package that constant came from.
then this particular instrumentation will also kind of, like, say, yes, I am emitting data based on the newest schema, even though it's not true, right? Yeah. I assume this is why you put the hard-coded constant there.
**Chris Lightfoot-Wild** 10:17 Yeah, I don't think we should just blindly bump that up without, you know, reading through the spec, or knowing that the changes that we're making do adhere to the right thing.
**Sergey** 10:27 But like I said, it can happen even without you even changing this instrumentation, right? You were not even aware, like, because some other component took dependency on a higher version of that package, and that constant got bumped up automatically, and this package didn't even do anything about it, right? So, it got kind of like… Chris Lightfoot-Wild 10:45 It reads like if… I think I've seen something, or verbiage that suggested that if you are explicitly saying the version, then… You shouldn't just drift it around like that. Versus you may not declare it, and then it's a bit more… It's kind of loose, but if we're trying to say we're emitting stable telemetry.
To whatever version, and that… it's not… it doesn't feel like it's necessarily true if… If we're just hard-coding this value and then bumping it at will without checking. And I don't know what the process should be, like… Do we just have to be… kind of on it before deciding to bump it, and should there be warnings in place somehow, or… I don't know, it might just be me making noise or worrying over nothing.
**Bob Strecansky** 11:32 I don't think… I don't think so. I'm looking here and seeing all the different places where this, schema version is defined, and this… like, this feels itchy to me, right? We probably don't want different… we probably don't want different… like, versions of semantic conventions being applied to different instrumentation and things, so that could get… I feel like that could get… Chris Lightfoot-Wild 11:52 I think, but… But he wasn't… Sergey 11:54 the original purpose of this. This was exactly for you to distinguish which… because if you didn't update Maybe I'm not following… sorry to interrupt me, Chris, can you please go ahead, what do you have to say?
**Chris Lightfoot-Wild** 12:05 Well, I think that's the intent, though, is that, like, when you've built the instrumentation, and you've built it out to, like, 1.32, and you've said, right, what I'm just emitting now adheres to the spec at 1.32, and then… Bob Strecansky 12:18 I see.
**Chris Lightfoot-Wild** 12:18 Let's a 135 is available, and some other instrumentation is built that emits telemetry that adheres to 135.
**The 132 kilometry is still… Bob Strecansky** 12:29 valid.
**Chris Lightfoot-Wild** 12:30 And then if you want to update that in future, because there's new attributes or whatever, there's some kind of… I imagine in my head, there should be some process to go through and check.
Rather than just bump the number up, that it adheres to the version we're about to bump it to, with the new.
**Bob Strecansky** 12:44 I see.
**Chris Lightfoot-Wild** 12:45 The dropped ones, or restructured, whatever it is, to now say this is the… we're adhering to this correct one.
**Bob Strecansky** 12:53 Yeah, it's almost like you need a CI check for that.
**Sergey** 12:55 So semantic versions are backward compatible, what you described, like, 35, 32, but only for the stable namespace, right? Whatever came from experimental namespace, that can change in compatible between versions. So, in that sense, so kind of like that part, even though semantic version of semantic conventions can say that it should be compatible, but if you use those experimental attributes, then they might not be compatible, right? They might change the… So, then the… so you're saying… You want to make sure we use explicit version everywhere?
And the second step that you mentioned, how can we kind of, like, make sure that if somebody goes and bumps that number, then they do it kind of, like, you know, with some confidence, that they know what they're doing, and maybe we can put some automatic checks for that, right?
**Chris Lightfoot-Wild** 13:45 Yeah, I was just… I guess I wasn't trying to be the bad guy, I just wanted to check that, actually, you know, was it… A worthy comment to add that… Maybe there should be a process around this, and then it should be caught somehow that you know, we need to… there's some sort of checks. I don't know what other SIGs do, obviously, around this… this kind of thing, but suggest… I imagine some of the other SIGs may have more, you know, members that are closer to, like, the SEMCOM Group as well, so props.
**Sergey** 14:15 I would wonder what other languages are doing, probably maybe they already have some, work, work process around the procedure?
But it sounds to me, using this constant, it always points to the latest thing that can bumped in automatically, regardless what that package that referred to it meant.
Sounds like we almost make that part essentially unreliable, right? So, we just produce version, but it doesn't mean anything if it just will be always the latest.
Based on what dependency was taken, like, by the, you know, by the latest. Whoever wanted the latest systematic conditions, they will be the ones that will essentially… will determine the value of this constant, right?
**Chris Lightfoot-Wild** 14:57 Yeah, I just… is there any tooling, then, that… exist. I know there's the Weaver thing for generating some stuff with SEMCONF, but is there… Some tests… Sergey 15:08 it can understand what attributes mean, and what should be the values there. Like, I heard about this, we were… our Python guy that works on the Python language in Elastic, he mentioned it. What does it do, like, it generates spawns?
**Chris Lightfoot-Wild** 15:26 I think it reads the, semantic convention spec, and spits it out in the relevant language for you, so we… Sergey 15:35 Okay.
It just generates stubs.
**Chris Lightfoot-Wild** 15:39 Yeah.
**Sergey** 15:40 Oh, okay.
**Chris Lightfoot-Wild** 15:41 It's integrated in the PHP… Brett put it in the PHP ecosystem in the past.
It used to work some other way, I can't remember what it was, and then the Weaver guys were like, hey, we've got this new thing now, and please use that.
**Bob Strecansky** 15:53 Is this what you were looking for, Chris?
**Chris Lightfoot-Wild** 15:56 I guess… yeah, validating examples… Yeah, maybe, maybe something along that line.
in our ecosystem, I don't know.
**Bob Strecansky** 16:08 Yeah, it'd probably be worth a GitHub issue to, like, test this out and see what happens, right? We probably would get some really valuable information from that output.
**Chris Lightfoot-Wild** 16:17 Yeah, I'm not saying sorry as well, that in that example I linked, that may well have been valid, that it was fine to bump it, but it was like, is there a process where someone said, I've done this, I've checked the spec.
It's all good, and then we sign off on it.
Like that.
because I… I don't know exactly, but I feel like if we do just say, oh, we're emitting the latest version, but we're not, other implementations, depending on… Certain attributes may just break, or… Not behave very nicely.
**Sergey** 16:47 I mean, it sounds to me like… so it's probably the other way around, like, when is it even worth bumping version automatically? Because if we don't use any experimental attributes, then… even if we keep the old version, it just… like you said, collector should understand that, okay, if it wants to transform the data to be compatible with the latest semantic conventions, it essentially doesn't need to do anything, right? It can just keep them… it just bump the version automatically. So it can be decided on the collector's side.
But if we do use experimental attributes, then… It will be… there must be some component, maybe it will be part of the collector, that has this knowledge which attribute from this version was… how do you map it now to this latest version, right?
So now you need some kind of, like, thing that will be able to map experiential attributes between versions. But that needs to be done somewhere, so it sounds to me that it's never useful to actually automatically just bump the version to the latest.
Like, it doesn't achieve you anything, right?
**Chris Lightfoot-Wild** 17:49 Yeah, it feels like we're bringing roots, potentially.
**Sergey** 17:52 Excuse me?
**Chris Lightfoot-Wild** 17:53 It feels like it could just bring risk, there's not… there's no real… Sergey 17:57 I mean, what do you get? Like, it looks more kind of like that you keep up with the latest version, but why do you need to? Like, it's like, you know, like saying, okay, I, you know, sometimes in XML schema, when you produce XML document, you also mention what XML language you use as standard, right?
okay, let's say they released some new version, like, why would you go and always increment that standard? You know that you are conforming to the 1-0 standard, that's good enough, right? Maybe where it is from 20 years ago.
But all the tools understand it, and I can parse it. So, the same thing with this, like, if whatever component wants to rely on that version and map it to a newer version.
Okay, it will do it, but there's, like, I don't see what will be achieved by just bumping it automatically on our side.
**Chris Lightfoot-Wild** 18:43 Yep, okay, I'll, I'll go off and.
**Sergey** 18:46 But I do agree with you that if we want to make sure that whoever does have this itch.
to go and bump it than if we want some good procedure, Apple.
Good procedure around how do we test that we now didn't reduce some breaking thin.
Because we didn't inspect what attributes are being used.
**But it sounds to me that it should be cross-language, right? If somebody already developed this tool, and we can just take advantage of it, that would be nice, but… Chris Lightfoot-Wild** 19:13 Yeah, it could've been.
**Sergey** 19:14 how easy it is to do, right? You need to understand the meaning of attributes.
**Bob Strecansky** 19:18 Yeah, that's why I mentioned, I think, like, just… giving it a rip in a CICD environment and seeing what the output is might give us some really good insight as to how it might help us, what we might be missing, what the tool might be missing. I think that that would be a good issue to create and good work for somebody to try out.
**Sergey** 19:34 You mean to use this waiver thing?
**Bob Strecansky** 19:36 Yeah, Sergey 19:38 I mean, it sounds like they're placed in the right location to take care of this if they are the ones that, near this semantic convention standard.
**Bob Strecansky** 19:47 Yeah.
**Sergey** 19:47 I developed some tool.
Although I must say that I will be hard-pressed to believe that they can do a universal tool, because they essentially need to understand, okay, so what do these attributes mean in the context of PHP, right?
And did we use the correct attributes to actually refer to them, right? So that's, A little bit, sounds to me… Hard to do universally across languages, but maybe they did something?
Name it.
**Bob Strecansky** 20:18 Could be.
**Pawel Filipczak** 20:20 Is this weaver told, Is it used to convert the… the same kind of specifications to the language? I mean, to the headers or PHP files? Is that… that one?
**Sergey** 20:33 Potentially generate stubs, right?
**Pawel Filipczak** 20:34 Yes, yes, yes, okay, I, I, I am… Sergey 20:37 But maybe it has additional use cases, maybe they extended it.
Now to use it… because they talk about some checks, so you can use it after the generation to check something.
**Pawel Filipczak** 20:51 I was using it once or twice, but never seen anything like that.
But maybe they updated it.
**Chris Lightfoot-Wild** 21:00 Maybe… I can have a look into that, and then maybe, if nothing else, we could always just put a note on the PR template.
**Sergey** 21:07 The only thing that maybe I can see… this is something that I did in our legacy product for Elastic, we essentially used JSON, and we had schema for JSON. So if I wanted to make sure that the agent or SDK doesn't produce data that is incompatible with that schema, let's say, for example, it produces, some fields that are not mentioned in the schema, right? And I'm checking it against the latest schema, so there should not be such fields, because latest is always compatible, it should contain all the fields that were there. Or, for example, checking the types of the fields, right? If the schema says it should be int, I should not place a string there. So then, maybe this is what this tool does in sense of check. So it takes exemplar of data.
instance of generated document, and checks it against schema that it satisfies all the field names and the types of data the way it's specified in the schema.
So maybe that's what this check can do.
But obviously, it cannot check the meaning, right? The word semantic… it cannot understand the meaning that we place correctly… correct value from the point of view of meaning, incorrect attribute, right?
For example, if we call it IP, but we actually put, you know, domain there instead of IP, then I don't think it will be able to check, but maybe, maybe.
**Chris Lightfoot-Wild** 22:28 Cool, thanks. Sorry for asking a… Sergey 22:32 But I think, so you want to… you want that PR, so you want… you create the PR to replace references to the latest, to the explicit version?
**By the way, how did you select explicit version? Just based on the time frame when that was created, that instrumentation, or… How did you choose the exact version to replace the… Chris Lightfoot-Wild** 22:52 when I was doing, like, the messaging one in Arabelle, it was the latest at the time, and then I just looked at the, you know, what attributes were supposed to be there, and what the value Was supposed to be.
And then in a later version, the value had flipped, So you can't just bump the version, because it would break that… expected value. So that was one of the just things in, you know, in my head that's like, oh, perhaps we should Perhaps there should be some sort of safeguards around it, and that's why I was posing the question, so… can have a look into this, and then report back, I guess.
just see if it does need to be a prompt, that the tool can't do it, so please, you know, sign it to check it, and we've got a tick box on the PR or something.
That says it's been done.
**Just… I don't know if there's a better language to use as, like, you know, a poster child for… following their lead. If Brett was here, I'm sure he'd probably say, lean on Java for that, so I could probably start with… with the… Sergey** 23:55 Cover cello.
**Bob Strecansky** 23:56 Java or Go, because Tigwyn is one of the Semitic mentions people, and he works on the Java SIG, so I'm pretty sure that those would be a relatively good one-to-one mapping.
**Chris Lightfoot-Wild** 24:06 Unless… Bob Strecansky 24:08 You're okay.
Okay.
So… The release today, I'm going to perform a release of our product today. We haven't done it in a little bit. Brett shared the release process with me, because I had not done the new release process with the Git Split, but I'm planning on doing that later today. I'll post on our channel when it's completed.
**Sergey** 24:33 When you say release, you don't mean 2-0, you mean the new miner?
**Bob Strecansky** 24:37 Yeah, new minor, that's correct.
**Sergey** 24:40 written.
Okay.
**Bob Strecansky** 24:42 Yep, so that is… It's on my plane, Hal, looks like you have Distro donation blog posts.
**Pawel Filipczak** 24:50 Yes, I created pull request and issue.
So I would like to publish the blog post on the OpenTelemetra IO.
**Bob Strecansky** 25:00 Got it.
**Pawel Filipczak** 25:02 And, yeah, so… I added you as a SIG sponsor, or something like that, so… Bob Strecansky 25:09 Okay.
**Pawel Filipczak** 25:10 I'm not sure if you should click something or not, but at least you can make your… put your opinion on the… on the PR, or engage.
**Bob Strecansky** 25:21 Alright, I will read through this later today.
**Pawel Filipczak** 25:24 Yeah.
**Bob Strecansky** 25:27 You're welcome.
**Alright… Pawel Filipczak** 25:31 I mean, all of you, except Sergei, because Sergey is, of course, the.
**Sergey** 25:35 Did you… do we want… do we have already a release? What is the order you want to deploy.
**Pawel Filipczak** 25:41 So, I'm working on the release today, so… I guess that blog posts will take some time.
Because of all of those stages, reviews, and all of those procedures, but anyway, I would like to make a technical preview today, or tomorrow, and… And, yeah, and I'm also working on the documentation, so we have the Markdown docs in the repo, but I talked with Savari Neumann.
And he told me that it's better to keep the docs in the same place as for any other technology and product of the OpenTelemetry.
So, I will move it to the OpenTelemetry I.O, and I will make it just in the auto-instrumentation folder in the tree of the documentation.
So, yeah, I'm working on that, and I will create bullet requests soon, so… So, yeah.
**Sergey** 26:45 So, essentially, we can maybe ask you guys, so if I understand the order, so maybe we can, if we go ahead and publish the technical preview version.
We'll let you go, guys, and maybe you can give it a try, and let us know, and then we can make you maybe… So, it will… we can do it even before the blog post, so maybe if there will be some serious things that we need to fix, we can do it even before the blog post, right?
**Pawel Filipczak** 27:10 So the blog post, it's mainly about the, you know, official release, not the technical preview, but yeah, you can always… Sergey 27:18 You want to publish it only after we'll have official release, stable one?
**Pawel Filipczak** 27:22 No, I want to publish this as soon as possible, and it doesn't matter if it's technical preview or feature release, and of course, I asked you for the feedback two weeks ago, so if you had a chance to test it.
with these custom-built packages, I'm not sure if they are still available to download.
But anyway, Please take a look, if you will.
Had the chance to do that.
**Sergey** 27:49 Yeah, so we can also, again, send the link on the Slack when we have a technical preview version, which should.
**Pawel Filipczak** 27:55 Who's been a really serious?
**Sergey** 27:56 Not disappear ever, right?
**Pawel Filipczak** 27:58 Yes, yes, yes, yes, yes. And if you will make a release, then the files will be available in the releases page, or tab on the GitHub, so it will be available officially for the download.
Not only as a, you know, result of the… of the… of the stage of the build, right? But… but the official.
Sorry for interrupting you, sir.
**Sergey** 28:24 Oh, no, no, just, I think I interrupted you. But, yeah, so… so… the way I see it, the order is probably… we definitely would want you guys to let us know if there are some issues that you think should be fixed.
That were definitely before the release, or maybe even before the blog post, but… so that's why, essentially, we are making this technical preview.
The biggest part that is missing there, just in case, maybe we'll also stress it in release notes, is that we didn't merge yet the shading part that I mentioned a couple of times. So, essentially, it means that depending On the application that you use, if there are some dependencies, even transitive ones, right?
that we bring with the distro, like, everything that SDK brings, translpendency, SDK itself, if there is a different version that the application depends on, and if those versions are not compatible, like, let's say, for example, PSR log, right? What we encountered with the tool, I think it was in Composer even, right?
When Composer had dependency on PSR10, and SDK broad 2-0, something like that.
So if this happens, then distro, this technical preview of Distro, cannot handle it yet.
So this is the next big thing that we want to do. So essentially, it will only work with applications correctly that don't have dependencies not compatible with SDK dependencies.
Right, so, obviously they'll work with simple applications that don't have any dependencies, so… Yeah, so… just a heads up, that's why we essentially call it technical preview. That's the last big thing that we want to merge this shader and thing.
That essentially will hide all the dependencies that we bring with Distro, so they never clash with, did benefit the application has.
**Chris Lightfoot-Wild** 30:08 Cool, yep.
Sounds good. I'll try and give that a go.
**Bob Strecansky** 30:16 Alright.
Chris, Code Quality Tools.
**Chris Lightfoot-Wild** 30:20 Sorry, I snuck that in. I know you're.
**Bob Strecansky** 30:23 That's alright.
**Chris Lightfoot-Wild** 30:23 Well, Mago, or Majo, or however you… Bob Strecansky 30:27 Yeah, yeah.
**Chris Lightfoot-Wild** 30:28 But, sort of, in lieu of that being, you know, available or whatever, or any decision on that?
The PR I've got with Laravel, I've, like, kind of got it there functionally, as a base point, then the CI just blows up with all the various… I think we've got 4 different cold calls tools, SAM, SAM, PHP Stan, and PHP CS Fixer.
There's one of the packages, I think it was, like, a plugin that was tied to Pharma or something like that, and it's pinned at an older version, it doesn't recognize PHPA attributes on some of the tests, et cetera, and thought errors, but then there's no newer version of it.
**I don't… Bob Strecansky** 31:14 Of course, there's not.
**Chris Lightfoot-Wild** 31:14 So, when I was like, oh, hey, ChatGBT, can you just decide if I can actually fix this with some odd, like, chain of dependencies?
And it just made up a version that doesn't exist, to be like, hey, try this, and, you know, that'll do it. So, digging a bit further, the suggestion was, like, you've got a lot of code quality tools here that some of them overlap and conflict, and it's… it's obviously painful as a developer to just try and get it over the line with all the CI failures, already, so that's kind of been holding people back, and it's frustrating that like, even FAN, for example, I'm pinned on an older version because of that, and I wonder if… does it give us much? Like, we've got all the various tools there, can… can we drop FAN on one of them?
**Sergey** 31:55 Well, first of all, pinning the versions of those tools is an absolute must. It's interesting.
You still don't have it? Like, in main, they're not pinned all the versions of all the tools, static analysis?
**Chris Lightfoot-Wild** 32:05 Also, sorry.
**Sergey** 32:07 So, what you're mentioning, I think we did it in legacy in our agent, we only use PHP stun, but even then, we quickly understood that we cannot allow it just to automatically get the latest, because then we cannot rely on build being stable. So, we pinned the… Chris Lightfoot-Wild 32:25 Yeah, I guess we've got minimum version constraints, at least, but .
**Sergey** 32:30 I don't know, it doesn't work with tools like that, it must be.
**Chris Lightfoot-Wild** 32:32 Yeah.
**Sergey** 32:32 Because they're technically not backer compatible, right? They will discover additional things in newer versions, and that's it. Your build is not repeatable.
So that's absolute must, but… but the second part that you… so that easily can be fixed, right? Obviously, you need to remember from time to time to upgrade that version, which… will involve also maybe fixing the failures that it will find. But the second part, what you mentioned, is that, okay, you're trying to use all the tools.
**Maybe that's kind of, like, too much, right? So the question is… Pawel Filipczak** 33:03 once I tried to fix one issue with the CS fixer, and it led me to the… back in the second tool, so it was insane just to keep them work together, because for one, it was force positive, for second one, it's… it was… it was okay, so it's… Sergey 33:21 Well, actually, it's interesting, guys, that you didn't arrive to put in just ignore, right? So, almost all these tools should have ignore, kind of like.
Comment or thing, so you can just ignore stuff.
**Chris Lightfoot-Wild** 33:33 Well, then that's what it feels like the majority of the pain is, I'm just going and adding ignores everywhere for all the various tools.
**Sergey** 33:39 Yeah, so that's… sometimes you need to just say, okay, that's too much into… so if ignoring, and it just, you know, litters the code with all those ignores, okay, then it's too… So my question, essentially, to you guys is.
Do you think maybe we can let go of a couple? How many? But it's interesting, I've seen Fixer, I'm familiar with it, maybe you put some plugin there, but I'm only familiar with it in the sense of… checking the syntax, it doesn't understand, or at least we don't use it in Legacy Agent as a understanding of control flow. For that, we use PHP stun.
So Fixer for us was only to, to check, you know, like, code format and stuff. It only understands the formatting, new lines, what needs to be on what line, but just to satisfy the whatever SIG standard that we wanted to… not SIG, I don't remember, but FIG… Whatever standards that you have for code formatting.
**Bob Strecansky** 34:34 Fig, Fig, Stan, Stan.
**Sergey** 34:36 Yeah, whatever three-letters, thing that they have there. But, I didn't know that it can also kind of, like, compete with PHP Stan, like, for static analysis. But anyway, all I'm trying to say is that, Ken, maybe we can stay with one tool, select one tool, whatever is the… Maybe consensus is the best one?
**Bob Strecansky** 34:56 Listen, so… Pawel Filipczak 34:57 Last time you mentioned the tool implemented in Go, right? Or in Rust.
**Bob Strecansky** 35:02 Rust, yeah.
**Pawel Filipczak** 35:04 Yeah.
**So, like… Bob Strecansky** 35:05 It's… so my… my two cents here, I'd like to start a community discussion about this, because I don't think that one person should make this decision. I think that my… like, too long didn't read my opinion would be we should take this PR that I have with Mego, and either ignore all of the lint and formatting that it has, or apply it.
And both of them have positives and negatives. And then, from there, we can deprecate some of the other tools that duplicate it. But again, I would like to get feedback from the community before we just, you know, load that change.
**I think we can put it… Sergey** 35:44 When you say lint, is it kind of, like, in the area of HP Stan? Is it… does it do kind of, like, static analysis of the… For example, can it understand, let's say, if you return the wrong type from function, is it capable of flagging that?
**Bob Strecansky** 35:58 I think so.
**Sergey** 35:59 Yeah, okay, okay, good.
**Bob Strecansky** 36:02 So… Chris Lightfoot-Wild 36:02 I think.
Sorry, go on.
**Bob Strecansky** 36:05 I was gonna say, I'm happy to start that discussion in our… Slack channel, I think that's a good place to start, and then we can go from there.
**Sergey** 36:11 To tell you the truth, like, my immediate reaction to the fact that it's implemented not in PHP is a little bit apprehensive, because I wonder… how… how well it will stay abreast with the tools like PHP Stunt. So, obviously, most of the tools that do the static analysis, they are implemented themselves in PHP, right? And people that implement them, they are motivated because they're probably developing PHP also maybe at their main job, or whatever. Now, here.
I find it strange, they… so I wonder, like, what kind of group of people I guess maybe they just chose to use Rust, but they still depend on PHP for their main job, so they will stay abreast with it. So they will invest this additional effort of essentially taking a tool like PHP Stan, whatever additional checks it adds, and re-implementing those checks in Rust.
Just for them to… I guess the main advantage is that it will run much faster. Is that the reason to do it in Rust instead of just staying with PHP?
**Pawel Filipczak** 37:12 Sergey, Bob showed the list of sponsors, and the JetBrains is the main sponsors, sponsor here. I guess the reason why they implemented that is just to make the IDE faster, so I guess the speed is the main reason here.
And even if the community is not so high vehicle-like for the PHP stand.
**then I guess, if it works, then it works. It doesn't matter if it's, you know… maintained by the… by the PHP users. I'm… I wrote something in PHP in my life, and I never updated the PHP stan, so… Sergey** 37:53 Right. No, look, I'm fine. I'm just, I'm just trying to see, like, if there is, if there is kind of, like, compatible interests between this team, if it indeed being sponsored by somebody who wants to make sure this tool is kept up-to-date, even though people… Because, for me, it was just a little bit of a mismatch, like, why would people that are interested in implementing stuff in Rust would be interested in continuing to support the PHP? But it sounds like they just want to optimize, that's why they converted to Rust. Fine, let's.
**Bob Strecansky** 38:25 Yeah, I think… I think that's always… that's always a risk we have to be concerned about, right? Like, there's always a chance, like, what is motivating somebody to keep up PHP stand or CS Fixer, or any of these… it's like, the open, you know, the classic XQCD open source picture.
**Sergey** 38:41 Hmm.
**Bob Strecansky** 38:42 I think… if… to… I have… another thing that we can do, at least temporarily, is we can enable this and make sure… and, like, watch it, It does, I mean, it takes… it takes, what, 11 seconds? So it's not like, it's not like it's a huge add to our CI-CD pipeline, and then we can see it over the course of time and see what happens, but… Sergey 39:04 But I think maybe… What do you think about this idea? Maybe we can do it in two stages. Can we select only one? Like, just… so I think there are two kind of, like.
The way I see it, again, maybe I'm seeing it incorrectly in part. So, the way I see it is we have existing tools, like the SpeechP stand, fun, and maybe a couple more.
If we select just one, keep one of those, right, it will immediately simplify the situation now, and then we have this new tool that also becomes a competitor, and then we can decide, okay.
what is we decide between this one that we kept from the existing ones against this one, new one, right? And that's gonna be the finalist. So, maybe we can do it in these two stages. And also, it'll help us then later to decide if this new one is good enough, right? Because we can just directly compare… We can, on purpose introduce, or maybe it will be not even on purpose. Maybe we'll see that this old one discovers issues that this new one didn't discover. The problem here is that we also need to take care of the, you know, what is called false positives, and false negatives, right? This tool might not be, you know, flagging too much, and it is good, but on the other hand, if it doesn't find the problems, then it's not… it's also not good, right?
**Bob Strecansky** 40:17 That's… that is why I proposed checking with the community and running it in parallel, because it will allow us to see the difference. It'll allow us to see if somebody goes, oh, no, you don't want to use that tool, we had, like, a huge production bug with it, or, oh, no, you might want to… you may want to use Mago, but you also want to make sure that you keep PHPCS Fixer with these, you know, I think we might get some feedback.
From the community about this, and running it in parallel will also help us to build confidence that it will perform the tasks that we expect it to, and maybe catch some new things that we previously did not have.
**Sergey** 40:52 So for now, do you… do you want to keep it… do you want to introduce it in main, main CD, workflow?
**Bob Strecansky** 41:00 That's my plan.
**Pawel Filipczak** 41:01 But with blocking, or just for info?
**Bob Strecansky** 41:03 Not block… not blocking, just, just to, like, to build an archive of tests of that to make sure that it follows the same patterns that our established CICD pipeline follows.
**Pawel Filipczak** 41:15 So, one question here, is it possible to get the reports from both tools? I mean, for example, PHP Stan or… and Mugo?
and then compare them? I mean, you know, maybe they are generating the reports in the same format, and we can somehow compare the results.
**Bob Strecansky** 41:34 I don't know, I would assume so.
**Sergey** 41:38 I mean, we will get the reports for all of them, right? They are run in parallel, or sequentially, but they are not stopping the build, so there will be reports from all the tools Existing tools that now run, do they stop the build? Do they allow next tool to proceed, or how does it work now?
**Chris Lightfoot-Wild** 41:56 Close up.
**Sergey** 41:58 No, it stops the build, the moment it fails.
**Chris Lightfoot-Wild** 42:00 There's no continuer, I think if it fails the formatter, then it… it blows up.
But then you're sort of going through, I'll fix the SAM ones, and then I've fixed the PHP SAM ones, and then the CS fix, it just… yeah, it's… feels like a battle, and I'm glad that a greater mind like yours, Powell, has also hit snags in the past with fighting these tools. At least it's not just me. But it is obviously very frustrating, because I feel like I've done the meat of the stuff, and now it's just trying to make the pipeline happy with all the competing tools.
And the dependencies that don't play nice together?
So, obviously, that would be… if you were to… when you put that in the… to the community, Bob, that's one of my, sort of.
Strong points in that it breaks away the dependencies in the project to some external thing instead, and… We don't have to fight those instead anymore, do we? But… Yeah, it'd be good.
**Sergey** 42:55 I wonder, maybe as a temporary… maybe we should introduce something like consensus thing? So if we run those 5 tools in parallel, and if at least 3 of them flag a problem, then we fail the bill.
But if the majority says that it's possible, Then they say, okay, no.
We will not fail the build, based on the majority of these tools.
**Pawel Filipczak** 43:16 And my opinion is that we are, you know… thinking about the service, talking a lot about, you know, how these tools… I mean, I'm getting this… I'm understanding this, like, we would like to get as much, you know, go as much deep as is it possible to detect the problems in the code, but maybe we should not, you know, be so strict, and maybe we can just, you know, I think that I'm not, you know, a fan of Mango, I don't know this tool, but maybe if it's very fast, and you can run it every build, every second, or you can check the source code very easy, and it's very fast.
And you don't have to install all of dependencies, you don't have to run Composer every time to update something. So it's ease of use is the main goal here, that you can check your code quickly.
So the quality is much better, even if it has some, you know, lack of features, or it's not analyzing the code so deeply.
**Maybe it's okay for us, so maybe we should just… Sergey** 44:31 But one thing doesn't contradict the other. You can run, like, for example, if you choose locally to run only the subset of checks, right, because you want them to be really fast.
You can do it locally, just for you not to send… if you want to save yourself time to commit, and then see that it fails on CI, you say, okay, I will run subset of checks already locally, then I will minimize the chance, but on CI, you can still run more checks, right? It can still be done in this way.
**Pawel Filipczak** 44:59 Yes, you can, but… from my experience, if I'm… if I'm… I can't run something locally because it's too big or it's too heavy, then I'm not executing anything, so I'm just pushing into it, waiting for the CIA results. So, it's, you know… Sergey 45:16 But the way you construct these checks, you can make, you can construct them in such a way that basic checks.
especially the fast ones, you can run them easily, right? And they will be the same as the run by CI. It's just that there will be more advanced checks after that, that you can say, okay, I will not run around them locally because they're heavy, so it's just easier for me to push and see what CI says.
**Pawel Filipczak** 45:36 Meow.
**Bob Strecansky** 45:37 I always have a difficult time making this decision, because, like, okay, yeah, we can run… you can run the easy CI-CD pipeline checks locally, but they're gonna run again in the CI-CD pipeline anyway, so… it's really just, like, are you… I guess it really depends on how your developers work. If they are committing often and pushing to branches and seeing the CIFCD pipeline run on a consistent basis, that's good if you're doing a lot of local development and then only pushing up every once in a while, but… You may be… you may benefit from pre-commit hook checks, but, I don't know, I tend to favor… I tend to be with… I tend to favor, like, doing all of them in CICD and keeping a consistent user experience, rather than, like, having some of them locally and some of them in CI-CD. Which ones do you keep locally? When do you determine… it's… I think, like, the cognitive overhead of doing that is… tough. I understand why you may want to do it. I'm of the opinion to, if possible, there's no reason why you shouldn't be able to run any CICD check locally. I feel like they need to be first-class citizens all over the place, so that way, if you're concerned about one, you can run it locally, and then you can run it in the cloud. I've… I've been of that opinion for a long time. To me, every CICD check should probably just be a bash script.
Or, you know, functionally equivalent, right? Like, I should be able to run it on my laptop, I should be able to run it on a CI-CD pipeline, I should be able to run it on my toaster. Like, that's… to me, that's where you get the biggest output.
**Sergey** 47:04 No, I mean, technically, you're right. You… but the question is, what about time that it takes, right? It's less of a issue of the… how hard it is for you to… it might be one-liner anyway, right? And Powell showed me that there is a tool that completely simulates the GitHub workflow locally.
**Bob Strecansky** 47:22 Oh.
**Sergey** 47:23 So you can just run it locally, it doesn't matter what it does.
**Bob Strecansky** 47:26 That's true. I think the other thing that is always difficult is we have lots of different kinds of developers with all sorts of different machines in all sorts of different situations, and supporting that is a non-zero overhead. If you have all these checks run in CI… like, in the CI-CD pipeline, we at least know we are going to be consistent in those runs.
**Sergey** 47:48 Right. So, I mean… Yeah, but I think in any case, so, yeah, I think trying to find, you know, something universal. Obviously, everybody have their own tastes, the way they work, so trying to, you know, find something universal probably would be impossible, but I'm saying, I think we all agree that using all the tools was a little bit of too much.
Unless maybe Brett will have some motivation. I don't know who was behind the decision. Maybe there will be some interesting arguments why it might be beneficial. So, yeah, I agree with you, Bob, that opening to community and hearing opinions.
But, for now, I'm just trying to say, okay, let's… I wonder if it's worth… but maybe not. I thought maybe it's worth splitting into two stages, like I said, maybe keeping only one from the old ones, and then against the… and then, you know, beating them against this new one, but maybe this new one is even… will immediately be voted in as the best one anyway, so we don't even need to decide Whom to keep from the old ones, so maybe we'll save ourselves, Making two decisions, maybe just one decision will… so will.
**Bob Strecansky** 48:50 Yeah, I have a strong feeling we'll get meaningful… I made that post in the OTELPHP channel, but I have a strong feeling we'll get signal from that, and just from running it in CICD as, like, our PR, because the more data we get, the more data-driven decision we can make.
**Sergey** 49:10 Yeah, I wonder, maybe we can use AI to analyze all the runs and tell us, like.
I don't know what kind of analysis we can do. Say, okay, what are the outliers, right? Like, if, for example, we see that this tool can, like, constantly flag stuff, and the rest of them don't, then maybe that's the outlier, maybe too many, kind of, like, true, false positives? I don't remember what is the terminology, but whatever. Yeah. And try to see what tool is, actually always errs on the side of, Flagging too much, and the other way around.
**Bob Strecansky** 49:41 We also have the ability to do sort of the same thing, but with, like, fake, like, automated remediation, right? If we decide that this new tool is wonderful, but it has a bunch of links and formats that it wants us to fix, we can always say, hey, hey, Mr. Claude, please help us out with changing all of these formatting things. And we have, I mean, we have a good enough… to me, we have a good enough test suite to have meaningful signal from the output of that AI-generated refactor.
As long as it's not re… as long as it's not refactoring the test, too.
**Chris Lightfoot-Wild** 50:17 Yeah, it just… obviously, we've got, like, we do have all these tools in place, but the pipelines are just failing all over the shop anyway. So, like.
**Bob Strecansky** 50:26 Yeah, but it's, like, innocuous failure. I think we should definitely… like, to me, that's, like, a separate but also equally important issue. Like, we need to fix that so that we have meaningful signal, and so that new contributors don't go, oh, this repo's broken.
**Chris Lightfoot-Wild** 50:41 Yeah, and it'd be interesting, I guess you'd never know, but how many people just turned away, because it's, like, too much of a pain to get it all green again, sorry.
**Bob Strecansky** 50:50 Yep, agreed. So, that… I think that should be somebody's priority.
**Sergey** 50:54 But I think, pinning the versions of all those tools, I think that can be kind of like… I think we can agree that it's a good thing to do even immediately, you know? Like, because we don't want any new build to be kind of, like, completely unacc… Unpredictable, and it can break it any day, depending on which release they made on those tools.
**Chris Lightfoot-Wild** 51:14 Yeah, in that particular example I had faced, though, that pinning to an older version meant not using newer language features, and by that was, like, PHP 8 attributes that aren't actually that new at this point. We're on 8.5, I don't know, it's been a few years, and it's just… Because of some… Sergey 51:31 But do we need to go that old? Like, can we just, pin the current versions and… Chris Lightfoot-Wild 51:36 Well, that's what I mean… could I do it just for Laravel? Could I get rid of FAN? Could I try that out? I don't know. Like, obviously, who… who's… there's not… there's not many people chipping in at the Laravel thing, and obviously it's hinged on a decision from Way back when, so… not saying it's wrong, I just… Wonder if we can change the stance on it.
**Pawel Filipczak** 51:57 from my point of view, is the problem is, I mean, from the maintenance point of view, is that… Each, for example, in CountryPo, each instrumentation, each plugin, or whatever we can call them, has its own set of versions, and if we pin the versions to the… of the static analysis tools, then we have to change it everywhere in the… if we would like to upgrade.
the static analysis tool, then we have to change all of the composer JSON files.
Because they are… In the, in the each… each subdirectory, so it's also a problem here.
**Bob Strecansky** 52:36 I think the important thing to remember about Contrib is it's, like, it's a best effort, right? There are specific subject matter experts for each of those Contrib things.
That should, like, can be or should be maintaining them if they want to use them, and if not, then they die.
What'd you think?
**Chris Lightfoot-Wild** 52:54 You may be happy, then, if one of those things did get dropped from Laravel, Bob, you'd not be too devastated. Not for the PHP, the main OpenTelemetry repo, but the contrib one for Laravel, if it's… Bob Strecansky 53:08 I would… I would be… I would be a pig in mud. It'd be fine with me.
**Chris Lightfoot-Wild** 53:12 Okay.
**Sergey** 53:13 Yeah, I would definitely prefer to distinguish, right? There are stuff that we commit to support, because obviously, we should commit beyond SDK, right? Obviously, because SDK by itself really limited, really limited use cases. So I would have probably preferred maybe to have, contrib, and then something that tells… it's not exactly contribib, but it's part of the core thing, but it's not SDK.
So, I don't know, maybe we'll… we're thinking about it. But I would not say that, for me, contributes the same. So, yes, I agree with you about that. Maybe some things that will be contributed there, that will say, okay, this is on the best effort basis, and if people that contributed initially, they decided to abandon it, then it's probably not that important to the community.
not to continue maintaining it, but Laravel and Symphony, like, these things, they are… if they are not.
**Bob Strecansky** 54:02 Very important.
**Sergey** 54:02 of use cases of PHP users. I think we should take commitment on maintaining them almost to the same level as DK itself, right?
Because they essentially use the conjunction.
**Bob Strecansky** 54:14 I agree with you, but I'm gonna say yes and. Yes, that is important. The people that are responsible… the people that have subject matter expertise in Layer Bell and Symphony should be doing those. To me, I can't put all of my effort on the API and the SDK and then those things, so those things become a second-class citizen, even though they are very important to the ecosystem. So I agree with you, it's like, it is a best effort. It's not… like a… primary support vehicle, but I think… It's tough, right? You can't… we don't just have unlimited time to do everything, so… Sergey 54:49 Yeah, I agree with you, but maybe then what I'm trying to say is that maybe we can have, like, more than two levels of this, right? It's not like, okay, all the effort here, and then whatever is left there, we can say, okay, if it's down, okay, but… this is maybe on the what is left, but then this thing, like, for some kind of, like, IBM technology, that's even less. That's only if the original people that implemented it, if they decided to come back and take a look.
**Bob Strecansky** 55:14 Yeah. Yeah, it's true. It's like, I care… it's… And it's, like, that's so subjective, too, right? Like, I care more about Laravel and Symphony than I care about the Azure connector, or whatever, like, but maybe somebody that works at Microsoft would cares more about the Azure piece than the, Symphony piece, so, like, it's a… that is always subjective, so I think we just have to, again, best effort, make sure that we talk to the subject matter experts in those fields. I understand what you mean by having, like, a… one and a half class citizen, right?
**Sergey** 55:47 Okay.
**Bob Strecansky** 55:47 Symphony and Laravel and WordPress are so integral into the entire PHP ecosystem, we can't ignore them, or else we, you know.
**Sergey** 55:55 Yeah, obviously, I have a lot of different color glasses than you guys. We, of course, come from the corporate environment, and we obviously will take commitment on particular supporting technologies, so the moment we took commitment, and we mentioned them, and our documentation has been supported, then that's it. From us, it's not different than SDK. We must at least fix whatever is deemed as necessary by our customers. So, I guess, yes, it gives us a little bit different perspective than you guys, which you do on a completely voluntary basis. So, yeah, I would agree with you there.
**Chris Lightfoot-Wild** 56:27 Can I add a note under that, agenda point, then, that I can, you know, you're happy with dropping, or me… changing the tooling a bit for Laravel.
Potentially.
**Bob Strecansky** 56:39 If you want to do that, Chris, I will support you the entire way.
**Chris Lightfoot-Wild** 56:43 I'll add that in. I'm not… obviously, I see the merit in keeping the tool in, and I hope that… I presume, because you've proposed Margo, that you kind of lean in that way.
**Bob Strecansky** 56:52 My heart tells me that, but I want the data to support what my heart tells us.
**Chris Lightfoot-Wild** 56:58 Yeah, of course. And as you say, like, JetBrains being the main sponsor, and they sponsor the PHP Foundation.
I guess the likelihood is it's… that's probably the future, isn't it? But… I guess we'll see.
**Bob Strecansky** 57:09 You know, it's one of those things, right, like, you look at, GitHub stars shouldn't be a real indicator of whether or not you use a tool or not, but when a repo has, like, 4,000 of them, you start to think, like, okay, maybe this is something that people like.
**Sergey** 57:23 Are they just for PHP? Okay, so just for PHP, okay.
**Bob Strecansky** 57:27 2000.
**Sergey** 57:28 It's not like the tool that, does additional things. Okay, that's interesting.
**Bob Strecansky** 57:32 No, but it is a fascinating project to me, and I probably need to learn a little bit more about it, but… Sergey 57:37 Although, I would be interested if you open, like, when you will phrase that issue that you want to open to community, I would be interested to reading, or maybe if you want to cooperate, kind of, like, if you want to define how you're gonna, like, what's gonna be the measures that, based on them, you want to make this decision, right? So, let's say we run it for a couple of months.
What does it mean? Like, does it mean that it does find some issues?
doesn't flag too many non-issues, right? So it's really interesting how can we phrase, like, what was gonna be for us.
**Bob Strecansky** 58:07 Yeah, what are… Sergey 58:08 Successful experiment.
**Bob Strecansky** 58:09 what is the success criteria for making this our primary tool? I think… I don't have a good answer for that right now.
**Sergey** 58:16 size, obviously, right? You don't need to say, okay, it's that many, you know, that many days it ran without flagging too much, and stuff like that. It would be interesting to at least define it, like, what is our goal here? Some kind of, like.
**Bob Strecansky** 58:28 Yeah.
**Sergey** 58:29 Some, some way.
**Bob Strecansky** 58:30 I think, at face value, what I see as a success criteria for using that tool, rather than the ones we have is, like, is it a functional equivalent replacement for what we have now?
As we see… as we see, pull requests come in our CI CD pipeline, does it react similarly to how our current tooling does? And does it offer us any additional features or functionality? And we see that it offers us the additional feature and functionality of speed and simplicity, but we also need to make sure that it has freshness and correctness along with simplicity and speed.
**Sergey** 59:04 It's simplicity in the sense that it's much easier to employ, like, it's much easier to run.
**Bob Strecansky** 59:09 I mean, one tool, rather than four.
**Sergey** 59:12 Yeah, that sense, okay.
Nice.
**Bob Strecansky** 59:14 Cognitive overhead is a big thing.
**Sergey** 59:17 Okay, let's see. Yep. That's good.
**Bob Strecansky** 59:20 Alright, wow, we had a full… a full-time SIG meeting today, a good discussion, everyone.
Alright, well, I started that discussion in our hotel PHP channel, and we'll, keep up to date there. We'll see you all next week.
**Chris Lightfoot-Wild** 59:34 Cheers.
**Pawel Filipczak** 59:36 Come on.
