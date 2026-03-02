SIG: Java Declarative Configuration
Date: 2025-07-17
Duration: 51 minutes
============================================================

## Zoom Recording Transcript

**GZ Gregor Zeitlinger** 00:12 Hello!
**Robert Niedziela** 00:13 Hello, Hi.
Jason! Are you going to stay? Hold this meeting, or we'll join to this and chase.
**Jason Plumb** 00:29 I'm not sure.
Was there a different invite sent.
**Robert Niedziela** 00:37 Yeah.
**Jason Plumb** 00:38 6, yeah,
**Trask Stalnaker** 00:44 Hey folks.
**Jason Plumb** 00:45 No, I'm I'll I'm planning on staying.
**Robert Niedziela** 00:49 Okay, I will probably switch if you stay, so we'll see what what Anjay says.
**Jason Plumb** 00:57 Okay.
**GZ Gregor Zeitlinger** 01:04 Shall we give it another minute.
**Trask Stalnaker** 01:07 Yeah.
**GZ Gregor Zeitlinger** 01:12 Think Jay is still in our all hands. That is still going for 15 min. But
I'm not gonna wait that long. Okay, okay.
**Jason Plumb** 01:25 I have been mostly ignoring declarative config, but I need to be paying more attention to it. So that's why I'm here.
**GZ Gregor Zeitlinger** 01:32 Great.
**Trask Stalnaker** 01:33 Awesome.
**Jason Plumb** 01:37 Robert's been paying a lot of attention to it.
**Trask Stalnaker** 01:40 Hey?
This is your meeting, Gregor.
**GZ Gregor Zeitlinger** 01:47 Alright, then that's
**Trask Stalnaker** 01:50 Whenever you want to start.
**GZ Gregor Zeitlinger** 01:52 Start. Yeah. Let me try to share my screen.
Is it good to read?
Okay.
Now, 1st of all, there's a board that has all the issues.
I'll jump in first, st because we're probably not gonna make it through all of the issues.
Important thing here is that there is a long list of things that are awaiting review.
And then there are some things that are blocked because of other issues that are awaiting review.
Mostly, and as maybe one or 2 that depend on a release in
and contrip or in the SDK.
All right, then.
let's go back to the issues. So here I have the issues where I think it still makes sense to discuss. If the
decisions that have been going into the Prs are the right ones.
yeah, probably we have to split at some point for the next one.
1st one is about thread details which we've already discussed.
And
I think, Trask, last time you recommended that we should disable thread details by default.
and since then Laurie is actually not in the meeting, has pointed out that
the the semantic conventions recommend that they are
enabled by default. That's why I wanted to go back to that. I think it's here in the spec. Pr. That this
comment was on. So spec is not a specification repository. This is
in the instrumentation repository, but it is the Pr that explains how
I'm planning to map all the properties. And this one was about thread details.
Yeah. And we have the comment here.
So the comment says, disabled by default. And
where did Laurie have the link to the specification?
Oh, here it was, semantic conventions recommending to set these attributes.
Yeah. And they are recommended. Yeah, that's
that's what I wanted to say.
**Trask Stalnaker** 04:51 Interesting.
I'm not sure what they what that means, though, because generally
in some I probably have to take it to the some comp group to ask for clarification, because generally requirement level applies to
attributes on a span
so like in Http client span, we have a list of recommended attributes for the Http client span.
I'm not sure what a standalone requirement like level means here.
**GZ Gregor Zeitlinger** 05:34 Right? Okay.
**Trask Stalnaker** 05:35 Alright. So if you look at the Http semantic conventions.
they don't recommend thread, id and thread. Name art recommended over there.
**GZ Gregor Zeitlinger** 05:46 Okay, got it. Okay.
Now, can I then add an action item for you?
**Trask Stalnaker** 05:52 Yeah, yeah.
**GZ Gregor Zeitlinger** 05:53 Okay.
**Jay DeLuca** 05:59 Isn't the fact that they're not stable also kind of
push us towards putting them behind the flag.
**Trask Stalnaker** 06:11 Would on stable stable semcons so like for Http.
If it wasn't stable we would hide it behind a flag. But for
our PC. Since everything is unstable in our PC. We don't.
Generally do that.
**Jay DeLuca** 06:36 Okay, thanks for that. Clarification.
**GZ Gregor Zeitlinger** 06:40 All right. Yeah, the other links are just links for the implementation where this currently is in the Prs.
And then there's also the question about lock settings.
that is because I made a comment that we should also use this for logs. I think this was from the discussion.
and then Laurie pointed out that locks have a different setting right here.
And then I looked up. That logs have log for Jpender experiment log attributes, and that actually means that
the thread name is set.
yeah. Question is, does it make sense to unify that? So that we also put this under threat details? So 1st of all in the comment section, then a thread details and then probably
block or yeah, blocking, maybe.
And then I looked at
that. There is at least one that I could find that is kind of similar.
which is, add baggage and not, and that baggage and threat is the same, just that there are
different instrumentations that share common features.
Question is, if we also want to unify more under common, or if that is maybe a separate project, and we should limit it at some point.
**Trask Stalnaker** 08:27 I'm not sure. So the reason to potentially keep it separate for spans and logs.
There's a couple of reasons that come to mind. One is that logs?
people. Often when they're adopting open telemetry logs, they want the same thing. They were getting out of their log system.
Whether or not it was useful, and most log systems do dump the thread name by default
into the log message.
Another reason would be. It is a little bit of a signal specific choice like metrics like you
probably wouldn't want it on metrics because of the cardinality issue and so putting it under common.
could like it's not as clear as, or we could maybe have it under common, but common spans and common logs.
so that it is still under common, and applies to all instrumentation.
But they're still. You still can configure them separately.
like in our distro. For example, we would probably want.
Thread name on logs. Well, what we do today is we have we put thread name on logs? Just cause. That's kind of what we did historically. Pre open telemetry.
so it's more like migration story.
But we don't put thread. We don't put thread name on spans. Because of telemetry cost.
**Jason Plumb** 10:32 But we are doing that for spans right now.
**Trask Stalnaker** 10:37 But we turn it off, so we hide it in our. In our distro we suppress those attributes.
**GZ Gregor Zeitlinger** 10:43 Okay?
But in the current agent implementation it's enabled by default.
**Trask Stalnaker** 10:49 Right, right.
**GZ Gregor Zeitlinger** 11:05 So here I just laid out how we could configure it under the common.
**Trask Stalnaker** 11:25 Yeah. And I just wouldn't even make it an option on metrics until we have some kind of thread name normalization support to. Otherwise the cardinality issue is too problematic.
**GZ Gregor Zeitlinger** 11:50 Okay, so should we do it like that with thread underscore details.
Do you like that?
**Trask Stalnaker** 12:00 I think so works for me.
**GZ Gregor Zeitlinger** 12:04 And that would replace log 4 Jl. Penda. Experimental log attributes just to double check.
**Trask Stalnaker** 12:15 Yeah, unless there's other experimental log attributes.
**GZ Gregor Zeitlinger** 12:18 Yeah, I check. I checked. This is just that.
And what about
this add baggage? Is this something that you see in a similar vein? Or is this different.
**Trask Stalnaker** 12:44 Yeah, I like, we've always wanted common baggage baggagey thing.
Like to stamp baggage onto spans.
**GZ Gregor Zeitlinger** 12:59 Well, this is the the current setting is for the Mdc. It's it's it's not setting it in any signal, actually.
for spans and.
**Trask Stalnaker** 13:11 Oh!
**GZ Gregor Zeitlinger** 13:12 Have a an implementation and contrip, and that also has an equivalent for declarative configuration and a Pr.
But that is done in a different way because you configure it right where you have your exporter. So in the SDK section you have some sections that do that.
**Trask Stalnaker** 13:36 I see it's a span processor that adds the baggage. Right? Right? Yeah, that's nice.
**Jason Plumb** 13:44 May I ask a naive question.
**GZ Gregor Zeitlinger** 13:46 Sure.
**Jason Plumb** 13:47 So I think
what I'm hearing is, there's there's a couple of decisions that are trying to be made in this. Pr, like, let's just talk about thread details. There was the idea that there could. There could be one entry in the configuration for thread details, and it would be enabled or disabled, and the value of that would determine. If thread details, then, are on each of the signals. Right? That was the original kind of idea. It seems simple, great.
Some pushback is like, well, maybe we need it to be more configurable. Maybe we need it to be per signal, in which case there would be multiple entries, presumably nested somewhere
that enable or disable thread details for a signal type. Is that is that correct?
**GZ Gregor Zeitlinger** 14:28 Like I've written down in the notes here.
**Jason Plumb** 14:30 Yeah, yeah, okay, good, good, and and we're also attempting to
both set kind of a precedent for the spec while also trying to match parity for what the agent does today
is that also kind of true.
**GZ Gregor Zeitlinger** 14:49 I didn't get the last part.
**Jason Plumb** 14:52 So we have some configurations that are defaulted one way or the other
in the agent today, out of the box. And we want to. We want to attempt to match or create parity with those defaults in the in the configuration defaults.
**Trask Stalnaker** 15:08 Maybe.
**Jason Plumb** 15:09 Maybe. Okay. So that one's a little.
**Trask Stalnaker** 15:12 It's a chance to potentially reconsider
especially if we time this with 3 O.
**Jason Plumb** 15:20 Okay.
**Trask Stalnaker** 15:21 To change some defaults.
**Jason Plumb** 15:25 Like my name.
Go ahead. Okay, with now that my understanding about that, I think, is is solidified and not completely in left field, I want to ask something about specifically about the configuration itself.
Would it be possible? Does the configuration, schema and syntax allow for setting a multi-valued value for something like thread details. So if we wanted
just to riff here, if thread details was at a higher level like it is in this Pr. Could you then have a list of signals for which it is enabled, like.
if he called it thread, detailed signals, or something, and then under that you could have logs.
**GZ Gregor Zeitlinger** 16:06 This is exactly how it is, so here you can only enable signal. So I'm I have not put.
**Jason Plumb** 16:14 Got it. So it's not you haven't inverted it and put it under something. It's that it gained additional sub context that's enabled or disabled. Okay, cool. Thank you. I'm I'm playing a lot of catch up. So thanks for baby stepping with me.
**GZ Gregor Zeitlinger** 16:27 No worries. It is a complex topic.
**Trask Stalnaker** 16:31 But you can do basically, any kind of yaml modeling that we want, we can do.
**Jason Plumb** 16:38 Okay, I mean, the implementation might get might get more difficult for multi-valued stuff in some cases. But okay, that's cool.
**Trask Stalnaker** 16:46 Yeah, I think the main thing is looking at how the existing declarative config SDK, declarative config is modeled and trying to stay consistent with that.
**Jason Plumb** 16:58 Okay.
**Trask Stalnaker** 16:59 And they've gone pretty explicit like of mapping things to the SDK,
anyway. Yeah, yeah, that's a something to watch when we put these Prs in so baggage. Gregor.
the Mdc. One. So this
Mdc. One puts the baggage into Mdc.
**GZ Gregor Zeitlinger** 17:29 Yes.
**Trask Stalnaker** 17:30 Okay, so that's totally different.
Right? That's gonna stay. I think a log back. Mdc, specific config.
**GZ Gregor Zeitlinger** 17:40 That's why I thought, actually, just wanted to make sure I'm in the right direction.
Okay.
**Trask Stalnaker** 17:56 The other one, though.
the log project context data. Oh, okay, that's also doing the same thing, I see. So these are not for stamping baggage
on to the log. X are like otlp log exporter.
That's covered in the contrib repo.
**GZ Gregor Zeitlinger** 18:22 Yes.
**Trask Stalnaker** 18:22 Log processor. Nice. Okay. Perfect.
**GZ Gregor Zeitlinger** 18:28 It should be one of the
a contract that are awaiting review.
**Trask Stalnaker** 18:37 Yeah, once we have with this declarative config, I think we'll want to
pull like it would be really nice to pull in more of these contrib
modules by default into the vanilla distro.
**GZ Gregor Zeitlinger** 19:02 I think they already are, but.
**Trask Stalnaker** 19:06 Okay.
**GZ Gregor Zeitlinger** 19:07 I'm making note, if that is actually the case.
Okay, next one.
**Trask Stalnaker** 19:37 And we could consider moving those that would definitely want to chat with Lori about that
into the instrumentation repo. I don't know.
With declarative config. I feel like the story comes together more
And I could see those all being part of vanilla.
**GZ Gregor Zeitlinger** 20:04 Okay, I'll create an issue to discuss.
all right. Then, next one.
Okay. Early init properties. So last time,
I had the idea that we could have everything in a declarative configuration, like as the ideal.
But it turned out to be more difficult.
and in particular. There is this setting about so long and disabled and lock level.
They are read at a very early stage, and Laurie has explained that
pulling in a bunch of classes, especially if they're from a different project, is dangerous, because we modify some classes.
and they might emit logs, and logging has not been configured.
So he recommended that we defer that to a later stage, and that's why
Some of the properties cannot be set in declarative configuration, and my current. Pr.
and I have listed them here for reference.
Yeah. So enabled and notably debug extensions, and the logging
cannot be set. The configuration file. The old configuration file is also read at that early stage, and
for that reason it's
hard to prevent that, because you've already read it. And then, later on, you could say, Oh, by the way, this is
illegal now, which I have not done
But wanted to have some feedback on that.
Do you think that's an acceptable solution.
**Trask Stalnaker** 22:19 For the
The old config file specific.
**GZ Gregor Zeitlinger** 22:24 In general, that all of but in general
properties cannot be set in the declarative configuration file. Is that good enough for a 1st goal?
**Trask Stalnaker** 22:33 Absolutely. Yeah, I would. I am fully with Lori on. Just
this is a hard topic, and may not be
super like, Yeah, I I would just.
It's not that important. These are like,
We'll cover this by documentation.
**GZ Gregor Zeitlinger** 22:55 Okay.
**Jason Plumb** 22:57 Are we gonna continue support for that properties file indefinitely even after declarative config lands
like, I, I think we might want to get rid of it.
**GZ Gregor Zeitlinger** 23:08 You mean this property?
Yeah, file.
**Jason Plumb** 23:12 Or or the ability to use a property file at all. If if declarative config exists.
**GZ Gregor Zeitlinger** 23:18 Are you only talking about this file? Or do you also actually mean to use system properties?
**Jason Plumb** 23:25 No, I just mean the file.
**GZ Gregor Zeitlinger** 23:26 Okay.
I mean, we could throw an exception after we have read the file and started the initialization, I mean, or just stop
doing something.
**Jason Plumb** 23:44 I don't know how great
change that is. Yeah, if users are using it, then they're gonna be mad. But.
**Trask Stalnaker** 23:51 I wouldn't do it in 3 o
like. I think we need
a major version where we have declarative config, and that side by side, and then we could
consider dropping it in a major version. After that.
**GZ Gregor Zeitlinger** 24:13 So in 4.0.
**Trask Stalnaker** 24:15 We could consider it.
**Jason Plumb** 24:17 I don't have any. I don't have any data to back this up, but I have not heard of any case where a customer of ours is using that properties. File.
do y'all?
I've got if they use it.
**Trask Stalnaker** 24:29 No but I don't know how to.
Yeah. I would want to take a conservative approach on deprecating and.
**Jason Plumb** 24:43 You're very nice, trosk.
I mean, a major version. Bump allows you to do breaking changes right.
But you're very nice.
**Trask Stalnaker** 24:58 It depends on how much how much does it save us? Right like is this gonna make our lot like getting rid of this sooner. Is that going to clean up a whole ton of stuff.
**GZ Gregor Zeitlinger** 25:10 No, from the code.
**Jason Plumb** 25:12 This is.
**GZ Gregor Zeitlinger** 25:12 Isolated in one place, and it's not gonna matter.
**Jason Plumb** 25:18 Think that's a good point.
Respect.
**Robert Niedziela** 25:24 One question. If we agree not to put this properties, we talked about in a config file, how we will be able to specify them, because right now all other options are discarded. After config file is parsed.
**GZ Gregor Zeitlinger** 25:43 You mean the properties that.
**Robert Niedziela** 25:44 Yeah.
**GZ Gregor Zeitlinger** 25:45 Are listed here.
**Robert Niedziela** 25:46 Yeah, yeah, yeah.
**GZ Gregor Zeitlinger** 25:49 We would fall back to you have to use environment variables or system properties. However, you want to specify those basically.
**Robert Niedziela** 26:01 Okay, however, I think May. Maybe I'm wrong, but I I think that this config that is created before the clarity config is parsed.
It's it's discarded.
It's no no longer processed.
**GZ Gregor Zeitlinger** 26:25 I'm not sure I understand what you mean. So the declarative configuration is reading everything from a file. So whatever you want to have you have to put in the file and system. Properties are not evaluated by default, they are never evaluated. If you have the
configuration file. If you want environment variables to be evaluated, then you have to put them in curly braces in the configuration.
**Robert Niedziela** 26:55 Bye.
**GZ Gregor Zeitlinger** 26:55 As an explicit mechanism.
**Robert Niedziela** 26:59 Yes. But since we disallow using Hotel Java agent, and in in the config file, how can we use this options at all?
**Trask Stalnaker** 27:13 I like specifying at the command line, dash d hotel, Java, agent enabled equal true.
**GZ Gregor Zeitlinger** 27:22 Right. That's how you do it. Huh?
**Trask Stalnaker** 27:25 Is that what you're asking, Robert?
**Robert Niedziela** 27:27 Yes, but maybe I need to. I need to double check it. I thought, it's it's at some point translated into config properties
that at some point are no longer past.
I mean, they are just forgotten.
But maybe I over interpreted something. Okay.
**Jason Plumb** 27:49 No, I think I'm following you, Robert. So I think I think what Robert's asking is, how do we make it such that these properties still make it into the config properties when they're normally nuked. When you're using file based config, those config properties are eliminated.
**GZ Gregor Zeitlinger** 28:04 Oh, okay, I.
And maybe I'm getting it. Let's take an example. This debug. This is a property that is read in early and late stages only 2 properties. This is one of them.
and and this one is explicitly passed to an object that is responsible for configuration, so that it's carried through.
And I can actually open the pull request.
Show you where that is.
Yeah.
**Jay DeLuca** 28:39 So I I think, in general. So we'll have sort of like an allow list, or like some other mechanism, for a specific subset of configurations to not be thrown away.
**GZ Gregor Zeitlinger** 28:49 Exactly.
**Jason Plumb** 28:49 And that has to play nicely with the the stuff from declarative config from core right
cause. This is not an agents. This would not then be an agent. Specific behavior.
**GZ Gregor Zeitlinger** 29:04 It doesn't.
**Jason Plumb** 29:04 20.
**GZ Gregor Zeitlinger** 29:05 Specific behavior because.
**Jason Plumb** 29:06 Okay.
**GZ Gregor Zeitlinger** 29:07 Properties that are affected
are both Java agent properties. So it's this Java agent, Debug, and just have to look at the Pr. To find the other one
and logging here it is.
So those are. It's just a plain map that is passed to the bridge.
and all the other and properties are just
because they have either been read in the early stage, or they belong into the configuration file. If you opt into using declarative configuration.
**Jason Plumb** 29:52 I see. So it's a feature of the bridge
having having an like an exception list.
What? That's what this Pr lands is. The ability to
put an exception list into the bridge.
**GZ Gregor Zeitlinger** 30:08 Right? Yeah, the. And this was the the test. But I think.
**Jason Plumb** 30:12 This is actually the place.
**GZ Gregor Zeitlinger** 30:13 Where this is past.
**Trask Stalnaker** 30:16 And so someday, Gregor, will we get rid of the bridge like, say.
yeah, could we get rid of the bridge at some point and.
**GZ Gregor Zeitlinger** 30:32 Yes, so we have to. We have to make
2 requirements come true. The 1st one is that we get rid of this class loading problem.
And the second one is that we drop support for
the system properties. Then we can get rid of it.
**Trask Stalnaker** 30:51 What is the class loading problem?
**GZ Gregor Zeitlinger** 30:54 That in the early stage we have to be conscious about what libraries to load, I mean for Yaml loading. You need a library. Just have to make sure that this is not
impacting any of the things that we have carefully
made sure in the class loading order.
**Trask Stalnaker** 31:15 So more. I meant so early. We can still read system properties early.
But then in the instead of
at some point, instead of mapping system properties into the Via the bridge, could we update the Yaml
during startup to put those system properties where they belong.
**GZ Gregor Zeitlinger** 31:48 Yeah, that would actually also be possible. Yeah, I have not thought of that. But we have the in-memory representation. So we could also put it in there. Yeah, maybe that's even an improvement for the Pr, I have to think about that.
**Trask Stalnaker** 32:01 Okay.
**Jason Plumb** 32:03 So that would be a new component, and it would not. It would somehow be different than the bridge.
**Trask Stalnaker** 32:10 It would be populating the yaml at Startup with the things that we want.
**Jason Plumb** 32:16 Instead of.
**Trask Stalnaker** 32:17 And then we wouldn't. Yeah, and then we wouldn't. Might not need the bridge.
**Jason Plumb** 32:22 Got it.
**GZ Gregor Zeitlinger** 32:22 We actually have the the Yaml here, so you cannot really see it. But here this config provider is a wrapper around
the in-memory representation of the Yaml
I cannot see it here, but here you could access the yaml and then modify it.
**Jason Plumb** 32:45 Cool, Robert. I know you're trying to drop. Maybe did.
**Robert Niedziela** 32:50 Yeah, yeah, yeah, thank you very much. Yes.
okay. 1. 1 more thing. Maybe I would like to talk at some point. Maybe it's a subject for next meeting, or or something like that. I think we are missing one component in the whole architecture, I mean, some dedicated spi for validating the config. Because we have some customizers, we can manipulate the config in it.
and it would, I think it would be good to have some validators staff that will be launched just to make sure that, after all the manipulations we we have the valid config.
**GZ Gregor Zeitlinger** 33:32 Yeah, I'm making a note that we discuss it next. If you can add some details and can also talk about next time.
**Robert Niedziela** 33:41 Okay, okay, thank you. So yeah, see you next time.
**GZ Gregor Zeitlinger** 33:47 Alright. See you next time.
Okay, all right.
So I think all good. Here. Next one is a topic that is a Pr. In the SDK, but it's essential for us.
It's the extended open telemetry. The the goal. Here is the
Jdbc instrumentation in Jdbc, we pass in an instance of opentelemetry.
and then we want to get some settings. I can actually.
**Trask Stalnaker** 34:56 What's the code?
**GZ Gregor Zeitlinger** 34:57 Jay.
**Trask Stalnaker** 34:57 Yeah. And we don't want to rely on the global.
**GZ Gregor Zeitlinger** 35:01 Exactly. So. We've spent so much time not to use a global that it would be a pity if we had
sad. Yeah.
**Trask Stalnaker** 35:10 Yeah. The the extended open telemetry sounded like a great idea. And you know, blessed by
Jack, so I think it's probably just need
Jack and John to review, I guess this, we we could review this also. Yeah.
**GZ Gregor Zeitlinger** 35:31 I have a I have a question.
**Jason Plumb** 35:32 Do you have an account already? Do we know.
**Trask Stalnaker** 35:34 Yeah, okay.
**GZ Gregor Zeitlinger** 35:36 I have a conceptual question, that is before the Code Review.
So I have taken the implementation of Josh, as Jack suggested.
but it did not work to put this instance into the auto configured instance, and the problem is
that the auto-configured SDK returns a class, not an interface, and that class is final.
And that's not working. You cannot
return something that extends a final class. So I removed the final. But I'm
wondering if this might bring some repercussions
that I have not thought about.
**Trask Stalnaker** 36:26 To can open telemetry. SDK, implement extended open telemetry.
**GZ Gregor Zeitlinger** 36:41 Wait. But what
what would happen if you do? An instance of check? If it implements extended? SDK, it would always be true.
**Trask Stalnaker** 36:58 in order to do an instance of check. What do we do to Jack? Does some tricky stuff for these for these incubating
things.
What's the pattern that we use for? If you look at tracer? SDK,
let's look at how that's designed.
**GZ Gregor Zeitlinger** 37:30 Extended tracer. I think that's the one.
**Trask Stalnaker** 37:35 Yeah. But let's look at Tracer SDK, or who implements this.
**GZ Gregor Zeitlinger** 37:40 I'm I have the wrong project open for that tracer.
Hang on!
Maybe it works if I open that project, too.
Oh, still working.
**Trask Stalnaker** 38:19 Jason. I was playing around yesterday with Dev containers. my goal is to have the Java Instrumentation project on merge to main.
create a dev container that has the whole build cache all ready for you.
Wow! That's we'll see. We'll see how that if that helps things.
**Jason Plumb** 38:49 Yeah, that's a really cool idea.
**GZ Gregor Zeitlinger** 38:52 To make bills forward.
**Trask Stalnaker** 38:53 Support.
Yeah, if we could use. That's a good point. I had it. So I know with the reason I started down that path was because co-pilot Prs
completely fail on our repo. I've been testing it in my fork because our build just takes so damn long that and it
times it out at like 5 min every time and
the co-pilot Prs will use the dev container if you've set one up.
But yeah, I hadn't thought about that, Gregor. If the
builds, if our builds themselves could use leverage, that
what? I'm sorry I'm naive again. What is a co-pilot? Pr, I mean, I know a co-pilot.
Yeah. You can. It's recent. You can. If you have copilot license, you can assign issues to copilot
and copilot will go and do it
best. Effort to write a Pr. For that issue.
**Jason Plumb** 40:06 Oh, boy, okay.
**Trask Stalnaker** 40:08 And like 30 min later, you can see what it did.
**Jason Plumb** 40:12 Cool.
Maybe this is a feature actually.
**Trask Stalnaker** 40:17 Sometimes it's
I mean, if you once you learn, that's kind of what I'm still learning like, what kind of tasks is good at and not good at.
But it's surprisingly good at some tasks.
and surprisingly bad at some tasks.
**Jason Plumb** 40:35 Yeah.
**GZ Gregor Zeitlinger** 40:37 Like.
**Trask Stalnaker** 40:38 Fix this fix the job. I tried it with the fix the Java doc errors, and it's solution to that was to remove the dash, w error, validation from the build.
**Jason Plumb** 40:52 That is one way to address that problem.
**Trask Stalnaker** 40:55 Right, yeah, like.
**GZ Gregor Zeitlinger** 41:01 I found the class. By the way. It is doing extend actually.
**Trask Stalnaker** 41:08 Okay, so it is okay. So SDK, tracer is not final then.
So I guess that's a question I would
put that question in all. But it's.
**Jason Plumb** 41:21 Yeah, it's package.
**Trask Stalnaker** 41:22 Protect.
So open telemetry. SDK itself is, can we look at open telemetry? SDK,
what do we have in here? So it's public.
What does it add, okay, we've got a builder right at builds
final.
**GZ Gregor Zeitlinger** 42:08 I mean, and we would also have to make the constructor protected. Otherwise it's not working.
**Trask Stalnaker** 42:23 That's true. As long as the constructor is not public, other people, it's essentially other people can't extend it.
**GZ Gregor Zeitlinger** 42:36 I mean, anyone can extend it if it's protected.
**Trask Stalnaker** 42:44 As well if we can.
**GZ Gregor Zeitlinger** 42:45 Prevent that.
**Trask Stalnaker** 42:46 If we can leave this package, protected the constructor somehow. Yeah.
**GZ Gregor Zeitlinger** 42:55 Dependent, then.
**Trask Stalnaker** 42:58 In the same package.
**GZ Gregor Zeitlinger** 43:02 Okay. I'll try that.
Well.
then, it's not following the conventions that it has incubator in the package, because the extended is in the incubator.
Think I already thought about that that puzzle.
**Trask Stalnaker** 43:25 Yeah.
**GZ Gregor Zeitlinger** 43:25 Same.
**Jason Plumb** 43:28 So what's the sorry? What's the reason for? Extend like the desire to extend it is to override the config provider.
**GZ Gregor Zeitlinger** 43:39 I can actually go to the class.
It is this, and only this method that is creating the concern, and that.
**Jason Plumb** 43:52 Got it.
**GZ Gregor Zeitlinger** 43:54 Not incubating, so we cannot change it.
**Jason Plumb** 43:57 But with this pattern, this incubating and extending pattern, wouldn't we, instead have
an extended auto configuration? Open telemetry? SDK,
so we would. We would extend the auto configure stuff as well. So if you want to use an extended open telemetry SDK, you have to go through the extended auto configure.
Isn't that.
**GZ Gregor Zeitlinger** 44:20 The pattern.
Maybe maybe not. What it means, at least is that everyone, including all distributions, have to
change their usage so that they can take advantage of this right now.
**Jason Plumb** 44:38 Correct.
**GZ Gregor Zeitlinger** 44:39 You wouldn't. That is the implication
extended instance, polymorphically, without doing anything.
**Jason Plumb** 44:49 You said the P. Word, and it makes me very twitchy.
**GZ Gregor Zeitlinger** 44:52 I'll take it back.
**Jason Plumb** 44:57 I feel like we've worked together long enough that you know that. But no, I I mean, I see where it's coming from. It does make it nice.
**Trask Stalnaker** 45:07 So if we don't go, I'm wondering like, can we make configuration not blocked on this
for now, because configuration, they are trying to stabilize the configuration spec.
at which point we would be able to
add the configuration to the open telemetry instance itself.
So what has what did Josh do
that? How did did Josh not run into this problem?
**GZ Gregor Zeitlinger** 45:47 No, because he had not considered this use case. This is not working in his Pr.
**Trask Stalnaker** 45:54 So. He is not extending open telemetry. SDK he? What is he doing.
**GZ Gregor Zeitlinger** 46:03 Yes. Making an implementation that implements extended open telemetry. SDK, but that is not extending anything.
**Trask Stalnaker** 46:20 Okay, and he made open to address Ck. Not final. Then.
**GZ Gregor Zeitlinger** 46:28 No, no, he he left opentelemetry SDK as final
extended opentelemetry. SDK is not extending it.
**Trask Stalnaker** 46:36 Oh, I see right, it's a separate got it? And this is the pattern sort of that Jason was suggesting here.
**Jason Plumb** 46:45 Yeah. Extended. Returning. Extended. Right?
**Trask Stalnaker** 46:49 Right.
**Jason Plumb** 46:49 Yeah.
I there was. That's just from memory around the logging stuff, like, I think I thought that that's how it worked as well.
But it's been a little bit.
**Trask Stalnaker** 47:02 Yeah. And also Jack kind of reworked all of that.
**Jason Plumb** 47:05 Okay.
**Trask Stalnaker** 47:06 At some point.
Yeah, Gregor, I mean, I think my recommendation would be leave a message in slack sort of about
this problem.
But try to find a way forward in the instrumentation repo.
Just go ahead. And if you need to hack some global accessors, for now that's fine, we'll clean it up. Once the configuration stabilizes and lands in the open telemetry
class itself.
**GZ Gregor Zeitlinger** 47:54 This is only an issue for library instrumentation. The agent instrumentation already use global state.
**Trask Stalnaker** 48:02 Okay.
**GZ Gregor Zeitlinger** 48:04 So we can just say that we defer this problem until stabilization, or until we have a better idea.
**Trask Stalnaker** 48:11 Yeah, I think that's okay for library. If that's just a limitation. That library instrumentation doesn't support
declarative configuration until stabilization.
And we'll essentially be working through all the issues via the Java agent stuff. And so it should be pretty easy to then
flip that support on once it's stable.
**GZ Gregor Zeitlinger** 48:44 Okay.
**Jay DeLuca** 48:46 Don't, don't most of the libraries don't they not support the environment, variables and system property, like.
I think, mostly configured. Yeah, through the builders, so it seems pretty natural to me to not support them in declarative
config, at least initially.
**Trask Stalnaker** 49:06 Yeah, it will be super nice, though, to that's been a
downside a kind of a glaring defect of our library instrumentation.
So it'll be super nice to be able to support that. But yeah, that's a good point that it's not. We're not losing anything for now.
**GZ Gregor Zeitlinger** 49:26 Yeah, that's cool.
Well, we're losing a bit of consistency. You could say that because
the library instrumentation would still be using
the system properties, even if they have adopted the declarative configuration.
**Trask Stalnaker** 49:49 What Jay was just saying. That which I think is true is the library instrumentation doesn't support system properties
today.
**GZ Gregor Zeitlinger** 49:57 Isn't.
**Jay DeLuca** 50:00 Pretty sure they don't.
**GZ Gregor Zeitlinger** 50:02 Okay. Then.
**Jay DeLuca** 50:02 You know, when I was when I was documenting the the configs, I didn't see any in the in the libraries themselves. Just the job agents.
**GZ Gregor Zeitlinger** 50:11 Yeah, I think we had that.
**Trask Stalnaker** 50:13 We had this problem where we don't have a kind of public configuration standard configuration thing.
And so yeah, we just made
setters for everything, and left it at that.
**GZ Gregor Zeitlinger** 50:36 I think it is, but I'll double check.
Okay, hmm, don't have time for
both. I'll actually switch the order of that, because that potentially taking more cycles.
Who to finish I don't know what's wrong here. So known Http methods.
**Trask Stalnaker** 51:12 And, Gregor, let's let's stop at 5 till just so we can have a break before the next meeting.
**GZ Gregor Zeitlinger** 51:19 Yeah.
Oh, no, let's just make the break here. It does. It's not so important.
**Trask Stalnaker** 51:26 Okay, cool, awesome. This was great.
**GZ Gregor Zeitlinger** 51:31 And see you in 9 min.
**Jay DeLuca** 51:34 Nice. Yeah.
**GZ Gregor Zeitlinger** 51:36 I.
