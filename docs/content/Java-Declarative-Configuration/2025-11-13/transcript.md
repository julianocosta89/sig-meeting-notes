SIG: Java Declarative Configuration
Date: 2025-11-13
Duration: 50 minutes
Zoom Recording URL: https://zoom.us/rec/share/Vv9cEgJ9LRI7ZoQLVHADPaWPfu-KxkJwW0JxIdJxlBePLDowJSGv3pPROQSLp2Gt.5hZs0YrJ5oW9e15m
============================================================

## Zoom Recording Transcript

**GZ Gregor Zeitlinger** 00:26 Hello!
**Prasad Sawool** 00:35 Hello.
**GZ Gregor Zeitlinger** 01:43 Hi, Jay!
**Jay DeLuca** 01:49 Hey, hey, how's it going?
**GZ Gregor Zeitlinger** 01:52 Good.
**Jay DeLuca** 01:56 I wonder if we're… is KubeCon?
Still going on?
Do you know?
**GZ Gregor Zeitlinger** 02:04 It is CubeCon week, yeah?
**Jay DeLuca** 02:09 I wasn't sure if it ended yesterday, or…
**GZ Gregor Zeitlinger** 02:16 Oh, it's Thursday, yeah. Let's see if… We have any messages in… And the channel… Trust didn't say anything.
**Jay DeLuca** 02:31 No, not that I saw.
**GZ Gregor Zeitlinger** 02:44 Ow.
**Jay DeLuca** 02:45 There he is.
**Trask Stalnaker** 02:47 That is…
**Jay DeLuca** 02:48 Let's fix that.
Hey, Trask.
**Trask Stalnaker** 02:53 Hey, fuck!
**GZ Gregor Zeitlinger** 02:54 Hey.
**Jay DeLuca** 02:56 Are you at KubeCon this week?
**Trask Stalnaker** 02:58 I was. I flew home last night.
I'm home. Yeah…
**GZ Gregor Zeitlinger** 03:15 I saw that Jack Shirazi put a topic on there, but now that I'm looking at the agenda.
I'm not sure if this was meant to be for this or the general meeting.
**Trask Stalnaker** 03:28 Oh, probably the… Probably the general.
**GZ Gregor Zeitlinger** 03:35 And I'll just… Just, cut that and put it in the general section.
I have quite a lot of topics,
which are mostly PRs, probably not gonna make it, but…
Let's see how far we can get.
**Trask Stalnaker** 04:01 Okay.
Alright, thread details…
**GZ Gregor Zeitlinger** 04:17 Yeah, we… I think we discussed this two weeks ago, I don't know if you remember.
Otherwise, I'll just give you a recap before you jump into the… all the… Discussion there.
**Trask Stalnaker** 04:31 Yeah, we were gonna try to put it in the instrumenter.
**GZ Gregor Zeitlinger** 04:36 Yeah, and my first take was to have a bridge that, That works,
Like, the instrumentation bridge that we have, but for this case.
for these last use cases as well, and
No, sorry, that was a different… that was a different PR.
Now I got confused. Yeah, yeah.
**Trask Stalnaker** 05:03 Okay, Hara, let's jump in, this check shouldn't… Right.
Yeah. Ideally, it wouldn't depend on the incubator, but… Today, It does.
**GZ Gregor Zeitlinger** 05:23 Yeah, it already does, so that's not a new thing.
**Trask Stalnaker** 05:26 Okay.
Can I share it too, okay.
Okay, let's look at the implementation.
**GZ Gregor Zeitlinger** 06:01 Gloria also put some good, comments in there that I left open,
Because they were not clearly resolved.
**Trask Stalnaker** 06:11 So, directly in the builder… If it's… Okay, open telemetry extended…
Open telemetry…
**GZ Gregor Zeitlinger** 06:37 Yeah, so there are two parts to it. The one is if this should be Agent Spring Starter specific, or this is… if this is a setting that
Put, apply everywhere, and depending on the outcome, the name will have to be adjusted. Okay.
And, the other question was whether this is technically sound. Like, can you disable it?
And I think it's technically found.
**Trask Stalnaker** 07:13 Where is the, property… How do you… how do you disable or enable it?
**GZ Gregor Zeitlinger** 07:24 It's in the, and.
**Trask Stalnaker** 07:29 Oh, I see. Yes, yes, yes, right.
**GZ Gregor Zeitlinger** 07:39 And you're only going into this if block if you have a declarative configuration block, so you're always able, to,
enable it.
It's disabled by default.
**Trask Stalnaker** 07:54 Okay.
So we'll need to, I mean, we need to preserve the existing behavior in the 2X agent.
**GZ Gregor Zeitlinger** 08:09 the existing behavior.
**Trask Stalnaker** 08:12 Adding.
**GZ Gregor Zeitlinger** 08:13 Argument doesn't apply, because this is only for people who have opted into declarative configuration.
**Trask Stalnaker** 08:21 Oh, are we not removing the span processor?
**GZ Gregor Zeitlinger** 08:27 No, this is an additional task that I left out to discuss if we should also change it for existing.
I…
**Trask Stalnaker** 08:38 Okay.
**GZ Gregor Zeitlinger** 08:39 Technically, it would be possible, but I would leave that as an additional task.
So that it's easier to review it one by one.
**Trask Stalnaker** 08:50 So, if somebody opts into this today, won't they get it stamped twice? They'll also have this ban?
processor.
**GZ Gregor Zeitlinger** 09:00 No, because you have two sets of callbacks, and you're only getting, either the set for declarative configuration or the traditional ones.
**Trask Stalnaker** 09:20 Oh, and so where in… so is the span… is the thread details span processor already disabled for declarative config?
**GZ Gregor Zeitlinger** 09:30 Yes, implicitly, because it's not… not called…
**Trask Stalnaker** 09:35 Okay.
Okay, that's, yeah.
Otherwise, thread details.
I see, okay.
the customizer…
Laurie mentioned Keston.
**GZ Gregor Zeitlinger** 10:26 Yeah, this is a related question of if we want this to be…
always baked in, or if this is something that should be, like, wrapped around, and that translates to, should it also apply to native instrumentation by default?
**Trask Stalnaker** 10:49 Yeah, that's a good… I mean, that's a good question. I don't… have a, I mean, it…
It's kind of nice not to have thread details baked in to the instrumenter.
itself?
like, it's a SEMCOM, it's kind of nice to have that separate.
At the same time, it's kind of nice for that to be global for everything.
Like, you're op… you get that always?
But I like the customizer, I think it's worth… Let's see… Disabling it.
Since it could be produced without the…
Do you understand this?
**GZ Gregor Zeitlinger** 11:43 I think this is where he is getting it wrong.
that we need a different way of disabling, for users that do not have this extended open telemetry instance, but
You only have the extended open telemetry if you have declarative configuration, so you can always put it in your configuration.
**Trask Stalnaker** 12:12 Okay.
How much complexity would it add to bring in… because, it would be nice to see…
For this to be unified.
It's kind of weird to have the… thread, span, processor…
Oh, but it would be a breaking change, I see, because span processors…
apply to even the manual instrumentation that's not using Instrumenter Builder.
**GZ Gregor Zeitlinger** 13:01 Alright, let's go a step back. Are you.
**Trask Stalnaker** 13:04 Yeah.
**GZ Gregor Zeitlinger** 13:05 Are you… Do you like the idea that,
Even native instrumentation have this feature? Or do you think it should be something only for starter and agent?
That kind of decides, Which, options we have for implementing that.
**Trask Stalnaker** 13:37 So what is our current config? We're saying… I see, we're putting it under… Yeah, I… kinda…
Maybe it should be… on… maybe it should be limited to Starter and Agent.
And the reason I was saying that is because… it…
We would then have it under those distros, the configuration option under those distros.
Because it applies only to Instrumenter Builder.
Right, and not the entire Java… API SDK?
**GZ Gregor Zeitlinger** 14:21 Isn't everyone, using the instrumenter Builder when they're creating a new instrumentation?
**Trask Stalnaker** 14:30 We are, but users… users aren't… a lot of users use just OpenTelemetry API to create a span.
Even if you go to our docs, I assume…
**GZ Gregor Zeitlinger** 15:01 I'm wondering if that is a valid argument, considering… What other settings we have.
So, in other words, I think we already have settings that, that only say Java,
And where you could make the same argument.
Q1?
**Trask Stalnaker** 15:26 Do we have a list of… do we have a list of all the settings somewhere that we…
**GZ Gregor Zeitlinger** 15:34 We… do, Jay!
Do you have a good…
Good one, we can see all the settings.
**Jay DeLuca** 15:44 Just… Oh, wait, not that.
**GZ Gregor Zeitlinger** 15:48 I think just, looking for hotelinstrumentation.java.
**Jay DeLuca** 15:52 If you click on, the configurations.
tab right there. These are all the agent ones that I've documented so far. Is this what you're looking for?
**GZ Gregor Zeitlinger** 16:02 Exactly.
**Trask Stalnaker** 16:04 But for… Declarative config.
**GZ Gregor Zeitlinger** 16:09 No, no, I think Jay is right, because all of those are translated using the bridge into declarative configuration. Oh, okay. So what we are looking for is things that are, like, common. I think common.
**Trask Stalnaker** 16:24 Common.
**GZ Gregor Zeitlinger** 16:25 That is exactly what we're looking for.
**Trask Stalnaker** 16:36 I see, so… what instrumenters… would… do what… Instrumenters should look at thread details… And… config, and add that.
To their own instrumentation, if they're instrumenting directly with the… API.
**GZ Gregor Zeitlinger** 17:05 I… yeah, I would say so.
**Trask Stalnaker** 17:12 Makes sense.
I think that makes sense.
So it's an intent that you would like thread details on everything, whether all of your instrumentation supports this config is a different story, but that's okay.
Because it's one of these common ones.
**GZ Gregor Zeitlinger** 17:39 Do we actually…
**Trask Stalnaker** 17:40 have a common… node…
**GZ Gregor Zeitlinger** 17:46 common mode?
**Trask Stalnaker** 17:47 Node, node.
**GZ Gregor Zeitlinger** 17:53 Yeah, this, is translated, so everything after hotel instrumentation is the first level under Java in the instrumentation bridge.
**Trask Stalnaker** 18:14 Okay, right, we have the general ones that are spec'd out, and then we have the Java…
**GZ Gregor Zeitlinger** 18:22 Yeah, there's no example for comment, maybe that would have been actually nice to add.
**Trask Stalnaker** 18:27 Okay, but yeah, you have, yeah, so instrumentation… pause under…
**GZ Gregor Zeitlinger** 18:48 Yeah, some of the common ones are actually not supported yet.
**Trask Stalnaker** 18:52 Okay.
So…
It is an intent… So, let's see…
**GZ Gregor Zeitlinger** 19:19 So I think both approaches are defensible, and they are consistent.
Either having it specifically for agent and starter, or having it globally.
**Trask Stalnaker** 20:09 Instrumenter Customizer…
Okay.
Yeah, I think that's… Okay…
I think that's okay. I think that… I like that.
Anything else we need to decide on?
I guess whether this is common.
**GZ Gregor Zeitlinger** 20:44 Yeah, yeah, that's a good point. If we're, making this analogous to the other ones, yeah.
Yeah, good point.
**Trask Stalnaker** 22:05 I'm just… I think we had…
Are we… oh, no, we're saying it will be off by default in declarative config already.
**GZ Gregor Zeitlinger** 22:18 Right.
So, we, can consider also making it off… Or… A traditional configuration, if If this is important.
**Trask Stalnaker** 22:42 Yeah.
**GZ Gregor Zeitlinger** 22:46 Yep.
**Trask Stalnaker** 22:47 I think we might have an issue for that, I forget.
Okay.
**GZ Gregor Zeitlinger** 22:53 Thanks a lot.
**Trask Stalnaker** 22:54 Move on… To bridge or not to bridge…
**GZ Gregor Zeitlinger** 23:02 Yeah, that was one that I was answering in the beginning. I thought I had the order differently.
So my first PR two weeks ago was to have another declarative configuration bridge, and here I do it basically manually.
And,
It felt quite verbose, but there are already some comments on making other utility functions that reduce
The verbosity, without,
Having a straight bridge that, makes it indistinguishable if you're using declarative configuration or not.
Just look at the changes to see if this is… if this feels too verbose or not.
I think that's…
**Trask Stalnaker** 23:58 Sure.
**GZ Gregor Zeitlinger** 23:59 That's a good starting point for the discussion.
**Trask Stalnaker** 24:04 Okay, so… We check, okay, benefits extended, we get declarative config… The default is false.
Get structured, get structured… else do this.
Okay.
I understand that.
What's the sanitization enabled?
**GZ Gregor Zeitlinger** 24:37 The rest is basically just extracting methods. That's really all there is to it.
**Trask Stalnaker** 24:45 Okay, so what is the… What's the concern with this?
**GZ Gregor Zeitlinger** 24:53 First, that it, makes the code, longer, so,
Harder to understand, and second, that this is another
Thing, where you can add typos, and where you,
Might want to add tests to make sure that you are not misspelling
Parameters to parameter, just in the one case and not in the other.
**Trask Stalnaker** 25:19 I see, so the… it's the question of whether it's okay for this to be if-else.
Or if there should be a common thing where you pass in something like this for the same constant, or… Correct.
I see.
**GZ Gregor Zeitlinger** 25:35 Yeah, and this is what my previous PR already did, so we have this as a comparison.
**Trask Stalnaker** 25:52 I mean, I like this.
If we were going to bridge…
I would want to try to bridge in the direction of… Having this exposed
Through, kind of, a fake instrumentation config.
**GZ Gregor Zeitlinger** 26:17 Yeah, that's also a possibility, right.
**Trask Stalnaker** 26:21 Because this is the forward-looking… API.
**GZ Gregor Zeitlinger** 26:25 Huh.
**Trask Stalnaker** 26:26 So that… this is what I would… Want to, promote.
**GZ Gregor Zeitlinger** 26:34 Right, yeah, just add that as a comment, then I'll…
**Trask Stalnaker** 26:37 Okay.
**GZ Gregor Zeitlinger** 26:38 Try that out, and then we can discuss it in two weeks.
**Trask Stalnaker** 26:42 Okay.
**GZ Gregor Zeitlinger** 27:02 That's also good input for,
the distro that I'm still playing around, how distros,
can support both styles without copy… copying everything, and if this is a good approach, then I will also apply it there.
Or propose it there.
**Trask Stalnaker** 28:04 Yeah, that would… I mean, I don't… Yeah, so instrumentation…
**GZ Gregor Zeitlinger** 28:28 Oh, so that we can also apply it everywhere else where we're using Yeah, yeah.
**Trask Stalnaker** 28:33 Yeah.
**GZ Gregor Zeitlinger** 28:34 I like that idea.
Then we can eventually get rid of the current bridge that we have.
**Trask Stalnaker** 28:41 Yeah.
Yep. I have no idea if it's gonna work.
**GZ Gregor Zeitlinger** 28:47 I, I, I think it will, yeah.
**Trask Stalnaker** 28:57 Alright, I saw…
**GZ Gregor Zeitlinger** 28:59 Let's skip that one.
**Trask Stalnaker** 29:00 Yeah, I think we need Jack.
**GZ Gregor Zeitlinger** 29:03 Jack already responded to it, so…
That was after I put everything on there.
**Trask Stalnaker** 29:11 What did… just curious, but.
**GZ Gregor Zeitlinger** 29:15 That is, actually related to it.
**Trask Stalnaker** 29:21 Oh, what did I do?
Oh, you have the… a different link there. Okay, no problem.
**GZ Gregor Zeitlinger** 29:33 That's the one that, that is related to the.
**Trask Stalnaker** 29:37 No resource.
Okay.
So, shall we go on?
**GZ Gregor Zeitlinger** 29:42 Yep.
**Trask Stalnaker** 29:43 Okay.
Extended open telemetry.
**GZ Gregor Zeitlinger** 29:50 Oh, I think this is… might already have been approved.
**Trask Stalnaker** 29:54 Yeah… Cool.
**GZ Gregor Zeitlinger** 29:58 Yeah, okay, that was going faster than, I thought.
Very, very good.
**Trask Stalnaker** 30:08 Alright, alright, this is a biggie.
But I know you want this, you want to get this into the release.
**GZ Gregor Zeitlinger** 30:16 Yeah, Laurie has already been a great help. He caught some use cases that I haven't thought about.
I… yeah, I need,
his review again, because he already looked into it. Jay already looked at it, but,
I think there's nothing, no outstanding question to discuss.
**Trask Stalnaker** 30:45 We've got new public API… Oh, just annotations.
Yeah.
**GZ Gregor Zeitlinger** 30:54 Yeah, and this is an access class that cannot be put in an internal Package.
Okay. That was actually Laurie's, suggestion to,
to create a, access class.
**Trask Stalnaker** 31:10 Okay, great. So let's… yeah, I think it will be better, given the extent of this one, for, wait for Lori to…
**GZ Gregor Zeitlinger** 31:23 Huh.
**Trask Stalnaker** 31:24 I'll hopefully look at it.
And I don't mind holding the, we can check with him if he thinks this is realistic to get this into this month's release. I don't mind holding the release until, you know, next… early next week, if that helps.
**GZ Gregor Zeitlinger** 31:45 Quote…
**Trask Stalnaker** 31:50 Alright, inferred spans…
**GZ Gregor Zeitlinger** 31:57 Yeah, we discussed, that in the meeting last week, and now Jack Shirazi, has it. Oh, perfect.
So I think it should be ready.
**Trask Stalnaker** 32:10 Just… Quick peek…
Oh, a lot of changes here.
Oh, I see, you pulled it and refactored it.
to.
**GZ Gregor Zeitlinger** 32:34 Yeah, yeah, I'm glad that's making it big.
**Trask Stalnaker** 32:37 Okay.
Where is… okay, this is our declarative config change.
Very strange.
I see, and then you're just looping.
**GZ Gregor Zeitlinger** 32:53 Yeah, it turned out, that,
The intent of the author was to use dot…
In a different way than we… commonly used.
**Trask Stalnaker** 33:08 Okay, and… This is the configuration bridge. Okay.
And so, possibly… if that…
Or, if bridging in the other direction does work, would we come back and replace these?
**GZ Gregor Zeitlinger** 33:28 Yes, of course. We would replace,
Every instrumentation… every case of someone getting, a configuration thing.
**Trask Stalnaker** 33:43 Alright, alright.
Warnings… Let me, what discard it.
**GZ Gregor Zeitlinger** 33:51 Yeah, this is just, just a one-liner.
**Trask Stalnaker** 33:59 YAML declarative config. Okay.
Yeah, we can… there's not…
The… this month's release already went out, so let's…
I think let's wait for Jack on that.
Okay, on distro support… Date native image.
**GZ Gregor Zeitlinger** 34:27 Did you click on the right link? Or did I… maybe I didn't put the right link?
**Trask Stalnaker** 34:31 Yeah, maybe the wrong link there.
**GZ Gregor Zeitlinger** 34:37 Yeah, yeah, it's… it's the wrong link, right?
**Trask Stalnaker** 34:40 Okay.
this one.
**GZ Gregor Zeitlinger** 35:16 Yeah, but I think I wanted to have the link to my POC.
Just a… just a second.
Okay.
There it is.
**Trask Stalnaker** 36:05 Okay.
Support for declarative config POC…
**GZ Gregor Zeitlinger** 36:16 Yeah, this is, again,
about the declarative config bridge, at least this is the part I think we should discuss first.
And I… I had a deep link in there…
I also forgot.
Yeah, this, declarative config property customizer, this is effectively a bridge and the PR.
Can you… can you open the pull request?
**Trask Stalnaker** 37:37 Yes.
Yeah.
**GZ Gregor Zeitlinger** 37:43 Just look at the…
**Trask Stalnaker** 37:48 This.
**GZ Gregor Zeitlinger** 37:48 Yeah, exactly.
So this is also doing string manipulation and splitting.
And what this allows us to do is, half,
Have an abstraction so that, distributions that want to set default values
Don't have to do the work twice.
And you can see this in the file…
Grafana Declarative Configuration Customizer Provider.
It's calling the customizer, and then it's saying add properties.
And it's, splitting the properties, and then adding them, to the, to the YAML model.
And by doing the splitting, the distro does not have to add the property in both sections…
And the plane properties, and the structured properties.
**Trask Stalnaker** 39:24 Right… Now, if we did have… Ayy… Bridge… from…
system properties, if we created a fake declarative config, if a user's not using declarative config.
And we created a fake declarative config based on system properties.
would we need… any of this? Or could we just tell distros, just use declarative config?
In the fu- going forward.
**GZ Gregor Zeitlinger** 40:12 So, if I understand you correctly,
the distro author would add their properties in the YAML structure, so writing them to the YAML structure, and then pass this YAML structure to the
what is it, actually? Is it a customizer? And the customizer would then turn this into…
let properties that are consumed by the traditional SDK setup.
Is that roughly what you're thinking?
**Trask Stalnaker** 40:52 No, I think I got us confused.
Let me, like… So… you're adding properties, so…
Let's take an example of,
One of the… can we take a specific example?
**GZ Gregor Zeitlinger** 41:15 Yes, sir.
The Grafana config customizer provider has, the three properties that are used in this distro.
**Trask Stalnaker** 41:27 Grafana… This guy.
**GZ Gregor Zeitlinger** 41:33 Exactly.
**Trask Stalnaker** 41:34 Okay.
Oh, I see, you're overriding the default.
**GZ Gregor Zeitlinger** 41:45 Huh? Yes.
**Trask Stalnaker** 41:46 Yes, I understand.
So, what if… the agent… When it starts up.
It sees that, oh, there's no declarative config, so it converts all of these into the declarative config model.
And then… You would not provide default properties like this, but you would…
customize the model, so you would only interact with declarative config, and you would add these nodes…
To the declarative config model.
**GZ Gregor Zeitlinger** 42:35 Right.
So, to summarize, if the user is not using declarative configuration, the, distro author…
And also the instrumentation.
what is… still use the new API, so that we can finally get rid of the old API.
**Trask Stalnaker** 43:01 Yeah.
And then we basically prove out… we have to… then that kind of leans us into the declarative config all the way.
And forces us to deal with if we have… if our…
Declarative config model story isn't good for setting defaults, then we need to fix that.
**GZ Gregor Zeitlinger** 43:26 Yeah, that's actually a good nudge to fixing this problem.
That would also mean that we are deprecating all the other callbacks for extensions, because,
If you're saying you, work on the YAML node, then you cannot use…
Callback methods that… that just don't know about this.
**Trask Stalnaker** 44:02 Yeah, oof, I think…
Yeah, I mean, we can… so we can make that breaking change in 3-0.
The question is… How do we… Not break people…
In… two acts.
If we start… Ugh.
**GZ Gregor Zeitlinger** 44:35 Well, we are not breaking anyone.
We just, don't have, like, the…
Easiest possible experience for distributions that want to support declarative configuration.
Could also put it that way.
**Trask Stalnaker** 44:52 But they already have existing… like, this is already in your distro.
**GZ Gregor Zeitlinger** 44:59 This is a PR, I haven't merged this.
**Trask Stalnaker** 45:02 Right, but I mean, you already have an auto-config customizer provider in your distro.
**GZ Gregor Zeitlinger** 45:11 Right.
**Trask Stalnaker** 45:13 That already works on… These system property names.
**GZ Gregor Zeitlinger** 45:19 Huh.
**Trask Stalnaker** 45:21 So, we need to not… break your…
distro…
**GZ Gregor Zeitlinger** 45:35 And two artists never…
**Trask Stalnaker** 45:37 In two, in two.
We can break it when we go to 3.
**GZ Gregor Zeitlinger** 45:46 And maybe it is, reasonable to say that,
the distro story will only be smooths in three. I mean, it's not impossible right now. This spreadsheet that I have created is a temporary workaround that other.
**Trask Stalnaker** 46:03 Right.
**GZ Gregor Zeitlinger** 46:04 Authors could also use.
**Trask Stalnaker** 46:07 Well…
we need to set that… we need to provide that, sort of, that bridge, I think, automatically into… somehow.
Right, so… If you have your…
existing distro, or extension, really. Distros, I don't care about breaking distros.
So much, I care about breaking extensions.
**GZ Gregor Zeitlinger** 46:34 Because distros sort of have to be recompiled against…
**Trask Stalnaker** 46:37 The agent every release anyways.
But for an extension, if you have an extension that has a customizer provider that
does this, provides these… attributes.
you shouldn't need to… you should be able to take the latest 2X version.
And you shouldn't need to change anything in your code.
**GZ Gregor Zeitlinger** 47:04 I don't agree. You're making a…
A change by introducing declarative configuration.
So it's not happening automatically.
**Trask Stalnaker** 47:19 If your user is using declarative config.
I agree that… that can break. That's gonna break you.
But… If you… if the user…
He is not using declarative config.
So if… if everything in your environment is the same, and you just go bump from 2.21 to 2.22,
that shouldn't break anything. You shouldn't need to recompile or…
**GZ Gregor Zeitlinger** 47:51 Oh, you're talking about that, okay, I thought you were talking about something else, right?
**Trask Stalnaker** 47:59 just adds a… Another wrinkle.
But, yeah, so… So, I think that is…
That is the trick, is can… how do we…
how do we move forward in 2X, where…
We can start having instrumentations using the declarative config, API exclusively, But we still… Don't break old usages.
Until we can drop that in 3.
**GZ Gregor Zeitlinger** 48:44 Yeah, let me… I'll just add that here as a comment in the document.
There's no good name For not declared of configuration.
I always struggle. Now I say plane properties.
**Trask Stalnaker** 49:27 System property… system properties…
**GZ Gregor Zeitlinger** 49:32 Yeah, that's better.
Yeah, I like that as a goal. That gives me something to… to, think about.
**Trask Stalnaker** 49:49 Hit your head against…
**GZ Gregor Zeitlinger** 49:51 Exactly.
**Trask Stalnaker** 49:54 Cool.
Alright, shall we take a break?
**GZ Gregor Zeitlinger** 49:58 That must… That was a really productive one. Thanks a lot. See you in 10 minutes!
**Trask Stalnaker** 50:04 Yep.
Bye.
