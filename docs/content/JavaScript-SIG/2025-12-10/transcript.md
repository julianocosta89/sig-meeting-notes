SIG: JavaScript SIG
Date: 2025-12-10
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Marc Pichler (Dynatrace) 00:01:15 No.
Jamie Danielson 00:01:20 Hello.
Hector Hernandez 00:01:22 Aye.
Trent Mick 00:01:24 Yo.
Jamie Danielson 00:01:43 Just gonna give it another minute or two before getting started.
So I wish you could, like, change the shape of the… Bar with the meeting controls.
Because it's always just super long.
Marc Pichler (Dynatrace) 00:02:19 I usually just move it to the other screen.
Jamie Danielson 00:02:22 Yeah, doesn't…
Marc Pichler (Dynatrace) 00:02:23 Get in the way.
Jamie Danielson 00:02:25 I was trying to figure out how to keep mute closer by.
In case… I need it.
I don't know, if it's in the other screen, I can never find it.
Alright, we can probably get started. Let's see… Okay.
So, first topic, right, today is the 10th, first topic is David.
David Luna Bistuer 00:03:42 Hi, everyone. Just this… just a quick one, just a couple reviews.
There was an ancient issue about, init method, with instrumentation-based.
But I could… Searching for a solution, and kind of the idea is… Yeah, basically the problem here is, like, init method, it's called in the constructor, and sometimes the instrumentation classes are not fully initialized.
So some properties, some private properties, or other properties are not defined yet, and we might run into issues.
Yeah, so kind of my solution to that, or also maybe a proposal to improve the… how to create instrumentations, is that, to provide a factory function. So yeah, there's a lot of… a lot of comments there, so if you want to know more about it, you can just, go through the comments of that issue.
One of the ideas is, like, to provide this, factory function, this kind of a… would say it started as a POC, but now it's kind of more solid. So, did you… the new ideas, like, to provide… create this rotation factory that say it's an object with a specific API.
Then that factory function takes care of wiring everything up with the required in the middle and import in the middle.
And just calls here, methods from that delegate object, when… when appropriate.
Okay, so there's an example. So I've done the… the API, but also I made a… a test, so the HTTP instrumentation, now we have another HTTP interpretation, which is HTTP delegate.
With Hassels with us, so… Of course, if we want to apply that, I need to do also the same API for browser, and then apply for fetch, XML HTTP request, and so on.
Maybe in another PR.
But at least, with this set of changes, you can see how is the API and how can it be applied to a coordinates imitation.
Okay, so it's a big one, so take your time, but just a heads up.
How about this?
Jamie Danielson 00:06:02 Cool.
Thank you. Yeah, this will take a little bit of time to read through.
David Luna Bistuer 00:06:07 Yeah, yeah, code is pretty similar.
But just the idea is, like, instead of just using inheritance to get treasures, or, you know, and get the hooks, and have everything in a state within the same object, what I'm using is, like, okay, so it's the factory function, what it's doing is, like, it's decorating that object.
with, with hooks, with, all this kind of stuff that is needed. And also.
the HTTP installation, the new instrumentation, could… could be.
really different, because now you're not, forced to use a class, but I used a class just to, you know, if you check, if you make the diff within the original HTTP instrumentation on this new one, there is just a few differences.
So you can keep… you can keep the same, you know, the same structure. You can keep a class if you like, or you can just give a plain object.
And have a state somewhere else, like, maybe in the top… in the top scope of your model, so… Whatever you like.
But the idea was just to make it as similar as possible.
Also, to make… to make, you know, to let the review to be easier. Also, the tests are kind of the same, just the difference is that the way that you are creating this notation.
Jamie Danielson 00:07:24 Nice.
Cool.
David Luna Bistuer 00:07:28 That's it.
Marc Pichler (Dynatrace) 00:07:31 Thanks for embarking on that.
it would be good to solve the underlying issue. It's been around for quite a long time, so I'm excited to see that heading in the in the direction there.
Jamie Danielson 00:07:53 Nice.
Cool.
Whoa.
Sorry.
I'm just putting a note in here.
Nice, thank you.
So yeah, I guess if we're gonna take a look when you get a chance.
Trent Mick 00:08:35 Just a question on that, David. Is the main motivation to support Like, the browser instrumentations that obviously Have no need for the… Require in the middle, import in the middle.
books. I guess it, like, it also would help maybe, if I'm understanding correctly, the Indici one that's based on diagnostic channels and also doesn't need any init.
Step.
David Luna Bistuer 00:08:57 Exactly. So, as for now, it's just mimic a little bit the same API that you have, but maybe the init method should be renamed.
But also, it's kind of, yeah, it's kind of, making two birds with one stone. So for web instrumentations, it would be easier for them, and also just exporting a function, it would be… More, friendly for bundlers and… Another step.
Trent Mick 00:09:27 Thanks.
Jamie Danielson 00:09:33 Marilla, you're up next.
Marylia Gutierrez 00:09:36 Yeah, I just had a quick question, because I was reviewing a PR that they are seeing, like.
There is specific case that might create a lot of spend, so they want to do, like, a skip.
not as the default, but an opt-in option to just skip the… basically connect for Postgres. The PR, for me, just, yeah, looks fine, but I was just wondering, do we have any guidelines about, like, skipping particular parts?
Of instrumentation.
Jamie Danielson 00:10:08 Skip these space.
Trent Mick 00:10:09 Dude, do we have something like that for GraphQL? I'm probably misremembering, but I know GraphQL kicks out reams of spans.
Marc Pichler (Dynatrace) 00:10:16 Yeah, that's the, trivia Resource Spans, I think the card. That you can disable.
or enable, but something like either or. One of these things, is possible there.
Yeah, I think the way that we have done it in the past, was to add an option.
for that instrumentation for people to be able to skip it. I would say anything that's in SEMConf, we shouldn't allow to skip.
So, if the connect span exists in semconf.
Then we would just keep it around, I would say, and not allow people to disable it.
Marylia Gutierrez 00:11:06 Because I don't think that is on a stable part.
Jamie Danielson 00:11:17 Yeah, I guess not probably… I don't know if any instrumentation attributes are stable?
Yeah, right? I could be totally wrong.
But…
Marylia Gutierrez 00:11:28 Yeah, because the ones that we have is more for, like, running the query itself. This is skipping just the connect part.
It's just because the concern is… mostly about the pool, that you're gonna, like, okay, get another one, and every time you get a new connection from the pool, it creates a new span, but that would help if it is, like, okay, you have a problem on your pool, you can investigate, but on a day-to-day, it's gonna create a bunch of, like, tiny ones that are mostly noise.
So that was the, kind of, context behind this PR, so give the option to just skip those, so don't create at all. But I don't know if we have this one was asking, any guidelines for… for this?
Jamie Danielson 00:12:15 Yeah, that makes sense. So, I like… I think both of those things make sense, like, if we want to double-check if there is anything in spec or semconv that says that you have to have those, which we don't think that they're…
Marylia Gutierrez 00:12:25 No, there isn't.
Jamie Danielson 00:12:26 Okay.
then I think, like, yeah, right, what the other people are saying, that we have it with GraphQL, so if anything, maybe we change the name of it to be ignore instead of skip, unless there's… is there… I didn't… I haven't looked at it at all yet. Does skip make more sense, or is it just, like, semantics, just a different… Word.
Span.
Marylia Gutierrez 00:12:53 Yeah, because I think they use it the same, because we have the instrumentation for flags, so if you, like, scroll up, there is the… should skip instrumentation, like, all together. Go a little down… If you see, like, the… on the red one that is.
Jamie Danielson 00:13:10 Oh. Okay.
Marylia Gutierrez 00:13:11 So there was already, like, a… Should it skip instrumentation? So they just added the, should it skip the… Deconnect. Kind of, like, keeping a similar…
Jamie Danielson 00:13:23 The naming there…
Marylia Gutierrez 00:13:25 of Skip.
Jamie Danielson 00:13:28 What is… should skip… Instrumentation.
It's interesting.
Like, I'm curious, because what do we have… what are the other things we have? We have, like, suppressed tracing…
Marylia Gutierrez 00:13:44 I think it's on YouTube's, yeah.
Jamie Danielson 00:13:50 Should skip instrumentation.
Do we have that in other ones?
Marc Pichler (Dynatrace) 00:13:56 Oracle DB has it.
Trent Mick 00:13:59 These are just internal methods, though, right? Yeah. That's their internal thing to capture the required parent span as the config bar for that one.
So not really in the same thing.
Jamie Danielson 00:14:11 If the… the… the only…
Trent Mick 00:14:14 The only ones I'm seeing in config options is, the ignore ones from.
GraphQL.
Though it's kind of hard to search just…
Jamie Danielson 00:14:26 Ignore 122 files.
Well… I guess we have ignore layers in Express and some of the other ones, right? Like, ignore…
Trent Mick 00:14:37 There's ignore or.
Jamie Danielson 00:14:38 Nice.
Trent Mick 00:14:38 spans, and it's a SQLized instrumentation, so I think we have… Both happening.
Jamie Danielson 00:14:46 So maybe… It seems like the, like the… Skip is used mostly for internal Methods… And ignore is… Used in more of the instrumentations for… This sort of thing.
So maybe, like.
the idea seems reasonable, and maybe we just change to ignore so it's slightly more consistent API with the other ones?
Trent Mick 00:15:20 I'm thinking ignore.
I see ignore network events and ignore performance paint events in document load. Ignore layers and layers type in Express.
Jamie Danielson 00:15:37 Okay.
And I think, Marillia, you… you know more of the PG instrumentation than at least definitely more than I do, or maybe a couple others, do you see any… reason… Why this is, like, doesn't make sense?
Maybe it's just a bit of double-checking.
Marylia Gutierrez 00:15:56 Yeah, it was more double-checking, I think, like, makes sense, the PR itself, like, the changes are very minimum, nothing, like.
that concerned me was more, like.
If we have some structure that we should be following.
Jamie Danielson 00:16:09 Yeah.
Does anyone else have an obvious objection that we haven't thought of?
So yeah. Yeah, I guess it seems like right now it's probably… Probably good to go then, and just changing to ignore.
Yeah.
Marylia Gutierrez 00:16:26 Okay, I'm gonna create.
Would I add the comments there?
Jamie Danielson 00:16:30 Cool, yeah, I just threw a couple notes in the doc, if that helps.
Marylia Gutierrez 00:16:38 That the one I just… Yeah, my next topic's just a reminder, if anyone was planning on submitting Lightning Talks, the deadline is this week.
Jamie Danielson 00:16:47 There's more.
Oh, for the maintainer trap. Is this for… are they…
Marylia Gutierrez 00:16:53 So, no, it's project lining talk, maintainer track, or ContribFast?
Jamie Danielson 00:16:57 Oh, I see.
Marylia Gutierrez 00:16:58 Those 3 things are… By this week.
Jamie Danielson 00:17:03 Did we do a ContribFest, do you know, this year?
Marylia Gutierrez 00:17:06 So, we are doing, but we are considering the topics, or who can help out, might be, like, Weaver-related.
horrible.
Yeah.
Jamie Danielson 00:17:16 Gotcha. Okay.
Cool. Yeah, so this one's in Amsterdam, so, big thing I've been pushing is, like, everyone loves Amsterdam, and it's always good to meet up with people there, so when you get a talk accepted, usually your employer's more likely to help make sure you're able to get there, so… agree, that's a good idea.
Marylia Gutierrez 00:17:37 Just a reminder, for Project Lenny Talk, if you get accepted, you do not get a pass.
Jamie Danielson 00:17:42 Oh, really?
Marylia Gutierrez 00:17:43 Yeah, it's different. There is the note there. Usually for Lightning Talks, you don't get it. If that is the only one, then you got accepted.
Jamie Danielson 00:17:52 Ben.
Still worth checking out.
It'd be awesome to have everyone go to this.
Cool.
And I think this has… so one speaker per lightning talk, and then I think there's also… there's usually a limit to how many things you can submit in general. Does this… have its own… Max, I wonder? Not sure.
Just something to keep in mind.
If there's a limit, but… Since this one's separate, it's probably got its own separate… limit.
Marylia Gutierrez 00:18:32 Yeah, it's not… it's not the same limits as the main one, yeah.
Jamie Danielson 00:18:35 Nice. Cool.
Right?
Anything else on that one?
Alright, so I put a note on here, because I realized we didn't talk about this last week.
So we have this issue for, like, focus topics for the Sing. The idea of when I think we first created it was also around when we wanted to do SDK 2.0, because we had been kind of… put, limping along with it for months and months and months, and finally, at the time, we said, okay, we have to try and focus and make sure we get it done, and we did, which was awesome, and I think that was how we realized it was useful to have a few things to focus on.
But also, we've realized we haven't really looked at this or updated this in a little bit. So I was gonna do it before this meeting, I didn't get a chance to, but one thing that's specifically missing that I want to add into here is the declarative config, that we've been working on, especially Marillia, who's been pushing most of that.
We want to have that on one of our, you know, upcoming backlog items to work on. Wanted to sort of note I guess the idea on this is to have, you know, the big things that we want to work on are something we're definitely focused on. I know we've talked about semantic conventions a lot, and it's been sort of sitting out here for a long time also. So, you know, people do have… any cycles, any space to work on this. This is useful because the sooner we get this done, the sooner we can move these out of the way and get working on the next things. I don't think there's much left to do on here.
But just, you know, if we see PRs out here for these, let's definitely get them reviewed and merged in as quickly as possible.
And then also on upcoming, I… wanted to update this to move the log stabilization effort up there. We've talked about that in a few of the meetings in the last few weeks. I think we're pretty close, right? There's a milestone, there's only a few things left to look at.
But the, you know, by being able to get that done, too, that also lets us keep moving through and picking up the next pieces, because… again, we've been working a little bit, but very slowly, on the config file implementation, and I think that's super important, and since it has a lot of eyes and traction right now, it would be nice to Be able to get that.
as one of our focus topics. Right now, the main holdup is that it's relying on experimental things that we need to stabilize, like, say, the logs. So, the sooner we can get those done, the sooner we can keep moving along with other things. So just kind of wanted to mention this. Like I said, I want to update this after this meeting for the missing declarative config and putting logs into the upcoming, or maybe even current, we're kind of working on that too. But, I guess, if anyone has any questions, or… Thinks that we should update things or whatever, If you want to talk about it now, or separately, just kind of wanted to… Bring attention to it, or if anyone has thoughts on it.
It's one of those things that's super hard, because… there's so many things to work on, as we all know, and everything's kind of… these are the very much less interesting things to work on, which is why it's been sitting out here for so long. But I know, Trent, you've done a lot of work on this, and really, I think you've done a bunch.
As well, so, we'll just keep working on that, and I'll try to help out here where I can to try and get these just done so we can… Move along off of these, finally, and be able to get rid of all the extra maintenance code in a few months.
Marc Pichler (Dynatrace) 00:22:30 Yeah, I think one thing that I would like to add to this is, Probably, since the next thing up will be… the SDK stabilization for logs.
we won't be able to do exporters at the same time, because they also depend on, logs. So, for stuff like declarative config and things like that, we could Probably start doing that already once, we… clear out, some of the existing work. So, thinking about HTTP, and database semconconf.
Once we get that out, we can start also on log stabilization, and then if there's a second topic, then… It could be, declarative config, or it could be something else, depending on, like, where our priorities are. But whatever we get done opens up a new slot for, something else to take its place. So, getting things done is, the way to move forward there, I think.
Jamie Danielson 00:23:49 Damn.
Marylia Gutierrez 00:23:53 So, just to clarify, if I keep putting PRs for the Clarity config, are they gonna get review or not?
Jamie Danielson 00:24:02 They're going to be slowly reviewed, not as an intentional, like.
fully ignoring kind of a thing. More of a… the reason… this came up the other day, because we were trying to figure out… I feel like an API for something, or, like, if something changed… And what would end up changing for the end user. Or, like, if we implement something one way, and we end up changing, say, logs, and have to rewrite how it's set up.
I think that's part of where it came up the other day.
And so there's a current concern, I think, that if we do… well, okay, it's a couple of things. One, if we do too much, and then have to rewrite it, but also, Since it is, like, a feature versus some of the other things for maintaining current Stuff and stabilizing the pieces that are needed for it.
The idea is that if we put the effort into that and get those done, they get done faster, and then we can go full steam ahead on this as well.
That was not a full… straightforward, obvious answer, because I also have the interest in moving the config file forward, too.
But it does become difficult. Like, when we put all the focus on SDK 2.0, last year, was it last year? We were able to finally get it done and off our plates, which was nice. And so I think that's kind of the hope right now, is these other priority items that have been sort of lingering, languishing, maybe, Hopefully, if we… if we just put all the focus and effort into there.
They get done faster.
That's mostly just what's limited.
mental… capacity, I guess, or context windows for the day is what slows down reviewing feature PRs.
So I think…
Marc Pichler (Dynatrace) 00:26:03 Yes, the answer.
Jamie Danielson 00:26:04 Huh?
Marc Pichler (Dynatrace) 00:26:05 the… I guess the answer is, to the original question. We will still try our best to, like, review all the PRs that are out there, but the database and HTTP SEMConf stuff will get priority for now, once everything has moved up, and then, once declarative config is in that focus topics area, then it will get the same attention that HTTP and database SemConf stuff does now.
Which ideally should be a lot of attention, too.
Get it done, and then hopefully stabilized as quickly as possible as the spec also moves to a stable state at some point.
Jamie Danielson 00:26:52 Yeah, I think it ends up becoming probably a more… a better… a better experience once we do have more eyes focused on it, which we were thinking we were gonna do. That was sort of my plan this fall, right? Of, having that as a top focus, but once we realize we still have to get these other things done, I've had to also set that aside.
Still looking at upstream declarative config and hoping, you know, trying to keep that moving forward. But… In the meantime, I think it's going to continue to be a slower process until we get the other things done.
Any other… Questions, comments, thoughts?
Anyone on that?
Like I said, we can also chat separately if… Things come up later, but… Okay.
Next up, Trent?
Trent Mick 00:28:04 Sure, likely a small thing. On one of the PRs for the… semantic conventions, earlier brought up a point. So, I was going through… so this is for the tedious instrumentation.
Did it not link to the particular line?
Search for a to-do in here.
Jamie Danielson 00:28:23 Is it hidden in one of the… oh, here.
Trent Mick 00:28:26 Okay, so as… when I was doing this PR, hmm.
I guess, to give. So… the… the database migration PRs that have been… doing, They're of a certain quality?
I wouldn't say that it is… solving all of the universe's problems in these things. So, to be specific, The database instrumentations typically emit a set of attributes on the spans. Mostly this is about span attributes, not always, but in this case it is.
And part of the migration is just migrating those to the new span attribute.
Which is fairly straightforward.
But then there also… the database migration also involved a number of other attributes that aren't necessarily Weren't necessarily being covered, and, I think for some of those attributes, they're recommended in the stable.
semantic conventions, so as part of my PR sort of migrating, I haven't been touching on Necessarily touching on the recommended attributes.
And so, at least in this case, I put a couple to-dos in there, just as I was passing by, as thoughts, like, oh, okay, well, sometime it'd be good to come back and do a better quality run at, for example, the tedious instrumentation.
And look at doing some of the recommended steps in the database semantic conventions. So, I slapped in these to-do comments. Would people prefer, generally, that I, create an issue, that's what Marilla is basically asking for each of these to-do things.
I'm fine to do that, I just don't know. I mean, for example, TDS does not have a maintainer.
Jamie Danielson 00:30:19 I kind of… like both. Happened to be told no on that. But… the to-dos are useful if you're not looking at issues, and you come across this, and you're like, oh, I want to help implement this, whether it's tedious or something else. But even an issue, even if it's not for every specific thing, maybe we have an issue similar to the existing, you know, update SEMCOM stuff of, you know.
second pass, because we didn't do it for HTTP either, and I think we have a few to-dos in that as well. Maybe we just have another issue, even if it's backlog, that says revisit, or… Whatever the, attributes that haven't been implemented yet.
For various instrumentations.
Trent Mick 00:31:05 Okay.
Jamie Danielson 00:31:06 The to-do… the main reason why I like the to-dos is you've kind of already done the work of what maybe should be in here, Right? Like, so you've already looked at, okay, we don't have this, or is this the right thing, and whatever, so it's kind of nice to have that. That could, I guess, go into an issue and say, like.
tedious notes.
blah, put that in there. But I can see us having both, having that be useful.
Cause we should probably have that at some point.
And if we combine it onto one issue. Sorry, Marilee, go ahead.
Marylia Gutierrez 00:31:41 I was gonna say, there was one type of format that I used to do, like, a prior company that I really liked, that was, like, something like this. So you can add a to-do, create an issue, and your to-do had the number of the issue.
So this way, you can have one for, like, all of those, add the missing things, then you put the to-do with the number of the issue. So it doesn't matter which source you came from, you know that it's the same thing you can assign to the things and whatever.
Trent Mick 00:32:07 I'll do that.
Jamie Danielson 00:32:09 That's good.
Yeah, and especially if we do start with, like, one generic issue that's very easy to then drop into anything else, And if we end up creating specific issues from there, cool, we can change it, but having a generic issue that says second pass it.
Instrumentation updates, I like that idea.
Trent Mick 00:32:27 I'll probably do a specific one, so it'll be, like, a tedious.
Here are some things you can do to follow up for a stable sync comp.
Jamie Danielson 00:32:34 Cool.
Trent Mick 00:32:37 Thank you.
Jamie Danielson 00:32:39 Thank you.
Nice.
Cool. Any other… Walk on topics top of mind before we go triaging?
nuts.
Okay… MJS hook hangs when using Experimental Loader.
Node.js24+.
Marc Pichler (Dynatrace) 00:33:50 This very much looks like an issue to be opened at the input in the middle repo.
Since we just re-export essentially the same hook, I would assume that the same thing also happens with input in the middle present.
We don't instrument that package.
Specifically, so…
Jamie Danielson 00:34:15 That might be something that we want to open… Ow.
Of this statement.
So if anyth…
Marc Pichler (Dynatrace) 00:34:43 Yeah, so that's the sampler that they provide here.
It's really just importing it.
And then… Everything stops working for them.
Jamie Danielson 00:35:01 Yeah.
So, what I'm thinking about… I mean, I guess I don't know if we have… like… Prior art on this particular thing, if the issue is with… the hook, and we're really giving them our hook to use. It's probably something that we should open upstream versus asking them to do Since it's technically our hook that they're using, and that's what we tell them to do, right?
Okay.
Marc Pichler (Dynatrace) 00:35:32 reap.
Jamie Danielson 00:35:36 And this… let's see… The entire application hangs, which is… bad.
Marc Pichler (Dynatrace) 00:35:46 Yeah, that would be P1 in that case.
Jamie Danielson 00:35:56 So… I'll assign myself on this right now to open the issue and follow it. We'll see if I can… do this to…
Trent Mick 00:36:43 You could also verify that… or to give them… have them give their actual hotel setup code.
COTL setup code block is…
Jamie Danielson 00:36:51 True.
Trent Mick 00:36:52 Awesome.
Marc Pichler (Dynatrace) 00:36:53 I think they're just using, auto-instrumentation's node.
Oh, no.
Jamie Danielson 00:37:26 Okay… That's over.
Okay.
Buffers are not serialized correctly as for the proto-JSON specification.
Using the OTLP HTTP exporter.
Marc Pichler (Dynatrace) 00:37:55 Yeah, I think that's because we just, probably put the actual Viewing the iterate into the data.
Thing.
I think we need to, add this to the… milestone for… blocks SDK stabilization.
Because it essentially means that our types, for the attributes aren't correct when you're using the JSON exporter specifically.
My guess is that it would work with, the protopuff exporter.
I've seen similar things in the past.
Jamie Danielson 00:38:48 Okay.
Marc Pichler (Dynatrace) 00:38:48 I'm not sure if this was fixed already by, by the change that Jared did recently, switching out the… Protopath chair's library with… Something else… I think… I feared.
Wait a second, let me check… That's 61.92.
I'll drop it in the chat.
Yeah, that's the one.
So, essentially, what this does is, Previously, we had used, Protopuff.js, which had some trouble, working properly in the browser. So, what this does is it uses, use a different generator, which doesn't use protopuff.js in the background.
And that also uses the same thing for generating JSON.
I guess one way to check would be… to just… Run this against the collector, and see… If the same input would… Still… cause the same result. I can take a look at this one. If you assign me, I will…
Trent Mick 00:40:49 He links it to a pro repo, but the package.json in there shows that he's still using SDKv1.
Era stuff.
Maybe the issue still exists, but I don't know.
Jamie Danielson 00:41:03 Hmm.
Marc Pichler (Dynatrace) 00:41:04 Hmm.
Yeah, it might also be a case of, outdated… Dependencies.
Trent Mick 00:41:11 I made this, like, 5 days ago, so why are people still using those old versions? No wonder.
What leads to that?
Jamie Danielson 00:41:40 I'm just putting notes in here so that we… And so I guess this is…
Marc Pichler (Dynatrace) 00:42:32 I just assigned P2 to it. Okay.
Because telemetry goes missing when… When that bug occurs, so… It's either incomplete or incorrect.
Jamie Danielson 00:42:48 Okay.
Marc Pichler (Dynatrace) 00:42:49 And I think it's really just, HTTP exporters that are affected by this, so… It's on the side.
Three HTTP exported labels.
Jamie Danielson 00:43:08 And you noted that you think we should put it on the log milestone?
Marc Pichler (Dynatrace) 00:43:13 Yes, I think so. Since… the OTRP export is affected, I think we need to sort it out before, marking stuff is stable.
Jamie Danielson 00:43:28 Makes sense.
Okay.
Maliformed metric export of value type is not specified.
Marc Pichler (Dynatrace) 00:43:46 I actually handed this one off to another person who, Said that they would like to…
Jamie Danielson 00:43:55 Huh.
Marc Pichler (Dynatrace) 00:43:55 Look into it.
The summary for that one is that, if our types are correct and the problem just, curse when… Passing in data that doesn't adhere to the type, then we would say this is a won't fix.
because we don't have, checks for… Most of our stuff, to check if the actual types are correct.
And if we were to start adding this there, we would likely need to add it everywhere, and We'll probably never get done with doing that.
Also, metric producers aren't… that common of a use case.
They were kind of added to the spec as an afterthought for, bridging between… Previous, or non-Outerre, metric systems.
to alter.
And, I haven't seen that many metrics.
Custom metrics producers out in the world.
Jamie Danielson 00:45:16 Okay.
So it's, like, also potentially a lower priority.
Marc Pichler (Dynatrace) 00:45:22 Yes, I think without actually having checked it, it's difficult to assign a priority. It would be, at most, P2, Possibly lower.
So I guess we could assign P2, and then, reduce it to…
Trent Mick 00:45:44 Whatever the priority is later on.
Jamie Danielson 00:45:49 You think, should I change the assignee to this other person from you?
Marc Pichler (Dynatrace) 00:45:53 They've commented.
Jamie Danielson 00:45:54 We should be able.
Marc Pichler (Dynatrace) 00:45:55 I think that would be great, yes. I should have done that when I posted the comment, but I didn't.
Jamie Danielson 00:46:03 It's okay.
Marc Pichler (Dynatrace) 00:46:04 Thank you.
Jamie Danielson 00:46:11 So I'll remove triage, too, because that's primarily for putting the… P label on there, isn't it?
Marc Pichler (Dynatrace) 00:46:20 Yes.
Jamie Danielson 00:46:24 Cool.
Alright, so that's those. Seeing if any new topics came in… I think so.
AI not working when… Create with responses used.
Marc Pichler (Dynatrace) 00:46:53 Looks like there's something on.
There, which gets lost when we instrument stuff.
Jamie Danielson 00:47:28 Okay, do we have… Guess probably, like, a code owner?
Well… Not in here.
Marc Pichler (Dynatrace) 00:47:43 It's in.
Jamie Danielson 00:47:44 component.
Marc Pichler (Dynatrace) 00:47:45 comment on us.
Jamie Danielson 00:47:48 So, Trent? -Oh.
Trent Mick 00:47:50 I stopped paying attention. Which one do we ask?
Jamie Danielson 00:47:54 Calling you out.
No, so this was a question on the OpenAI instrumentation. I guess there's something that's not being patched.
And so, an error is thrown, with response is not a function.
Yeah. It seems like.
Sounds possible. But, I guess…
Trent Mick 00:48:17 Yep.
You can assign to me.
Jamie Danielson 00:48:21 Just assign you.
Trent Mick 00:48:24 Yeah, sounds good.
Jamie Danielson 00:48:35 Okay.
Right, so that's our… Bugs… Look at each of these. Can't remember if we looked at core last week.
Marc Pichler (Dynatrace) 00:48:50 I think we did Contrip last week.
Jamie Danielson 00:48:56 Should we swap and look at core?
Entities prototype.
There's more in Contrib still, though.
So… What is the latest on this?
Oh.
So I think this one is still kind of looking for… Maybe a little bit more input from… Other front-end folks, it's definitely stalled.
This is not really browser.
So, I don't think they talk about it in… the browser… SIG. I don't know if there's another… Client side.
There's another client-side SIG or not right now, but this might be worth… Potentially looking at again.
I guess.
Marc Pichler (Dynatrace) 00:50:04 Yeah, I think…
Jamie Danielson 00:50:05 modes in here.
Marc Pichler (Dynatrace) 00:50:06 Yeah, this was just a very quick pass at the, instrumentation itself.
I think this will indirectly benefit from the work that the browser sync is doing.
Though it's not, like, entirely, related to the same thing.
Jamie Danielson 00:50:32 Yeah.
Marc Pichler (Dynatrace) 00:50:41 I feel like this might even, warrant having another SIG being spun up at some point.
the same way as, like, Android and iOS are the same, their own 6, I think.
Jamie Danielson 00:50:59 This had come up, I feel like, when this instrumentation was first being proposed. I feel like… they may have requested to have a SIG or working group, and it was decided that there wasn't enough people to do that. So I feel like this ended up being in sort of this weird limbo state.
hmm.
Marc Pichler (Dynatrace) 00:51:23 it's difficult for this one, specifically, because I feel like we can't just close it. There's, It is the most… it is the single most requested feature, if you go about, if you count by thumbs up on issues.
Jamie Danielson 00:51:41 Yeah.
Yeah, it has a long and sordid history, because originally that issue was closed, and that… Caused a lot of problems.
Yeah, so there was a request in October to have a React Native working group And… Lack of staffing.
Hmm.
I feel like… Maybe this ends up needing another, like.
look at some point, if it… I don't know.
Marc Pichler (Dynatrace) 00:52:44 Well, I'm mostly worried about, with this PR is that… It adds a lot of dependencies to, The repo, which is already suffering from many dependencies, and… like, it doesn't look too bad, when you just look at the thing here. It just looks like any normal, any normal JS package there. But once you start looking at the package log, and… Checking which transitive dependencies and stuff like that are being pulled in, it kind of starts painting a bit of a different picture.
Trent Mick 00:53:34 Only 72,000 lines.
Marc Pichler (Dynatrace) 00:53:38 I… I think, like… There is… So, the question that we have to ask about this is, is there a reason to… for it to be in the contribo, other than discoverability? And I don't think there's a good case to have it here.
It being split into a separate repo would definitely, help development speed and, like, just focusing on that sort of stuff.
But then we run into a similar issue as we have.
with… Browser essentially being in a different repo, where if we introduce something in the core repo that doesn't work in the browser, and we don't catch it there, it's kind of affecting the other ones as well.
So, there's a need to figure out how do we do testing and stuff like that.
End.
I think once that has been figured out by, Like, the browser sig and us.
How we're gonna do testing from… Then on… then it also becomes a possibility for… another repo to exist, which is just focused on React Native.
And, moving stuff there and copying a lot of the approaches that the browser sync will be doing.
That is a lot of ifs, I do realize.
There are… there are steps, that can be taken once.
Everything has started up, and… One way of working has been established there.
I think one thing to add to that is, react Native is, thing that's been requested quite often, but I still think that the appetite for, support… for browser support is more than, React Native support.
So it seems to be the clear priority for now.
Of people working on web first.
and, React Native later.
Trent Mick 00:56:36 Thank you for answering with concrete details. I haven't, and I've been mostly staying silent. I hate saying no, but what a humane thing to do.
B to close this as not planned?
Or at least not planned right now.
I mean, I agree with you because of the… The load here and the lack of expertise in the maintainer group, that we can't support this well.
At least in this repo.
Jamie Danielson 00:57:05 Is there an issue? There's an issue.
Right.
Each of these things.
That is the one with… Whole bunch of those.
And this is the instrumentation request. Like, one thing that we could do, Yeah, as if we, like, keep the… like, if we were to close the PR as not planned, but keep the issues there, And I don't know if we have some kind of label for, like, Maybe one day.
Or later, like, somehow… I'm not sure, but we can't close this. This is the one that we closed that, definitely… cause some problems. But yeah, like, I don't know that it makes sense to leave the PR open.
I can at least put some notes on there of what we just chatted about.
Marc Pichler (Dynatrace) 00:58:09 I wonder if we should put the notes on the issue in the core repo.
And just link to it from, from the PR.
Jamie Danielson 00:58:22 That makes sense.
Marc Pichler (Dynatrace) 00:58:25 I guess people would go towards the core repo and, like, check the support for React Native issue, Possibly on a more regular basis, and then… I think… Buh.
If we have some… clear guidance on, like, what we think the steps are that are needed to get to a point where this becomes a thing. People might be… More understanding of the whole thing.
Because if we say the browser sigk is doing this, we are hoping that this and that will happen, and… People can then copy that workflow and start working on, like, a different repo on that instrumentation.
Using that same workflow.
It… Kind of gives a timeline, or at least gives people a series of events that need to happen for that to move forward.
And that might be good enough already.
Or better than no update.
Jamie Danielson 00:59:40 Yeah, because right now, in the state of no update, no one's… I guess no… like, myself included, no one's really sure of what the next step is, or who needs to do what, or whatever, so… Yeah, I'll put that note in there. Sorry, we're at time. Thank you for the details on that. I'll put a note in the issue and link that PR.
And we can see if that… You know, generates any more interest in seeing if there's something that they can do now, or if it's, you know, works as we need it to, of pointing to, here's why we haven't done this yet, and, you know, it's on the… it's on the radar.
Cool.
Marc Pichler (Dynatrace) 01:00:15 Yeah, thank you. If you, if you need anyone to have a look at the comment before you post it or something like that, feel free to send it to me, and I will have a look at that.
Jamie Danielson 01:00:27 Sounds good. Thanks.
Marc Pichler (Dynatrace) 01:00:29 Okay.
Jamie Danielson 01:00:31 Well, thanks, everyone. Sorry for keeping you a minute over, but we'll see you next week, and see you online.
Bye.
Hector Hernandez 01:00:39 Thank you.
Marc Pichler (Dynatrace) 01:00:40 Thank you, bye.
