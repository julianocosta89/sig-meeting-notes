SIG: Prometheus WG
Date: 2026-05-08
Duration: 70 minutes
Zoom Recording URL: https://zoom.us/rec/share/IyQVJ29LlfpxuZRKH055TAFuTx4eP52zJizrSTQVjsfZC2g-4q9vMuVxj3DJ_5iL.ut4z3D7uIE58t9Tj
============================================================

## Zoom Recording Transcript

Arthur Silva Sens 00:05:35 Hello.
krajo Krajcsovits 00:05:50 I'm on call, and… Just got the page, like, 5 minutes ago, so I might have to rerun.
Arthur Silva Sens 00:05:59 Okay.
Is David here?
David Ashpole 00:06:09 Sorry, I'm muted.
Hello.
I'm just, I forget that there's a cover over this, off camera.
Arthur Silva Sens 00:06:23 Should we start? I don't know who else is joining.
David Ashpole 00:06:30 Yep, we can just get started, and then maybe Owen or others will trickle in.
Arthur Silva Sens 00:06:45 So far, there are only two topics for myself, so feel free to add… If you have anything to talk about, First one is, the Yotel.net SDK maintainer.
Reached out, saying that he… wants to… to test?
the output that the Prometheus exporter Generates, and he was trying to do prompt tool metrics check.
And then he realized that it doesn't support open metrics at all. Not even the 1.0.
David Ashpole 00:07:33 Is there…
Arthur Silva Sens 00:07:33 So, yeah.
How are the other SDKs?
Testing this.
David Ashpole 00:07:40 I did, like, a manual audit of the spec language last time.
Like, you just look for all the shoulds and musts.
And, like, looked through their code and tried to figure out if they were following it.
I don't know.
It's a good question. The… The other thing we could do would be, if we… We could write a compliance test case.
Like, basically, a scrape.
Or a series of scrapes, if we want to do, like, And then… like, write an example in Go of, like, okay, so you're supposed to get a meter with this name and these attributes.
And then make a counter on it, right? And then, like, have a… kind of canonical… test case, basically. Kind of like the Prometheus compliance repo has.
We could just, like, write a… write one test.
And then write a… a description in English of Take a meter, do this, make a counter, increment it, increment it again.
Something that'll produce some consistent output, and then… They should be able to run against and produce that, like, text output. So that's one thing we could do if we wanted to, like, write a little test suite.
Arthur Silva Sens 00:09:11 Yeah, but how… How much work is that?
David Ashpole 00:09:16 I mean, so, typically.
like, the way that we verify spec compliance is by reading the text, right? So, we'll read the spec, look for all the normative statements, go through one by one, and make sure that they are Following them, right?
So that's typically how stability works, and the official process is something like.
a SIG requests an audit from the TC, and in this case, the TC would delegate that to our SIG, presumably.
And so one of us would be going through the .NET, and implementation and going, hmm, do they follow this? Do they follow that?
They follow that.
Hmm.
Arthur Silva Sens 00:10:04 Okay, okay, I, I f- I f- I think we are talking slightly different things.
a prompt to metrics check. It's like, it's… it's like a scrape, and verifies against, open metrics.
It's not about spec compliance, it's just the output is correct.
David Ashpole 00:10:27 Is .NET… did they write their own…
Arthur Silva Sens 00:10:31 Yes, several… several hotel SDKs write their own permits exporters.
David Ashpole 00:10:38 Okay, we should… We should figure out why. I'm not… I'm not gonna… Awesome.
But…
Arthur Silva Sens 00:10:48 There are no official .NET Prometus clients, there are no official Rust, there are no official JS, there are no official… I don't know, several languages doesn't have a Prometus client.
David Ashpole 00:11:06 Do you think… Do you think Prometheus is interested in hosting?
an official… It doesn't even have to be an official client for those languages.
But even just… The protobuf to… All the various… even just, like, a thing that handles content… content negotiation and translates from the protobuf to the… Text format.
Do you get, like, you know the stuff in Go that's, like, in… Prometheus, model… model? Is that where it is?
like…
Arthur Silva Sens 00:11:49 I don't think the group would be against it, like, there's nothing wrong about this, it's just, like… Nobody would need to do it, and it's probably us.
David Ashpole 00:11:59 Yeah, well, so, okay. Like, here's my thought, which is… Well, let's… let's see, I'll start with, like, my worries, right, which is that they're gonna write this thing.
Oh, Cryo has his hand up. I'll let Cryo talk first, and then I can… I'm sure we all have maybe some ideas.
krajo Krajcsovits 00:12:15 Yeah, we talked about… Posting… kind of… or making official instrumentation libraries at the Dev Summit in Amsterdam.
I don't remember the details, but it should be recorded in the Dev Summit doc.
Nope.
So, Richie has the… had, obviously, like, opinions on it, so… You could ask him, he probably remembers better, but it should be in the dev summit, though.
David Ashpole 00:12:48 Mute.
krajo Krajcsovits 00:12:52 And I ran… the… What is it?
Yeah, Claude on prompt 2, and it says that… We're not using the internal parser.
Or checking metrics, but some external bars are… what?
I don't know.
David Ashpole 00:13:22 see anything.
krajo Krajcsovits 00:13:25 I'm sorry, the meat person. That was, like… Well, that works.
It was about the Swift, I think.
David Ashpole 00:13:36 Hmm.
I think Hotel Swift is just getting going.
Arthur Silva Sens 00:13:44 Yeah, yeah, I remember this. The Swift team has created a Swift Prometheus library, and they are… they want Prometus to call this official Swift SDK.
David Ashpole 00:14:02 Yeah, I mean… Like, my… I… I want to make sure, I guess, like, my thinking is, I want to make sure that Prometheus owns… The parts of this… that Prometheus needs to be able to evolve in the future, if that's at all possible. So, like.
If, like, today there's… They are probably just writing The text format directly to… Or they're probably just writing the text format directly. So if they want to support, for example, OpenMetrics 2, we would need to go into .NET, the hotel.net Prometheus exporter, and implement it.
It feels like it would be… It would be ideal if there was at least the library to go from the protobuf format Which is kind of like the… like, the… I guess it's like the, the broader… the broadest… Prometheus-supported one? I don't know.
that's how Go works, right? Is everything writes to Protobuff, and then Protobuff gets translated into the various text formats or whatever. So… I just don't want… I don't like the idea of hotel owning this and not caring about it, and then it just becoming, like.
diverged from what actual Prometheus should do.
Or non-compliant in ways.
And, I would prefer if, like.
Because I know that people in Prometheus are going to care about Whether it's compliant.
An hotel's just gonna kinda care if it works.
It's like, I feel like it would be much better if… Even if it was just a thin library that… Like… produce the text format correctly or something, that it lived somewhere in the Prometheus org, and even if the maintainers are the same, right?
I would rather we, like, welcome some of the hotel maintainers as… you know, temporary Prometheus.
People, if they're gonna be the ones implementing it, or something.
krajo Krajcsovits 00:16:12 So, wait, Sorry, I'm trying to look at two things at once. So, you say something in primatives, that thin thing that creates text format from Protobuff? Is that what you're…
David Ashpole 00:16:27 Yeah, I mean, that seems… like, that seems like the way that Go is modeled, right? Where the client library The Prometheus Client Library produces Protobuff.
And then there's a library that turns Protobuff into the various scrape formats.
Right?
krajo Krajcsovits 00:16:47 I mean… there's a… at least in Google, there's a detail, but I… Don't think that's… is that Protobuff?
I thought that was just handwritten.
And I'm confused that, like, That means forcing protobuf on whoever's trying to implement something.
In, in, like.NET.
David Ashpole 00:17:12 Does it force protobuf on them? I thought it just forces… they would only interact with the generated.
Is this the thing? So this is the protobuf. This is the protobuf, right?
The protobuf format.
krajo Krajcsovits 00:17:26 Yeah.
Arthur Silva Sens 00:17:26 Yes.
David Ashpole 00:17:27 Okay.
And then… There's a generated Go one. This is the DTO…
krajo Krajcsovits 00:17:33 Oh, this is the D2, okay, yeah.
David Ashpole 00:17:35 That everybody actually relies on. So this is client model, this is not… and then it's like in Prometheus… Common… And we have all the various encoders.
here.
Like… And these all rely on… the thing generated.
krajo Krajcsovits 00:17:58 Hold up.
David Ashpole 00:17:58 turn above.
krajo Krajcsovits 00:17:59 Okay, so the DTO is the… is the… Okay, so what, what are you saying, then?
David Ashpole 00:18:07 I'm just… all I'm trying to do is I'm trying to come up with an interface, between… an open telemetry all I want is an interface between the open telemetry Prometheus Exporters.
And… All of the var- and… a library.
in the Prometheus org that will do all of the content negotiation.
And support all of the formats properly.
And my initial… my initial proposal is that the protobuf format could be the… could be that interface, right? So you give this library the protobuf format, and then the library will handle open metrics 1 vs. 2 vs. text format versus protobuf format.
And it'll handle all the stuff that's done through content negotiation.
And that way, when we want to roll out the next thing, whatever it is.
As long as it's supported by the protobuf format.
It's easy enough for us to do.
And that… that seems safe, because that's how Go does it.
So that's… that's my hypothesis.
Arthur Silva Sens 00:19:22 I think this is a good goal to have.
And I think that we should work towards This, at some point in the future.
David Ashpole 00:19:32 Okay.
Arthur Silva Sens 00:19:33 I just… yeah, but I don't know if, like, how feasible that is.
Like, right now. Okay. Because we're stabilizing the… we're stabilize… we're trying to stabilize this pack as soon as possible, and if we block on this huge new project that's gonna take, I don't know, a year.
David Ashpole 00:19:52 No, no, I don't… we shouldn't block the spec on this.
It's more… should we, for the people in .NET, Should we try and connect them with someone like Richie?
Or whoever else is gonna care about this.
And see if they're interested in… moving the Prometheus-specific logic into a Prometheus-owned repo. That's it. So that's, for me, the question.
Arthur Silva Sens 00:20:24 I'm interested. I would be down to help.
but yeah, I'm a little bit afraid that it's just gonna be you and me, David.
David Ashpole 00:20:35 It's just gonna be a can of worms and just us? Okay.
Arthur Silva Sens 00:20:38 But but let's try it. Let's talk to Ricci, let's talk.
David Ashpole 00:20:41 Beautiful.
Arthur Silva Sens 00:20:42 there's…
David Ashpole 00:20:42 Do you know who from, .NET is?
Let me…
Arthur Silva Sens 00:20:48 Dana?
David Ashpole 00:20:49 Is it just…
Arthur Silva Sens 00:20:51 It's March…
David Ashpole 00:20:51 nature.
Arthur Silva Sens 00:20:52 It is the author of the PR that I have on the notes, Martin Costello.
David Ashpole 00:21:02 notes.
krajo Krajcsovits 00:21:04 can ask questions in the meantime.
Arthur Silva Sens 00:21:08 Yep.
krajo Krajcsovits 00:21:09 I'm just trying to understand. So… Someone would maybe do this PIN layer, but in all kinds of various languages, right?
Probably just… basically… AI coded, probably, because it's quite well-defined.
You have… you have the Protovac specification, you have the spec for text format, so you could… Auto-generate something.
And then somebody else, in, like, auto, boots… the… like, the… The business logic behind it, and writes to this… Protodorf.
basically writes to the DTO, and the thin layer exposes it.
So now we have… Soona… the instrumentation library is basically split into two. One is maintained by us, which is the thin layer, and then the Other part, which is the… I'm converting hotel internal crap into detail is… is… On the other side. It's on the other part.
Arthur Silva Sens 00:22:16 Yeah, yes.
krajo Krajcsovits 00:22:17 I think and I understand.
Arthur Silva Sens 00:22:26 That's how… that's how Go does it today.
David Ashpole 00:22:31 The… the objective would be that when Prometheus wants to make updates.
to the form… to any of the formats, right? Or introduce a new one, or… do whatever that… we… that there's someone in Prometheus that's… like, that there's a… we can actually just go through and update all of the thin layer libraries.
Like, if… like we did for UTF-8, right? Instead of having to be like, hey, hotel, like, we want to add this feature to your Prometheus exporter in .NET.
Which is probably, like, a more annoying… Process to try and go through.
I don't know.
Maybe that's not… Maybe that's not that important to…
Arthur Silva Sens 00:23:30 I… I can… I can talk with Martin, if he can… if… if he knows… Some automation that he can use in the… from the… for our client model, for… for .NET.
David Ashpole 00:23:47 This is someone from Grafana.
Not too.
Arthur Silva Sens 00:23:49 Yeah, yeah, he is.
David Ashpole 00:23:50 Well, I mean, maybe he has opinions, so actually, probably we should ask him what he wants.
Arthur Silva Sens 00:23:57 I… If Grafana, honestly.
David Ashpole 00:23:59 is gonna step up and maintain a lot of the Hotel Prometheus libraries anyways, then maybe there's not as much point.
Because, obviously, Grafana is very involved in Prometheus as well.
Arthur Silva Sens 00:24:12 I feel like he just wants… use SDK to be, like, a good citizen model, and implement the things. I don't think he has a strong, like… His team is not… not 100% interested in Prometus Exporter.
It's just his personal feelings about being a good citizen in Hotel.
David Ashpole 00:24:38 Okay.
Arthur Silva Sens 00:24:40 But I can talk to him and double-check.
David Ashpole 00:24:43 like, I think Java does something similar, right? So… Hotel Java reimplemented all of the… exposition formats.
I think.
It'd be interesting to look at how many how many, SIG's decided to do that.
Arthur Silva Sens 00:25:05 I know… from what I know, I've been talking with a lot of SDK maintainers, Rust doesn't want to use Even if it exists, because they want to be a dependency-free library.
David Ashpole 00:25:20 Hmm, okay, maybe… If… if that's, like, a common… if that's a common… like, yeah, I guess it's interesting, because… Maybe the… Oh, I remember, because Rust had an issue with… the upstream Prometheus one being marked unmaintained or something.
the Prometheus. Like, something happened to it, and they were like, never again. We're just doing this ourselves.
Arthur Silva Sens 00:25:48 Alright.
I mean, they… they… they could become maintainers of the Prometes bond.
David Ashpole 00:25:54 I know.
Arthur Silva Sens 00:25:55 Doing that on their side.
David Ashpole 00:25:56 I think they want to.
Maybe the conclusion is that it's actually just best for us to do our audits, and maybe write a test.
But it's good that they want to stabilize.
Arthur Silva Sens 00:26:10 And JavaScript and .NET, there are no official Prometus libraries.
David Ashpole 00:26:19 Okay.
Arthur Silva Sens 00:26:22 Swift… Maybe there will be, but right now there isn't.
But, let… Okay, action items here, shh.
Who and when should we be reached out about this idea?
Of, like, creating this thing libraries.
For all languages.
krajo Krajcsovits 00:26:54 I feel like this is the same kind of question of hosting Swift, so it's a Dev Summit question.
David Ashpole 00:27:01 Yes, I agree.
krajo Krajcsovits 00:27:02 If you ask anyone, they will just say that, bring it up on the Dev Summit.
Arthur Silva Sens 00:27:07 Alright.
krajo Krajcsovits 00:27:07 I feel like this could be a very good exercise in how easy it is to do this with AI.
I'm sorry, LLM, there is no AI. But, like, Because… it's… I'm sure the first thing will be, okay, who's going to maintain it, but… if Is there a way to fully automate it, basically? That's my question.
Oh, how… That would be high goal, too.
Arthur Silva Sens 00:27:35 The LLMs are super, super good at implementing when the documentation is well written.
And this pack is great for this.
Like, we've been… I saw David doing some PRs, and I tried myself as well, just… Point a codebase to the spec and say, please fix, versus, like, some really stupid prompt, and it nails it.
krajo Krajcsovits 00:28:02 I think… I feel like the primitives text format and the OpenMetrix 1 might not be well defined enough, because we haven't used LRMs there to verify internal consistency.
David Ashpole 00:28:15 It's actually quite easy if there's already an implementation, like the Go 1 to point.
krajo Krajcsovits 00:28:20 Yeah, that's true.
David Ashpole 00:28:20 they make this behaviorally identical, and it's just like, oh yeah, I can do that.
Arthur Silva Sens 00:28:26 I saw… you know how we have a Go library called OTLP Translator that translates names?
I… the Java SDK maintainer pointed their LLM to that codebase and said, please implement the same thing in Java.
And now they have an OTLP translated in Java.
krajo Krajcsovits 00:28:49 You don't have… you don't have to remove my vote, by the way, so copy-paste is good in this.
David Ashpole 00:29:03 Okay, cool. Oh, you're watching me right, that's right.
krajo Krajcsovits 00:29:05 Yeah, I'm not too much to do.
Oh, yeah.
And I'm scrutinizing your speed and accuracy, so…
David Ashpole 00:29:13 Because I'm using LLM, I can't type anymore.
krajo Krajcsovits 00:29:18 Oh yeah, the typos.
Arthur Silva Sens 00:29:24 Oh, no.
krajo Krajcsovits 00:29:25 I mean, I think one kind of obvious pushback will be, oh yeah, they might do this, but… What guarantees that they are… Following the semantics of the… of the matrix.
I guess… Oh, that's where the check comes in, right? That check that you said?
Right at counter, increase it, and should increase, and stuff like that.
David Ashpole 00:29:50 Well, so we… we are… we are responsible for that.
Regardless of this, this is more.
krajo Krajcsovits 00:29:55 Yeah, yeah.
David Ashpole 00:29:57 It makes me nervous that I will have to re-review A variety of implementations of people writing, like, Open bracket, whatever, close bracket.
type… like, that's what they're going to be writing, right?
The hard part of all these reviews is going to be making sure that they are outputting the characters and not, like.
whoops, there's a dot somewhere where there's not supposed to be, or like… I wouldn't… maybe the AI reviews will catch that, but…
krajo Krajcsovits 00:30:31 Hmm.
Arthur Silva Sens 00:30:39 Yeah, I think we are agreeing here. Let's discuss this on Dev Summit.
krajo Krajcsovits 00:30:47 I agree to discuss it on the website, I don't know if it's a good idea, but…
Arthur Silva Sens 00:30:50 Oh, okay.
krajo Krajcsovits 00:30:53 I mean, it makes sense, but, yeah, splitting things into… I don't know.
I don't know, it's… I guess, you know, whatever… It's the option where… the… a lot of the work that I put into Provitus is not lost, and it's not… Ew.
Killed off by Otto.
That's my personal agenda.
Arthur Silva Sens 00:31:33 A lot of your work is killed by hotel.
krajo Krajcsovits 00:31:35 No, no, I'm, I'm like, you know… I… I want to support, you know, things that mean that from ausc… Around for a little bit more.
And not killed off completely by auto.
So…
David Ashpole 00:31:55 I mean, I suppose the alternative is to… like, I'm proposing thin clients for these languages, because they're not supported by Premium. Like, the alternative is, like, real clients, and maybe… maybe LLMs are good enough that they could just write a real client, and then… People don't have to use meters and whatever else, people find distasteful.
God.
krajo Krajcsovits 00:32:19 Yeah, I mean, there was another discussion that… you know, the Autel SDK isn't… Termly.
performant, so… It might… Makes sense for it to… introduce some more prominus-like way of working.
And on the metric side, at least.
So… This might be actually a way towards That? I don't know. Richie has much more context on this, for sure.
David Ashpole 00:32:59 I complete… what is this?
Is this… Oh, this is… wait, why is this… Is this the right issue? I thought he was working on .NET.
Arthur Silva Sens 00:33:12 He is working on .NET, and he wants to use Promptu Metrics Check.
David Ashpole 00:33:17 Oh, that's why it's an open metro.
Arthur Silva Sens 00:33:18 Yes.
David Ashpole 00:33:19 officer.
I see, I see. Okay.
So it's not motivated by this.
Arthur Silva Sens 00:33:24 He doesn't… he doesn't… he wouldn't need that.
if the Prometheus client… if .NET or Telo SDK use Prometheus SDK, and Prometheus SDK has the test.
krajo Krajcsovits 00:33:37 Yup.
There will be a question, where would you open it to sort, yeah.
But they would be their own.
repose, I guess, right?
Yeah, they need to be their own repos.
Arthur Silva Sens 00:36:33 Do they?
krajo Krajcsovits 00:36:36 Yeah, where else would you put it?
Arthur Silva Sens 00:36:41 In one repo, but…
krajo Krajcsovits 00:36:45 Yeah, I guess. I don't know, Yeah, I don't have experience with hosting multi-language repos, to be honest.
the most complicated I've seen was just some language plus TypeScript or JavaScript.
Arthur Silva Sens 00:37:16 Hey, should we move on?
krajo Krajcsovits 00:37:17 Yep.
Arthur Silva Sens 00:37:20 Okay, next one, one of my teammates was working on permitted receiver documentation, and she was asking me… hey, there is this metric that is on your README, I don't see in the code.
And then I was looking at the RETME, and there is a whole section that got merged and was totally vibe-coded.
And yeah, a lot of informations that are incorrect.
David Ashpole 00:37:52 I missed the one, apparently.
Arthur Silva Sens 00:37:54 That's fine, that's fine. I mean, I'll open up PR.
David Ashpole 00:37:58 Yeah, yeah, you can remove as much of it as you want.
It, like, it looked helpful to me.
And I didn't see anything wrong, but clearly, I should've… should have thrown an AI in it. That was before I just hit co-pilot for every PR that comes my way.
Arthur Silva Sens 00:38:17 Yeah, it is an old… very old PR, so our README is incorrect for, like, at least 10 releases.
David Ashpole 00:38:25 Great.
Arthur Silva Sens 00:38:25 Who, who reads… who reads documentation anyway?
krajo Krajcsovits 00:38:31 AI.
David Ashpole 00:38:31 Just LM started, yeah.
krajo Krajcsovits 00:38:33 Yeah.
Exactly.
Arthur Silva Sens 00:38:38 Okay, I'll open up PR, I'll delete all the wrong stuff.
Okay, cryo.
your topic.
krajo Krajcsovits 00:38:48 Yeah.
I guess you already know that, I'm working on… on turning the… various things that we had going on for metadata in Prometus into a new proposal now.
But… Be very strict in coming from requirements and use cases side, and not implementation.
And, but that's already… that's my main project for the next quarter. But then I told my manager that I don't have enough time on Tuesdays, which was my OSS day.
To go through promitu stuff and then open territory.
to the iPhone stuff.
So we agreed that I'll take Monday afternoons for open telemetry. So now I have dedicated time for things outside that project.
like, helping out with the stabilization, which I haven't been doing a lot in lately, but now I have, like, some… a couple of hours every week for sure to spend on it, because I can't tell Grafana to, you know.
I'm not working on that, I'm working on this.
So, I haven't seen a PR yet from… But I bought…
Arthur Silva Sens 00:40:04 Yeah, John.
krajo Krajcsovits 00:40:05 Jonathan? Jonathan?
Arthur Silva Sens 00:40:06 Yeah.
krajo Krajcsovits 00:40:06 So, I… Yeah, I'll reach out to him, and then I can just quickly write up the NHCB spec next Monday.
And then take it… and maybe… that shouldn't take that long, because we already have code, so I… my plan is to just, you know, ask LLM and then make it human.
And then, take on something else. I don't know which one should be the next one.
From the project board.
Arthur Silva Sens 00:40:39 There are a lot of… Items in the board that, like, we need to discuss before we commit?
Maybe we can use the remaining 20 minutes to discuss that?
krajo Krajcsovits 00:40:54 Yeah, yeah, let's do at least one that I can, like, you know, take on then.
David Ashpole 00:40:59 Yep, yep, let me bring it up. I keep forgetting that I'm… Okay, so the Prometheus receiver should be basically there.
But let me open all the boards.
krajo Krajcsovits 00:41:08 Yeah, that had that dropped metric issue that's still blocked, right?
David Ashpole 00:41:12 Yep.
Arthur Silva Sens 00:41:13 Yep.
David Ashpole 00:41:14 I'm not… I'm not losing sleep over that.
So we've got… Let's see, so this is the Prometheus Exporter, and this is the… What is this compatibility spec?
Arthur Silva Sens 00:41:35 So this is Prometheus 2OTLP. The only one left is the resource.
David Ashpole 00:41:40 Right, right, I think this is… Yes, so this is the one I have a PR out for.
krajo Krajcsovits 00:41:47 I guess you need a review done on that, right?
David Ashpole 00:41:50 Yeah, I think we were looking for… I think… did Arv respond? I don't know if I've looked at it yet.
Did we ever figure this out? I asked, and nobody said anything.
I'm gonna ignore it for now.
But yeah, if you want to take a look at, do you want me to ping it to you?
krajo Krajcsovits 00:42:12 Yeah, or put it into the docker, like…
David Ashpole 00:42:15 Yeah.
krajo Krajcsovits 00:42:16 a link, so that I know which I should look at.
David Ashpole 00:42:25 Okay. Okay. That's the resource, and then that's everything from this board.
Let's see, we already said these are workable, so if anyone wants to pick Summaries, exponential, you're doing.
krajo Krajcsovits 00:42:39 Oh, okay.
Yeah.
Arthur Silva Sens 00:42:47 can assign, because it needs to be at least 3 Azure in the report story.
krajo Krajcsovits 00:42:53 Yeah, that's one OKR for me to move up on the ladder in OpenTelementary as well, so… Hopefully I can.
B, triage, or whatever the next level is.
Arthur Silva Sens 00:43:04 Yeah.
David Ashpole 00:43:04 Remember?
You remember, right?
krajo Krajcsovits 00:43:06 I think I'm a member, because, yeah, I can review stuff, although I don't have approved rights, but I can… review and get automatic assigned stuff, so I'm kind of code owner.
David Ashpole 00:43:21 So there's, summaries, histograms, and exponential histograms. These are for the SDK ex… these are for the… OpenTelemetry to Prometheus exporters.
But this also applies to the Prometheus server's OTLP endpoint.
krajo Krajcsovits 00:43:38 Reach from?
David Ashpole 00:43:39 all of these. So these… everything that's OTLP to Prometheus applies to all of the exporters, and then also applies to the, Prometheus servers, OTLP endpoint.
krajo Krajcsovits 00:43:51 Okay, okay. Yeah, yeah. Yeah, yeah, I remember. I mean, yeah, we're always looking at this spec.
David Ashpole 00:43:57 exporter spec.
So, let's see.
I mean, this seems… I don't think this needs discussion.
I can't see how anyone would.
implement this.
Other than as a poll exporter.
Oh, there's more to this.
I guess it's kind of weird, cause it… Links to the… Compatibility.
Arthur Silva Sens 00:44:29 Yeah.
I, I think, I think Johanna was too granular.
David Ashpole 00:44:35 Oh, really? Did she open one for each sentence?
Arthur Silva Sens 00:44:38 Yes.
Yeah, yeah, she… she's very beginner in Prometheus, so I think she didn't understand much of the things that she did.
David Ashpole 00:45:11 Okay.
Since they're, It's fine.
Is there a blocked category?
Arthur Silva Sens 00:45:24 There's, relationships a little bit below.
David Ashpole 00:45:27 Oh, yeah, yeah.
blocked by… Nice.
Does that work?
It's blocked by one. Okay, cool.
Oops.
Resource attributes, that one's blocked.
That one's blocked.
Metric Exporter spec client libraries.
Okay, should use Prometheus Client Libraries.
Arthur Silva Sens 00:46:21 Yeah, we just talked about this.
David Ashpole 00:46:27 Okay, how many actually do that?
So this is… it's just… .NET and JavaScript. Let me bring the Dev Summit back up.
Arthur Silva Sens 00:46:42 No, like, if you look at the comments.
she says, yes, we use an official client library, like, for example, C++.
But it's not an official, like, yeah.
David Ashpole 00:46:55 Oh. Is that… I'm okay with that, I've heard the C++ one is okay…
Arthur Silva Sens 00:47:20 I, well.
I have no idea if it implements content negotiation, I have no idea if this implements open metrics text.
David Ashpole 00:47:31 Okay.
So, but the three that we would consider would be C++.NET, and JavaScript. I just wanted to add that to the Dev Summit.
Arthur Silva Sens 00:47:45 And rest.
David Ashpole 00:47:47 Addressed.
But it has to be dependency-less.
Okay, cool. Back to… back to this.
I mean, I think this guidance is correct.
Should we put the word official in here?
Or…
krajo Krajcsovits 00:48:40 That's for Prometus to decide, so I wouldn't.
On that list.
Arthur Silva Sens 00:48:46 What is the definition of official?
krajo Krajcsovits 00:48:49 Yeah, I wouldn't get into that. I mean, on that link, current lives, I think there's a list, and there's… Like, two categories, basically, if you look at that link.
David Ashpole 00:49:02 Which link?
krajo Krajcsovits 00:49:04 Oh, from this? Yeah, this one.
That one. I think you opened…
Arthur Silva Sens 00:49:10 This is the same page, yeah.
krajo Krajcsovits 00:49:11 Yeah, it doesn't say pitch.
Yeah, it has been… yeah. So… There you go. I don't think we need to…
David Ashpole 00:49:20 There's a Rust one.
Well, at least they rely on the correct one.
I assume we don't want… to offend.
Arthur Silva Sens 00:49:38 I think Prometheus should talk with maintainers of those libraries, and just onboard them into the organization.
David Ashpole 00:49:48 I'll put that down.
krajo Krajcsovits 00:49:51 Yeah, that should be, like, easier now, right?
Arthur Silva Sens 00:49:55 Yep.
krajo Krajcsovits 00:49:56 Although, I don't know what it means, like, in practice.
But that's, I guess, the steering committee issue.
David Ashpole 00:50:17 Okay.
It won't be, it might be a little bit controversial, but I… For this text here, do we have any problems with it? I feel like this is still correct.
Arthur Silva Sens 00:50:33 Yeah, it looks good to me.
David Ashpole 00:50:36 Okay.
Okay.
Version and format.
Regardless of whether a Prometheus content library is used, the Prometheus exporter must support this version of the text format.
Seems good.
Must not use.
It must not use open metrics per above. Good.
krajo Krajcsovits 00:51:43 enough.
David Ashpole 00:51:44 Or Prometheus thermal, right? Good.
Must not add explicit timestamps on metric points.
That seems… Let me… Is that also a must in open metrics?
Like, right now, I feel like it's a should-not in…
krajo Krajcsovits 00:52:09 Yeah, it should not be open metrics 1 and 2.
Arthur Silva Sens 00:52:13 Why, why the must then?
krajo Krajcsovits 00:52:15 I don't know.
David Ashpole 00:52:17 Yeah.
Arthur Silva Sens 00:52:21 Like, for example, CAdvisor… Can, like, depend on this.
David Ashpole 00:52:36 I mean, I feel like we should change it to should not.
I think we… yeah, we kept that in OpenMetrics, too.
krajo Krajcsovits 00:52:59 Yep.
David Ashpole 00:53:14 Next.
Default aggregation… I think there's already a PR out for this?
No.
Arthur Silva Sens 00:53:39 What the hell is an aggregation?
David Ashpole 00:53:43 This… so this, for example.
Would let you expose all of your histograms as counters instead, if you wanted to.
So aggregation is like histogram versus counter vs. gauge vs.
sorry, the aggregation is last value, I should say, right? So an aggregation is a thing that turns a series of measurements Into a data structure, like a histogram, or a counter, or a gauge.
Arthur Silva Sens 00:54:17 Got it.
David Ashpole 00:54:20 This is… I think this is correct.
It's a little weird. It's not particularly important.
It's… if… In most OpenTelemetry languages, you get this for free.
Because the… Prometheus Exporter is a manual… Metric reader.
Meaning it, like, gets the metrics from the SDK on demand.
Instead of on an interval.
And the manual metric reader has this functionality.
So it's sort of, like, impossible to implement.
Prometheus Exporter and OTEL without doing this.
Arthur Silva Sens 00:55:02 So… Should we even document this? Why not just delete?
David Ashpole 00:55:11 It's possible they're hiding it.
Let's… hmm…
Arthur Silva Sens 00:56:49 Feels like we are kind of leaking… Part of the other spec into this one.
David Ashpole 00:57:00 It may be that languages need to re-expose this to their users, but it should be trivial. It should be, like.
When you build the Prometheus exporter, you just take a thing and hand it to the manual reader that you build.
Arthur Silva Sens 00:57:14 Got it.
David Ashpole 00:57:46 I'm gonna leave it as discussion needed, just because it's not ready for, like, a spec PR. Oops, I did it again.
Resource attributes.
May offer config to add resource attributes as metric attributes.
By default, it can't do anything.
Should allow users to select which resource attributes to copy.
krajo Krajcsovits 00:58:23 Does it actually… like… The… the first sentence suggests Wait, where are I?
David Ashpole 00:58:32 Sorry, there you go.
krajo Krajcsovits 00:58:34 Yeah, so the first sentence suggests that you convert resource attributes to metric attributes, and then do the conversion to probatos.
Is… is… Do we want to say that, and… Does it matter?
Because the other option is to say that when you expose stuff, you put them on labels, but not turn them into metric attributes.
David Ashpole 00:58:58 Right, so I think you're right that we should probably say configuration to add Resource attributes as metric labels.
krajo Krajcsovits 00:59:08 Yeah, I know I'm nitpicking, but I don't know if it matters, but it sounds a little bit weird.
Arthur Silva Sens 00:59:18 I, I agree. It doesn't hurt.
krajo Krajcsovits 00:59:22 Yeah.
David Ashpole 00:59:25 The only thing… The only other thought I have is if we want to be more prescriptive.
Huh.
Arthur Silva Sens 00:59:32 Another thing that I thought was that in Prometheus, there is a promote resource attributes that is the same thing, but it's not rejects-based, it is… Like, a hard-coded… I agree.
David Ashpole 00:59:49 So it's only an include list, right?
Arthur Silva Sens 00:59:53 It is only include, exactly.
No, wait.
I think there are both, include and exclude, but they are not rejects.
David Ashpole 01:00:04 Sorry.
Oh, not regex?
Arthur Silva Sens 01:00:08 Yeah, the regular expression base.
David Ashpole 01:00:11 Yeah, yeah, I also don't know if it should be regular expression-based.
I would like if this was a little bit more… like, solidified, because I think in declarative config.
And in the Prometheus servers config, we'll want this to be… Is this what it's… Yeah, we should remove the width.
Let me just… Let me just, like, split this up.
So for this sentence.
How does the Prometheus one look?
Oops.
Remote resource attributes… Does that look better?
Arthur Silva Sens 01:02:17 Yep.
David Ashpole 01:02:29 That's fine.
Hit this.
That's what we want it to be named.
Do we care about changing the name? Do we care if it matches what Prometheus has?
Arthur Silva Sens 01:03:12 F?
I feel like consistency is good, but… We're not… we are not… but yeah, I'm not strong with Peter and Ada here, because it's gonna be a pain to… to, like, rename all… all the SDKs.
David Ashpole 01:03:28 resource constant goals. I feel like they all…
Arthur Silva Sens 01:03:40 And renaming the Prometus config is out of…
David Ashpole 01:03:45 Yeah.
Arthur Silva Sens 01:03:46 Out of discussion.
David Ashpole 01:03:52 Yeah.
Okay, we are out of time. There should be a good chunk of… actionable issues in the list from the exporter side. So.
Arthur Silva Sens 01:04:08 Yes.
David Ashpole 01:04:09 Maybe if we can each get one done in the next two weeks, or two, we'll be… A decent chunk there.
Arthur Silva Sens 01:04:17 Sounds good to me.
krajo Krajcsovits 01:04:19 Yep.
Arthur Silva Sens 01:04:20 Alright, thank you, bye-bye.
David Ashpole 01:04:22 Dip.
krajo Krajcsovits 01:04:23 Have a great weekend, bye-bye.
David Ashpole 01:04:27 Christine.
