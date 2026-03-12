SIG: PHP SIG
Date: 2025-11-05
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Chris Lightfoot-Wild** 00:25 Nope.
**Bob Strecansky** 00:27 How you doing?
**Chris Lightfoot-Wild** 00:28 Yeah, I'm okay, thanks for you?
**Bob Strecansky** 00:31 How you doing?
**Chris Lightfoot-Wild** 00:32 I'm okay, thanks here, how are you?
**Bob Strecansky** 00:35 Doing alright?
**Chris Lightfoot-Wild** 00:38 Nice.
sort of thing this morning online where there was some… I don't know what it was, but it popped up, and some guy who lived in Georgia, who was getting up at, like, half 4, and then threw in his, like, day in the life off. I kind of thought of you when it said people in Georgia tend to get up really early to get into work to beat the traffic.
**Bob Strecansky** 01:05 I think that's… I think that's true for a lot of non-tech workers. I found a lot of my coworkers do exactly the opposite. They don't… Leave their homes until, you know, 9.30 or 10.
To beat traffic on the other side.
**Sergey** 01:19 Yes.
**Chris Lightfoot-Wild** 01:21 Yeah, wild. Certainly good being able to work at home from time to time, isn't it?
**Bob Strecansky** 01:29 Yeah, so I live, like, Roughly 15 kilometers from my office.
And it can definitely… like, if I went at the wrong time, it would definitely take an hour and a half.
There was one… so, like, I don't know, what was that? Maybe 5 or 6 years ago? Halloween is a very, like, it's usually a very heavily trafficked day, and the traffic was so bad, I parked my car, like, 3 miles away from my house and walked the last little bit.
**Chris Lightfoot-Wild** 01:58 Wow.
**Bob Strecansky** 01:59 dropped a 5K home, just so I didn't have to sit in traffic anymore. I, like, rage-quit my dress.
**Chris Lightfoot-Wild** 02:05 I was like…
**Bob Strecansky** 02:07 I… my wife's name is Bree. I was like, Bree, take me… like, can you take me back to get my car later? She's like, why? Where is it? And I was like, I just walked home.
War.
I'm excited, I found out that I get to meet Severin in real life.
For… during the conference.
**Chris Lightfoot-Wild** 02:37 Oh, you're going to that KubeCon this year?
**Bob Strecansky** 02:39 Yeah, it's, it's actually image, like I said, it's like… I don't know, 5 minutes away from where my office is.
**Chris Lightfoot-Wild** 02:46 Whoa.
**Bob Strecansky** 02:48 So yes, I will be attending.
**Sergey** 02:56 How… is it, are you sponsored by your company, or how expensive is it?
**Bob Strecansky** 03:01 It is sponsored by our company, but I, like… here's, like, classic Fortune 500 stuff for you, like, we… I registered for it, because I knew I wanted to go, and then later I found a group of other people that were also registering, because they wanted to go.
And…
**Sergey** 03:17 But you don't get, like, the fact that you're a maintainer in, one of the… of the Cloud Foundation, how it's called?
**Bob Strecansky** 03:24 The spontane. The CNCF.
**Sergey** 03:27 They don't give any discounts for those people?
**Bob Strecansky** 03:30 You know, that surprised me. I thought, like, maintainers would be able to go for free, but I guess… I wonder if, like, the grouping of people that are both maintainers and work for big companies is to the point where they're like, the companies are just gonna pay for it anyway, we might as well get the cash.
**Sergey** 03:48 Yeah, it's possible, I guess.
**Bob Strecansky** 03:52 Alright, let's see… November 5th, isn't it?
So you're… this year just disappeared.
Alright…
**Chris Lightfoot-Wild** 04:13 I mean, bonfire night in the UK?
**Bob Strecansky** 04:16 Say that again? Say it again, Chris?
**Chris Lightfoot-Wild** 04:17 bonfire night.
**Bob Strecansky** 04:19 Bonfire night.
**Chris Lightfoot-Wild** 04:20 Is that, like…
**Bob Strecansky** 04:24 Is it a holiday, or is that just something you're doing? For fun?
**Chris Lightfoot-Wild** 04:27 Fun, but it's like, yeah, it's got some historic things to it. You can look it up if you want.
**Bob Strecansky** 04:34 Nice, I will… I will make sure to check it out.
Alright, does anybody have any agenda topics that they'd like to talk about today before we walk the boards?
Who knows is good news?
Alright, let's take a look.
The Pendabot and Renovate have been, very, very busy lately, and I have been going through them. I'll probably go do another pass today, because they, they've been updating a lot, which I guess is good, but… Oh, let's see… Send max… minute max histogram data, so this is a new PR, I will approve the workflow and review that later. I think that's the only open one that we have to… Assess.
Yee, yes.
**Sergey** 05:27 I guess it's just a matter of time until somebody will create a bot and just give it, give it to approve these NPRs, right?
**Bob Strecansky** 05:36 Yeah.
**Sergey** 05:36 It's just a matter of time. They will start… maybe they are in cahoots, like, they will create thousands of those PRs in just a matter of time, then you give in and just create… give it to another bot to approve them.
**Bob Strecansky** 05:48 Yeah, I think… so, I'm… I'm… that… yes, that is funny, and that is… like, that is an idea, but I… I have a tough time with this sometimes, because it's like, this is a lot… a lot of manual overhead work, and my opinion is, like.
If the package upgrade passes all of the CI tests effectively, then we probably shouldn't be that worried about it.
But that's not true for every repo, and some people are a lot more discerning about this than others, too, right? Like, some people will read the upstream commit with a five-tooth comb, make sure that everything's perfect, and then other people are like, oh, whatever, we all merge it.
**Sergey** 06:23 But if you limited… if you… this is what I meant, like, if you create a bot just to make sure that this PR is limited in its scope, only upgrading one of the versions, right? If that bot verified it, and like you said, all the tests passed.
Sounds like, there's nothing much that humans can contribute here.
**Bob Strecansky** 06:42 Yeah, I mean, I think there… it's not that there's not much that a human can contribute, it's just the overhead of that contribution would be too big, right? Like, for me to go and review some other third-party package to see if it has, you know, read it line by line and see if it has some vulnerability is very unlikely.
**Sergey** 06:59 Yeah, that's what you do, you go and check that version.
**Bob Strecansky** 07:01 No, no. No, no, I'm saying I don't do that, and, like, I'm saying that's the only thing you could really do, but, like, I'm… I know I'm not doing it, and I'm pretty sure that none of you are gonna do that either, so…
**Sergey** 07:11 But again, even that can be… Bart can do that as well, right? He can go to repos of the vulnerabilities and check that that package under that version is not listed yet. Even though I assume that PR that upgraded, maybe there was some time raised there.
After the upgrade, maybe something was discovered.
So…
**Bob Strecansky** 07:30 I mean, haven't.
**Sergey** 07:31 And bot is even better from a different point of view. Like, if you have dozens of this every day, like, the bot can just put them in the queue, let them slip there a little bit. Maybe something will be discovered, right? You can produce some kind of delay, and not being worried that those are just in the queue, and bot will take care of them after the delay.
after the quarantine period, that you just wait, like, 3 days, 5 days maybe, something will be discovered, and then Bud just approves it.
So… .
**Bob Strecansky** 07:59 Yes.
**Sergey** 07:59 I mean, it sounds like it's pretty mechanical, I wonder, like, who will be the first one that will just give the buds to do that.
**Bob Strecansky** 08:06 Yeah, I don't know, in the age of AI, I think that that is very likely that that will happen sooner rather than later, but… Like, that review… that review is done much better by a computer than it is done by a human, more than…
**Sergey** 08:20 Yeah, because the criteria that you just mentioned, that you apply, that fully… can fully be automated without even AI. It sounds like pretty mechanical steps that can be automated, right?
**Bob Strecansky** 08:30 Yeah, but you gotta sprinkle the AI sugar on top, or else you'll never get buy-in from the executives.
**Sergey** 08:35 Alright.
**Bob Strecansky** 08:37 Alright, I'll review this later. The… let's check the rest of the repos… contrib… Probably the… yep, Grint Trib is about the same. I prob… so, my goal… I guess I should be intentional in telling you all this, my goal is… to monitor both Dependabot and RenovateBot for a little bit, and I don't know what that little bit is yet, but I want to monitor our repos with that, make sure the changes are relatively similar, and then remove Dependabot, because Dependabot has been less dependable than RenovateBot has been.
Historically, so we'll see, that's my… that's my long-term intention. I just want to make sure that people knew that.
**Sergey** 09:14 What you gonna do if, if the Penderbat is gonna be more innovative or renovating than the other one?
**Bob Strecansky** 09:20 I… I think…
**Sergey** 09:22 That's…
**Bob Strecansky** 09:22 I think that's the problem, right? Like, we could leave these both going ad nauseam, but… it's probably smart to stick with one of them, and I want to make sure that the one that we choose is, like, the one that seems to be more… for lack of a better word, because it's not really quantifiable, it's reasonable? Like, that's, like, what we feel is… are closer to the right things, so… Anyway, alright, nothing crazy there.
Nothing in instrumentation except for updates, too. Wonderful.
Looks like no news, tech overflow questions… Looks like we're up to 23 million installs.
I think that's about all I got today. Y'all have anything else you want to talk about?
**Chris Lightfoot-Wild** 10:12 Did you have… I saw one PR in, the main repo, but it's maybe we're waiting on even Brett, but…
**Bob Strecansky** 10:20 Which one are you talking about, Chris?
**Chris Lightfoot-Wild** 10:23 the, what was it about now?
the SDK had been disabled during Composer.
**Bob Strecansky** 10:31 Yes. That was yours. It looks like… yeah, I thought that that was… that they were discussing this with you.
Hmm?
**Chris Lightfoot-Wild** 10:41 I kind of nudged on it last week, but, yeah.
It's not, like, an urgent rush or anything, just…
**Bob Strecansky** 10:56 Yeah.
**Chris Lightfoot-Wild** 10:56 So it goes more styled from where I leave it.
**Bob Strecansky** 10:59 Cool. Well, bumped it.
**Chris Lightfoot-Wild** 11:02 We'll hook it.
**Bob Strecansky** 11:03 Yep.
**Sergey** 11:06 Maybe I have one question for Chris, for you. Do you remember we discussed, maybe I can share if you want to see the context. Remember we discussed this issue with injecting the configuration source?
And, that was around time when the disability to use SPI for that was introduced. And I remember we encountered the fact that this is kind of, like, multiple sources for the… Oh, that class is, called, the one that… Exactly this time, the… this stopped work navigation.
So… There's this SDK… so essentially, remember we discussed it that there was kind of, like, two multiple, ways to read environment variables, and they were all a little bit different, so I was wondering… Because, I want to, kind of, like, redo the way we integrate with SDK to use this SPI, but I was wondering, what is the latest, kind of, like… So there is this one branch, I guess.
One branch of it is using this environment reader, right? And I think that's the newer one. And then there is a classical one called Resolver.
You remember something like that? And they… I think it's this one called Resolver… Something, right? There's, like, two… two alternative ways to read configuration. I was just wondering, which one is the… yeah. So, you see there's this interface to read configuration?
It kind of.
**Chris Lightfoot-Wild** 12:39 Oh my god.
**Sergey** 12:40 two methods to verify… to see. Should I make it bigger?
Presentation.
So, there is this, this interface, Resolver.
And it has two steps, right? You check, and then you read, and I guess there is, it can… the difference is that also it can return, I think, empty strings. You can distinguish between empty and non-existent using this has method. And then there is this other one that's called reader, right?
Which I think relies on, and reader.
This one only has one method.
And even though it returns, I guess it returns null , but then I saw that it actually checks if it's empty, then it can… oh, okay, I see, here.
So I guess, it doesn't. So I was wondering, those two seem to be somehow very similar, right? Do you remember… how they are different, and how they use the… Like, in what circumstances each one is used?
**Chris Lightfoot-Wild** 13:47 I thought it preferred to use the SDK configuration thing, and then the MV reader was one of the sources, maybe? I'll probably have to have a look and.
**Sergey** 13:57 It's the key configuration, you mean? This one?
**Chris Lightfoot-Wild** 14:01 If you go back to the… there's, like, that Resolver interface, is that the… or the end reader?
**Sergey** 14:05 The dissolver comes from… Okay, so this is…
**Chris Lightfoot-Wild** 14:08 Okay, so this is what the speculation.
**Sergey** 14:10 SDK configuration package.
**Chris Lightfoot-Wild** 14:12 Yeah, if you click on the left-hand side, on line 7, it shows you what implementations are.
**Sergey** 14:18 Okay.
**Chris Lightfoot-Wild** 14:19 SDK configuration resolver.
You look at that one.
**Sergey** 14:23 Yeah, okay. So this, yeah, so this is kind of like the ultimate thing that unifies all of them, right? It also brings the other ones that can be loaded via SPY, like Laravel and stuff, right?
**Chris Lightfoot-Wild** 14:36 Because I think… when I did this, there was some overlapping, like, on lines 33 and 34, there's, like, the server Mv source and phpinit Mv source, but there's already some, like, older ways of getting those as well, I think, isn't there?
**Sergey** 14:51 So this source, it's based on this reader, this is the later one. So if you look at the source, source essentially, I think, is this the… this is the INI, and environment… It's implemented… oh, okay. So there is also a source, so I guess we found the third one. So there's a reader.
**Chris Lightfoot-Wild** 15:10 This one… so…
**Sergey** 15:12 But then it converts it. No, eventually it converts it, so I guess it uses as a source this third one, but then it converts it back to this reader interface. So, a resolver, but reader… Please readily…
**Chris Lightfoot-Wild** 15:26 Probably with… I wouldn't mind, I can look at it again if you've got a…
**Sergey** 15:31 I guess, if I'm asking a practical question, not to bog you down, essentially, what do you say about… so my, my goal is to essentially… add additional source of configuration, let's say that came from remote configuration from some service, right? But I want to give, obviously, the chance to local configurations.
whatever they are, including Laravel and SNN, I want to fall back on them if remote doesn't bring anything, right? So would it be enough, then, to just use this class directly? So, essentially, I can register my, new I will implement Resolver interface, right? I will register as a new thing. I think it will come first, right? If we look at where Resolver is used, I think it's used in the… It's registered as SPI in the… in the Composer JSON, right? This is how it's been used.
**Chris Lightfoot-Wild** 16:29 Yep.
**Sergey** 16:30 In Compose a JSON of the… Of the, yeah, here.
But, if I… if I… essentially, so if I want to introduce a new one.
I do it via the… not the registry, but the other one, it's called Service Loader or something, right?
Let me see quickly how it… the NiveWe… I need to use the Neve package directly, right? I cannot use… because there was alternative way, but I didn't find, there is also this registry thing.
that I can use to, to register various, interfaces via here. Like, for example, I can register research detector.
And it will be used, but I didn't find for this resolver.
So I guess Resolver needs to be done on lower level, using this Neve package directly, right? How it's called Service Loader.
So, the way I found it, it might do it, let me quickly show you.
Sorry, let me exit.
So, because I didn't find a way to register resolver via this interface, so I… before, I tried it with this detector, and it worked. So, it seems that if I want to do it programmatically, not via the JSON configuration, I can use this registry class and register some interfaces directly from the code, right? If I… I couldn't use the JSON configure, Composer JSON, because at the time when plugin runs.
we didn't load our classes yet, so it was a little bit complicated, so I didn't want to investigate too much, so I just used directly this programmatic way to register… to register a service against the interface. But then I saw that it doesn't have a way to register this resolver.
So, what I did instead, I… I tried… I used another interface directly from Niveve, Let me find where I did it.
There was this, another interview, another thing.
that I, I think, maybe here.
Yeah, so there is this, hotel, this is Niveay service loader thing.
So, it seems to be… I don't know if it's present here in the presentation, but let's see if it, yeah. So, if I use this, I guess this one.
If I use this, and I can call register on this class, then it seems to work.
But I was not sure, like, what it will do with the… with already present, so it seems that there is no way to kind of, like, stand in line. Like, if I will register my implementation via this method, it will shadow, it will hide whatever was registered via the composer.json, right? So this class will not be loaded, like, if I… so there's no way for me to say, okay, load the next in sequence, right? So essentially, I want to fall back on this.
There is no way to do it other than just call it directly from my implementation, right?
Exactly like you did here, hmm?
**Chris Lightfoot-Wild** 19:36 Yeah, not specifying your own MV source provider as the… because that would be the first thing, but you're wanting it as the fallback, as the last thing.
**Sergey** 19:45 Well, I… no, I wanted to be the first thing.
I want it to be given the first, first night, privilege, right? So it needs to be… if it has an option, then it should take priority, but then if it doesn't, then it wants to fall back on this, on local source.
**Chris Lightfoot-Wild** 20:02 Yeah, I guess I'd need to double-check, but, like, the MSource provider there, if you were to register that in your package SPI.
**Sergey** 20:09 And then compare…
**Chris Lightfoot-Wild** 20:11 I guess the assumption is that that would be first, and then this dependency would register its after the fact.
**Sergey** 20:17 Yeah, you think when it scans those JSON files, it combines kind of, like, some kind of chain, and it will fall back on this, because it.
**Chris Lightfoot-Wild** 20:26 Yeah, you can register those things yourself, but it's just… I guess I just need to test how it, is supposed to stack them up.
Like, what order they get registered in? Because that's obviously…
**Sergey** 20:34 I don't want… but if I don't want to rely on that, sounds maybe a little bit, not 100%… I mean, I guess I can investigate, but if I don't want to rely on the… on this order, I can just, via my implementation, because it seems to me that when I register it like this.
then it will definitely not call all the rest. It will call only mine, right? Like, whatever it found during the scan.
Like, for example, what it found in this composer JSON, It will not call it, like, it will only call my implementation, right? Or… I should read this code.
**Chris Lightfoot-Wild** 21:09 do… I think it just appends them, doesn't it?
**Sergey** 21:12 Yeah, you think… so you think this, calling this register is essentially equivalent to the space defined in the SPI section in Composer.json?
**Chris Lightfoot-Wild** 21:20 Yeah, because I think that's what we'll be using in our, sort of, more traditional register functions, where we just call service loader register.
I see.
**Sergey** 21:28 Okay, I will check in.
**Chris Lightfoot-Wild** 21:30 Then Composer has a script that runs outside of, like, regular runtimes, and generates, like, a cached version of all this.
**Sergey** 21:37 Hmm.
**Chris Lightfoot-Wild** 21:38 So, I wouldn't mind… if you want to ping us that sort of question, I can, like, look at it.
I was like, damn.
**Sergey** 21:45 I will formulate a question better, because the first time, I went ahead and added my class like this, but it's a little bit finicky the way we do the loading. We can do it in two stages. First, we load only our classes, and we register out the loader directly for PHP. We don't use Composer for that.
And it seems that I'm not 100% sure how Composer, like, when it goes and tries to find this class, does it do the regular, like, the regular load by… it relies on PHP to load this class, or does it look only in its own sources? Like, if you didn't mention this namespace in one of the composer JSONs, is it possible that it will not find it, that it will not even try to just load it?
Just wonder, like, how does it re… how this mechanism tries to even resolve it, because.
**Chris Lightfoot-Wild** 22:34 If you let the Composer plugin for SPI run, which I guess you probably have done here, if you then look in the vendor Composer directory, there's a Generated Service Providers, or something like that it's called.
**Sergey** 22:48 I see what you say. The plugin runs at which time point does it run? When you do install, at what point does it run?
**Chris Lightfoot-Wild** 22:55 Yeah, yeah, it's, post-autoload, I think it is.
**Sergey** 22:59 Huh.
**Chris Lightfoot-Wild** 22:59 So, if you enable the plugin, it does that outside of regular runtime.
**Sergey** 23:04 And which file did you say to check after that?
**Chris Lightfoot-Wild** 23:07 Vendor composer, it would be then, like, generated service load or something?
**Sergey** 23:13 Inside… inside vendor folder, composer… folder, or compose of some file?
**Chris Lightfoot-Wild** 23:18 Yeah, that generated service provider data.php, that's the…
**Sergey** 23:22 Okay, so this is what the plugin, this PI plugin does, this, yeah.
**Chris Lightfoot-Wild** 23:26 So then… But if you've got in your distro, like, two vendor directories, I'm not… I'm not entirely sure if that's the setup you've got, but you kind of inject something first, don't you, on autoload?
**Sergey** 23:37 No, we don't want to have one vendor that we eventually load, but our classes will load, we are directly registering autoloader, you know, this SPL autoloader, a class that will automatically discover our classes.
**Chris Lightfoot-Wild** 23:49 So I guess you… We don't.
**Sergey** 23:49 flow them via the composer.
**Chris Lightfoot-Wild** 23:52 And you'd probably not be wanting to touch this then, because then that would be, like, the user-generated.
**Sergey** 23:57 I mean, I guess we can fool it, and for… so now that I understand how it discovers those classes, so you're saying that after it created this file, then this is what it will use,
**Chris Lightfoot-Wild** 24:08 When you call service loader, load or whatever, it iterates from that.
**Sergey** 24:12 Got it. So this is already kind of, like, frozen in stone after the install, and the… when you call this, search on the interface, this is what it will consult, this map.
**Chris Lightfoot-Wild** 24:23 As long as the plugin has been run previously, yeah. And if not, it just depends on what order you register things in.
Oh, yeah, got it done.
**Sergey** 24:32 Okay, I see now. So you're saying there is no determinism at runtime, this map is decided on install, and it's not touched at runtime, this is what it's being used, and this is the order.
**Chris Lightfoot-Wild** 24:43 It is, but then we… I think in the past we've spoken about somewhere there was an extension to the interface where it then orders them, so if you wanted to register one with a higher weight.
That you, you know, to jump first to the line, you can do that.
Mmm.
**Sergey** 24:57 It's already implemented now, it already exists?
**Chris Lightfoot-Wild** 24:59 Not for this… this particular aspect of it, but there's some others that have that, and I think we discussed that we could do that down the line, if there's a need for it. Sounds like maybe there's a need for it now.
No problem.
**Sergey** 25:12 Sorry, you said the Navy works on it now?
**Chris Lightfoot-Wild** 25:17 Not… not a part of Neve's package, but we've already got that in… In, like, the core bit, anyway.
**Sergey** 25:24 Okay, so it's something that exists on top of his implementation?
**Chris Lightfoot-Wild** 25:28 Yeah, I could try and dig it out, because it's, like, it's part… a bit patchy off my memory, but .
**Sergey** 25:34 Okay, so I will check it out.
**Chris Lightfoot-Wild** 25:35 example of that.
That's okay.
**Sergey** 25:38 Okay, I will check it, got it. Okay, okay.
**Chris Lightfoot-Wild** 25:41 So is that something you're actively working toward now with your distro, soon to be, I guess, the newer open telemetry distro?
**Sergey** 25:50 Right, yes. Sorry, what did you ask? Can you repeat it, please?
**Chris Lightfoot-Wild** 25:54 So, based on the news you'd shared the other week that the… the EDOT, or Elastic Distro for OpenTelemetry, full name or whatever, is going to be donated, is this part and parcel of that?
**Sergey** 26:08 No, it's just a regular work, but this work that I'm doing now, it will eventually be donated as well. That's why I want it to be in line, like, not doing hacks.
But do it in a way that can be used, yeah. But, no, just integrating what we discussed in the past. Better integrating, because currently, the way we integrate this remote configuration is just by setting environment variables.
But, if we want to be better integrated, it seems that we need to integrate it via this SPI mechanism.
So that's why I wanted to revisit that topic. But.
**Chris Lightfoot-Wild** 26:44 It doesn't fully work as is, we can just change it to accommodate, rather than, you know.
**Sergey** 26:48 Yes, that's true. If I will encounter a situation that it's impossible, but I guess in the worst case, like you said, I can always just, Because in this case, I tell you the truth, I don't even know 100%, like, what would be the point of it calling, like, let's say you registered some interface for this resolver, right?
Resolver returns a result of this method, right? So, calling multiple implementations in the sequence, in the chain, like, what it will do, it will use the last result, like.
**Chris Lightfoot-Wild** 27:23 I'm not 100% sure how this event changes will work. This is the first available one, so it goes through until it gets an answer, is how it's kind of currently set up.
**Sergey** 27:33 Right, right. So it sounds to me, then, then if I don't… if I want to make sure, I guess, that I am… I can just register with my information on using this, and assuming that it will be already on top of what was scanned during the install.
then, I can just, as a fallback, call to this class directly.
and call it a method and retrieve the value of the local configuration. Do you think it's a valid approach?
At runtime, essentially, register my implementation via this.
And then, and then if I don't have an option that came from remote, then I go and call this class to fetch a local configuration value.
**Chris Lightfoot-Wild** 28:19 Yeah, I've understood the question there, but maybe if you… I'd be happy if you could, ping us a message, and we could just discuss it.
**Sergey** 28:26 Okay, okay, no problem. I, when I have it working, I will, I will, I will pin you and show you what I have.
**Chris Lightfoot-Wild** 28:32 Even if you've got, like, a… if you're doing it, like, in the open, and it's a public branch somewhere.
**Sergey** 28:36 Yeah, it will be in the open, yes, it's… Our repo is open, I think. Should be open.
But, yeah, definitely, it's open. Right, Pavel? Our repo is open.
**Pawel Filipczak** 28:47 Yes, he's open, huh?
**Sergey** 28:49 Yeah, yeah, definitely, it's open, nothing… yeah.
**Chris Lightfoot-Wild** 28:52 I mean, so if you've got some work already pushed up, and if you just ping us up here…
**Sergey** 28:56 It's currently kind of like, I stashed it, but I want to have them done with the current thing, I will switch back to it, and yeah, in a day or two, I will definitely pin you, thank you.
So just to make sure, obviously, during the contribution, we can always reduce certain things, But yeah, so it's essentially just to better integrate this remote configuration into the way we read configuration. Because if I understand correctly, setting environment variable might not be always the best, because it seems that some sources, and I think Laravel and other sources will come from here, right?
Yeah. I think. So that means that if larval.env sets that option, it will override. Like, if I… if I tried to… to integrate it via here, then the order might have been different. So, I guess… and relying on environment variables is also incorrect, because Laravel.env will override environment variable.
So it seems that it's the… it's best to cleanly integrate in SPI. So I will pin you after I have something working, at least from my point of view, then to make sure that I'm not missing anything.
**Chris Lightfoot-Wild** 30:03 Yeah, I'll try and dig out that thing about how it weights some of them as well, because that was something that maybe is applicable, or could be applicable here, so… I'll try and reach out when I find that.
**Sergey** 30:16 Thank you. Okay, that's it for me.
**Bob Strecansky** 30:19 Thanks, y'all. We'll catch you all, next time.
**Chris Lightfoot-Wild** 30:22 Cool, filler.
**Pawel Filipczak** 30:24 Thanks, man.
