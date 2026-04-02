SIG: PHP SIG
Date: 2026-04-01
Duration: 59 minutes
Zoom Recording URL: https://zoom.us/rec/share/R5T4GjAF839BNFqHHU0ZqAhtWQtXRoyR3xUidPB3fhUXpN6ySQFCRYnnuGVi0kne.AmrHhRlvLXXN2CyH
============================================================

## Zoom Recording Transcript

**Chris Lightfoot-Wild** 00:59 Hello?
**Bob Strecansky** 01:01 Welcome in.
**Sergey** 01:03 Alright, guys.
**Bob Strecansky** 01:04 How are you?
**Chris Lightfoot-Wild** 01:05 See?
**Bob Strecansky** 01:10 Just so y'all know, I have a hard stop at 30 past the hour today.
**Chris Lightfoot-Wild** 01:15 Yours?
**Sergey** 01:17 Do we have a lot in the agenda?
**Bob Strecansky** 01:20 I have, like, a handful of things, but nothing… nothing Herculean, hopefully.
Our.
**Sergey** 01:28 I wanted to ask you guys' opinion about, but .
**Bob Strecansky** 01:32 Here we go.
**Sergey** 01:32 We can do it after the… The standard walkthrough.
**Bob Strecansky** 01:39 You staying safe, Sergey? How's everything going over there?
**Sergey** 01:42 I guess if you… we will be experiencing air siren together.
Oh, yeah. You will see it in real time, if it… I'm hearing artillery.
Working about, like, maybe 10 kilometers from here, but I can hear them.
So, it's not that loud, but yeah, depending where they are coming from, it's from Iran, then we get about 5 minutes forwarding.
Advanced warning to prepare, but… Then the… if they… if they cannot shoot it down successfully, then it's about, like, 20-second warning, only relevant to a particular area.
That has a chance of… but if it's from Lebanon, I live not far, maybe about 50 kilometers from Lebanon, so… Then we don't have this advance warning. Then we only have about 30 seconds.
**Chris Lightfoot-Wild** 02:38 Whoa.
**Sergey** 02:40 But all the houses here, we have a special room, kind of like a… Enforced concrete, double width, so… We just need to go there. It's not like I need to… I don't need to go and find, like, a neighborhood bomb shelter.
**Bob Strecansky** 02:54 the… the United States calls that a safe room, which I think is, like, the dumbest naming scheme for something like that, but…
**Sergey** 03:01 It's the other way around. The safe room is, it's… well, I guess not exactly. The safe room is about, like, more, like, about robberies, right? You just, you just, shelter yourself,
**Bob Strecansky** 03:12 A lot… so, a lot of American construction is, like, built on top of concrete slab to begin with, so many people will, like.
double reinforce the, like, that's called a basement, it would, like, double reinforce their basement, and call that a safe room. So, like, for bombs, or tornadoes, or doomsday prepping, or whatever, you know, whatever your du jour is.
**Sergey** 03:34 Okay, I guess I got exposed to that concept about, like, maybe 10 years ago. I think there was even a movie with Jane Fonda.
Foster, I think, larger funder.
**Bob Strecansky** 03:43 There was a safety movie, that's true.
**Sergey** 03:45 It was mostly in the context of robberies, right? When, like, rich people just need to quickly…
**Bob Strecansky** 03:51 Yeah. Yeah. And there's, there's all sorts.
But… Anyway, well, I hope you stay safe. I'm keeping a good thought for you.
Thank you. Yeah. Alright, so… As I mentioned to Surya and Chris, I do have a hard stop at 8.30 today, or, you know, 30 past the hour for all of the international speakers. So let's get rockin' on our agenda for today.
So I'm, like, 90% of the way through our release.
The only thing that got caught up in our release was there was an instrumentation, fault, and I put in a fix for that instrumentation fault.
Paul, you may actually be a really good reviewer for this. I think Brett would be, but he's not really responding very well right now, for good reason, because he's on paternity leave.
**Pawel Filipczak** 04:40 I will pick them,
**Bob Strecansky** 04:42 Cool, it's just adding an environment flag, so, if you wanna… This should… this should be… I'll ping… oh, it's in that… it's in the document, it should take you about 30 seconds to review, but, if you have any.
**Pawel Filipczak** 04:53 I agree to that now.
**Bob Strecansky** 04:55 Well, thank you so much. Then I'll be able to finish the release. And then next week, or maybe later this week, I'll probably do a subsequent release, because there were a couple people asking for features in… A latest release, so we'll, we'll probably finish this release and then start a subsequent one relatively quickly after.
**Chris Lightfoot-Wild** 05:13 Which, the only… I had a quick look at that as well, Bob. I just wondered, can we target 8.1 specifically, or is there risk introducing that flag for all versions, if only 8.1 is problematic, or…
**Bob Strecansky** 05:26 We… we Perhaps we could, but I feel like it's probably safer to be more cons… like, consistent across all of them, and when I tried it, I… In my PR, you can see there's a link to the GitHub action that I attempted, and all of them passed with flying colors with that action. If we want to do it just for 8.1, that's fine with me, but, that's what the discussion.
**Chris Lightfoot-Wild** 05:47 I just wonder if, like, anything else masks in future, you know, just because we've got.
**Pawel Filipczak** 05:50 Yes, yes, sorry.
**Chris Lightfoot-Wild** 05:51 plug.
**Pawel Filipczak** 05:51 I will take a look, I will build it locally, and check what's triggering this error, and then… I, I, I will… maybe there is some better way to…
**Bob Strecansky** 06:01 Ranger.
**Pawel Filipczak** 06:01 Maybe we can just put a local pragma in the file to skip this particular error displace, and then…
**Bob Strecansky** 06:11 I'm happy with whatever result we come with, I just want to make sure that we get some releases out, because some people are asking for them.
**Pawel Filipczak** 06:17 Okay.
**Bob Strecansky** 06:18 The next thing on the agenda, in the maintainers meeting this week, Jack Berg mentioned that they are adding a response body size limitation to mitigate memory usage risks in the collector.
So, there's, like, a very, very fascinating attack vector where you could potentially compromise a OpenTelemetry collector, and then if you are able to do that somehow, then you can, quote-unquote, infect the upstream app servers by sending back very, very large responses to open, like, to OTLP, Requests, so they are putting in, like, a… pretty… I think it's a 4MB artificial, limitation on response size for, OTLP responses, and they asked all of the languages to implement this in, like, the corresponding API and SDK changes in their languages, so I opened an issue for this, we'll see if anybody, tackles that.
other things. I added a ClaudeMD for Claude code guidance in our repository. I'm sure y'all are starting to use AI a little bit more, and this is becoming a lot more commonplace. It has a lot of cool, interesting.
Things about a repository, so, just so you know that that's there.
And then, last but not least, I added… I finished my edition of Mago to this repository, and now… does full, successful checks for all the… for all the Mego stuff, even though if you go and look at the code quality checks in Mego, they are, they still definitely throw all the things that we eventually will need to fix, but I just wanted to get this in sooner rather than later. It should be relatively, it should be relatively not impactful to RCI. The total thing takes under 10 seconds to run. So, I'm hoping that we can get an approval and merge this in so we can start tracking this for a little bit, longer.
Those were my agenda items.
Sergey, you said you had an agenda item you wanted to talk through?
**Sergey** 08:35 Yeah, something I wanted to run by you. So, let me quickly share the… Would you mind, me sharing?
**Bob Strecansky** 08:43 Yeah, oh yeah, sure, go ahead.
**Sergey** 08:45 Oh, but it's replace current share, okay.
**Bob Strecansky** 08:48 Oh yeah, you could have done that.
**Sergey** 08:49 Didn't know that you can do that.
Okay, so let me quickly see. Okay, so, So the context is we have this distro, and we have a piece that is… We can optimize for, because of a piece isn't done in native code.
So one of the pieces that we optimized is essentially sending of the data, so we do it in the background.
And also serialization, we do it in native, Even though we do it inline, in the same thread and the process, because we need access to the PHP data. But we wanted to optimize it, so we're using… I think Brett discussed it multiple times, that it's possible to do even with the SDK, by just having an extension, right, that does the… a protobuf serialization, but we, since we already kind of, like, self-contained, we do it, automatically. No need to install the additional extension. Now, but unfortunately, the way, for us to do it was we had to duplicate this class, so here.
The issue is that… so this is the, essentially, the class, for example, that does for the exporting for the spans, so we wanted to be able to replace this piece, right? We want to serialize, Not by calling this serializer, because this serializer has been deduced automatically based on transport.
And transport, it's okay for us to keep it as it is. Well, we're registered in a separate transport, but I think it's only kind of, like.
mapping is type of transport, so it's based on the interface. So, I was wondering if you… if you think it's okay if we kind of, like, modify this class a bit, instead of, we can add kind of, like, additional, maybe, argument here, that it's probably possible to pass this serializer explicitly.
And and if it's not passed, then it will fall back on this mechanism.
But then it will allow us, essentially… so the way we solved it for now is just we duplicated this class.
and just replace the piece that we needed, so this is what we did, essentially. This is this original class, and in order for us to replace this piece of serialization and call into a native function, we just replaced it, But it forces us to… so this is the call to the native function. But this forces us, essentially, to always check and pin the version of this package where this class is coming from.
And essentially, kind of like, we need to, you know, merge, Essentially, if we're keeping our own copy of this class, it's obviously not ideal, because every time any changes to this class is made, and we want to update the version of the… I think it comes from the exporter's package.
Then we need to essentially rebase it.
So… What do you think is the solution to just, maybe, for the next release.
Creating a version that will just allow us to pass, Additional argument for serializer here.
Or maybe there is a better human solution to this, Because when I watched it, I think it only allows to change… let me quickly see this, for transport, it's based on the… content type, even. So… So, if we want to use this content type, it will not allow us to register a different serializer just for… for distro.
Although… Yeah, I guess we could, like, if we really want to hack it, like, I guess we could have, in the cost of this room, registered our own serializer, even for JSON and Protobuff.
But I don't know what other side effects it might have that would not be desirable. So if we want to really control it only at this point, explicitly, where we create our own Instance of this class, That would be nice. Although, I think we don't do it, I think we just rely… we kind of, like, shade out the original class, we just created this file.
So I wonder… Baba, what do you think? It will work for us? It will just… this class will be extended?
I think we still need to find a way to integrate it somehow into the flow, right?
I wonder where…
**Pawel Filipczak** 13:12 Oh, I don't know.
**Sergey** 13:13 use that.
**Pawel Filipczak** 13:13 I have to announce.
**Sergey** 13:14 So, guys, what do you think? Like, did I… did I confuse the way I described the… So, essentially, our goal… maybe it can be done even cleaner, maybe we don't need to kind of, like, change this class in particular.
Our goal is essentially… so if we open our project, what we want, In… to doing distro is, like I said, we're calling here, instead of calling the regular PHP-based serializer, we would like to call native function for that.
And, And it also, after it's been done, it also calls native implementation for the transport, but we do register it, right? So for this, we don't need, But for this class, we kind of, like, used this Hark additional fact. We just created the copy of this class, and because we load first, we kind of shade all the… The class that comes with, you know, in vendor folder.
So if we can avoid this, doing that… But I wonder… yeah?
**Chris Lightfoot-Wild** 14:20 I was gonna say, it'd perhaps be good, at least for me, to see it is in a draft form somewhere, to look at it in a bit more context.
And then I just wonder if there's a crossover with that.
**Sergey** 14:29 this… so it's already public, and I can send you the link. So there is this distro.
**Chris Lightfoot-Wild** 14:36 Hmm.
**Sergey** 14:37 repo.
So, let me send the link, Yeah, so… so if you go to the distro, you can see that, here in the prod.PHP, These classes are here in the… so essentially, the distro is the new code.
But you can see that suddenly we also, for some reason, have this namespace, which technically we shouldn't have, because it doesn't belong to distro, and we only have it here for this hack, right? So we essentially have these classes that completely… this is the namespace that is the same one that is in SDK, But because of reloading these classes first.
They will shadow whatever comes with the SDK that has been bundled with the distro.
So this… this is the files that will be loaded, so the classes that come with the SDK, they will not be loaded, so they essentially, kind of, like, essentially shadow them.
And this is where we do what I showed. We essentially call the native function here.
This convert spuns is a native function.
And, yeah. And that's the whole purpose of doing that.
So, if we could… so, my question is essentially… what would be the best mechanism? As I showed before, there is this mechanism where we can register serializer. I wonder if that might be the solution, if we… probably if we just register serializer for all.
**Chris Lightfoot-Wild** 16:06 Are those changes that you're showing now on a separate branch, or are these on mine?
**Sergey** 16:10 So this is main, but we don't have a stable version, so it's a main branch.
But we're only in the mode of technical preview, so… there are no changes, so it's all in this distro repo, right? There are no corresponding changes, like an SDK repo.
It's all been done here, on…
**Chris Lightfoot-Wild** 16:33 Yeah, concerned.
**Sergey** 16:33 Here's job.
**Chris Lightfoot-Wild** 16:34 You were showing, like, a protobuf serializer. Why is that the onset?
**Sergey** 16:37 So let me… by the way, you guys can see it okay? Should I make it bigger?
So, okay, so this is the… this is this repo distro, the new one that we are creating.
Our goal, essentially, Sora, can you repeat it, please?
**Chris Lightfoot-Wild** 16:53 Sorry, I might be confusing things, but I'm looking at the same link you've got there, and you were just showing some code that has got, like, some protobuf serializer somewhere.
What was that?
**Sergey** 17:03 Okay, so, okay, sorry, maybe I'm jumping too fast, confusing you. So this is the copy… so this is not the original file, just named the… so this file also exists in the SDK, it's been packaged into OTLP exporters or something package, right?
So, if I compare… so if I compare the original file that we based from SDK to… so our goal, even to doing that, like I said.
It is to invoke serializer that comes from native, and not, And not implemented in PHP.
**Chris Lightfoot-Wild** 17:36 You were different that to the one that's in… the men… Open telemetry.
**Sergey** 17:42 It's a good question. I wonder how it's being done when extension is being registered.
Is SDK somehow detects… do you know how SDK can fall back on using… I guess it's not fall back, it's kind of like upgrade.
How SDK decides to use, I guess the difference is, is on the… on this API for the protobuf itself.
So it, I guess the extension exposes, the same functions that the PHP library protobuf serialization, right?
So extension, in that sense, replacing it, so… so SDK itself doesn't even need to be aware, it just calls the same API, but it goes to extension.
An extension is being used for protobuf serialization instead of HP library, right?
Here, we only wanted to replace, .
**Chris Lightfoot-Wild** 18:33 Sorry, I think I've understood now, so you were kind of diff in your version of Spark Explorer.
**Sergey** 18:39 Yeah, so this, the gift that I…
**Chris Lightfoot-Wild** 18:40 I just put.
**Sergey** 18:41 before, this is the… on this side, this is the original version in SDK, at least…
**Chris Lightfoot-Wild** 18:45 Yeah, sorry, that's what I was trying to… I didn't know if there was a PR with, like, these changes in it that I could have just linked, but…
**Sergey** 18:50 No, no, there's no PR, we just did this diff on this distro, so…
**Chris Lightfoot-Wild** 18:55 Sure.
**Sergey** 18:55 the original file on the left, this comes from SDK, and we just changed it to what is on the right, and this is the copy we have in distro on the right.
But, yeah, we didn't check it back, we didn't submit it back to SDK.
**Chris Lightfoot-Wild** 19:08 It feels like the newer way is, like, using SPI, isn't it, to optionally swap out… the, you know, the binding of these things, but I don't…
**Sergey** 19:16 Okay, so you…
**Chris Lightfoot-Wild** 19:17 Who's back.
**Sergey** 19:18 Does SPI… will SPI allow us to replace… so, if we go back to… this is what I wanted to ask you, like, if I look… so this is the SDK code, this is the latest, I think, from main.
So, let's say if I… We want to replace this piece, essentially, of a serializer.
convert, right? So, essentially, I guess we will.
**Chris Lightfoot-Wild** 19:39 Well, you just want your own serializer interface, I guess, don't you? And then…
**Sergey** 19:43 I don't know if we also want to replace this piece, but let's for now assume… I don't know… I don't think we called this, let me quickly see.
So we take the bench, we also skipped that part, I don't remember why… why we did it, but I guess we can… let's… let's for now ignore the fact that we also have this converter. I don't remember off the top of my head what the converter does, but let's assume we only want to change the serialized part, right? So, serialized should convert it to protobuf.
So we want, instead, we want to essentially plug in custom thing here.
That will do it. So you think that it's possible to do via… because serializer is being… so it's being deduced based on the… on this call, right? This is where serializer currently comes from.
And here I can see that it's based on the content type of the transport.
Which I… we can control.
**Chris Lightfoot-Wild** 20:38 I just don't know how that works in with the distro as well, though, because, I'd probably just have to have a look at it to try and understand it myself.
**Sergey** 20:44 So this code is the same, we didn't change this code. So the code I'm showing now, it's in SDK, and this part of SDK, we use it in distro directly, by bundling SDK.
So we didn't… we don't have any changes in that part, so whatever, Maybe the difference might be that we maybe don't have the latest version of ASDK in a distro, but we can update it as long as, you know, if distro… if SDK has mechanisms that will allow us to achieve what we want.
**Chris Lightfoot-Wild** 21:11 Yeah, I mean, maybe it could be good to put an issue, or a… I don't know what you think, Bob, but a Slack thread or something to say, like, this is what we're doing, but, you know, there's probably a better way, And gather some thoughts on that. Like…
**Sergey** 21:24 Have a little fun.
**Chris Lightfoot-Wild** 21:25 stuff's ever gonna land in B2, or let's wait until Brett's back, or… Okay, let's go.
**Sergey** 21:32 So, okay, okay, I will do that. So, it sounds to me that maybe… from what I'm seeing now, there is no way to do it in SPI right now, right? I see that it's completely self-contained. It doesn't try to reach to SPI.
**Chris Lightfoot-Wild** 21:46 No, SPR's, like, a lot newer, I think, than a lot of this…
**Bob Strecansky** 21:49 Yeah.
**Chris Lightfoot-Wild** 21:50 Not the codebase, so we would have to put…
**Sergey** 21:52 Okay, okay, I will open an issue. But you think maybe the right way to do it is maybe to extend this piece here to somehow allow plugging something from… with this PI?
**Chris Lightfoot-Wild** 22:01 Yeah, SPI basically gives us the pluggable dependencies, isn't it? And then you can switch them out, kind of at runtime, so you just have…
**Sergey** 22:09 Okay.
**Chris Lightfoot-Wild** 22:09 binding for that. But we'd need to obviously build that base functionality into the SDK, so…
**Sergey** 22:16 Build, excuse me, build what?
**Chris Lightfoot-Wild** 22:19 Well, we'd basically need to support the service loader, where we'd need that functionality.
**Sergey** 22:24 Even here, if you want to, in this area of functionality, if you want serializer to be able to have it customized via SPI, then we need to change code in this area, right?
**Chris Lightfoot-Wild** 22:34 Yeah, I think there's a V2 branch, on the core, Which, you know, not merged in yet, but that would be useful, perhaps, to use as a comparison of where… Service Loader is using the… So, pluggable components.
**Sergey** 22:49 You think that maybe in V2, it maybe already has some changes in this area?
**Chris Lightfoot-Wild** 22:55 I'd have to…
**Bob Strecansky** 22:56 Probably.
**Chris Lightfoot-Wild** 22:56 I'll have to check, yeah, I'm not sure, off the top of my head.
**Bob Strecansky** 22:59 If you look… if you go back to the repo, and there's a branch that's, like, it's named, like, V2.0 or something.
**Sergey** 23:06 Here, right? Here.
**Bob Strecansky** 23:07 That's right.
**Sergey** 23:08 Okay.
**Bob Strecansky** 23:09 Just type…
**Chris Lightfoot-Wild** 23:10 Yeah, it's like 2.x, yeah.
**Bob Strecansky** 23:12 Yeah, there it is.
**Sergey** 23:13 Okay, and it's located, it's inside,
**Chris Lightfoot-Wild** 23:17 He has a bunch of examples of using ServiceLoader, but it's probably a bit stale now, and…
**Sergey** 23:23 Oh, okay.
**Chris Lightfoot-Wild** 23:23 It'll be a case that's covered, but we can… we can see.
**Sergey** 23:26 Okay, so you're not saying that this particular use case might be already covered, but you're saying I can look at the… But we already have SPI in version 2, so let's say if I want this change to be already present even in V1… by the way, what, When you mentioned the release, Bob, at the beginning, did you mean V2, or we…
**Bob Strecansky** 23:50 No.
**Sergey** 23:51 on something.
**Bob Strecansky** 23:52 So, I'm releasing 1.x.x for the repos this week, and then another 1.x later. V2 would take a pretty significant concentrated effort. Brett did a lot of this in a silo, and I don't understand a lot of it, so if we were to release 2.0, we'd have to… A bring the 2.X branch up to date with main, B, make sure that we understand all the things that go in, which would be a pretty large effort, and then C, merge it in and make sure that we don't break… like, that will be a breaking change for people, so we would have to communicate that effectively.
**Sergey** 24:25 Okay, so if I understand correctly, then, if I wanted to have it done in near term, it's probably better to go to V1 and see how it's done with PI and V1, and use the same mechanism in this area.
That will… so not to rely on the V2, right? If we later would want to adapt it to V2, then we can do it when we're preparing.
**Chris Lightfoot-Wild** 24:47 The concept's the same, it's… there's a V2 because there's some braking changes.
**Sergey** 24:52 So you're saying the difference in CPI itself is not that large between V2 and V1? So, as long as we do it with V1, but it would be pretty straightforward to… it will go just as it is most likely to V2.
**Chris Lightfoot-Wild** 25:03 Yeah, an SPI is available, but just not plugged in everywhere, so it's, like, the effort was to try and get it plugged in in more places, and I guess this is just another example of where you'd need it, so…
**Sergey** 25:13 Right.
Let me ask you this, so what would you recommend for me to… if I want to model, let's say, if I want to open a PR and model, this here, this change here, on some other already present, example that you think best way… how SPI should be used.
For example, if I want to plug some custom layer or extension point in this area, right, to say, okay, how do I register? Maybe it should be done where this was acquired in the exporter.
But I was wondering what would be the best example, you would say, of how SPI… most similar example to what I want to achieve here. So, for example, the fact that I want this call to be SPI, kind of, like, extend… extensible, right?
**Chris Lightfoot-Wild** 26:02 We do.
**Sergey** 26:03 Okay.
**Chris Lightfoot-Wild** 26:03 I guess you need an interface for that serializer that accepts a transport, I guess, and then returns…
**Sergey** 26:09 What would you recommend for me to look at in the existing usages of SPI? Like, for example.
**Chris Lightfoot-Wild** 26:14 I'll try and find one and ping you a link if you want. Also, I'm just conscious of Bob's time, so.
**Sergey** 26:20 Okay, no problem, no problem. Okay, so, yeah, if, whatever you would consider. Yeah, that would be great, okay.
**Chris Lightfoot-Wild** 26:29 And it might… this might already exist in V2, and you can book it out, or… I'm not sure, but I've not looked at it for a while, so, I think I've got enough context to know roughly where you run with the question, so…
**Sergey** 26:39 Just for me to better understand, when you say that there is existing V2, you mean for this particular use case, like, for the serialization?
**Chris Lightfoot-Wild** 26:48 for swapping out components, various components, but maybe not that one, I'm not… I'm not sure exactly what extent.
So…
**Sergey** 26:56 Okay.
Okay, okay. But like you said, it should… it's also possible to do in V1. So, we already have examples on V1. Like, for me, it probably will be easier to get example that works in V1, because then I don't need to guess, okay, what part does and doesn't work between V1 and V2, right?
**Bob Strecansky** 27:15 No, no, dude.
**Sergey** 27:15 Obi won.
**Bob Strecansky** 27:16 And then do the upgrade later, yeah, that would be my opinion, too.
**Sergey** 27:20 So that's why I was kind of, like, asking what would be the most close example to this, what we want to achieve in V1, so we can just go and use the same approach on this piece.
And then, we don't need to guess, like, what was improved in V2, and it is not available yet in V1, right? So, because we don't want.
**Chris Lightfoot-Wild** 27:40 The concept's the same, though, but you've…
**Sergey** 27:42 Yeah, I agree with you, you probably like…
**Chris Lightfoot-Wild** 27:44 Probably right.
**Sergey** 27:44 I understand that you're saying that it's probably, you know, 99% is the same between… but I don't want to suddenly fall on this 1% and, you know, trying to debug and see, okay, because I'm not familiar with this particular area of V2, I don't know.
I know that V2 itself is not… it's not kind of, like, called V2 just because of the SPI. It's probably for different reasons, but, or maybe… It's because we only want to rely on SPI, right? But SPI itself is almost the same.
So…
**Chris Lightfoot-Wild** 28:13 Hmm.
**Sergey** 28:13 Yeah, so, Yeah. I guess, I just want to make sure that I'm not… because I saw a couple of examples that may be not… will not be considered pure SPI. Like, for example, I know that we have this registry here in… but it's not SPI, right? It's done… By other mechanisms, like we have this, something registry.
**Chris Lightfoot-Wild** 28:39 Well, originally.
**Sergey** 28:39 Do you know what I'm talking about?
**Chris Lightfoot-Wild** 28:40 rhythm and stuff like that.
**Sergey** 28:42 Yeah, this one.
Is this, is this… for the SPI?
**Chris Lightfoot-Wild** 28:48 Well, that's going away in V2. If you look at the 2.x branch instead of main on there…
**Sergey** 28:54 Thanks.
exist.
**Chris Lightfoot-Wild** 28:57 Yeah, let's go.
**Sergey** 28:59 So…
**Chris Lightfoot-Wild** 29:00 Right.
**Sergey** 29:01 So this… so this mechanism by itself is… it's not SPI, so that was created before SPI, and we want to eliminate it.
**Chris Lightfoot-Wild** 29:08 FBI's, like, very new.
So… But I can… I'll try and have a look outside this call and send you, like, an example of what I…
**Sergey** 29:16 Right, right. So, for example, relying on this mechanism… so I see that, for example, spun exporter does exist in this thing, so indirectly we could have maybe used it, but it's probably not a good idea, because then we will use an old stuff that we will need to redo for V2, right?
So, this is exactly what I want to avoid, and if I wanted to make changes.
I guess we can use this without making changes to SDK, but… If we're already touching it, probably would be better for us to do it the right way, so it will be as compatible with V2 as possible, right?
Okay, okay, thank you. So, your recommendation, Chris, just for me to understand, is you… do you still think it's worth opening the issue in, in this repo, in the SDK repo, just to see if, people flow different ideas?
**Chris Lightfoot-Wild** 30:04 I think it's still useful just to flag that… what your intent is, because obviously you're building out the distro, and then these are the proposed changes you're going to make to the SDK to facilitate it.
**Sergey** 30:15 Okay, I will do that.
**Chris Lightfoot-Wild** 30:16 So there's, like, visibility of it, I guess.
**Sergey** 30:18 Yeah, sure, sure, no problem there. I will, I will, I will make sure that, we understand.
**Chris Lightfoot-Wild** 30:23 I guess it gives people, like, asynchronously as well, a chance to look, rather than just have to attend this call and…
**Sergey** 30:30 Okay, I will open an issue, and then we can, yeah, it will be public, so we can even discuss it there, so other people might chime in. Okay. Thank you very much.
**Bob Strecansky** 30:40 I got it.
**Sergey** 30:40 Alright, bro.
**Bob Strecansky** 30:41 I gotta jump y'all, we'll see you next.
**Sergey** 30:43 Thank you, guys, but I think that was it for me.
**Chris Lightfoot-Wild** 30:46 Well, I guess we can probably just skip all the formalities of jumping through the boards, right? If we're, we don't… did you guys… are you happy with that?
Beautiful.
**Sergey** 30:56 Which ones? Which, which, which ones?
**Chris Lightfoot-Wild** 31:00 Just going through the usual issue boards, etc, like, we… we can't.
**Sergey** 31:04 Okay, you mean, okay, I thought that Bob did that, but okay, so he… he deferred the regular going through the usages and all that stuff issues?
**Chris Lightfoot-Wild** 31:15 He just… he just had a hard cap on his time there to drop.
**Sergey** 31:18 Yeah, I understand.
**Chris Lightfoot-Wild** 31:19 Talking about it.
**Sergey** 31:19 Yeah, I think we… we can do it next time, yeah, unless, yeah, I think we're fine.
**Chris Lightfoot-Wild** 31:24 I'll try… I will try and have a look at, those two, like, branches, and see what you're trying to, sort of achieve, and see if there's an example I can send.
**Sergey** 31:34 Yeah, yeah. I mean, like I said, mostly it's about… but I actually kind of, like, wonder… I don't remember, Paul, do you remember what did we do with this converter thing?
Do we call it before? Because.
**Pawel Filipczak** 31:47 knowledge.
**Sergey** 31:47 Can I define…
**Pawel Filipczak** 31:49 Well, it's not needed in our case, in the native code, so… Oh.
**Sergey** 31:56 Good.
**Pawel Filipczak** 31:57 Yeah, so it's implemented at the same, so…
**Sergey** 32:00 Okay, okay. Interesting, because I didn't remember, yeah, if it existed before, but I assume it did, at that point where we kind of, like, forked and created our own copy of this.
**Pawel Filipczak** 32:13 Oh, you see, but it's simply implemented in the native side, so it's…
**Sergey** 32:18 Okay.
**Pawel Filipczak** 32:19 Yes, it's iterating through the tree of the span, and then it's converting into the protobuf.
So that's what it does, actually. So it's converting the response. So it's implemented in the native.
**Sergey** 32:34 Okay, so you're saying, essentially, we implemented both serialization and convert, whatever this convert does?
**Pawel Filipczak** 32:40 So, the converter is creating protobars.
**Sergey** 32:47 Well, I think the naming may be a little bit confusing. So, there is this… okay, let me maybe show again, in case maybe we're talking about different things. So, there is this exporter, this is the kind of, like, the entry point to this, right? So, the exporter being given the spawns that come from… directly from API, right? This is the…
**Pawel Filipczak** 33:05 Exporter is calling… exporter is calling spam converter to… to get the… the serialized data.
**Sergey** 33:14 So there are two calls here, one called serialize and one called convert.
**Pawel Filipczak** 33:19 And, and…
**Sergey** 33:19 convert, serializer works on the convert. So, when… if I look at the convert, it seems to me that it doesn't create protobuf, it just does some manipulations on the data. It… I think it converts it from from the classes that come from… so there are classes that come from, from API, right? Like Spun.
That come from this namespace, and then there are classes that come from, from this, so it's kind of like in preparation to… to make them.
**Pawel Filipczak** 33:49 Yes, so there's additional.
**Sergey** 33:51 I know I'm slow.
**Pawel Filipczak** 33:52 which is called this… this service request, export trace service request, and then it's… it's… it's being serialized by… by the protobot, Bob.
**Sergey** 34:01 Serializer… so the purpose of serializer is take these classes that come from proton namespace, and essentially convert them to binary data.
**Pawel Filipczak** 34:10 Yes, so it's kind of just, Just data being, so nothing cares.
And then the protopox cellulizer is just cellulized with the pure data.
**Sergey** 34:22 string. Okay, I see. And so, we kind of, like, do both. So, for us.
**Pawel Filipczak** 34:27 Yes.
**Sergey** 34:27 So we would… so we would like to then replace both calls, That are done here, in this, in this step.
**Chris Lightfoot-Wild** 34:38 Yeah, as long as the output of that thing there is compatible with send, you can.
**Sergey** 34:43 Yes, yes. But the fact that it existed as two separate pieces in, in, Yeah, so it kind of, like, adds, some… so, yeah.
I guess what we would probably do… is to… yeah. It's kind of like my flash… I mean, it depends how we define this SPI, like, if we will allow to to replace these pieces independently, then it makes kind of, like, more problematic for us, right? Because then this API of serialize, it will expect this class, which we don't want to create in PHP space, because we want to optimize the whole thing out. We want to do both steps in the native side.
**Chris Lightfoot-Wild** 35:25 Yeah, but I guess the likelihood is it would just be a wrapper to native one there, so it's not…
**Sergey** 35:32 Right, right, but if… okay, I guess we just need to discuss, like, because if we'll have two issues, two separate interfaces, one that does serialize and one that does convert.
then it by itself will not be enough for us. We would prefer to have even the third piece that does both.
And then we will just inject the third, short component, short interface, that just does both. So, I mean.
I will open an issue, we can discuss that, but I hope, I didn't.
**Chris Lightfoot-Wild** 36:00 Yeah, I'll try and diff those files as well, and see what… what changes you've put in, and then what might… Okay, okay.
**Sergey** 36:08 Okay, so… yeah. And I think… We've already discussed it, I wonder… But I guess, let's try to solve this then, maybe.
**Chris Lightfoot-Wild** 36:18 Everybody's working, and you're not blocked on it, I guess, right?
**Sergey** 36:21 No, no, we are fine. We just adds some overhead for us, the fact that we… we essentially… we had to pin the… because we… we essentially forked that file, right? So, in order for us to be compatible with the rest of that package, we pinned it.
So we had to pin the version, and if we would want to update it, that means that We need to take the new copy and rebase again with our changes, right? So… If we can avoid doing that.
**Chris Lightfoot-Wild** 36:49 Given you're obviously… you're putting a lot of work into building the distro, you guys, like, it makes sense that there's an issue where… where you've encountered something like this that's not easily customisable. You, like, just stick it on there and say, and we've had to do this bit and this bit.
And just that there's a collective, like.
opportunity for other people also to sort of say, oh, and we could change it this way to accommodate. So you don't, like, become blocked by the SDK, but… It's all there, but…
**Sergey** 37:19 Right, but I'm not sure what you're proposing to… I'm not sure… What, can you repeat? Yeah, we might encounter from time to time, like, a necessity to introduce additional, like, extension points, right, to facilitate some difference, but how do you suggestion to… how do you suggestion to handle it?
**Chris Lightfoot-Wild** 37:40 Well, it was just more that you put… sort of sticking an issue on the… on the board, and maybe we need a new label or something that, is, you know, distro-related changes.
**Sergey** 37:48 Okay, I see.
**Chris Lightfoot-Wild** 37:50 You can sort of say, right, we're doing this, and then you can get on with making it work, and then we can come up with a solution, and you're not blocked by waiting on said New SDKs.
**Sergey** 38:02 Yeah, yeah, we can always do some hack, but for… Yeah, but… Oh, okay, okay.
In that sense, label is just informative, it's not like it will… it will, you know, speed… speed it up or something like that.
**Chris Lightfoot-Wild** 38:18 No, just…
**Sergey** 38:19 We would want to solve it cleanly with SDK.
**Chris Lightfoot-Wild** 38:23 I just meant so we can see it on the GitHub issues, and filter them out, and…
**Sergey** 38:28 I see, I see, okay, got it, I see. Okay, okay, I see now. So you're saying, just understand what, what is the kind of, like, parallel, but also open telemetry component, is motivated by, by this change. Okay.
Yeah, we can add a double, but I probably will also mention in the issue itself that it comes from the distro, the insisted for this.
But, okay, I can add the label as well, that's no problem with that.
Okay, no problem. Thank you for that point.
Okay, that's, that's about it. I think additional things I was wondering, We can, I guess, discuss its, But, yeah, so, additional point that maybe it would be interesting to hear, if you, if you think it was, because it's kind of, like, different from SDK, the distro is kind of, like, self-contained, right? And we want to make distro to be completely kind of, like, a reproducible thing. So, let's say, for example, that, We have a release for the distro, after it becomes stable, let's say 0 or 1.2, right?
Let's say, when somebody complains.
And we solved that problem, and we want to release 1.21, right? With a pitch.
So, but we would like the rest of the stuff to be exactly the same, except for the page. So that's, the reason what we do is that we have a log file that is also being… part of the repo. So, essentially, we… whatever we pinned, all the rest of the dependencies.
As long as the log file stays the same, it will be exactly the same.
So we keep dependencies spin. So, it's different from SDK, because SDK is being taken as dependency by the application developer, right? So if application developer wants all the dependencies to be stable between builds of the application, they can do it in any way they want, for example, by… by keeping log file or whatever, right? But Distro is different, because Distro is not a library that you take dependency on it, it's kind of like an application, it's a… it's an external tool.
So, the way we do it is, essentially, we generate the log files, kind of like, From time to time.
Essentially, we get all the latest versions of whatever based on these constraints in the JSON, And then we keep those dependencies pinned in the log file that is being checked in. So, it's a manual thing to… so even if you have a, let's say.
later version for this component, we will not take dependency on it. It will not be packaged in distro until we update the log file, right?
**Chris Lightfoot-Wild** 41:01 Yep,
**Sergey** 41:02 So… so you think this is how it's done in DHP, right?
**Chris Lightfoot-Wild** 41:06 There'll just be a bit of a natural, like, with… I mean, it's not typical how you… you're… I guess what you're doing in vendoring your own Versions of that isn't typical, is it?
From my experience, at least.
But you're building a distro, so it's, like, a different use case.
But I don't know how you'd, maybe it would be quite interesting to see how you… if these packages are getting tagged You know, all separately, on whatever cadence, like, how often are you gonna then update yours?
**Sergey** 41:36 But we thought maybe between each… before each minor release, right? So… because if, when we release patches, we probably would not want… unless… unless some page requires us updating one of these dependencies.
then we will maybe do it by… I don't know. That's actually quite hard, because the way we… if we want… let's say, for example, we are fine with any version, you know, that can satisfy this constraint.
If we want to… there is only… the only way for us to take the latest version of this component, let's say we needed to solve some bug.
We cannot just take our current scripting, doesn't allow us to say, okay, update log file, but only for this component. It will update, it will take the latest versions for all the components that we depend on. Obviously, those versions that are being pinned explicitly here.
they will stay the same, but any transitive dependencies, right, that come transitively, they will be updated, right? So… We don't have, like, we don't have the ability to just update a particular component version.
I guess if we ever need it, maybe we'll do it, but… So, if a bug fix, we need to, let's say, have later version of this component, we'll have to regenerate the log file that will use latest under the constraints of everything, right? So it will go and update, and then we will release, but Like, other than that, like, if we… Don't need newer versions for bug fixing.
then we will not update the log file, we'll just fix the bug in this row, and then all the dependencies will be the same, based on the log file. But we will update log files between… before the minor release, right? Or major. Between, actually, releases… before releases that are not bug fixes.
So every time we make a release, then we can… I mean, unless it introduces some compatibility issues, then we can.
**Chris Lightfoot-Wild** 43:27 It was just more like, if one of those packages had its own patch release, would you then… Potentially, you have to do your own patch release as well, or would you.
**Sergey** 43:37 Right, right, so if we want to do that, then we will have to… yes, you are right. If we want to… yes, if, for example, fix comes… fix is not something that we need to fix in our code, but we just need to include the newer version, the patch fix for one of the transitive dependencies.
Then, we will have to regenerate the log file. It will pick up the latest release of that package.
And then, we will release a new version that will include that.
But, yeah, but it will automatically, like I said, the way the scripts that we have now, they will pick the latest versions of everything, right? Whatever is, you know, satisfies these constraints that we have in this JSON file.
Whatever, it will just go and get the latest that satisfies the constraints.
And it… yeah, unless, you know, obviously we'll have all the automated tests passing. If they're all passing, then… I guess we'll have to rely and say, because technically, between releases, when we will regenerate those log files, we also don't have any mechanism to verify that we didn't introduce any problems, other than automated testing, right?
So I guess we will rely on the same mechanism that will ensure that, The latest versions of whatever we updated are okay, With the rest of it, so… Yeah, but but yeah, it's interesting, a good point, I didn't think about it, but yeah, if we will ever need to release a bug fix version, patch version of distro, and And the only difference there will be that we need to include the newer version of one of the big dependencies, then we'll also need to run update on the log files and essentially build a new release.
Yeah.
**Chris Lightfoot-Wild** 45:21 And it's probably also a good case as well to make sure that we're a bit more strict on those contrary packages, not just breaking, because sometimes That we have accidentally, obviously, introduced braking changes.
And you don't want that to affect your distro.
**Sergey** 45:39 Yes, that's the reason we put explicit version, we pinned all these direct dependencies that we wanted to control, which versions we bring in.
Yeah, I guess we will need to be really discerning about that, yeah, so… Yeah, I guess we will need to do it manually, like, if we… yeah, I don't know if we want to automate that in some way, or just do it manually on each minor release, maybe evaluate, look at all the… whatever is pinned in here, and say, okay, can we try to update? But when you say that the RSA country packages did introduce breaking, changes, are those changes, like, breaking in the sense that they are breaking their own tests, or… in what sense are they breaking? What do you mean?
**Chris Lightfoot-Wild** 46:26 Well, I guess people have maybe done… introduced something that's not correct by mistake.
**Sergey** 46:33 Alright.
**Chris Lightfoot-Wild** 46:33 I guess it's hard to caveat that, but then we've not necessarily gone, all right, this should be a V2 of the package, or, you know, this technically, you know, we've been a bit loose around it, I think.
**Sergey** 46:44 Right.
**Chris Lightfoot-Wild** 46:44 Obviously, that's… Now everything's at least version 1 plus, then… Should probably be, you know, a bit more stringent on those checks, because.
**Sergey** 46:54 I mean, do you have a concrete example? How then later… when it's later discovered, what do we do then? Do we kind of, like, roll it back, and is that something that actually happened, or it's, like, more hypothetical?
**Chris Lightfoot-Wild** 47:07 like, in the SDK, for example, there was a… if you look at the issue board, but you don't have to do that now, but there was a dependency on something in SEMConv.
That wasn't available.
Until a newer version of SEMConf, but the dependencies weren't set up correctly.
So, like, it was possible that you could be on an old version of SEMConv, and then the SDK would blow up.
Trying to access something that wasn't that.
So, like, maintaining the dependencies is… More important, if you're also using them like this.
**Sergey** 47:39 So when it was discovered, it was rolled back? Was the change to roll it back?
**Chris Lightfoot-Wild** 47:45 Possibly. It's happened a bunch of times that I'm aware of, without having all the, you know, issue numbers off the top of my head, but… there's probably, like, something that Contrib and Core could benefit from in the testing. There's probably a lot of crossover between the distro testing, isn't there, of these packages?
And how Contrab and Core could also test, because it could just be… help drive it forward.
**Sergey** 48:10 Hmm.
like, obviously, we would like not to duplicate whatever is being done separately in other depots, right? So, for example, whatever tests are bundled with each instrumentation or SDK, We would like to reuse those and contribute to those to catch those things that you mentioned, right? So, we don't want to, kind of, like, add additional tests that are, like, for example…
**Chris Lightfoot-Wild** 48:34 Ideally.
**Sergey** 48:35 Kayo.
**Chris Lightfoot-Wild** 48:36 You're saying about, like, it provides Laravel or SlimNet, and you're not going to test those frameworks, because they've got good tests, so… you'd expect the same with Contra packages that would just have those.
**Sergey** 48:46 Right.
**Chris Lightfoot-Wild** 48:46 Let's.
**Sergey** 48:46 We will run the tests, we would like to run the tests as part of the CI for the distro as well, right? To make sure that when we bundle this whole thing together, it works together correctly, right?
But we will not have them separate, so we will just rerun them on the… on the distro itself, right? So, for example… we will introduce… maybe we will introduce, like, some really small, kind of, like, sanity checks, like, the fact that we, like, we included the Laravel, but maybe we somehow, you know.
affected it negatively, and it doesn't even work for basic stuff. So maybe we will include some really basic tests that run some simple larval flow, and checks that we do create, you know, spawns and stuff, right? So it will maybe do some really basic Because reusing the existing contribs in that context is a little bit hard, right? Because the way contribute tests run, they don't assume that you kind of, like, install that package from outside. They run directly on the code as… kind of like, it's more development flow than production flow, right?
**Chris Lightfoot-Wild** 49:54 Well, yeah, it's just, like, I think we could probably solidify the testing in future anyway. Just, like, with Laravel, it tests version 8.1 through 8.5, but it doesn't test Laravel 6 through to 13.
Even though that's what we say the dependencies are, and supports. So, like.
You wouldn't benefit from that currently, but…
**Sergey** 50:17 Why, why, why doesn't it test all the versions? It was a matter of time, just creating separate,
**Chris Lightfoot-Wild** 50:22 Yeah, we're just… none of the… none of the existing contrib does that, and then it's already at, like, 100 and something, Deviations on the, you know, build matrix, so there's a lot of… Yeah.
**Sergey** 50:36 That's actually interesting, maybe I should check how you do in larval… how do you do larval testing? Because technically, all the testing in Contrib is being done from PHP unit, right?
Collateral is a separate framework, so I can understand how you can do this kind of testing Like, for technologies that are not frameworks, like PDO or MySQL, because if I understand correctly how country works, testing is that you invoke some technology that you want to instrument, like, let's say, MySQL, right?
And then you check that whatever spans or whatever was generated in memory, you check the results in memory, right?
**Chris Lightfoot-Wild** 51:17 Yeah, and with, like, Laravel, there's a workbench thing, and it sort of has, like, a dummy application for testing purposes, and it's the same in, I guess, in.
**Sergey** 51:25 you're using the ability of Laravel to itself run in the PHP unit flow?
**Chris Lightfoot-Wild** 51:31 Like, the dev dependencies of one of the, you know, test packages, yeah, so it's…
**Sergey** 51:35 Okay, so it doesn't run exactly the same way as it would run when you use it as a framework. It would run a bit differently, but Laravel itself has this special flow to facilitate testing application code.
**Chris Lightfoot-Wild** 51:49 Beautiful.
**Sergey** 51:49 No, that's full.
**Chris Lightfoot-Wild** 51:50 testing thing that is basically the skeleton test Laravel app, and it uses the framework as a dependency.
So… but… and that'll be the same with, like, Symphony, won't it? Like, there'll be… depending on components or Symphony framework as a whole, and testing specific bits, so… Right, because the way we're testing this is…
**Sergey** 52:09 We're running this application as completely, kind of like real life, right? We're not… we're not trying to run… the application in context of PHP unit.
the way we do it in distro is that we're running it as a separate process.
And that process supposedly, like, we didn't… we don't have more complex applications like Laravel, we use really simple ones, but technically it should be extendable to Ralava as well.
So if we have a… we hopefully will soon add, also, tests for Laravel, but we would want to run it exactly as people will do it in production, right? We will not try to run Laravel in context of HP Union.
So it runs the test themselves, but what it will do, it will spawn the separate process, it will run the Laravel there.
And that process will be instrumented by the distro.
**Chris Lightfoot-Wild** 52:58 And…
**Sergey** 52:59 And it will send the spans, to the more collector that we have, and then HP unit code will pull… pull the spawns from the mock collector, and it will test those spans that were sent by the distro.
To the mock collector, or that they correspond to the expected, whatever was expected.
So this is what we already do for other technologies. For Laravel, it would be maybe a bit more complex, because we need to build this application, but So, in that sense, it will be better tests than what can be done by contribs when they need to run in the context of HP Union.
Because then you can run, real, kind of, like, real setup, right? You can even run it in Apache or HP FPM, You don't need to run it, like, in CLI and PHP unit.
So, hopefully, I wonder, like, but… after we're done, maybe we can discuss it and see if maybe… if you maybe will have some ideas, maybe we can extend CONTRIP tests to… but I guess later. I wonder if there were any technology that you found hard to test for Laravel in the context of HP Unit, Because, obviously, it's limiting a bit, because it's not, like, a real flow, right? But in between, are you sending, like, real requests, like… or is it, like, simulating the request, and it skips the whole layer of, kind of, like.
**Chris Lightfoot-Wild** 54:23 They are mocked requests.
**Sergey** 54:25 Okay.
**Chris Lightfoot-Wild** 54:26 the framework does support that, because it obviously abstracts what a request is via the Symphony HTTP component, so it's just.
**Sergey** 54:33 So you're skipping the layer of this HTTP engine itself, of, kind of, like, receiving this as a request, and possessing it. You go directly already to the application, to the framework itself, where it already kind of, like, you know, constructed this abstracted copy of the request, and you can, like, mock that abstracted copy, right?
**Chris Lightfoot-Wild** 54:54 Yeah, and that's abstracted, because, like, obviously the request being served by Apache or PHPFPM is just a stream that's, you know, a HTTP message, so it's… But… Right.
**Sergey** 55:04 So I guess if you want to, like, for example, test more, more kind of, like, advanced scenarios, like, for example, streaming.
It will be really hard to simulate streaming in this kind of, like, thing, right?
**Chris Lightfoot-Wild** 55:15 I guess it'll probably need some thought. It's probably not as easy as just what we've got now, but I'm sure…
**Sergey** 55:21 Right, right.
But did you find it limited? Did you find anything that was not possible to test using this kind of, like, shortcut?
**Chris Lightfoot-Wild** 55:30 I think on the Laravel contrib was just the number of permutations that we say we support 6 and above, and that's why I've got a branch that's still in work in progress, but I'm trying to drop all the old ones.
you know, people can still use the old, already existing tagged packages, but there's not enough people in these meetings, is there, to, like, come and maintain all these things? It's hard.
So, that was the primary reasoning.
**Sergey** 55:57 So… I'm not sure I follow… so you're saying about this… the fact that you… so you… but you would like to still continue? Or you would like to drop those old versions, not…
**Chris Lightfoot-Wild** 56:08 Grab the old ones from, like, mainline, just like anything with dependency, you know, they've not got security updates for 10 years, you know, they're really old. No one's probably using it. The PHP versions they support are outdated. End of life. Right, right. Just part of the software maintenance, isn't it, I suppose.
**Sergey** 56:26 By the way, don't we have, like, for Laravel, the same approach as for PHP itself SDK has? Like, the fact that we stopped after the year after the security update stopped, right?
Like, so… but OpenTeunter SDK doesn't support PHP versions that, after the year of the last security update, right? So, let's say, if, PHP guys say, oh, is it even… Not even security, but the…
**Chris Lightfoot-Wild** 56:54 Exactly.
**Sergey** 56:55 You can stop…
**Chris Lightfoot-Wild** 56:56 We were a bit more lenient, but probably we couldn't move in line.
**Sergey** 57:00 Yeah, so when you decided… so you kind of, like, support for more. Why is that? Is that because people do use older Laravel versions, and you thought that it's not worth dropping them?
So fast?
**Chris Lightfoot-Wild** 57:13 I'm not sure on that decision, I guess it was initially… OpenTelemetry was around from 8 and above for auto-instrumentation for the Observer API, and You know, it's not… It's not… we're only just getting toward a point where the older, earlier versions are just totally dropped.
So, I guess it's just still figuring it out.
M.
**Sergey** 57:34 Okay, but you're saying, for Laravel, you… you were not, kind of, like, hard-pressed to… to try to, kind of, like, really optimize that policy. You're saying, keeping all the versions for now.
York, you can live with that.
**Chris Lightfoot-Wild** 57:48 Well, I think they will be dropped as part of just software maintenance, unless other people can support Because the framework itself has changed how stuff works, so it's obviously harder to instrument all the things in the same way.
without various code paths, and it just getting messy, and so obviously that's why you can just tag a newer version, and bump to a V2 at some point, and say, we only support whatever, and… Yeah, we don't take away the old packages, people can still use them. Like, the same with your distro, you'll still be able to use V1.
But when is the.
**Sergey** 58:20 Right, right.
**Chris Lightfoot-Wild** 58:20 Dude, zoom.
You won't support all the old stuff.
**Sergey** 58:25 Right, right, yes, you're right. Yeah, obviously, then they will… might be, you know, like, have security problems, like what Bob described, with this whole responsibility with the collector sending too much data and stuff like that, so it's kind of like, With, you know, there are always some caveats. Yeah, people can use all the versions, but then they're exposing themselves to something that they need to be aware of, right?
**Chris Lightfoot-Wild** 58:47 Yeah, sorry, not to… not to cut you off, sorry, but my battery's, like, almost about to die, so…
**Sergey** 58:52 Yeah, no, I think, I think you're covered, yes. Thank you for your time. So, just to make sure that we are on the same with action steps, I will create an issue, and I will send the link on the Slack, and then we can maybe continue discussion there for that spun exporter stuff, right?
**Chris Lightfoot-Wild** 59:07 Yeah, sounds good.
**Sergey** 59:08 Okay, thank you very much, have a nice day.
**Chris Lightfoot-Wild** 59:10 Love it.
**Sergey** 59:12 See you, bye.
