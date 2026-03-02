SIG: Android SIG
Date: 2025-08-26
Duration: 53 minutes
Zoom Recording URL: https://zoom.us/rec/share/VwnH3aVrwLGu6mHJrEcpuKuCU-lqJDLpjycr6FGYOXesxErjCS3xWqgRsxdE9zqH.RUYvpsx8SToLfXz8
============================================================

## Zoom Recording Transcript

**Jason Plumb** 00:20 Good morning.
**Hanson Ho** 00:21 Hello?
**Jason Plumb** 00:24 How goes?
**Hanson Ho** 00:26 Ugh, trying to catch up, I was away for…
about a week, and then I came back, and just have to keep catching up.
I think I'm still behind on all the… Reviews and comments.
Has, … … never mind, I'll share that. I'll talk to you after.
**Jason Plumb** 00:47 Okay.
**Hanson Ho** 00:52 Hey, Manuel!
**Manoel** 00:53 Hello, hello, long time you'll see.
**Hanson Ho** 00:55 Yeah, I was just gonna say!
**Manoel** 00:58 Yes, over in Europe, you know, EU is a bit longer than the rest of the world.
**Hanson Ho** 01:05 Hello. This is her.
**Jason Plumb** 01:06 Very true. Very true.
Not bad.
I'm pulling up the thing, I'm just struggling to use my hands, apparently.
Brain not working yet. Okay, there's the meeting notes.
Cool.
That looks right.
Look at this, says, alright, I already had your tab open, like, somehow I didn't even look at the agenda, and I knew that this topic was gonna come up.
Actually, I started reviewing it, but I don't think I've made any comments yet.
**Cesar Munoz** 01:59 Okay, well… Yeah, that's all I wanted to do here, actually, just to… Bring attention to it.
Cool. It looks huge. I just wanted to emphasize that note that I… I deleted 25…
Files for… from the old implementation, and…
Those add up into that number, and files change, but it's just remove files, so…
Still, it seems like Greg… Gregor…
would like to get it, smaller, so I asked a question.
Let's see what… What we could do.
**Jason Plumb** 02:39 Yeah, I mean.
**Cesar Munoz** 02:40 ….
**Jason Plumb** 02:40 Not that bad, though. Maybe we can talk him down from this. I don't think it's that big.
**Cesar Munoz** 02:46 I mean, the number is big, so that's why I know it might be….
**Jason Plumb** 02:49 Yeah.
**Cesar Munoz** 02:50 a bit scary.
So yeah, anyway.
**Hanson Ho** 02:53 do you have enough test cases to cover? Because, generally, it's going to be hard to find, you know, issues and reviews anyways, so if you have enough test cases to cover afterwards that things should work as they do, then that's…
you know, I think that's better than splitting up reviews, especially when you're doing a migration like this. It may be trickier to kind of pull things apart, simply for readability.
**Cesar Munoz** 03:21 Yeah, I actually had to touch a lot of tests,
Update them and all the stuff, so… so those also add to the…
amount of files change here, so it's…
Yeah, if you're interested, at least in an overall test, there's one called… Is it integration?
functional? I don't know, I think it's integration. Test.
Where it's like the old… Usage of the new… API…
Like, in a… in a… in its final form. It's not like…
If you want to see it all working.
**Jason Plumb** 04:01 And that was not touched in the PR?
**Cesar Munoz** 04:04 Yeah, it was, yeah, and there it is, integration test.
**Jason Plumb** 04:09 This one.
**Cesar Munoz** 04:11 Yeah.
**Jason Plumb** 04:13 Do… you know why it's gray, this icon?
**Hanson Ho** 04:17 What is this?
**Cesar Munoz** 04:18 I think that means it's changed.
It's the new….
**Jason Plumb** 04:22 That's all that means.
**Cesar Munoz** 04:23 It's just stuff.
**Jason Plumb** 04:24 I feel like… I feel like visually it's different in my brain somehow, but….
**Cesar Munoz** 04:28 It has changed. I think it's been a lot.
**Hanson Ho** 04:30 They changed the icon, I guess, yeah.
**Jason Plumb** 04:32 Is it gray for you as well?
**Hanson Ho** 04:34 Yes.
**Jason Plumb** 04:35 Okay, so it's not, like, a settings thing.
It's like a GitHub thing.
**Cesar Munoz** 04:39 But I… I don't remember what was previously, probably yellow or something, but yeah.
**Hanson Ho** 04:45 Yeah, it was yellow.
**Jason Plumb** 04:47 Okay.
That's cool. …
I had two thoughts when I was reading your description, and I'll try and set aside time to go through this, but …
It might be helpful.
to know if you're going to try and split it up. I don't know how.
But… ….
**Cesar Munoz** 05:08 I can duplicate a lot of code so that, you know, the old code that I need is changed, but I still.
**Jason Plumb** 05:14 Yeah.
**Cesar Munoz** 05:15 remove the files so that they didn't add up. I don't know.
Could be a bit clumsy.
Yeah, you can also see the usage here in the description.
**Jason Plumb** 05:24 Do you have to change the reading and the writing side at the same time in a PR? Like, could you do just the reading side and then just the writing side?
Or are those coupled.
**Cesar Munoz** 05:36 …
I changed so many files.
**Jason Plumb** 05:43 Yeah, I don't wanna… I don't wanna….
**Cesar Munoz** 05:45 Oh, really?
**Jason Plumb** 05:45 25.
**Cesar Munoz** 05:45 I probably cooled. I probably cooled, to be honest. Maybe, I mean, if…
I mean, have a look. If you think it's quite vague, I can, I can… Try to split it.
Yeah.
**Jason Plumb** 05:59 Cool. I think… so my initial thought, and this is… this is, again, just… I'm just thinking out loud here, and this is not a criticism of the approach or the design.
I was thinking, as a user who was coming into this, for the first time, if I saw this.
I might think it was more complicated than I wanted.
I'm imagining a user who's just, like.
I want to buffer to disk, I want to tell it what directory to use, and kind of, like.
how much maximum to use, and maybe, like, maybe some sane defaults, but, like, maybe I can adjust the period if I want. And just have it, like, conceptually, one exporter that does this implicitly, right?
And we've… we've got a… in here, it's, like, broken out by signal, which I think makes a lot of sense.
But I think there's maybe room to put another layer on top of this that hides some of that signal
I mean, it's stupid because our exporters are tied to a signal type, like, it's literally the interface of exporters, like, it's a per-signal type thing, so I guess you do maybe have to do it this way.
But I was just thinking, of a user coming… I was trying to put myself in the mindset of a user seeing this for the first time. And then, on the reading side, my other thought was that… I guess you have the network exporter.
That's the thing that's gonna send on the wire. Okay, so you just iterate what's in storage, and then you export it. So this is kind of signal-free, though, right? Like, this kind of doesn't…
Coupled to a specific signal type?
**Cesar Munoz** 07:36 It does, yeah. There's….
**Jason Plumb** 07:38 Yes.
**Cesar Munoz** 07:38 urge.
**Jason Plumb** 07:39 Okay, span, span sword, okay, that's what I missed.
**Cesar Munoz** 07:42 Which is the one that's definable.
**Jason Plumb** 07:43 Okay, yep, and so you'd want to do… you'd have 3 of these, one for each type.
**Cesar Munoz** 07:48 Yeah. The thing is that… If I understand correctly.
You're trying to find a, like, a…
Single place where people can get all the signal-related stuff.
Maybe we can create a kind of, kind of like a manager or something?
**Jason Plumb** 08:04 Yeah.
**Cesar Munoz** 08:06 But, but we… At the end of the day, we still need
The tree signals to be treated, separately, because that's how the core also treats them, so….
**Jason Plumb** 08:17 Yeah.
**Cesar Munoz** 08:17 Yeah, we can make it prettier with something… On top of this, yeah.
**Jason Plumb** 08:23 No, this is cool, I think it's a good improvement, though. I'm looking forward to it.
**Cesar Munoz** 08:28 Thank you.
**Jason Plumb** 08:29 Yeah.
**Hanson Ho** 08:29 I'll take a look at today and add some comments, but yeah, definitely, if we could have a one-line thing, basically initialization with all the… all the defaults that you'd want.
I think that's good enough.
**Jason Plumb** 08:44 Cool.
**cleverchuk** 08:45 Yeah, I think, making a facet would be good, like, if you just get, like, a file name, I can, like.
Perfect, suffice them with the spans.
For each of those, then create the rest of them.
**Cesar Munoz** 09:00 Yeah, they….
**Jason Plumb** 09:02 Good luck at everything for work.
**Cesar Munoz** 09:04 4?
The prefix is for what, sorry?
**cleverchuk** 09:12 for the file names, so… They give you a file name, then you say, this… Dash, Spanish, dash…
Metrics, dispatch, logs.
And then there'll be different files. It'll just be, like, creating the… yeah, these other stuff would just be hidden.
**Cesar Munoz** 09:31 Got it.
**Jason Plumb** 09:32 Yeah, if they could share a storage, I think is what Cleverchuck is saying, and then the signal type would be determined by the file name within that directory, or within that storage.
**Cesar Munoz** 09:43 It is, it is possible.
To be honest, it's just easier with a single… a dedicated folder, because
Also, part of the… probably faster in terms of performance, because part of the work that's done on every write is to check
The amount of files already there, and how much they take from disk, and then compare it to the configuration that you provided as what's the maximum amount of
size that you want to take from this, for this specific synonym.
So, it will be possible, but then, you know, I have to create some sort of rejects pattern to find the specific amount of
Size that's taken by each signal.
**cleverchuk** 10:24 Well, the storages can still be, like, different.
The thing is just, you're creating…
you're creating them underneath something else. You only get the file name from them, you can just…
Everything else can, like, be abstracted. Like, using, like, a facade or something to hide it.
**Cesar Munoz** 10:45 But the bylamp is also… it's also used because it's the timestamp. Yeah, so it gets pretty complicated.
**Jason Plumb** 10:53 Yeah. I mean….
**Cesar Munoz** 10:55 I don't think it should be a big deal to create.
3 sub-tiers, like this.
**Hanson Ho** 11:01 It's… it's… it's a…
Unix files and directories are, you know, it's just a path, so it doesn't really matter. I think the configuration part is the more important one, so what folks have to actually specify when they use this. And if we get that, I think, solid, everything else is just implementation details. No one's gonna go in there and muck in, you know, the directory and do all that stuff. Having an easily addressable one is
Nice.
**Cesar Munoz** 11:28 Yeah. Oh, but what about the way, one of the changes that I think this enables, too, is that now you can pass a different configuration per signal.
Just in case you wanted to have something like, I don't know, I want to have a limit of 10 megabytes per spans, but then only 5 for the other signals, something like that.
**Jason Plumb** 11:45 Yep.
**Cesar Munoz** 11:46 I think it was not possible, so now you can pass the configuration after the file, which is optional, because by default, you get
Default graphics for all of them.
**Jason Plumb** 11:58 Cool.
**Manoel** 12:01 Well, that was it.
**Cesar Munoz** 12:02 Thank you.
**Jason Plumb** 12:04 Nice.
Well, this is Vague, Hansen.
**Hanson Ho** 12:09 Yeah, well, I saw, I saw a discussion on… on what happens during a crash, from last week that I wasn't here for. I know Jamie did a, PR that converts the crash, excuse me.
instrumentation. And I also have this, crash semantic convention thing outstanding for a while, so I kind of want to talk about the state of the crashes, and how we want to kind of go forward, improve, given that there are moving parts right now. So that's what I call crash stuff. I want to figure out,
if there's a desire to improve, what happens during a crash in terms of what's being recorded and lost, as well as discuss some of the ongoing work. The ongoing work is probably more, you know, a quicker discussion, in that, I think the implementation change is good. I think the
semantic conventions will go ahead once I find some time, but more to the question that might have been discussed last week already, is there a desire to improve, what happens, during a crash?
Or someone just pointed out that, hey, what happens? Other than we log a crash.
**Cesar Munoz** 13:22 In terms of improvement, you mean, a general improvement? Because I know one thing that Jamie mentioned there.
Which makes a lot of sense, which is to try to, trim the stack traces after
You know, pass some, some sort of size.
Is that kind of improvement that you're talking about, or is it more something more specific?
**Hanson Ho** 13:46 Something more specific. So, current behavior has crash-generated, so, basically, so…
two things. The instrumentation, I haven't taken a look in that detail. Jamie probably looked at it in more detail, so the things that he brought up, probably about, like, you know, truncating the number of frames that we actually send and all that stuff is probably reasonable. I… I am specifically more talking about, I think… I think what was… was discussed last week, where,
what happens, when a crash happens with regard to the session? So long-running spans, you know.
other things. …
Was there an issue that was logged to say, hey, let's improve how we handle this, or is this just brought up as a discussion point about what we can do?
**Jason Plumb** 14:35 Yeah, so I'd encourage you to go back and watch the recording, from last week to get caught up on it, but I think this was Fallout from Leo. Like, I think it was just, like, a continuation of this. So I think they… I think that they were hoping to model, or attempting to model,
portions of the session, like, groups of user behavior as a long-running span, and there's… there's lots of complexity, as you know, that come out of that approach, and one of those is, what the hell do you do with that activity when the app crashes? And there's no… there's currently, like, not really any great way…
To shut that stuff down, ensure it's flushed, and clean up nicely.
And I think… keep me honest, the rest of you please, but I think that that's where this discussion kind of came from, is like, if we have these, like, long-earning activities that were kind of… I'm using activity, I know it's an overloaded term, these user groupings of…
business functionality in an application. If they're using a span to sort of capture that, because they want stuff parented in it, then what do you do when it crashes?
Sounds good.
**Cesar Munoz** 15:41 bits.
**Jason Plumb** 15:42 Mostly where this came from.
**Cesar Munoz** 15:44 Back to you.
It may… I think it's… I remember mostly the same that you just mentioned, Jason. The one topic that I…
And I think we kind of answered a lot of these questions.
in the call, but there was one which I think we were still not sure, which was what happens when… so, we realized there.
Well, we confirmed there that The session is attached to a span on its creation.
Which is fine. But I think that the one outstanding question was, what happens when there's a parent span that was created when… during a session.
And then…
It's a very long span, so at some point it gets a child span that's created after the session changed, then, you know, what session… you know, these two spans, which are related, will have different sessions.
But I think… Yeah, I think that was the only question that I didn't have clear enough.
Yep. So… Yep.
But it kind of… it's also kind of an edge case, though.
**Hanson Ho** 16:54 Yes and no. I think by definition, the session related to a span is simply the session that it was created
in. So, a trace having different… a trace with different spans having different sessions is perfectly reasonable.
Given that the span doesn't belong to a session, it is merely associated with it. So, this is why the parent-child relationship is a bit tricky, which is why span links are great when you want to find relationships like that. So, I think if we just clarified what
session ID means, then that goes a long way into actually
clarifying that part. And if we do want additional metadata to associate, concurrent
sessions and spans, we can always add additional, IDs or span links, to it. So, right now, if the canonical session ID attribute defines the session, that the span was started in, span links can be created, or other metadata, I should say, like, attributes could be used to associate, these things.
So I think it's about, what we want to do in terms of how thorough the relationships we want to describe are. And if that's the case, then it's just about defining
that semantic convention, and then implementing it. The issue with.
**Cesar Munoz** 18:24 document sessions.
Yeah. This monthly commission? Our own session, okay.
**Hanson Ho** 18:29 Yeah, because I think… I think it's pretty simplistic right now, the way it is. And it could be… we could improve on,
how we work with it, in terms of, if we want to associate data with it, if we want to, you know, do different fancy things. So it's, it's…
There are, there are approaches, …
And, it's just a… we've got to figure out what we want to do, and what right now is missing. …
So, modeling it, I think, between the objects, between signals is probably the easy part. I think the harder part is doing what… that whole thing, what happens when it crashes, because effectively, what you would have to do is, is, …
snapshot, every once in a while, the state of the current running spans. And then, if there's a crash, you resurrect what is, you know, in that, snapshot. And of course, those snapshots have to be persisted and all that stuff. So you wouldn't get, like, the latest down to the millisecond, of, of the state of things when the crash happened, but you can get an approximation.
The problem with OTEL is a span doesn't exist until it's done. So you kind of have to work around it, you know, in order to know the state.
during the running. So, Embrace handles this by doing span snapshots, and then persisting the snapshots, every couple seconds. And then on the next time we, we, awake, when the SK starts up, we look for these tombstones.
And then if one exists, we basically do what we do, to, create the telemetry from the old data, making sure the resources and all that stuff is what it was before, and then send it over. So it's, it's, we call it resurrection. I call it resurrection. But it's, it's, it's, it's one of those things that is…
is useful, … But it's… it's… it's involved.
**Cesar Munoz** 20:32 Got it. It's to preserve the ACE information about the… on…
the… the spans that… that couldn't get closed before the crash happened, basically, that's… show them as a… you create… you create new spans, or… or… or is it like a log? There were these spans that didn't finish.
**Hanson Ho** 20:55 Yeah, so basically, a span that is started, but is not done, will never be exported. So if the app crashes, that span is effectively gone. What we do is we basically take an in-memory snapshot of the ongoing spans, basically keeping the memory repository of what's going on, with the current state and all that stuff.
In a file. And then if, we… if the session ends, or, you know, whenever we decide to flush something, we get rid of those tombstones. So if we find a tombstone and we start an app, it means that, the previous process was
killed at a time before we can actually close something off. And we take a look at what those are, we take a look at when the last crash time happens, or whatever, and we kinda, kinda, …
You know, fix the data that was captured in memory, and then re-log a span to make sure it gets exported, to represent what it was, you know, at the time of crash, or approximate what it was at the time of the crash.
As close as we can.
**Cesar Munoz** 22:01 So….
**Hanson Ho** 22:06 It only works if your backend is configured to handle,
data coming… telemetry coming in that's fairly late. Like, if you're one of those ones that, you know, hold the session open for 5 minutes, and then basically anything after that, it's ignored, then that's not useful. So, it depends on how the data is used, whether that's useful or not.
**Cesar Munoz** 22:29 Now that we're discussing about this, it occurs to me that it seems like session has kind of been, like, like, like the elephant in the room, always, for a long time, not only for Android.
Or lion's stuff.
And, … it looks like…
if what you're saying is that we need to have a better definition, I think that… that… that… that… that… that's a great start. But, ….
**Hanson Ho** 22:58 It's on the list! We have a stub page now, and I have half a draft.
**Jason Plumb** 23:05 It's on the website, right?
**Cesar Munoz** 23:08 I remember you created a draft, Anson, or… I don't remember if it was only in Slack, or if it was a PR.
**Hanson Ho** 23:16 It's on a Google Doc from over a year ago. I was looking for a place to put it, and now, you know, we have the stubs on the website that we're waiting for,
the metrics recommendation from, from, from Santosh, …
But, the idea is that we can start putting stuff like definition of sessions and stuff in there, and…
It's on the list.
**Jason Plumb** 23:44 Yeah, it was in here, right? Yeah, this is the… I'll just link to it from here.
**Hanson Ho** 23:58 I think I got the go-ahead, internally at Embrace, to get folks, get some of our, Doc and DevRel folks to start adding some stuff, to here. So hopefully we could, get some basic stuff in here, at least generate discussions to see if folks are still….
**Jason Plumb** 24:17 Yeah, yeah, yeah, so I think, I think over in…
No, I think it's in specification.
There is this PR that Santosh… we don't have Klein Sig this week, right? It was last week?
**Hanson Ho** 24:30 It was last week, yeah.
**Jason Plumb** 24:31 I missed it. … … Okay.
I think that's his thing.
**Hanson Ho** 24:40 I think it was closed because we talked about,
**Jason Plumb** 24:48 Isn't that his handle?
**Hanson Ho** 24:51 It's… So, to the C….
**Jason Plumb** 24:54 I thought it did.
**Hanson Ho** 24:55 Yeah.
Yeah, something like that.
**Jason Plumb** 25:00 It's like, maybe there's an….
**Hanson Ho** 25:02 No, that's, that's… Oh! Oh!
**Jason Plumb** 25:04 Is that right?
**Hanson Ho** 25:06 No, … it must be. Yeah, Santos Cell… yeah, yeah, that makes sense. Yep.
**Jason Plumb** 25:13 But… Wasn't there something about metrics? This is the thing I'm trying to find, this metrics one.
**Hanson Ho** 25:19 Yes.
**Jason Plumb** 25:21 But I don't see it in here. Is this the right person?
**Hanson Ho** 25:26 He might have, like, two different… oh, I think this is not, because that last one, the newest one is 2023, so….
**Jason Plumb** 25:35 Maybe it's… maybe I'm… maybe it should… maybe it's in the semantic conventions?
Sometimes I….
**Hanson Ho** 25:41 Here's a different account, … I'll take a look.
Whoops, -oh.
**Jason Plumb** 25:48 You think there's a different one?
Oh, and it was not a PR, it was an issue, I think that's the whole thing.
**Hanson Ho** 25:56 Okay, okay.
**Jason Plumb** 25:58 I think it's an issue.
**Hanson Ho** 26:00 Wait, I thought, I thought I saw, like, a diff, whatever.
**Jason Plumb** 26:10 This one, yeah, this one, okay. So….
**Hanson Ho** 26:14 Okay.
Oh yeah, it was just written in the issue itself, okay.
**Jason Plumb** 26:19 Yeah, yeah, I wanted to bring that one up because, …
you know, this was… this was something that we had talked about, and we're like, well, no one liked the idea, apparently, of it going in the spec. There was a lot of pushback on them. It's like, no, we don't want this in the spec.
And…
Then, you know, there was like, well, we talked about it, maybe we'll just do it in the website.
Which I think there was some… some rallying about that, and I think that's where this one ended up.
**Hanson Ho** 26:48 Yep. And I got a… I got a downvote from, ….
**Jason Plumb** 26:51 Yeah, I saw that. I mean, this person, I think, is gonna downvote a lot of things.
**Hanson Ho** 26:56 Interesting, yeah.
**Jason Plumb** 26:57 Yeah. I think this person really likes the idea of using metrics on mobile, and I don't know that they have fully thought it through, but they've been pushing really hard on this topic, and so…
Yeah, maybe they're going to.
**Hanson Ho** 27:11 Good luck finding a collector, take that.
Oh, my God.
**Jason Plumb** 27:15 Anyway, like, so we do have these stubs out here, and we can start to… to flesh some of this out.
And we can put some of the guidance, you know, at the client-side level, because it's very, very simple right now.
**Hanson Ho** 27:29 Oh yeah, I was waiting for, well, I mean, I was gonna do something, and then…
bit Santosh put it on top of that, I was like, I may not get to it, so I'm getting him to do it first, and then….
**Jason Plumb** 27:38 Yeah.
**Hanson Ho** 27:38 We're both busy, I suppose, so….
**Jason Plumb** 27:40 I mean, this hasn't really had much traction in a while, but what is this one?
Somebody mention this one?
I'm not even looking at this in this meeting. Okay. What else?
Oh, I… I wanted to… so I… Go ahead.
**Cesar Munoz** 28:00 That's just one thing that I thought it was interesting about sessions last week was that, …
it looks like… if I remember correctly, this person, they were trying to use Jaeger.
for… for…
this… to see the spans. And, I think the idea that they wanted to have a, like, a big span
for everything was so that Jaeger would show it properly.
And I think that's… Probably gonna be a… quite a big, … …
I don't know, pain point for users to get used to sessions.
Because, what we discussed was that usually, at least open source EOIs.
are not prepared for that later on. It would be really cool if you could see spans and logs related to a session in a single place, but…
That's not the case, so….
**Jason Plumb** 28:58 There's no RUM UI. There's basically no open source RUM UI, is what it is, yeah.
**Hanson Ho** 29:04 people try to slap this stuff on… try to model this as a distributed trace, and it's just not. It's a bunch of, like, semi-related, concurrent kind of thing. It kind of sort of works if you model a certain way, but it's very limited, especially when you get out to the, to the edger cases. It kind of works if you just throw it up on there, but…
it starts to break down quite easily. But yeah, I think that is something that's completely missing, is a way to visualize, RUM, and client performance, stuff. We….
**Jason Plumb** 29:39 We even have that same problem with our own demo app, like, you have to run Docker ComposeUp, and it brings up Jaeger, and it brings up the collector.
And in the demo project, they use OpenSearch for logs, so it's like you have these, like, possibly, like, two or three different tools to go look for your data in, and there's nothing that pulls these together into, like, a cohesive RUM UI, or a session-based UI.
**Hanson Ho** 30:05 So that's what I'm trying to… that's what I'm trying to work on. … Yeah. Yup.
**Jason Plumb** 30:11 I wanted to make sure that people know where to go see these recordings. Have you ever looked at these recordings? I mean, it's not the most exciting thing to watch a recording of a SIG meeting, but if you go to the community repo.
I think you can look for, recording, and I think this is the link.
Cool. Yeah, so the history of this, this is, like, it's pretty hard to look at this, but…
The history of this is that the recordings used to auto-publish to YouTube.
And I think it was about 2 years ago.
I think the governance committee decided to pull that because there was a lot of…
and I'm sure there still is, but there was a lot of concern back then about AI scraping YouTube for video content, and possibly training models on individual people, and when you're contributing to open source, if you're giving an hour's worth of your visage and your voice.
Every… every week.
then that, you know, it's a liability, is really what, sadly, what that's come to be, and so they put those down. You can still get to them, though, and, like, if you wanted to see the Android one, I think you can just look for Android.
**Hanson Ho** 31:19 Sweet.
I mean, I say I'll take a look, I probably won't, but, eventually….
**Jason Plumb** 31:24 Eventually.
**Hanson Ho** 31:24 Will.
**Jason Plumb** 31:25 I think the old ones fall off, let's see….
**Cesar Munoz** 31:30 Oh, there is, there is one.
**Jason Plumb** 31:31 Yeah, so if we go down to, like.
This is probably last week. There we go.
**Hanson Ho** 31:37 Nice.
**Jason Plumb** 31:38 What the hell is this column? The minutes? The duration, maybe?
**Cesar Munoz** 31:41 Wow.
**Jason Plumb** 31:42 What that is… I gotta scroll back up.
**Hanson Ho** 31:45 s….
**Jason Plumb** 31:46 Reasonable. Yeah, okay.
So that's what that is. Anyway, that's how you can find this stuff, and then I think…
I think the password's even in the link, yeah, no password or it's in the link, yeah.
There you go. So, that's how to find those. It's from the community page. Just look for the word recordings. It's, …
This could actually… this README could use some love, because the… the only mention of recordings here…
is under Governing Bodies, that's where the link to the thing is. And it doesn't… like, in the SIG list, it doesn't talk about there being recordings. And maybe that's… maybe that's intentional, but it's not obvious if you were just reading this section.
So maybe that's feedback.
**Hanson Ho** 32:34 We can certainly put it at the top of our document. Just create a link to the spec sheet or something like that.
**Jason Plumb** 32:41 Yeah, we could do that.
Now that I've closed it.
Let's see here…
Cool, that's a good idea. And then, …
They do roll off, I'm not sure, because it looks like…
there's, like, 15 months or something, and… or maybe that's when this started, I don't know. Whatever.
The other thing I thought was fun to mention, maybe, is something I called out in the channel, but maybe not everyone saw this.
Is, that part of our release process goes in and updates the versions of all of… in the documentation.
So it's… the implementation is not sophisticated, but what's cool is that after we do a release, like, we're at 0.14 now, you can come into any of our instrumentations.
And…
Look at here, and there is, like, how to install it, and it's, like, it has the version in here.
**Hanson Ho** 33:51 Oh, nice.
**Jason Plumb** 33:52 Is this wrong, though?
Did I just… did I… yep, it's wrong.
So, for some reason….
**Cesar Munoz** 33:58 Did we commit the PR? The PR had the right… yeah, was it merged? Yeah. And now it was merged to the release… release, branch.
**Jason Plumb** 34:07 Okay, yeah, yeah. Okay, so….
**Hanson Ho** 34:10 Okay, we….
**Jason Plumb** 34:11 Hmm, so the same thing should happen. There's another PR, so this is 1178.
There should be one right next to 1178, so it's either one before or one after.
Yeah, so here…
I'm glad we're talking about this. Okay, so this is lacking. So this one should do the same thing that's happening in the release branch, but with the current snapshot, right? So, when you go to, just the main branch, we should either have 15 snapshot, or we should have 14, and I think probably 14.
But… Okay.
So, I'm glad we're talking about it. There's a bug… there's a bug here, so there… this is actually a problem.
**Cesar Munoz** 34:55 But I think that the… complicated part, it's… it's done in that PR.
**Jason Plumb** 35:00 Yeah, we can just copy that word. Yeah, for sure. I'll take that as an action item.
I just, I like the release automation, it's really helpful when the time comes to push the buttons and to have it just happen, is really nice. And I thought that was happening, and I was excited about it, and…
Still some work to do, it turns out, okay.
**Cesar Munoz** 35:21 But I get you, it's… I love automating stuff.
I mean….
**Hanson Ho** 35:30 Sure, beats a checklist.
**Jason Plumb** 35:34 What do you mean?
**Hanson Ho** 35:35 Oh, so things I can't automate, I have a checklist that I have to go through, and some of them are like, fuck, we're about to do this for me, kind of thing.
**Jason Plumb** 35:43 I mean, you've seen that we have that too, right?
**Hanson Ho** 35:46 Yeah, yeah.
**Jason Plumb** 35:46 Yeah, I mean, this is… this is basically our checklist. Yeah.
Dude, the one for core is so long.
No, it's just called Java.
**Hanson Ho** 35:58 Chat, yeah.
**Jason Plumb** 36:00 Look at this thing, it's like, there's a lot in here. And it's not all… I mean, there's… whatever, it's not all just the release stuff, but…
It's kind of a lot of steps. …
Cool, so yeah, I will take that as an action item to go fix that, …
Is there one… oh, I thought there was one other thing. Oh yeah, …
Please have a look at the Jenk pull request.
If you haven't yet….
**Hanson Ho** 36:26 Hmm.
**Jason Plumb** 36:27 And that is because, this got merged.
So we at least have the very basic, minimal, jank definition in SEMconf.
**Hanson Ho** 36:39 Sweet.
**Jason Plumb** 36:40 And this is the prototype slash implementation of it. And I tried to… I tried to keep… …
the existing span-based one in there for one release, and then we can depra- like, it's deprecated, we should, like, remove it in a release. It's a little bit of overkill because none of this is stable, but I'm just trying to be nice to people that are migrating. If they're using the existing one, that gives them a version to hopefully adjust to that.
So, Cleverchuck, thank you for looking at that. I appreciate it. These other approvers, take a look.
**Cesar Munoz** 37:15 I'll take a look, first thing tomorrow.
**Jason Plumb** 37:19 And I… I'm torn on this one. I mean, this… you make a good point here. Yeah, probably.
I think, you know, you're probably right. I didn't know.
Is it a reporter of jank events?
It kind of is, that's kind of… I… It's unpacked, but…
Yeah, I don't think it… yeah.
**Hanson Ho** 37:40 it's not a spans exporter, right? So….
**Jason Plumb** 37:44 exact.
**cleverchuk** 37:47 I mean, it's a knit, it's fine.
**Hanson Ho** 37:50 No, no, it should… I believe in naming conventions like this.
**Jason Plumb** 37:54 Yeah, it's important.
**Hanson Ho** 37:57 It's easy, right? It's not like we're debating colors, it's either one or the other.
**Jason Plumb** 38:04 Was there anything else exciting in here? So this one, we should probably just merge this, right? Do you know if Jamie's gonna come back? There's a couple of… couple of threads that I think were not resolved, but….
**Hanson Ho** 38:15 He's been out… he's been out for a week, so he's back later this week, so he's away from… he'll… he'll come in and, I think the reason why it's not a data class… he'll… he'll come and explain it, but yeah, I'll try to do that, maybe, but we can wait. I think it's okay.
**Jason Plumb** 38:29 There's no rush, right? It's fine. Okay. I just get… I get a little bit twitchy about this list getting too long, because it's really easy to let that get very long.
Cool. And then, are there any new issues?
**Cesar Munoz** 38:41 By the way, just wanted to mention that Jamie has helped us a lot.
Oh, yeah. In a very short period of time. So, so… You know, kudos to him.
He's good.
**Hanson Ho** 38:54 He's very….
**Cesar Munoz** 38:55 Italy will be back.
That's so important.
**Jason Plumb** 38:59 Oh yeah, the other thing I wanted to, mention was this discussion that was happening over in one of the Java core issues about…
… strict mode that Cesar was brought into.
Let me find this real quick.
**Hanson Ho** 39:19 We need to just weight it up, …
you do need to do a disk read on startup, unfortunately, and that's gonna violate strict mode. ….
**Cesar Munoz** 39:27 This one is related to, Java SPI loading, which does….
**Jason Plumb** 39:34 Yeah.
**Cesar Munoz** 39:34 This rating under the hood.
**Hanson Ho** 39:37 Go?
**Cesar Munoz** 39:40 Some people, it seems like they're claiming that Probably in all devices.
This, this read might be causing A&Rs?
I'm not sure.
**Hanson Ho** 39:53 I will comment on this. This read will not take 5 seconds, but this read can potentially take a couple hundred milliseconds.
**Jason Plumb** 40:02 And so, I mean, there's a good discussion already happening in here. I think Cesar did a good job of describing that, like, this is a dev function, and there is stuff that needs to happen. This, however, I think is the workaround. You can just set this system property.
**Hanson Ho** 40:19 Yeah.
**Jason Plumb** 40:20 then the SDK doesn't have to go find the contact storage provider, it just… it has it, right? And…
So hopefully they will circle back on this, but this got me wondering about other strict mode violations, and I will see if I still have this… I don't… I may not still have it open, but let's see if I do.
Okay, let's just do this. I'm gonna… I'm gonna reshare, since we have a little bit of time, if that's fine with folks.
**Hanson Ho** 40:45 Yep.
**Jason Plumb** 40:46 Alright.
**Cesar Munoz** 40:47 Yeah, bye.
**Jason Plumb** 40:50 this thing.
Okay, so this is just the tip of main, I'm running the Android demo, let's just… tank the…
Oops.
Ugh.
Right, so… I think I've already removed it at my local, but let's do a… Local history…
Yeah, here we go, let's grab this… Alright, gotta import it.
Let's run this.
**Hanson Ho** 41:31 we do a discrete to find a bunch of stuff when the SDK starts up, so it….
**Jason Plumb** 41:37 So, well, it's true, it's when the agent starts up, especially. Yes. And…
So, whoops, I don't have a collector, so we're gonna see a lot of these, but ignore those. So, if we, …
Or maybe I'll just… maybe I'll just launch a collector, I can do that very quickly, one sec.
I just… I have it in another window, so let's… let's do this again. Stop that.
clear…
Did the collector come up? Yes, it did. Okay, so now we won't see the collector things. And I think this won't be a surprise to anyone, but there are violations, and it is finding instrumentation.
Because the agent, the initializer.
**Cesar Munoz** 42:19 SBIs.
**Jason Plumb** 42:21 Yeah, exactly. So… We have this one here, which is a disk read, looking for…
service loader, Android Instrumentation loader, right? So we're looking for anything that is annotated with Android instrumentation, or implements the interface, I forget which, but it doesn't matter. It's still gotta go walk.
The classes on the class path to find these, right?
And so we get dinged on that as a discrete. The way to avoid this, if this is sensitive to your application, the way to avoid it right now.
Is to not use the agent.
It's to… I think it's explain….
**Cesar Munoz** 42:57 You can disable the search, the automatic search.
**Jason Plumb** 43:02 you can.
**Cesar Munoz** 43:03 I think.
I think so.
And then you have to manually install stuff.
**Jason Plumb** 43:10 You have.
**Cesar Munoz** 43:10 That's what I was getting.
**Jason Plumb** 43:11 You can manually install, but I think if you go through the initializer, you can't.
Can't.
**Cesar Munoz** 43:18 Yeah, because initializer is… … opinionated, so….
**Hanson Ho** 43:26 So is the goal here to have a path forward for agent users to not have any strict mode violations? ….
**Jason Plumb** 43:35 I think that's taking it too far.
I'm not prepared to say that that's an end goal, but I think that this will continue to come up.
periodically, with people that see these, like, they're like, I put in strict mode, and what is all this? And you're slowing my app start down. That's the thing I care more about, is people that are like, hey, I did a side-by-side comparison, and like, you've slowed me down by…
let's call it 200 milliseconds, right? And you're like, well, yeah, we spent 200 milliseconds looking on the class path for instrumentation because we made it easy for you to have instrumentation. Like, that's the trade-off, right? And the flip side there for users that cannot stomach the 200 milliseconds, I want them to have an option.
Where it's like, okay, at build time, I can configure somehow these list of instruments that I want, and I want that to be easy, and avoid the class path hit, if possible.
And it looks like we hit it a couple of times, and I'm not… Entirely sure why it's repeated.
**Hanson Ho** 44:36 We, there, there are multiple disk reads, including reading the, so asking for the, the application version and names to put it in the resources. Those are both disk kits. Yeah, but, ….
**Jason Plumb** 44:49 I'm seeing this one multiple times, the instrumentation loader.
**Cesar Munoz** 44:54 Yeah, she don't….
**Hanson Ho** 44:55 Oh, interesting.
**Cesar Munoz** 44:56 once.
**Jason Plumb** 44:56 Yeah, I'm just a little confused by that.
**Cesar Munoz** 45:01 Again, I can create an issue, because if I understand what you're saying, it's like, we should try to at least provide a
A… a… a configuration so that…
none of the automatic stuff that my reads from the disk happened, so that people will have to do it manually, or file time, or something. But as Hanson mentioned, there are cases
Where there's just no… like, when you have to read the app version.
Oh yeah, that's why Malay does, it does this reading, so….
**Jason Plumb** 45:35 legit.
**Cesar Munoz** 45:35 That goes to the resources.
**Jason Plumb** 45:38 Which is why I'm not ever suggesting that we try and get to zero strictment violations. I think that's… that's a little idealistic. I think, yeah, reading some things…
I mean, and a lot of those can be mitigated with build time Gradle trickery, right? If you want to have a build time Gradle plugin that takes the version or whatever we're reading and putting it… puts it in a class file, like, we could do that.
And then… then the class load doesn't get… the resource load, whatever it looks like, doesn't get attributed to our app. It's just part of the OS then. It's part of the platform at that point. But, you know, you're just moving stuff around.
**Cesar Munoz** 46:15 It's more to maintain, and it's more to maintain, but at least if they have a setter, That prevents….
**Jason Plumb** 46:21 Way more to mean to me.
**Cesar Munoz** 46:23 Search, yeah.
**Hanson Ho** 46:24 maybe we can create an issue that basically says document our policy towards strict mode? I mean.
**Jason Plumb** 46:29 That would be really helpful.
**Hanson Ho** 46:31 a combination of, like, fixing the egregious things that we can, offering an option to opt out, but then still there being a couple. So, you know, the Embrace SDK, we looked at how we can actually create automation to find it and reduce it. It is…
it is difficult even creating automation because of race conditions. And in fact, the actual impact isn't quite, like, 200 milliseconds. It's… it's part of the emulator that's doing this. But it… it is… it is… it is… it is…
more time, like, than… than you would want. The SDK may take, you know, 100 milliseconds to start up. That may add another 20, or… I think the problem is that it's, it depends on how the OS, how busy it is. So it could be, like, no time, it could be, you know.
2030. And I think that's… that's… people don't like that, so if we could just, like, at least have a policy of what
you know, this is our approach to strict mode, then at least we could… people who create issues like this, we could just point it to them and say, hey, we understand this, if you want to, you know, have a test that does it, you know.
do these things. But in production, you're taken hit one way or the other.
So….
**Cesar Munoz** 47:41 Yeah, I also think people… You know, get scared about the strict mode.
violation logs, and it's like… my understanding is that Android, the OS, it's just telling you what's going on in the main thread, but that doesn't mean that it's gonna cause an actual issue.
Yeah. But it's noisy, so….
**Hanson Ho** 48:01 Some ones you actually should turn on and make sure it doesn't happen. So, like, doing networking on the main thread, bad idea. Don't do that. But there's a few… not all strict vote violations are created equal, so…
But we should be more explicit about our approach to it, so….
**Cesar Munoz** 48:19 Sounds good.
**Jason Plumb** 48:20 I was trying to do this dumb thing to put a breakpoint on this to see if it's actually getting hit more than once, but…
I still don't understand why we're seeing it multiple times.
**Hanson Ho** 48:29 Is it a race condition without proper locking?
**Jason Plumb** 48:32 I don'.
**Hanson Ho** 48:33 I don't know. My spidey sense is tingling, but we're only hitting this once.
**Jason Plumb** 48:38 that I know of.
And…
I think these are all within….
**Hanson Ho** 48:49 Is the same violation being propagated.
**Jason Plumb** 48:51 Why are we crashing? Whatever, I'm being mean. It… I think it is the same thing, though, right? So, but, okay, so the way that this works is, like, this loader, finds them all, right? So it's lazy, use the service loader, find us all of these, and then put them in a map.
Where their class is associated to that class.
And then you make a map of it, but that shouldn't hit this multiple times, should it?
**Cesar Munoz** 49:20 No, I shouldn't.
**Jason Plumb** 49:21 Oh, next provider class. Maybe… hmm….
**Hanson Ho** 49:25 Oh, it's one hit per iteration.
**Jason Plumb** 49:28 Maybe, that's what it seems like. So, service loader… That's a platform class.
we're saying… Service loader load… That just might be the way it works.
**Hanson Ho** 49:42 Yeah.
**Jason Plumb** 49:43 I hate it.
is, like, every time it finds one of these, it has to do a disk read, and that's what we're getting dinged on, is, like, for once… actually, can we… can we filter, like, by this?
It's not specific enough. You can filter, like, on this, right? And then…
We get a count? No, because it gives us the whole stack trace.
**Hanson Ho** 50:07 Hmm.
**Jason Plumb** 50:08 Do we get a line count in here anywhere?
Got it.
I don't know. I don't know what I'm doing, I'm… whatever. I bet you that's what's happening, though. It'd be… it'd be interesting to, … we could do an experiment and take a bunch of these out of the class path.
Like, we can.
**Hanson Ho** 50:28 Whoa!
**Jason Plumb** 50:29 Just get one now, right?
Maybe?
**Cesar Munoz** 50:36 Yeah.
**Hanson Ho** 50:38 That's odd.
**Jason Plumb** 50:41 Sorry, this is just, like, a fun kind of experiment with extra time here, y'all.
**Hanson Ho** 50:45 This is what makes these recordings so awesome.
**Jason Plumb** 50:49 Why is this not running? Like, why did the run option go away from me here? Do I have to… oh, I have to.
**Hanson Ho** 50:53 You have to sync, yeah.
You touched the Gradle file, who knows what you changed?
**Jason Plumb** 51:00 There is a way to turn that, like, on to auto-sync, but, like, then it's also perilous, if I remember.
**Hanson Ho** 51:06 Yeah, you make a line change, it auto-sync.
**Jason Plumb** 51:08 Oh my god.
**Hanson Ho** 51:09 We're gonna 19 yellow sinks.
**Jason Plumb** 51:11 Okay.
Notice again.
**Hanson Ho** 51:14 I think it failed.
Oh, wait.
Maybe not.
**Jason Plumb** 51:18 Maybe it's still running.
**Hanson Ho** 51:20 ….
**Jason Plumb** 51:22 Because I removed a bunch of stuff, of course it's gonna take a long time. Okay, so….
**Hanson Ho** 51:26 Yeah, you need it.
Okay, so the initializer….
**Jason Plumb** 51:33 Yeah, okay, so we do need some of that. Well, whatever, that was a fun experiment.
So, I can create the issue, and we can figure out what to do with it.
I was gonna make… yeah, yeah, I appreciate that, please do.
**Cesar Munoz** 51:45 Thank you.
**Jason Plumb** 51:46 put it in the notes. I think, I was gonna also mention that I think it would be great
for us to have a docs directory in the repo that we can start pointing stuff to when repeated questions come up. And we don't have to call it a fact, but it's, like, effectively, like.
you know, our rationale, our reasoning behind certain decisions that have been made over time, and at least we can point to a place and say, here's why we did it this way, or here's why we think you shouldn't use metrics, right? It's like, at least we can start to write that stuff down, because
Finding it in our notes or finding it in the recordings is not practical for most
Common things that will get brought up again, so….
**Hanson Ho** 52:25 Yeah, we often answer this stuff, like, in text form anyway, either through an issue or through Slack or something like that, so you might as well, you know, once people are okay with it, copy and paste, dump it up there.
**Jason Plumb** 52:36 Yeah.
Cool.
Alright, does anybody have anything else?
**Hanson Ho** 52:46 Who's going to KoopCon?
**Jason Plumb** 52:49 I hope to.
To November?
**Hanson Ho** 52:53 Yep.
**Jason Plumb** 52:54 Atlanta?
**Hanson Ho** 52:55 Yep.
**Jason Plumb** 52:55 Yep.
**Hanson Ho** 52:57 Excellent.
**Jason Plumb** 52:57 My talks were not accepted.
So, it's a different… it's a different route now for me, but we'll see if I can get out there.
**Hanson Ho** 53:06 Yeah, I'll be talking about, life of a, a mobile span. Cool. So, did you, did you see, Jamie and, …
I did.
Yeah, I basically took that and said, hey, I'm gonna do it the mobile version. So, we'll see. Hopefully, it'll be good.
**Cesar Munoz** 53:25 book.
Well, this year is no travel year for me, so…
I also will miss this one, but….
**Jason Plumb** 53:32 You know, in the spring, it's in Amsterdam, right?
**Cesar Munoz** 53:36 Yeah, but it's a… It's complicated right now, I cannot travel.
**Jason Plumb** 53:40 I get it. Yeah, okay.
**Hanson Ho** 53:42 Fair enough.
**Jason Plumb** 53:43 Alright, well, hopefully everyone can have a great rest of your day. Please be well, and we'll see you soon.
**Hanson Ho** 53:50 Take a look at the reviews.
**Jason Plumb** 53:51 Right.
**Cesar Munoz** 53:52 Right?
