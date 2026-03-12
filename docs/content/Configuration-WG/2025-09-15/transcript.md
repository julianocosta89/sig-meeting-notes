SIG: Configuration WG
Date: 2025-09-15
Duration: 34 minutes
Zoom Recording URL: https://zoom.us/rec/share/NjoAOtjBN2Cx0MjRlle9QiPghU881SbGV4KBIPlzrfdTaH7llYBcw51uZZuHR5XV.IaXXb7QFVnZUKZY4
============================================================

## Zoom Recording Transcript

**GZ Gregor Zeitlinger** 00:35 Hello?
**MG Marylia Gutierrez** 00:37 Hello!
**Jay DeLuca** 00:40 Anna showing up.
**MG Marylia Gutierrez** 00:43 Because I just feel like it's a regular weekly for us.
**Jay DeLuca** 00:51 I just got out of meetings with the two of you.
**MG Marylia Gutierrez** 00:53 Terrific.
**Jay DeLuca** 01:05 I saw Arthur might have had some stuff on the agenda, too. I wonder if he's gonna join as well.
**GZ Gregor Zeitlinger** 01:10 No, no, no, I… I put my name in front of it.
**Jay DeLuca** 01:15 Oh, yeah, I gotcha. See it.
**GZ Gregor Zeitlinger** 01:23 And I think there's been movement already.
Sends…
**Tyler Yahn** 01:44 Hey.
**GZ Gregor Zeitlinger** 01:45 Hi, Tyler!
**Tyler Yahn** 01:47 How's it going?
**GZ Gregor Zeitlinger** 01:48 Court.
Door is ringing.
**Tyler Yahn** 02:12 Sorry I'm a little bit late, the, notification didn't seem to work this morning. I'm looking at the agenda, it looks like we have a few things we wanted to… Talk about possibly… it's in the template section.
But anyways…
**Jay DeLuca** 02:31 Yeah, I imagine that was just a mistake, but I think Gregor will be back in a minute.
**Tyler Yahn** 02:34 Yeah, okay.
Yeah, I guess if you haven't yet, please go ahead and add your name to the, attendees list, and then, you know, we can get started here in just a second.
**GZ Gregor Zeitlinger** 03:20 Hello?
**Tyler Yahn** 03:21 Hey.
**GZ Gregor Zeitlinger** 03:34 I hope I don't have the only agenda items.
**Tyler Yahn** 03:37 I think he might.
**GZ Gregor Zeitlinger** 03:40 Yeah.
And it's probably a quick one.
**Tyler Yahn** 03:44 Yeah, well, we'll see. Yeah, you want to start us off, Gregor?
**GZ Gregor Zeitlinger** 03:50 Yep.
**Tyler Yahn** 03:52 Although I think ours… Arthur might… is Arthur here as well? No.
**GZ Gregor Zeitlinger** 03:56 Well, I just edited, for him, because I thought it… it's relative… or I thought it's relatively straightforward. If not, at least, we have some movement, because it, he was waiting for Some feedback. Quite some time.
**Tyler Yahn** 04:16 Yeah, so this is, just… provide context, right, Gregor? This is, so that we're adding a new way to provide this… Translation strategy?
It's replacing these two different other options that we already have, right? And there's a… Desire to try to do this in a backwards-compatible way, just to not introduce issues.
Right. And then… yeah, the… The long-term plan, is it to remove these?
**GZ Gregor Zeitlinger** 04:48 Yes, the reason for that is because OTel Collector needs to have a time… To, deprecate the options.
Because, they don't want to have a breaking change.
**Tyler Yahn** 05:08 Yeah, I think we might have talked about this last time. So, Alex, do you… can you, sorry to put you on the spot, do you know a little bit more about the deprecation strategy in the, Collector around the Prometheus exporter?
**Alex Boten** 05:22 Yeah, so the… the deprecation strategy in the collector is to, Make a release that has feature gates that make an, like, a config option, as, like, an opt-in, if you want to… migrate to it. After a few releases, it gets turned on by default, meaning that users still have the feature gate, but they would have to enable the feature grid if they want to use the old, configuration for, format.
And then after a few more releases, it… that flag gets deprecated, and there's no more way for anybody to use the old, configuration.
This is all completely independent from the schema itself, because the collector currently is still running on V0.30 of the schema, because that's the last version that was released in the hotel.
HotelConf package.
So, yeah, I don't… You know, other than creating a release that includes both options here.
for any implementations that would want to be able to support both options at the same time for migration path, you know, there's no dependency here on the collector to do those.
**GZ Gregor Zeitlinger** 06:40 In other words, we don't need to have this deprecated here, is that right?
**Alex Boten** 06:45 That… that's correct. Now, I can't remember the details of our plan for supporting backwards compatible… incompatible changes. I guess since we're not at 1.0 yet, and we're still at the release candidate, we could make this breaking change now, and it wouldn't… Like, go against any policy or anything that we've defined, so…
**GZ Gregor Zeitlinger** 07:08 Yes, I think.
**Tyler Yahn** 07:09 That was kind of my question as well, is like, are… do we want to go through, in a release candidate, are we okay with removing these things?
**GZ Gregor Zeitlinger** 07:22 Think so.
**Tyler Yahn** 07:23 Okay.
So the feedback is that we want to just remove this, and that the collector itself can handle this because it's an independent configuration?
**Alex Boten** 07:37 Yeah, I mean, I approved it, you know, if we did want to support both at the same time, I don't think that's really a problem. I don't know that we should release 1.0 with already deprecated options, so… you know, maybe this is the right time to do it, and implementations have to manage this themselves.
I don't know who this would hurt otherwise. The collector has its own path for migrating configuration, so I'm not worried about it from that standpoint.
**Tyler Yahn** 08:07 Yeah, it just seems a little odd that, like, so, I think we're at, like, release candidate 1 right now, so the plan, if I'm not mistaken, is to do, like, if we did, if we went down this path.
We would do a release candidate 2, it would have deprecations, and then we'd do a release candidate 3 that has a removal.
**Alex Boten** 08:24 Right.
**Tyler Yahn** 08:25 Or, or we just do a release candidate 2 that has a removal.
**Alex Boten** 08:30 Is there a pref… I don't know that there's a… there's a big reason for having that in-between step for release candidates.
**Tyler Yahn** 08:39 Okay.
I think that makes sense to me, too. I do know that a lot of this was coming from the, like.
concern about the collector, but it sounds like, as you're pointing out, like, they're independent, and that this shouldn't actually cause that effect.
or cause a break and change there. Like, I think another question is, like, if… If for some reason, like.
the collector upgraded to… let's say the hotel conf comes out with, like, a new package that can, like, it removes this and it, like, adds this. I'm pretty sure you can still use the old collector configuration to then translate into something like this, right?
**Alex Boten** 09:17 Yeah, so the, the way that I implemented this the support for configuration in the collector. I've had to support migration strategy anyways from, like, V0.2 to V0.3, so, like, this is not gonna be any different.
**GZ Gregor Zeitlinger** 09:40 So, I… My comment here that I've prepared is, this PR can already remove the options instead of deprecating, since the collector isn't using this schema.
**Tyler Yahn** 09:50 Okay. Yeah, thanks. I won't even add it, yes, but that looks great.
**GZ Gregor Zeitlinger** 09:59 Yep, I added that now.
**Tyler Yahn** 10:03 Just at the end here, I'm guessing, yeah. Okay, cool.
Awesome. Yeah, thanks, Gregor.
Okay.
If that's the case, we'll wait for some feedback on that. Go ahead, sorry.
Gregor, I'm sorry.
**GZ Gregor Zeitlinger** 10:19 I just, said thanks.
**Tyler Yahn** 10:22 Oh, okay.
Sorry, I must have choppy connection or something like that. But okay, cool. Moving on then, Gregor, migration schema bug.
**GZ Gregor Zeitlinger** 10:33 Right, I noticed that when I played around.
**Tyler Yahn** 10:40 This is just an open issue. Are you asking for feedback on it, or are you just trying to bring it to our attention?
**GZ Gregor Zeitlinger** 10:47 I'm wondering what to do about it.
Because the migration config says you can use, an environment variable And a place where an integer is expected, but the environment variable can also be a string that has a unit attached, at least in Java. That's where I tried it out.
And, there are different possibilities. We can, add a warning that says it doesn't work if it is not an integer, or we could say, no, we want this to be compatible, and we are changing declarative configuration, maybe something else that I haven't thought about.
**Tyler Yahn** 11:34 So… Sorry, can you walk me through this a little bit, like, slower? The… the… this replacement here… Should work with an integer, but what you're saying is it doesn't work with a string, like this?
**GZ Gregor Zeitlinger** 11:52 Exactly.
**Tyler Yahn** 11:54 And we want it to work with a string like this?
**GZ Gregor Zeitlinger** 12:00 Well, if we want, the migration schema to be a true migration schema, where users can have all their values in the wild, then we should support a string, because otherwise users will run into the same exception that I'm running into.
**Tyler Yahn** 12:18 So, but this isn't valid in the OTEL spec, though. Like, this is not supposed to be a string in the OTEL spec.
**GZ Gregor Zeitlinger** 12:27 regardless of spec or not, this is how Java currently works.
So it's de facto spec, I would argue.
**Tyler Yahn** 12:40 I don't know if I'd accept that argument, like, I think it may be de facto behavior in the Java implementation, but I don't think this is specification. Like, I'm not… like, that's not… this isn't in the specification, like, it literally says that it needs to be an integer in the specification.
For this environment.
**GZ Gregor Zeitlinger** 12:56 Yeah, I'm not arguing about that.
**Tyler Yahn** 12:59 So, then… I'm… why would we want to support this, then?
**GZ Gregor Zeitlinger** 13:05 Because it is currently possible to use in Java, as I said. People are using…
**Tyler Yahn** 13:09 Java… Can Java support this, then?
**GZ Gregor Zeitlinger** 13:15 No, because Java is generating the code based on the JSON schema, or it is, There is no escape hatch to support more than the JSON schema does.
**Tyler Yahn** 13:31 Hmm.
**GZ Gregor Zeitlinger** 13:32 At least no easy one, maybe there's some trickery that I have not thought about, like modifying the schema after downloading or something like that.
We can also add a big warning into the migration schema config that says, It might not work if the… Environment variable is not an integer.
**Tyler Yahn** 14:04 Yeah, so is there, Is there something in the schema that we could change to make this work, is what you're saying?
**GZ Gregor Zeitlinger** 14:14 We could, turn it into a string, but that… that would mean that we are, Going all-in, that we would say, that, I guess we would say that we are supporting units, because otherwise, why would you make it a string?
**Tyler Yahn** 14:34 Well, it also does seem a little odd that, like, we wouldn't… Generically support all of these for being strings.
Cause, like, in… in… Guess I don't know about Windows. Like, most operating systems don't interpret values from environment variables as anything but strings.
Right?
**GZ Gregor Zeitlinger** 15:03 You lost me a bit. What does that have to do with it?
**Tyler Yahn** 15:07 Well, okay, so this value that I'm getting here, right, this interpolation that I'm doing here, like.
if I set this in my environment, right, I'm setting it to be a string, right? Like, that's how it's actually interpreted at the shell, right? Or…
**GZ Gregor Zeitlinger** 15:22 At the shell level, it's a string, yeah, I agree with that.
**Tyler Yahn** 15:25 Yeah, so that's kind of what I'm saying, is like, if it's already a string at the shell level, why are we imposing an additional, like, typing restriction here?
Also, like, yeah, this is I'm confused, sorry, because, like, this is a string here, right?
**GZ Gregor Zeitlinger** 15:44 Right, but this JSON schema makes a distinction, that some things are strings, and some things are integers.
This is, like, in the schema. If you go to the left in the steamer folder, then you can see that it's actually an integer right now.
**Tyler Yahn** 16:03 I see, and so what you're saying… in here, this is where it's gonna fail.
**Dan Gomez Blanco** 16:10 Just to…
**GZ Gregor Zeitlinger** 16:10 Right.
**Dan Gomez Blanco** 16:12 Just to check in my knowledge, and so the Java implementation does allow basically to pass just an integer, right? Like, if you pass in, let's say, 5,000, it doesn't expect the suffix of a unit, like, in milliseconds in Java.
**GZ Gregor Zeitlinger** 16:29 Right, so the default unit, if you don't specify anything, is milliseconds, so Java supports a superset of the specification right now.
**Dan Gomez Blanco** 16:39 So it's not like, you know, if someone were to… let's say, do the migration and run them, I don't know, in an environment in parallel, that could… let's say… if it had a warning, I mean, they could… it's not like they couldn't run one or the other in Pilot, they could change… The one that they pass by an environment variable to.
and some Java.
sort of like SDK, and then remove the… So if we had it as a warning, it wouldn't be so much of an issue.
For people that are at that stage.
To just have it as an integer.
**GZ Gregor Zeitlinger** 17:15 But right now, in Java, it is, It is an exception, you cannot, use the configuration file at all, because it… It just, Stops at the parsing stage.
I can add a warning in the documentation, but users still have to figure out what this means, and have to fix it, because otherwise they have no observability at all.
**MG Marylia Gutierrez** 17:42 But when you do the actual parsing, can you have, like, the extra keys, like.
on… just on Java, you create, like, a function for check if it is a string, you convert to the number, and then save as a number.
Because this way, the user doesn't have to think about it, they can use number and string, and you were the one Thinking about the actual parsing.
**GZ Gregor Zeitlinger** 18:08 I have not found a way, but, I'll take this as… That's something to check out.
Okay, so, takeaway is, Turning this into a string is not a good idea, and, I'll have to find a Java-specific solution or add it to the documentation. That's not possible.
**Alex Boten** 18:36 Yeah, I mean, I think if we did want to turn this into a string, then, like, this conversation should be started at the spec level.
Not… not in the schema, right? Because the… Currently, all of this is specified in the spec, and all the schema is doing is it's implementing the spec, so… I… personally, I would love to be able to add units, like, on… just me as a user, because I find this much better than specifying 60,000 when I want to put 60 seconds.
But that's not supported today.
**GZ Gregor Zeitlinger** 19:12 Okay.
**Dan Gomez Blanco** 19:13 So that would be a change to, like, the duration type, right?
**Alex Boten** 19:18 Yeah, yeah.
**Tyler Yahn** 19:24 Yeah, okay. Alright, I think, yeah, Gregory, your summary was apt, so yeah, I think that sounds like the right course there.
**GZ Gregor Zeitlinger** 19:31 Okay, cool, thanks.
**Tyler Yahn** 19:36 Okay, alright, this is just notes. Alright, so, alright, that looks like the end of the agenda.
I can stop sharing my screen here.
Any other topics people wanted to talk about?
I see your typing as well.
**GZ Gregor Zeitlinger** 19:50 Hey, I've just started working on, documentation.
For, declarative configuration in Java, and I realize that, some of this stuff is actually not Java-specific.
Let me try to share my screen.
I can show you what I currently have.
Oh no, I closed the window already.
Okay, I'll just open the pull request then instead of the rendered version.
Can you see my screen?
**Dan Gomez Blanco** 21:15 Yep.
**Tyler Yahn** 21:16 Yep.
**GZ Gregor Zeitlinger** 21:17 So this is, our, documentation page.
And I have a new entry, under the Java agent.
And it's meant to be… Yeah, I think a general description of declarative configuration So it has a, getting started.
Section, then it has… A starting point for a configuration.
which I hope will serve most users.
And then it's also explaining that environment variables don't work anymore. So, nothing really specific about Java here. Okay, maybe that you have to pass a system property to your configuration file, but… But then there's some general stuff, environment variables is also quite general, and then it calls out That you should be aware that environment variables are only added if you… Specify them, then I'm… Talking about the migration configuration, the available configuration options… also… also nothing Java-specific, and then endpoint, per… Signal, also not Java-specific, gRPC, also not Java-specific. And then here, this is what I just mentioned, the duration format. This is probably Java-specific.
Yeah, and then there's more that will be Java-specific.
What do you think about that? Is, Is there a different place that we have right now, or should we create a different place? Maybe not in this PR, but, like, as…
**Tyler Yahn** 23:15 I think this is great.
**GZ Gregor Zeitlinger** 23:16 Come on, Steph.
**Tyler Yahn** 23:17 So, I… yeah, I think this is great, Gregor. I think… I think, so this is for, yeah, for OpenTelebitrary.io. I think what we can do here is, is what I would see, like, is just taking this and copying it into the other languages that would also be using this.
I think also something similar for, like, the collector, would be cool, but that'd be way different, you know? It'd be, like, very specific to how it's embedded, like, maybe a little bit more details on, like, how you'd want to set things up.
I can see in, like, the Go auto-insertation, or .NET or something like that doing something very similar once it's supported. So, I think I would see this more as, like, a foundation from which we could build other documentations, but I don't think I'd put it in a different place. I think having Java-specific things in here is great. I would leave it the way you have it, yeah.
**GZ Gregor Zeitlinger** 24:05 We also have, a place where we have common environment variables.
Today, which is, Just, here… Am I sharing the right one still?
**Tyler Yahn** 24:32 No, this is still looking killer.
**GZ Gregor Zeitlinger** 24:34 PR.
Now better?
**Tyler Yahn** 24:39 Yeah, yep.
**GZ Gregor Zeitlinger** 24:41 So here, This has environment variables currently, and we could also think about creating something similar for declarative configuration.
And so, to avoid, copying, Yeah. The documentation.
**Dan Gomez Blanco** 24:58 So he…
**Tyler Yahn** 24:59 Yeah, go ahead.
**Dan Gomez Blanco** 25:00 Here's a question. If you're, like, do you think if you're a user, and, like, you know, let's say you want… you… You land on there.
landing page, and you've got language APIs and SDKs, and you've got zero-code instrumentation.
would you expect to have a high-level, like a top-level, I don't know, configuration?
That can be… As in, like, I don't know if users would then go into, like, hey, zero-code instrumentation, and go into, like, how do I configure?
the agent, right? For Java, for example.
And then… Yeah, I just don't… No, if we've got the SDK config stuff and the languages, APIs, and SDKs.
Mmm… If it would almost, like, feel like we would… If it would make sense to have a more, like, high-level Configuration.
**GZ Gregor Zeitlinger** 25:56 So I do plan to have a new section here next to configuration that says declarative configuration, so that users actually find it when they're looking for Java agent. But I could easily say, I could easily add a link that says, if you want to know how general works.
how declarative configuration works in general, then go over to this section here under SDK config that explains declarative configuration in general.
And, the other way around is also true. So if you go to declarative configuration, then you could also say, go to, zero-code instrumentation, to have… language-specific details. I don't know if we actually do that. Actually, we don't do that for environment variables right now.
**Dan Gomez Blanco** 26:48 But…
**GZ Gregor Zeitlinger** 26:50 And this documentation… Can definitely be improved, so… We don't have to do it exactly the same way as it is right now.
**Dan Gomez Blanco** 27:01 I think it would be nice to have something general, at least for people that, you know.
To show that.
The concept, you know, the schema is general for all.
For all languages, so…
**GZ Gregor Zeitlinger** 27:13 Okay.
And.
**Tyler Yahn** 27:16 help, but I also am a little worried that, like, it's not implemented at the SDK right now for a lot of languages.
**Dan Gomez Blanco** 27:21 True.
**Tyler Yahn** 27:24 I think there's nothing stopping us, I think, from adding it, but I would just also maybe point out that, like, if a user like, goes to the Go SDK and tries to configure it with a file right now, like, there's no… there's not even an option to do that. So, like.
you have to, like, set this up completely different.
**MG Marylia Gutierrez** 27:43 Or maybe have the tape, because we have that issue that shows, like, for each language, what is… already working or not, so maybe transfer that table to this page as well.
**Tyler Yahn** 27:53 Okay, yeah, yeah. Okay. Yeah, that's a great idea, yeah.
**Dan Gomez Blanco** 27:56 Yeah, I think that'd be cool.
**GZ Gregor Zeitlinger** 27:58 that table?
**MG Marylia Gutierrez** 28:00 Not that we have… yeah.
**Tyler Yahn** 28:01 Yeah, sorry, go ahead.
**MG Marylia Gutierrez** 28:03 I was gonna try to find it, that is just the one saying, like, this one can parse, this one can return…
**GZ Gregor Zeitlinger** 28:09 Oh, yes.
**MG Marylia Gutierrez** 28:10 For… and it's by language?
**Jay DeLuca** 28:14 It might be in the spec.
I touched it recently.
**MG Marylia Gutierrez** 28:20 Yeah, it's not gonna be here, Gregor.
**Tyler Yahn** 28:23 is, like, is on GitHub, not here. Yeah, Craiger, it's an issue in the config.
**GZ Gregor Zeitlinger** 28:29 I thought we have a page here as well, I'm actually pretty sure.
I think there is a corresponding page, but I always struggle to find it.
It says, what is, supported where, like, logs are supported in Python, something like that.
**Tyler Yahn** 28:53 Oh, just like the spec compliance matrix, you mean?
**GZ Gregor Zeitlinger** 28:56 Exactly!
But that's not what you were talking about, apparently.
**MG Marylia Gutierrez** 29:02 It is… yeah, me and Jay just posted a…
**Tyler Yahn** 29:05 Oh, okay, yeah.
**GZ Gregor Zeitlinger** 29:07 In our chat?
**MG Marylia Gutierrez** 29:10 Here on Zoom, the chat from Zoom.
Okay, put it on the notes as well.
**GZ Gregor Zeitlinger** 29:21 Yeah, right, but this… I think this is not very end-user friendly.
**Tyler Yahn** 29:29 Yeah, I think… I think the suggestion, though, was just to, like.
just take the section for declarative Config and maybe include that.
In the… in the declarative config docs as well, just to show compatibility.
**GZ Gregor Zeitlinger** 29:45 Would we move it or reference it?
What would make more sense?
**Tyler Yahn** 29:53 I, I don't know, I think, like, having… Maybe even just, like, a high-level… Compatibility, not, like, the very specific details and maybe a summary of saying that, like.
you know, if you set up Java right now, you can pass in a… you know, it does support declared config. If you set up Go, it does not, right? So, like, I think something that… even at that high level, for, like, all the languages and all, like, the components or something like that, would be… be plenty, at the… Declarative config level.
**GZ Gregor Zeitlinger** 30:20 Okay, yeah, yeah, yeah, now I see the picture, yeah, I agree.
**Dan Gomez Blanco** 30:24 Can you link to… Two different docs within the documentation page, right?
In each event.
**GZ Gregor Zeitlinger** 30:32 Right.
So, what about… a good place. So if SDK config could be confusing, would it make sense to have an entry under, language APIs and SDKs, Directly?
**Tyler Yahn** 30:51 Well, it's to configure the SDK, so I would want it associated with the SDK. It's not associated with the API, right?
**GZ Gregor Zeitlinger** 30:58 But then… it's not supported by all… it's implemented differently in some languages, not at the SDK level, I think you were saying.
**Tyler Yahn** 31:08 Right, but I mean, at the end of the day, like, the… it's not, it's not in, like, so it's not in the Go SDK currently. I imagine when it goes stable, and I imagine when we have the OTelConf package, like.
we're going to want to be able to accept this file to set up our SDK. Like, I think that's, like, the end goal of the… it's just not there yet, is the idea, yeah.
**GZ Gregor Zeitlinger** 31:32 Okay, so it would make sense to add it under SDK config.
**Tyler Yahn** 31:36 I agree, yeah.
**GZ Gregor Zeitlinger** 31:38 Okay, cool.
Yeah, thanks a lot for the feedback, Ben. I will, either change the PR or make this as a follow-up.
**Tyler Yahn** 31:49 I… yeah, I like your other one as well, because, like, having specifics, but maybe also, like you're saying, like, doing some linking between, like, a general one and the Java one might be helpful, so yeah. I wouldn't… I wouldn't close your existing PR, is all I'm saying.
**GZ Gregor Zeitlinger** 32:03 No, no, I'm trying to think about it as a combination of the two.
**Dan Gomez Blanco** 32:09 Will the idea be, then, if you're, like, you know, you start from zero-code instrumentation, you go into, like, Java.
You know, how you configure the agent.
And they mentioned that, you know.
yeah, here's the part for the SDK config. You can use the Clarity config with the agent and pass this config file like this, but it follows the schema that is defined in this hire.
Level.
Ding.
I think that makes sense. And then the specifics to Java to be in that… in that, in that part, right?
**GZ Gregor Zeitlinger** 32:41 Yep, exactly.
**Dan Gomez Blanco** 32:43 Coop.
Sounds good.
**Tyler Yahn** 32:51 Well, cool. Alright, I'm looking at the notes again, or the, yeah, the notes. I… any other topics people wanted to discuss?
Things that come up, or they've been working on, maybe?
Any cool implementations?
Maybe in Ruby?
**MG Marylia Gutierrez** 33:17 Yeah, for the JavaScript, it's a little slow now, because people just stopped reviewing mine. Because I was doing, like, the… all the preparation to have, and they were, like, very easy to review, and now they actually started with, like, the parsing. People were like, I'm gonna take a look later, and it's actually this week complete, like, a month.
And they still have a look. But, one of the TC members came and checked and said, like, look good to me, so I'm just, like, waiting for somebody from Montaigners to actually give the approval.
**Tyler Yahn** 33:49 Yeah, I, I think hotel in general in the past month has been also really slow, so I wouldn't take it personally.
Well, cool, alright, yeah, let us know how it goes, and we can, we can always find Daniel Dyla and poke him.
**MG Marylia Gutierrez** 34:05 Yeah, I usually, like, poke him, but he's been off for the past couple of weeks.
**Tyler Yahn** 34:09 Yeah, yeah.
Cool, awesome. Well, I guess if that's the case, we can end the meeting early here. Thanks, everyone, for joining. Good seeing y'all. I'll see y'all, asynchronously here in, two weeks.
**GZ Gregor Zeitlinger** 34:26 See you.
