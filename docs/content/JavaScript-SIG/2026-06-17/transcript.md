SIG: JavaScript SIG
Date: 2026-06-17
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Trent Mick 00:00:36 Let's see if someone else came, I thought I was in the wrong channel.
Marc Pichler (Dynatrace) 00:01:57 Hello?
Trent Mick 00:02:00 Blue.
Raphaël Thériault 00:02:02 Hello.
Marylia Gutierrez 00:02:36 Before we start, I'm gonna take this moment just to vent.
I'm trying to create the PR to update to send just the HTTP stable, and you think, like, oh, it's very simple, just remove the old stuff.
you make a change, and it breaks 5 files. Like, okay, now I fixed this thing, and then it breaks another 5 after that. So right now, like, at 20-something files change, and I just remove it, like, don't send old one. One day, I will finish that PR.
Trent Mick 00:03:07 Yeah.
HTTPS tests are the worst.
Marylia Gutierrez 00:03:12 Yeah, so right now I'm trying to fix the tests, because I think I've… change it all the places, but there was a lot of places that I did not see it coming, but… One day.
Marc Pichler (Dynatrace) 00:03:31 Yeah, I think a lot of our tests, do just… weird stuff sometimes. Aye.
It's one of these situations where we have a bunch of tests that do test things in a way that we really shouldn't, and then, like, all the other packages follow that same pattern, and then if somebody adds something new, then it also follows that same pattern, so it's, Yeah, never-ending story.
Marylia Gutierrez 00:04:03 Yeah, because, like, if I remove, now I have to, like, update the documentation. But then, like, the tests are gonna fail, so I need to delete that. But now that means all the semantic conventions for the old things are not getting used anywhere, and some functions were only created for the test, so it's so much cleanup for, like, just a couple of things, but yeah, like.
I put it on draft right now, because I'm still fixing tests, but this is just, like, removing stuff.
But yeah, over 2,000 line of just removing stuff.
Marc Pichler (Dynatrace) 00:04:37 Thanks for working on it, though.
Once… once we have migrated to the… to the stable SamCon, everything will be… better.
Marylia Gutierrez 00:04:46 So yeah, actually, I had that question, because the next one that I'm gonna do is the database. So this one was, like, was one PR for everything. So for the database, it's gonna be mostly, like, on-con trip. Should I do one PR per package, or can I do one PR for every day?
Trent Mick 00:05:07 Who… did we… Sorry, not to make it more difficult, but did we have a… A middle ground where we… just remove… just change the… yeah, remove the ability to change it to anything with the default. I guess all the tests need to get removed then, right? Because they'll be testing of the old.
Marylia Gutierrez 00:05:25 Yeah.
Trent Mick 00:05:25 Yeah.
I don't know.
Marylia Gutierrez 00:05:27 Because my initial idea was, like, okay, let's just change to, like, the only value possible is just stable. But at this point, why do I have all this extra code that is checking if it is stable, if it is only sending stable? So this is why the cleanup got quite huge.
Trent Mick 00:05:44 Yep.
I don't know.
One way or the other.
Marylia Gutierrez 00:05:54 Yeah, was this a…
Trent Mick 00:05:55 You know the truth.
If you can find a sucker to review the big one, it's all done in one shot. Otherwise, you gotta find… 20 lesser suckers.
Marylia Gutierrez 00:06:04 So, Trent, what are you doing this afternoon? So the good thing is, like, it's easy to review, because you just see, like.
when it has the word old, it's getting deleted.
Trent Mick 00:06:21 Oh my god.
Not a pun. Okay.
Marylia Gutierrez 00:06:26 But yeah, still need to… I'm still updating the tests, but yeah.
Marc Pichler (Dynatrace) 00:06:36 I guess we can get started now.
So, the first topic here is…
Marylia Gutierrez 00:06:48 Yeah, he asked me to take ownership, but yeah, but I saw that it got already merged, so… Yay! Because, yeah, because they were marking as a release candidate, and they want to have a few merge before then, so thanks for watching.
Marc Pichler (Dynatrace) 00:07:02 Yeah, thanks for, driving the review on that.
didn't have a lot of time recently to dedicate to Upstream.
So, thank you for looking into that. There was nothing left for me to comment on, so, it was good to merge.
After a few.
Smaller fixes in the package log and stuff.
Trent Mick 00:07:28 this environment carrier thing, like, for it to get used by anyone, they have to manually be using the propagator API, right? Around… Whatever, spawning child processes or something, yeah.
Marc Pichler (Dynatrace) 00:07:40 Yeah, it would be the same as if somebody was using the propagator to write an instrumentation for a custom Well, it's card, for, like… If they have some sort of a custom transport thing that… has a trace context attached to it, they would have to, like, also use the propagate API, so, this is similar to that.
And I tried it out, To see if it, like, actually propagates, to… spawns up processes and stuff, and it works fine. So, seems to be very good.
Trent Mick 00:08:23 Okay, great.
Marc Pichler (Dynatrace) 00:08:26 Alright.
Yeah, that one's merged, so nothing to do here. We just need to make sure that, once we do the next release, we just publish the package manually.
Yeah, but since none of the others depend on it, it won't.
Slow down anything on the release.
Then this one… Trend objections to renaming the buffer config.
Trent Mick 00:08:56 So, since I added this, some discussions moved on. So, Mark, you gave your opinion that the way I have it in the PR, it works for you, same with Jared.
I've… updated for Jackson and Jared's feedback.
And then 8 minutes later, Jared… approved it. I would, for one, would like to know Jared's workflow. Like, this guy reacts like that. He's just sitting there waiting, to review things. Anyway, just very good.
So I think that one's ready to go, I'll merge that soonish, but… What kind of the reviews people want.
So that'll change… that's a breaking change for SDK logs. So I guess after this goes in, I'll… oh no, I actually went and looked. There is no current documentation on OpenTelemetry.io using that BashBand processor directly, so there's nothing there that really changes.
I think the changelog entry's good there, so we'll have that.
But, I guess, for people to be aware of.
Marc Pichler (Dynatrace) 00:10:00 Yep.
Trent Mick 00:10:04 And then next, I'll start moving things over to the SDK trace package, so we can… Eventually, deprecate the SKY trace dash star packages. I think David… David can't be on the call right now, because he's… busy with something else, but I think he was gonna help with the migration of the… the few utilities that were in the SDK Trace web package.
To get those moved over to the, Just copied over to the couple instrumentations that use those.
And I think that's it for this topic.
Marc Pichler (Dynatrace) 00:10:44 Sounds good. Thanks for, changing that.
Here, too. This is something that people had run into from time to time. I commented here, as well.
It was mostly copy-paste errors, where people would configure one and then copy-paste for metrics, and then wonder why metrics didn't work, or, like, they did metrics first, and then configured trace, and wondered why it didn't work.
Trent Mick 00:11:11 The same way, the same arguments, yeah. Yeah, cool.
Marc Pichler (Dynatrace) 00:11:14 So… I think this… makes… makes it a bit easier to configure stuff, though. Hopefully, in the future, people would just be using the clarity config and stuff.
Boom.
But yeah, still good to have it cleaned up where we have the chance.
Alright, does anybody have any thoughts on that?
and comments.
If not, then we can move on to Marilia's topic about, plans for… Client to move to the Prometheus work.
Marylia Gutierrez 00:11:54 Yeah, so basically they… they were trying to find… so someone brought this up to me, just to see if anyone is able to help out. The gist is that… that… was this, like, some maintainers?
They were basically, well, maintaining the… this… this one, but they are not able to do this anymore, so they are planning to actually put this officially on Prometheus, not their, like, personal accounts, but that means that they need somebody to help my team, so they are looking for people that has knowledge on, like, the JavaScript side, and not necessarily the Prometheus side, because they say that they can help, on that, but they're gonna need people not just for, like, reviews itself, but whenever there, like, releases and stuff like that. So just, well, things like this would be a good group to ask. So, take a look and see if you think that is something that you can help out, let them know, or, like, hear in the comments, or let me know, because I'm talking with a few people involved in this as well.
Marc Pichler (Dynatrace) 00:13:02 Thanks for bringing it up.
Yeah, if anybody is interested in taking on maintainership of that, I think it, would be good to see that package maintained in the future. I think, if it then becomes a official package, there would also be a possibility to start using that for the Promise exporter, right?
Because the specification, I think, mentions to use the official libraries, the official client libraries for export, and we do that all, in the Prometheus Exporter right now. So, having that… live elsewhere, where people are familiar with Promethos and stuff like that, could also… take some, maintenance burden away from, the JS SIG, so… Yeah, I think it's definitely a good group to ask here.
Trent Mick 00:14:03 Is PromptClient currently being used?
What's he using?
Marc Pichler (Dynatrace) 00:14:09 It's just writing the lines itself.
Trent Mick 00:14:12 by itself. Yeah. Okay.
Marc Pichler (Dynatrace) 00:14:13 Yeah. The… the reason… I don't recall the original… rationale behind that. I think in the past, people have tried to add it, but we refused to… do it because it seemed unmaintained for some time. And… Yeah, also it was not, like, official package. A lot of the other Sikhs, they were able to just use an official package from the Prometheus org.
Or something that was endorsed by them.
And we didn't have that as well with this package, so, If it moves over to the Prometheus org and it is maintained, then there would be… no good reason not to use it, I think.
Trent Mick 00:15:06 Interesting, I was just looking to see how big and complex it is, but it has a dependency on the OpenTelemetry API, which is interesting.
It's creating spans, so it has manual instrumentation of itself.
Marc Pichler (Dynatrace) 00:15:21 Interesting.
So, yeah.
Trent Mick 00:15:23 to enable exemplars, so there's exemplar stuff in there. Interesting. Okay, cool.
Marc Pichler (Dynatrace) 00:15:31 Definitely something worth looking into, I think.
I would volunteer, but I have volunteered for input in the Middle, and I have no time to work on that already. So, I need to… stop myself from… Taking on more things.
Alright, if anybody's interested in that, please head on over to the, issue and comment there, and I think, Then we can move that forward.
Alright.
Next one is Trent.
Review…
Trent Mick 00:16:20 Looks like Marley approved it, so… we're good.
Fair enough.
Marc Pichler (Dynatrace) 00:16:35 This, fail-fast behavior is, a warning. It's not throwing then, right? No.
Trent Mick 00:16:46 So, the… code that handles creating SDK components. So this is… okay, so… For people who aren't as… familiar with. So the declarative config is kind of broken into two steps. There's parse, so parse the file, the YAML file, into an object notation. Currently, that lives in the configuration package, and then there's a create step, which is create all the SDK components from that thing to set up the SDK. And that stuff lives in SDK node right now.
So, this fail fast behavior, which is part of the declarative config spec, I'm changing it so that the… those create functions, that functionality will throw.
But the code that's using to create wraps it in a try-catch, and then just falls back to a no-op SDK. So basically, if there's a problem creating any of the SDK components from the pair of config, it throws up its hands, gives a warning, and then it falls back to a no-op.
Yeah.
Marc Pichler (Dynatrace) 00:17:49 Yeah, that makes sense. Thanks.
Trent Mick 00:17:58 And this has a start, because I just did it for the logger provider so far, so I have to… We'll follow up and do the rest.
Marc Pichler (Dynatrace) 00:18:05 So we will never throw, Or create, in that sense, right?
Trent Mick 00:18:11 And we won't throw for parse either, so it… in the SDK, In SDK node, yeah, so it calls parse, wrap, scan, and try-catch.
I'll create wraps, and try-catch.
And just falls back to an OAP SDK, which is what the Java implementation's doing as well.
Marc Pichler (Dynatrace) 00:18:29 Alright, sounds good.
Thanks for working on that.
Trent Mick 00:18:37 Yep, sure.
Marc Pichler (Dynatrace) 00:18:44 And the next one is my topic here, which is, I'm gonna be out of office this week in July. Anybody up for running the SIG meeting?
This week?
Trent Mick 00:18:59 Yeah, I probably can.
Marc Pichler (Dynatrace) 00:19:01 Alright, thank you.
Right, thank you. Then, moving on… There's a question about… Pierre, we had talked about this. I didn't have a lot of time this week to review, but I took some time today to add a few more comments.
So, there's just… Two small… one larger thing and one smaller thing, I read this code here again, and then realized that it actually does… It does try to await… Like, if there's an ongoing export promise, it awaits that airs, it does this run once.
Bing.
And I think we actually need to… Do it in a way where we… await the ongoing export promise, then… To run once, regardless of whether it was in progress right now or not.
Unless there was another export scattered in the meantime, in which case we actually have applied the effect of the… Of the forest flush here already. I did, Give an example of what I think this could look like.
Yeah, so this is mostly to… oh, sorry, go ahead.
Pranav Sharma 00:20:53 Sorry, I… I did not notice that there were, fresh comments there.
I'll take a look, but since we last discussed, is the behavior changing? Like, is this a new behavior, or… Like.
Marc Pichler (Dynatrace) 00:21:09 This is mostly just making sure that we keep the old behavior, where… forced flush would always do this run once. Before, we had the thing where We force flush, it would.
scheduled an export regardless whether an export was already going on. And this changes the behavior slightly to first await the ongoing export.
And then do the run once.
unless… there was another one scheduled in the meantime. So it changes the behavior slightly, and it might need some changes to the tests, but then it should satisfy the spec. The spec mentions that Forest Flash should collect and export the latest metrics, and the thing that is currently in progress here is… they might not be the latest metrics, right? They might be wrong.
Some time ago, which an export is still in progress, so once we await that and do another round of exporting.
we should be good.
It's mostly around the forest flush, which people are using to, flush their metrics in, like, fetch.
Pranav Sharma 00:22:42 Isn't there, like… I was looking at that again, so, isn't the current, behavior, like, if there's an ongoing export promise, it lets that promise finish, and then, it does the exporter.forceflush.
Marc Pichler (Dynatrace) 00:23:01 Doesn't that…
Pranav Sharma 00:23:02 suffice the thing? Like, on line 272 on that.
Marc Pichler (Dynatrace) 00:23:10 So, 272 is this one here, right? Yes, yes. So, yeah, so this does the export of force flush, but the spec actually mentions something like, should collect and export latest metrics. We can, Check that real quick, one second. Metrics, SDK, and then we have, First flush on the metric reader?
And it says, Forest should collect metrics split into batches if necessary, then call export on each batch, And then… And then force flush on the configured metric exporter, and just force flushing the metric exporter actually, Doesn't do the collection part.
Pranav Sharma 00:24:08 I see.
Marc Pichler (Dynatrace) 00:24:08 So, yeah.
I first, read the code, or last week I had read the code, and I was like, that looks good, and then I read it again today, and then I saw that it doesn't do that in case something is already in progress.
So I think that's the main thing that we still need, and then it should be good to…
Pranav Sharma 00:24:32 Okay, cool. I'll take a look at your comments. Thank you. Yeah.
Marc Pichler (Dynatrace) 00:24:37 Thanks for working on it. Sorry for the runaround here, but I've had so many situations with the metric readers and the processors in the other SDKs that, this change can be high impact, if… if it goes wrong. So… I just want to catch the things early.
And the second one is, just some performance thing in, like, very, very, very weird edge cases that hopefully should never happen. So you can ignore this if… If we think that it's… Not necessary to change, okay.
Pranav Sharma 00:25:19 Okay, I'll take a look. Thank you, Mara.
Marc Pichler (Dynatrace) 00:25:22 Yeah, thanks for working on that.
Alright, I'm moving on to Carlos, SDK logs review.
carlosalberto 00:25:36 Yeah, hello. Good on time because I got to drop in a few minutes. I can just briefly mention that I went and did a small pass, like, general pass on the review process for the SDK logs. It's looking great, there are just minor things that are mostly minor things, in my opinion.
We can probably discuss them. I didn't want to open issues for them, because probably they are… things that we can discuss, and maybe you can explain me, like, some things why this or that. The first one is that, And this is something, probably kind of… It's not very strict, but basically, in the specification, when you are creating a logger.
that should be done, hopefully, only through a logger provider. You shouldn't allow this to be created on itself.
So it's a huge, but I think it could be nice to go there. Then I also realized that TypeScript doesn't have any internal access modifier, maybe that's why, but yeah, that's one of the things, and we are fine.
Marc Pichler (Dynatrace) 00:26:38 Sure, Sorry, sorry to interrupt, but is there any way that we can create a logger right now via, Not via logup provider?
carlosalberto 00:26:48 A constructor is public, if I remember correctly.
Marc Pichler (Dynatrace) 00:26:52 Oh.
I thought that the logger class was not exported, from the package, so…
Trent Mick 00:27:00 Yeah, the logger class is not exported. The only… only place there's new logger is… it's… it's only accessible internally, or less… I mean, it's JavaScript, so it's only so limited, so you could cheat, but, we don't… we don't export the logger class, so… Right. So, currently, users of the SDK logs package can only get there via the logger provider, so I think we're good.
We had had that issue in the tracing SDK, was we did export span, and you could do new span, but we got rid of that over time, so… We learned the lesson, I think.
carlosalberto 00:27:31 Perfect. So in that case, that's done. The second one is that there's also a class called SDK log record, and this is what it could be known as, read-write log record. You already have the readable log record.
Just for your consideration, you know? To make it, like, like, more aligned with the specification, it's nothing, like, Of a requirement.
So that's just for your consideration. If not, we are fine. One of the interesting things, however, is that this SDK log record class, It's supposed to allow users to modify a lot of members, and a few members, they're… like, the timestamps, they are read-only. But we should be able to modify them. A funny thing is that I was checking the Java implementation, and the Java… they don't allow this to happen. So, they expose everything through getters and setters, so in theory, they could allow that in the future by adding more setters, but that's probably an important one, because, as I said before, only some of the members of SDK log record can be updated.
That's probably the biggest one. And the final one is just something very small that I saw, and of course, it doesn't matter. But a logger emit, when you're creating a logger.
A local record.
basically, it's, nothing will happen if its logger provider is already shut down, but some things are done on the side, and if I remember correctly, there's some metric being increased, you know, for this, even though you are doing nothing.
Just, it could be, like, a minor optimization, if you consider that, and for example, Java has… a shared state that log record, logger, provider, and logger can see, and when you are shutting the logger provider, then you just shut the rest. Sorry, you just… sets a global, Azure object, and this can be accessed by loggers. So, like, for example, when you're creating a train to emit something, nothing will happen there, you know?
Marc Pichler (Dynatrace) 00:29:36 Nope.
carlosalberto 00:29:38 So that's all. Other than that, I think it's fine, and I think…
Daniel Dyla (Dynatrace) 00:29:43 ne…
carlosalberto 00:29:44 Yeah, vocaust.
Daniel Dyla (Dynatrace) 00:29:45 Can you share which SDK log record, fields are not modifiable.
carlosalberto 00:29:53 Yeah, let me look for that.
Daniel Dyla (Dynatrace) 00:29:56 Because I'm looking right now, there's a couple of read-only things, like, you could… it's read-only attributes, for example, but there is a set attribute Method on it.
carlosalberto 00:30:07 Yeah, I can probably share my screen. Oh, wait. Can I share my screen for a second? Yeah.
Marc Pichler (Dynatrace) 00:30:12 I'll stop sharing for a bit, and then.
carlosalberto 00:30:17 Okay, let me share this for a second.
So this one, this is the SDK log record, and you can see that these fields are… Read only.
Daniel Dyla (Dynatrace) 00:30:34 So… okay.
which… which fields are… I guess, in the specification, does it specify which fields should be…
carlosalberto 00:30:44 timestamp.
Daniel Dyla (Dynatrace) 00:30:45 Beautiful.
carlosalberto 00:30:45 And Hispan context, at least, yeah.
Daniel Dyla (Dynatrace) 00:30:49 Okay.
carlosalberto 00:30:50 I put a link there, let me share… I think… oh, yeah, I did paste that, in the, in the doc.
there's, link to the specification. I'm reading that, it says timestamp, observed timestamp.
And the span context stop, which is trace ID span ID and trace flags.
Daniel Dyla (Dynatrace) 00:31:09 Got it. Okay, thank you.
carlosalberto 00:31:15 Yeah, other than that, yeah, I think we're fine, and if you want to ask for a formal review from the DC, probably Jack… Jack Berg, job maintainer, he was interested in doing a full review, but I think that… In my opinion, this is a good state.
Marc Pichler (Dynatrace) 00:31:31 Thank you. We should definitely create an issue from, what we discussed now, so that we don't… We'll get, and then also the side work.
Thing with the metrics is also something that we should fix before.
Yeah, thank you for looking into that and doing the preliminary review there.
carlosalberto 00:31:54 Alright, yeah, alright. Sorry, I have to jump to another call, so, thank you so much, and yeah, see you online. Ciao.
Marc Pichler (Dynatrace) 00:32:01 Thank you, see ya.
Alright, I'll share my screen again.
If I can find the right window to share from the 50,000 windows I have open, That looks correct. Alright, moving on to Hector's topic here, concert instrumentation, PR, and… OpenAI support responses.
Hector Hernandez 00:32:36 Yeah, these are pretty old PRs. First one, there was some discussion about the naming, browser, actually.
already published to NPM, and it's called, Browser Instrumentations Package. They include everything in there, so there's not going to be, like, conflict between browser console.
a Node.js console.
So, please take a look at this one. I suppose names should be fine.
And, Other one, the OpenAI. This is some PR that someone else created a while ago. This is to support Responses API.
The person said that he was not going to be able to continue with the PR, so I actually grabbed and started pushing to The… that person's branch.
I should be closer to be green, so…
Marc Pichler (Dynatrace) 00:33:26 This is…
Hector Hernandez 00:33:26 take a look at it. And apparently, OpenAI is getting… this instrumentation package is getting super popular, even if it's not super up-to-date. There's, like, 17 million downloads in MBM, so… I think it's perfect timing to make this in… to leave this in good shape.
So yeah, please take a look at it. It's just to bring it up to your attention. I will… if you add any comment, I will address it right away, so…
Marc Pichler (Dynatrace) 00:33:57 Yeah, thanks for, updating that PR and, bringing it over the finish line, also for the other one.
I will have a look at that one.
And… yeah. I think I had a brief look at this before, but I'll have another look, and… Then we can get this merged, hopefully. This one… I'm not too familiar with the OpenAI package, so I would appreciate if… Somebody who had looked into it before can take a look.
Any volunteers?
Trent Mick 00:34:40 Yes, technically, I'm a code owner, so… I should probably take a look.
Hector Hernandez 00:34:46 Thank you, Trent.
Marc Pichler (Dynatrace) 00:34:55 I will try to have a look as well at this one, if I find the time, but if somebody else gets to it first, I would very much appreciate it.
Trent Mick 00:35:06 So on the naming thing, you prefer, Hector, you prefer just console instead of console-node?
Hector Hernandez 00:35:13 I don't care. I don't really care.
Trent Mick 00:35:16 Is there node-specific stuff in there? Because Node's console isn't exactly the same as, like, browser console.
at MDN, er, documented.
Hector Hernandez 00:35:29 I think there's some Node.js thing. Yeah, I created this a while ago.
Yeah, it should be something… is there an import? Can you go to Instrumentation?
Marc Pichler (Dynatrace) 00:35:42 Yep.
There's probably nothing nodes specific, since we have the node types anyway.
Hector Hernandez 00:35:56 Yeah, we're just trying.
Marc Pichler (Dynatrace) 00:35:56 into.
Hector Hernandez 00:35:57 something global that is called console, right?
Marc Pichler (Dynatrace) 00:35:59 - I seem to remember there was, like, some small thing that was different to the… Browser version of the… Instrumentation.
But it looks like it could work.
On both sides.
Yeah, I guess we don't have to review it here, but I will have another look to see.
If there's anything different, I'm not… I think the name should be okay, We can rename it later if it's… Crossing.
Confusion.
Trent Mick 00:37:28 Okay, cool.
Marc Pichler (Dynatrace) 00:37:31 Right.
Looks like we are out of topics for today.
So… If anybody else has… Something you would like to talk about? Some smaller thing that popped up.
talk about this, or otherwise we can do bug triage and ER triage.
Let's do backtriage then, as always, if anything comes up.
Feel free to interrupt me, and then we can talk about, your topic. Maybe I will, just briefly mention something.
Just, Me too… Open something very quick.
So, some of you have probably noticed I just published This earlier, this… week, or last week, I think I did.
this has mostly been published, to be cautious. It probably won't affect anybody, but I just wanted to bring it up to your attention. There's… a vulnerability in the baggage propagator, and the CV for it has already been published. Oops, it actually shouldn't be public here. So, yeah.
If, you have any, things that use that old core package, consider updating.
Most of it should already be caught by this… Makes HTTP header size, thing, but if it's raised on services, it could cause issues. Other than that, it… Mostly shouldn't affect anybody.
But the new, version now applies limits on parse.
Or on extract, so… There shouldn't be any issues with the newer version.
Just so that everybody's aware. Wanted to bring that up.
Alright.
I guess we can move on to actually do bug triage here.
We don't have anything in the… Very poor.
And… Country repo also doesn't seem like anything new is here.
That's just… Check again if there's anything that's, Looking like a bug, but not reported as such.
Like, everything's fine here, and then… Your looks also fine, looks like nothing.
New here?
Before jumping into, PR review session.
Does anybody have any… issues, Maybe from the list here that you would like to talk about?
I would like to talk about this one, maybe.
This allows scripts.
and dev engines.
Where we're at the security topic, maybe, could be interesting.
I had looked into this, last week.
And I'm kind of in favor of doing that. To my understanding, it would just… Require us to… like, the allow scripts thing, would just require us to… Bump.
NPM to, like, that version, and I would be fine.
Doing that, since, it just affects development and not… like, what's happening, for users. I'm not sure if anybody has any ideas or thoughts on this.
Trent Mick 00:42:52 David, do you know if there's some things to copy for what Jared did in the browser repo? Like, they can… the browser repo can just say, hey.
everyone needs to use this minimum version of Node and NPM, so… they kind of did that. I'm not sure if we can do exactly the same, but… I think we can get started on… doing this. I haven't thought through what the implications are.
Marc Pichler (Dynatrace) 00:43:13 I actually haven't fully, thought through… thought through the implications, but I think, if we can… Do it in a way that we can still run the old tests.
In CI.
possibly also locally, even if we just have to npm install with a new version, and then switch back to an old node version to, actually run the tests, I think that's a… trade-off, that's okay. If it prevents Contributors, or, like, really anybody from… from getting hit with supply chain attack when they're just working on, stuff, then I think it's worthwhile to do it.
So… for the few cases where we actually have to use the old node version, I think there's… It's… An okay annoyance, to have.
To avoid larger problems.
Trent Mick 00:44:26 Was that Raphael volunteering?
Go for it.
Oh, no, that was something else, too, sorry, I just saw that.
Marc Pichler (Dynatrace) 00:44:34 Somebody else, yeah.
I think they had been looking at… Good first issues to pick up.
Trent Mick 00:44:42 Okay.
Marc Pichler (Dynatrace) 00:44:45 I'm not sure if this one is a good first issue. I would say that this is probably one of the more difficult… could be very easy, could be very difficult, depends on…
Trent Mick 00:44:55 Yeah, I think there's.
Marc Pichler (Dynatrace) 00:44:55 Well, it goes.
Right.
Other than that… Don't really have anything, so let's move on to PR triage.
We have 35… All requests into contract people, and 53 in core, so let's do core.
this time around.
I did actually try to go through and, see if I can merge or, like, review all the PRs that were, that had review requests in Slack.
So, I actually did pick off all the easy ones already.
I had been looking into… This one, it seems that, the person here is not working on this anymore. I assigned myself already, and I will push… The changes that were requested.
I am myself, and… Then, after… Today, I will… I will probably do that tomorrow, and then we can… get that PR merged. I will move this to the new SDK trace package instead of SDK Trace Base.
So that everything is in the correct place already there.
And this one here was blocked on some of the work I was doing.
Trent Mick 00:46:59 That one might be… like, things have changed there, so that one might be, updated.
David Luna Bistuer 00:47:04 I think that maybe we can close this one. The serialization, I think, is already, the university is already doing the same that the SPR is doing. I'll confirm, and then, I'll close it myself.
If you're okay with that.
Marc Pichler (Dynatrace) 00:47:18 Thank you.
Thanks for looking into that.
Alright.
Mind if I send this one to you?
David Luna Bistuer 00:47:31 Yeah.
Marc Pichler (Dynatrace) 00:47:31 David?
David Luna Bistuer 00:47:32 Go for it, go for it.
Thank you.
Marc Pichler (Dynatrace) 00:47:37 Thanks.
Tin… Moving on, as I've seen, there was some movement on this one here.
Trent Mick 00:47:57 I'd had that on my list to take a look at, too.
David Luna Bistuer 00:48:00 Yeah, he did, basically, he did the changes and removed… This period at the beginning was changing the tooling to use TSNOWN instead of TSC.
And also, changing the… the testing framework.
kind of a month ago, or even more. I asked if it was possible to keep the testing framework so the PR was, was, smaller.
And… and the slash changes, what he did, Jared, what he did was just to keep the testing frameworks as is, and now… and now it's only… the change is only about, the compilation.
So if you check, you will have… you will see that there is a lot of DS configs that are being removed.
Now we have tsun configs.
Instead of that, yeah. And then it… yeah.
The… maybe the… what could be more controversial would be the exports, but I think that he is trying to keep compatibility, so to not have any breaking change.
with that, Lucas got fooled me, but I think that the last comment that Jared did was.
He'd prefer to wait until… I think he's put a label here for the SDK 3.0.
So, so, I think he's fine.
Yes.
He's fine with, aligning this with the new SDK.
Marc Pichler (Dynatrace) 00:49:36 Awesome. I think, yeah, having… the PR just to do the migration to TSTOM is… Good step. We could still then look into changing the dev tooling, I think… I'm not too opposed to switch to what he had proposed before, but just having to change Do one thing is, he's good there.
Yeah, would be… would be great to actually have, like… functional ESM exports now.
David Luna Bistuer 00:50:16 It's the same tool that we are using in the browser repository, so… It's already, so we already… it's already tested there.
And I think that one of the options is that it's keeping… Tiesta and also have an option to not bundle things.
So, the compilation is the same, so each module is the TS file, gets, compiled to a JavaScript file, which, with the same name, so it has the same modules. So, we are not breaking, the current user's data.
that are using common.js, or… yeah.
Consuming.
Marc Pichler (Dynatrace) 00:50:51 Anyway.
Probably should be smaller than this way, right? Because we are just doing one ESM version.
Exactly.
Yeah, so… That's also good, yeah, moves towards smaller packages.
David Luna Bistuer 00:51:10 Exactly. So the build folder, it contains only MGIS files and CSGIS files.
And also the types, I think, that they are, in… yeah.
And yeah, so, yeah, I don't remember the extensions right now.
One thing to mention, though, is that in order to do that, taking the tools Requires a specific node version, So these, for testing… it's kind of using the same strategy that Contrib does, so it's using a specific version to compile.
And then, it tests with the node version that is set in the metrics.
Okay, if you check on… I think it's in unit tests, yeah, I think… Yeah, so you just see here it's using Node version 26 to compile, and then it's setting again.
To the version of the matrix to run the tests.
Marc Pichler (Dynatrace) 00:52:11 Sounds… sounds reasonable to me, I think. Huh.
Just compiling it with a different node version, and then testing it.
David Luna Bistuer 00:52:19 Huh.
Marc Pichler (Dynatrace) 00:52:20 as long as we can test stuff, we should be fine.
David Luna Bistuer 00:52:24 Yeah.
The drawback right now is that, we are using, it's using… if you check package log, the package JSON file is using NX to compile everything, instead of just… Using TSC with the… with the paths, with the refs.
At the beginning, we were just compiling around, remember? We were compiling… we were using TSC, and then we have the TSconfig.
That has, has a reference to each project, and was compiling all projects, to all projects at once.
Now it's compiling every package independently.
That takes more time.
But, like, contrib, then we can do, an improvement there. So we can use caching, and then we can compile just once, and then use the compilations results for testing.
But I suggested to have it this in a follow-up PR, maybe.
Marc Pichler (Dynatrace) 00:53:15 Yeah, I think having it in a follow-up PR makes sense, and if we then merge it for 3Doodle as well, we'll have some time to clean it up. I think it should be fine to have a follow-up there.
Okay. And also, we already see it, how it works in… in Contrip, so… should be… should be doable.
Don't just move stuff over here.
David Luna Bistuer 00:53:42 Okay, sorry, I guess…
Trent Mick 00:53:43 Is the understanding… so is the understanding that we're targeting 3.0 with this?
Or do we try to merge this to main before?
David Luna Bistuer 00:53:53 Check the comment from Jared. Maybe you get a different interpretation of that.
Trent Mick 00:53:59 Yeah, well, he said… so, reading Jared's things, to be clear, as much as I would like this merged as soon as possible, I think SK3… oh, okay, I misread that. I think the SK3.0 tag is appropriate here, because the breaking change from exports.
Okay. That means, potentially, him.
Or someone maintaining this PR for a while, and it's gonna have merge conflicts, like, all the time.
That's a pain.
David Luna Bistuer 00:54:24 No.
Trent Mick 00:54:27 Okay, I guess the only, yeah, the only alternatives are us saying, do bad exports, we don't consider breaking change.
Or adding exports.
field, or we do 3.0 sooner.
Which we didn't yet want to do, because we were pushing that towards September-ish, right?
Marc Pichler (Dynatrace) 00:54:47 Yeah, that's… that's the plan.
Trent Mick 00:54:51 Okay.
Marc Pichler (Dynatrace) 00:54:51 Or no.
I still have to create the issue, to announce that and everything.
Kecto, there's… Still some work to do.
Good at our setup.
I'm not sure if there's nobody from Sentry here today, alright?
Oh, looks like nobody's on the car.
I might reach out to, Andre, Jan.
To see if… they have changed their mind on the dropping of the versions, but otherwise we'll just push it out to September, I think.
Giving people some time to migrate is… It's not a bad thing.
Trent Mick 00:55:52 So, and we're thinking with September release, we'll drop 18 and 20?
Marc Pichler (Dynatrace) 00:55:57 I would… I would think so, yeah. So the reason to, drag it out a bit is so that we can drop 20. Yeah.
Trent Mick 00:56:07 Okay.
Marc Pichler (Dynatrace) 00:56:10 And then we'll have, native… native fetch, in all the node versions, and we can… Do a lot with that.
Alright.
So let's step here… I wonder if there's… Some smaller things that we could already start pulling in.
I'll look at that, at some other time.
Probably nothing to discuss here, but, like, the change in the build.
Like, compiling with a newer version, and some of the other things we might be able to… pick from that PR, and… Aren't using already, so that the change here becomes smaller, and there's less of a potential for conflicts.
But I think the main source of conflicts is gonna be… is here.
So I probably wouldn't have much.
Alright, another PR that is signed to me, that I didn't get to yet.
The gRPC export, the transport… Hong Song.
I wanted on this one, so… But that's still in progress.
volume.
And there's this draft PR, which I didn't get to yet. Entity resource prototype.
Then created… I'm actually not sure what the current status is for entities in the spec.
That might be something to… Look into in the future.
Not sure if there's any entity… Off going on right now.
I'll just look into that async.
Unless somebody has… Up-to-date entity info.
Right, been… This one here is allowing fetch.
Oh, I haven't looked at that one for a while. Send this to me.
And we'll have a look at this one async, because we're out of time.
Thank you, everybody, for joining.
Have a nice week, and see you next week.
Trent Mick 01:00:01 Excellent.
Jackson Weber 01:00:02 Yeah, I've been going off.
Hector Hernandez 01:00:04 Thank you.
