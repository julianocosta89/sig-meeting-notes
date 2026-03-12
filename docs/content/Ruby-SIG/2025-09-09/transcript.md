SIG: Ruby SIG
Date: 2025-09-09
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Eric Mustin** 00:40 What's happening, Arjun?
**Arjun Rajappa** 00:42 Hey, hey.
**Eric Mustin** 00:45 B.
Tuesday.
Where are you, where are you calling in from?
**Arjun Rajappa** 00:58 Bangalore?
India.
**Eric Mustin** 01:01 Oh, Bangalore?
Oh, okay. Well, I appreciate the, must be, what is it, 11.30 over there? It's quite late.
**Arjun Rajappa** 01:09 At 10.30, it's 10.30.
**Eric Mustin** 01:11 30. Okay, well… Hopefully, yeah, everyone just… No wonder.
**Wendy Smoak** 01:26 Hello!
**Eric Mustin** 01:29 I realize I'm chewing gum on college extremely late.
Come on.
I guess so early.
Whoa.
So let's give folks… A couple more minutes.
Ishwan.
**Hannah Ramadan** 03:46 Hey, everyone.
**Eric Mustin** 03:49 What's up, Hannah?
So we… Okay.
**Hannah Ramadan** 03:55 We don't have Kayla today, just so y'all know.
**Eric Mustin** 03:57 Oh, no!
**Hannah Ramadan** 03:59 I know.
**Eric Mustin** 04:00 Oh gosh. You guys might want to drop now.
That means I have to talk.
I'm just… I'm just… I'm, I'm, like, half… I'm only half joking, actually.
Okay, well, yeah, I don't know if, do you know if Rob or Arielle popped up last week?
**Hannah Ramadan** 04:21 Oh, Rob did, come last week.
And he said he's gonna try to come a bit more, but not sure.
Alright. Everybody's coming today.
**Eric Mustin** 04:30 No worries. We can, I mean, I, yeah, I was out, and I'm getting, a little bit… pulled into a few things at work, so I have done absolutely zero work on this, and have not reviewed anything. But I'm happy to play MC and kind of open it up to the floor, early, and Hannah, thank you for adding your… Your name, cool, I'll just, I'll just share my screen, I guess, Somewhere, here's… okay. So… Yeah, I wasn't here last week, so I don't know if there was any burning questions from last week?
I see, it looks like Rob has picked up the SEMCOM, updates that he's working on, like, to, to, you know, to support the new, sort of, like, Weaver format.
That's cool, that's awesome. And… I did not… Yes, Juan, I did not review your… either of your PRs, or even open them.
So I don't have any updates there.
And, yeah, I don't know. I'd pinged a Puma, Nate from Puma, and he didn't have any opinions on that PR.
With that in mind, maybe I'll do a 7… I'll try to do, like, a 5-minute spec sync update, and then we can open it up, if that works for folks.
I will take your silence as agreement, unless I've restated.
Okay, so… And then I did also notice, anyway, I'm being ADD.
So yeah, earlier today, looks like it was a smaller, nice. They also were at a small meeting. There was a… Question on… let's see, there's two questions, it seems.
The first one… is… extremely hard to understand language.
They are… Asking, okay, spec change around, I have no idea.
Something around enabling and disabling things?
That's a draft, and was open for comment, and I have no context or opinions on… So I don't need to dig into it.
I guess around when some of these changes to configuration should take place, whether it's immediate or eventually?
And then there was a… Open question.
Around… Dropping attribute value restrictions, they are… let's see… I guess relaxing some of the restrictions in the hotel proto?
Which… Previously had, only been supported in the log signal. I guess maybe now they are supporting some of these MarketPlex attributes.
They're enabling attribute types to be… Jesus. Very fair language. Extremely hard to… Understood.
Okay, looks like they're adding things that an any value can be… to include… Lots of things.
So, that's good.
I don't have any thoughts or opinions on it, and it's an open, question. It looks like in the SIG itself.
there was just discussion. Doesn't look like anything got merged, so… I think we're okay to cheat and just kind of, like, ignore the SIG this week. Not that we actually ever, like, followed too closely.
Okay.
And that's… that… that was 3 minutes or so.
So… that was a spec seg. So… I, does anyone have any questions or PRs on, on core, I guess, to start, that, people want to talk about?
**Wendy Smoak** 09:15 Couldn't someone open a PR in the channel? Ask about it.
Good afternoon.
**Eric Mustin** 09:20 Probably.
**Wendy Smoak** 09:21 Was that on court, or was it…
**Eric Mustin** 09:25 It's in Trib, never mind. Next section.
**Wendy Smoak** 09:27 Oh, no, sorry, that's Ariel, it's…
**Eric Mustin** 09:30 I did see… Nope, it's on there.
**Wendy Smoak** 09:33 Update upstream OTLP exporters to send a remote flag?
**Eric Mustin** 09:37 Yeah, okay, that's the one that, yeah. So…
**Wendy Smoak** 09:40 Some… they just posted a channel, so we should probably have it and see if someone can review.
**Eric Mustin** 09:44 Yeah, I had seen… it looks like Francis had looked at it briefly, and provided some, Yeah, or, provided some feedback. I think this is.
**Wendy Smoak** 09:57 Sounds great.
**Eric Mustin** 09:58 Yeah, yeah, I… I think span… you know, like, these, what is it?
the… the isRemote thing, we don't actually pass… we don't actually, like, expose at export time. Like, we don't pass, you know, so you don't know.
Which makes it difficult, probably, you know, probably the context here is they're attempting to do some sampling-related things.
And just looking for consistency. Looks like this guy's coming from Cygnos, who's a, you know, has a vendor backend.
Cool, yeah, yeah, and without that flag, they can't validate entry point spans, like, they don't know what's the start of a service.
Which is fair and valid, but looks like a lot of feedback has been requested. Well, huh.
There's still an open change. I guess we're one way… I can review and, you know, if I… time permitting, see if I have additional comments.
It does…
**Wendy Smoak** 10:49 I had not clicked it open, I just saw it in the channel, and…
**Eric Mustin** 10:51 Yeah.
**Wendy Smoak** 10:52 We usually have that list of PRs.
**Eric Mustin** 10:55 Yeah, that shows how organized I am for… why don't… let's fake it as though I was prepared.
**Wendy Smoak** 11:00 Sure, just paste it in.
**Eric Mustin** 11:02 Yeah, yeah, yeah.
You guys are all over beyond my 360 reviews.
But yeah, okay, so Francis had given feedback and a pretty thorough review. Yeah, what looks to be relatively minor, just like perf, you know, hey, we can get some micro, improvements.
And, but he still hasn't… it looks like that person has implemented all the requested changes, at least, so it's a matter of… I guess Francis will… See if, you know, see if he can update to approved, It does look like, let's see, an area I'll just… You're absolutely right. Oh gosh, is this a Chechy?
That's concerning. This is 100% auto-generated.
Am I wrong? Yeah, So, okay, looks like there's maybe some… additional Ariel, both Ariel and, Francis, probably still want to review it, or have to approve it. But yeah, seems… seems reasonable. I can understand why people would want.
On that, especially if you're a vendor.
Besides that, let's see what's going on. I guess check out what's going on in Contrib.
Unless anyone else had… Any core-related questions?
Let's see what we got, A bunch of bumps.
from… Dependabot, and then… Why was this opened? On a release?
For… a… a patch?
release on rack? Was that that there was, like, a circular dependency issue in there?
I think that was causing… some integration… Test to fail. Anyway.
Besides that, anything else come in?
Okay, there's a… oh gosh, there is actually a PR in here.
around middleware args, and then maybe I can… after that, Hannah, I think, this might segue into your Your, burden question, because I don't see anything else that's popped up over the week.
But let's see, looks like middle… they want to update… They want to update, rack… middleware works. So what does that mean?
They're saying that when we initialize… rack applications initialize middlewares explicitly, However, this doesn't take into account the new stability opt-in MVAR.
this PR ensures that… that ARGs bake that in, basically.
So… They've updated the rail time.
to… I see.
So previously, we were… I'm actually a little confused on what's happening here.
**Hannah Ramadan** 14:33 So… Yeah, what are they doing? So previously, what this change did was, depending on which environment variable you're using for the opt-in, it would prepend the middleware associated with whatever Santa convention you want to use.
I… Don't… see what they're doing here.
**Eric Mustin** 15:00 I think in… so… In our rail tie, were… Yeah, I gotta understand, there… What?
It doesn't? Okay, use… Yeah.
**Hannah Ramadan** 15:28 Looks like… Yeah, it almost looks like they're… Undoing some of the previous.
**Eric Mustin** 15:35 Yeah.
**Hannah Ramadan** 15:36 work.
**Eric Mustin** 15:38 Yeah, I, I mean, it's a draft, so… maybe… I guess I'm confused on the use case he's saying is broken, or what's the issue?
Need to initialize?
**Hannah Ramadan** 15:57 Yeah, I'm not really sure what… because I think it was doing that.
Well, I guess it's in draft, and…
**Eric Mustin** 16:09 Basically, I think if you're just, like, if you're… just using a rack app, if you just have a rack app, I think is the context here. It's like, assume it's not, you know, Rails or Sinatra built on top of Rack. Like, you just have a rack app.
You can't, like, auto, you know, the instrumentation is, like, you have to add the middleware yourself.
In his example, you have to explicitly pass this use block in.
But he appears to be saying that when you… like… you… I don't know. You're not able to determine… you're not able to, like, use the MVARs, I guess? Like, make that stability optimum determination in that case?
Cause all you pass in is the… I don't work, but… Yeah, right.
You're not, is that right?
**Hannah Ramadan** 17:15 You know what, I'll take a look at this.
**Eric Mustin** 17:17 I'm so… I think, he's added this determined CENCOM, and then… You… call the… right. So, previously you just called, like, this one… Method here. But now, because you have to, like.
the… it's not clear what your… when you have a rack app?
you're… you would have to have either… now, like, if you're just instrumenting your rack app normally, and you say, like, use OpenTelemetry, instrumentation rack instrumentation, dot instance.middleware args, like, you don't know whether, say, like.middleware args old…
**Hannah Ramadan** 17:55 Or a dupe, or… or whatever.
**Eric Mustin** 17:58 And that's not… that's sort of, like, implicit, You know, evaluation isn't baked into, any of the methods you can pass in.
So, like, you'd either have to, in this case.
Like, if we go back to this conversation with this demo… In this case, if you wanted to support the stability opt-in, like, you'd have to bake in that logic yourself right now, if you just have a Rack Builder app.
Which is probably not what we want. We don't want you to have to write a bunch of, like, stability, you know, checking environment variables.
we just want you to… to pass in the instrumentation, and then… It will, you know, make that… it will make the resolution for you.
So, I don't know if he's implementing it the right way, that's like… because he's just, like.
Yeah, I think he's… Basically, he's, like, has this… .
**Hannah Ramadan** 18:52 Yeah, actually…
**Eric Mustin** 18:53 This same middleware exact, but it has, under the hood, it does, like, the inference of what it's supposed to be doing, and then sends.
**Hannah Ramadan** 19:00 Yeah, actually, Stepping back, it does actually… Makes sense, so maybe this is actually a good… It may be a…
**Eric Mustin** 19:09 a use case we haven't thought about. I mean, at minimum, like, there's no test, so… and it's in draft, But, yeah, why don't… I'll comment on this and say, hey, like, just to confirm.
And I'll tag you, are you looking… you know, is your use case currently that, like, you want to be able to… you're building a rack app manually? Let's just, like, confirm his use case, which seems to be valid, but, yeah, isn't something… I certainly don't have, like, any just, like, standalone rack apps floating around.
I guess I could fill one.
Let's confirm the use case, and then, make sure that, It's just, looking at it quickly, it seems like he's… Yeah, Let's make sure we're not breaking anything, but yeah, this, like, okay, the analyzing stuff, let's at least ask for, like, a test as well. And like, I guess there ought to be a test saying, like.
In our rack instrumentation, saying, like, if you're just passing in this method, will it make the determination without having to explicitly check the MVARs, or something to that effect? But yeah, it seems… okay, seems reasonable.
Why he wants this.
I don't know, it's, you know, kind of an edge case. I don't know how many people out there are doing this, but cool. I, I'll comment and tag you, and we can follow up async.
Cool. Besides that, let's, that's all I had. I'll just… I'm just looking for clarification.
Okay, great.
Alright, well, that's all I got. That's my… my job is down here.
Does, do we want to move on to burning questions? Does anyone else have any, Thoughts, feedback?
Concern… Okay, we're not gonna move on to… yeah.
Yeah.
Yeah.
**Hannah Ramadan** 21:35 Okay, so… I think so, Eric, so… A while ago, when I was looking at doing some additional, like, SQL processing work, to add an attribute.
it was discussed, I think Arielle brought it up, that perhaps if we're creating, like, new code that does some kind of, like, SQL processing, and it's shared between multiple libraries, it makes sense to put it into the SQL… some kind of, like, SQL gem. Right now, we have one called SQL Obfuscation.
But it was brought up that maybe it'd make sense to rename that, which I guess is… basically deprecating the SQL obfuscation gem and kind of creating a new one. I think the name that was tossed around at the time was SQL Processor, so that we could have the obfuscation code and any other SQL processing code live inside that particular gem.
I wanted just to see if, you know, I've never done any kind of, like, gem deprecation, Or, like, I know we're in… In early, like, we don't have any… major version, so, like, we kind of do have flexibility to, like, do some of this stuff, but I wanted to see what anyone… if anyone had any, like, particularly strong feelings about What it would take to, like, rename a gem and basically, like.
have people stop using the SQL obfuscation, move all the code into a processor.
**Wendy Smoak** 23:05 Is there anything unreleased in the old one? Like, that got merged that hasn't been released yet? I don't know if… is that automated? It just magically happens when you merge domain, maybe that's not… Something that could happen.
**Eric Mustin** 23:17 There's… no, that could happen.
there's a… there's, like, a GitHub action there, you know, that admins have to… Anyone can open a release PR, but then… Yeah.
**Wendy Smoak** 23:29 Okay, I would just want to make sure that we've done a, like, a release of, like, if there's anything out there that maybe hasn't been released, like, just… Release that one one more time, and… Right. Say that it's the last time this will ever happen.
And then, like you said, you basically have to make a new one and copy stuff over, so…
**Hannah Ramadan** 23:47 Right.
**Wendy Smoak** 23:48 If there's anything you don't like, here's your chance, should change it, and then…
**Eric Mustin** 23:52 Yeah.
Yeah, I mean, I think, in theory, we're basically just pub… Like, we're publishing a new gem, and then because this is mostly internally relied on, like, I think it's mostly something that, you know, is just for dryness.
But it's, you know, like, I don't think there's really any or many folks who are, like, directly pointing at.
**Hannah Ramadan** 24:14 Good point.
**Eric Mustin** 24:15 this gem, it's just mostly getting, it's a dependency of our other, like, database, related instrumentations. I doubt, like, no one's not gonna kick up any fuss, I think. I probably do, but yeah, it should be fine. It's not like we're going to delete the… we just will stop publishing new versions of the old gem. It's not like we're not going to have a… like, I would have concerns around typo, you know, like, typo squatting or something, or squatting on the old chimney, but it's not like we're… Pulling that gem, or just, like, having a final release of it.
So yeah, I do think at the hotel level, there's a, there's some prescriptiveness around how the… like, the cadence that you do deprecations, and it's, like, there, you know, I… who am I talking to? Like, you know this all too well, right, Hannah? Like, there's some… some, you know, they like to have some, Ceremony around saying, like, okay, for this many versions, you… give a warning. I don't remember what that is off the top of my head, but yeah, like, I certainly support, holistically, what you're saying. I think it makes a lot of sense, to have a more, like.
SQL-ish, you know, anything related to touching SQL stuff, Jim, rather than one that explicitly just does obfuscation of SQL queries. I think, you know, there's… other… you know, actions we want to do. It's a little bit of a… Hard. You know, like, whatever, leaky abstraction problem, where, like, we don't know in the future, maybe we'll want to, like, abstract things further into just, like, any HTTP client-related span helper gem. But, like, yeah, I think this is a good abstraction, just, like, SQL-related stuff gem.
And… yeah, we'll just have to be thoughtful about the deprecation plan, you know, like, Deprecation roadmap, and then also, just making sure that we update the, you know, like, the gems which depend on it, and do, you know, ensure that the timing of those releases goes out in the right cadence, because we'll first have to cut A release of this new gem, then we'll have to go around to all the other ones, point them at the right, the updated new package, or whatever.
And then, like, I guess there's a question of, like, docs. Like, do we… we'll have to go find, like, you know, orphaned references and stuff in docs and update?
But yeah, I'm on board. I think it makes a lot of sense, and I'm sure in, like, 2 years, we'll revisit this, whoever's… if I'm like, we're all still around, and be like, hey, now we want to call it, like, a new thing, but that's okay, like… Nuh.
Yeah, I don't know, so… Arjun, Sean, do you… Or Hannah, what do you think?
**Hannah Ramadan** 26:59 No, I think both the… yeah, thanks, Sean, for the thumbs up. I think that sounds great, super helpful. Also a good note on… probably not a lot of people actually don't like using this gem directly. It is kind of used internal, so that makes me feel a lot better about it. Yeah, I think that's something… hopefully SQL processor is a broad enough… Turn this.
**Eric Mustin** 27:19 Yeah.
**Hannah Ramadan** 27:19 to do this again. But, I think if that sounds good to y'all, I'll probably just go ahead and get started on… research on that, and then… Yeah.
**Eric Mustin** 27:29 Okay, yeah.
**Hannah Ramadan** 27:30 Excellent.
**Eric Mustin** 27:32 Naming things is hard, I think. That's one of the rules, right? Caching, naming things.
Counting, Okay, yeah, that makes sense to me. I don't have… I know there's some open PRs out there that I haven't looked at, so I'm sorry, I will… I'll try to steal time again this week. I guess I have 30, you know, if we end this call, I might have a couple minutes.
Yeah, if there's nothing else, though, I, you know, happy to open it up to other folks, but otherwise, I'm happy to, you know, give everyone a record-breaking 33 minutes back. Could do that.
Pretty cool, too.
**Hannah Ramadan** 28:12 Yeah, I got nothing else, that sounds good.
**Eric Mustin** 28:15 Okay, I got… Do I have anything fun or cool, not really? No.
Yeah, I got nothing. Awesome. Well, yeah.
**Wendy Smoak** 28:24 Adding more metrics! Thanks to Schwan for working on metrics, but I gotta have… I've gotta have metrics on the metrics one of these days.
Because the metrics are silent.
Like, they're not… they don't say anything about what they're doing, so I've got some stuff locally, maybe I will…
**Eric Mustin** 28:41 Hmm.
**Wendy Smoak** 28:43 Working.
**Eric Mustin** 28:45 Like.
**Wendy Smoak** 28:45 Like, when you put it in… when you put it in debug, so, like, I post it somewhere else, like, the log… when you put… when you put the SDK in debug.
the logging will say, hey, I exported 6 logs, I exported 7 logs, and…
**Eric Mustin** 29:01 Right, right.
We're just like, metrics, who knows?
**Wendy Smoak** 29:06 Yeah, I know, that's exactly what I'm staring at it, going, what are you doing? Am I doing it wrong? What's happening? So, yeah, that…
**Eric Mustin** 29:12 Gotcha. That's good. Just as far as usability.
Yeah, yeah, no, that's really good. That's… that's user feedback, right? That's really good user feedback.
**Wendy Smoak** 29:21 And I know…
**Eric Mustin** 29:21 Oh, sorry.
**Wendy Smoak** 29:22 Ashwan's typing furiously and getting actual stuff that makes it work done, which is…
**Eric Mustin** 29:29 Yeah, I feel… I've never felt more like a product manager in my life than just being like, man, that's Ron, he's really.
**Wendy Smoak** 29:33 I know, like… you people who are working for free. I mean, I'm sure some of you get paid to work on this, but…
**Eric Mustin** 29:40 Not me. Not enough. No, I don't. I don't get paid. I don't get paid enough, and I also don't get paid to work on this, but anyway.
**Wendy Smoak** 29:48 Super appreciate all the… all the work that just magically appears.
**Eric Mustin** 29:52 Yeah.
Yeah. Infinity Beers, if I happen to bump into you guys at KubeCon or anything like that. But cool, that makes sense. I think we do have stuff to model it after, like, in the collector. They give you debug logs that are, you know, include metrics, so we can cheat a little and see what they're doing there and stuff. But yeah, that's good, that's good, maybe we can open a… also might be a good, like, first-timer type issue. I feel like that's, like, right up an alley.
**Wendy Smoak** 30:19 And there might be one already, because I brought it up, I think, in the… there's an issue for metrics feedback, and Kayla may have… Gotcha.
Kelly, may I have already opened something. It was just.
**Eric Mustin** 30:28 Yes, you.
**Wendy Smoak** 30:28 It came up today, because I'm.
**Eric Mustin** 30:30 Swimming, sorry. Yeah, well, I appreciate, again, appreciate you being the, the tip of the spear here, and, Yeah, thanks everyone again for all the great work. Enjoy your evenings, your afternoons, all that good stuff. Cheers, everyone.
**Wendy Smoak** 30:45 Thanks.
**Hannah Ramadan** 30:46 Amazing, thank you.
**Eric Mustin** 30:48 Au revoir, bon soire.
Stop sharing and leave. Cheers.
