SIG: .NET SIG
Date: 2025-06-17
Duration: 54 minutes
Zoom Recording URL: https://zoom.us/rec/share/zTpiknNTF-qHo9FfT8VaY-WE9obhBc5uie1xuJbcX0L3rhfDh7B8WvX0jwZm8R80.CHqFHvI3drIOxkJT
============================================================

## Zoom Recording Transcript

**Alan West** 01:22 Hello, everyone!
I don't see anything on the agenda yet, but if you have anything, go ahead and put it on there.
There was one individual Julius from last week that I think said might join today. He wanted to talk about something, but we'll wait until he's here.
Nope, Julius is here.
**Julius Koval** 02:43 Oh! Hi!
**Alan West** 02:44 Hello!
Why don't we start by talking about your Pr.
Julius will kick kick things off with that.
And one second I can share my screen.
Yeah. So I think, I guess just to kind of summarize the things that are on my mind. So for those of you just kind of catching everyone up here. Through this as a Pr out here to add event, name to log record. And, Julius, if I understand you right. I think your main desire at this point in time is to support the the bridge Api, or add add support to the bridge. Api for event, name.
And currently, this Pr also changes the behavior for our ilogger integration, which is basically where we wanna be, we. We do want a solution for that.
Though, after kind of thinking about this a little bit more this week.
I made some comments on the original issue that was open for this.
and made a proposal that maybe we introduce some configuration essentially to allow users to decide for themselves how to translate ilogger events to open telemetry events.
And I was kind of hoping that maybe we could further that discussion a little more here, if need be.
I was. I was actually still kind of hoping to get Lyudmila's. Input she's opened up the issue.
I might just ping her on slack directly this week.
Just kind of curious. The main thing at this point in my mind is.
personally, I like the idea of of a configuration. Api Blanche proposed something slightly different, that I actually like a little bit better.
Which is that that Api reside on open telemetry logger options, which is essentially a class that is pretty. I logger focused. This is really an ilogger concern, so I think it makes sense that it that it belongs there rather than off of the the builder that I had proposed.
Needless to say, I think while I like where this is going, I think there's still a couple of open questions like, should the default behavior be?
I think C. Joe made a comment here, suggesting that maybe the default behavior be that the just straight up the event name from Ilogger is used, but then it can be overwritten. And he goes on further to say something about an enum.
I'm not so sure about this idea personally, but I'm curious about other people's thoughts. If you have any and then sorry. I'm just kind of like spewing everything that's on my mind. I want. I want to get other people's thoughts. But then, lastly.
the question to you, Julius, is, you know, I don't know how easy this would be for this. Pr. I haven't really thought super deeply about it. But you know, if if the bridge Api is is your main desire at this point?
Then you know. Maybe maybe this Pr could be scoped town. I think the only the main benefit to that would be Our other Maintainer. Raj is out for a little while longer, and in his absence I'd feel comfortable pushing out a you know, a Pr with with a change to the the experimental bridge. Api though I am curious to get his feedback and opinions as we discuss changing the the public facing Api, for, like the ilogger stuff.
So I'll stop there, Julius, what are your thoughts, and anybody else feel free to chime in.
**Julius Koval** 07:55 Hi, so like, I said in the issue.
yeah, my main desire, I guess, was supporting the event name and bridge Api. But I'm not in a hurry to merge that, I guess. So I don't.
yeah, I guess it would make sense to wait and not necessarily split it into 2.
**Alan West** 08:20 Okay, that's fine. So so, depending on where this conversation heads with this event, name resolver.
as I'm calling it, is this something that you would be interested in implementing if if we settle that conversation.
**Julius Koval** 08:39 Yeah, I can take a look.
**Alan West** 08:42 Okay, okay, sounds good.
Then. Yeah, let me do a little more work this week. I do like, I said, I do want to get miller's input mainly just because I'm curious to get more insight from someone who may have more expertise and like how I logger events are used.
namely, to try to answer questions like, what should our default behavior be? And so on.
But with the other folks on the call today, do you have any thoughts about that? Like the, namely, going back to cj's comment about thoughts or opinions about the default behavior?
**TimothyMothra** 09:36 I'm out of the loop. I'll need more time to just review the discussion.
Like I'm I'm a little lost. Why, we need an enum here.
**Alan West** 09:49 Yeah, I think cj, was recommending this simply because there's more room for doing something wrong with a more complicated Api like this.
the problem with the enum as I see it, though, as he's at least proposed it, I'm not opposed to like the idea of like basic like default behavior, and also, like maybe some, some had default resolvers or not default resolvers, but like out of the box resolvers that are just easy to plug in rather than having to write your own logic.
But as he's described it here, he's like saying.
default behavior set set the event name to the pi loggers event name.
although, allow the user to choose from. These other 2 options, which I think are kind of non options, in my opinion, like, I don't really see this as a very valuable one. So like the Id is just basically an integer.
I don't think that is going to be desirable for anybody to use as as a as an open telemetry event name.
And then, as we get into, like, you know, some weird concatenation. I also am kind of skeptical that this is very useful.
So.
**TimothyMothra** 11:14 Alan, just a clarifying question, what is set on the log record? Is it both the event, Id and the event? Name.
**Alan West** 11:22 Just the event name.
**TimothyMothra** 11:23 Just the event name is on the log record.
**Alan West** 11:26 Yeah.
So I, logger has an event. Id struct which has 2 fields, an id and a name.
**TimothyMothra** 11:35 Oh, oh, it's event, id! That's the struct. It has both the id and the name. Then, as a as a sub property.
**Alan West** 11:43 Great.
which is one of the things that kind of drives the question that you know. Maybe maybe there is some ambiguity in how we should map ilogger events to open telemetry events.
The original suggestion, or at least the, as as Lyudmila has stated, is like, Hey, just use the event name.
or I guess it's actually the name property typo here. But basically event, id.name.
**TimothyMothra** 12:23 And because I assume this isn't coming from the open telemetry spec, so we're just making up a new attribute like dot net event name, and like putting it in there.
**Alan West** 12:33 Oh, no. So the a little more context here. So if we go to like the the otlp proto for logs, there is a new stable event, name field on a log record.
It's optional, and when it is set it means that this particular log record is an event. So this is coming from the spec. But what isn't coming from the spec is the ilogger integration. Right? It's up to us as.
**TimothyMothra** 13:19 Gotcha.
**Alan West** 13:20 The owners of the ilogger instrumentation to decide how to support this new feature.
**TimothyMothra** 13:27 If we take this like just just strictly as it's written like event name I would lean towards. We'll map only the name into this field, and then like.
For, like further discussion, is there any value in having, like an event underscore Id. If we want to capture both, and then the end user can decide what they want to do with them. At that point.
**Alan West** 13:50 Yeah, whether Id ever makes it, you know, into the spec or not is a question. And just because the the fact that things are named the same is never an indication to me that they are the same. So that's 1 of the reasons why I hesitate to just like make a.
**TimothyMothra** 14:06 Yeah.
**Alan West** 14:06 Make a a blind something there, but that that is actually one of the reasons why I do want to get. You know, those input, you know. Given that. She made this suggestion. Maybe she has some familiarity with like, how people have been using event. Id Blanche, I think you tossed out like a question to me last week, which was like, I don't even know how many people are using this yet. So you know.
it's it's use and how people are using it is.
well, that's a question to me, you know. It's I I'd I'd love to know more from people who maybe have seen it in use to get a better sense for whether.
**TimothyMothra** 14:48 Yeah, I think I think that's fair. My my gut tells me that. Like, if I'm a user and I've set this up like I've set a value for the name, and then I probably wouldn't care what the Id is, and so like on the flip side of that, when the data is ingested into my telemetry system like like having the id in there is just gonna make things a bit muddled. I'm only gonna care for the the actual like readable name part.
that's my gut feeling, anyways.
**Alan West** 15:15 Okay, yeah, I would agree. I think, that people who are probably adopt would be adopting this as like an open telemetry user probably would use iloggers event in that way.
But since I loggers have had predated open telemetry.
I suspect that there are systems where.
since the the name is totally optional. You don't have to have a name.
The the Id is not optional. It's basically it's going to be an integer, you know, it might be 0. But it's gonna be, you know, non- null .
And so there's this possibility. I think Blanche put down a nice scenario here where you know you have. You have 2 sources of of events essentially with the same name. You know the name is effectively not like in in some sense.
**TimothyMothra** 16:19 Oh!
**Alan West** 16:20 Primary key. Right? So you, this is this is this is one of the big reasons why, you know I raised this issue, that you know these? The the idea of an open telemetry event is that the name is identifies the structure of the log and its attributes and the structure of its body, and and so on.
anyways, that's where the conversation's at.
**TimothyMothra** 16:59 The the example there helps because I was. I was imagining more of the like the source generated loggers, where, like the id is obfuscated.
But this, like it's much more like the user's chosen an id number. In that example.
**Alan West** 17:16 Yeah.
**Mike "Blanch" Blanchard** 17:17 Put something in the chat that I find really interesting in this arena.
Check out that when it comes to comparing event id structures, the event. Name is not even considered.
**TimothyMothra** 17:40 Oh no!
**Mike "Blanch" Blanchard** 17:43 So if you you know, the default, Id is just 0.
So I've seen issues really just writing unit tests and different exporters where you're attempting to test like is event id default, and then skip it.
That will lead you down a wrong path because you may have 0. But you may have an event name. So you have to be really careful and not use the built in equality. If you want to be able to separate the 2.
**TimothyMothra** 18:16 Quick question, does it make any sense? They're online 69.
Like, the authors here have decided that, like the 2, string is name or id.
Would it be appropriate to use that for?
The log mapping.
**Alan West** 18:38 Oh, just to string it!
**TimothyMothra** 18:40 Yeah.
**Alan West** 18:41 Hmm.
**TimothyMothra** 18:43 We're kind of punting the decision. Then, too.
**Mike "Blanch" Blanchard** 18:47 But that's if we later wanted to support Id and name.
**TimothyMothra** 18:53 Yeah.
**Alan West** 18:59 It is an interesting observation, though in the sense that the Ilager authors have prioritize name in this in this context. But you know id in the context of like.
And so that's a yeah, interesting.
**TimothyMothra** 19:26 Alan, I like your instinct of getting Luke Miller's. Input. I wonder if she just is any closer to this than this group? Is.
**Alan West** 19:32 Yeah, I'll I'll I'll ping her. She she's probably overwhelmed with github ping! So I'll slacker this week and see if see if she has any thoughts. If she doesn't, that's okay, too. I think that we can still, you know, make a decision going forward.
I think, just personally, I'm I'm I'm I favor the discussion here. This this discussion of A, of A, of this thing called an event name resolver. I don't know what we'll end up really calling it. But I think that name is okay.
But adding something like that.
and it's really just going to be the default behavior. I think that's the name, the main thing that we need to kind of like settle on. I was curious, Blanche, if you had any thoughts on like just opinions. Just hot. Takes on.
**Mike "Blanch" Blanchard** 20:27 No, I'm always full of opinions.
**Alan West** 20:29 What are they?
**Mike "Blanch" Blanchard** 20:32 So I was really deeply involved in event Id and name a couple of times never got anywhere with it at the spec level.
What I was really pushing on was Riley's vision and Riley's very opinionated that event. Id is the more important thing.
trying to recall exactly why I mean it goes back to like windows.
and you have millions of log entries in windows and these giant things.
and they're very good about strongly typing the id. I don't think there's any concept of name.
and it becomes very important, like some developer will, you know, push some line of code?
And all of a sudden the back end gets spammed, you know, like petabytes of spam, and like you can't go and patch windows right away. But you can patch the telemetry systems to say, like, if you see this unique number, just drop it on the floor.
And then it's also really easy to take that unique number. Find the line of code and make some change.
So Riley's vision was always like, we don't care about event name at all. It was always like pushing hard for Id, but seems like the spec went a different direction, and it's like more geared for the name portion.
I don't know how this relates really to.net like I've never in my own code or any of the code I've worked on. Seen anybody like taking the time to go really set up event. Ids.
But that's also sort of why Runtime, if you use the source generator, why it started. Auto generating these things is, though, that so like we in Microsoft tell everyone like, use the source generator. We're pushing everybody to do that so that all of a sudden they get these strong things. They just start showing up in the telemetry, and then, when they need it, it's there to put in those rules and say, like, Oh, this log is costing us too much money. We just want to chop it off, you know, at ingestion or something.
So that's that's the use case that I'm aware of.
**Alan West** 22:56 And in that use case the Id is automatically set, but the the name still may be just empty or null , right.
**Mike "Blanch" Blanchard** 23:04 It's yeah. It's sort of designed to not be important. You just would do the Id. And the idea is more efficient in your pipelines to filter on right. It's like a numeric comparison versus like a string. Compare. So there's also, like some minor efficiency to be gained by using the the numeric form.
**Alan West** 23:29 Right.
which you know, circling back to my question like what? What would make sense as a default behavior? My, my! I'm kind of leaning towards no default. Behavior, like event. Name, is not set unless you decide that you want it set somehow, and you have to specify it.
in which case, you know, if if somebody is like, yeah, event, Id is the most important thing to me then and they can decide that. That's that's what they're gonna do thoughts on that thoughts on that Blanche, like versus I think C. Joe's see, Joe's in intuition was just set the event name as the default behavior.
**Mike "Blanch" Blanchard** 24:25 Have a strong feel for it.
I wish we were getting more feedback like I can't recall ever seeing like an issue where some user was like, I need this. And here's why it's like we're solving something we don't really understand.
We could, you know, we could put out a beta thing or an experimental thing. Call for feedback. I don't know if that will yield anything useful.
**Alan West** 24:55 Right.
**TimothyMothra** 24:58 Yeah, I agree with what Blanche said, like solving something we don't understand, I'll say, like the the default being nothing.
And then users need to now like well, understand open telemetry enough to know that they need to configure this event. Name. Resolver sounds like kind of a like a steepish learning curve alright.
In that case I'd be more inclined to go with what Cj. Was saying, just like default to the event name. But I do hear, like Blanche's point about the Id being a bit easier to like filter on.
**Mike "Blanch" Blanchard** 25:30 What we do today. Our default right now is this stuff just gets dropped.
**TimothyMothra** 25:35 Yeah.
**Mike "Blanch" Blanchard** 25:35 Will turn on the feature you get both.
you know. You just get the raw Id and name as attributes.
So if we just by default just started admitting the name.
Then you can go use that feature to get the Id as an attribute. That's basically the plan.
**Alan West** 26:00 Oh, you're talking like the feature flag. Yeah, the feature flag still being used right now for getting the id.
**Mike "Blanch" Blanchard** 26:07 So what's what's our ideally? What would we do? We'd go to the spec, and we'd get a spot for Id, and we would just send them both where they belong.
**Alan West** 26:20 Well, I guess. Sure, if that happens, I don't know. I'm not up on that conversation. Whether that's, you know, has has legs or not Part of me would not be surprised if event Id never becomes a thing in open telemetry, right? In which case, you know, it's up to us. We need to decide, you know, like what what what to do with this thing.
**Mike "Blanch" Blanchard** 26:50 Yeah.
**Alan West** 26:51 I mean it, I think I think as as it would pertain to any other kind of instrumentation, right? That has some important information that was like, very framework specific we would invent our own conventions right around it.
Things that I tossed around in the past was like, if this is just an ilogger thing.
then have like an you know.net dot ilogger dot event id attribute, you know.
**Mike "Blanch" Blanchard** 27:28 And go see if I can figure out what rust is doing, because I think I think in rust and C plus plus.
we had a similar need. There.
see if I can figure out if Cj. Did anything over there.
I know where I'm looking, but I'll poke around.
**Alan West** 28:05 Yeah, that's fair.
I mean, I think that's what it would take right like is in order for there to be hope. That event Id is going to be something that makes it into the spec. It's gonna need to be a concern that we've, you know, spotted in a number of places, kind of across languages, across different frameworks, and so on.
**Mike "Blanch" Blanchard** 28:37 There's something in rust called a target.
Let me just put this in the chat.
So I think this is their like log record, dto thingy.
So there's event. Name. It's a string. And then there's this target thing.
Seems sort of like what we have for, like category names.
**Alan West** 29:22 Override the instrumentation scope, name.
**Mike "Blanch" Blanchard** 29:36 Yeah, it's fine.
**Alan West** 29:43 Yeah, we're based off the comment here. I don't quite understand the the reason for this, but and it and it's specifically it says that that it's it's something that the exporter may do something with if it so chooses.
Seems seems fishy to me.
**Mike "Blanch" Blanchard** 30:05 Bit. Yeah.
**Alan West** 30:12 Besides that, it looks like you know it it the rest data model sticks pretty close to spec.
Hmm.
**Mike "Blanch" Blanchard** 30:33 It looks like c plus plus has something more interesting.
**Alan West** 30:42 I see. So what they are. They saying creates a single logger.
These appenders create a single logger.
**Mike "Blanch" Blanchard** 30:54 Well.
**Alan West** 30:56 No, this, this still seems fishy to me like I don't know that their concept of an impender necessarily makes sense to me.
Oh, you were saying something about c plus plus.
**Mike "Blanch" Blanchard** 31:10 Yeah, open that sequel plus link.
**Alan West** 31:19 And yeah, they have a straight up set event. Id.
And then I wonder what this
**Mike "Blanch" Blanchard** 31:25 Where it goes.
**Alan West** 31:26 Where it goes. Yeah, I mean, that must be another one of these things where it's like, yeah, the exporter can decide.
**Mike "Blanch" Blanchard** 31:34 This makes a lot of sense to me, because this is like the windows case where it needed, like a a number.
**Alan West** 31:48 Right.
**Mike "Blanch" Blanchard** 31:56 Interesting that we're looking at, you know, 3 different sig implementations.
and they all have variants which says to me that the spec has not done a good job.
It hasn't defined things well enough for people to be successful. So dot net rust c plus plus. Each has a little quirk based on its needs.
**Alan West** 32:20 Right?
Yeah. Yeah. And again, I don't know where the conversations are at the spec level. If there's any momentum there, I kind of suspect not. But maybe that's another thing that I need to kind of poke at this week, just to kind of dust off and see.
because I know you, Blanche had opened up, you know, some at least issues, or made some proposals way back in the day, but I'm sure that they've kind of growing some dust. In the meantime.
**Mike "Blanch" Blanchard** 32:53 Oh, yeah, I tried 2 different times, and both times it just got pulled into like the events conversation and just didn't go anywhere.
**Alan West** 33:07 Right.
All of that said, you know, like.
Yeah, this is all interesting, I think, though I think the beauty of this idea of this event. Name resolver is that to me it kind of, you know, there's always going to be.
The whole point of instrumentation is to basically, like, you know, get get structured data about a framework and basically map it to open telemetries, conventions and data model.
And so for what that means for ilogger is okay, ilogger, has this notion of an event. Tell us, tell us what you want. How do you want this to to map, to to hotel?
Kind of seems natural to me. But I also agree with Mothra's comment earlier, which is, you know.
that's gonna require users to educate themselves. They don't just get something out of the box with with, you know, doing nothing, which is, you know.
often desirable.
**Mike "Blanch" Blanchard** 34:24 Why do you? Why do you think it's not good to just by default set event id.name as the event name on the proto.
**Alan West** 34:36 Well, I guess 1st and foremost, I I guess I hadn't really.
Has. He asked the question again.
It's actually probably going to be null most of the time right like, if people do that.
how the that new format of logging with ilogger right where you get an automatically generated id.
you're still gonna be in the like, the the situation where you basically have null events, names in in hotel terms.
**Mike "Blanch" Blanchard** 35:11 Doesn't. It only generates Id. It doesn't generate a name.
**Alan West** 35:21 I thought. That's what you told me earlier is when the event, when I logger automatically generates Ids. It does not necessarily generate a name.
**Mike "Blanch" Blanchard** 35:32 I'd have to go double check. I know it generates something I would assume it's both, but I don't know for sure.
**Alan West** 35:47 Well, if it does, that would be interesting. Yeah, if you find that that would be interesting then, and then, you know, if it does. Then it just kind of comes to me. It comes back to this concern of the fact that the name is not really the is not really the, you know, primary key.
So you could effectively get collisions, you know, different differently structured log messages could have the same open telemetry event name.
which is not, you know, I think, the end of the world, but like it would, it would be.
It would be a a thing that I think would be more difficult for a user to discover.
Then you know, just the fact that they're not getting any names at all, and that they need to do something and make a decision for themselves.
**Mike "Blanch" Blanchard** 36:50 The the point I was trying to raise on my comment is like, I don't even think Id and name are enough.
you need to know, like the the event id class.
fully qualifying like it, needs a namespace to me.
**Alan West** 37:08 Which is which is, yeah, you're not gonna have that. This event name resolver doesn't necessarily solve that problem.
Yeah, you need to know, like library, one versus library 2.
**Mike "Blanch" Blanchard** 37:25 Yeah. And if, like, you can always just like those lines below where it's just calling the log, you could just new up an event, Id, and pass it. There would be no like. I don't even know what the namespace would be. In that case.
it's strange event. Id is a strange thing.
**Alan West** 37:58 well, I think we've talked enough about this.
i'll, say, this, I can be swayed, if, if if if I do get enough kind of input or feedback from folks that they think you know. See Joe's intuition right setting, like using event name as the default. And then, you know, offering some Api for doing something else. If if a lot of folks think that that's makes sense to them that would help. If you just wanna kind of like plus one. That idea versus, you know.
plus wanting some other idea.
That would be useful, input, I think at this point.
I'm not entirely opposed to this idea. I just, I just want to make sure that we know we've thought through the the implications of it.
So with that, said, yes, just to quick glance at Prs. I know that there are a lot of open Prs. I think a lot of them are these dependable things? I haven't circled back.
Martin's not on the call today.
But I had a question to him.
That's maybe one of you on the call here could knows more about. So I'm not super familiar with Dependabot this.
But I am familiar with this issue. So this yet again. We had this instance where you know the SDK was upgraded, and then a Oh, no! This is not the Pr. One second one second, let me find out I was looking for.
So right we've we've had this issue with with basically having to manually come in and get these like these these hashes. And so Martin did something that he attempted something.
How?
Where? These hashes would get changed in an automatic way.
but it didn't quite do the right thing as you can see here in that it updated both.
The 8 dotnet 8 and.net 9 and that's not what we wanted. So think he put out another Pr somewhere in the sea of things.
Maybe it was this one.
and I could just probably blindly merge this again, and just see what it does. I just haven't had the time. Necessarily. I see it as kind of low risk to just try it out. I haven't spent a whole lot of time really trying to like, understand appendibot and understand whether this is actually going to do a thing.
But I was curious if any of you were more familiar with Benda Bot, and maybe add some time to just kind of walk me through this. What is this actually doing? And do you think that this might actually solve the problem?
Does anyone know.
**TimothyMothra** 41:55 I've not played with, depend upon as it pertains to docker. My experience is all just SDK based. And so yeah, depend upon sees a dependency. It tries to update that like single dependency to the highest version, like the configuration allows. And I know the configuration. You can say like, we'll keep it at the major version. Only update the minor, you know.
But in that one file you showed a minute ago it looked like the config had both like an 8.0 and a 9.0, and so depend upon sees it as 2 separate dependencies, and tries to take them both to the latest.
That's what it appeared to be doing.
So I alright.
And I'm not familiar with this configuration. I my guess is version updates. And for Major.
Yeah, I'm not familiar with this configuration here.
**Alan West** 42:47 Okay, yeah, that's fair. Yeah. I I guess the the thing that was just unclear to me is like, what about this configuration would lead me to believe that you know it would, only it would only touch the 9 dot. Oh, let's see. Actually, this comment was.
yeah, like, like these lines, like.
I guess the presumption is that it's not gonna touch this one. But it's only gonna touch this one.
**TimothyMothra** 43:20 Yeah, I that's not how I read that his change.
because it looks like he's saying it's giving it permission to update both the major and the minor maybe could test this behavior in a like a a dummy repo just to see.
And then I wonder if we need to have like I don't know, and I don't know Docker, so I don't have any useful advice here. Specifically.
**Alan West** 43:54 That's fair. Yeah. You suggest doing it in a dummy repo, you know. Honestly like I was just thinking about doing it in the repo like again. I think it's low risk, but you know, if you, if you think otherwise.
do you? Or do you.
**TimothyMothra** 44:09 I agree. I think it's low risk.
**Alan West** 44:11 Yeah, I think I think I might just merge this pr of his just to see what it does.
**TimothyMothra** 44:18 This is 6. I just want to see this one.
Sorry, just like it's changing tabs a bunch I'm trying to like. Like. Look at it.
**Alan West** 44:24 Sorry about that. Yeah.
**TimothyMothra** 44:25 2 6.
I just wanna make sure he's is. His configuration is only gonna affect the docker and not affect, like all the other dependencies.
**Alan West** 44:35 Oh, right! I think the reason why this only affects Docker is that there's this package ecosystem.
**TimothyMothra** 44:40 Got it? Yeah.
**Alan West** 44:41 This was his previous pr, his his previous Pr, which which automatically bumped all of the things, was because of these lines here, for each of the for each of the folders or directories.
**TimothyMothra** 44:56 Yeah, I think this is low risk. I'm curious. And I saw this same change, not this same change, but the Docker dependency, configuration on the contribut repo just this morning, and I commented on it.
Do you know why he's doing like instead of just a test Slash Star Directory? He's doing like these 3 directories individually. I'm just curious.
**Alan West** 45:17 I don't know why. It's a good question you said you commented somewhere else.
**TimothyMothra** 45:21 Yeah, comment on the contrib repo, because he's onboarding the contrib repo to the the docker and depend about sorry, that's a bit off topic from what we're discussing here.
**Alan West** 45:32 This one here.
It's not totally off topic. I mean, this is, oh, yeah, sure, thanks.
I totally don't know.
**TimothyMothra** 45:42 That's that's a good answer.
**Alan West** 45:44 Sure.
Yeah, I mean again, you know, if he maybe I'll just keep on iterating with them in the in the main repo again. I think it's pretty low risk to just merge them and see what Dependabot does.
because, you know, I don't have a whole lot of time to like, dig in and try to figure this out myself. But if he's.
**TimothyMothra** 46:07 If if you want to do it just iteratively until you get it, I say, like on the main repo, change the interval to daily.
**Alan West** 46:13 Yeah, that's.
**TimothyMothra** 46:14 Like. Reject the Pr. And let it like. Keep trying.
**Alan West** 46:17 So basically.
yeah, and so we walk me through that one more time. So basically, this needs to change. So take the schedule away so that I get quicker feedback.
And then from the standpoint of like, basically kicking dependabot back into gear.
Sorry I'm switching tabs again. But if I come back here to like one of the Dependabot prs.
But I think.
**TimothyMothra** 46:42 There's a way to reject it, so that dependabout will try again.
If you expand that commands and options, it might tell you like. If you reject it the wrong way, then it won't try again.
**Alan West** 46:51 Gotcha. Okay, we'll reopen this Pr. If closed.
No, that's not quite what I want. I don't think recreate.
**TimothyMothra** 47:04 That might be the best one. Don't do close. I'm reading the the lower ones.
Close, we'll like tell it not to retry.
**Alan West** 47:11 Yeah, yeah, yeah, okay, okay.
**TimothyMothra** 47:13 Achieve the same result by closing it manually. Okay, so don't close manually. That's the.
**Alan West** 47:20 Yeah, so don't close it manually, and don't run this.
**TimothyMothra** 47:26 Yeah. So I think the recreate is the one you want to do.
**Alan West** 47:29 Okay, yeah, maybe I'll give that a shot.
I'll ping Martin on that one Pr. If he wants to make that change to of the to the schedule, and then And then that way we can come back, and once once we figure it out, and you know this repo, then you know, we'll.
**TimothyMothra** 47:48 Make the same change and contribute. Yeah.
**Alan West** 47:50 Change and contribute.
**TimothyMothra** 47:51 I wonder if if for the for the, because the the docker has the 2 dependencies right, the 8.0 and the 9 dot. Oh.
I wonder if you could like pull those out to separate files and then tell Dependabot like.
only do minor updates don't change the major version.
And then, if the docker file can pull in those 2 separate like dependencies.
that might be a way to like skip this issue.
But I don't know if Docker like permits that.
**Alan West** 48:31 Yeah, splitting.
Basically, you want like 2 docker files. But the the results effectively be kind of merged.
**TimothyMothra** 48:38 Yeah.
**Alan West** 48:41 Yeah, I don't know. Interesting thought.
Okay, but no, that was helpful. Yeah, mainly. I just wanted to like, you know.
sort out a way to just kind of like iterate on this with with Martin without me spending too much time trying to figure out.
**TimothyMothra** 49:00 That's fair.
**Alan West** 49:02 So I think that kind of gives a path forward for for some iterations on this.
**TimothyMothra** 49:07 Cool.
**Alan West** 49:09 Cool. Yeah, thank you.
Besides that, really, I think that most of these Prs are Martin, just doing small kind of info things which I'm gonna catch up on. And then it's just this, depend upon noise.
And then, I think, stuff that we've talked about before. So not not a minute big there to talk about, and then, I think, contribute of not. I think it's.
**TimothyMothra** 49:42 Yeah, I'm playing catch up over here. I approved a small few of them this morning.
**Alan West** 49:47 Okay, yeah. I know that I see some things here that I should probably take.
Look at, and we'll probably just go ahead and merge, assuming they've got the right eyes from the from the component owners, and so on.
Okay, yeah, thanks for your help on that, too.
That's all I have last call for anyone else.
**Mike "Blanch" Blanchard** 50:19 Just check out, Alan. I threw a link in the chat we were talking earlier about the auto generation. I think you're right. It only does the Id.
**Alan West** 50:30 I've seen those already. Yeah.
interesting.
**Mike "Blanch" Blanchard** 50:46 So I don't know. I think it feels okay to me to just make the default set event name as the proto thing probably be null for most people if they want Id.
they still have. We still have the feature flag.
If the spec ever gives us a spot for it, then we could just eliminate the feature flags.
**Alan West** 51:14 Right?
Yeah, that would get them event Id. And then, on event name, they would basically like anyone who's using that like source generated style.
they could either set names, I mean they they. If they're using open telemetry, they'd be like, oh, I want event names, so I know I need to do something.
They'd probably be inclined at that point to maybe set their event id and name explicitly rather than relying on this random generated.
**TimothyMothra** 51:57 Sorry I spaced out for a second. If Blanche said what he thought, I said I'd be in favor of that would be just record name in the name field, and have an experimental for the Id, and put the id in an id field.
**Mike "Blanch" Blanchard** 52:11 Kind of have that today.
If you turn it on, you'll get Id is like an attribute.
**TimothyMothra** 52:21 That that sounds pretty great, and then, if the spec ever does take Id formally, then we just removed the experimental.
**Mike "Blanch" Blanchard** 52:36 What's really nice about that is like it's it's very easy to document right ideal.
**TimothyMothra** 52:43 Think that's.
**Mike "Blanch" Blanchard** 52:44 Get event. Name. It goes here. If you want event. Id, do this and you get it over here, and we're we're kind of done.
**TimothyMothra** 52:53 Yeah, I like fully support that.
It's it's simple, it's straightforward. We're not doing this extra resolver stuff, which I think is just a barrier to entry personally.
Yeah, where? Where can I upvote? That's.
**Mike "Blanch" Blanchard** 53:11 Yeah, I mean, it's simple, like, if you know, we could do the simple thing. And then if users come back and they're asking for. Oh, I need to put this over here like we could always add the resolve, or like we can always make it, you know, add little options to do advanced things. If there's demand you could also do it with like a processor. Right? You could just take whatever you see on the log record. It'll give you the event, id structure, and you could swap them or combine them, or do whatever you want.
**TimothyMothra** 53:47 Yeah, that's true.
**Mike "Blanch" Blanchard** 53:51 So it's a little bit heavy lifting, but users wouldn't be blocked.
**Alan West** 54:01 I think Julius's Pr is pretty close to effectively, that proposal at this point in time, so yeah, let's let's just sit on it a little bit longer like I said I, I still do want to reach out to Ludmilla just since she opened the issue originally.
and author. You asked where you can. Where can you upload it? Feel free to chime in if you let's see, this is the Pr. But chime in on this on this issue. 61 0, 8. If you.
**TimothyMothra** 54:33 61, 0, 8. Okay, I gotta find that again.
Okay, I got it. Thanks.
**Alan West** 54:37 This discussion cool?
Alright. Y'all, thank you very much.
**TimothyMothra** 54:46 Have a good day.
**Alan West** 54:47 See you all next week.
**TimothyMothra** 54:51 Bye.
**Alan West** 54:53 Bye, bye.
**Julius Koval** 54:53 Like.
