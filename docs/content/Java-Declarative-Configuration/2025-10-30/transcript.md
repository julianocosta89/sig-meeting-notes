SIG: Java Declarative Configuration
Date: 2025-10-30
Duration: 36 minutes
============================================================

## Zoom Recording Transcript

**GZ Gregor Zeitlinger** 05:28 Hello!
**Prasad Sawool** 08:15 Will this be starting soon, or will we resume at 12, 9.30?
**GZ Gregor Zeitlinger** 08:22 Just waiting for Trask, he said he wants to join.
**Prasad Sawool** 08:29 Okay, sure.
**Trask Stalnaker** 08:56 Hey folks, sorry I'm running late.
**GZ Gregor Zeitlinger** 09:00 Hi, Trask.
**Trask Stalnaker** 09:02 There you go, girl.
**GZ Gregor Zeitlinger** 09:09 So I… I'm joining from my phone today, because my internet is slow, and I want to see if it's my computer.
**Trask Stalnaker** 09:16 Huh.
**GZ Gregor Zeitlinger** 09:18 But I can see you if you want to share your screen.
**Trask Stalnaker** 09:23 Sure.
Clear it up, config. Alright, what do we got here?
**GZ Gregor Zeitlinger** 09:45 We have some topics, I already looked at it before.
**Trask Stalnaker** 09:56 Got it.
Okay, let me just fix up the…
I can never figure out the fonts on this page. It's ridiculous.
Oh, yeah, right.
Alright…
**GZ Gregor Zeitlinger** 11:14 Should I… start?
**Trask Stalnaker** 11:17 Yeah, yeah.
**GZ Gregor Zeitlinger** 11:19 So, the declarative config bridge is back.
And, this is, the work, that resulted from the extended open telemetry.
Do you remember what this is about?
**Trask Stalnaker** 11:39 Extended open telemetry?
**GZ Gregor Zeitlinger** 11:41 Right.
**Trask Stalnaker** 11:42 Yes, yes, to access the config provider.
**GZ Gregor Zeitlinger** 11:46 Right, and after that has been merged, I, took a look at how we could take advantage of it.
And, the pattern that,
I saw is that we are reading system properties directly.
In places where we don't have the config properties object,
at hand, no, not config properties, but the instrumentation config object, because these are places that are read early, or for some reason don't have access to it.
And… what I did is I created another… Interface, that,
Reads the system properties directly if there is no declarative configuration.
But, uses declarative.
configuration if the OpenTelemetry instance is an instance of the extended OpenTelemetry.
And then it, looks at the declarative configuration object.
And, this turned out to be a very similar pattern to the declarative config bridge. Indeed, it is so similar that I extracted the common code, and that is what this
PR is about.
So, conceptually, this is different because the new declarative config bridge is an API thing, where the old one was an SDK thing.
That is because config properties is an SDK thing.
Or maybe an auto-configure thing, but not an API thing.
Whereas extended open telemetry is an API thing.
And, therefore, it made sense to add it to the
Instrumentation API, or API incubator, actually, because it's incubating.
And what I did is, that I… import it.
The common part of the declarative configuration in the…
instrumentation API, and I just excluded the SDK part so that instrumentation API would not suddenly
turn into an SDK thing.
This is a takeaway from the feedback last time, that… that you gave Trask, that,
We should, Keep those two aspects separate.
**Trask Stalnaker** 14:49 Yeah, is… So my initial preference is to… the instrumentation API To only depend on… the,
the API… Like, the… the real declarative conf… like…
Can we avoid having the instrumentation API use the declarative config bridge, the bridge?
And just keep instrumentation API clean.
What are the properties that we need to access? Is it just… is this the only one?
That's been…
**GZ Gregor Zeitlinger** 15:42 If you scrolled through…
**Trask Stalnaker** 15:43 suppression.
**GZ Gregor Zeitlinger** 15:44 If you go over the usages, like, everything that's in the instrumentation package, then you can see how it's actually used. Maybe it's good to start from that angle, like here on the left.
**Trask Stalnaker** 15:57 Left side.
**GZ Gregor Zeitlinger** 15:57 Bottom of the screen, AWS.
That's… that's one of them. And you can see how it's used.
**Trask Stalnaker** 16:12 Right, right, so we were supporting, even though we were trying not to support config system properties in instrumentation.
We were in a few places.
**GZ Gregor Zeitlinger** 16:27 Exactly.
That's how we got into this situation.
**Trask Stalnaker** 16:34 So… Do you think we could… I mean… Maybe this is… would just…
Make this a braking change in 3-0.
That these system properties are no longer supported in these instrumentations, and…
You have to use declarative config.
**GZ Gregor Zeitlinger** 17:06 Mmm…
So you're saying that, we would use the declarative configuration API directly here, instead of having this new kind of bridge?
**Trask Stalnaker** 17:19 Yeah.
**GZ Gregor Zeitlinger** 17:26 That is a possibility, but what… what's your,
argument against, using the bridge? Is it because it's…
Too complicated, or… what is it?
**Trask Stalnaker** 17:42 Yeah, I would rather… I mean, I… long-term.
We don't want to be bridging our own stuff.
Out of Bridges, things that you need to pull together two different systems, like, you know, micrometer, Bridge.
**GZ Gregor Zeitlinger** 18:08 Right.
**Trask Stalnaker** 18:09 So… long-term, we want to get rid of the… we don't want to be bridging
Anything, basically. Yeah.
**GZ Gregor Zeitlinger** 18:25 Yeah, I agree.
**Trask Stalnaker** 18:26 And…
**GZ Gregor Zeitlinger** 18:26 And, and for, the bridge that we already have.
we have a time horizon. When, eventually we only support declarative configuration, then we would get rid of
the bridge. And we could,
View this new bridge the same way, that it is helping us until people have migrated Through declarative configuration.
**Trask Stalnaker** 18:59 Yeah, it, it bothers me less on the Java agent side, because it's hidden, And,
I guess we could… Look at this as being hidden also, since it's an implementation… dependency… .
**GZ Gregor Zeitlinger** 19:26 It's not hidden, actually. It is a regular API.
I actually don't know if we could make it hidden.
**Trask Stalnaker** 19:39 Yeah, I mean, it's not an API dependency, so somebody would need to explicitly pull this in.
But, yeah.
Given that
there's not that many usages. I mean, we really did try not to create system properties, use system properties in
Library instrumentation, We just, the auto-configure ones were a special case.
Right, because there's no programmatic API.
**GZ Gregor Zeitlinger** 20:24 Yeah, in some cases, I think it's not possible. With JDBC, you cannot configure it programmatically.
**Trask Stalnaker** 20:40 I think only if you're…
Using the, like, the data source…
basically using it as an SPI.
Let's see, I think we have it.
I guess we don't even document that way anymore.
You should be able to hear… always, param, programmatically.
set stuff.
**GZ Gregor Zeitlinger** 21:40 Hmm, okay.
**Trask Stalnaker** 21:43 Capture query parameters… Yeah, not sure why we were pulling system properties there.
What about,
Would it be weird to just have, kind of read… System properties directly… In these instrumentations…
**GZ Gregor Zeitlinger** 22:16 You mean like we did before?
**Trask Stalnaker** 22:20 Oh, I see, config properties util… right, right, right.
Yeah, I mean, we could… convert these…
What do… what do we want to do?
for… declare, declarative config. Let me see, so this is config, API config, so…
And this is using the global…
Oh, I see, because we were having to use…
**GZ Gregor Zeitlinger** 23:01 Yeah, it's using the same global instance, it's just checking if this is the extended
OTEL, and then it can get the config provider out of it.
**Trask Stalnaker** 23:15 Right. So in this case, Kafka telemetry, already has…
I mean, so, sorry, I'm going off on a different tangent here.
Kafka telemetry… Question is whether… the… oh, I guess the builder…
So we've got OpenTelemetry over here.
Do we want to, sort of, default? We could… default things.
directly in here.
**GZ Gregor Zeitlinger** 24:00 What do you mean by default?
**Trask Stalnaker** 24:03 So… see how here you're calling setCapturedHeaders?
Right.
Potentially we don't need this anymore. We can just, in the builder itself, initialize the default
Right, we're passing in an open telemetry here. Now we could initialize the defaults right over here.
**GZ Gregor Zeitlinger** 24:34 You mean check if this is the extended open telemetry?
**Trask Stalnaker** 24:38 Yeah, yeah.
**GZ Gregor Zeitlinger** 24:42 Okay, so basically, instead of using a bridge.
we would, use the declarative configuration API
it would mean that we duplicate the logic, if I understand this correctly. We would either
Have the system properties, because we…
Cannot remove it until a major version bump.
But we would maintain, at the same time, the declarative configuration API.
**Trask Stalnaker** 25:19 Yeah… Yeah, so… Okay, sorry, I'm getting distracted by, like, bajillion,
the GC, they're trying to get the election results out.
**GZ Gregor Zeitlinger** 25:36 Oh, okay, exciting day, right?
**Trask Stalnaker** 25:41 So, okay, so the… If we left this as is…
Don't touch this. This is kind of, like, back… backwards compatibility for now. We mark it as…
To be removed, maybe in a major version bump.
And… The declarative config support inside here.
And then we could add more properties than just the ones that we were supporting before, if there's…
Something, you know, if… if we…
want to define, like, a declarative config property for propagation enabled, or any of these now, we can do it, whereas before, we had been
Holding off on adding system properties for them.
**GZ Gregor Zeitlinger** 26:38 Right.
**Trask Stalnaker** 26:41 I think I like that.
So we… that way, we kind of pave the path towards… the… declarative config…
how we want declarative Config to work.
while… Leaving in place the backwards compatibility stuff for the time being.
**GZ Gregor Zeitlinger** 27:14 I'll… I'll have to give it a try to, see how…
**Trask Stalnaker** 27:18 Oh, yeah.
**GZ Gregor Zeitlinger** 27:18 how it feels. Yeah, okay, let me, let me try that out.
**Trask Stalnaker** 27:24 Cool.
Yes, thread details.
I was thinking about this.
A couple weeks ago, and then…
it wasn't super obvious to me how… because I do like the idea of…
Still, like, the idea of, adding it.
At span start…
Yeah, I mean, maybe…
Just in the… Instrumentation. Yeah, so I started with, like, oh, maybe we should have a thread attributes extractor?
Where you have… Where you add that to your instrument or builder explicitly.
Like all the other attributes extractors, kind of all the other SEMCOMS pattern.
What I didn't like about that is…
Thread attributes are something, basically, you…
Want on everything, or want on nothing?
**GZ Gregor Zeitlinger** 29:03 Generally.
**Trask Stalnaker** 29:05 So, I think I agree with Lori on…
We would need to add it in the instrumentation… in the instrument… in the instrumenter itself, basically, have an option to capture thread attributes.
And then it would automatically add them in the instrumenter itself.
**GZ Gregor Zeitlinger** 29:38 And this would check for declarative configuration.
None.
**Trask Stalnaker** 29:46 So… Instrumenter…
Do we have an open telemetry?
Instant… yes.
So, we do have an open telemetry instance here, so you could add another Boolean property here.
Capture thread attributes.
Default it here, but also have a setter for… I said, having a setter, kind of.
Sucks, because that implies you could do it different for different Ones.
How… will that work, for the Java agent?
Does the Java agent have an… Extended… telemetry… OpenTelemetry.
**GZ Gregor Zeitlinger** 30:54 I just have a PR open for that.
**Trask Stalnaker** 30:58 Okay… And so, will our extended open telemetry config properties…
Okay, and then we can…
Yeah, so something like that. I think there's some complicated details, to work out still, but…
That's what I would try.
**GZ Gregor Zeitlinger** 31:26 Hey, and is that answering Laurie's comment?
Where he said, either let rule-based sampler compute thread name itself, or the instrumentation API.
Instrumentation? Yeah, is that what you just proposed, the instrumentation builder?
Okay. Okay, got it.
Okay.
**Trask Stalnaker** 32:14 Yeah, I mean, give that a try here, if it's, extended open telemetry.
Then we can get from there, and let's,
I don't know if we can see how that… goes…
**GZ Gregor Zeitlinger** 32:30 Yep. It's a similar pattern to, the previous,
discussion point, using the declarative Configuration API, More sprinkled around.
Then we can see how this… Fields.
Okay.
**Trask Stalnaker** 32:51 Cool.
**GZ Gregor Zeitlinger** 32:53 Thanks,
pretty fast today. Last one is a spring starter. That's really a big PR that has been sitting there for, since June, actually, because I started that as the first item to make sure that
declarative configuration would work, but now.
**Trask Stalnaker** 33:14 Right.
**GZ Gregor Zeitlinger** 33:14 Lord.
Now it's, ready, and I'm looking for more reviews, or feedback on what I should change.
**Trask Stalnaker** 33:28 Okay, cool. I will, I'll leave it… on my… To do, and try to…
Start getting through it.
**GZ Gregor Zeitlinger** 33:43 Yeah, I… I already discussed with Jay,
that, he, will also help out with a spring start in the future, given that, Jean,
is not working on Java anymore.
So that we have a second person to look at things in the future.
**Trask Stalnaker** 34:06 Awesome.
**GZ Gregor Zeitlinger** 34:11 That's all I have for now.
**Trask Stalnaker** 34:15 Alright.
**GZ Gregor Zeitlinger** 34:16 Do you have anything?
**Trask Stalnaker** 34:21 No, no, still excited about the progress here.
**GZ Gregor Zeitlinger** 34:28 Correct.
Tell me who, got elected, then. Yeah.
**Trask Stalnaker** 34:34 Morgan just said the tally is underway, but… Okay.
So, I think if you go…
I'm trying to find the link.
To the… Let's see, tabulate election results…
**GZ Gregor Zeitlinger** 35:00 And, you're up for an election next time?
**Trask Stalnaker** 35:03 Next time, yes. Okay. Okay, the, elect… the results are in.
Wait.
Bizarre.
Okay, that's not the right link, that…
Morgan posted. I went to it, and I'm like, wait a minute, these are people who weren't running this year. He posted the 2023 link.
Okay, anyway, yeah, you'll find out soon. I will find out soon. Alright.
**GZ Gregor Zeitlinger** 35:46 Alright.
**Trask Stalnaker** 35:47 Bye.
**GZ Gregor Zeitlinger** 35:48 We're in a half an hour.
I'm… Yeah. Okay. Yeah.
**Trask Stalnaker** 35:54 Have a good one.
**GZ Gregor Zeitlinger** 35:55 You too!
