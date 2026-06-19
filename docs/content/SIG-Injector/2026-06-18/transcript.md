SIG: SIG Injector
Date: 2026-06-18
Duration: 48 minutes
============================================================

## Zoom Recording Transcript

**Bastian Krol** 02:46 Hey there, nice to meet you.
**Paulo Janotti** 06:29 And.
**Bastian Krol** 06:34 Hey, hey!
**Paulo Janotti** 06:36 Hey, I, I've been the one, with the proposal for, an extension point, I didn't… I had some emergencies this week, I didn't… I couldn't finish. I can show, high level, right now, kind of, what that entails, and then I, I, I think we… then I have to wrap up a PR, even… it's kind of a draft, but kind of show what, I want to test how we ensure that we don't expose anything on the lib, and how somebody downstream can, leverage that.
One thing that I wanna leave clear that is that It's actually… there is, risk for downstream. If the downstream doesn't do the same thing with the symbols that's done, When, the injector from open the lens.
**Bastian Krol** 07:45 Yeah.
Let me interrupt you here, because right now it's only the two of us, I don't know where everybody else is. I think that's… That's very interesting, I think that's something that we should… Discuss with maybe a couple more people?
Around… I know that Antoine already said he's off this week and also next week, but I'm not sure where Michaela and Jack and… Nikola, they are usually in the meeting… So that's a bit weird that nobody is here, except for the two of us.
Yeah, I already asked in the…
**Paulo Janotti** 08:36 Yeah, no, that's…
**Bastian Krol** 08:37 No.
**Paulo Janotti** 08:37 That's fine. I understand that.
If, if you wanna, I can just kind of very briefly show to you, I, I understand that, this will be… kind of have to kind of go over, perhaps again with the full SIG. But I… any… any feedback and… and… idea, preview of that, I think, it's worth, so we can… So, let me see if I can…
**Bastian Krol** 09:12 Take a look. Hi, Michaela.
**Michele Mancioppi** 09:14 Bye.
**Bastian Krol** 09:15 This is Paolo, we… if you remember, maybe we discussed about that extension point for other… Prefixes for the environment variables?
**Michele Mancioppi** 09:28 Yes, that thing again. Okay.
**Bastian Krol** 09:30 with the weak symbols, so, I mean, this is right up your alley, right, with Linker stuff.
**Paulo Janotti** 09:38 Yeah, I… I'm not sure if it… and my idea was to share just the small screen, it seems that Zoom is sharing everything.
It's true.
**Michele Mancioppi** 09:49 It's a very nice desktop background.
**Paulo Janotti** 09:53 Can… can you… can you read here,
**Bastian Krol** 09:56 Oh, yeah.
**Paulo Janotti** 09:56 Love it.
Yeah, so…
**Michele Mancioppi** 09:58 We see your, what we see is the… the… a very beautiful, screen share, and then three reminders for add-on data collection sync, in-personal planets fitness.
**Paulo Janotti** 10:11 With.
**Michele Mancioppi** 10:12 A lot of T's and a lot of S's.
**Paulo Janotti** 10:14 I don't think it's working the way that I intended.
Yeah, because I'm using Zoom from the browser, I think that.
**Bastian Krol** 10:30 And on Linux, probably.
**Paulo Janotti** 10:35 Yeah, I can drop and try to use the Zoom application. Give me just one minute, and if you guys wanna take other direction, feel free. I'm gonna jump out of the browser and join via the application.
**Bastian Krol** 10:51 See you in a minute, then.
**Michele Mancioppi** 11:00 Hey, Jack.
**Bastian Krol** 11:07 So we just had Paulo here, he needs to reconnect, and then he wants to talk about… so he's the person that came up with that, environment variable prefix.
suggestion of doing that, not via recompiling, but we are an additional weak symbol, so we wanted to showcase this, I think.
**Paulo Janotti** 11:31 Yeah, just, kind of, it's, it's not ready, I still have to do more tests, I just have imbued what I want. I, I don't have the thing tested. So… the first thing is that I don't want to change the SO, I want to build, a separate thing that's not the package that we install. Are we linkable.
These are in linkable.
Does have a weak symbol?
that somebody downstream can relink on top of that and build their own SO, But, they are sold from… Libotel, it has a bunch of text symbols, and that function itself is still, just one text symbol here.
as it was any other function there. So, there is no weak symbol dynamic that leaks on the SO itself that's produced by, the OpenTelemeter official release.
What I'm asking is that the release also includes the… a new deliverable that is very linkable, that's intended for downstreams to use.
**Bastian Krol** 13:04 And… how would the main… S-O-C, anything from that additional…
**Paulo Janotti** 13:13 No, no, it's just when I'm linking, instead of generating the SO, I also generate this. This is a… So you have your distribution target that you build. I have a distribution target to build the relinkable. It's completely separate.
So…
**Michele Mancioppi** 13:32 Understanding why we need relinkable.
**Paulo Janotti** 13:35 They're linkable, because, This is a thing that, for instance, we do on the collector. The collector, you can rebuild the collector, and have your default configurations, you can have custom components.
So, in our case, we need to keep… preserve the defaults that we have for our solution that is basically the same thing that, the injector does. I think Antoine already, explained that.
That we have the same, We have a Lib doing the same, and we want to migrate to the open telemetry one.
So, we want one extension point to let us preserve our defaults for our environment variables.
**Michele Mancioppi** 14:29 Yes?
And I'm still not understanding they're linkable.
**Paulo Janotti** 14:34 The relinkable. We pick up the relinkable in our build, use that, I link the… the function that's gonna, allow the… the extra environment variable prefix.
And we produce ISO that is basically all the code from the OpenTelemetry, And just one difference.
And that difference allows us to migrate to basically use the same thing as.
**Michele Mancioppi** 15:10 Let me see if I understand.
What you want is that we publish an intermediate step in the building process.
That then you can get and link To actually fill the… this symbol that otherwise would be unspecified, and what this symbol does is to specify a prefix for environment variables.
**Paulo Janotti** 15:35 Yes.
**Michele Mancioppi** 15:39 But we would keep… all the variables the way we have, you just want the prefix. There is no remapping, right?
**Paulo Janotti** 15:51 No.
**Michele Mancioppi** 15:52 want to make sure that all the variables you tell your customers to set, they start with Splunk.
**Paulo Janotti** 15:58 Yes, we keep the hotel ones, and the Splunk ones. In our case, that's the only extension that we want to have.
**Bastian Krol** 16:08 The, the symbol that you would contribute, is that a function, because that auto-injector is enforout sounds like a function, am I right?
What is… what kind of…
**Michele Mancioppi** 16:22 Yeah, to be an object. An object symbol, and then you relink it.
I mean, by default, we would, we would, like, in the final build, we would make it in the empty string.
**Paulo Janotti** 16:37 So, you can make a, we can… We can make this symbol, anew, and, just, Have the code to deal with that case, but… Because… the alternative is us rebuilding the whole, injector, you know? And, I… I think the extension becomes a little bit cumbersome, because then we are… We are gonna sync to a tag, we are gonna rebuild that.
And then, basically, we have to run the full CI and have a full fork.
So…
**Bastian Krol** 17:25 I'm not quite seeing what that gives you. I mean, okay, now you don't need to rebuild it, but at least you need to do the linking step again on your end, and basically.
**Michele Mancioppi** 17:36 The outcome.
**Bastian Krol** 17:37 is still different, and I would say you probably need to run the CI for the outcome of that as well, so I'm not sure how… do we really… Win that much.
**Michele Mancioppi** 17:51 And it's also… it introduces constraints in which we can look up the code, because we need to make sure that there are no compiler optimizations that inline that symbol when generating the A part. It's also… Sounds a trivial. The name for the symbol, like, auto-injector isn't allowed, it doesn't make sense to me. In reality, if I understand what you want, it should be something… Auto-injector environment prefix.
Environment for our nation.
**Paulo Janotti** 18:20 Yeah, sure.
**Michele Mancioppi** 18:20 something like that. But it's parallel out, it doesn't compute in my head. But I kind of think… I think I understand what you're trying to reach with this.
I am not sure… I assume you tried this, right?
**Paulo Janotti** 18:35 Sorry?
**Michele Mancioppi** 18:36 I assume you have a working prototype for this?
**Paulo Janotti** 18:39 Yeah, yeah, this is the prototype. It's not… it's not like… for instance, you were very correct, the name is not the best name for this.
But it's just a prototype that I'm… I'm driving.
**Michele Mancioppi** 18:52 Tell me the way that you need to change the zig.build for this to work?
**Paulo Janotti** 18:57 We can see here…
**Michele Mancioppi** 19:11 Okay.
And, show me the code in, the way that you look up the environment variables.
**Bastian Krol** 19:21 Look up the prefix, you mean, right?
**Michele Mancioppi** 19:24 Now, in reality, when we do… when we look at the environment, you know, we no longer use just the hard-coded,
**Paulo Janotti** 19:31 You mean here in the config? This is the old code that existed here.
**Bastian Krol** 19:38 Starts with info prefix, okay.
**Michele Mancioppi** 19:43 Yeah, but this doesn't make the environment variable consumable.
This is not enough.
So, did you actually try?
To consume the environment variable from within the code.
**Paulo Janotti** 19:57 That's… that's what I was saying, I was just, starting on the… the next step is me to try to really rebuild with the linkable, you know, but I'm basing this… To be fair, I'm not, knowledgeable about SIG, but I know about the stuff in C, so, my idea was to relink within the same kind of settings that we have for,
**Michele Mancioppi** 20:25 In reality, that is… I don't think this is as simple as you make it, because when we go and consume an environment variable, we have a call site.
The call side is saying, look up that environment variable.
How the hell are we going to consume the new symbol that we want to introduce from there?
**Bastian Krol** 20:43 Michael, I'm not following. What do you mean by consume an environment where we are…
**Michele Mancioppi** 20:47 So inside the logic of the injector, we are.
**Bastian Krol** 20:51 Yeah.
**Michele Mancioppi** 20:52 Drop a bunch of environment variables by name in different parts of the code.
Right now, we are inlining the strings, For those environment variable names.
**Paulo Janotti** 21:03 No, a dead year's hot.
**Bastian Krol** 21:04 No, this is the mechanism where you can specify additional environment variables in that settings file, and they get injected. The other ones, like node options and stuff, these are… all stay hard-coded anyway.
**Michele Mancioppi** 21:20 Is this just toy?
**Bastian Krol** 21:21 the custom environment variables that you give key-value pair mappings for via the extra info config file, and there we restrict it to OTEL underscore as a prefix, and that's the context here.
**Michele Mancioppi** 21:37 Alright.
Good. I, I remember something different, didn't want to. All right.
Then, now I understand why you were saying MVAR allowed.
Still not a great name, but it makes more sense.
**Bastian Krol** 21:52 Okay.
So.
**Michele Mancioppi** 21:55 It's really weird.
**Bastian Krol** 21:57 Combine the…
**Michele Mancioppi** 21:58 Integration like this, but as a build step.
It's really weird.
**Bastian Krol** 22:04 Yeah, I mean, we cannot allow to configure the prefix, because that would defeat the whole purpose of restricting the prefix in the first place.
**Michele Mancioppi** 22:11 No, it's good.
**Bastian Krol** 22:11 I could just…
**Michele Mancioppi** 22:13 Yes, but why not making it as a build parameter? That's the part that I don't remember why it was not, it did not come across well.
**Bastian Krol** 22:22 But Paulo is saying we don't want to rebuild, and my question is based on.
**Michele Mancioppi** 22:26 But in reality, you are rebuilding just half of it. You're doing the That's my kid is.
**Bastian Krol** 22:30 Well, we more or less do it.
**Paulo Janotti** 22:33 But we are reviewed, but the scope is much smaller. But, I think it's a fair question, and I think since this is, kind of decision that we need to get very carefully whenever we go. I think I should kind of put both things kind of working, so we can compare then and say, hey.
**Michele Mancioppi** 23:01 I don't want to come across as mean or anything, but effectively, what you're asking is, like, an incredibly Like, I've never seen this done.
Has a way of… I've never seen it. In all the open source software I've done, this kind of mechanism of customizing a library by giving an intermediate build step so that you avoid rebuilding the .a before the linking, like, I do not remember, I haven't seen it done. It's very clever, but it's… It feels unnecessarily complicated.
And effectively, we would put out a .A object that nobody knows how to use.
For a scenario that we can probably get away with passing a build flag instead.
**Paulo Janotti** 23:44 Yeah, no, we can… if there is a build flag, we add the build.
**Michele Mancioppi** 23:48 And then you just compile it.
**Paulo Janotti** 23:50 Huh?
**Michele Mancioppi** 23:51 And it's a build flag that you just need to recompile, passing that build flag.
And it doesn't give… doesn't make us produce an artifact on GitHub that nobody would understand how to use.
Like, nobody would understand how to use it.
And instead opens the door to having build time customizations, which is something that is more generic.
it kind of makes sense. For example, I could imagine, at some point, being asked to disable some functionality entirely. Like, we don't want the injector to add environment variables.
Cool, we'll make a build flag, and that logic doesn't exist.
In the compiler.
**Bastian Krol** 24:33 That leaves very little functionality, but, yeah, that aside, yeah.
Oh, they dictator.
**Michele Mancioppi** 24:39 I mean, having feature flags like this, you don't want.
**Bastian Krol** 24:41 No.
**Michele Mancioppi** 24:42 Even them at runtime, making it in the build process parameterizable.
Testament.
**Paulo Janotti** 24:48 In that sense, I think you have a good point. It's very similar to the OCB, the OpenTelement Collector Builder, in a sense that you select components, remove components, and… Yeah.
**Michele Mancioppi** 25:06 Get me wrong, the idea is very geeky, and I appreciate But it's something.
**Paulo Janotti** 25:12 No, ugh!
**Michele Mancioppi** 25:13 would understand.
**Paulo Janotti** 25:14 I'm not, I'm not committed, to one or the other in that sense. I have a kind of preference because I don't like the idea of, cloning and building the REP, but maybe that's what makes more sense in this… in this case, you know?
**Michele Mancioppi** 25:33 Makes way more sense, yes.
**Paulo Janotti** 25:35 Yeah, and .
**Bastian Krol** 25:37 Oh my god, I'm feeling too.
**Paulo Janotti** 25:39 Perhaps I'm too old, but, I see this used by C stuff in the past, you know?
Oh, God.
**Michele Mancioppi** 25:46 Like, I promise you, like, I cannot name one project that does this.
I cannot name one of them. I, I think I have heard of something like this in internal pipelines for some packages in Ubuntu.
I don't think I've ever seen it done by… definitely not an OpenTermetry project, and much less, like, something that's published on a release, as a release artifact on GitHub.
I'm saying it's hard.
**Paulo Janotti** 26:16 Yeah. Yeah.
All right, I'll… I'll do… I… I was gonna continue this anyway. I'll do the experiment with, adding the switch and rebuilding, and then we look at the… the final format of this and make a choice.
**Michele Mancioppi** 26:35 I'm pretty sure that, exposing a build flag in, in Zig, in ZigBuild, and then make a macro.
It's gonna be trivial.
**Paulo Janotti** 26:45 Yeah, hopefully that… that is the path, that we…
**Michele Mancioppi** 26:50 And it is also… it is also a pattern that… is extensible to things more than just, hey, you need to read that memory location and compare. It's something that will work much more… in a much more general fashion.
**Paulo Janotti** 27:03 Yeah, yeah, that's really true, because then, as I said, I think the OCB is the kind of good analogy for something that OpenTelemeter already does, and then you can kind of have… have a map of features if the injector grows, and you can say, hey, this I don't want it, this I wanna, and…
**Michele Mancioppi** 27:25 Yep.
**Paulo Janotti** 27:26 Even… even things like, I just care about the Java instrumentation, or… Yeah.
**Michele Mancioppi** 27:35 Disable, like, do never inject Python, not even by mistake.
**Paulo Janotti** 27:39 Yeah.
**Michele Mancioppi** 27:40 We'll make a build flag. Do you support Python? No.
**Paulo Janotti** 27:43 Yeah.
**Michele Mancioppi** 27:43 We drop that code path is done.
**Paulo Janotti** 27:46 Yeah.
Sounds good, sounds good. Good conversation.
**Michele Mancioppi** 27:51 Fuck.
**Bastian Krol** 27:51 Excellent.
**Michele Mancioppi** 27:59 The.
**Bastian Krol** 28:00 I'll make a couple notes about this in our shared Google Doc, yeah.
Nikita, you were going to start another topic, or…
**Michele Mancioppi** 28:09 No, just a very short one. So, Ted is going to open an issue. Antoine had offered to do it, then he went on vacations. Ted is going to open an issue to, shorten the time slot of the SIG to 30 minutes. In general, I mean, we like to to kick around, and I tend to bring everybody on tangents, but 30 minutes, it tends to be a bust. Don't sneaker, it's unseemly.
It's… 30 minutes tends to be enough, and that gives us a much better slot location for the system packaging sync.
Which is something that you desperately need, because right now it's, like, 7, 8 p.m. European time, and it's… it's… Terrible.
**Bastian Krol** 28:50 Sounds good.
**Michele Mancioppi** 28:54 Jack, the, that PR for… changing the path for the rail use cases to go on the… the, DSIM. Is that something that landed?
**Jack Berg** 29:11 Yeah, when we cut a release.
**Michele Mancioppi** 29:14 Oh, nice. I completely missed it.
Sorry.
**Jack Berg** 29:21 Now, now I'm second guessing.
**Michele Mancioppi** 29:34 Yeah, landed 3 weeks ago, using GetM instead of Environment.
**Jack Berg** 29:40 Yep.
**Michele Mancioppi** 29:42 Whoa.
**Jack Berg** 29:44 Alright.
So are you all gonna run to the packaging thing in 2 minutes?
**Michele Mancioppi** 29:50 No, it's not there yet.
It's something… the issue needs to be opened. Tad volunteered to… to… to be on-to-one and open it, but it hasn't taken place yet.
**Jack Berg** 30:02 Okay.
**Michele Mancioppi** 30:06 Hi, since I have you here, Jack, I have, questions that pertain to the packaging signal.
**Jack Berg** 30:13 Yeah.
I'll see what I can do.
**Michele Mancioppi** 30:17 You know we were gonna talk about declarative topics.
**Jack Berg** 30:21 I don't mind that, yeah, yeah.
**Michele Mancioppi** 30:23 You know, when I start like that with you, it's declarative config. So, there is something that is very… so, I find myself between a rock and a hard place, with, on the one hand.
Opamp.
And, the desire to have only one file to apply to all, languages.
Which is something that is both good for OPAMP and good for the end users, where, for example, they would need to set up the utopi exporter and the resource attributes in only one place, not one per language.
Since, as far as I know, we threw away the idea of making overlays between files.
The files need to be self-contained.
**Jack Berg** 31:07 You can do overlays, but you're gonna have to use your own YAML tooling if you want to do that. There's not going to be anything built in.
**Michele Mancioppi** 31:13 Yeah, you cannot do overlays. If it's not a feature of the subsystem, it doesn't make sense to have system packages doing something like that behind the scenes, nobody's gonna understand.
**Jack Berg** 31:22 Yeah, yeah, I don't think system packages should do it either, yeah.
**Michele Mancioppi** 31:26 So, there are no overlays. The idea of having a single configuration file across multiple languages is a very interesting idea, irrespective of OPAMP, But, the support for, language-specific overrides is in that minus i to the power of 2 state.
Where only Java implements it, and nobody else seems to have it on the roadmap, as far as I can tell.
What's good news can you tell me?
**Jack Berg** 31:59 So when you say language-specific overlays, you're talking about, like, how Java has sort of invested in, in exposing all of the configuration knobs of the Java agent in declarative config?
**Michele Mancioppi** 32:13 No, it's a nice way for you to put it like that, but in reality, in the model, there is a, For instrumentation specifically, a way to, to declare, those configurations per language, as opposed, having to use always the main top entry that most languages, with exceptions, actually support. Let me actually find out which one it is.
Because I don't remember…
**Jack Berg** 32:43 Just while you're looking for that, so the idea there is, like, within the instrumentation block, there's… language sections, so Java.NET, Python, and then there's a general section, and everything in the general section is supposed to be language agnostic. And so, if semantic conventions comes up and says something like, hey, database instrumentation should have a configuration option to toggle whether the entire query is captured.
then that would manifest as, like, a configuration option within the general section, within, like, general DB.
And, you know, every database client instrumentation should conform to that and listen to that, and… You know, within those specific language sections, that's, like, supposed to be configuration knobs that are specific to a particular instrumentation library.
**Michele Mancioppi** 33:34 Certainly.
**Jack Berg** 33:35 Yeah.
**Michele Mancioppi** 33:36 So I'm looking at… it's this experimental instrumentation, right?
**Jack Berg** 33:40 Yep, that's the one.
**Michele Mancioppi** 33:42 Which levers can you pull for this to actually get implemented?
**Jack Berg** 33:48 I can't poll lovers. I cannot force the languages to go and do this. I try to tell them it's a great thing to do, but, you know, those maintainers have to make it a priority.
**Michele Mancioppi** 34:01 Because… I mean, the having experimental in front doesn't exactly scream… You must have it.
**Jack Berg** 34:11 Yeah, and we… and the reason it's experimental is because not a lot of languages have it.
So it's like a chicken and an egg problem. We need to have 3 implementations that have gone and implemented this instrumentation config bit, and then, you know, we can make it a candidate for stabilization.
**Michele Mancioppi** 34:33 Okay.
**Jack Berg** 34:35 Yeah, and so… So there's an… I can point you to an issue at the spec that's, like, tracking that. I think it's just PHP and Java that have support for that right now.
**Michele Mancioppi** 34:48 Oh, I didn't think of looking for PHP.
Which means that if we happen to line up a third, then we have a shot at this.
**Jack Berg** 34:58 Yeah.
**Michele Mancioppi** 34:59 On the one hand, I mean, I would love to be able to architect the system packages around this thing happening.
On the other hand, I suspect that until system packages happen, people are not going to see the point of this.
**Jack Berg** 35:12 I mean, I see the point of it from, like, a Kubernetes standpoint, like, you know, it's still useful to have Kubernetes, like, operators in Kubernetes to deploy, you know, instrumentation across all of your apps, and to have centralized config for that instrumentation, so…
**Michele Mancioppi** 35:29 Which is actually something that Jacob, is allegedly, working on.
**Jack Berg** 35:36 We're working on it, too, at Grafana, and Dash Zero is working on it, and other people are working on it, so, like… you know, I don't know if I'm actually referring to the same thing as you, but, like, what Grafana wants to see out of the OpenTelemetry operator is, rather than this annotation-based approach, we want to see a central instrumentation CRD, where it's arranged as an array of rules.
Each rule has a predicate matching workloads and a configuration to apply in the event that a workload matches that predicate.
And the configuration, the way that I see it, you know, you got two knobs that you can turn. You can do it via declarative config, or you can do it via environment variables. And I don't want to be, like… I'm not so pro-declarative config that I want to say, like, it's only declarative config. I want to meet, you know, languages and instrumentation.
**Michele Mancioppi** 36:33 I would say it's fairly to me, I would be… it's only the config, because more than one way of configuring things is one too many.
**Jack Berg** 36:41 Well, I… I want it to be one or the other, like, you just choose your adventure, and You know.
**Paulo Janotti** 36:48 I…
**Jack Berg** 36:49 I think declarative config will win on its merits in the long term, so…
**Michele Mancioppi** 36:54 I have said news for you, Jack.
**Jack Berg** 36:57 What's up?
**Michele Mancioppi** 36:58 This that you see on screen, I'm going to put in the chat, is what I understand to be the current proposal, or, advancing the CRD for instrumentations to Beta 1, And that, is based on labels instead of on notations this time.
**Jack Berg** 37:16 Well, they can't get out of labels until they incorporate the injector.
That, like…
**Michele Mancioppi** 37:23 That is where I think this may need another round. That is where I understand Jacob is working on, but I don't think there is a… I have not seen yet a coherent proposal around this.
**Jack Berg** 37:36 Well, so we're building it in Grafana.
And, like, I'm not a maintainer or an approver in the operator, and so, like, I… and, like, between not having, like, status in that group, and I actually can't attend that SIG either, because it conflicts with the Java SIG, so, so, you know, we're first gonna build it for Grafana, and then we're gonna propose it upstream.
Because we want to see all of this stuff take place, and, like, you know, I don't know if the operator will be responsive to it, if, like, the operator sign will be, but I think that's probably more aligned with what Dash Zero wants to see in an operator as well.
**Michele Mancioppi** 38:15 Then, you should really have a chat with Jacob, because he is also going in the same direction.
And, maybe you could use your input.
**Jack Berg** 38:23 I opened an issue in the operator, like, 6, 12 months ago, like, laying out this vision for, like, hey, let's have a centralized CRD, let's have it have an array of rules.
predicates and resolve config, this is how you do this thing, and, you know, this is all unlocked by having the injector. I think they… I think they've got their hands full. Like, I don't… I get the feeling they got a lot of stuff to do, and they don't have necessarily, like.
I don't know, I, like, I think… I see PRs sort of, like, languishing over there, so I'm not sure that they have… the people that are maintainers are, like, really full-time maintainers, you know? But this is just speculation. Maybe I'm wrong, and they just really like the annotation-based approach.
**Michele Mancioppi** 39:09 It might be worth checking, because I think that annotation and label-based approach are terrible ideas.
**Jack Berg** 39:14 Yeah, yeah, me too. Yeah, that makes the two of us. Actually, I think a lot of people think that, but, yeah.
I'll… Jacob, he should come to this meeting, right? So, I think we've talked about that idea at this meeting in the past, and Jacob was, like, nodding along, so…
**Michele Mancioppi** 39:32 Yeah, but they… yeah, I don't… I'm not saying… I don't think… I'm not saying Jacob is a proponent.
**Jack Berg** 39:37 Yeah.
**Michele Mancioppi** 39:38 labels. He also, I understand, wants and gone, is that I, I see a conflicting proposal, in, as a PR, and it confuses me.
**Jack Berg** 39:48 Okay. Yeah, like, I was articulating this internally somewhat recently. I was like, the operator has got 3 problems. It made, like, 3 fundamental mistakes. Like.
The one, annotations. So, it has this annotation requirement, and I'll forgive that one, because that was the only thing possible at the time, because they didn't have the injector. The injector's here now, so that unlocks a new approach.
SIN number 2. They allowed the, they have default versions for all the instrumentations that are installed, and so rather than requiring the user to specify the version of the instrumentation, they have a default.
And while that feels really nice, because your snippet for installing can be a little bit shorter, what that does, it makes you have to be responsible, as the operator maintainer, for making sure that there's no breaking changes to those instrumentation versions. When the user has to specify the version, they're taking ownership of, like, which, you know, versions that they want to install, and when they want to do minor and major upgrades.
**Michele Mancioppi** 40:48 I have to say that… The fact that we should not allow breaking changes.
That's stable by default. So the… having that thing, I think it aligns… having a default instrumentation aligns with where we want to be as a project eventually.
**Jack Berg** 41:04 No, no way, because all those instrumentations still need to do major version bumps. The Java agent is always going to do major version bumps, and, like, the operator, you should be able to do upgrades to the operator without having to be forced into upgrades to major versions of your instrumentations. Like, upgrading a minor version or even a major version of the operator shouldn't necessarily be bundled with upgrading instrumentations. Those things should be decoupled.
**Michele Mancioppi** 41:29 I am happy to agree to disagree on this one.
**Jack Berg** 41:31 Okay, all right. And then the last sin that they made in the operator was they tried to come up with their own pseudo-config schema for instrumentation. Rather than just relying on environment variables.
And, you know, declarative config didn't exist at the time, so they get a pass on that, but they should have just relied on the environment variables. So, yeah, they solved those three problems, and it'll be heavy.
**Paulo Janotti** 41:55 I… I have not been, deep on this configuration of the instrumentation, but I got the impression that something that you guys, before you went to the operator and Kubernetes part, I got the impression when I tried that, that everything is opt-in.
And without distinction between the languages that I think this was the point that started the conversation, it's very hard to use the declarative config for instrumentation.
Because it's like… If you have, two languages. It'll have .NET and Node.js.
it becomes the declarative, if everything is opt-in, you can't use, because the sets right now, they don't match. So I think this is the first thing that starts the conversation, if I'm understanding correct.
That have sections for each language, that will be really helpful.
**Jack Berg** 43:02 Well, there are sections for each language.
**Michele Mancioppi** 43:06 In this fact.
**Paulo Janotti** 43:07 Yeah, but…
**Michele Mancioppi** 43:08 It's only to SDKs that support it.
**Paulo Janotti** 43:15 Yeah, perhaps I should look again at that, because it was pretty hard to do a configuration file, That, worked for… three major languages, Node.js.NET, and Java. So, perhaps I'm not using correct words.
**Michele Mancioppi** 43:35 No, it's expected at this stage, because the kind of feature functionality that would allow you to make the difference is, is implementing only one of the SDKs that you just said.
Oh, I see. Because you are going to happily ignore whatever you put in there, and that is the same problem I'm having on the system packages side.
**Paulo Janotti** 43:56 I see.
**Jack Berg** 43:58 Yeah, it's like, you know, I would say if declarative config, the actual SDK part of the config schema, is extremely complete.
there's basically no features that are not expressible in the schema, and it's great, and it has, like, pretty good adoption. On the instrumentation side, it's just, like, it's still very immature. Like, what I would like to see, in addition to, like, more adoption from, you know, the languages, is more integration with semantic conventions, so that everything that is… should be configurable according to the semantic conventions is, you know, part of the schema, and that instrumentation's going to respect those after that point. But, like, you know, it's, it was, like, sort of, like, a couple of us drew some lines in the sand, and we're like, hey, you know, these properties and semantic conventions are discussed as being configurable. Let's, like, just put those in the declarative config schema. But we don't… we haven't done, like, We haven't, like, searched all of semantic conventions and made sure that all of the configurable properties are expressed in the schema, so it's not, like, complete, and there's nothing keeping it in sync. Like, I want automatic integration, so whenever a semantic invention says, like, hey.
here's a new convention, this thing should be configurable, it automatically becomes part of the declarative config schema. And Ludmel and I have talked about that, but, like, so far, it just hasn't been a priority.
**Paulo Janotti** 45:30 Yeah. So, yeah. I, I, I… I even wonder if… if the config was completed through your visual, we would not need anything that I was talking about before, not even the… the cloning.
**Michele Mancioppi** 45:44 I would give several limbs to have the declarative configuration implemented thoroughly in every single SDK that matters.
**Paulo Janotti** 45:53 Yeah, but…
**Jack Berg** 45:56 Yeah, yeah.
Me too.
I would also give a limb for, you know, to solve some of these, these packaging problems, where, you know, I want, I want all the languages to, to, like… approach instrumentation maturity with the same, like, sort of vigor that they have done for, like, SDK maturity.
Like, you know, it's, you know, the fact that Python in the operator is… there is no, like, sort of overarching version of the Python instrumentation. It's just, like, this composite image of a bunch of different versions that are… come from contribib and from Core. Like.
How are we, at this point, in 2026, and that's still the case? How is there not a group of people.
**Michele Mancioppi** 46:46 I, I won't.
**Jack Berg** 46:47 curating a major version of the Python instrumentation, and same with the other languages.
**Michele Mancioppi** 46:52 I, I've gotten, Diego, Hurtado, and, and, Carlos.
Interzero, and Matware also, and those two, even Carlos, they're going to be focused on Python, because that SDK needs help.
**Jack Berg** 47:05 Oh, Diego joined Dagio? Dagio? Oh, that's great.
**Michele Mancioppi** 47:09 Diego, Carlos, and Matt. We're going, it's actually, they started last week, and we'll post on LinkedIn, I think, tomorrow or something.
**Jack Berg** 47:17 Yeah, congratulations. Great.
Well, we've been just sort of, like, ranting about topics not strictly related to the injector. Any more injector topics, or…
**Michele Mancioppi** 47:28 it's… everything is related within Jatter. Jatter is in the middle of all this enablement, where actually it matters to have all this stuff working.
**Paulo Janotti** 47:36 Yeah, I was gonna say that for me, what's useful, this… semi-diversion, because it's writing related. As I was saying, the stuff that I was talking about, if we had the configuration as you imagine, Jack, I'll just put the file.
**Jack Berg** 47:54 Right, you don't need your Splunk-specific config option.
Right? Huh? Yeah.
It's a stopgap, so…
**Paulo Janotti** 48:05 Yeah.
**Jack Berg** 48:10 Alright.
**Bastian Krol** 48:11 Alright.
Let's wrap this up. I guess it did turn, yeah.
Do you rounds, and…
**Paulo Janotti** 48:19 Alright, nice to meet you.
Bye.
**Jack Berg** 48:21 Thank you, Apollo.
**Michele Mancioppi** 48:22 It's on…
**Bastian Krol** 48:23 But I…
