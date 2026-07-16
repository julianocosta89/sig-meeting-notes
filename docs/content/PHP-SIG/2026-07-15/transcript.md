SIG: PHP SIG
Date: 2026-07-15
Duration: 34 minutes
============================================================

## Zoom Recording Transcript

**Sergey Kleyman** 00:32 Hello!
**Bob Strecansky** 00:33 Hello.
**Sergey Kleyman** 00:35 Hi, Bob, can you hear me?
Jacob.
Try a new microphone microphone.
**Bob Strecansky** 00:43 Nice. Which one did you pick?
**Sergey Kleyman** 00:46 I took Sennheiser, instead of keeping the old headphones just for the microphone, and trying just to… Keep one on the desk.
**Bob Strecansky** 00:55 Nice. Yeah, I have.
**Sergey Kleyman** 00:56 Synthesis or profile or something like that?
**Bob Strecansky** 00:58 Have fun, buddy.
**Sergey Kleyman** 00:59 Awesome.
so the microphone that you use is not on your headphones?
**Bob Strecansky** 01:04 - no.
**Sergey Kleyman** 01:05 How far that that microphone looks like pretty far from you. How far is it?
**Bob Strecansky** 01:09 Meter.
**Sergey Kleyman** 01:11 And it picks up quite well. Okay, interesting.
**Bob Strecansky** 01:14 Yeah, but.
**Sergey Kleyman** 01:14 I looked at all the modern microphones, but they kind of like all kind of like declared that you keep pretty close.
So what kind of microphone is that? What brand?
**Bob Strecansky** 01:26 The brand is called Blue Yeti.
**Sergey Kleyman** 01:30 Okay, I think I saw that. Is that, like, a directional, or omni, kind of, like, direction?
**Bob Strecansky** 01:35 It's a. Yeah, it's omni. It's omnidirectional. I bought it like during the pandemic. So I I haven't.
**Sergey Kleyman** 01:42 No.
**Bob Strecansky** 01:42 In a long time.
**Sergey Kleyman** 01:45 Hmm, interesting. So, despite meter distance.
First of all, thank you very much for For doing the conversion on the fly.
**Bob Strecansky** 01:55 Yeah, that's.
**Sergey Kleyman** 01:56 Does it fit?
**Bob Strecansky** 01:58 Yeah, I mean, we can see.
**Chris Lightfoot-Wild** 02:00 Hello?
**Sergey Kleyman** 02:02 I guess.
**Bob Strecansky** 02:02 Hello.
**Sergey Kleyman** 02:04 Wow! Looking much better, Chris. Last time I saw you were like full Monty.
was really bad back then. No, like 40 degrees.
**Chris Lightfoot-Wild** 02:11 Oh, yeah.
**Bob Strecansky** 02:13 Oh, okay.
**Chris Lightfoot-Wild** 02:14 I was wearing a different, more casual shirt.
**Bob Strecansky** 02:18 Oh, man, that's 40 degrees.
**Sergey Kleyman** 02:21 You probably don't have any air conditioning, right.
**Chris Lightfoot-Wild** 02:24 Yeah, no air conditioning here.
**Sergey Kleyman** 02:25 Mmhm. Okay.
**Chris Lightfoot-Wild** 02:27 Just the the windows.
**Bob Strecansky** 02:29 I will say that that is one of the only things that I think the USA has way better than any other place in the world, is there is nothing worse than a — or nothing better than a 40-degree day walking into a 15-degree building.
**Chris Lightfoot-Wild** 02:44 Mmhm.
**Sergey Kleyman** 02:46 I heard about Europeans using it as one of the justifications why you should not have air conditioning.
because of those drops in temperature, but, I don't know.
**Bob Strecansky** 02:54 You did.
You definitely can get, like, an… for lack of a better phrase, you can get, like, an air conditioning cold, where you, like, do that transition way too often, and then you start getting, like.
Sort of like, it feels like a cold because your body is just like, no, this is not what should be happening.
**Sergey Kleyman** 03:09 Even though fins like sauna, you suppose it's good for your health to jump directly out of sauna into the snow, so…
**Bob Strecansky** 03:16 Yo.
**Sergey Kleyman** 03:17 Like, something doesn't, doesn't adapt here. Either it's good for you or not.
**Bob Strecansky** 03:21 Yeah, I'm not sure.
Alright, let's get… let's get rockin'. Hal, you got a… an issue open.
That you wanna talk through?
**Pawel Filipczak** 03:34 We, so this is issue reported long time ago. It's about missing periodic exporting of the metrics.
**Bob Strecansky** 03:44 Okay.
**Pawel Filipczak** 03:45 So, maybe you can assign it to me, and because I'm on Matrix now, so maybe I'll just… try to implement that, and my plan is to enable the SDK to to… for the periodic reporting, and then implement the… interrupt function in the in the distro.
first, and then maybe in the… in the classic extension. I will… we will see. But I made a research, and it should be possible to… to handle that. If not, if it… if it will be hard to implement that in the classic.
Into eBay's.
**Bob Strecansky** 04:29 Yes.
**Sergey Kleyman** 04:31 You want to. You want to do it asynchronously. You want to interrupt the flow of application asynchronously, and try to create metrics.
**Pawel Filipczak** 04:38 Yes, yes. That's how it's described in the specs for other languages.
**Sergey Kleyman** 04:44 But you will try to keep it kind of like outside SDK, and then somehow convert it when you want to send it, or you can use SDK API while replicating?
**Pawel Filipczak** 04:55 Yes, yes, it will just see… the native will… will just interrupt, then… then… but on the… on the beginning of the request, SDK should register the… The… the… the trigger function, right? The… the… the closure… and then the native part will execute that it will make everything happen right export the metrics. Probably they will go back to the native.
To the, to the asynchronous sending, but if with the classic extension.
It will, it will build the, and it will trigger the, the metric collection, and then, And then it will send it synchronously, or put it into the queue and send on the request end, or whatever.
**Sergey Kleyman** 05:46 But do you think it's safe like to use? So essentially you will be calling like parts of SDK while maybe it was already, like essentially SDK might be, must be reentrant safe, right? It's kind of like reentrancy. In the middle of use of SDK, you kind of like essentially asynchronously calling to the different part of SDK.
**Pawel Filipczak** 06:07 Yes.
**Sergey Kleyman** 06:08 Technically, like, just imagine…
**Pawel Filipczak** 06:11 It, it, it works, it works exactly.
**Sergey Kleyman** 06:13 in consistent state, right? If you call to something else, you might encounter that some of it is in some kind of intermediate state.
**Pawel Filipczak** 06:20 But what? Which state? State?
**Sergey Kleyman** 06:23 I can throw you, like, example, you know, classic example that you give. Let's say you have double linked list, right? And then you updated one pointer, and you… before you updated second pointer, you're being re-entered, and now you're trying to access it, and obviously that list is not in consistent state.
So this is kind of like the class example. Why, like, how do you? Obviously, SDK doesn't use a double link list, right? So it's not relevant. But I'm saying, technically, let's say, if you have 2 fields, they might must be some.
**Pawel Filipczak** 06:48 Yeah, but I…
**Sergey Kleyman** 06:49 That's why I asked. I thought, I think in in in short spans we do something against that right. We try to keep it on native, but I don't remember.
**Pawel Filipczak** 06:59 So let me explain you. So maybe, so it will work exactly the same as inference spans. So, but it will just execute call to which you will execute metrics collection, right? Getting fetching metrics from the metric sources.
From the data sources. Of course, in some cases, if there is some coexistence between some components, it may lead into the problems, but… We are here to solve the problems, but, you know, it's difficult to do anything, do whatever we want to do without I guess not.
**Sergey Kleyman** 07:34 No, we can discuss that. I agree with you that technically it may be possible. By the way, I thought that inferred spans have employed some kind of like something in order to avoid that situation, but maybe I'm wrong. Okay, so I just wanted to raise the potential issue, but yeah, I agree with you that it can be worked around.
**Pawel Filipczak** 07:52 Yeah, so, of course, I don't have any… I wasn't thinking about any possible problems, but of course, it might be some… there might be, you know, some problems, maybe not. I don't know.
First, I would like to do some POC, and then… just… just try it out. I'm not sure about the… as I said, I'm not sure about the… the classic extension, so if it would be possible, I guess, yes, but… But first I would like to focus on the distro native implementation and and and then maybe maybe implement that in the in the old extension, too.
But in other case.
If there is a long running application like in laravel application.
And it's it can.
at least if I will expose some trigger function from the SDK, then it can call it, let's say, manually from the application to fetch the metrics and send them out. Now, everything is only done on the request end.
So when the application ends, I mean that when the PHP process ends and there is a request shutdown code.
So… It will make some difference.
**Sergey Kleyman** 09:15 So the main difference will be that we don't want to buffer metrics. Is it because we don't want to store them to, like, memory? Or is it if application crashes? Like, what is the main…
**Pawel Filipczak** 09:24 So the so the main motivation is that if the application is running for for 2 h, you will get the metrics dump only once right on the on the on the end.
**Sergey Kleyman** 09:36 Okay, you're saying with… You're saying if we do sampling, so it's, we want to do more frequent sampling of the… some status, like CPU and stuff like that.
Yes. Is that… okay, I see. So it's not just about the storing, but also about the frequent sampling of the… of some kind of, like.
**Pawel Filipczak** 09:57 Yes.
**Sergey Kleyman** 10:01 Okay, interesting.
**Pawel Filipczak** 10:07 So yeah, that's what I would like to focus, and maybe it will be possible to implement that. Yeah.
That's that's that's mostly all from me.
**Bob Strecansky** 10:19 Cool.
**Pawel Filipczak** 10:21 Mmhm.
**Bob Strecansky** 10:24 All right.
Does anybody else have agenda topics that they'd like to talk through?
I wouldn't mind.
**Chris Lightfoot-Wild** 10:31 Throwing one on. Ish.
Like AI stuff.
Yeah, it looks like…
**Bob Strecansky** 10:38 Yep.
**Chris Lightfoot-Wild** 10:39 Yes.
**Sergey Kleyman** 10:39 So that's very specific. Can you be more broad?
**Chris Lightfoot-Wild** 10:42 No, it's very broad, isn't it? Yeah. Just looks like this is quite, I don't know, there's a suspicion that some of the contributions recently look very AI generated.
And I've even seen one of them that said, you know, By Claude.
And then even, like, some of the, you know, I'd sort of gone through anyway and commented on something, and even the response kind of felt a little robotic. But I don't know what the, I know in the community guidelines, there's some… Talk about Agentic sort of contribution, et cetera.
But then I've seen there's… there's Codex code reviews and stuff as well going on, I don't quite know, I guess, where the… Where it's heading in terms of like, should, are we more and more accepting of AI or should it not be?
Should there be more wording around it or?
Obviously, it's typically just like, oh, here's a PR for something, and it's like this really elaborate, long description of something, and there's no issue. Like, it always supports it.
**Pawel Filipczak** 11:45 Awesome.
**Bob Strecansky** 11:45 So damn.
**Pawel Filipczak** 11:45 Yeah, for descriptions. Yeah, we are using that to make descriptions and also sometimes it's translating comments so to To be more clear, this is because of the language barrier. So English is not my native language.
**Chris Lightfoot-Wild** 12:01 No, sorry, no, no, no, not, not using yourself.
**Pawel Filipczak** 12:03 No, no, no.
**Chris Lightfoot-Wild** 12:05 That'.
**Pawel Filipczak** 12:05 Some, some, yeah, yeah, I, I understand, but.
**Chris Lightfoot-Wild** 12:09 It wasn't for you. Sorry. There was I've seen some others.
**Pawel Filipczak** 12:12 I'm giving you my feedback, so what I am using it for. So definitely, it's helping me a lot.
with the descriptions, and sometimes they are too long, and people are just making copy-paste of the AI's descriptions, and they are… Overspoken.
Mostly, and…
**Chris Lightfoot-Wild** 12:36 Sorry, I've not even seen any of your… definitely wasn't me and you, I just meant some people that I'm less familiar with that… I'm not sure like it's even relevant as a contribution. I don't know where it sits kind of thing.
Sorry, I hope I didn't come off wrong.
**Sergey Kleyman** 12:52 If you look at the code, does it look okay, like the code itself? If you didn't know that there is such a thing as AI.
**Chris Lightfoot-Wild** 12:57 Well, this was it. There was some like questionable stuff going on.
**Sergey Kleyman** 13:01 Hmm, okay.
**Chris Lightfoot-Wild** 13:02 And I can put, maybe I can link to some of them in like the, sort of SIG.
Php chat. Is that done there?
**Sergey Kleyman** 13:09 Is the area completely new or something that already exists, like Laravel, something that…
**Chris Lightfoot-Wild** 13:14 It was across, like, various instrumentation, and then, like… I'll drop some links in, and we can sort of see, because it was more… again, it's like a… Not someone that's, like, done one or two Contributions are ramped up, so there's just suddenly a wave of them And it could just be someone that's really keen, or, you know, various people, but… Yeah, what… I'm just curious what the stance is, because obviously, like.
We're just going to be reviewing AI stuff all the time in our spare time as well. It's, like, overwhelming when there's The same going on in our work lives, presumably in like.
Yeah, okay.
**Bob Strecansky** 13:51 I think I think that from the Maintainer's discussions it's been I don't know, it's been… it feels like it's… the answer to that has been kind of wishy-washy. It's like You know, like, yes, we recognize that AI is becoming used more and more frequently.
Code review becomes a burden. So people then use automated code reviewers, which adds in even more complexity. Small nuances get missed. Things don't get tested correctly. Things don't get functionally tested. They're just like, oh, it passed the unit test.
Let's let it rip, you know?
I think… I think the right answer to it is we need to be… as reviewers and stewards of these repositories, we need to be good stewards of them, and we need to be conscientious that we will be getting review, code… we will be getting pull requests that are generated by a computer.
Period. End of sentence. Like, yeah, sure, now it says sent with Claude, or, you know, optimized with Codex, or whatever, but that doesn't necessarily mean that people have to do that. Like, you can easily remove that from the pull request.
I think the important thing that we need to focus on is, like, is the code syntactically correct? Like, will it cause problems?
And I'll be the first one to say, like, I've been using the Copilot reviewer as a first pass to give me some ideas whether or not a pull request is right or not, and then I'll review it myself after I do that.
But it's very easy to just not do that, right? So I think we just need to continue to try and be diligent and do what we can. If you see a point where it's egregious, just bring it up. We can always — if it gets to a point where it gets unmet.
even more burdensome or unmaintainable or whatever, then we can talk with Severin or the other TC or GC about it in the maintainer's meeting, but I think for right now, like.
Treat it as a PR that came in just from somebody.
**Sergey Kleyman** 15:59 Is there anything to give, like you said, Copilot, but I assume we can… maybe we can add to the repo some kind of, like, instructions? I don't know if they can be shared between all of them, like Claude, Copilot?
like you mentioned, like, make sure that it has enough code coverage with good tests or whatever. Like, I don't know what is going to be the false rate that it will complain, and then we'll have to also understand that complaint is not justified. But I was wondering, do you know if it's something useful that we can do if we… Already, it sounds like if other side's using this weapon, let's call it, that means that we'll have to use as well, right? We'll have to use it to help us with that.
**Bob Strecansky** 16:39 Yeah, you're difficult.
**Sergey Kleyman** 16:42 Mmm.
**Chris Lightfoot-Wild** 16:43 So that'll probably be like a robots.txt for a search engine, won't it? Like, the good ones might honor it, the other ones will.
**Sergey Kleyman** 16:49 Because I know there are these instructions that people give it to ClaudeMD or stuff like that, right?
**Bob Strecansky** 16:54 Yeah.
**Sergey Kleyman** 16:54 that you can tell.
**Bob Strecansky** 16:55 We have them in our repo.
**Sergey Kleyman** 16:58 Okay but so we can invoke but we can only invoke it it's not part of the CI so it's not there is no like comment that I can write or we can just tell it automatically so when you say you're using Copilot you invoke it separately or is it invoked automatically as when PR is opened and.
**Bob Strecansky** 17:15 So when you.
**Sergey Kleyman** 17:15 Magically added.
**Bob Strecansky** 17:16 When you go… when you go… when you go into a pull request in GitHub, like, for example, this one.
You can request a Copilot review here, and then Copilot will review it.
**Sergey Kleyman** 17:29 Oh, but only copilot. We don't have cloud.
**Bob Strecansky** 17:31 No, we don't have Claude there.
There is CNCF Quad licenses, I asked for one, and I've been waiting for, like, 3 months to get one, so I'm not gonna hold my breath, but…
**Sergey Kleyman** 17:42 But Copilot is good enough for our purposes? So let's say… let's say we're just specifically talking about Copilot.
do you think it's worth adding, maybe some kind of like instructions like, please make sure that they are as tests for the new features. Stuff like that. Is it something that copilot can really check with good, you know. Good rate.
**Bob Strecansky** 18:02 I've found the Copilot reviews to be… okay. I think, at least from my perspective as a reviewer and a maintainer of this repository.
Copilot gives you ideas of things where it might be wrong, but you'll still need to investigate them yourself. It's not… again, AI is not a be-all, end-all, but a lot of people really, treat it as one, right? Like, at my work, they're encouraging us to only use AI to write everything, which is disheartening. And it's, you know, it's one of those things you, like, you have to kind of get used to… a lot of, you know, we can't put all of our faith in these computers. We have to. It's trust, but verify. But that's it's easy to trust. It's hard to verify.
**Sergey Kleyman** 18:50 Right, no, I was just interested in maybe in your experience, like what is the signal noise ratio, right? Essentially, is adding Copilot will flag more issues, will turn out just waste of time, or is it like one to 10, right?
**Pawel Filipczak** 19:04 Okay.
**Sergey Kleyman** 19:04 9 issues that I… it's good that they were flagged, but one is, okay, waste of time, but it's good ratio.
**Pawel Filipczak** 19:11 Sergey, it depends. So I noticed that some AI generated code it contains a lot of shortcuts, and Copilot can find those shortcuts, let's say, and it can point to that. It might be a shortcut, something will stop working because of the change, so… but there are a lot of false positives.
issues there with the review. So you have to be careful and read what Copilot is trying to explain.
But, yeah, if it's sure that it stays that, it's quite sure that there is a problem, and sometimes it's just, let's say, mention that something may not work as expected, so…
**Sergey Kleyman** 19:57 When you say sure, do you mean you can enter into discussion with it? Can you kind of like… Yes, you can.
**Pawel Filipczak** 20:02 Yes, and you can ask us answer replies. You can paste the code and you can convince him or convince it that it works. So it's it's intended.
So, yeah.
**Sergey Kleyman** 20:17 Okay, interesting.
**Pawel Filipczak** 20:18 Okay.
**Sergey Kleyman** 20:19 Online.
**Bob Strecansky** 20:21 Yes, Chris, I feel your strife, too. I've seen PRs that are Obviously, AI generated, obviously incorrect. Obviously, you know, it's out of the next thing, and we just have to.
Be as diligent as it can.
**Chris Lightfoot-Wild** 20:36 It's like the concern is probably like To this point, it's mostly, well, very much a towel, they've been handcrafted, and, like, it's supposed to be a, like, a stable thing that, you know, is transparent, that you can plug it in, and it… observes the application, doesn't blow anything up, doesn't do funky stuff. Obviously, it's got its corner cases and bugs itself, no doubt, but… If we're just throwing AI at it, or people are throwing AI at it, and we're sort Willingly accepting it all without that much, like I say, due diligence, then it comes unstuck at some point.
Yep. There's a lot of reliant… things on the stability. Isn't that so?
**Bob Strecansky** 21:15 Very, very important. I think the other thing, too, we have to be conscientious with there is keep… keep the… as I was saying, trust but verify, we need to keep the guard up. It's… but just even underscores more how important our unit and integration tests need to be, and, you know, we don't have alerting here, so that's not really that big of a deal, but, like, in AI land, alerting is very important so that you can catch things we need to… There are a lot of, like, we may need to put more emphasis on the demo, the demo repository to make sure that our features and functionality don't break with new releases, you know, all these things.
**Chris Lightfoot-Wild** 21:55 Yep.
**Bob Strecansky** 21:58 Well, that's a perfect segue into releases. I'm finally to a place where we can do a release, I believe. I've merged in all of the, all of the open PRs that I think are reasonable to merge. I need to merge in some of the Renovate bot PRs, and then I will probably… I will most likely attempt a release today. I'm very much hoping that we can get this release out.
**Pawel Filipczak** 22:21 Cool.
**Bob Strecansky** 22:25 Excellent.
Alright, we don't have to walk the board today, because I've already walked it, like, 3 times, trying to find all the open PRs that we need to close.
Does anybody else have anything they'd like to discuss today?
**Chris Lightfoot-Wild** 22:41 Well, there was only one in there that… was for… Paul, did you see, Nivea had done a PR for metric stuff?
**Pawel Filipczak** 22:49 Yes, yeah.
**Chris Lightfoot-Wild** 22:50 But I couldn't tag you as a thing on it for some reason.
**Bob Strecansky** 22:55 Sort of like what just happened with me trying to tag him on that issue.
**Chris Lightfoot-Wild** 22:58 Yes.
**Bob Strecansky** 22:59 Was.
**Pawel Filipczak** 22:59 Spot loop, right?
**Bob Strecansky** 23:00 Oh, sorry.
**Pawel Filipczak** 23:01 It's a lot.
So I'll… I I I'm not sure about the naming. So it's he's changing the name from the from one to I mean the metric name.
or changing convention. I'm not sure if the Php. Uptime is is correct, or or it should be.
**Chris Lightfoot-Wild** 23:24 There's a, there's a different angle for it.
**Pawel Filipczak** 23:27 I mean… No, no, that's not the… not the one.
**Bob Strecansky** 23:31 Okay, there's sorry, a different one Which one? Let's just look for it.
**Pawel Filipczak** 23:36 Boom, boom.
**Chris Lightfoot-Wild** 23:37 the.
**Pawel Filipczak** 23:37 Add process paging faults.
This one.
**Chris Lightfoot-Wild** 23:46 So those not from semantic conventions, then, are they just…
**Pawel Filipczak** 23:49 Yeah, I'm.
**Chris Lightfoot-Wild** 23:51 I just made up once.
**Pawel Filipczak** 23:53 So here, in the description, it says process uptime, then it's changing it to PHP uptime. I think it should be process uptime, but… You know.
Maybe there is some mistake, but at least maybe I misunderstood something from the… From the… from the diff.
But in general, it looks good from my point of view, but he's suggesting to change it to… from the process uptime to php.uptime, so… Here.
**Bob Strecansky** 24:32 You you made a comment.
**Sergey Kleyman** 24:34 Hmm. Is this possible?
**Chris Lightfoot-Wild** 24:35 Oh, sorry. I didn't. I hadn't realized you'd reviewed it since I'd lost.
**Pawel Filipczak** 24:40 Mmhm.
**Sergey Kleyman** 24:41 There is a distinction between like process. And maybe he he wants to measure user land uptime like how much code. But I I assume the way you I mean.
**Pawel Filipczak** 24:51 Is it possible?
**Sergey Kleyman** 24:52 The way of the information that you obtain only measures when the user code is the user land is invoked, not native. I don't know if it makes a difference.
**Pawel Filipczak** 25:00 No, no.
**Sergey Kleyman** 25:01 People don't care much, they probably.
**Pawel Filipczak** 25:03 Prototype.
**Sergey Kleyman** 25:04 Yeah, okay.
**Pawel Filipczak** 25:05 You can't measure the user length. Of course, you can try to…
**Sergey Kleyman** 25:09 Yeah, I'm just thinking, like, why would anybody care? Like, if they're calling into native function, it still takes time from the applications. Okay, that's interesting.
**Bob Strecansky** 25:16 I'm I'm I'm gonna agree with you, pal. I think that it should probably be process uptime, because that's what the spec designates, and we really don't want to deviate from the spec when possible. it's just, I think this is a Small… a small semantic thing, but…
**Sergey Kleyman** 25:36 No, it's worth finding out why he thinks it should be PHP, because maybe he, for some reason, thinks that the information that is stored under this name is not what, like, from native point of view, we call the process of time.
**Pawel Filipczak** 25:48 But I looked into that and actually it is, it's a process of time, so it's a…
**Sergey Kleyman** 25:53 So maybe just misunderstanding.
**Pawel Filipczak** 25:55 Yeah.
**Chris Lightfoot-Wild** 25:57 Is there any, like, funky handling or something, if you're into, like… FPM, does that report a different Uptime itself or something like that.
I was just.
**Pawel Filipczak** 26:07 So…
**Chris Lightfoot-Wild** 26:08 Miss Norma.
**Pawel Filipczak** 26:10 So for the P… for the FPM, you can get the average process lifetime, right? So if you have a worker and there is a… If it depends how about it depends on the configuration. But if you set, for example, one day process lifetime.
Then you can get some average from that with the FPM, but it can be useful.
But it's still, it's not PHP specific metric, it's process OS metric, right?
So I guess it should be. It should be processed anyway.
**Sergey Kleyman** 26:50 Although this whole thing becomes kind of like an interesting case, like, what if you're using this thread-safe mode, and you're running multiple, essentially, runtimes in the same process?
Will it count all the threads and sum them up as a thread?
**Pawel Filipczak** 27:05 Oh, no, it will get the same value constantly. It will just report it more frequently for the same process, because it's the process.
**Sergey Kleyman** 27:15 No, but what is considered to be process uptime? If any of the threads was executing on any of the cores, then it counts toward the process uptime?
**Pawel Filipczak** 27:23 Process uptime is the diff between now and the time you started the process. It's a process.
**Sergey Kleyman** 27:29 Nothing to do how much you actually executed, it's just the difference in time, like the clock on the wall. So even if you were suspended on IO the whole time, it still will count in that time.
**Pawel Filipczak** 27:39 It's uptime of the process.
**Sergey Kleyman** 27:41 Okay. Like a uptime of the operating system, like when it was booted and until now? Yes. Okay, interesting.
Then, especially then, it's not clear why would PHP make any, like, why would they name it PHP, but whatever.
**Pawel Filipczak** 27:54 In other case, you have the system time and the user time in the…
**Sergey Kleyman** 27:59 -H.
**Pawel Filipczak** 28:00 You can measure that. And I guess I implemented that that you can.
or and context switches and other values, interesting values. But yes, this is just about how how long the process is alive.
**Sergey Kleyman** 28:15 Okay.
**Pawel Filipczak** 28:18 So how it is implemented right now without this suggestion, it's okay for me. But if you will decide to apply this suggestion, we have to update the README and so on because it's mentioned in other places.
Yep.
**Chris Lightfoot-Wild** 28:35 I mean, maybe he was on the fence with it himself. I guess why he committed it one way and then suggested the other.
Interesting to see if he, watches these videos and, We'll have some thoughts on it.
**Sergey Kleyman** 28:49 So that is a that's not a review of your Pr. Right? Your Pr. Is already merged. That's a kind of like additional on top of what is already exist. Okay.
**Bob Strecansky** 29:04 Cool.
Hopefully, we'll get some feedback from them there. Thank you for reviewing it.
**Chris Lightfoot-Wild** 29:14 There was one other thing. Sorry, Bob.
**Bob Strecansky** 29:16 Here, go ahead.
**Chris Lightfoot-Wild** 29:17 Be quick, the code owners in Contrib is set to PHP Maintenance Group instead of PHP… Contribent and his group.
**Bob Strecansky** 29:27 Oh, I see.
**Chris Lightfoot-Wild** 29:28 Are we okay to update this?
**Bob Strecansky** 29:31 Yeah. If you wanna update.
**Chris Lightfoot-Wild** 29:33 Like the Java thing and stuff, they've, they've divvied it out differently. And, I think the, the change that Severin did the other day, like the PHP sort of maintainers is still a sort of parent of.
the subgroups anyway, so you still get tagged as I understand it.
**Bob Strecansky** 29:48 Cool, works for me.
**Chris Lightfoot-Wild** 29:50 But then maybe in future, at some point, if Paolo's considering it, he could be part of that contrib group, and then we can tag… on the reviewer.
**Bob Strecansky** 30:03 Sounds like… sounds like a player to me.
**Pawel Filipczak** 30:06 makes sense.
**Chris Lightfoot-Wild** 30:09 Okay.
Awesome. How was that, sir.
**Bob Strecansky** 30:12 Oops.
Oh, I have one other thing. I will be missing the meeting next week. We are going on a family vacation for the week, so I will be away from my keyboard and out of the office.
**Chris Lightfoot-Wild** 30:22 Nice. Whereabouts are you.
**Bob Strecansky** 30:24 We're going to a very small town in rural Massachusetts.
**Chris Lightfoot-Wild** 30:31 Exce.
**Bob Strecansky** 30:32 I want to… Oscars Bay, Massachusetts.
Oh, thank you!
**Chris Lightfoot-Wild** 30:39 You've mentioned this before, Buzzards B.
**Bob Strecansky** 30:41 Yeah. So Cape Cod.
**Chris Lightfoot-Wild** 30:43 How firmly there was that you've got like some firmware.
**Bob Strecansky** 30:46 Yeah, yeah, that's right, my wife's extended family is all there.
**Chris Lightfoot-Wild** 30:50 Nice.
**Bob Strecansky** 30:52 So, this is Cape Cod, and then that's, like, the… No.
**Sergey Kleyman** 30:57 Is it close to Nantucket? Is there Nantucket somewhere there?
**Bob Strecansky** 31:00 Nantucket is a little bit further away, let me see.
**Sergey Kleyman** 31:02 Okay.
That's found at Melvin, right? White Whale, Nantucket?
**Bob Strecansky** 31:08 Nantucket stuff.
**Sergey Kleyman** 31:09 Yeah, by the way, okay.
**Bob Strecansky** 31:12 I will be eating some lobster and some ice cream, and not thinking about Php telemetry for a week, so it should be nice.
**Chris Lightfoot-Wild** 31:22 Nice. We're coming over to Florida again at Christmas.
**Bob Strecansky** 31:27 Oh, wonderful!
**Chris Lightfoot-Wild** 31:28 My wife just booked it the other day. She booked the flights, at least. We don't know. I think my father-in-law's coming as well. We may be considering not going to theme parks.
Maybe going somewhere with a bit more class, but
**Bob Strecansky** 31:42 Alright.
**Chris Lightfoot-Wild** 31:43 We're looking at Hutchinson Beach.
**Bob Strecansky** 31:46 I don't know it, but there's lots of good beaches in Florida. Is it on the Atlantic.
**Chris Lightfoot-Wild** 31:51 I think one tick. Oh, I don't.
**Bob Strecansky** 31:55 Yeah, you tend to want to go to the Gulf side of…
**Chris Lightfoot-Wild** 31:59 Or,
**Bob Strecansky** 32:01 What's that.
**Chris Lightfoot-Wild** 32:02 The warmer sea, the warmer side.
**Bob Strecansky** 32:04 Well, yeah, but, like, the beach, the sand there is whiter and the ocean is bluer on the Atlantic side. Like, I'm from the Atlantic side. The sand is, like, browner and the beach is, like, murkier most of the time.
So.
**Chris Lightfoot-Wild** 32:20 Nice.
**Sergey Kleyman** 32:20 But if you have been, like, I really recommend, there is this, is it Biscayne National Park? There is a nice national park close to Miami.
**Bob Strecansky** 32:28 Oh, you're talking about Key Bisc.
**Sergey Kleyman** 32:31 Which one?
**Bob Strecansky** 32:32 G. Biscayne.
**Sergey Kleyman** 32:34 No, I think it's called Biscayne. It's before the Keys, you don't need to go all the way to the Keys. Yes, obviously Keys are also very beautiful, but if you're just in the area of Miami, there is this… I think it's called Biscayne National Park.
it has areas where you can just, paddle on the paddle boat, and they have, like, a lot of, shallow areas where you can see all the kind of, like, really small, like, young fish, I wouldn't call them small, like, small sharks, small, kind of, like, they stay there, so they're not getting eaten alive, you know, much bigger depths, so they're trying to kind of, like, you know, grow.
**Chris Lightfoot-Wild** 33:08 Journals.
**Sergey Kleyman** 33:08 So yeah, those are mangrove trees, right? So they're kind of like running between those trees. So it's kind of like quite nice areas to paddle around.
Yeah, it should not be really hot during Christmas, I assume.
Probably quite nice.
**Chris Lightfoot-Wild** 33:22 I'll have to have a look out for that. And if you've got any more recommendations, let us know.
**Sergey Kleyman** 33:27 Obviously, the keys and the keys.
**Chris Lightfoot-Wild** 33:29 I've never been to the Keys, no, but…
**Sergey Kleyman** 33:32 If you get to the Keys, I really would recommend also going to the tour. I think it's called the Dry Tortugas Island.
**Bob Strecansky** 33:39 Yeah.
**Sergey Kleyman** 33:40 Something like that. You can see like 18 hundreds for there, and it's quite nice area to snorkel. Yeah.
**Bob Strecansky** 33:48 Key West is also a very, very big popular tourist destination.
**Chris Lightfoot-Wild** 33:54 Less.
**Bob Strecansky** 33:55 They have my favorite dessert in the world in Key West, Florida. It is… Are y'all familiar with Key Lime Pie? Is that a thing that y'all know?
**Sergey Kleyman** 34:05 This is how it's originated, that's why it's called Key Lime, because it's.
**Bob Strecansky** 34:10 So regular limes are, like, yay big. Key limes are, like, you know, a lot smaller, and they make a pie out of it that's, like, a custard style. It's so good. It's, like, very sweet.
But there's a restaurant that does that, freezes the pie, and then dips it in chocolate and puts it on a stick. So, like, you get, like, this stick that has you on pie dipped in chocolate. It is insane.
**Chris Lightfoot-Wild** 34:34 Sounds good.
**Bob Strecansky** 34:35 Like, that's peak American right there, for sure.
**Chris Lightfoot-Wild** 34:39 Sounds like it would come with a sparkler as well, just for, you know, the.
**Bob Strecansky** 34:43 It does. It comes with this part. And fireworks.
**Chris Lightfoot-Wild** 34:47 Absolutely.
Awesome.
**Bob Strecansky** 34:50 Well, we'll see y'all in 2 weeks.
**Chris Lightfoot-Wild** 34:53 Have a good week off. See you later.
**Bob Strecansky** 34:55 Dude, good job.
