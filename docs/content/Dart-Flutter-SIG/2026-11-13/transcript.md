SIG: Dart & Flutter SIG
Date: 2026-11-13
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Robert Magnusson** 00:16 Hello, good morning.
**Michael Bushe (Mindful Software, LLC)** 00:17 Hey, Robert.
**Robert Magnusson** 00:21 Hello.
could learn new stuff, thanks for sharing. I just knew the concept, I never heard a name on it.
**Michael Bushe (Mindful Software, LLC)** 00:29 Oh, yeah, yeah, right. That, iron triangle comes up, I think originally it comes from, like, military, right, like, a tank can be fast, or powerful, or defensive, I think, you know, so it's a little different.
But yeah, yeah, that's a…
**Robert Magnusson** 00:50 Yeah, makes sense, because I think I heard it mostly from… was it? Martin Fowler, or from Uncle Bob?
I don't remember which, but I… it makes sense that they tied in, because one of them are really into, like, I think it's… with Uncle Bob, he's really into, like, old stories from his past building up.
**Michael Bushe (Mindful Software, LLC)** 01:06 Definitely, definitely. Yeah, that's probably more Uncle Bob than, than Martin Fowler.
I had the rare chance of seeing Martin Fowler speak He hates to speak. He hates to speak to other people, yeah. And but he came to Boston one day and gave us a talk on when the refactoring book came out. Hey, Yusuf, how's it going?
**Robert Magnusson** 01:28 Hey, Yusuf.
And little guy, future use of… future, hotel maintainer.
**Michael Bushe (Mindful Software, LLC)** 01:35 There we go! Got a little guy.
Howdy!
Woohoo!
I don't know how to say good morning, and… And, what's up, Bonsai?
How do I set… I have a brand new background I'm trying to set. How do I set that?
Settings here, okay.
Backgrounds, I could add mine, add mine.
**Yusuf Rosman** 02:20 Oh, yeah, I won't speak. I've been speaking, but I didn't realize that I'm They were ruined.
**Robert Magnusson** 02:29 I don't know, that's, that's life with small kids, how you forget stuff.
**Yusuf Rosman** 02:39 I don't…
**Michael Bushe (Mindful Software, LLC)** 02:39 Good evening, you're still awake?
Hi!
**Yusuf Rosman** 02:43 So…
**Michael Bushe (Mindful Software, LLC)** 02:44 Hello!
**Yusuf Rosman** 02:44 Hello?
**Robert Magnusson** 02:47 Not very cute.
You're, you know, that's your first kid. Like you said, you just got a new kid also?
**Yusuf Rosman** 02:54 Yeah, second one, is expected to be next year.
**Robert Magnusson** 03:00 Okay.
**Yusuf Rosman** 03:01 Yeah.
**Robert Magnusson** 03:03 Exciting. Enjoy the time with one.
**Yusuf Rosman** 03:08 I am, I am.
**Michael Bushe (Mindful Software, LLC)** 03:11 How old is he?
**Yusuf Rosman** 03:13 He's going for next month?
**Michael Bushe (Mindful Software, LLC)** 03:15 And what is your name?
Does he speak any English?
**Yusuf Rosman** 03:21 I didn't… I haven't exposed him to English yet, and yeah.
**Michael Bushe (Mindful Software, LLC)** 03:26 What is your name?
**Yusuf Rosman** 03:28 November.
Rainy?
**Michael Bushe (Mindful Software, LLC)** 03:32 Yes!
**Yusuf Rosman** 03:33 It's eigen.
How you doing?
**Michael Bushe (Mindful Software, LLC)** 03:35 Wow, that's a nice name!
Hi, Ivan.
**Yusuf Rosman** 03:41 Actually, I'm surprised, because he answered.
**Michael Bushe (Mindful Software, LLC)** 03:47 Thanks for that.
**Robert Magnusson** 03:48 That's usually how it is, right? When you're alone with your kids, they don't do like you want, and then other people come, and then they are all super nice and happy, and…
**Yusuf Rosman** 03:55 Yeah, I guess most of the time when people ask him, just very quiet, and, like, just close himself, or hides behind me.
I'm very surprised that you actually answered it.
How old are you?
I am one naive.
Oo? Oo? I am.
4? O. Yusu. Yes or.
**Michael Bushe (Mindful Software, LLC)** 04:23 You are 4 years old! You're a big boy!
**Yusuf Rosman** 04:28 And big boy.
O paddles.
**Michael Bushe (Mindful Software, LLC)** 04:41 Plus O Yahashi, too, good.
Well, let's get started. I don't think I filled in the agenda exactly, but there's, Right, no, I did do one thing, good approval practices. So I just posted, just now, I meant to do this yesterday, but I reviewed it with other people first. But I just posted into the Slack, y'all can take a look. We can take a look now if you want.
But basically, Harshit is going to become an improver. He accepted that role.
And we're going to have, and this is similar to what we've been doing anyway, but, two approvers.
And those approvers have to include one maintainer.
This is not… This is pretty typical for most projects, and pretty typical around open telemetry. It's almost the standard thing, and you know, most businesses kind of work that way, too.
So, congratulations to Harshit. Harshit was also, nominated, and at least got some votes for, OpenTelemetry Community Contributor, is that it?
We'll, I guess, we'll see the results of how that comes out.
**Harshit Kushwaha** 05:58 The results were already out yesterday.
**Michael Bushe (Mindful Software, LLC)** 06:02 Oh!
**Yusuf Rosman** 06:02 Oh.
**Harshit Kushwaha** 06:03 Huh.
**Michael Bushe (Mindful Software, LLC)** 06:04 Did you make it?
**Harshit Kushwaha** 06:06 No, I didn't.
**Michael Bushe (Mindful Software, LLC)** 06:09 I'm gonna… I'm gonna lobby… now that I… I'm gonna lobby for you next year. You're gonna get it next year. I'm gonna be… I'm gonna lobby 100 people to vote for you.
**Robert Magnusson** 06:23 Yeah, me too. Sorry about that, I was too late, I missed… I saw it half a day too late, I was so underwater that week, but…
**Yusuf Rosman** 06:29 Maybe my.
**Robert Magnusson** 06:30 boat still got in, but next year, I will also push more forward.
**Yusuf Rosman** 06:32 Yeah, next year, you'll get 3 from… you'll get 3 points.
**Harshit Kushwaha** 06:35 Thank you.
**Michael Bushe (Mindful Software, LLC)** 06:37 No, I'm gonna lobby every language, and you're another group, too. What are the other groups that you contribute to?
collector.
**Harshit Kushwaha** 06:45 The collector SIG and the Java SIG.
**Michael Bushe (Mindful Software, LLC)** 06:49 Wow, yeah, okay, so, right, there's a lot of people in those two SIGs, they're the most popular, so, I will cross-lobby with them.
**Yusuf Rosman** 06:58 No doubt.
**Michael Bushe (Mindful Software, LLC)** 06:59 maybe I should be sitting in on some of the Java SIG meetings anyway, just for interest. I'm an old… my… well, my original language was Basic and then Pascal, but for a long time, I was a Java guy.
And, I love Java. And one of the reasons why I do Dart is, something I always say is that, Dart is a better Java. Do you guys know that?
this Gilead Bracca is the name on the Java language specification, and he's also the name on the Dart language specification. And, there's also, like, if you look at the collections in Dart.
Neil… oh, what's his name? Neil? I want to say Neil Cassidy, but he's a famous beatnik. Neil, I can't remember his last name now. He did the Java collections, and he helped out. A lot of the Java guys moved from Sun to Google.
And, they were involved. And a lot of the Java Swing guys, were involved in creating Flutter.
Which is pretty cool. That's one reason why it's so strong. And they both have the same kind of right once run anywhere.
But in Dart, we get a binary, which is awesome, instead of needing the JVM hanging around.
**Robert Magnusson** 08:18 Yeah, this I didn't know. So the JavaSwing guys, that UI library for Java.
**Michael Bushe (Mindful Software, LLC)** 08:23 Yeah, that's right.
**Robert Magnusson** 08:23 build up, okay. I don't have so good memories of it.
That was, like, our university… first university coding experience.
**Michael Bushe (Mindful Software, LLC)** 08:33 When you order… so, I worked at Amazon Robotics, and you've probably seen the robots running around in videos, right? They bring your item up to a packer.
when the robot comes up to the packer, I worked on the UI for that, and it's a JavaSwing UI.
And it shows the item, and the… they come with a, they come with a bunch… the robot brings up a whole bunch of bins of random stuff, and it'll tell the packer, A4, you know, with a picture of it, and so he could just reach in the bin really quickly.
And pull it out. So, yeah, Java's used all over the place still, and then… and on the back end, it's… you know, Java swings kind of dead, that was kind of rare. But, Java is still a huge, huge, huge in the back end. And do you see my, my AI-generated graphic.
We're one of the last languages here, and I always forget his name. Chad, no, what's his name? What's the mascot's name?
**Robert Magnusson** 09:31 And fuck. I just read it yesterday.
**Michael Bushe (Mindful Software, LLC)** 09:36 Yeah, I forget, I said it last week, too, but I forget it. He's got one… Anyway, he's about to get, He's about to get wet with open telemetry, so that's…
**Yusuf Rosman** 09:48 Oh, dash, dash.
**Robert Magnusson** 09:51 Yes, Dash, thanks.
**Michael Bushe (Mindful Software, LLC)** 09:53 Dash, that's right, Dash is about to get wet. He's gonna have to dash away from that.
Okay, so, great, good approval practices. I… I have to admit, I've been slow this past week. I promise this time, over the next two weeks that I'll be, spending some more time. I… what I'm trying to do is… is make sure that the… official repository is clean, and then the, and then the API is kind of, like, what I worry about first, and then the SDK, right? So, kind of the more base to the… to the leaf.
And I… I'm gonna… I think… Yusuf, you've probably moved the, the, the, your PR along in the Dart and Classroom? Yeah.
**Yusuf Rosman** 10:38 Yep, the Open Telemetry Dart. Yep, I've updated my last PR.
I haven't responded to your comments yet, but I already do the change.
Just that I haven't dropped the comments yet.
No, no.
**Michael Bushe (Mindful Software, LLC)** 10:54 No rush. You got, you got a little kid and a pregnant wife, so we don't expect, we don't expect it, right? But that'll be nice when we get that in, then we have, a directory structure that we can set up, and it looks really good.
the 8… what I want to… what I keep trying to work on next is, the any value, and I keep dropping it because it's just, again, a big chunk.
And I just want to make sure I have the time to do it properly. I think it's our… I've already done this once or twice, but I just want to… it's a big… it's a big deal, and I just want to take a careful look at it one more time. Hopefully, I'll have that in.
On… on this weekend, and then we can start attack and the… the SDK issues. I do have… I have been doing some work, it's just you haven't seen it. And I have, 5 new SDK issues. One might… one might be, an API issue.
I didn't realize that… I thought that our SDK, or the API… oh, no, the SD… right, that's why. The SDK does not specify the telemetry SDK name.
And, the version and the language.
I think what I'm… and I do want to get some feedback on this, even before I post it, There's a telemetry.sdk.name, attribute that every SDK is supposed to stamp.
I could put Dartastic OpenTelemetry while it's in Mindful Software, but I don't think I want to do that, because that would cause churn. I think I'm just going to put in OpenTelemetry, which would be the official one, even though it's not quite official yet. Does that make sense to everybody?
**Robert Magnusson** 12:39 Yeah, I think it's okay with you. I mean, no one's really stopping at… I mean, anyone who spilled something can put whatever they want in there. It's not a… there's no copyright on the name, I guess, on what you send as the protocol there, so I guess there's no problem there. I mean, if it's okay with you, I guess… Because it's… yeah, no, that… I think that makes sense, sorry, to not talk too much, if you're okay with it.
**Michael Bushe (Mindful Software, LLC)** 13:04 It's a matter of, if somebody's using Dartastic OpenTelemetry versus OpenTelemetry, what are they going to want to see for this value?
**Robert Magnusson** 13:13 Yeah.
I guess that's, like, also how they pull it in, because now if they pull it in from… OpenTelemetry… PubDev, OpenTelemetry, that's now pointing to Dartastic, right?
**Michael Bushe (Mindful Software, LLC)** 13:24 Correct. Right.
**Robert Magnusson** 13:26 will swap at some point, and then they will be maybe a bit surprised. I mean, they would have to probably do a manual version bump to get the latest, but… Since it's… most people get it from there, and that is supposed to be the OpenTelemetry one in the future.
Maybe it makes sense to say it's OpenTelemetry Dart.
**Michael Bushe (Mindful Software, LLC)** 13:42 I think that's exactly what my thinking was. Otherwise, I think I would have put Dartastic OpenTelemetry until then.
Did… did everyone see… I know Harshit saw my LinkedIn post, and I don't know if you guys also saw my X post. We have open telemetry sighting in the wild.
Did anyone see the Flutter announcement yesterday? The Flutter announcement for 3.5, which is really great, because the FFI gen stuff, direct access to native code, is in there. If you kind of scroll down there a little bit, one of the announcements is Genkit UI… I'm sorry.
Genkit, 1.0 is… was announced, and Genkit has open telemetry, and it was actually put in there in the, in the announcement, so that was… that was very exciting. I… yeah, right? I took a look at the, At the, at the repo, and they did a nice job, and yeah, they imported Dartastic OpenTelemetry 0.11.0, and there we go. Yeah, right?
**Robert Magnusson** 14:49 Cool. Yeah, this is… I mean, this is really great, because then you start getting… instrumentation for free in Europe. You don't have to instrument everything, and you don't have, like, in our Flutter layer, we don't have to build too much out instrumentation, because ideally.
Library is just instrument, and you just get it for free anyway.
**Michael Bushe (Mindful Software, LLC)** 15:05 Right? Okay, that's awesome.
**Robert Magnusson** 15:07 Yeah, that's cool, that's really cool.
**Michael Bushe (Mindful Software, LLC)** 15:09 Yeah, I'm sick about that.
**Yusuf Rosman** 15:12 They just, they just assigned that.
Things are getting more serious for us.
Alright, we've got official libraries.
**Michael Bushe (Mindful Software, LLC)** 15:22 Right? And it's not just, you know, it's not just an indie developer using it, this is Google putting it out, so yeah, that's in a 1.0 of something that they keep promoting, so yeah, I think that's huge. I think it's a big deal.
And they use the, another big thing that, and this… I've talked about this in our semantics, but the semantics is really important, but the Gen AI semantics is especially important right now, right? Everyone's creating new GenAI applications, and people want to be able to query people want to get telemetry from the AI, you know, so it's not such a black box, especially with pricing, and tokens and speed, and size, and caching, all these things. I think the caching would be outside the GenAI semantics, but… and so they use the standard semantics. That was another thing I was… making sure that they use, which makes sense, which is just beautiful. And Claude also, announced OpenTelemetry. I, today, my Claude.
that I… you have an API key, and the open telemetry from that API key gets fed into my Dartastic, backend, telemetry backend, so I can see what's happening with my keys, which is totally cool.
And if I switch to OpenAI, the telemetry would be the same, so I could use, like, the same dashboards, and so that's really neat.
**Robert Magnusson** 17:01 Yeah, that's cool. Yeah, I just saw this now. Yeah, that's the package, right? The Gentile, Jankit Hotel?
**Michael Bushe (Mindful Software, LLC)** 17:05 Yeah, that's right. Yeah, well, the hotel is, like, the sub-package for it, right? Right. Actually, because it has to.
**Robert Magnusson** 17:10 direct, reference there, how to set that up with Darcastic.
**Michael Bushe (Mindful Software, LLC)** 17:14 Right? Isn't that great? Hotel.initialized.
Now, now I guess we can't take it out anymore.
We can. We can, you know, we can… it's 0 without 11, so we can, but let's… you can think about it.
**Robert Magnusson** 17:33 Cool.
**Michael Bushe (Mindful Software, LLC)** 17:35 Robert, you got anything else for us?
**Robert Magnusson** 17:39 What did I have? Yes, I'm going to PRS, I think I'm mostly caught up. It's just a bit of a problem with talking about AI.
so many PRs coming in, like, internally, and open source projects.
I feel like I only did PR reviews the last two weeks.
**Michael Bushe (Mindful Software, LLC)** 17:58 As soon as I.
**Robert Magnusson** 17:59 I'm done, there's new updates coming in.
Yeah, I think there's still a gap there in the new engineering culture, how to manage reviewing PRs. Like something we're doing internally, everyone sort of does their own review currently. There's not a standardized pipeline.
I think, like, down the road, as AI gets a bit more stable, also for open source like this, probably there should be some sort of standardized AI that just reviews it according to fixed practice.
**Michael Bushe (Mindful Software, LLC)** 18:24 Sure. Yeah, I like the idea.
**Robert Magnusson** 18:28 Yeah, but that's, I guess… future us, and I'm also not sure how well approved that is by open source at OTEL. It's a bit more anti-AI still, but for reviewing It could offload a bit, but that's the Futros.
**Michael Bushe (Mindful Software, LLC)** 18:44 We do it anyway, right? I use AI in my reviews, so… and that is up to each… at the end of the day, we gotta sign off, we're humans, but I think, you know, also, every project… the OTEL API, the SDK, the, you know, the actual bits and the telemetry has to be the same and consistent across all languages, but each project can do… can make it the way they want, and so we do have that liberty.
**Robert Magnusson** 19:13 Yeah, but on that, also, what we talked about for the quality, I think that's really key that we are… hands-on. Like, you don't really need to use so much AI code, maybe, if you're building, like, the Flutter app, the app itself, or, like, a web page.
But where we're starting, especially now what you just showed, like, the Jenkit using our things, it has to be really, like, locked down and follow the spec, and be semantically correct, but I think there we really have to be hands-on. But the reviewing part of it, I mean, that's just… reviewing things, and if it's a false positive, that's okay. I think just that could ease a bit the initial, like, Putting everything in a good state before you invest too much mental load reviewing everything.
**Michael Bushe (Mindful Software, LLC)** 19:57 I like to think about reviews as that place where, where the quality happens. I mean, quality happens at every step, right?
team gets involved, and we all have great minds, and we're all sharp folks, and when we work together.
we produce a better product than any of us can work… can create on our own. Yes, definitely.
**Robert Magnusson** 20:24 Exactly. It just feels like, a bit like this, When I started, we were, like, sending code back and forth to each other, and just manually reviewing it. There was no, no linting, no code analysis, and then adding that before you even started reviewing helped a lot, because then you already knew, like, all these compiler errors, and linting and docs mistakes. I think AI could do something like that. You just do an initial run, and you sort of put it in an okay state, that now you make sense to start reviewing it.
**Michael Bushe (Mindful Software, LLC)** 20:51 Oh, yeah, I like that. Oh, I got you, right, for sure. The more tools we… the more you, what, shift that left, yeah, the better that we're in a state. Right, we already do that with… especially with Dartlinting, which is really nice, and and with… I think the other, the other nice, It's a difficulty, but we… you can't put in code without having tests that covers those lines now, you know, especially as we get close to 100% on each one, and I think that goes a long way, too.
**Robert Magnusson** 21:26 But that's just a general note, and it's, like, future us to set that up.
Now, otherwise, I'm not sure. Should we go over open PRs and see?
What's the next things to tackle?
**Michael Bushe (Mindful Software, LLC)** 21:35 Go, go, you wanna share your screen?
**Yusuf Rosman** 21:37 Actually, I just wanna ask…
**Michael Bushe (Mindful Software, LLC)** 21:39 Yeah, go ahead.
**Yusuf Rosman** 21:40 I just want to ask if you have, like, common AI skills for, I mean, since we talk about AI for reviews. I do have one, I'm just curious if everyone has their own That, you know, something that we can align on.
Right. Yeah.
**Robert Magnusson** 21:59 I mean, that's… I think that's… that's something that's missing. That's my general pain point I had recently, also at… internally at Grafana.
it's very unstructured right now. It's, like, a bit like Wild West. I have my skills, I have my tooling I run, everyone else has their own, and depending who runs it, you get different results, and it feels like, at some point, it should be sort of standardized, and it's everyone trying their own thing now, and Claude offering their own code review, I guess Codex also has their own.
So that's an interesting question, yeah. So what I had good success with is always running both. So I always run cloud and codecs in parallel, and then have them interact with each other and brainstorm what the other one found good, found bad, because they have a bit of different qualities.
Both models.
**Yusuf Rosman** 22:43 Where you're, you run both.
How much tokens did you get?
**Robert Magnusson** 22:48 Yeah, I mean, that's a luxury being at Kafana, they pay you a lot for the tokens.
**Yusuf Rosman** 22:53 Oh, whoa.
**Robert Magnusson** 22:55 But what also helps, we have a starting to define a fixed one, where you say, like, you have these five spots you always want to review. I can share, I have a PR review skill I open-sourced.
I have, like, my own dashboard app that picks in all the reviews, and I can kick off AI reviews.
And I can quickly show you.
I can share the link later.
Yeah, yeah, that would be great.
If I can, I can share here.
**Michael Bushe (Mindful Software, LLC)** 23:20 It's interesting, I think it's just like… I keep finding that AI is like humans, and it's the same. You don't want 5 people who think the exact same way looking at code, because it's not going to get.
**Robert Magnusson** 23:32 Yeah.
**Michael Bushe (Mindful Software, LLC)** 23:32 This is where diversity, you know, diversity of minds, not just of skin color, right? Diversity of culture, diversity of ways of thinking makes things better. Oh, this is pretty cool!
**Robert Magnusson** 23:43 I have this web app I built, I can kick off an AR review here.
And it does a whole bunch of stuff, I can just kick it off on one, maybe. I don't know, take this one, maybe?
And then what it does, it does all these specific checks.
And then writes me an explainer of what this is being doing.
And then it has a different agent also reviewing what the output is, so they sort of work together, codec and Claude. And you can tweak it to your liking. I can share the link data to these people.
And then each sub-agent has its purpose only. And it usually turns out to be good. And I'm trying to get this standardized across, that we have some sort of common understanding.
And then once it's done, you get done, just explain if I have one that is done…
**Michael Bushe (Mindful Software, LLC)** 24:27 So, I have a bunch of, you know, agents. My agent's file points to other files, some that would help us with this. How could I contribute what I have into this.
**Robert Magnusson** 24:44 So this is actually just a skill, might I open my GitHub.
This is a bit more also, so this is my way to manage all my inbox, because I have so much PRs flowing at me. So this is the explainer code changes, and I get this out of the box, sorry, one more here. I get this out-of-the-box also tips, what it finds, and then I go over this manually. So at the bottom, it explains all the code.
And at the bottom, I get these proposed findings by it, and then I can walk over these myself.
And it's here… Second, PR review scale… Ugh, no!
Come on.
It's just a skill that you put in your skill docs, and then it runs a local Python server.
And it talks to Cloud Code and the codecs. Like, it… there's no AI harness itself, it just feeds the… the request down to… And it runs all the code in a, like, in a small sandbox and verifies all the changes. So it doesn't just do code analysis, it actually Checks the code.
There might be bugs in it, mostly this is just vibe-coded.
And then my priority here is that I get all the new PRs, it pop in here, up next.
And then I can put them in a review, and I start review, and I say done, and then they go away from my mind, and as soon as there's a change to them, they pop back here.
that some… something changed, and I can start reviewing them again.
**Michael Bushe (Mindful Software, LLC)** 26:10 That's super…
**Robert Magnusson** 26:12 And it's pretty well defined, but I don't have an eval around this. I'm not really sure if it gets better or worse, so that's the thing missing.
**Michael Bushe (Mindful Software, LLC)** 26:20 Right?
**Robert Magnusson** 26:22 Which you probably should have, to evaluate, are you doing worse or better?
Yeah, I can share it in the chat with her now.
Feel free to, and do with it what you want.
**Michael Bushe (Mindful Software, LLC)** 26:35 I'll take a look at that. Let's, I do want to make sure we touch everybody.
Lapier, you, you had something you want to tell us about what's going on, your… any updates, or…
**La Pyae Oo** 26:51 I'm going to just retry, recrying.
Yeah, that's… that you assigned me.
There's
**Michael Bushe (Mindful Software, LLC)** 27:00 Great, great.
**La Pyae Oo** 27:02 events.
**Michael Bushe (Mindful Software, LLC)** 27:05 Harshit…
**Harshit Kushwaha** 27:10 Y… Yes.
**Michael Bushe (Mindful Software, LLC)** 27:13 Any, any, any, is there anything we should be focused on with your, as we review your… the work that you've been doing on the various PRs?
**Harshit Kushwaha** 27:26 I'm still working on, like, the Prometheus one, the environment variables.
But all the changes are still local, I haven't pushed them yet. But I think I will push them by tomorrow.
**Michael Bushe (Mindful Software, LLC)** 27:41 Awesome, awesome.
**Robert Magnusson** 27:43 Yeah, hey, one thing I forgot about. So, on the Harshit topic, how do we move that forward? I saw I got an email some time ago.
And you mentioned something, we have to first open a PR on the OpenTelemetry… now I forgot the name.
**Michael Bushe (Mindful Software, LLC)** 28:00 Yeah, so this involves an admin change. The admins… it involves a change that we can't do, we have to ask the admins to do it, so there's a little bit of process that we… this will probably take a week, I assume.
**Robert Magnusson** 28:13 Okay, and that then comes first, and then after that, then we can, Is it also, like, managed as code? It's not a manual going to GitHub and adding, Harshit into, Teams.
**Michael Bushe (Mindful Software, LLC)** 28:26 there, there's that, right. So the first, I think, if I remember right, and I, and I remember so little that I forgot that I had nominated Harshit to be a contributor, to be a, you know, to, get him some recognition. But, if I remember right, it works like this.
I think one approval, or two approvals work from anybody, and And so we have to ask to change our repo so that a maintainer is always As always one of the approvers.
And then, Once that's done, then we can adjust our… we could do it early, right? But we could put our sheet in there, and just, you know, we don't need the system to enforce it, we know, right?
**Robert Magnusson** 29:17 Okay, but this I can do now already then, because I saw… I got an email, and it said I should add, approve or deny request, and just add him to the… to the members list in GitHub. This I could do now. Of course. This is no harm. Yeah, okay, cool. Then I will add you there, Harshit. You should get an email then, I guess.
**Michael Bushe (Mindful Software, LLC)** 29:34 Alright, right on.
**Harshit Kushwaha** 29:35 Okay.
**Robert Magnusson** 29:39 And… To this team… sorry, it's with an auditor, yeah.
Yes.
**Michael Bushe (Mindful Software, LLC)** 29:55 Yusuf, you got anything else for us?
**Yusuf Rosman** 29:59 Nope, nope, I'm… A bit more, I mean, a bit… very tight hands now.
So, yeah.
I just hope… I just hope the bootstrap… I'm just focusing on the bootstrap, and… Hopefully by next month, when things are a bit more chill.
Hopefully.
**Robert Magnusson** 30:18 It will not get more chill, I think. No, because…
**Yusuf Rosman** 30:21 Because in my work, next month is gonna be… Release freeze.
**Robert Magnusson** 30:28 Okay. Oh, nice. Aha, you mean work-wise, okay.
**Yusuf Rosman** 30:30 Yeah, so, yeah, I think I can start to balance things out, because now… now, what's taking my time a lot is because we are doing, like, a huge UI migration.
It was… it was so sudden, the announcement, they announced it, like, last month, early, like, early last month.
But they want it to be delivered before 23rd November. I was like, whoa.
**Robert Magnusson** 30:51 By the way, do this now.
**Yusuf Rosman** 30:54 Me too.
**Robert Magnusson** 30:54 No, I think you don't have to depend. I mean, I think it's great work you're doing, all of us, I think you're… it's great to see all the peers coming in. I think also, like, quality is great.
So, thanks for all of you.
**Michael Bushe (Mindful Software, LLC)** 31:04 Right, we have 3 repos to work in, so no one's getting blocked by anybody. Don't feel like you have to do anything.
**Robert Magnusson** 31:13 Yeah.
So I shared the link now, I think it should be in the team now, Harshit.
Bold.
**Harshit Kushwaha** 31:18 Yeah, I bought them in.
**Robert Magnusson** 31:21 And I have one… one last thing before I have to jump to a different meeting. I guess we cannot really put… move over code yet, right? We sort of have to write new code in Otel Dart still.
**Michael Bushe (Mindful Software, LLC)** 31:32 This is really important. I… I… this… I… let's… let's figure this out before the next meeting, but he… Oh, let me… we do… we have… let's… bleh? Okay, so there's a stack of things here. One is… there's a… the reason why we can't move code right now So, moving code means we want everyone to have, credit for what they've already done. If I move in all the code, I get all the credit, and I don't want to take the credit away from you guys, or Robert, whatever. So, And the other thing is, there's two other kind of blockers. One is, most of my code that was done before we had a team.
have, authored by Claude. So, at some point, I have to do, like, an update that changes all those to assisted buys.
And it's gonna take a Git reset, which means we all have to, like, redo our sandboxes, so we'll have to coordinate that.
And the other thing is, there's, In order to put code in, everyone has to sign off on, everyone who's contributed has to sign off on… legally, to be a contributor to say that their copyright… they don't own the copyright. OpenTelemetry does, or the Linux Foundation, I'm not exactly sure how that works.
And that's something that Severin, our governance committee liaison, is working on, and so he's going to get back to us on… legally and how to do that. He's asked the legal team a couple weeks ago, but, you know, these lawyers, you know, they sit around and play golf, so they'll get back to it.
**Yusuf Rosman** 33:14 I mean, there's a bigger open source project? Wow.
**Michael Bushe (Mindful Software, LLC)** 33:16 Did I say that and it was recorded?
Oh, no, no, legal team's gonna be on me now. We have lawsuits against me.
But they'll get back to us really quickly with a high-quality solution, I'm sure. And so once we have all that, we'll probably have to do some kind of sign-off, I imagine, and then we can start moving code in.
I think what we're gonna have to do is basically cherry-pick Huge sets of, of, of code. Put them into the repo.
This is where my Git magic maybe isn't up to snuff, but put them in the repo, in the existing directory structure, which would be outside of our new stuff, and then move it over.
Something like that.
We'll get there. In the meantime, we're not blocked because, Robert and I agreed that he can take credit for my generated code, for, semantics, and that's our first step anyway. So, whoever wants to work on semantics, everybody wants to work on semantics, can jump into the semantics PRs that I think he's starting.
And, and get that going, and that's going to generate a whole bunch of code.
**Robert Magnusson** 34:31 Cool, yes, so that's my goal, to get that going.
I think today I will not get to it, because I have already booked my whole day, but on Monday, I will try to… I will start working on that.
**Michael Bushe (Mindful Software, LLC)** 34:44 Now I know you will, yeah.
**Robert Magnusson** 34:48 Yeah, cool. I have to go to a different meeting, but it's nice to see all of you. Thanks again for all your contributions.
**Michael Bushe (Mindful Software, LLC)** 34:54 Bye, Robert, great seeing you all. We'll see you in two weeks, and see you online, everyone.
**Yusuf Rosman** 34:59 Alright, they're on.
**Harshit Kushwaha** 35:01 Hey, bye.
**Michael Bushe (Mindful Software, LLC)** 35:02 Okay.
**Yusuf Rosman** 35:03 Oh, my go, Michael.
**Michael Bushe (Mindful Software, LLC)** 35:04 Yes, yes.
**Yusuf Rosman** 35:05 If you don't mind, Yufusa, I just want to ask about the semantic PR.
Right?
So… So basically, the last time I verified that most of them are code-generated.
But to a certain extent, because I realized that In the current semantic… even in current semantics, there are some files that was manually created, right? For example, like, the candidates.
Right?
**Michael Bushe (Mindful Software, LLC)** 35:41 Oh, I think I… are you talking about, like, the base files, like the OTEC.
**Yusuf Rosman** 35:46 Yes, yes, yes, yes, yes.
**Michael Bushe (Mindful Software, LLC)** 35:48 Okay, so that has to… if you just look at what we have in the API, I think it should explain it, but the way Weaver works is you have to say, include this too, or use this as part of the template.
I had Claude do it, I didn't even look. But yeah, there's a way to do it. It came out okay, so I'm like, okay, it's generated, it works. I was good with that.
**Yusuf Rosman** 36:08 Yeah, yeah, yeah, kind of answers on that.
But there's this thing where I read about, semantics, where there is, like, one stable, and then everyone is incubating.
So, QBiting is the one with… Those, that is in… Development semantics, something like that.
**Michael Bushe (Mindful Software, LLC)** 36:31 Yeah, I don't think it's incubated, I think it's the… I think it's development… I think it's just… there are two, development and stable.
**Yusuf Rosman** 36:37 No, that's stupid.
**Michael Bushe (Mindful Software, LLC)** 36:39 If you look at our… whatever Weaver configuration files.
that are there, or maybe this is just the way Weaver works, but I think it's… I think this part is in the configuration file, too.
what gets generated includes documentation that says stable, stable, stable, development, development, development, and they're all fine to include. You know, people have to know that development is development, and it might change.
**Yusuf Rosman** 37:04 Hmm.
because… because currently my imprint… implementation is, like, I… There will be two entry points for the… for the package.
One is… currently, I'm calling it… I'm using the term incubating, because I think I saw some… some reports are using that term. I'll change it to development.
Another one is stable, so there is… there will be, like, OpenTelemetry semantics, slash OpenTelemary semantics. That one is gonna be stable, another one is, like, OpenTelemetry… OpenTelemetry semantics slash, development, I'll say, right? That's gonna be, like, all the development keys.
**Michael Bushe (Mindful Software, LLC)** 37:44 I… I would… I wouldn't… I think including more is better than less. It certainly should include every… has to include everything we have. We can't bring clients And including more is okay, as long as they're marked okay. The other thing you gotta pick up is, we're starting the fed… the OpenTelemetry is starting the federated semantics, and Gen AI is the first case, so if you look at the gen kit, it refers to the OpenTelemetry semantics for GenAI, which is in their own repo. So it's… now we have more than one repo to deal with.
**Yusuf Rosman** 38:20 Oh.
**Michael Bushe (Mindful Software, LLC)** 38:23 You… you don't have to do that all at once. You can… you can do whatever we did, just to keep it the same, and then update it, but, Yeah, maybe we should do an extra check, especially because Google's using it in Jenkit.
**Yusuf Rosman** 38:39 Oh, yeah, yeah, yeah, yeah.
**Michael Bushe (Mindful Software, LLC)** 38:40 Right? We do need to do, we need to make sure that everything is compatible. We're not breaking anybody, right? There's no breaking change.
**Yusuf Rosman** 38:47 Yeah, right, right, right, right, right. Good stuff.
**Michael Bushe (Mindful Software, LLC)** 38:50 And that would be not just in API, but in value.
the…
**Yusuf Rosman** 38:56 Boom.
**Michael Bushe (Mindful Software, LLC)** 38:57 the, the, openTelemetry stable means more than stable in most In most kinds of software. Most kinds of software, it means you can't remove a method, right? A public method, right?
**Yusuf Rosman** 39:14 Oh, yeah, yeah, yeah.
**Michael Bushe (Mindful Software, LLC)** 39:16 But in OpenTelemetry, it means you can't remove a constant, and the value of that constant can't change, because that's going into people's… backends, and people make dashboards off that value. So you're gonna… if you change it to a semantic value, you'll break a dashboard for a thousand.
**Yusuf Rosman** 39:36 Oh, yeah, yeah, yeah, yeah.
**Michael Bushe (Mindful Software, LLC)** 39:40 Which will take, probably… it'd be good if you had a… if you also made, just a test, a test that goes through all the semantics. There may be… there already are tests to do this, but they don't… internally, but maybe you can extend that test to kind of point it at… the existing, the outside repo, the Mindful Software repo.
And make sure that the values are all the same.
**Yusuf Rosman** 40:10 Oh, yeah, yeah, that's for sure. I mean, because currently, I'll say.
This should be the same. Sorry, I'm sorry, I haven't validated that, but since these are all code generated, so there should be, Should be one-to-one.
For the… for the… for the one. But maybe it's some difference on the… On the copyright, I'm not sure if it's the same, I haven't checked on that.
But, yeah.
In general, no, and… The values, the code generator should be the same here.
Yeah, I was thinking to, like, having maybe some CI to validate this, but, yeah… But, there can be some answers, because I'm thinking, like, if there are changes.
from the upstream, we were, right? And I was thinking, like, you can, like, auto-create a PR.
Instead of us, like, having to run it manually every time, and then, or there's a change, and we have to create a PR ourselves.
**Michael Bushe (Mindful Software, LLC)** 41:16 Right, yeah, yeah, automating that as much as possible would be good. Remember that this can be done in stages, right? We could just.
**Yusuf Rosman** 41:22 Yep, yep.
**Michael Bushe (Mindful Software, LLC)** 41:22 That way we could all take a look at it while it's, you know, while it's being created.
**Yusuf Rosman** 41:30 Right, right, right, yes, yes, yes.
Alright, so, guys… First thing is gonna be the bootstrapping. I… hopefully, I… yeah, I believe I have addressed all the comments, forgive me if I miss some, some.
robot layer proof of PR.
**Michael Bushe (Mindful Software, LLC)** 41:53 Awesome, awesome.
**Yusuf Rosman** 41:54 Right, right.
Alright.
**Michael Bushe (Mindful Software, LLC)** 41:57 Anybody else?
**Harshit Kushwaha** 42:00 There is one thing, like, I noticed that CNCF maintainer maintain a list in their landscape repository, and you are… Robert is still are not in the list, so I guess you both have to raise up PR.
I was checking it yesterday, so I thought, like, your name is missing and Robert is also missing, so I thought I would remind you.
**Michael Bushe (Mindful Software, LLC)** 42:24 This is in the OpenTelemetry Dart repo?
**Harshit Kushwaha** 42:29 No, the CNCF landscape maintained its own repo… for a maintenance list.
So you have to raise up PR there to add you as in the maintainer list in the CNCF landscape repository.
**Michael Bushe (Mindful Software, LLC)** 42:42 Oh, I thought this was done already. Okay, that's… I'll follow up on that.
We definitely want to be maintainers.
Or no PR will get through.
Alright, cool.
Thanks, everybody.
**Yusuf Rosman** 43:01 Alright.
**Michael Bushe (Mindful Software, LLC)** 43:01 Appreciate your time.
**Yusuf Rosman** 43:04 Thanks, everyone. Bye.
**Harshit Kushwaha** 43:06 Bye.
