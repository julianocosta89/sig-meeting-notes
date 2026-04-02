SIG: Semantic Convention Tooling
Date: 2026-04-01
Duration: 61 minutes
============================================================

## Zoom Recording Transcript

ariannavespri 00:06:21 Hello!
Jeremy Blythe 00:06:25 Hey, seems like it's.
ariannavespri 00:06:27 Yeah, I wrote… I wrote, I don't know if it's because of the summertime, whatever.
Jeremy Blythe 00:06:36 So, there was a message from… So, Laurent said he couldn't make it. LaMilla says she can join… The second half of the call.
ariannavespri 00:06:48 I don't… I don't see, I don't know where this was posted.
Jeremy Blythe 00:06:52 Oh, I tell you what, they've put it in a DM.
That's why.
ariannavespri 00:06:57 Okay, that's why.
Mystery solved. Okay.
Jeremy Blythe 00:07:02 And I don't know where Josh is.
He kind of hangs it all together.
So… I guess we may get with Miller.
In, like, 20 minutes or so.
I forget which bit you're working on. You were working on the, Some stuff for the packaging, right?
ariannavespri 00:07:32 Yeah, I mean, I had… I made the markdown templates, and now, exactly today, I started working on, you know, putting them into the package.
In the packages repo, because, I'm building on top of, Ludumila's branch, the one that she used for her demo, and basically what she did, she, she passed everything to, to, to V2 already, and so I'm building on top of that to, To put the stuff into the package repo, and, packages repo, and, to… to make the test and everything, every, you know, clean up things, and everything needs to be done there. And what I'm also working on, and it's, It's, on a, on a hotel collector contribib.
Jeremy Blythe 00:08:21 Right.
ariannavespri 00:08:22 it's using Weaver And it's basically an automation to, To, to, detect whether, whether, the telemetry of the hotel components is actually, you know, compliant with semantic conventions, and so we are… I'm working with, on this with Braden Keynes. I don't know if you're familiar with him, if you know him. He's a Googler, so maybe, well, I would say Josh probably knows him, even though Google's got a million employees, but he's also based in America, so… Yeah.
Jeremy Blythe 00:09:01 using LiveCheck for that?
ariannavespri 00:09:02 Yes.
Jeremy Blythe 00:09:03 That's amazing.
ariannavespri 00:09:05 And, so this is really, like, this is really, like, focused on, open telemetry components.
And so, in order to have, like, you know, a check be… a CI level, so before… before the code even gets into production.
So, to prevent…
Jeremy Blythe 00:09:26 Yes.
ariannavespri 00:09:26 Yeah. And, And so I, I, I mean, I had this draft PR for… for a few weeks, and yesterday I, I marked it as ready for review, and, I'm already getting some, some very, like, like, partial reviews just on, for now, it's mostly on… on… Go style. So, GoCode style.
And, but in any case, I mean, there's… it's also my fault, because I should be surfacing a lot of coordination and a lot of, conversations that me and Braden are having privately.
Jeremy Blythe 00:10:01 Hmm.
ariannavespri 00:10:02 Because this is built on top of a prototype that I started, so I continue to work.
And, so that people also have more context, just that it's a bit difficult to find the time.
Sometimes, you know, you just, oh yeah, you just forget, you take things for granted. So yeah, so I'm… I'm doing that, I'm doing that, right now.
Jeremy Blythe 00:10:24 That sounds cool. Hey, I'd be interested to see that PR if you…
ariannavespri 00:10:28 I can, I can…
Jeremy Blythe 00:10:28 In the chat.
ariannavespri 00:10:29 Yes, let me… let me… let me find it, yes, just one moment. And sorry for not having the video, but I'm… I still haven't… I was at KubeCon, and even though I'm not… I'm not… I'm no more in Amsterdam, I'm still, like, on the road, I'm not home just yet, I'm in Norway right now, so I mean, I can… In a hotel room, so it's, yeah, not the best setting.
It is what.
Jeremy Blythe 00:10:52 and you're.
ariannavespri 00:10:52 Let me… yeah.
So, I'm gonna… Yo.
Jeremy Blythe 00:11:02 I always love to see… I was talking to some of my colleagues at work, like, it's just amazing when you do open source things, and then… People start using it, it's just so cool.
ariannavespri 00:11:15 Yeah, yeah, yeah, yeah.
Jeremy Blythe 00:11:18 Alright, let's take a look.
ariannavespri 00:11:19 And of course, it's like, you know, once it gets… what… once it gets… approved, or, you know, after I change, whatever I have to change. Then, Braille and I were talking about what would be, of course, the best candidate.
because this pa… this is a package, this is a Go package, you know, that should be then adopted by some… by some component, and he had some ideas, because he was talking with the… I don't know, add colleagues of his.
And we will… we will see, we will then, I will then open a PR on… on some, on some components, repo, and, you know, integrating this, and see how it works. I mean, for now, the… the tests, of course, is synthetic data, and the tests seem to work.
Yep. But of course, you want to test with the real thing, and yeah, so…
Jeremy Blythe 00:12:14 So originally… so I'm looking at this now.
So where… where is the call to, to live check.
Is that in… Is that in the make file? No.
ariannavespri 00:12:32 Yeah, I don't remember enough, so I would love to see the code.
They're behind it.
Jeremy Blythe 00:12:38 I'll take a look. The thing is that, there's some fairly recent stuff, and we, I added this for… it was an issue that Miller raised, actually, because they were doing something, I think, in some… I don't know, I think it was some… one of the Python, The sort of… one of the Python bits of the SDK, I think. I can't remember exactly, but anyway, they were doing this… you can… So with Live Check, obviously, you can run it, and you can have the results sent to Standard Out, you can have them sent to a file, and then you can pick them up from the file. But you can also, when you stop Live Check, if you stop Live Check with the HTTP command, so you send, You just, you send a, I think, a post… maybe a post?
to, slash stop, you will then get the live check result back in the return payload from that HTTP call. So, that can save you a round trip to the file system if you're, going and getting the results from the file system, for example.
ariannavespri 00:13:47 Do you have, do you have, do you have the issue? Like, it's, like, is something, like, is… is there, like, an issue for this, or…
Jeremy Blythe 00:13:57 We… yeah, it's an issue, but it's been implemented now, and it was in the recent version, so I'm just wondering if you, If you saw that. Let me just see if I can find it.
It was in a recent release.
That's why I was just curious how your.
ariannavespri 00:14:15 Yes.
Jeremy Blythe 00:14:16 Because it might be a little bit smoother now if you're using the… So there were two things that came at the same time. Sorry, I'm a bit over the place. Let me… let me just get the release note, and then I can show you.
Really smooth.
I think it was in .21.
We did it.
Sorry.
I'll share my screen in a sec.
ariannavespri 00:14:41 Yes.
Jeremy Blythe 00:14:42 Dot 21… Oh no, it was in the latest, was it?
Sorry.
Find it now.
Okay, yeah, let me just share my screen.
Okay.
ariannavespri 00:15:12 I'm not…
Jeremy Blythe 00:15:13 Okay.
ariannavespri 00:15:14 Okay, now, now, now C, yes, no.
Jeremy Blythe 00:15:18 So in the 22.1 release, so the one that just came out.
ariannavespri 00:15:21 Yes.
Jeremy Blythe 00:15:22 So if you've been working… well, maybe you missed this one, but we added two things.
So if you're using the admin port, the first thing that's useful is there's this, health endpoint. So, if you go to the… what you can do in your… in your code is… You can, start live check.
On the… you know, by making a call out to the command line. And then, in your code, you can pull this, health endpoint. And that will return a 200… When it's ready for you to start sending data.
And then, when you're done, if you set, if you set output HTTP, And then you call stop.
On the admin port.
The report that would go in a file, or that would go to a standard out will be returned in that… in your… in response to the slash stop that you send.
ariannavespri 00:16:19 Okay.
Jeremy Blythe 00:16:19 That might make the process a little smoother and avoid… avoid the, having to go to, like, a temp file or something. Maybe.
ariannavespri 00:16:27 Hmm.
Jeremy Blythe 00:16:28 It depends. I think other people have… are using… I saw something that the team were doing who were doing this kind of thing, but for the GenAI, semantic conventions. They're doing some.
ariannavespri 00:16:39 Yes.
Jeremy Blythe 00:16:39 running a life check on it.
They're using the health in order to determine when it's ready, but they're still going to the file system, because I think they want a record in a file, and then they're reading that file back in. So they're, like, they're keeping the file for some purpose. So, it's up to you, but I just wondered if you were aware of that.
ariannavespri 00:16:57 Yeah, I mean, like, like, what we are doing with, with that PR is basically that, so Weaven, Weaver, like, runs as a So, it's a Docker container. Yeah. So, there's containers.
And, and so, yeah, and basically the command that gets executed is the… With a registry life check.
Jeremy Blythe 00:17:19 Yeah.
ariannavespri 00:17:20 Then we use, we use, FS Notify.
To watch the, You know, after we… after we call Weavers, the DM point, called stop, and then there is the output. And so, FSNotify, kind of, is the watcher for that output.
Jeremy Blythe 00:17:46 Okay.
ariannavespri 00:17:47 So, yeah, but this is interesting, I mean, I, like… Most of the work was done probably before this.
Yeah. So this is, it's pretty new. This is very… this is very… I will, I will have a look. There's been a lot of back and forth with… in preparation for KubeCon.
Yeah. And so, a lot of things, like, complete the… Might have slipped, you know, in the… In the Bronx.
Cool.
Jeremy Blythe 00:18:16 Yeah, no, this… it's super new, and it, like, it… it doesn't… it doesn't matter, like, really. I just… It might… it might make things a little smoother, maybe.
ariannavespri 00:18:27 Yes, yes, Absolutely. We were also, we were also, we were also, I think, I think Braden, at some point, mentioned the, the other new feature that I see here, the Amid OTLP logs.
Jeremy Blythe 00:18:48 Yep.
ariannavespri 00:18:50 And maybe… maybe we… we could have… we could have use for that as well in his vision, but as a… as a next step.
First, we have to really have this basic version, kind of validated.
by other maintainers and see if, you know, if, can be adopted as a gold package, basically. So, yeah.
Jeremy Blythe 00:19:12 That's cool.
That's great.
Yeah.
Alright.
Yeah, I've got your code, yeah, I'll take a look. Yeah.
ariannavespri 00:19:26 Yes.
Jeremy Blythe 00:19:28 So, maybe it's in here.
We've OTLP this import. Okay, maybe this is the unit where you may… Where do you do it?
ariannavespri 00:19:39 Yeah, then I still have to… I really had, like, a very quick look to the… to this, comments that I got.
Yeah. So, it seems to me, mostly… Mostly related to… To go idiomatic.
Stuff.
Jeremy Blythe 00:19:59 I'm not a Go person, so I…
ariannavespri 00:20:01 Okay, no, I am, or I'm supposed to be, at least, it's just that, Yeah, I mean, especially around the context, there were some decisions that were made, there's some reasons around it also, the legacy from Bradon, and… you know, I'm all for going idiomatic, but sometimes you have to… be, like… Sometimes, like, the idiom is not always, like, the highest priority, let's say, especially when it's, like, at this experimental level, but makes sense.
Jeremy Blythe 00:20:35 Yeah.
Oh, here you go, this is where you send the stop.
ariannavespri 00:20:39 Yeah.
Jeremy Blythe 00:20:42 And then… That's writing to a file.
Okay.
ariannavespri 00:20:47 Yes.
Jeremy Blythe 00:20:48 But you could. You could, instead of writing to the file and then reading the file.
You would get the response.
As the response to this.
To the stop command here.
ariannavespri 00:21:00 Okay, I'm taking notes.
Jeremy Blythe 00:21:06 Yeah, so this, I guess the resp… I don't know, go very well, but I guess this… the… the response body here would actually contain the live check report.
Which you can still have as JSON, or…
ariannavespri 00:21:20 Yes.
Jeremy Blythe 00:21:20 or YAML, or you can template it, or whatever it is you want to do, but… You would just get it back in the response, and then… You don't have to kind of go to the file system.
But if you've done all of that, I mean, it doesn't really matter, and it's in a container anyway, I guess, like, it doesn't… It's not a big deal, it's just a…
ariannavespri 00:21:39 But it's good to know, I'm taking notes.
Jeremy Blythe 00:21:46 And I've done this… I've got a PR where I'm using… we have a… to live… like, weave it to live check itself. It's kind of a dog food thing, and I do that in that, but that's all written in Rust, but you can take a look there as well if you want to see.
ariannavespri 00:22:04 Yes, yes, please.
Jeremy Blythe 00:22:05 That's a PR. Can you share it?
Yeah, that's a PR I've got open at the moment. Where are we here? Releases, let's go.
ariannavespri 00:22:18 What, what would be your, your, like, historically, your main language?
Your main programming.
Jeremy Blythe 00:22:23 Oh, me? Yeah. Oh, I'm really old. I, I, I did, Pascal, then I did Java for years, then I did, Python for years, and now everything I do is Rust.
That's…
ariannavespri 00:22:37 That's really, really cool.
I mean, I am not… I'm not super young, but I've started into this career relatively recently, just 8 years ago, so that's why.
I… I can say I started with Go.
Jeremy Blythe 00:22:53 Yeah. I know lots of people love Go, and there's a guy… On my team, who does, like.
tons of stuff in Rust, and then he still reaches for Go to do some things, so I think it's a good language for, It's good to… Language to have, amongst other things, you know, when… depending on what you're reaching for.
ariannavespri 00:23:16 Yes, I mean, it's, it's compact, you know, it's practical.
Jeremy Blythe 00:23:20 Portugal?
ariannavespri 00:23:21 And, but, definitely Rust is, the thing that I… I want to… to learn and, better, like, learn, because I just… I mean, it's that… it's that thing that, I mean, it was on my… on my to-do list since… 2000… 2019.
Like, when I first bought a book and everything, and then with the fact that I never really used it for work or whatever, it was… like, I don't know how many times I started and how many times I just… Stopped.
So, that's also why I'm… I like being close to Weaver, because it's, you know, it forces me to… to not, to not… to not desist.
For, for the, I don't know, 100 times, or something.
Jeremy Blythe 00:24:11 Yeah.
Yeah, so it's in this PR… this is a giant PR that hasn't… hasn't, gone in yet.
ariannavespri 00:24:21 But this is something that you talked about already, like, 2 or 3 weeks ago, right?
Jeremy Blythe 00:24:25 Yeah. And there was, like, the… That scared people with the… too many things in the PR in one go, but anyway. So yeah, so in this… in this test.
so this is a point where I'm… Polling the health endpoint.
Until it's ready.
ariannavespri 00:24:46 Yes.
Jeremy Blythe 00:24:46 So then you know, okay, now is it… rather than having… Rather than just having a delay.
if you poll health, then you… because it's not… especially if you're reading your registry from somewhere that isn't local, you don't know, there could be, like, a delay on that call.
If you're going and pulling it from GitHub, for example.
ariannavespri 00:25:07 Yes.
Jeremy Blythe 00:25:08 Maybe one occasion in 5, it takes, you know, 10 seconds for some reason.
ariannavespri 00:25:14 Yes.
Jeremy Blythe 00:25:14 and you get a flaky test at that point. So, the polling the health endpoint's quite nice.
ariannavespri 00:25:19 Yes, absolutely. Yeah, that's what you would have, like, intesto single, instead of having, I don't know, 10 seconds sleep.
It's more efficient, otherwise you… you might… you might either… I mean, best case scenario, you basically, waste time.
Worst case scenario, you get flaky tests, because you don't get things in time.
Jeremy Blythe 00:25:42 And then, I don't know, a bunch of stuff happens, but it ends up calling this stop and collect.
Method, where it's going… it's calling stop.
But the response comes back. So I actually get… I get the response back.
And then that is returned in the string to wherever stop and collect is called, and… I can't quite remember where that is, but then it, Where is that? Yeah, so this is where we… this is where we launch the… this is where I launch the command.
You know.
Wait for the health endpoint.
Then… Send stuff.
Yes, this is running the tests that are emitting the OTLP.
And then… Make sure we flush.
ariannavespri 00:26:42 Yes.
Jeremy Blythe 00:26:44 Yeah, and then we do this bit where I call stop and collect, so that's gonna call the stop endpoint, get the report back here.
And then… We go on to validate the reports, and then there's a whole… there's stuff that I'm looking for specifically, so I want to make sure a few things. Maybe you've already done this, but if you look at the statistics, this coverage within… this is… this is a good one, to make sure you've got. So, you want to… you want to check that your… LiveCheck is going to report to you If it's… if your code that's under test has emitted, like, an attribute that doesn't exist, it's not in your registry, so you'll get a violation, that's great. But what about, What about, if your tests haven't exercised the entirety of your registry, so that's what gives you the… so that's what… what you want is for… and I'm testing it here.
Checking the coverages… is also zero in here, so here we go. So the coverage has to be… 1.
ariannavespri 00:28:00 Yeah, so it has to be, it has to be there, yeah.
Jeremy Blythe 00:28:03 Yeah, so what that means is that it means that not only have I not sent I haven't sent any attributes that I've not got in my registry, and I've also sent I've also made sure I've got full coverage.
ariannavespri 00:28:21 Cool coverage of everything, yes.
Jeremy Blythe 00:28:23 So that will show you if there's a deviation one way or the other, right? So I don't… Yes. So that's another thing to make sure you're checking.
ariannavespri 00:28:34 Yes, makes sense.
Jeremy Blythe 00:28:37 So basically, it all boils down to these, like, two assertions at the end. I must have no violations, and I must have 100% coverage.
ariannavespri 00:28:45 Yes?
That makes sense. So I don't remember exactly what the concerns were that Josh had, but that was about, like, I mean, that was, like, some 3 weeks ago, so probably in any case, you… You must have done work in the meantime, so the code that is today is not the code that was 3 weeks ago, right?
Jeremy Blythe 00:29:07 Yeah, I have updated this, Not this particular piece, this piece has stayed the same.
the issues we had with this PR were… Because it's… using itself to test itself, how do you use yourself if there's a bug? So if you haven't compiled correctly… You can't…
ariannavespri 00:29:25 kind of recursive argument, like, yeah.
Jeremy Blythe 00:29:29 So I… my… I changed this… PR so that it actually calls the latest Docker container version of Weaver.
ariannavespri 00:29:38 Okay.
Jeremy Blythe 00:29:39 to be the engine that's testing the new Weaver that you're trying to release.
So…
ariannavespri 00:29:47 Okay.
Jeremy Blythe 00:29:47 Basically, the previous build is testing the new build now.
ariannavespri 00:29:51 Yes.
Sort of, like, generational heritage from one… from one Father, yes.
Jeremy Blythe 00:30:01 I guess so, yeah.
ariannavespri 00:30:03 Makes sense. Makes sense.
Thank you for all the explanation.
Jeremy Blythe 00:30:10 No, it's fine. Maybe we should have a meeting, I don't know.
I always get a bit lost when there's no Josh, because he just does such a good job of, like, organizing everything.
ariannavespri 00:30:22 Yes, because, normally, normally 15 minutes, 15 minutes before the… At the beginning of the meeting, you can already see that he has already written all the items on the agenda.
Jeremy Blythe 00:30:37 Yeah.
ariannavespri 00:30:38 And, yeah, it kinda… We're a bit spoiled, I guess.
Jeremy Blythe 00:30:46 I don't know Is it like… I don't belong to any of the other OpenTelemetry, groups? Is it like that? Is there generally one person who kind of runs each one?
ariannavespri 00:30:59 I mean, yes and no, because I am… I'm part of this, and I'm part only of the Hotel Collector 6, the one that is North America, I guess, because there are many, depending on the… on the time zones.
And for me, that one is, like, the most practical in any case. Well, not today, because of summertime, it's too late, so today I won't make it. And, so… there are a couple… there are, like… Like, it's one person among a group of three, more or less, always.
But everybody writes their own, issues in the agenda previously.
Jeremy Blythe 00:31:41 Oh, okay.
ariannavespri 00:31:41 So, it's, yeah, you have to… do your stuff yourself more than… than in this. This is… this is more, like, grassroots, if you want. It's, like, also very small, whereas the… the hotel SIG meetings is, like, there's always a lot, lots and lots and lots and lots of people. I normally recognize, I don't know, 3… three, four phases. Now, now, well, let's say… Now, 3, 4, 5, because I met people at KubeCon. So there were a lot… there were lots of Americans also.
And, and so now I… you know, it's… I can really put, names to faces.
Or faces to names, whatever.
Jeremy Blythe 00:32:29 Was it a good show?
ariannavespri 00:32:31 Kubecon.
Jeremy Blythe 00:32:32 Yeah.
ariannavespri 00:32:33 It was amazing. It was, really, really, really, really cool. I mean, I was there for the European one also last year.
And I think this year we had 2,000 people more, so it was, like, around, 14,000.
Jeremy Blythe 00:32:50 Well…
ariannavespri 00:32:51 participants, and I think that the venue was better.
The food was definitely better, and I didn't manage to see a lot of talks, because I was on booth duty with my company. It was the first time that we had a booth, and since my company is super small, we are literally, like.
Without counting the… the founder, we have, like, 4 engineers, because we are, like, 8 people together.
So of course, You know, somebody had to be at the booth.
And so.
Jeremy Blythe 00:33:25 the week.
ariannavespri 00:33:26 We had very heavy shifts.
Jeremy Blythe 00:33:28 Like.
ariannavespri 00:33:28 4 to 6 hours a day. And then I had… I had a couple of, I had a small talk, for Prometheus, I had to do the talk about the project update on the first day, basically.
So you also have to prepare for that, even though it's basically, like, then a lightning talk, but… You're basically represented… representing the whole project, so you really want to get it right, so there was a lot of coordination work, even for 10 slides.
Just to make sure that I was selling the right things. Yeah. And then we had, together with another… with other maintainers, we had, this workshop at ContribFest, to, entice people, not only to contribute to Prometheus, but to review. Because, of course, nowadays, reviewing is… You know, the most, the most… where's the… the bottleneck is?
Jeremy Blythe 00:34:31 Yes, yes.
ariannavespri 00:34:32 And, and so, yes, and I think it was a very good experience, very, very good experience, and I think that's… like, having those kind of guidelines is really, really useful, because it's the kind of things that nobody really teaches you, and you have to otherwise, learn by yourself, like, Hitting the ground running, pretty much, if you can.
or really, building, expertise about and knowledge about the code base, but it's not something that you do overnight, right? So… So I think that was a really, a really nice angle.
And So yeah, it was really, really good, just physically, objectively, a bit, a bit tiring. I could feel it, I could… I can still feel it, so…
Jeremy Blythe 00:35:28 Yeah.
ariannavespri 00:35:29 But super nice, and super… A very nice way of, of listening to people, what their pain points are, what their points of view on observability is, and also I… hello, and I also met Lyudmila… Lyudmila in person for the first time, so…
Jeremy Blythe 00:35:49 I missed out on that myself, with the US one, but yeah.
Hey, Lamila.
Liudmila Molkova 00:35:58 Hey.
ariannavespri 00:35:58 Yeah, we're talking about KubeCon.
Liudmila Molkova 00:36:00 Yeah, Jeremy, you should finally make it to the Salt Lake City next year.
Sorry, this year.
ariannavespri 00:36:06 You see ya.
Jeremy Blythe 00:36:08 Yeah, I don't know.
Liudmila Molkova 00:36:11 That's sweet.
Jeremy Blythe 00:36:12 I'll see.
Liudmila Molkova 00:36:15 So actually, Weaver was… One of the highlights, people who are interested, we… We had to seek office hours. Adrena, did you join?
ariannavespri 00:36:27 I was on booth duty.
Liudmila Molkova 00:36:28 Oh, right, yeah.
So…
ariannavespri 00:36:32 As you know, we are, like, 8 people, so we were 6, and somebody had to be there.
Liudmila Molkova 00:36:38 Yeah, I understand.
But yeah, we didn't have a lot of people interested, like, Arthur was there.
R… They gave a talk, I didn't have a chance, I was on a bus duty to go, but people were talking about the talk.
And people were very interested. Oh, Austin was showing the demo of MCP Server in Weaver, and showing the demo of Weaver in a hotel bus.
I think all.
Jeremy Blythe 00:37:07 I'm…
Liudmila Molkova 00:37:08 the day. Yeah.
Jeremy Blythe 00:37:10 My little MCP server.
Liudmila Molkova 00:37:12 Yeah! There was a Claude who was running, doing stuff through the MCP server, doing some instrumentation, fixing some stuff and whatnot.
It was cool.
We had, some interest from some employee from Google. They have their schemas described in, you can guess, Proto, and they were interested in what, how we can approach, like, the, Weaver for their proto schemas, and how to stop reinventing the wheel, and we talked about Proto to YAML compiler that would then turn it into semantic conventions.
Jeremy Blythe 00:37:51 Bun.
Yeah, I've been using the MC… actually, I've got a couple… one of the things I wanted to bring up was I have… So I've been building for my work.
a, A skill to help the application teams.
So, it's, it uses the Weaver MTP, So what the skill does is it, it's called the CheckSemConf skill, and it… it… looks at your codebase and tries to figure out, okay, you're Java, then you're probably… I'm looking for things that are… So that's how it starts. Oh, it's a Java app. Okay, I'm gonna look for where the OpenTelemetry SDK is. Now I'm gonna… and it starts sort of crawling all over the application, looking for things that are hints of, oh, look, they're adding a span, or an attrib… or, like, here's things where, like, attributes are injected somehow, and whatever.
So it crawls the whole codebase, and then, And then for each one of those things, you then get a report that shows you this… In this file, on this line of code, you're using this attribute, and… And… So it collects all of that up, and it calls MCP… It calls the MCP server with a live check, so it's made that up as a sample. So it's… it looks at… it's crazy what it does, like… So, if you're sending… It would kind of make up what is a good example of data based on its understanding of the code around where the attribute is placed.
So then you get reasonably good, like, examples injected.
it passes that through LiveCheck, gets the report back, and then it uses a bunch of the searching in the MCP, To go and get the brief and the notes.
and compare that with the… compare that with the intention that it's gathered by the surrounding code of where the span of the attribute is, and go, like, yeah, is this actually a good match? Are you using a good attribute here to express what you're trying to express from your code?
Liudmila Molkova 00:40:01 This is a code review tool now.
Jeremy Blythe 00:40:03 It's… it's a… it's a code review that's, like… I'm trying to replace what I do when people go, hey, Jeremy, like, am I doing good telemetry here? And I have a look at their code. I'm going, well, maybe you should be using this, you should be using that. I'm trying to, like, replace myself.
with a skill.
But what I found with doing that is there are a couple of additions that I wanted to add to the MCP tool.
just based on iterating with it on this skill, I found out that, like, it really wants to… once it thinks it's found the right sort of namespace, like, you're talking about things to do with RPC, it just wants to know all of the RPC things.
So it's just a simple little search to go, you know, show me all of RPC.star sort of thing, so it's got a kind of, oh, these are all my things.
So that was one. And the other one is, live check, as we all know, can be very verbose in its response, which uses up a lot of context. So there's a kind of brief mode where it just gives you the findings back.
So it's just those two things. There's a PR in called MCP Editions that… then will help my skill. I'd love to get my skill out to my team.
And then… I don't know, but I think that… I think that skill could be something that… We could even release.
As well, somehow, if I make sure it doesn't have any sort of… Company-specific things in it.
Liudmila Molkova 00:41:32 You have the PR for it, yeah, I saw it, but I didn't have a chance to review.
Jeremy Blythe 00:41:38 That's what that's all about.
But it's, it's mind-blowing, really, what it's able to do. It's just… Just… It's just crazy, because it's… It's like… I got it so that once it understands the namespace, If you're… if the… person who's written the application has, like, invented a newer attribute, but they haven't registered it in… because this is what happens all the time in real life. They go like, oh, but I want an attribute that's like this, and they put it in their code, but it's not part of the registry.
Then it will critique what they've… got in their application. So, well, you should register this, but probably try… you should probably rename it to, like, this before you go and register it in the… in the, in the library.
It will suggest, oh, you know, this is… Yep.
Because it understands the namespace, it will be like, oh, you should put this… you should, yes, use this root level, but then put this bit in. Anyway, you have to play with it, see it. It's very cool.
Liudmila Molkova 00:42:46 You know, it reminds me, Tarask Nishar, if you know Tarask, I hope you do, he was playing with, LifeCheck for GenAI stuff, and he asked Claude to generate a bunch of use cases that trigger specific scenarios for, like, certain libraries to then later on, validate the telemetry they produce. Then you can… use Weaver… oh, sorry, MCP and Weaver, MCP, and AI to, like, find these places in the code that adds a certain telemetry, and you can write the coverage tests that, later on, you will check with LifeCheck.
Jeremy Blythe 00:43:25 Mad.
Liudmila Molkova 00:43:27 Yeah.
Jeremy Blythe 00:43:28 It's loops on loops on loops. It's all about the feedback, right? That's what it is.
Liudmila Molkova 00:43:33 Right. Oh.
Feedback and information, the grounded information, the short.
Jeremy Blythe 00:43:38 Sure.
Anyway, I was just saying how I… Feeling a bit lost without Josh, because he just takes care of everything for us, always.
And I don't know where he is.
So I don't really have much… we were just talking, really.
ariannavespri 00:43:59 Yes.
Liudmila Molkova 00:44:00 Yeah.
ariannavespri 00:44:05 I don't know if she saw my message, Ludmilo, but in any case, today, I finally… find the time to start on the, you know, on Ummah… Building on your branch, that you use for the demo in order to, to have, the DMD, templates, transferred into the packages, repo.
Since you, already, like, converted them to V2.
So I started working on that, on that issue, finally.
Liudmila Molkova 00:44:39 Oh, that's cool, that's awesome.
ariannavespri 00:44:41 Yes, yes.
Liudmila Molkova 00:44:41 We can use this time to, take a look at how the markdown looks like.
And we can… See, I think I modified your markdown slightly from the V1.
So maybe I can share my screen.
So, here is… what I've done, dear.
Sorry, I… For some reason, my normal tricks work.
So… This is… How metric looks like… I think it's slightly different from… Or was it? Forge… Wherever forge… I'm trying to find the place.
Where's the… Oh, templates, right.
Oh, we don't generate them. We… oh, we have observed output here somewhere, right?
ariannavespri 00:46:13 I wish we would…
Liudmila Molkova 00:46:17 She… This is.
ariannavespri 00:46:26 Yeah, I'm in a hotel room right now, so I don't really have the… I'm, like, on a very small screen, so I'm, like, literally with my eyes attached on the screen.
No latency.
Liudmila Molkova 00:46:36 Yeah, sorry.
ariannavespri 00:46:38 Yeah.
Liudmila Molkova 00:46:39 Sorry, this one's… let's see if we have it… Expected outputs… Metric… GTP… So, okay, yeah, this is what I've done, and I'm not married to my approach or yours, it's just what they've done was closer to what we have in… semantic conventions.
I'm sorry, I'm so slow today.
ariannavespri 00:47:20 My worries.
Liudmila Molkova 00:47:21 follow me.
I'm still recovering from the KubeCon stuff.
Okay, so this is Hollywood.
ariannavespri 00:47:29 I feel you.
Liudmila Molkova 00:47:29 Today?
ariannavespri 00:47:30 Yes.
Liudmila Molkova 00:47:31 And… and… So what I changed, I added a stability marker here.
I replaced it with just the text.
And, yeah, this is a list of attributes.
And if we look into something else… Maybe metrics… So our attributes.
Yes, this is the… Corinth one, this is what I've done here.
Yeah, the same stuff, just the marker.
Of stability here, and… I… think… It's just shorter. But anyway, so if you like yours better, let's go with yours.
ariannavespri 00:48:39 And then I'm…
Liudmila Molkova 00:48:40 et cetera.
ariannavespri 00:48:41 For me, it's… I mean, I have no strong opinions, I'm just taking notes, so I… I know where to… to look at, immediately.
And, yeah.
Thanks a lot for walking me through this.
Liudmila Molkova 00:48:58 Yeah, and I think I've done a bunch of, helpers.
Well, I've done, as Claude did, I've done a bunch of helpers to… Render things together.
Yeah, to… Minimize how we… use Ginger.
ariannavespri 00:49:24 Yeah, that's, that's good, for sure.
Liudmila Molkova 00:49:31 Yeah, by the way, since I have your attention, I've also played a lot with Python CodeGen.
Based on also Ginger templates. We don't need to do it right now, I think I have a draft PR open, I need to polish it, but, look what we can do.
So, this is generated.
This, let's say it's an exception.
It takes exception as the… parameter, like Python exception in this case.
And it generates the… Attributes for this exception.
Following semantic conventions, and hides all this ugly boilerplate.
For metrics, I go over and Further.
I create… class.
For the operation, for a specific metric.
I initialize it with all the things from SemConf, and then I have a type to record.
That has required parameters as required, like, non-required as optional, and so on.
And… it… is much easier than just passing a property bug. I was super excited about this. It's so easy now!
ariannavespri 00:50:57 Wow.
Jeremy Blythe 00:50:59 Yeah, that's really cool.
Liudmila Molkova 00:51:04 Yeah.
Cool, so I'll work on the, this part. I think there are some bugs here, and some of them are coming from, weird dependency resolution. You see, for example, this server port is literal string literal, and this is a constant, and this is because I don't include unreferenced or something.
So it generates only the things from this registry, but does not generate things from the semantic conventions Registry.
But anyway, this is… Pretty close.
Cool.
So, I'll take a look, Jeremy, at your PR, at Rena, if you have a… if you need any help with templates, let me know.
ariannavespri 00:51:58 Absolutely, I will let you know. Thank you.
Liudmila Molkova 00:52:01 Yeah, thanks. I had a small PR, I don't know if we want to… for Josh to approve it, I think Laurent approved it, Maybe, if, Jeremy, you're fine, you can merge it, it's just dogs.
Jeremy Blythe 00:52:20 Okay.
Liudmila Molkova 00:52:26 Okay, I'll… I think something changed. Okay, I'll work on this. I'll ping you once it's ready.
Jeremy Blythe 00:52:37 Yeah, sure, I'm a little behind on, So I'm looking after my puppy as well at the same time.
I'm a little behind on, approving some things. I think there's one for Arthur that… I need to look at as well.
Liudmila Molkova 00:52:52 Okay, so there isn't…
Jeremy Blythe 00:52:54 as a group, I think we seem to be getting a bit behind on… PRs, in general.
Because it's exciting to make things.
Liudmila Molkova 00:53:03 Exactly. Is there something… oh, there are some peers from Josh that I didn't review yet.
Jeremy Blythe 00:53:11 Yeah. But you have the power now, right? Because you're a maintainer now, right?
Liudmila Molkova 00:53:16 I… I'm not… I think Josh proposed it, but it never… Rent.
It never happened?
Jeremy Blythe 00:53:25 Not merged yet.
Liudmila Molkova 00:53:28 I can't merge, no.
Jeremy Blythe 00:53:31 Okay, well, we should fix that.
I don't know how to do that.
But if it was proposed, then…
Liudmila Molkova 00:53:38 Yeah, let's wait for Josh to come back, and yeah, he will do the motions.
Okay, so, anything… the source.
Stupid… Cool. Do you know what this one is, Jeremy?
OpenAPI support for V2 structs.
Jeremy Blythe 00:54:09 Let me have a look.
Liudmila Molkova 00:54:14 Oh, I, I'm, I'm not sharing, sorry.
ariannavespri 00:54:17 Nope.
Jeremy Blythe 00:54:19 Are you gonna shift?
Yeah, okay.
Open API for beta store.
Oh, I did see that. So… Yeah, I think I wanna find out what… What, Josh… Feels about that, because… Obviously, we have the JSON schema.
But you can use OpenAPI's version of schema.
To describe the same thing.
So…
Liudmila Molkova 00:55:00 Probably what this person does, they use Weaver as a library?
Because otherwise, how would they serve this resting point?
And then… I have so many questions.
Jeremy Blythe 00:55:21 I think this is the… The confusion you're feeling is the same confusion I was feeling, I think.
For this one. I'm not entirely across…
ariannavespri 00:55:33 Oh, do you…
Jeremy Blythe 00:55:34 Easily for it.
ariannavespri 00:55:36 Do you know why here he says that… That is, like, the non-hockey way of doing things.
like, Translate this, from the schemas, but this is the non-hockey way.
Jeremy Blythe 00:55:53 Because you can use the, You can use the crate that we already have generating the OpenAPI spec that we have for the API that's in Weaver.
You can use that So if you look at the code, you'll see that you just put these annotations above, just like you do for schemas.
You put these little annotations with the to schema.
And now you've got both flavors of how you… can make JSON schemas.
the OpenAPI one, and the JSON spec one.
So yeah, he's just… he's just included that.
ariannavespri 00:56:36 Okay.
Jeremy Blythe 00:56:37 That thing in there.
I mean, it's probably fine, and we… maybe we want to extend… what we do with OpenAPI deeper into the objects that we're returning in the… in our API, and so it probably is fine, but… I just feel like Josh has been in this piece… A lot.
the… I wanted his opinion, I think.
ariannavespri 00:57:08 Makes sense.
Liudmila Molkova 00:57:11 I'm leaving a comment that's for the other to share a bit more context so that we can… like, maybe Josh has it, maybe not, but it would be useful if the person shares it.
Jeremy Blythe 00:57:22 Hmm.
Liudmila Molkova 00:57:26 So I'm going to ask if they're using Weaver as a library and serving just the models, or just clicked on the reason I understand how they can… where it can be important.
I don't know how you folks feel about it.
I would not take dependency on the waiver APIs at the moment.
Jeremy Blythe 00:57:50 No, no.
ariannavespri 00:57:51 Yeah, yeah, I wouldn't want them either, I mean…
Jeremy Blythe 00:57:59 It's, I think we still say that it's experimental in… when you've… When you, If you go dash dash help… I think it says that serve is experimental, which is the API serving the API, so… I hope… I hope it still does, anyway.
Certainly more.
Liudmila Molkova 00:58:19 We have version 0? And we didn't publish, like, what is… do we publish Weaver crates on…
Jeremy Blythe 00:58:26 No.
Liudmila Molkova 00:58:27 is their Centro package registry now? They just, I don't know, fork it and, sorry, not fork, but clone it and build it.
Jeremy Blythe 00:58:35 But in the… if you're running Weaver, serve.
You can go to the… you can go to an OpenAPI endpoint.
And it will return the OpenAPI spec to you.
So if you annotate this the way that he's annotated it in this PR, you will also get that back in that OpenAPI spec, if you hit the OpenAPI endpoint.
Liudmila Molkova 00:59:00 Right, for his service.
Jeremy Blythe 00:59:02 So you can… and then… and then he can use that spec in his service, yeah.
But yeah, I think it'd be good to find out what… What the heck they doing?
ariannavespri 00:59:16 Yeah, that's always a problem when you, when you review other people's PR that are based on something that is not, like, an open issue.
Kind of actually understanding what the needs… where the need stems from, and what the context is that generated the need.
Jeremy Blythe 00:59:34 Yep.
Liudmila Molkova 00:59:48 A… Cool. So, we have one minute left. Great to see you both.
Jeremy Blythe 00:59:57 Yes.
ariannavespri 00:59:57 Good to see you, it was really great to see you in person, and yeah, maybe, maybe Jeremy should make it to KubeCon Europe, not only KubeCon America.
Jeremy Blythe 01:00:09 See, the one that I missed was… that I should have gone to was the one in London, because that'll be going back to my… Home country.
Liudmila Molkova 01:00:17 Oh!
ariannavespri 01:00:18 Oh, oh, now, okay, so… like, so I was writing the, like, the accent that I kind of…
Jeremy Blythe 01:00:27 Yes.
I'm a dual citizen of Canada.
So I, yes, I lived in England for… 35 years.
Oh.
ariannavespri 01:00:40 Wow.
Jeremy Blythe 01:00:41 So what?
ariannavespri 01:00:42 Just… just 35 years.
Jeremy Blythe 01:00:44 Yes, that's how old I am.
ariannavespri 01:00:48 Anyway…
Jeremy Blythe 01:00:49 Sorry.
Liudmila Molkova 01:00:49 I have to drop. Thank you all.
ariannavespri 01:00:51 Thank you so much.
Bye. Bye-bye. Thanks. Bye.
