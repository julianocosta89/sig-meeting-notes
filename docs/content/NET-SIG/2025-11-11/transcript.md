SIG: .NET SIG
Date: 2025-11-11
Duration: 7 minutes
============================================================

## Zoom Recording Transcript

**Zach Montoya** 02:25 Hey, Martin, how's it going?
**Martin Costello** 02:29 Hey, I'm good, thanks. How are you?
**Zach Montoya** 02:31 Good. Just, watching some, .NET Conf, and, yeah, just, working on… watching that on the side while I work.
**Martin Costello** 02:40 Oh yeah, I was just watching that as well, but I closed it to join the meeting, and then home time after this meeting.
**Zach Montoya** 02:47 Oh, yep, absolutely.
Yeah, I'm a little bit behind on this livestream, but the, what, C-sharp 14? Whichever C-sharp version that they're, showcasing right now. It's got some interesting, features in there.
**Martin Costello** 03:04 Yeah, there's a lot of stuff in it that's… I'd need to remember loads of really old code and go back and revisit it to see where I'd write it differently.
There's, like, there's nothing in it that's like, oh, I could just quickly nip and change that somewhere.
**Zach Montoya** 03:23 Yeah, I think the… having the field property, the first class field, is actually really interesting.
**Martin Costello** 03:29 Yeah, they've also got, there's a code analyzer for it, because.
**Zach Montoya** 03:33 Oh, okay.
**Martin Costello** 03:34 projects.
**Zach Montoya** 03:36 Oh, do they use field as a variable name?
**Martin Costello** 03:39 Oh, no, no, no, it's where I've… done something… I can't remember the exact code pattern, and then the analyzer's gone, hey, you could use the field… you could use the field here.
**Zach Montoya** 03:50 I see.
**Martin Costello** 03:51 And then get rid of, like, an explicitly declared one.
Not sure if… Raj, or Alan or anyone who's gonna…
**Zach Montoya** 04:19 Oh, you know what? Is, isn't there a KubeCon or something going on right now? Maybe a lot of people are over there?
**Martin Costello** 04:26 Oh, I remember, actually, I remember last week Alan said he was on holiday.
But I don't know if Raj is a cute cod or not. I haven't seen him say he was.
**Zach Montoya** 04:37 Okay.
Well, I… I don't have any topics. I'm… I want to start attending these meetings a little bit more often, but I don't have anything to contribute at the moment.
**Martin Costello** 04:55 Yeah, I put, two items on the agenda, but the first one… Someone with merge rights needs to be here to merge it.
**Zach Montoya** 05:04 Got it.
**Martin Costello** 05:05 So that one can't move anywhere, which is unfortunate. And, the second one… Probably needs a wider discussion.
**Zach Montoya** 05:13 Than just you and I. Oh, yeah, yeah, for sure.
Interesting. EF core, okay.
**Martin Costello** 05:20 The TLDR is… Someone opened an issue…
**Zach Montoya** 05:26 the…
**Martin Costello** 05:27 doesn't work with Cosmos DB?
Which is true.
But then I opened an issue with the AFCore folks, and then it sort of went off into a tangent about, Well, if you want that, then turn it on in the Azure SDK, and if you want SQL, turn it on in the SQL drivers.
And then it turned into, like, well, what should EFCore be doing?
Should it be doing EF core things and ignoring the database stuff?
In which case, then it's maybe not really… an open telemetry thing, because it's then just inventing Spans and metrics, or should it do what it's currently doing, which is implementing the semantic conventions?
And then suddenly the scope of it massively increases to try and work with every possible EFCore provider.
**Zach Montoya** 06:20 Yeah.
That seems like I'm… Pretty massive, kind of… Scope creep.
**Martin Costello** 06:29 Yeah, so yeah, I was… I was just gonna bring it up for discussion to see… what direction it should go in, because also, I think if it changed direction there, that would be breaking change.
**Zach Montoya** 06:41 Got it.
Yep, I'll need to wait to have that discussion.
**Martin Costello** 06:49 I think not much else has been going on in the repos this week.
So… Unless you've got anything to discuss.
Unless Raj joins in the next 5 seconds, I guess we can call it a day for this week.
**Zach Montoya** 07:05 Yeah, I think that sounds fine, yeah, I have nothing, no topics.
**Martin Costello** 07:09 Okay, cool. I'll speak to you next time.
**Zach Montoya** 07:11 Yeah, have a nice evening.
**Martin Costello** 07:12 You said, bye.
**Zach Montoya** 07:13 I…
