SIG: Specification SIG
Date: 2025-10-28
Duration: 55 minutes
Zoom Recording URL: https://zoom.us/rec/share/ADgT4LJyaDvkb8q_KytrI6XHMapR95IPpdQGuDVXdWnIu6U6YNYjT1Lx-wdmPl_y.nSsWwRK_MIP5CV1g
============================================================

## Zoom Recording Transcript

**MG Marylia Gutierrez** 00:26 Hello.
**jberg** 00:30 Bye.
**Ted Young** 01:00 Jack's back.
**jberg** 01:03 Back-ish, almost back.
**Ted Young** 01:05 Almost back.
I think I posted the right election link. I just splatted what was…
On the website. Let me know if that's not the right thing to be handing out.
**Alex Boten** 02:33 Oh my god, I can see who you voted for!
I'm kidding, it's fine.
**Ted Young** 02:41 Don't blame me, I voted for Kronos.
**jberg** 02:46 Alright, we'll give it another minute or two, and then we'll get started. In the meantime, if you have any topics, add them to the agenda.
**Liudmila Molkova** 03:07 Hey, Jack, it's official! Congratulations!
**jberg** 03:11 Yeah, thanks.
I'm coming back, and I'm joining a new company.
**Trask Stalnaker** 03:21 Congrats on both things.
**jberg** 03:24 Thank you, Trask.
**Trask Stalnaker** 03:26 I mean, not coming back to work, but the thing that preceded being out of work.
**jberg** 03:31 Oh, I picked a great time to, have a baby, because I got to enjoy, the fall, which is my favorite season, so… just an excellent time.
**Austin Parker** 03:40 I'm very Mr. Fall Man right now, I will say.
**Daniel Dyla (Dynatrace)** 03:45 Even the background is warm colors.
**Austin Parker** 03:47 Yeah. Do you have a pumpkin spice latte, by any chance?
**jberg** 03:53 That's not my style, but everything else is.
**Austin Parker** 03:55 Apple cider?
**jberg** 03:56 Yeah, there we go.
**Austin Parker** 03:58 Yeah, I can just sit… nice hot steaming mug of apple cider, the flannel on top of the Henley, nice warm background, like I said, you gotta get a little… you gotta get a…
Little fireplace, too.
**jberg** 04:12 It's peak fall in Chicago right now, so…
**Austin Parker** 04:15 Gee, I couldn'.
**Daniel Dyla (Dynatrace)** 04:16 Be convinced that you're in a log…
**Ted Young** 04:17 I've been fly fishing off of your.
**Austin Parker** 04:20 I do, I do get… I get log cabin vibes.
**jberg** 04:28 All right, it's for after, let's get started. First item on the agenda is from Pellard. He's not… he's not here today.
So… not sure how we should address this. He's just requesting a couple of…
things be merged before KubeCon NA. When is KubeCon NA?
**Austin Parker** 04:49 The… not next week, but the week after?
**Daniel Dyla (Dynatrace)** 04:56 November 10 to November something.
Yeah, 10th to 14th, I think.
**Austin Parker** 05:01 Yeah.
**Liudmila Molkova** 05:03 So, I think that… Okay, go ahead.
the first PR, extended set of attribute value types, it's got the approvals.
I don't believe there are active discussions, so there is one with Carlos, but I think it's… it doesn't look blocking. So, in theory, we could hit merge.
Perhaps we should give people maybe till the end of the week to make the final look, and then…
We can merge.
**Austin Parker** 05:35 Yeah, I see Carlos approved on behalf of TC Inspect.
Yeah, I'm willing to say give it until the…
Or if… I mean, does anyone…
Do you know if he's gonna be at the LogSig meeting later?
**Liudmila Molkova** 05:58 Yes.
**Austin Parker** 05:59 Okay.
**Liudmila Molkova** 06:00 10 AM, 2 hours from now.
**Austin Parker** 06:02 Yeah, does anyone wanna… if… I'm willing to… I feel like we should just say, hey, if you have any further comments, please add them in the next 2 hours.
**Ted Young** 06:12 Yeah.
**Austin Parker** 06:14 It's been open for a while.
**Ted Young** 06:16 This is an issue that has been beaten to death.
**Austin Parker** 06:19 That too.
**jberg** 06:21 So this is just the PR that confirms the OTEP that was beaten to death, correct?
**Austin Parker** 06:25 Yes.
**Ted Young** 06:26 Yeah.
And the blog post is the other thing, right? So he's like, can we please both confirm this and launch the blog post that's been sitting there forever about this, so we can tell everyone at KubeCon. I think that's totally reasonable. I don't think we have to do it today, but if we do it by the end of the week…
That's fine.
**jberg** 06:47 That sounds fine with me, although I'm not up to speed on this. So, does one of the TC members, that has approved this want to, you know, follow through with that?
Merging, if there's no further comments in a couple of hours.
**Liudmila Molkova** 07:02 I can match it.
**jberg** 07:06 Great.
Austin, were you gonna leave that comment?
**Austin Parker** 07:11 I'll…
**Liudmila Molkova** 07:12 Yep.
**Austin Parker** 07:12 I'll put a comment on it, yeah.
**jberg** 07:26 All right, I think that's probably all for that topic then, unless there's any additional comments.
So, let's move on. This is, AP. I think that's you all.
**Austin Parker** 07:36 Let me, Yeah, so this is just a FYI. I posted about this a few places, but
We… in relation to some…
End-user feedback we've gotten, and also various surveys and other things we would like to…
Start the process of, making some changes to how we think about stability and, releases and a few other things, so…
Just as a FYI, the goal of this blog specifically is to announce the intention to do this. We will have discussions both online and in person.
To turn this into various OTEPs, so what I would appreciate is if…
People haven't looked through it and reviewed it.
If you could look through it and review it before Friday, And then Friday…
We'll get it set up for release next week, because we would also like to have this
Oh, before KubeCon.
**jberg** 08:48 So we've got a blog that expresses the intent of the OTEP that will be codified.
**Austin Parker** 08:54 Yeah, let's, let's just…
I love, open source, don't you?
**jberg** 09:07 Is the idea in your head that, you know, with a blog, we can maybe solicit opinions from more end users than we typically get on OTEPs?
**Austin Parker** 09:16 Yeah, very specifically, this is, we are trying to drive more external, because a lot of the…
Express desire for these changes is coming from, sort of, end users.
And adopters, so we would like to…
Have a discussion that deliberately includes more of them?
**Ted Young** 09:37 Yeah. We've spent, up until now, basically answering the question, what does OpenTelemetry do?
Right, and that's been very much a vendor fest, it's been very much, just trying to get things to spec so that it works with
backends and everyone's requirements, and now we're kind of switching into a phase with… where we want to say, like, how would you like this to work for you? Like, how would you like to install this? And I feel like it's a lot of questions where end users can really just give us their direct opinions, because we're just trying to…
You know, improve the installation experience, improve the usability for them.
So really getting a lot of end-user feedback into this phase is helpful.
**Austin Parker** 10:22 We also definitely want maintainer opinions and feedback as well. Maintainer and contributor opinions and feedback as well, because, you know, ultimately maintainers are the people responsible for
Implementing these things.
So, yeah, I definitely understand that it…
Feels like a lot of,
talking about… feels like a lot of talking about how we're gonna talk about things, but let's… let's trust the process here for a little while, at least, and…
Rask.
**Trask Stalnaker** 11:02 Yeah, I brought this to the, Santa Convention SIG yesterday to discuss, because I, the…
parts about semantic conventions.
And the… There was some feedback about, like, the idea of… Beta SEMCOM…
Or, like, the instrument… I think there's a preference for instrumentation stability to be based on not necessarily SEMCON stability, but the telemetry stability being its own concept.
For instrumentation, like, don't… instrumentation shouldn't break their telemetry. It doesn't necessarily have to be tied to
Stable SEMCON.
And so my, my only ask here is… Can we, kind of.
loosen the specificity of this… the recommendation in this post around semantic invention, and maybe just focus on the prob… like, the problem, and that we're…
Want to solve the problem, as opposed to laying out a particular solution?
**Austin Parker** 12:22 Could you just make that comment?
In the relevant place on the posts and the PR, so that we can…
Wordsmith is there?
**Trask Stalnaker** 12:34 Okay.
**Austin Parker** 12:35 I'm totally fine being less specific in the post, because, again, the goal is to Have these discussions in…
the discussion and then have that translate into the OTEP. I don't want to oversteer things, but I also don't want us to, like.
Yeah, I understand, I don't want it to be totally…
**Trask Stalnaker** 12:56 Yeah, yeah.
**Austin Parker** 12:58 I don't want this to just… I would like to at least have this be, you know, somewhat, like, directionally, like, hey, this is where the thinking go… this is where the thinking lies right now, and it can change, but, like…
I don't want to just be like, hey, yeah, problems.
Let's talk about them more.
Anyway, I, again, like, I'm just asking if people have, if people haven't reviewed it, or they'd like to, like, I would like to time box this to the week,
So that we can… Keep the ball rolling.
**jberg** 13:38 So, I see there was a discussion on this last week. Sorry I wasn't attending the SPECSIG last week, so, maybe this was already discussed, but, I see an intersection in this sentence.
With some of the work and conversations that are happening in declarative configuration in that SIG over there. And it's specifically about,
So, instrumentation libraries, and whether they are an enabled or disabled by default, and, you know, the properties in which the, you know, an enabled or disabled property to, whatever we name that thing, to change the default configuration of that.
And so, so I guess one of the questions is, like,
If we have experimental instrumentations disabled by default, and later they become stable.
is it okay to switch the default behavior, and do we want to make project-wide guidance for that? To, you know, have some sort of promotion project process where, you know, an instrumentation goes from off by default to on by default, and, you know, I guess, are we all on the same page that that's a good thing?
**Austin Parker** 14:50 I think very specifically, the guidance here is that
when things are promoted to stable, whatever we determine stable is for this, then yes, like, they would turn on by default, but a part of what that promotion process looks like is specifically having guidance around
You know.
Not just the stability of outputs, but also things like documentation, example code, published benchmarks, and overhead of that information being enabled.
And being part of a, like, somewhat… slower…
you know, release process where people could choose to adopt OTEL in… smaller… But bigger chunks.
Again, nothing set in stone, nothing's done till it's done, but, you know…
This is where the thinking is.
Ed.
**Ted Young** 16:02 Yeah. When it comes to instrumentation, I just wanted to clarify, like, I think it's fine to have, quote, unstable semantic conventions turned on by default. We feel like the instrumentation package
itself is stable, in the sense that we don't believe it's going to cause dependency conflicts, or blow up on people, or otherwise. It's, like, untested to be used in production. We're just telling people, like, hey, the semantic convention's coming out of this, there might be a 2.0 that comes out at some point that changes that.
And we've got a backlog of techniques we can use to…
to maintain, you know, allow people to transition from 1.0 to 2.0. We may have to do more maintenance of, like, 1.0 versions of things alongside the 2.0 version of things, but…
It's just decoupling those concepts of whether the package itself is stable versus the data coming out of it.
Our users misunderstood what we were saying when we…
communicated using the same version number for both things. So that's why we want to change it.
**jberg** 17:12 Okay, and the relation to declarative config is, you know, there's a topic that Alex has added later in the agenda about this enabled or disabled, like, how to name Boolean properties when you're enabling and disabling things.
And, so the guidance that we follow in declarative config is the spec. So, you know, we have this principle that we're unopinionated about things. We don't decide which properties should be configurable, we delegate to the spec.
And similarly, we're delegating this naming decision of Boolean properties to the spec.
And so, you know, the specific text that we're referencing, I think everyone here is probably familiar with it, we've kind of beaten this conversation to death as well, but it's like, the name of the Boolean property, whether you use enabled or disabled, should be such that, the, like, a default value of false, or empty, or null should align with the default behavior of that, of whatever the thing you're configuring.
And if you can imagine, the intersection between this and
Instrumentation going from off by default to on by default is such that the name of the property changes.
Right?
So, like, when the instrumentation goes from experimental to stable, and it goes from off by default to on by default, we have to change from,
Naming the property enabled to naming the property disabled.
And, you know, that's kind of backwards, right? So, like, you know, we talked about this in the declarative config sig yesterday, and I think I'm just gonna say what Alex, I think, was gonna bring up, but it's…
you know, we delegate to the spec… to the spec for this naming recommendation, and you know, if… if we want to change this sort of backwards behavior that I'm articulating here, we need to carve out an exception here in this language, or say something to the effect of, like, hey, this naming recommendation only applies to environment variables, and, you know, this new configuration interface
is not subject to this. Something along those lines. Or else, you know, we're gonna get ourselves into a bind with instrumentation, specifically.
**Austin Parker** 19:23 I think we discussed this… Last week as well.
**Ted Young** 19:32 Yeah.
**Austin Parker** 19:33 I…
**Ted Young** 19:38 I feel like it's fine for us to change the spec.
**Austin Parker** 19:41 I feel like it's… I think we should have… I think the principle that we all tend to agree on is we should avoid double negation.
I believe Pablo's done a lot of work?
here to kind of, write down all the current values and variables, so I think we just need to look at it and figure out
What makes sense, and then add it to the spec, and then say, okay, this is it from here on out, and go from there.
**Tyler Yahn** 20:14 So, Austin, what about the opposing arguments?
**Austin Parker** 20:17 I think we can… Have that discussion in the spec issue, or the spec PR?
**Ted Young** 20:25 Yeah.
I think what Jack is bringing up here is, like, the debate I heard last week was about, like, should enabled or disabled, should we, like, pick one of these two things, or, you know, which one's better, or whatever, but this feels like something different, right? You're saying regardless of what we pick.
You have an issue in declarative config where things might start off disabled and then become enabled.
like, the default behavior may change if something goes from beta to stable, right? And that's, like, different from a question about, like, do we like disabled versus enabled as, like, a naming.
**jberg** 21:00 Yeah, so a change in default behavior from disabled by default to enabled by default, you know, puts us in a bind with this naming recommendation in terms of whether we name something enabled or disabled, because it essentially switches the name that we should call something. And then the secondary thing, and this is kind of related, is, like, even if we were to settle on enabled or disabled as the property name.
when the instrumentation goes from off by default to on by default, like, the default value changes, and, like, that's… that's kind of a no-no. You know, we should have…
and maybe this is okay, because it's an experimental portion of the config interface, but, like, for stable portions of the config interface, we can't change stable… or we can't change default values. That would be considered a breaking change. Like, for example, if we change, like, the span length… or the span attribute length limit from, like, 1,000 characters to 10,000 characters, that would be a breaking change. So we can't change default.
And, you know, all of this promotion from experimental instrumentation to stable kind of, you know, just is something we need to consider with this.
**Liudmila Molkova** 22:10 I would…
**Austin Parker** 22:11 I'd really like for us as a project to, like, be more comfortable versioning.
like…
I mean, I don't know. I feel like if we make a breaking change, all we have really said is, like, okay, we're gonna support the other one for 3… if we make a breaking change in a stable artifact, then what we have… our existing commitments say, we will support the old thing for 3 years.
Which is a long time.
But… It's also a fixed period of time.
And I… Tend to feel like users would prefer…
guarantees more than they would prefer us.
**Ted Young** 23:00 But…
**Austin Parker** 23:01 debating… This for 3 years.
**Liudmila Molkova** 23:04 I don't think… I don't think we need to break anything for this specific…
change. We are not going to rename environment variables.
And we don't have to change any guidance around environment variables, we only need to rename experimental.
config.
And I… I like the principle, like, the principle we had that
based on the default values. I think we should give up on the default values being static and global. So I can imagine up on telemetry,
Verbose profile, or open telemetry, compact profile.
If we ever have them. The defaults would be different for different things in these profiles.
And then saying that something is enabled or disabled makes no sense by default.
So, I hope we can keep the old principles that are tied to environment variables, we don't need to break anything, but for the new things.
We can change stuff.
Tyler, do you feel like this includes your voice here and your concerns?
**Tyler Yahn** 24:20 You're… you're saying… the… Leave the environment variables alone, and then define new… Guidelines for the configuration file?
**Liudmila Molkova** 24:30 Yep.
**Tyler Yahn** 24:33 Yeah, that's not really… I'm agnostic on this one. I, like…
I think Jack's point is a little bit more, related to this. I'm more about, like, if you have definitions for what the defaults are.
then I think that they need to be applied, like we're doing.
And what we've done, like Jack has said, is we've inherited this because the environment variable configuration is how most people use…
Configuration for the project, and so we've inherited a lot of these, ideas and policies into the configuration file.
And I think what Jack is saying is, like.
That's… that's how we've come up with this decision.
For how we've defined the configuration file. Like, if we want to go in a different direction, that would be a spec change, and, like, we're happy working on that, but it's a spec decision at that point.
**Liudmila Molkova** 25:23 Right, and from the config file perspective, defaults of enabled, disabled are very way more nuanced.
**Ted Young** 25:33 I think you've got something special there. I totally agree that defaults should not be changing when things go from experimental to stable, ideally, you know, unless it was just an oopsie and we're making a breaking change. But whether something's enabled or disabled.
Related to whether it's, like, a beta feature or not. That seems, like, a little bit different than how we treat the other defaults.
In that situation, it feels reasonable to pick what you think the default will be once it's stable. If it's something that once it's stable, the plan is to have it on by default.
Than to have the default reflect that.
In the naming, so it'd be enabled.
But, set to false, While it's…
**Tyler Yahn** 26:17 It would… it wouldn't.
**Ted Young** 26:20 Well, that's what I'm saying, is like, if you're… if what you're saying is where you plan on going with it, is that it's enabled by default.
Like, you should aim for that, and then have it… Do the opposite for the…
**Tyler Yahn** 26:34 Do you understand that, like, what I'm saying is, like, if you want it to be enabled by default.
And if it's not included in the configuration, the default is false.
So what you're saying is actually it would be disabled by default?
**Ted Young** 26:46 Right.
Right, if you're saying the only way to do defaults in the config is false by default, then we're kind of like…
Is that what you're saying, Tyler?
**Tyler Yahn** 26:59 Yeah, like, with Boolean values, yes.
**Ted Young** 27:05 Right.
So, maybe that's the actual specific thing we would have to look at, if…
Whether or not something can, if it's not set, be true by default.
**David Ashpole (dashpole)** 27:18 Yeah, Tyler, did you imply that that's specified in the spec?
Somewhere?
**Tyler Yahn** 27:25 Yeah, it currently is specified in the, right, right, what's being shown on the.
**David Ashpole (dashpole)** 27:29 Those are environment variables, though, not like…
**jberg** 27:31 David, so we've… we're inheriting this,
this in declarative config right now. We're saying that this… this same spec applies to us, and we're basically saying if we don't want to follow this for declarative config, we need to carve out, and maybe say explicitly somewhere that this… this language is only applicable to environment variables.
And in some ways, that's implied, because it's under this Environment Variables document, but, like.
In practice, we have taken a lot of the concepts, a lot of the language from this, you know, this file, which used to just be called configuration, and, you know, have taken it and inherited it in declarative config.
**David Ashpole (dashpole)** 28:14 Right?
**Ted Young** 28:15 And I'm saying I think that's totally reasonable. I think it's reasonable to make that change. I'm curious if anyone's opposed to… to that.
**Austin Parker** 28:25 I would like to just express… a position here that…
like, taking this to the extremely narrow scope of what started all this, which is, Jack, you saying, okay, we have instrumentation foo, and instrumentation foo is experimental.
And then… Some work happens, it's promoted into stable.
Previously, it wasn't.
**jberg** 28:58 Yep.
**Austin Parker** 28:59 That promotion… Like, would involve a version upgrade.
The desire of this… like… Stability discussion is to basically have a single way
That is very clear to end users.
How to opt-in to experimental behavior, with the understanding that
If you have not opted into experimental behavior, then you get all non-experimental behavior, right? So the default for non-experimental behavior would be true.
So…
if I was thinking about, like, an environment variable or something, or I was thinking, you know, then the environment variable would be, like, otel.enableExperimental equal true opts me into these new things. If something…
Like, there's no… I…
like, I'm not talking… you know, I don't think the defaults for that instrumentation itself really come into play here.
Except in the notion that, like, we're changing, you know.
If we had a stable instrumentation, and one of the config values for that.
one of the default values for that config option change, then yes, that would… that's breaking, that would require a major version bump, but simply promoting an unstable artifact to a stable artifact would bring it into the default config of everything going forward, which should be stable by default, right?
like, only stable things are automatically enabled. All unstable things have to be explicitly opted into, either via specific
like… otel.instrumentation.java.blah enabled.
That, you know, equals enabled, or whatever. Or a global flag of enable all experimental behavior.
I think these are… like, and if that means we need to, you know, edit the spec, then cool, let's edit the spec. It's…
**Ted Young** 31:12 I… I gotta run. It seemed like two things getting brought up, though. One is, like, a generic way to flip on or off all experimental behavior. I don't know that we need that. Maybe we do, but…
It seems a little bit separate from… The question of, like.
Hey, we have to rename these environment… we have to rename these config variables and, like, flip their polarity when things go stable.
Or do something weird, right? That's the part that seems super strange to me.
Saying, like, the name of this flag would have to go from disabled to enabled.
In order to… To follow our guidelines about what the default should be.
That seems a little wack.
Not being able to have true by default.
Anyways, I have to run. But that seems a little bit separate from your question, Parker, of, like, should there be a generic
Way to turn enabled or disabled off.
**Austin Parker** 32:09 I… I think my point is more that…
we can avoid a lot of these questions by having… or, I guess here's a better way to think about it. Rather than, like, a…
Split the difference, so you have a…
Minimum stability level config value.
**Ted Young** 32:35 Yeah.
**Austin Parker** 32:36 And then you don't have… and then that avoids the enable experimental features thing, right? Like, you just say, like, oh.
By default, this is set to Beta, and if you want to change it to Experimental, or RC, or stable, then…
Cool, it just checks against all of these other components.
And you don't have to… Wait, you might be both.
**jberg** 32:58 You might.
**Austin Parker** 32:59 I mean, you would still want a way to enable or disable individual instrumentations, but the, hi, Ted.
But the, like, generic… the top level…
Minimum stability level, config property would override it.
**jberg** 33:17 That's actually nice. That's a nice idea, I think, because…
You know, if we look at the two kind of scenarios that we could get ourselves in, so if we follow the current spec language, then, you know, as an instrumentation goes from experimental to stability, we have to change the property name from enabled to disabled.
And that… that sucks.
If we change the spec guidance so that properties are always called enabled, which is like, you know, Pablo's take on things, then, you know, as an instrumentation goes from experimental to stable, the default changes. So, you know, the default value goes from false to true.
And that's not great either, because that, like, you know, brings this advice that we have in declarative config that, you know, changing the default value is a breaking change.
**Austin Parker** 34:05 Right.
**jberg** 34:05 But, like, what you're saying, Austin, is like, hey, let's introduce a top-level value that defines the defaults for all instrumentations, right? And so, you know, you have something,
You know, you have something like this, like, you know, instrument… you have an instrumentation block, and, you know, you have something like this,
default stabilities threshold.
**Austin Parker** 34:29 Yeah. Something like that.
**jberg** 34:30 And it defaults to stable, but, like, the other values are, you know, beta, alpha, etc.
And, you know, that acts as, like, a stand-in for having to define, you know, the defaults for each individual instrumentation. The default value for every instrumentation is dictated by this higher level, threshold.
**Austin Parker** 34:54 Right, and it solves both of these problems, which is people…
Solves both problems, because the end-user-facing problem is
People are getting experimental behavior without realizing it.
And it also solves, sort of, the bigger question of, like, how do you promote things without changing defaults?
**jberg** 35:17 Right.
**Austin Parker** 35:18 Because the default for instrumentations could always be… like, the default for an instrumentation could always be enabled unless it's, like, something very specific… for very specific reasons, like, we would always want this to be disabled by default, unless you had a reason
You know, and it allows you to kind of shape all this stuff safely.
**Pablo Baeyens** 35:38 So, I joined the call in the middle, so I lost the first part of it, but I think it may be interesting to look at the examples on the collector. Like, some of them are not…
related to stability at all. They are more things like
do you want this particular feature to be applied or not? And it's…
Hard for me to see how this… Would be applied.
If we're talking about a dinner exclusion.
**Austin Parker** 36:11 I mean, are these, like, feature gates?
**Pablo Baeyens** 36:13 No, I mean, well, we have a different thing that is feature gates. This is… so… is, do you want to add exemplars to your trace metrics, for example? That's…
One of them. Is that related to stability? I wouldn't say so, it's just, like, in some use cases, it makes sense to have exemplars, in other use cases, maybe it doesn't.
**Liudmila Molkova** 36:35 That's the argument in favor of that defaults are subjective. It's, there is one default for one distro, and a different default for a different vendor. And it makes no sense to tie API or config properties to the default value of something.
**jberg** 36:58 So, these are great discussions. We've been… we've been talking about this for a while. I think I do have to timebox this, so that we can get to these other items in the agenda.
You know, I, I, I…
I guess I'll wrap this up by saying, I think that this type of concept solves one specific problem sort of elegantly, which is instrumentation getting promoted from experimental to stable. You know, I don't think… I think we can kind of tease these apart, then, and, you know, separately address the naming of these Boolean properties, whether they're enabled or disabled, or some combination of them.
But, you know, my specific question, which related to Austin's blog post, I personally like this idea.
But I think we need to socialize it and talk about it and refine it.
**Austin Parker** 37:44 Yeah, again, and… I will say, part of the goal of this process
It's to be able to have the discussions like we just did.
in GitHub, asynchronously.
with a broader set of stakeholders, right? So, I appreciate that we… I feel like we got to a good place on this one, but, you know.
I would like for us to…
Continue having these, in an async format.
**jberg** 38:18 Okay, moving on.
Aye vote.
**Ivo Anjo** 38:23 Hey, yes, I added that one. So, hello, I'm Evu, I work at Datadog, and we've been participating in the hotel profiling SIG, and so I have a bit of a meta question in terms of asking feedback on this document.
So, we basically have this challenge in, profiling, which is the fact that the current, hotel eBPF profiler works, by using the Linux kernel eBPF API, so it works from outside the process.
So you have… if you have, like, a bunch of, services that are instrumented with the hotel tracer SDKs, maybe, like, Java, Python, etc.
They have a bunch of things that are going on inside there, and then the profiler is kind of coming in from the outside and, like, reading what's going on, and then reporting profiles based on that.
The problem is, there's a few things, for instance, like, some process-level things that we would like to have, things like the…
the service name, the service instance ID, and things like that, that in some cases even get generated inside the tracer library. So it's kind of hard for an external observer to figure out, like, okay, what's the current service instance ID for this one process I am observing while profiling?
And, and so, we've been… we've at Datadog, we've been putting together this spec to kind of say, like, okay, let's create this mechanism whereby the, libraries can kind of publish
kind of say to the void, saying, like, if there's someone out there listening, here's my service name, here's my service instance ID, here's, like, some metadata that you might care about, and then the thing out in the void, the hotel profiler, could read these things and attach them to profiles when it sends them.
And so, kind of, I… I've been trying to, to go around and get feedback on, on this document, and on our proposed specification, because it's kind of a weird specification, because it's not kind of, it's…
the specification for the, writing side, which are tracers to kind of say, like, oh, hey, hello Void, this is the information you might be interested in. And then the other part is just the hotel profiler that will read them. So, like, what's the best way to kind of come up with, like.
propose the specification, get feedback from the… I've gotten a lot of feedback from the folks on the profiling side, because we've kind of started this work there, but I feel like we've been in the profiling echo chamber, so I'm trying to get out of the profiling echo chamber and get feedback from the folks on the other side, which kind of would provide this information.
Does this make sense?
**Josh Suereth** 41:09 Hey, so, I'll jump in quick. You're at the right spot. This is how you engage with the whole ecosystem. I think what we probably would like to see is what we call an OTEP, which is an Open Telemetry Extension proposal around this. Okay.
I read through this briefly, and you're not alone in needing this. When we do, like, pool-based Prometheus exports, for example, we need the ability to, get,
get resource information to Prometheus and expose that. And we had this… we had this discussion in the NC SIG about, multiple observers trying to get the same identity, right? And so, if the owner of the identity is the process itself, how does an external observer see it? You have to expose it in some fashion.
that's part one of your problem, and so I think, like, having, like, consistent ways we think about that makes sense. The way we do it for Prometheus won't necessarily work for the profiler, because you don't want to force everyone to open a port that you can read, right? That's kind of awkward.
The other side of this, I think, is around eBPF, and I think that's where we want the auto instrumentation SIGs here, of…
I think we want to have a cooperative nature between our APIs and our SDKs and eBPF-based instrumentation. And so, like, what you're trying to do here, I believe, and I haven't read through the details, is, like, there's a set of bytes that you write somewhere that you can read.
that gives the identity of a process, right? That cooperative nature between API and SDK, we haven't explored in an official capacity in OpenTelemetry, but it is something I am kind of gung-ho to see happen.
Because I do think there's a lot of potential with eBPF-based solutions and that kind of exposure.
That is why I think we need an OTEP, O-T-E-P. In the specification repository, you'll see a directory for OTEPs. There's a template. What you wrote here is effectively 90% of the OTEP, of what you want to do. When you put it into that, like, PR form, then we can all comment on it.
And it tracks all of that, kind of like a Google Doc, but, like, more…
officially, open telemetry. So I think that would be…
one of the next steps, but I think, you know, thank you for sharing the doc, because I think everybody should take a look at this and understand. Contextually, those are the two things that I think you're addressing that are important. It's, like, cooperative EVPF, you know, nature with APIs and SDKs. There's probably more to look at there, and there's probably, like, a convention you're setting here that I think is important.
And the second bit is this notion of, in entity SIG, we call it the multi-observer problem. You want two different things to have the same identity for the same concept.
**Ivo Anjo** 44:01 Yeah.
Exactly, that's it. And, in fact, even,
At Datadog, we have a few other use cases for things like this, and so exactly we would, exactly, we would have more… we were hoping to have more observers even beyond just the profiling part, although, like, as a… yeah, we're starting with the profiling part, but we have a bunch of teams, like, looking at me and asking, like, when can we have this kind of thing.
**Josh Suereth** 44:34 So, yeah, getting something driven across all SDKs, I will just tell you, is not an easy thing to do in OTEL. In terms, like, just practically, you know, it's every language SDK, unless you're willing to write all the code yourself, it's really hard to accelerate it, and it takes a while to get these things through the specification.
We're kind of doing so. So, I… yeah, in terms of, like, next steps, I think it's OTEP participation, talking to folks here. I don't want to monopolize time. I do have some feedback on the proposal, but I put it in comments, so you can read it offline.
**Ivo Anjo** 45:07 Thank you, and yeah, like, definitely, like, getting on the libraries might, the SDKs might take a while, but I think the most important part here is also, getting, like, agreement on the specs, so that we can start on some, because otherwise we're like, okay, I'm…
working a draft version for this one, but until we haven't agreed, the draft is kind of, like, still draft, but can change, so trying to kind of break the loop and get the chicken and the egg in the right order kind of thing.
Cool, so I think that's… that's it from me. Thank you.
**jberg** 45:47 Alright, thanks, Ivo. Next two topics… Seemed to be quick.
This is a reminder from somebody to vote in the GC election.
I think there's been lots of posts about that in a variety of places, so yes, please go and do that, it's really easy.
I think I saw recently that 20% of eligible voters have submitted a vote, so we can still do better. So, small group here, but if any of you haven't, please go vote.
Alex, who, based on chat, has left the meeting, and we talked about this previously.
You know, so I think we can skip this topic. We already pretty much covered it.
And then, on to, Anton.
**atoulme** 46:37 Hey, very quick, we have a schedule for the observatory that we started to push based on the results from the form for interest.
So we went ahead and put some names and SIGs in different places. We reached out to individual SIGs yesterday on Slack to ask them if there's any trouble with that scheduling.
if you'd like your SIG to be listed in here, or if you wanted to have a conversation.
please make sure you either respond to the form ASAP, or get in touch so we can add you. Now, there's a couple things that we left open, and if you can see here, the first slot in the day is kind of open, because we like to make… maybe if people want to meet at that time.
You should feel free to use the space for that, it can be a kind of a write-in. Same for lunch.
We want people to feel free to come in over lunch and kind of say, hey, today I would love to talk about, like, whatever, right? Just pick something and talk about.
If you want to book and put it explicitly on the calendar, no problem. Feel free to let us know, we can do that. But for now, that's open. There is another thing that's currently open, is on Tuesday night, there's a cube crawl, and we're not…
putting anything there yet, but I think it would be cool if the maintainers were hanging out at the observatory, so that there's a maximum of people who can meet them.
And that would be it.
**Austin Parker** 47:56 You should, usually we do a GC…
Like, meet and greet there too, so we should put that under.
Cube crawl.
**atoulme** 48:04 Okay, we'll do that.
**Austin Parker** 48:07 But yes, other maintainers, we would love to have you there.
**atoulme** 48:09 Yeah, like…
You know, this is going to be the moment where most people are going to be in the space, so…
If you want to be social and meet people, this is a great time.
Thank you.
**jberg** 48:23 Thanks a lot.
All right, it looks like there was a last-minute addition from Josh McD. Want to talk about these?
**Joshua MacDonald** 48:33 Thanks, I thought I'd mention this. One of the, somebody came to the sampling SIG last week, asking for some guidance. First of all, this is David's PR, and I think it's been sitting for 2 or 3 weeks. We should merge it. Nothing more to say on this.
unless anyone objects.
So this is changing the default exemplar selection algorithm to be, unbiased with time, so that you don't always get the latest one. The other issue came in from a user who had observed that the SDK spec does not include a way… would you link to the other PR? Thank you.
**jberg** 49:09 Yep.
**Joshua MacDonald** 49:10 does not include a way to always record, and that there are examples of this in four SDKs, so it's a pretty straightforward request, in my opinion. And although it's still in draft, I mentioned that I would speak up on it this meeting, so here we are. I support this, it's pretty straightforward.
And wanted to say that. Thank you.
**jberg** 49:33 Yeah, I've come across this myself. I've implemented my own sampler for this very situation. It's trivial to implement, but why not just have it as a built-in sampler if it's trivial?
**Joshua MacDonald** 49:42 Yep.
Thank you. That's what I've concluded as well. Alright, that's it.
**jberg** 49:55 Just a real quick question on this first one from, David. So, this is… I haven't studied this or looked at this, but so, the one thing that would come to mind about, reservations about merging this is…
you know, changing the implementation details and stability. And so, I think somewhere we have language in the specification that, you know, basically says that the implementation of these reservoirs isn't stable, something to that effect.
**David Ashpole (dashpole)** 50:24 If you look at the issue, so… Okay. …on the issue, and then scroll down to, like, the…
fourth or fifth comment, I think we found it and linked it here.
**Joshua MacDonald** 50:34 That's right, and Tigran basically asked exactly this question, I think, 2 weeks ago, and we found it and looked at it together.
**jberg** 50:41 Thanks for catching me up, appreciate it.
**Joshua MacDonald** 50:43 Yeah.
**David Ashpole (dashpole)** 50:44 Thanks.
**Joshua MacDonald** 50:45 Thank you all.
**jberg** 50:47 Alright, well, that's all the topics on the agenda, and we came in, you know, right about at time, so…
Let's all save a few minutes and have a good week.
Take care.
