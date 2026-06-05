SIG: Java SIG
Date: 2026-06-04
Duration: 59 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 00:59 Good morning, fellow balded, bearded folks.
**Jay DeLuca** 01:06 Hello, hello!
**John Watson** 01:09 Good morning.
**Jack Berg** 01:38 Hey, welcome back, Joe.
**John Watson** 01:42 Thank you, it's good to be back.
**Jack Berg** 01:45 Good trip.
**John Watson** 01:47 Yeah, a little… a little long, but it was good.
You know, it's good to be back in your own bed.
**Jack Berg** 01:58 Yeah.
Eating your own food.
**John Watson** 02:02 Although I do… I, do very much like Italy, because they have gluten-free food everywhere, it's awesome.
**Trask Stalnaker** 02:18 That's cool, I wouldn't expect that.
**John Watson** 02:20 Yeah, it's actually pretty interesting. They test every baby in Italy.
For celiac disease.
And if it comes up positive, they give them a lifetime stipend to help pay for the food that will be more expensive for their whole life.
**Trask Stalnaker** 02:39 Nice.
**John Watson** 02:42 So there's, you know, there's gluten-free pizza, gluten-free pasta, it's all available pretty much everywhere.
**Jack Berg** 02:48 Are you gluten-free or celiac?
**John Watson** 02:50 Not diagnosed celiac, but mostly because I don't want to go through the testing process, which involves consuming an enormous amount of gluten, which will make me very, very unhappy.
So I can't technically say I'm celiac.
**Jack Berg** 03:05 But you're in the ballpark where you're pretty sensitive.
**John Watson** 03:08 Very sensitive, yes.
**Jack Berg** 03:11 Ouch.
**Trask Stalnaker** 03:12 That seems like a horrible way to have to test that.
**John Watson** 03:15 I mean, testing allergies is tricky, because you kind of have to expose yourself to them to see whether you react to them.
**Jack Berg** 03:27 We have no agenda.
That's great.
**Trask Stalnaker** 03:39 We are so efficient and just handling everything online.
Asynchronously?
These days?
**Jack Berg** 03:49 I think AI's doing it all.
**John Watson** 03:51 We should add an item to shout out our new approvers on… in the agenda.
**Jack Berg** 03:58 Yeah, that's a good idea.
We've, added… to OpenTelemetry Java to the core repo, we've added Jay DeLuca and Pranav Sharma, so thank you, Jay and Pranav.
Excited to have you join us.
**Pranav Sharma** 04:15 Great, thank you.
**Jay DeLuca** 04:17 Thanks, guys.
**Jack Berg** 04:21 I think there's a new Android.
**Jason Plumb** 04:24 Yeah, David sometimes joins this call, is he? Yeah, he is, yeah.
Sorry, I'm just kidding. I had to reboot to join this call.
But yeah, we're stepping up David to approve her in Android. Congratulations! And thanks for all the help!
**Trask Stalnaker** 04:42 Awesome.
**DavidGrath** 04:43 You're welcome, and also thank you very much.
**Trask Stalnaker** 04:56 Well, we can look… Briefly at our… 3O… Project…
**Jack Berg** 05:12 Good idea.
**Trask Stalnaker** 05:13 Although we've got… The goal is… Oz.
thinking to try to do that, the July release for 3.0, we will… C, I think we've got some of these in… Let's see, that one's in PR… That one… Should be… Straight forward… Did we make a decision on… was there a decision left?
your… trigger… What's our current distro name?
**Gregor Zeitlinger** 06:09 I… I don't know what it currently is, but I think we decided that we want to align.
**Trask Stalnaker** 06:18 Yeah, that makes sense.
**Gregor Zeitlinger** 06:19 Can you open up.
**Trask Stalnaker** 06:20 Yeah, I was curious.
The invoke dynamic… Duff… I've seen some activity, Jack Shirazi as the representative for that work.
Do you… think that will… Leah, is there anything… Sort of critical to get in there.
Before 3-0.
**Jack Shirazi** 07:00 Actually, I think Laurie's done some work on it.
And Sylvan's working on it.
There's nothing critical, it's just, if we can get it in for 3, then… We can work on removing the shading for 4.
**Trask Stalnaker** 07:19 Okay.
Cool, so yeah, they're just… I mean, I think Sylvain knows who's tagged… he's probably tagged these as… Yeah, to the 3-0 milestone.
I will just… Make a note here…
**Gregor Zeitlinger** 08:03 Trask?
**Trask Stalnaker** 08:04 Yeah.
**Gregor Zeitlinger** 08:05 The distro name can also be implemented with this, preview flag, is that right?
**Trask Stalnaker** 08:12 Laurie pointed out a prob- possible problem here.
Oh, as well as a question here.
**Gregor Zeitlinger** 08:31 Okay, it's not… not super important. Maybe we… can just… Somehow, flag which ones can be implemented before, so that it's easier to go over the list.
**Trask Stalnaker** 08:48 Yeah, I'm hoping most of them can. Currently, it's… oh, okay.
**Gregor Zeitlinger** 08:54 Maybe add a label or so?
**Lauri** 09:00 I'd like to point out that if we're going to target the first half of the year, then everything that gets included in 3.0 Needs to get implemented.
Like, in the next week or so, I think.
**Trask Stalnaker** 09:19 So that we can have an RC release, Lori?
**Lauri** 09:25 Well, so it wouldn't be implemented, like, on the last moment.
Like, logically, we'll probably slip.
I assume.
Book.
**Trask Stalnaker** 09:36 Yeah.
**Lauri** 09:37 Well, we could at least try.
**Trask Stalnaker** 09:40 I agree, that's a good point.
**Gregor Zeitlinger** 09:43 Maybe more realistic if we say that we want to have all PRs up this month.
**Trask Stalnaker** 09:53 What do we have? Deter… okay, let's… let's be, let's be ruthless here.
This does not feel like something that has to happen for 3-0.
So, I'm going to kick it.
**Jason Plumb** 10:14 There are 19 open issues with Milestone.
**Trask Stalnaker** 10:22 Let's see, what else do we have? Database SAM constability… Okay, there's… I will… Check this… I think this is… should be done, but I'm not sure.
Invoke Dynamic, a bunch of them are invoke dynamic things.
This one, we have a PR open… Health metrics.
Is this just a… flipping a switch?
Jack?
**Jack Berg** 11:14 So… Yes, there is an environment variable to be able to toggle the version of the health metrics which are used, and there is also the declarative config equivalent, so both system properties and environment variables have a mechanism to select this.
And I guess the one thing that it might be worth discussing is the fact that The semantic conventions for this aren't stable yet.
And, you know, they're pretty good. They've been low churn.
And so I guess, do you care with the fact that they're not stable? Because technically, in core, the… we have an enum for the version of the internal metrics you want.
Which is, like, there's, like, the legacy, and then Latest.
And we name it latest, and not a specific version, because we want that to be, like, floating, and we want the ability to change the telemetry in the latest as the semantic conventions change.
**Trask Stalnaker** 12:19 I see, so… If we opted in to this, we can only opt in to latest.
**Jack Berg** 12:29 You can only opt into latest, exactly.
**Trask Stalnaker** 12:31 Okay.
**Jack Berg** 12:32 And I guess, like, you know, what we could do is… in the event that… because we talk, right? We're not like different groups. Like, in the event that semantic inventions changes, and we want to break something in core, like change the telemetry schema in core such that it would break users for the Java agent, we could add a new NUM value.
to, reflect, like, that version that, you know, the version before the change took place. And then, so, like, latest continues to be afloat.
Yeah, but we introduced, like, let's say 1.35, or something like that. And then, when we make our breaking change, the Java agent switches to the 1.35.0 pin, and so there's no breaking change for its users. That's the best that I have.
**Trask Stalnaker** 13:33 Another option, we could… Say that internal telemetry Is not covered by our stability.
Guarantee… And another option is just to wait.
**Jack Berg** 13:54 Right, okay, so… with updating the versioning policy, we've historically sort of treated it as part of our stability guarantee, but we're saying, like, with a new major version, we're breaking that. And so, like, you know, we're not changing an API, Or in addition to changing, like, the telemetry schema, we're also saying… changing, like, what we state about the guarantees around that telemetry schema for this, like, narrow niche.
**Trask Stalnaker** 14:23 Yeah, I mean, it… yeah, so we could change… we could change it in a major version bump, the definition.
But there's also… Potentially, kind of, like, Wiggle room here in that The changes to telemetry produced by stable instrumentation, versus internal.
health metrics, I don't think that's really… necessarily worth pursuing. I guess… I'm kind of inclined to not… to just bump it out of 3.0, Unless you want… unless you're going to sort of… I'm worried that it could change.
In the SDK release, and… yeah.
**Jack Berg** 15:15 I can't champion it… like, what would… what would really need to happen is semantic conventions would need to stabilize.
And, like, I would, of course, if we were to make breaking changes within the core repository, and I knew this was the default for Java instrumentation, I would, of course, like, coordinate with you all to do something to not break the Java agent. And, like, yeah, so, you know, I think I would… I don't think it's that important to get into 3.0, because… It sort of… it sort of creates issues for us, and it's still possible…
**Trask Stalnaker** 15:53 in…
**Jack Berg** 15:54 You can opt into it anyways, exactly.
So, I'm kind of with you. Unless you really want it, I'm not gonna push for it.
**Trask Stalnaker** 16:03 Let's keep it simple.
**Jack Berg** 16:05 Okay.
**Trask Stalnaker** 16:07 And we'll have… if it stabilizes within… I mean, first of all, people have the opt-in, and if it stabilizes in the 3-0 timeframe, I figure we'll have, like, one of those SIMCOM opt-in things, or some kind of standard opt-in.
**Jack Berg** 16:24 Yeah, Ludm?
about that at the spec call the other day, that, like, there would, we'd extend that environment variable to support internal telemetry opt-in as well.
**Trask Stalnaker** 16:35 Cool.
Switch to stable, SIMCon, so this one, we can… Do… Let's try implement this behind the V3 preview flag.
We'll see. Oh, I like how it shows you who… assigned it to Copilot.
That's nice.
Okay, the distro question… 83… Laurie, do you remember what the problem here with resources created…
**Lauri** 17:47 Because the… Reading East Preview Flag requires the OpenTelemetry instance.
If we read it from the declarative configuration.
**Trask Stalnaker** 18:03 I see.
**Gregor Zeitlinger** 18:08 Is that what we're trying to do, read it from declarative configuration?
**Lauri** 18:12 Well, the utility, by default, reads from the declarative configuration.
**Gregor Zeitlinger** 18:18 Right, by default, but I mean, is that really what we want to do? Because other flags are not possible to read from there.
**Lauri** 18:27 The thing is that, The sole purpose of the V3 preview flag is to get pull requests merged.
Without breaking things.
So it would be easy to find them when we finally need to switch it.
**Gregor Zeitlinger** 18:46 Which means it's not important that it goes into declarative configuration.
Right?
**Lauri** 18:53 Well… It is important in the sense that we need to find… be able to find it when we make the release.
So yeah, like, in that sense, it's a nice-to-have feature.
So that it would be possible for end users to actually enable the preview of mode.
**Gregor Zeitlinger** 19:15 Okay.
**Trask Stalnaker** 19:17 Okay, so this one is a… I mean, it's a pretty super straightforward, though, whenever we're ready to make that… Change.
The only question is then… Yes, we have, I… While we have, in text.
Gone, been going with the space, the two words.
I guess I would say this probably makes the most sense to me, aligning with the artist, since that's the artifact name.
But… There's… there's…
**Gregor Zeitlinger** 19:54 There's also the, the setting and declarative configuration of the distro.
And I think it would be nice if that was aligned.
**Trask Stalnaker** 20:07 So, explain that again, Gagor?
**Gregor Zeitlinger** 20:10 In declarative configuration, we put the instrumentation suppression into the distro block.
And there we have a name for the distribution, and maybe… We just want to have the same string in there.
**Trask Stalnaker** 20:28 What do we put there today?
**Gregor Zeitlinger** 20:33 I'm going to double-check before I say something.
**Trask Stalnaker** 20:36 Can I see that in the Ecosystem Explorer?
**Gregor Zeitlinger** 20:40 I don'.
**Jay DeLuca** 20:41 Yeah, yes, you can.
**Trask Stalnaker** 20:43 Okay, how do I get that? Help me.
**Jay DeLuca** 20:45 No, it's explore.openslemetry.ia.
**Trask Stalnaker** 20:49 Oh.
Thank you.
**Jay DeLuca** 20:51 Yep.
**Trask Stalnaker** 20:52 Oh, not Baker, yes, yes.
**Jay DeLuca** 20:55 And then go to the Java agent… Go to the configuration builder.
And then click to the Instrumentation tab.
On the left.
Yeah, and then scroll down and just click, like, one of those instrumentations.
The customize button?
Yeah, and then scroll up, it should be…
**Trask Stalnaker** 21:20 Distribution Java Agent.
Interesting.
**Jack Berg** 21:31 So all signs are pointing to Java Agent, one word.
**Trask Stalnaker** 21:36 Yes, but should… it's kind of an interesting, good question, though. Should it be exactly… should the distro name exactly match the thing under here?
Right now, we're proposing OpenTelemetry-Java Agent over here.
**Gregor Zeitlinger** 21:56 I would make it exactly the same.
**Jack Berg** 21:59 What do you think… what do you think vendors would do? What are vendors doing under this distribution here? Are they saying… if you have a Splunk distribution of the Java agent, are you saying.
Splunk Java agent, or just Splunk?
**Lauri** 22:17 Look at what we do.
**Jason Plumb** 22:22 I can look it up.
**Jack Berg** 22:23 Yeah, Gregor and Jay, we do… we have a distribution as well, so… So, I… what… Is that… is that key that we're using in there, Java agent?
Is there… is there any chance that would change?
**Lauri** 22:51 I think for Splunk, we are using just Splunk, because, Some of the configuration is shared by multiple language agents.
**Jack Berg** 23:04 Yeah, that's the tough part, so then… Yeah, what does a vendor like Splunk do if it… If it has, you know, agnostic properties.
or language-specific properties, does it have two different configuration blocks, Splunk and Splunk Java Agent?
Here.
Not great.
**Gregor Zeitlinger** 23:34 We don't have so many distributions that we have a problem. We just have a Grafana-openTelemetry-Java.
**Trask Stalnaker** 23:47 distro version…
**Jason Plumb** 23:56 I don't know that that's correct, but that's currently what we're providing.
And to be… just to be clear, I mean, that's what's coming out, that's not what's coming in, like, that's not the configuration.
Yeah.
**Trask Stalnaker** 24:24 Yeah.
So would a distro name… Does… I feel like it should probably have open telemetry in it.
**Jack Berg** 24:47 I think that's the key thing you would want to act on, or identify.
Is whether it's the vanilla upstream one, or one that's from a vendor.
**Jason Plumb** 24:59 Just via the name, yeah. I… I feel like we should change ours.
**Gregor Zeitlinger** 25:07 And Trask, is your intuition that we should also rename the distribution block while we can?
**Trask Stalnaker** 25:22 I don't know.
**Jack Berg** 25:26 I don't think it's unreasonable to… for, like, the vanilla upstream distribution to sort of stake the claim on, like, the base name, on just Java Agent, and not have to say, like, OpenTelemetry Java Agent.
And that's, of course, setting aside, like, the argument that was made previously about it'd be nice if the key was… the key in declarative config was aligned with the value of the, you know, distribution name resource attribute.
But, like, it is nice to have it be short and terse.
**Gregor Zeitlinger** 26:03 In the configuration?
**Jack Berg** 26:05 Yeah, yeah.
**Trask Stalnaker** 26:09 I kinda like this. I mean, it's… kind of implicit. Also, like, when thinking of, like, you know, Splunk, Grafana.
Next to that. Like, they're going to be using… This is sort of the stuff that they're probably inheriting.
**Gregor Zeitlinger** 26:33 It is, yes.
Sounds good, let's do it.
**Trask Stalnaker** 26:42 Yeah, yup.
**Jack Berg** 26:48 Nice, a decision.
**Gregor Zeitlinger** 26:52 Everyone is too tired of the public.
**Trask Stalnaker** 26:57 I think it's a legit, let's see, history…
**Jason Plumb** 27:01 I'm not trying to derail this, but, like, conceptually, it almost seems like we should have a third semantic convention, which is telemetry distro vendor name, or vendor.
**Trask Stalnaker** 27:11 Like, Java.
**Jason Plumb** 27:14 Yes.
**Trask Stalnaker** 27:28 Alright.
So yes, whether we can implement that Right away is still… I could go either way.
Continuing on, wrongs, parent… Due to… Let's see… Oh, a lot of discussion.
Question is, let's consider disabling… with span coroutine support in 3L.
I mean, this made sense to me at the time, I think it still makes sense to me, given the problems with Wispan, but I don't know. We've been… we've done some other magic since then, Laurie, that I can't… Recall off the top of my head.
**Lauri** 28:49 I think the instrumentation just doesn't work correctly, because the… What the Kotlin coroutines do is too complicated.
And I wasn't able to make it work yet.
**Trask Stalnaker** 29:05 Of course, so… Let's… do this.
**Lauri** 29:12 I think the end result will be that, our default, which span instrumentation doesn't instrument, Kotlin Coreoutines, so… If we disable this instrumentation, then no spans will be created.
**Trask Stalnaker** 29:33 Let's see if it was.
**Lauri** 29:36 So, so basically, like, currently.
**Trask Stalnaker** 29:39 Boom.
**Lauri** 29:40 It's broken traces, but then they won't get any traces for us with span methods.
**Trask Stalnaker** 29:52 Do we know that… In the wristband, we know that we're in a coroutine.
**Lauri** 30:00 Yeah, I think we can guess it.
Based on the method argument types and stuff like that.
**Trask Stalnaker** 30:10 Okay, this one feels too complicated for Copilot.
Isn't there?
**Gregor Zeitlinger** 30:20 Is there some bread local that tells you that you're in a coroutine?
I think… I… I saw that some time ago.
**Lauri** 30:31 Well, we do something easier. We basically need to make the decision at bytecode modification time, so we can't check any thread locals.
**Gregor Zeitlinger** 30:39 Okay.
**Lauri** 30:40 Just look at the method signature, and we know that, Good core routines, Have a specific signature.
Think that that… They take some sort of coroutine-specific parameter.
**Gregor Zeitlinger** 30:55 I think some context it is, yeah.
**Trask Stalnaker** 31:17 Why did I do that? .
**Gregor Zeitlinger** 31:41 Says co-routing.
And hide the…
**Trask Stalnaker** 31:45 Thank you. My finger is… that ING is strong. The force is strong with the ING.
**Gregor Zeitlinger** 31:55 I have a key that prints ING in one go.
**Jack Berg** 32:02 Do you really?
**Trask Stalnaker** 32:04 How many keys do you have?
Imagining Gregor, like, a thousand.
**Gregor Zeitlinger** 32:13 No, no, I use a lot of combos, so you have to press two keys at the same time.
So my keyboard has 34 keys, to be exact.
**Jack Berg** 32:27 That means you save one keystroke.
**Gregor Zeitlinger** 32:31 No, it has more features, but I did not want to bore you to death.
**Jason Plumb** 32:37 But those keystrokes happen concurrently, so it is more efficient.
**Trask Stalnaker** 32:40 Yeah, there you go.
**Jack Berg** 32:41 Alright.
**Trask Stalnaker** 32:43 Love that.
**Jack Berg** 32:46 Words per minute is just off the chart.
**Trask Stalnaker** 32:49 So, just to make this clearer, what's actually for 3.0 there, now we have a better tracking issue.
Remove deprecated method…
**Gregor Zeitlinger** 33:13 Yeah, I just added that, so, because it was on the wrong, dashboard.
**Trask Stalnaker** 33:20 Deprecated method… Oh, yes, okay. So this is the stuff… this should get caught up normally in, is it, from… Is it marked with to be removed in 3.0?
**Gregor Zeitlinger** 33:39 I… I cannot remember, too long ago.
**Trask Stalnaker** 33:41 Can you… yeah, could you check while I'm… Carrying on, because that's… that's kind of the… keyword that, I'll be looking for when, We're… Doing the final bump is basically removing all these things that have the deprecated annotation and something similar to comment about to be removed in 3.0.
**Gregor Zeitlinger** 34:09 But this cannot be done earlier, I guess, so this has no point of this preview of, like…
**Trask Stalnaker** 34:15 Right.
System property access…
**Gregor Zeitlinger** 34:34 Do you… should I give you a short recap what this is about?
**Trask Stalnaker** 34:39 I think I remember there's certain library instrumentation system properties we've exposed for library instrumentations.
Even though, kind of, ideally, we were trying to just force everything through programmatic access.
**Gregor Zeitlinger** 34:59 Yeah, it was more accidental, I think.
What is the word to watch out? I have the… File open now.
**Trask Stalnaker** 35:14 Something like 2B removed in 3.0.
**Gregor Zeitlinger** 35:20 No, that's not there.
**Trask Stalnaker** 35:22 Okay.
**Gregor Zeitlinger** 35:23 Do you want to have a PR just with that?
**Trask Stalnaker** 35:26 Sure, yeah.
Yeah, and then potentially we could close, we could close this issue, and if you want to open an issue, just an umbrella issue about removing all those things that are commented to be deprecated to be removed in 3-0.
**Gregor Zeitlinger** 35:51 Yep, okay.
**Trask Stalnaker** 35:53 Thanks.
Laurie, do you… I still have… Thoughts about removing property access from library instrumentations, and just… only supporting declarative config…
**Lauri** 36:23 Mmm… Well, I don't know if, If this would be a win for the end users.
**Trask Stalnaker** 36:40 Let's, let's put together a list, I can do this, of…
**Lauri** 37:00 I think this only applies to, like, those… auto-configured instrumentations, I guess?
**Trask Stalnaker** 37:13 I think we… I think those were at least the ones we did intentionally. I think there were a couple that… We did, maybe unintentionally.
But I could see, especially the auto-configure ones, I mean, I could see keeping those as system property, like.
Leaving those as is for now.
We could reconsider.
**Lauri** 37:36 But I guess, like, maybe one concern would be that, If declarative configuration is required.
Then that sort of implies that It would be impossible to configure it if somebody… decides to manually set up the SDK.
**Trask Stalnaker** 38:08 You mean without having… I mean, you could set up the SDK manually.
**Lauri** 38:14 Like, I meant, like, programmatically. I think John…
**Trask Stalnaker** 38:17 That's the…
**Lauri** 38:17 I think that he prefers setting it up programmatically.
**Trask Stalnaker** 38:23 That's an interesting question, Jack.
For declarative config.
**Jack Berg** 38:28 Yeah.
So, I mean, declarative config is… One of three config interfaces, and you know, from my perspective, the base config interface is programmatic config, and declarative config is always just about interpreting this structured schema and calling the equivalent programmatic APIs.
And so, I mean, that's how I do it, and that's how we do everything in the core, and so there's nothing you can do with declarative config that you can't also do programmatically.
**Trask Stalnaker** 39:04 So, I think the… Potentially, the issue we have in instrumentation, which is… might be slightly different, is we have a couple of auto-configured library instrumentations.
I think we have one for AWS, SDK, and a couple others.
Where, just by a… Being on your class path.
It sort of auto-configures itself into the AWS SDK SPIs, for example, something like that.
And… so the question is… If you're manually configuring the SDK, Can you… Give it some, like, a declarative configuration to use for instrumentations.
**Jack Berg** 40:01 I mean, yes… Because… If you're manually configuring the SDK, then one of the things you configure is SDK config provider.
An SDK config provider is sort of the in-memory representation of all the data that would be in your YAML config file, and you can build that up programmatically.
It's inconvenient, but…
**Lauri** 40:33 But that also assumes that, you are in control of the way the OpenTelemetry instance is built.
**Jack Berg** 40:45 Isn't that what we're, like, sort of the path that we're down, when we say that we're talking about, you know, programmatically building the SDK?
So you're saying.
**Lauri** 40:55 I guess it could be that some library is building the instance for you.
**Jack Berg** 41:09 That's, like, that's an interesting question, because, like, should you have the ability to control the configuration of the SDK if you're not the one building it?
It's environment variables and system properties.
Are sort of, like, anybody that can modify the environment or system properties can influence the… configure the system.
So, that we're sort of taking that away.
**Trask Stalnaker** 41:35 Yeah, but I mean, that's kind of… generically, we are not… We only expose system properties to libraries in a few places. Like, overwhelmingly, we're… it's… Just programmatic configuration, or now we are going to support declarative configuration?
**Lauri** 42:01 I guess another, maybe, maybe more realistic issue would be that, Perhaps there are, like, some sort of initialization sequences.
like, the auto-configured instrumentation then requires that the global telemetry instances set.
**Jack Berg** 42:25 Right, I think…
**Lauri** 42:27 Which might not be always true, and which might not be desirable.
Or… I don't know, like, whether our current, how to configure the instrumentations, like, how they handle it when the OpenTelemetry SDK is initialized after the instrumentation itself is initialized.
I guess they could work due to some, like, lucky coincidences, maybe?
**Jack Berg** 43:08 Yeah, I think what Tross was suggesting with putting together a list of these would really help ground this.
You know, just see just… on paper.
**Trask Stalnaker** 43:18 Yeah.
**Jack Berg** 43:18 And sort of what we're rug-pulling or taking away by… with this type of proposal, and… It might be… It might be something that, you know, it really does affect the users, and thus we hold it back, or…
**Lauri** 43:36 Yeah, now that I think that maybe the coupon telemetry thing isn't an issue at all, because… Without setting the global open territory, then the… Auto-configure instrumentations.
don't usually work at all, because they don't get access to the open telemetry. Only the logging ones, I think, have the setters.
**Trask Stalnaker** 43:58 Yeah, and I think the Kafka ones, or there's some that you can… I guess those aren't pure auto-configure, though, so yeah.
Okay, I think that's a good next step there.
**Gregor Zeitlinger** 44:16 I think I have the list now.
**Trask Stalnaker** 44:21 Nice.
**Gregor Zeitlinger** 44:22 All the ones that are. Do you wanna.
**Trask Stalnaker** 44:25 Oh, list of…
**Gregor Zeitlinger** 44:26 No, I'm gonna just put it on the.
**Trask Stalnaker** 44:27 Oh, the system? Yeah, yeah, if you can just dump… drop it on the ticket, That would be great.
**Gregor Zeitlinger** 44:36 Okay.
**Trask Stalnaker** 44:36 I think it would be worth… I think we're gonna maybe get to the end of this list.
Today.
**Jack Berg** 44:44 Amazing.
**Trask Stalnaker** 44:46 Peer service… This one… kind of… stalled out in, semantic conventions. I thought we were gonna stabilize it.
But, it kind of didn't, and… Hmm… How do I implement the peer service?
What did we do?
**Lauri** 45:18 I think we have an opt-in flag.
**Jay DeLuca** 45:27 That's one of the SEMCOM opt-ins.
**Trask Stalnaker** 45:32 And it's service.peer.name.
So is this done?
asking myself.
**Jay DeLuca** 45:58 If you go to the, instrumentation list and search for that attribute, there are… Handful of modules that do have it.
If that's what you're asking.
**Trask Stalnaker** 46:08 Yeah, shoot… Okay. I think it's done, but I'm gonna… I'm gonna… Double check on that.
So, we've got… okay… Oh, yes.
**Jason Plumb** 46:37 What are we doing with this one?
**Trask Stalnaker** 46:39 Yeah… Sylvain was looking at this, and… Said that there were some… potential… Issues, what did he see… say?
He was concerned that… Yeah, that his plan might… B2M, not realistic.
Alternate… Okay, Sylvain said he's thinking about what to do here.
So… but if… yeah, Jason, if you have any simple… Any ideas?
2…
**Jason Plumb** 47:38 The idea is to be able to stabilize some of the JMX sets, right? So, like, Tomcat or whatever.
**Trask Stalnaker** 47:44 Yes, and or at least to make it… Clear that the… which ones are not, or that, you know, they're all not stable.
**Jason Plumb** 47:55 Right.
**Trask Stalnaker** 47:56 I would be fine… I'd be fine if they're just all not stable.
**Jason Plumb** 48:01 I think what he said in this issue, he's like, let's experimental by default, right?
And… we'd all… I would also very much need… need to or want to understand if… If we were to declare one of these, like, stable and not changing, does that prevent us from adding new metrics to it?
**Jack Berg** 48:24 No.
**Trask Stalnaker** 48:25 You could still add new metrics. Okay. Yeah, you just can't change… there's certain things you can't change about existing metrics. I would say for metrics, almost nothing you can change.
Okay.
**Jason Plumb** 48:36 So the Declaration of Stability is purely for… these sets as defined in the JMX system as not going to change version to version.
That's… it's not that the semantic convention around them is stable, it's that we're saying that we won't change them.
**Trask Stalnaker** 48:54 In… yeah, with… until we get to V4.
**Jason Plumb** 48:57 Okay.
Hmm… Did you write this one originally?
**Trask Stalnaker** 49:08 Yeah…
**Jason Plumb** 49:09 Yeah…
**Trask Stalnaker** 49:13 Basically, I just… I came across it because it… The property name doesn't have the word experimental in it.
**Jason Plumb** 49:20 Mmm.
**Trask Stalnaker** 49:21 And so, according to our… Versioning policy, that means it The behavior is stable, which now includes stable telemetry.
**Jason Plumb** 49:40 So, I think then what he's suggesting is to do the opposite, to make everything experimental in 3.
And then as we slowly start deciding which things we want to make stable, we could… we could migrate them, or…
**Trask Stalnaker** 49:57 I see, so he's suggesting to keep the same property name, but make the different options, config options, prefixed with experimental?
Sorry, I don't think I had really clearly, or at least I don't remember.
Volumes…
**Jason Plumb** 50:24 But when you wrote this originally, you were not… You were not going after the metrics themselves, you're going after the configuration option name.
**Trask Stalnaker** 50:33 I mean, both.
Right, the… it implies… right now, the, like, if a user uses this and says target system equals Tomcat and.
you know, Kafka.
There's nothing in there that… Gives them an indication that that could break.
In a minor version bump.
**Jason Plumb** 51:01 Got it.
Yeah, so if we put the word experimental in there instead, if we renamed it to Experimental Target System or Experimental JMX, And that solves this, right?
**Trask Stalnaker** 51:16 Yep.
And the other option would be, I guess, the target systems themselves to have the word experimental underscore Tomcat.
**Jason Plumb** 51:28 Oh… Is as, as… As an additional thing, or as a separate thing?
**Trask Stalnaker** 51:34 Like, if you wanted, like, you could… I think you could keep this name… And the enums say Experimental underscore Tomcat.
**Jason Plumb** 51:44 Yeah, what is that?
**Trask Stalnaker** 51:45 then allow you to make the Tomcat ones stable.
**Jason Plumb** 51:51 Yeah, that seems like a smoother path, maybe, right? And it's not going to break existing people as badly?
Maybe?
**Trask Stalnaker** 51:59 I mean, existing people are gonna get broken. Oh, I think that's actually what I even proposed here.
**Jason Plumb** 52:05 Yeah. Pretty fixed.
**Trask Stalnaker** 52:06 Seeing the target system name.
**Jason Plumb** 52:08 Okay, now I'm awake enough to understand what you're saying.
That seems good for 3.
**Trask Stalnaker** 52:23 Yeah, I'm trying to think why Sylvain, texted me, DM'd me, that he thought that wasn't realist, his plan wasn't realistic.
Alright, I'll… I'll reply to him in chat, or maybe we've… yeah… Maybe I'll take it to the, the Slack channel.
**Jason Plumb** 53:04 Cool. That seems reasonable.
I want to see that… I wanna see that start to happen, because people use this stuff all the time, at least over here, and… having some excitement about stability would, I think, be helpful.
Even if… even if our baseline is… declaring everything experimental is still a baseline.
**Trask Stalnaker** 53:28 Yeah, I mean, you know, given that we are… do… that we do do major version bumps.
you know, I mean, I think it's okay to be a little aggressive with marking certain systems as stable.
And, you know, if we… we can always hide stuff, changes behind flags, If we change our mind.
It just means, like, we can't do freeform, you know, change whatever we want.
Kind of thing.
Declarative config… I think… We decided that this is… Sort of a non-issue?
**Jack Berg** 54:26 My memory was something like, it's not quite ready yet, even if we wanted to do this type of thing. There's a couple of issues, there's, like, like, the declarative config artifacts in core aren't stable yet. You can't do everything that you want to do with declarative config via stable APIs, like the customization SPIs and things like that.
And then there was this question about, like, what is the default config file, that we bundle with the agent?
If we were to make declarative config the default, and like, how do you edit that, and things like this?
Gregor, is that what you remember?
**Gregor Zeitlinger** 55:12 Yeah, yeah.
Absolutely.
**Trask Stalnaker** 55:17 Makes sense…
**Gregor Zeitlinger** 55:20 So we just have to replace, 3 by 4, and then… Shick the can down the road. Yeah.
**Trask Stalnaker** 55:29 Yes.
**Jack Berg** 55:30 Next week, we'll talk about the 4.0 changelist, and what's blocking.
**Trask Stalnaker** 55:37 Let's see, okay, a bunch of… these are, Sylvain's invoked dynamic issues, we're gonna skip over those.
We have a PR open for this, and we talked about this one earlier, and we just hit our 5-minute bump.
**Gregor Zeitlinger** 55:57 Perfect.
**Trask Stalnaker** 56:02 Alright, any last words?
**Jack Berg** 56:06 Real quick for me, so,
**Trask Stalnaker** 56:08 Oh, fuck.
Sorry.
**Jason Plumb** 56:10 No, actually, no.
**Jack Berg** 56:11 Nothing important on here I would have interrupted, but, like, the releases tomorrow for OpenTelemetry Java, I don't think that there's anything pressing that needs to get in there. If you know otherwise, please let me know.
**Jason Plumb** 56:27 I would like that no-op, but I won't lose sleep over it.
**Jack Berg** 56:31 I'll get that in, you just gotta add the same for metric exporter.
**Jason Plumb** 56:34 Oh. But there isn't one.
You want me to add it?
**Jack Berg** 56:39 There's not a NOAA metric exporter? That seems… Okay.
**Jason Plumb** 56:44 Yeah.
**Jack Berg** 56:45 Okay, I did… if you commented to that effect, then I didn't see it, but yeah, there should be a no-metric exporter for symmetry. I won't block your PR on it, but I'll…
**Jason Plumb** 56:55 I did put it in the original description, Jack.
**Jack Berg** 56:57 Oh, you did? Yeah. So I just… okay.
**Jason Plumb** 56:59 Fine.
**Jack Berg** 57:01 Going too fast.
**Jason Plumb** 57:02 Cool.
**Trask Stalnaker** 57:06 Alright.
See y'all next week!
**Gregor Zeitlinger** 57:10 Fair.
**Pranav Sharma** 57:10 Thank you.
