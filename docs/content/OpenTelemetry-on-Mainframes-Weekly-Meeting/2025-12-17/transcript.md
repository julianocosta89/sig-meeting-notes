SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2025-12-17
Duration: 29 minutes
Zoom Recording URL: https://zoom.us/rec/share/fbybXkguvwy0FoqJiJ1eF5Wj15oHqH7SpgOCvEh3pkNJenlcpC3Z_3I-yLegR9j2.so_Z_uvkKm9KkSSI
============================================================

## Zoom Recording Transcript

**Angelika Heinrich** 00:24 Good evening, Andre.
**Andrej Chmelo** 00:27 Hello, good evening.
**Angelika Heinrich** 00:34 You're in progress.
**Andrej Chmelo** 00:36 Yes.
**Angelika Heinrich** 00:37 Is it… Colder this week than last week.
**Andrej Chmelo** 00:41 Yeah, I guess it's, like, 10 or 15 degrees less than last week.
**Angelika Heinrich** 00:48 Okay.
I was lucky when I was there last week, it was… quite warm for winter.
**atoulme** 00:56 Hello.
**Angelika Heinrich** 00:58 Hello.
**Andrej Chmelo** 01:01 It looks like we won't have white Christmas, but maybe at least a cold Christmas.
**Angelika Heinrich** 01:07 Yeah.
Yeah, even here,
In the Cologne area, it's also just cold, but not a lot of snow so far.
**Jim Porell** 01:17 Where are you located?
**Angelika Heinrich** 01:20 Do you know Cologne in Germany?
**Jim Porell** 01:23 Oh, sure, yeah.
**Angelika Heinrich** 01:24 Yeah. We got some snow, like, 2 weeks ago, but…
It didn't really, you know, stick around, and since then, we've had nothing.
**Jim Porell** 01:34 Room.
Yeah, it's… I mean, this week, it's actually getting warm today, but, it's minus 4 going up to 6.
next week, I think, looks like Christmas is gonna be minus 2 as the high, so…
**Angelika Heinrich** 01:52 Hi, hey.
Hmm.
**Jim Porell** 02:00 That's at… this is in New York, upstate New York.
**Angelika Heinrich** 02:02 New York? Okay.
Yeah, New York does get pretty cold.
**Jim Porell** 02:09 Yeah, I got a… I got a lot of snow. I have probably about 10 centimeters of snow right now, but it's gonna rain.
**Angelika Heinrich** 02:15 Bye-bye.
**Jim Porell** 02:15 It can be… Pretty warm tomorrow, about 12 tomorrow.
**Angelika Heinrich** 02:19 Okay, yeah.
So it'll just be sludge then, or maybe just mud.
**Jim Porell** 02:24 Yeah, it'll start melting, yeah.
**Angelika Heinrich** 02:26 Yeah.
And I think I saw in the Slack channel that, I really go and make it today.
**Jim Porell** 02:38 Do you know Thomas Esser by any chance?
**Angelika Heinrich** 02:42 Hmm.
**Jim Porell** 02:43 Cologne's a big city, so I…
**Angelika Heinrich** 02:45 Yeah.
**Jim Porell** 02:46 He's the only person I know from there. He used to work for BMC, and now he's… and IBM, and now he's with Rocket, so…
**Angelika Heinrich** 02:52 He's with Rocket now? Yeah. Okay. Me.
What was his surname again?
**Jim Porell** 02:57 Esser. E-S-S-E-R.
**Angelika Heinrich** 03:02 Let me have a look. I'm very… I'm much better with faces than I am with names.
Maybe I know his face.
**Jim Porell** 03:10 Like, asking me who lives in New York City. Oh, yeah, sure.
No problem.
**Angelika Heinrich** 03:18 You just tell them you know everyone, right?
**Jim Porell** 03:20 Yeah, yeah.
**Richard Nikula** 03:23 So I used to work for the state of Washington many, many, many years ago.
And… I always laugh because I would be out somewhere, and
somebody, I'd say, well, where do you work? And I said, oh, I work for the… stated…
And they would say, oh, do you use, you know, such and such? And I'm like, you know, you know, come on, gosh, you know, there's only, you know, how many thousands of people who work for the state, right? But I'd be driving down the road, and I'd see a car that had, you know, State of Washington markings on it.
**Angelika Heinrich** 03:55 I pulled…
**Richard Nikula** 03:56 up to see, I wonder if I know him, you know? Yeah.
**Jim Porell** 03:58 True.
or, like, Greg's at Broadcom, I feel like I know everybody there, because they're all, you know.
**Angelika Heinrich** 04:06 Awesome.
**Jim Porell** 04:06 People seem to be ex-IBM, so…
**Angelika Heinrich** 04:10 It's quite a… there's a few, that's true.
**Jim Porell** 04:17 The mainframe world in IBM is pretty small, in reality.
**Angelika Heinrich** 04:22 Yeah, I think the mainframe world in comparison to, you know, cloud or other platforms is definitely a niche community.
Nope.
First time I went to a mainframe conference, I was like, who are all these people?
Next time, I was like, okay, I recognize faces. The third time, you're like, okay, no, I'm furniture, not too, it's done.
**Greg Shriver** 04:50 Yeah, hey, everybody.
**Jim Porell** 04:52 Go there.
**Angelika Heinrich** 04:55 I'm not putting on my camera, I was at the dentist today, and I'm… Feeling a bit icky.
**Greg Shriver** 05:02 I… I really dislike the dentist.
**Angelika Heinrich** 05:05 Hmm.
I don't think there's any other more disliked… necessity?
And a dentist, right? It's like, we all have to go, but nobody wants to.
Although I did read.
**Jim Porell** 05:20 Go work.
**Angelika Heinrich** 05:20 Run some?
**Jim Porell** 05:21 But do you have kidney stones?
**Angelika Heinrich** 05:23 Oh, kidney stones? Oh… I've heard stories.
**Jim Porell** 05:28 This is the piece of cake.
**Angelika Heinrich** 05:30 Oh, yeah.
Okay, I won't argue with that.
**Greg Shriver** 05:37 I don't have a lot today. I guess a couple little housekeeping things, I mean, I think I posted this in the chat. It looks like…
It looks like, no, Morgan's not here today, and I think he's the one that's been doing, sort of, the updates of the calendar entries.
So, it looks like we're still… I mean, the moving… moving to the… an hour earlier is approved by everyone, I think. It's just a question of he wanted to make sure that he, contacted Rudiga before we just changed the time.
But it looks to me like the calendar entries for next week, which is the 24th and the 20… and the 31st, are both canceled, so I guess… I don't know what the first Wednesday in January is, but my guess is that this will be the last meeting for 2025.
And we'll… we'll meet again in 2026, first Wednesday in June.
**Jim Porell** 06:34 Yeah, January 7th.
**Angelika Heinrich** 06:35 7th.
**Greg Shriver** 06:37 Thank you. Thank you.
So, yeah. So, I, let me see, I had one item.
Which was the, the doc PR, which I also, submitted. I also, sent that on the, on the,
the Slack chat.
I did get some feedback, both, you know, internally here at Broadcom, and some external folks as well. Rudiga, I think, mentioned that he was gonna try and take a look at it, you know, sometime soon.
And, so, I did have some questions. There are some…
Some things in there about adding, no, I don't know.
Where it is about adding maintainers.
Like the SIG, for SIG approvers for the, for the mainframe space.
I don't really know that much about that. I was kind of hoping to ask Morgan, but maybe we'll just push that off until…
Until, next… our next meeting.
I think I did… Let me throw the… Here's the pull request… oops.
Oh, I didn't mean to do that.
I updated right over somebody else's note, my apologies.
I don't know where my cursor is.
Does everybody else have this problem, or is this just me?
Okay.
So there's the doc… the doc PR,
I… and I'm not sharing my screen, but I just threw it in the meeting notes, so…
I don't really… other than… other than what's there, I mean, I would encourage everyone to go and at least take a look at it.
But, you know, we've got time, so…
**Angelika Heinrich** 08:39 I had a… I did have a quick squeeze over, and I really liked the flow.
It felt like it was… Enough information to give an introduction, without going too…
Too low level, so I thought the content was well-scoped.
**Greg Shriver** 08:57 Thank you, thank you. So, yeah, I mean, I appreciate that feedback.
There's some other stuff in the doc…
space that I… the OpenTelemetry doc space that I don't really understand. It looks like you've got some, some linters that you can either manually use or apply them with a bot. I don't understand what that is. I didn't mess that up when I made changes, but anyway,
So that's… that's really my only update right now.
And I don't have anything else. Does anybody else have anything for our… Last…
**Angelika Heinrich** 09:37 Meeting of 2025.
I know that, Kai, last time we were here, he had talked about the mainframe, sorry, the messaging.
semantic conventions,
were we… I know, Kai gave me, like, just… I think it was you, Greg, or someone gave us a quick update. Did we give an update to this group as well, on just what the next steps were?
**Greg Shriver** 10:02 I think we talked about it last week. Kai had mentioned, hey, that we want to add
We want to add… we wanted to add IBM MQ to the list of messaging systems, and he…
**Angelika Heinrich** 10:15 Oh, sorry.
**Greg Shriver** 10:17 Yeah,
I don't know if Kai actually drafted a PR or not. I know there was, there was… there was an issue…
with the messaging SIG, is paused.
So, I think Kai wanted… and, you know, I'm fuzzy on the details, but I know that the messaging SIG was currently paused, and rather than, I don't… and I don't remember if he was going to just draft the PR,
in, you know, in absence of any, of any feedback from the messaging… the paused messaging SIG.
Or…
**Angelika Heinrich** 10:59 Yeah, I think he said…
Also, jeez. I feel like he said he had the PR, but it was auto…
Rejected or canceled, because there is no… no messaging sick.
**Greg Shriver** 11:12 Yeah, you're right. You're right.
**Angelika Heinrich** 11:13 And I think it was Trask who said when he's done with… and I can't remember which one he's busy with now, but when that's done, he'll try and see if there's capacity to revive the
bet.
**Greg Shriver** 11:25 That's right. Yeah, I… thank you, because I have the memory of a goldfish, so I…
**Angelika Heinrich** 11:30 Same. We pieced it together. So, I think it was basically just go with, you know, the suggestion was just go forward with, what he proposed, until…
You know, and so that's… that's a group can be put together.
**Greg Shriver** 11:48 Right, that's what I recall as well.
**Angelika Heinrich** 11:51 Yeah.
**Greg Shriver** 11:52 Yeah.
Cool.
**Angelika Heinrich** 11:58 Okay, and then I only had one question, so I know we…
So we've talked TPS, and that's… that TPS pull request is still kind of being reviewed, I guess? .
**Greg Shriver** 12:12 So…
**Angelika Heinrich** 12:13 The… the other group of resource attributes that I don't think we have, definitions for, for the mainframe SIG is,
database?
So… you know, DB2 or any other database type, resources,
Do you… does anyone know if Ridiga had also any proposals for that somewhere in the background, or…
**Greg Shriver** 12:47 I don't, but I know we're still in this weird place where we have some stuff that was articulated in that Google documentation that is…
Up, that… that's… that's in… it's referenced in one of the links at the beginning of the meeting notes. I know there was a bunch… there was stuff in there, and I don't recall if DB2 was talked about there. I don't believe that… that we've made any
any progress on putting DB2, you know, in an actual PR. I know we had discussions a few meetings ago about taking some of the, you know, the,
Taking some of the… the… the items.
and kind of piecemealing them into smaller PRs, but I don't know that we've done anything… I don't know if we've done anything official. And apparently, you know, if it's not a PR, it hasn't really happened. So we have it in the Google Doc, we have some stuff in the Google Doc.
**Angelika Heinrich** 13:48 Taking a look at it now again.
**Greg Shriver** 13:49 Jack was…
**Angelika Heinrich** 13:50 She talked about it.
**Greg Shriver** 13:52 Yeah, I remember that.
**Angelika Heinrich** 13:53 There is a long table here.
**Greg Shriver** 13:55 Oh, yeah.
**Angelika Heinrich** 13:56 Very specific to DB2, I was just wondering if we did anything just general DB, right, on mainframe, that is, like, common between, like, IMSDB, or DB… DB2DB, or…
you know, anything that for mainframe, because I'm sure a lot of the database resource attributes are going to
Transfer really well.
So, maybe what I'll do is, over the holidays, I'll just have a look.
what's in the OTAL semantic conventions for database?
And, try and…
see or identify from our last conversation on DB2, if there's anything we need to call out that's really mainspense, mainframe-specific.
Right, so… I know we have, like, sharing groups in DB2 and things like that that may not be…
Covered.
But we may also just want to agree on what does exist in the database resource attributes, how would we map that to mainframe pieces, right? So, okay, I'll take another look at that.
**Greg Shriver** 15:11 Yeah, there's… There's some stuff here in the Google Doc, Angie.
**Angelika Heinrich** 15:17 Yeah, yeah, I see it here. I see DB2, and…
**Greg Shriver** 15:21 Yeah.
And then metrics.
**Angelika Heinrich** 15:24 June?
**Greg Shriver** 15:25 metrics, there's a metrics section that follows it here. Let me share my screen.
And this is… Oops.
I did that wrong.
Okay, so this is… this is, again, in that… in that Google Doc that I mentioned that was in the, in the OpenTelemetry, mainframe meeting notes.
**Angelika Heinrich** 15:55 At the top.
**Greg Shriver** 15:57 And so there's… there's some stuff here, and I think either Jack or Anon did this, I'm not sure.
Or maybe Rudica, I don't remember.
But, it looked like they had proposed
several new ones that weren't, and I guess there's this DB system that is existing, but all this other stuff looks…
Yeah, again, I don't know which… whether these ones are newly proposed, or whether those.
Yeah, so… so, yeah.
That'd be great. That would be great.
**Angelika Heinrich** 16:36 Let's see, and then… I'll try to boil it down, and then prepare a pull request.
Maybe just so we can have that in there.
**Greg Shriver** 16:46 Yeah, it'd be.
**Angelika Heinrich** 16:47 Because then we'll have, okay, MQ, you know, we can't really go far too quickly, but DB2, I think, was one… yeah, one other one we'd already discussed to some degree. Okay.
**Greg Shriver** 16:58 Yeah.
**Angelika Heinrich** 16:59 Cool.
**Greg Shriver** 17:03 Awesome.
Any other… Any other topics for today?
Or holiday songs that anyone want to sing on a recorded line?
**Andrej Chmelo** 17:18 Yeah, I would have a question. I don't want to steal a meeting, it's… It's a general question, if…
Yeah.
**Greg Shriver** 17:27 Go for it.
**Andrej Chmelo** 17:29 So, like, we are very early in the process of adoption, the open telemetry, and so we are wondering
Like, if you can… And suggest, or if you have experience, like, how are you testing this integration in…
In your applications, like… We want to produce some signals.
**Angelika Heinrich** 17:54 But…
**Andrej Chmelo** 17:54 We… Are kind of struggling, like…
How to… how to test this.
**Angelika Heinrich** 18:06 So, you mean from a, like, a user experience point of view, or what kind of testing are you looking for?
**Andrej Chmelo** 18:15 With some automated testing, like, if we produce something.
Then, to make sure that we don't break it in the future.
If…
**Angelika Heinrich** 18:25 Huh.
**Andrej Chmelo** 18:28 Have some experience with this.
**Angelika Heinrich** 18:30 Hmm.
I think Kai would be the person.
I can maybe answer that question, but maybe, Greg, you have some insight, right?
**Greg Shriver** 18:40 Not really. I mean, I don't… so, I don't know that we… I don't know that we have any automated testing. I mean, we certainly, you know, I assume you're, you know, producing signals and sending them through, you know, out to an OpenTelemetry collector, and then out to back ends.
And… I mean, we do have some automated testing with that, but if I understood your comment, it sounded like automated testing, like comparing against the
The… what's currently in the semantic conventions and what you're producing, is that what you were talking about?
**Andrej Chmelo** 19:19 So…
I'm more aiming to… If we want to produce some signals to validate that they were really produced.
**Angelika Heinrich** 19:33 Oh, oh, oh.
different.
**atoulme** 19:37 Question.
**Greg Shriver** 19:38 Well, that's doable, yeah.
**Angelika Heinrich** 19:39 Yeah, yeah, and the collector… Yeah.
**atoulme** 19:43 Through the collector, I think there's multiple ways. Sorry, I cut someone off.
Yeah, I can show you an example of a test that we ran.
Here.
So you can, a couple things. You can use Golden. It allows you to test against reference files, so you can check that your instrumentation is returning the right data.
there's some fuzziness allowed, like timestamps and other attribute values can be kind of null ified. For example, if you have a Docker container ID as an attribute, it will change on every run, so you want to be able to ignore that value.
Let's still check that it's present.
But the other thing you can try is the Weaver Live Check feature, which is…
Admittedly, I haven't tried it myself. It's allowing you to test against a schema.
That the data looks like what you would want it to look like.
So…
**Andrej Chmelo** 20:44 Okay, that sounds like something we are looking for.
**atoulme** 20:51 Yeah, but you're asking a question which is more generic, right? You're not asking about mainframe.
There's… are you using a menu today?
**Andrej Chmelo** 20:59 Yes, yes, our…
Like, I'm from… I don't know if you know Zoe API Mediation Layer, which is basically a gateway on mainframe.
**atoulme** 21:09 Okay, baby.
**Andrej Chmelo** 21:10 Exactly.
So… but this question is not…
specific to mainframe testing, we… yeah, we want to do both, like, some… Integration testing the GitHub Actions.
And then some… something on the… On the mainframe.
**atoulme** 21:28 Yeah, so in that case, you would want to check with Golden, because you have a reproducible use case.
And you would be able to do that. Take a look at what you can do.
It allows you to do sorts of, of matching, of course, so you will…
Depending on how you configure it, right, you can… you can make it go code, so you can programmatically match on the first one, or keep retrying until you find something that matches what you want.
So, that's… It's possible.
**Andrej Chmelo** 22:01 Okay, yeah, thanks a lot for this, certainly.
Go through it.
**atoulme** 22:15 Alright. I do have a… Someone mentioned IBM MQ earlier.
You are familiar with the fact that we do have a OpenTeometry Java ContribQ integration, right?
**Angelika Heinrich** 22:34 Sorry, I didn't catch that last part. Say again.
**atoulme** 22:38 with the fact that we have a IBM MQ Java contrib.
implementation.
**Angelika Heinrich** 22:46 No?
I didn't know that, did you?
Thank you.
**atoulme** 22:51 Let me see…
I'll put it in chat here.
So… for what it's worth, this is a model that runs as a standalone Java application.
It's, going to use a IBM MQ jar.
To create a connection to, either remotely or using bindings.
MQ Server?
And then it's going to perform all sorts of metric capture from there.
There is a Weaver model, If you're into that, that's… Always interesting.
And, there's probably some resource attributes where you would have opinions about how things should be done.
So… That's… Let's the attributes.
So, maybe that's, something this…
I'm unclear where Mintframe stops and starts, because as you mentioned, like, messaging sync could also be a good place for this.
**Angelika Heinrich** 24:14 Yeah, I think it's probably a good reference. I know Kai was just trying to understand what…
semantics are being followed, if that makes sense, for the messaging sake, for…
I think he was looking specifically on the queue manager side, not the client application side.
**atoulme** 24:36 This is a…
**Angelika Heinrich** 24:36 Yeah.
**atoulme** 24:37 Yeah, so…
we kind of map 1-1 to some of the… it's not 1-1, it's pretty close to what the calls you can make against the IBM MQ.
You end up having, like, a lot of things around the status, and some of the state, and interesting data, like, you know, buffers received, and bytes sent, and whatnot, and stuff like that.
**Angelika Heinrich** 25:05 Yeah, I think this…
Sounds… I mean, I think it would be a good reference for Clark, because I know he was trying to understand.
What should… what is the naming, you know, the naming conventions on that side?
So I think that was well-defined for clients, and…
Producers, but not so much for the queue.
**atoulme** 25:27 Yeah, the queue itself is…
It's too specific to IBM MQ, because there are things in there, like there's depth high event, which are…
**Angelika Heinrich** 25:35 Yeah.
the full events, which…
**atoulme** 25:39 MQ-specific… Uncommitted messages, okay, oldest message, that's probably okay.
file size might work. I don't know if it really is something you would apply to Kafka the same way, if that makes sense.
**Angelika Heinrich** 25:54 Sure, no, that does make sense, yeah.
**atoulme** 25:58 there's ways to kind of formalize that more, sounds fun, but yeah. So, FYI, this exists.
**Angelika Heinrich** 26:07 Yeah, cool, thanks.
**Greg Shriver** 26:09 Yeah.
Cool.
Any other topics for today, before we wrap?
**Richard Nikula** 26:23 Okay, so I have to…
I'll throw this in, since you said any old miscellaneous thing, so hang on, let's see here.
How do I… How do I share? Hmm…
**Jim Porell** 26:36 But the boss…
**Richard Nikula** 26:36 Oh, there we go. Share. Yep, there we go, got it. Share…
Applications… where are you at?
Dang it, let's see… oh, I know, because I clicked on your link, that's why I didn't there.
Alright, so just hang on here, sorry.
Alright, so it should be… It's this guy.
Share your screen?
**Jim Porell** 27:07 There you go.
**Richard Nikula** 27:08 Bunch of.
**Greg Shriver** 27:08 Yes.
**Richard Nikula** 27:08 YouTube screen?
**Greg Shriver** 27:10 Yes, YouTube.
**Richard Nikula** 27:12 Okay.
So, this is… this is my house.
**Angelika Heinrich** 27:16 Oh!
Oh, wow.
**Greg Shriver** 27:18 Oh, that's fantastic.
**Richard Nikula** 27:22 That is…
**Angelika Heinrich** 27:22 Very festive. We'll let it play for a second, because it's going to pan left, then right. So this is far to the left.
**Richard Nikula** 27:29 There's me!
Almost… there we go.
**Greg Shriver** 27:32 Oh, wow.
**Jim Porell** 27:33 What are you doing workin'? How do you have time?
**Richard Nikula** 27:35 Yeah, right.
**Greg Shriver** 27:35 Yeah, I was just gonna ask, how long does this take you? Wow.
**Richard Nikula** 27:41 I start putting them… I start organ… well, it's an all-year thing.
But I start physically putting them out, I start in October.
Oh, wow. And get serious in November.
**Angelika Heinrich** 27:53 It takes me a lot longer to put it all away.
**Greg Shriver** 27:57 I'm sugar.
**Jim Porell** 27:58 Well, and I always tell people, because I have motivation to put it out, right? This is the motivation, and when I get it out, this is what it looks like.
**Angelika Heinrich** 28:06 Yeah.
**Jim Porell** 28:08 Where do you live? Looks like a lovely climate. California?
**Richard Nikula** 28:12 This is Houston. Yeah, it's a lovely climate for a few weeks a year. Yeah, it's true.
Yeah, yeah.
Anyhow, then…
**Angelika Heinrich** 28:21 That's really cool.
**Greg Shriver** 28:22 Amazing. That's very nice. Wow, very nice. Thank you for sharing. Oh, man.
**Angelika Heinrich** 28:27 I'm just gonna screen capture and send this to my.
**Richard Nikula** 28:29 Oh, sorry, I just stopped.
**Angelika Heinrich** 28:30 Too late. Too late.
**Richard Nikula** 28:32 Go to… Magnolia Musical Christmas. If you search that, it's on YouTube, it's on a few places, but…
**Angelika Heinrich** 28:40 Oh no.
**Richard Nikula** 28:41 Magnolia, like, the three musical Christmas.
**Angelika Heinrich** 28:44 Awesome.
**Greg Shriver** 28:46 Richard, I'll let you put that in the meeting notes if you want to share.
**Richard Nikula** 28:51 Oh, that's true, it's all recorded, right?
**Angelika Heinrich** 28:55 Well, I think that was a great, a great end to the last meeting for us here.
**Greg Shriver** 29:00 I would agree.
**Richard Nikula** 29:03 Okay.
**Greg Shriver** 29:05 All right, well, thank you all. Yeah, thank you, yeah, thank you for that.
**Jim Porell** 29:09 Have a happy holiday.
**atoulme** 29:11 Good morning.
**Greg Shriver** 29:11 Nope.
**Richard Nikula** 29:12 Alrighty.
**Angelika Heinrich** 29:13 Happy holidays, everyone. See you in the New Year.
**Jim Porell** 29:15 Right.
**Andrej Chmelo** 29:16 Yep, same. Bye-bye. Happy holidays. Bye.
