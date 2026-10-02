SIG: Python SIG
Date: 2026-10-01
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Aaron Abbott (Google LLC)** 03:31 Hey everyone, how's it going?
**Tammy Baylis** 03:37 Hey, Aaron. Hey, everyone.
I think I'll just get started on the triage while we wait for others. Yeah, welcome back.
Oops.
Welcome back to the OTEL Python SIG meeting.
We'll do triage till about 9:10. Meeting notes in the chat if you want to add your name and any Any topics?
So let's, let's look at the core dashboard first.
you Got a lot of… well, not too bad. We'll look at the most recent Waiting on Reviewers PRs as usual… And, within the last day, hot off the press, we got… 5, 7, 1, 7… Fixes issue 5716, Delta Exponential Histogram.
Never goes back to the maximum scale after a wide range interval.
Scale 2, positive offset, bucket, relative error. Oh my goodness.
Sorry, it's early for me. Metrics, yay!
Okay, so it's a well-described issue. Thank you for that.
And, say that's ready for review.
Next, from Lucas… Hotel export HTTP transport update URL of 3 transport to move proxy.
Yeah. Yeah, I know… Some of the other exporters support these, so it'd be good to have… At parity for sure.
Oh, and someone's marked it ready. Thank you.
It's a great idea.
Fix the Zipkin exporter.
No issue, but decent description, I think.
Value… oh… This might, this might tie into the, Export Millie's issue? No, I don't think it's related.
Sounds similar.
**Lukas Hering** 06:39 This is just, like, I think how we parse, like, it'll… we'll throw a value error if it's invalid.
And I think the desired behavior is to just… Fall back to default and log, so…
**Tammy Baylis** 06:51 Mmkay.
Yeah, more gracefully.
Thank you. Ready for review, sounds good to me.
Another from Lukas.
The Grpc. Proto reconstruct client on 1st and line exceeded error.
Whew.
**Lukas Hering** 07:18 Yeah, this was just from a bug report.
I'm not sure, it sounds like it's actually a real issue.
And… I think it makes sense.
That's good.
**Tammy Baylis** 07:36 Yeah.
**Lukas Hering** 07:38 We want to avoid… Stuck.
connections. I would think that the gRPC client might handle this for us, but I guess it's not the case.
**Tammy Baylis** 07:50 Yeah.
Wonder what the the spec has to say about About this… There is one.
**Lukas Hering** 08:02 I think it's probably more like implementation details, so I don't expect there to be anything on it, but.
I've actually… I actually adjusted the behavior so that… If we get any of those, like, connection errors three or more times in a row, then we'll just reconstruct the client.
It was just on 1st, but… I guess the motivation is to prevent churn in the connections.
**Tammy Baylis** 08:32 Okay.
**Aaron Abbott (Google LLC)** 08:35 Lukas, is there, like, a bug in gRPC that you found? Were you able to search through?
**Lukas Hering** 08:41 Well, we originally, you see the line, the original line.
**Tammy Baylis** 08:47 available.
**Lukas Hering** 08:48 That's from an older issue, which is.
Which… I don't know, I think there's an issue open in gRPC, but I don't think it's addressed.
And this new one is different with the deadline exceeded errors.
I'm not exactly sure.
I mean, I think it's… It's a harmless change anyways.
to add it.
**Aaron Abbott (Google LLC)** 09:18 Yeah, I thought the thing I'm confused about is I thought that it would manage, gRPC would manage like a connection pool.
So, like…
**Lukas Hering** 09:30 Yeah, that's what… that's what I was… I was under the impression, too. But, like, for example, that unavailable error.
it, like, the original… so, like, the original check there, like, served a purpose, because, like, I think people were reporting, exporting, like, hanging, like.
If exporting starts before collector starts, or something like that.
**Aaron Abbott (Google LLC)** 09:54 Mmm.
**Lukas Hering** 09:55 And yeah, gRPC wasn't… it wasn't able to automatically, purge that connection.
**Aaron Abbott (Google LLC)** 10:06 Okay.
**Lukas Hering** 10:07 That's why I also added the multiple.
You know, if the if gRPC is able to handle it, then it should this this logic should never be hit again.
**Aaron Abbott (Google LLC)** 10:17 Kim.
Okay, I mean, yeah, I can try to take a look, but… I know there's like also this weirdness where to pass options through to the C++ layer, you sometimes have to, Do it in, like, a separate place, so I… I'm assuming you checked all that, though, so, yeah.
**Lukas Hering** 10:37 Yeah, I can check again. Yeah, I was trying to see if we could just configure the client differently, and I didn't see anything immediately, but…
**Aaron Abbott (Google LLC)** 10:47 Cool. I can try to take a look at this one.
**Tammy Baylis** 10:52 Thanks, Aaron. Thanks, Lukas.
It's 9 11, so… Let's go to some regular topics.
Radhika, nice to see you.
**Radhika Gupta** 11:08 So… So my topic is regarding like the update on log stabilization. I know we were using this tracker to figure out some of the open issues that Ludmila had flagged at the end of this Like, at the very end.
And all… like, all of the issues she flagged are already merged, so I'm wondering, like, where we are at with this, and if we can move forward.
With the FS.
**Liudmila Molkova** 11:44 I think I can… it's great to hear, first. Second, I can go ahead and close the… Community issue?
So, we can mark it as officially approved.
**Lukas Hering** 11:56 I think there's actually still one more PR in Contrib.
At least for, Let me check again.
But, yeah, we discussed this last SIG about stabilizing the logs package.
Before the next release.
**Tammy Baylis** 12:21 Yeah, I am not gonna… Find it the correct way.
**Lukas Hering** 12:25 The yeah. There's there is actually one more. I don't know if it's missing from the tracker.
**Tammy Baylis** 12:31 It.
**Lukas Hering** 12:32 This one.
**Liudmila Molkova** 12:36 If it's in the country, then it's not technically a blocker for… Right. API and SDK.
**Tammy Baylis** 12:52 I'll just… link it so we don't lose it again, but I guess paraphrase, so… Yeah, I… I do not have the power to close this, but, I'll… I'll leave this with… I think, yeah, Ludmilla, if you could.
Could you close this one? Please.
**Liudmila Molkova** 13:36 Let me see.
I have the power.
I do have the power, so yes, I will leave a comment and close it. Yay, that's awesome!
**Tammy Baylis** 13:46 Also…
**Radhika Gupta** 13:47 Sounds good. Thank you very much.
**Liudmila Molkova** 13:50 Thank you.
**Tammy Baylis** 13:54 Yeah, thank you. That's been a long time for that epic.
Back to Lukas.
More big things, Semconf.
**Lukas Hering** 14:08 Yeah, I… I posted it, I think, about this in… a little bit about this in the Approvers channel, but.
I think so, as a part of.
While we're looking to stabilize some of the HTTP and database instrument or libraries.
I think we also might want to stabilize some of these other packages, particularly semantic conventions is a good starting point.
So Yeah, I mean, pretty much all that's involved here is bumping the version.
Oh, wait, oops, I messed it up, I need to remove that .dev there, but Oh, wait, never mind, actually, that stays.
I did update the README, though, to explicitly call out that Anything in the public namespace is considered stable, and it will follow semantic versioning.
Whereas, from my understanding, anything under incubating could… tech… I don't know if this is the case currently, but from my understanding, it could technically break at any point in time.
So, Yeah, just included, like, a warning there, and just, like, mentioned library authors that If they depend on that, they need to, they really need to pin it in their dependencies.
Yeah, so… Another, actually, idea that I had, and it's maybe a little too late.
I mean, we could explore this if we wanted to, but it might be worth maybe splitting this out into two packages, a dedicated semantic conventions package and a semantic conventions incubating package.
And the incubating one would always stay in the beta release line.
Just so that the versioning and stuff is kind of more explicit there.
But I think, for now, we can just stick with this.
Yeah, Erin.
**Aaron Abbott (Google LLC)** 16:20 I think Lyudmila, you were going to say something, so please go ahead of me.
**Liudmila Molkova** 16:24 Anna, go first.
**Aaron Abbott (Google LLC)** 16:28 Yeah, I was gonna mention that I think it's sort of along the same lines, but in JS, I don't know about some other languages, and maybe in, like, the Gen AI stuff we're doing, we've just started recommending people copy the specific conventions, like, directly… basically vendor the conventions they need, and they've even added some tooling in JS that, Does this in the contrib library.
Because I think that the issue will probably be, like, a lot of packages will end up depending on incubating, even if it's a separate package, and then we'll just be back in the same scenario where they pin a specific version or version range.
**Lukas Hering** 17:06 Yeah, so I've… I actually mentioned that, in here, in the README as well. Although I don't have any info on the tooling, just that if you don't want a pin, then you should vendor any of the incubating attributes that you're using.
Somewhere under here.
Yeah, I'm lining you for it.
**Aaron Abbott (Google LLC)** 17:29 Yeah.
Cool. Ludmila?
**Liudmila Molkova** 17:36 Yeah. Two things. First, it's awesome. Second, a small one. Like, I think we don't have a lot of success with metrics.
Maybe we can exclude metrics.
For now. But, well, we can talk about it more.
The second bigger thing, if we need it for HTTP.
We have the Http util.
Can we bake it and just generate this into?
HTTP UTL, so that… Nobody would even care about this dependency, any version conflicts would not… like, apply…
**Lukas Hering** 18:21 Are you saying we just fender everything, including stable attributes?
**Liudmila Molkova** 18:29 In the UTL, we would… in HTTP UTL, we would only generate things related to HTTP.
And we would not even expose them publicly. We can, but we shouldn't, probably. This package, it doesn't matter.
**Lukas Hering** 18:46 Yeah, I was just thinking along… the lines are, I guess, what's, like, proper, The idea, once we make this stable, we can just have a, like, tilde equals dependency on this.
For the, HTTP, Any HTTP instrumentation will depend on this for the stable attributes, and would vendor everything unstable.
That was my original intention.
Are you saying maybe we can just… you know, not have a dependency on Suncom at all.
I guess if that's the case, then I don't really know… like, at that point, what's the purpose of this package, I guess, is maybe my question? If, like, everything is going to vendor it in anyways?
**Liudmila Molkova** 19:30 For the applications, to… Take dependency on that for… for us.
**Lukas Hering** 19:41 Okay, yeah, I mean, I don't really actually have a preference either way, but,
**Liudmila Molkova** 19:47 Okay.
**Lukas Hering** 19:48 Others have a preference on that approach, but I think either way, like, there's no harm in doing this in my eyes.
**Liudmila Molkova** 19:56 I see what you mean. So it's not harmful to stabilize it regardless of the dependency story for HTTP. Yeah, I see. And maybe we should talk a little bit about metrics.
So the way… They are generated now. It's not super helpful because it does not include histogram boundaries.
And… They will be added at some point, and if somebody wants to add them to the, like, semantic convention schema, let me know, I'll support you.
But, like, they are basically unusable.
In the current shape.
So maybe we don't stabilize it. Maybe we rename it to underscore metrics for now.
**Aaron Abbott (Google LLC)** 20:47 Ludmila, you're talking about the instrument creation helpers?
**Liudmila Molkova** 20:51 Yeah.
**Aaron Abbott (Google LLC)** 20:52 Yeah.
And just to be clear, the issue is, like, the semantic convention YAML schema doesn't support the, The advice.
**Liudmila Molkova** 21:11 ground boundaries. Yeah.
**Aaron Abbott (Google LLC)** 21:12 Okay, yeah.
So.
**Lukas Hering** 21:20 Are we worried then if we release this, like, so are we expecting breaking change or are we just gonna add stuff? Because if we're just adding It shouldn't be an issue in my… From what I can tell.
**Liudmila Molkova** 21:33 It's not a breaking change. It's just that nobody should use this.
Because it's unusable.
**Lukas Hering** 21:41 Okay. Yeah. I mean, we can I don't know if people are you I I would be a little hesitant on making it private now because.
**Liudmila Molkova** 21:48 Oh.
**Lukas Hering** 21:49 It's gonna blow up stuff.
Okay.
**Liudmila Molkova** 21:52 6…
**Lukas Hering** 21:52 Even if they're not technically supposed to use it.
**Liudmila Molkova** 21:56 I see.
**Lukas Hering** 21:58 So, I mean, maybe we could just keep it and, deprecated. I I don't know.
**Liudmila Molkova** 22:08 Well, I mean… It seems there is more harm in hiding it now than in letting it be.
So… let's just let it be, then.
**Lukas Hering** 22:28 Okay.
**Aaron Abbott (Google LLC)** 22:34 Since we have you here, Ludmila, I had another question. It's like.
I think it's a coincidence, but the version looks vaguely similar to, like, the Semantic Invention release versions that we have.
**Liudmila Molkova** 22:46 software.
**Aaron Abbott (Google LLC)** 22:47 6.
Are other languages trying to… Use, like, the language-specific package versioning to mirror the semantic convention version, or does everybody kind of have this weird problem?
**Liudmila Molkova** 23:01 I think JavaScript tried.
And there were some downsides to it. I don't specifically remember which.
But you either.
staying consistent within the Python versioning scheme, whereas semantic conventions.
And I think it's… Oh, for the… for the JavaScript… Remember, it came up in Gen AI that, let's say this package contains more than just Yeah. the central semantic conventions, which we don't have a clear decision yet, then there will be multiple versions associated with it.
So I… my personal opinion, it's not worth trying to stay consistent with semantic conventions, better to be consistent with other fighting things, but I, like, Whatever you do, it's okay.
**Aaron Abbott (Google LLC)** 23:53 Yeah, yeah, no, I was getting at that, because I think I agree, like, And the point I was going to make was regarding the metrics and all that, like, we could do a two-dot 2.x release as well, if we want to change stuff. I think Just, like, relying on the semantic versioning would be better than what we currently have, where everybody just pins everything.
**Liudmila Molkova** 24:14 Right, yes.
Great point.
**Aaron Abbott (Google LLC)** 24:22 Awesome. Thanks for working on this, Lukas. I think this one's a long time coming. The only other thing I wanted to mention was there were like a couple accidental breaking changes.
I remember it happened for Java where the generated code accidentally introduced a breaking change. I think we have — our detection script would run on this still.
And it would probably notice, at least, like, a mechanical… Thing, like, if a symbol was deleted or whatever, but… Yeah, I guess that's not intentional, so I don't think that should block us.
**Lukas Hering** 25:03 Yeah, I can double check to make sure that the public symbols check will run on this as well.
Yeah, also, yeah, small thing on the whole versioning thing, I also added… I think it's a good idea, we… I added in the README the latest semantic conventions version that it's supported, so… Hopefully that should.
**Aaron Abbott (Google LLC)** 25:25 Yeah.
**Lukas Hering** 25:26 Make it more clear.
**Aaron Abbott (Google LLC)** 25:28 Definitely.
**Liudmila Molkova** 25:30 Do we have it automated? Like, it will definitely get…
**Lukas Hering** 25:34 Yeah, I didn't automate this. I was thinking about doing it. I could probably, set that up, too, if we want it. I just have in the development that, yeah, when you're regenerating, just, like, bump that.
**Liudmila Molkova** 25:47 Yeah.
And it's not, like, it's not, shouldn't be a blocker, it can, it should be possible to automate after.
This is exciting.
**Aaron Abbott (Google LLC)** 26:02 Yeah, very, very cool. Maybe one more question, just since we're talking about this, like… I wonder, is the long-term idea that like, say, native instrumentations and instrumentations in this repo, they would just use Weaver.
directly to generate what they need, and then we wouldn't need this package, so kind of like the vendoring approach we discussed, but there would be, like, a super easy way for people to generate everything they need. Is that the long-term vision across OTEL?
**Liudmila Molkova** 26:33 Good question. So, yeah… I think this package mostly exists for the applications to avoid the need to generate stuff.
And it's just a convenience, pure sugar.
**Aaron Abbott (Google LLC)** 26:51 Yeah.
Okay, I've seen some other — it's kind of similar to the issues we have with Protobuf. And I've seen the way Buff solves it is pretty cool, but it's probably out of scope.
But yeah, maybe I'll… Drop a comment on the issue or something like that, just for history.
**Lukas Hering** 27:27 Okay, yeah, next one for me, hopefully I'm not stealing all the time.
**Tammy Baylis** 27:32 How dare you? Kidding.
**Lukas Hering** 27:35 Yeah, so this is kind of related to the previous one, but, so, like, we recently finished, adding the… Or not recent.
Several months ago.
I think at this point, we've added the opt-in environment variables for emitting these stable HTTP semantic conventions.
So, I think the next step here is we want to start transitioning the packages to stable, where they will just only emit the stable attributes by default, so bring them into the 1.x line.
And I guess just kind of, like, doing a survey of all the packages, I think that before 1 edX is maybe the best time to do this, which is kind of consolidating a lot of the logic that we have for… I mean, this isn't unique to just HTTP, but really for all the semantic conventions, but starting with HTTP clients.
Doing, you know, having a general purpose you know, instrument or library framework that can be used to apply to an arbitrary HTTP client. So this is kind of, you know, I mean, it's pretty simple. I think the Gen AI instrumentation library does something like this, and Java does as well. So, basically, we just have, like, yeah, this generic HTTP client telemetry.
You can… there's different ways to use it. One's, like, using the context manager, or just calling start and end for, libraries that maybe you can't use the context manager with.
And then it just has, you know, all the information that you could possibly, have. Basically anything… everything that's needed to construct the Corresponding, like, spans and metrics.
So yeah, I mostly just wanted to bring this up to see if, like, people have feedback on this and, like, what they think. One call-out is, I think with 1.x.
I know that the emit stable by default isn't… That hasn't… that OTEP hasn't been, merged yet, but I think for… because this is a stable package, I think we should only emit the stable semantic conventions, by default.
is kind of the view that I'm thinking. It's similar to, I believe, like, what Java does, for example.
So, the way I've kind of broken it down is I've kind of actually done similar to what we've done for our SEMCOM package, which is, like.
this library will have, parts of this, like, anything that's stable will be public API, and everything that's not will be in, like, incubating. So there's, like, the incubating configuration, and then the regular configuration.
So if you wanna… and then there's also the environment variables for turning on the incubating stuff.
So… and then the general assumption is, like, all the incubating attributes, those won't follow semantic versioning, so, like, that stuff can break at any point.
Whereas the stable stuff, like, it's stable, so… yeah, just yeah. So yeah, this is kind of what I was talking about here. So Yeah, I guess… Yeah, if anyone has, like, feedback or… ideas, or maybe, like, alternate approaches, yeah, I just kind of wanted to get this in people's… Faces to see if there's any thoughts, so… Yeah, Luke Miller?
**Liudmila Molkova** 31:22 Yeah, a couple of thoughts. The first one, again, this is awesome.
I wanted to check, have you seen we have a conformance test for HTTP instrumentations in Python?
And they have some issues, so, like… we would, like, as a part of HTTP stabilization.
We would probably need to look into resolving those, and probably by updating to the shared helpers, like, 90% of them will go away.
**Lukas Hering** 31:56 Yeah, yeah, for sure. So.
Yeah, I would have to see… yeah, so this is just, like, I mean, this is, like, in a presentable state, but once we add it, we can add, like, like, the intention is that this will be extremely hardened, so… Yeah, I would… I would want to break… I would want to fix, like, all those conformance issues, before we start applying and, like, moving packages to 1.0.
And… yeah, I've pretty thoroughly gone through the spec and, like, make sure that everything that is done here should be, like.
I'm not gonna say… it's probably, like, 95% of the way there, for sure. It should be, like, pretty… it's pretty.
the… it's… yeah, it's… it follows the spec very, very closely. So, yeah, hopefully this should resolve a lot of those issues. If not, then, yeah, we can just, like, address them.
**Liudmila Molkova** 32:59 Yeah, I think this is, Like, from my experience, the eyeballing I wouldn't say it's reliable. I believe you that you did amazing effort, it's just that it will change over time.
And it won't be possible to prevent incompatible changes. Like, there are two ways to prevent. The first one.
Not mutually exclusive. The first one is testing, so we can incorporate the conformance testing into Python repo.
Which is straightforward. It's, like, no brainer at all.
The second one is… Can I take cover and share something?
**Lukas Hering** 33:50 Yeah.
**Liudmila Molkova** 33:51 Okay, thank you.
**Lukas Hering** 33:53 Oh yeah, by the way, I'm not, like, I'm, like, totally for the conformance testing, just adding it, like, directly here.
**Liudmila Molkova** 34:01 Yeah, awesome. I'm sorry, I've lost my branch. Give me a sec.
Okay, so… I have a prototype. It's mostly… it's a prototype because it's through the config.
But it is not.
On.
Unlimited by the config.
And, sorry, it's in Java, but it's something we're actively not super actively, but working on with Jack, with regards to configuration.
But what I… do here… Is I essentially generate.
all the… HTTP semantic conventions.
And, for example, this friend… Has, ignore this, the HTTP tracer… can… It receives the tracer and config, and it does, it can even react on the configuration changes. Anyway.
But, it has the HTTP, it starts the HTTP client span.
And it checks if the state is enabled, and it does a bunch of optimizations, and… It, for example, filters HTTP request method based on the configuration options, or it can… Do more interesting things, so for example, there is.
The service peer mapping that's defined for HTTP, and there is some code that should also be able to set Patters.
Like… Like this. This is fully generated based on semantic conventions.
It misses, like, the configuration options are a tiny bit tricky, because they are not in semantic conventions yet, and this part, we probably will take time. But, like, probably all the code that you wrote can be generated, and the generation is not unique to HTTP, it's the same for HTTP. Oh, sorry, for databases.
Or RPC. Or anything else.
**Lukas Hering** 36:24 Yeah, for sure. I would, yeah, I think I would've to see, but yeah. Yeah, there's.
Have to check again, but… Yeah, I guess for, like, some of the header stuff, I would imagine you still need at least, some… hand rolled… code for… You know, actually implementing the header, like… the, like, header, redaction and all the, like, specific HTTP semantic stuff.
**Liudmila Molkova** 36:59 It probably… Does, but it can still be done in the way.
So, like, the goal of the prototype I'm showing now is to eliminate this need.
But it can probably be configurable in the code gen. See now how, like, in the generation, there is this… The Viva YAML and you can do quite a lot of things there and configure a lot of stuff so here it's not.
Actually… There is not much configuration, but there could be.
So it can still be doable, but even without it.
It's.
There's a lot that can be auto-generated.
And the benefit is that, like, when the new semantic convention comes, like, you don't need to hard-code a vendor in the incubating attributes, right? We, react to some subtle changes, just renovate can go and regenerate stuff.
well… When Renovate detects the version update, we can go ahead and regenerate the stuff.
Umm.
It does not mean that.
We shouldn't do what you've done. So, like, the trickiest part with the codegen is to figure out the API shape.
And then just, like, give AI the API shape, and then say, write this ugly, terrible ginger that I never read.
To repeat what… what you wrote by hand.
So maybe… I think a good step is to polish the API that you have.
And then… .
I can just make a pass, do the prototype, and we can see how far we can go with CodeGen.
**Lukas Hering** 38:57 Yeah, so the public, like, if you go back to the PR, the public API is, like, extremely minimal. It's just the HTTP client request and response objects.
So… I would think that we could add the code gen, I mean, almost later, without impacting the public API at all, right?
**Liudmila Molkova** 39:19 Yes.
Exactly. So let's, I'll take a look, because… anyway, I'll take a look, and let's get it in, and then… The content comes after.
**Lukas Hering** 39:35 Yeah, that… yeah, I… I mean, we could do that, like, do the whole… everything proper right away. I… I don't know, like, I feel like that might be a little too much, though, but…
**Liudmila Molkova** 39:45 Exactly, yes, yeah.
**Lukas Hering** 39:49 Yeah, Aaron.
**Aaron Abbott (Google LLC)** 39:51 Yeah, so, I mean, I had… I guess this is what you're saying about them being not mutually exclusive with Miller, but, like, if you have… for example, additive things in the spec, the update happens, and we generate more code, but, like, the instrumentation obviously still needs to be updated to use it, so, like.
that's expected, right? So, for example, say, like, headers… headers were added.
It would generate the new setters, but nobody would call that code, right?
**Liudmila Molkova** 40:25 Yeah, so it's a mixture, right? So sometimes the changes are… like, for example, I've seen in the Lukas prototype that it takes the complex object and populates things from it, right?
So, if the information is already present in this complex object, if instrumentation already calls this method, right, then nothing needs to change, or, like, we would… I don't know, when we report exception, we would pass the exception object.
And there will always be cases when it's not yet Instrumentation does not call it yet, but at least we will have the There.
Generation automated, so it can start calling stuff.
**Aaron Abbott (Google LLC)** 41:09 I'm curious, do you have examples where, like, the semantics changed in such a way that just updating the generated code would Suffice.
like, I guess a rename is a good example, but wouldn't the generated code just change the… like, I know there's not going to be breaking changes in HTTP, for example, or there might be, like.
New unstable things that get added, and then… Say it's, like, set… set route versus… I don't know, set… Something else that is similar to Route, right?
I guess I'm having a hard time understanding Examples.
**Liudmila Molkova** 41:52 The configuration?
It's a good example, because we will add more configurations.
Add.
E- even if it doesn't, like if it gets you halfway.
It's still better than if you need to write everything manually.
**Aaron Abbott (Google LLC)** 42:09 Okay, yeah.
Umm.
And then one of the… well, maybe actually Lukas, go ahead, please.
**Lukas Hering** 42:15 Oh, yeah, I was just gonna comment. So I think… I mean, in my eyes, the way I see this working is we have our public Python API, we have some glue code that would bridge to the auto-generated code, but the glue code would probably have to change whenever the auto-generation reruns, right, for the… but that would just really change for the incubating stuff, just because the stable stuff would never change.
But yeah, so I think we should try to… I guess, Lumila, what you're saying is we should try to make the, like, auto-generated stuff as big as possible. And then have, you know, the minimal amount of glue code, and then the API, right? And it's only the glue and the API that we write by hand.
**Liudmila Molkova** 42:52 I would imagine that like ideally the glue there won't be a glue code.
like, in the no-glue common code. The instrumentations will still be some glue between, like, what the instrument, right, and the generated code, but Ideally, the HTTP UTO should dominantly expose generated helpers.
**Lukas Hering** 43:18 Okay, I mean, yeah, maybe I'm thinking… I'm thinking more like what Aaron's thinking, like, I'm not sure exactly how that… are you saying we just… I mean, our API is the auto-generated code, and at that point, all the HTTP… I guess the issue with that, though, is that, you know, breaking changes you know, we'd have to basically update all of the H. We we kind of run into the issue.
**Liudmila Molkova** 43:41 Oh, there won't be breaking changes, right? Why would there be?
**Lukas Hering** 43:44 For incubating, though, oh.
**Liudmila Molkova** 43:46 for me.
**Lukas Hering** 43:47 that HTTPs support incubating,
**Liudmila Molkova** 43:52 Oh, you want the stable API for incubating things.
**Lukas Hering** 43:57 Right, yeah, that's also the idea of this, is that the stable API would also be able to, underline, or… like, the idea is, like, it's supposed to be as… I mean, we might have to add stuff to support, incubating stuff, but the API would be stable, and then it would be able to internally implement anything.
It's like…
**Liudmila Molkova** 44:20 imagine.
**Lukas Hering** 44:21 which.
**Liudmila Molkova** 44:23 Imagine like we are adding new attribute and semantic conventions like URL template is a good one. It's incubating.
For now.
And… There should be a a method that sets it.
Like.
**Lukas Hering** 44:40 The public, the public request object. So if it ever goes away, it's just instrumentation will pass it. It's dead, dead weight basically. I mean, we can remove it to two dot x basically this kind of idea.
**Liudmila Molkova** 44:51 Yeah, but, like, the API you would generate is not set attribute, right? Or the API you want instrumentations to call is not set attribute, because… Maybe you just want to pass the euro.
Like, where it's a complex object, you don't want to even care about serializing it or whatever.
And… you would… A.
I… or maybe it has some configuration options to sanitize and whatnot, and then… We would want To generate or invent a method that allows to set this thing.
And… It is an additive change.
But maybe… We cannot have the experimental method on the stable class. And then we would need to generate two versions of the same.
span, and helpers for the same span. The one for stable, one for incubating, and instrumentation decides which one it works with, depending on the flags.
You see what I mean?
**Lukas Hering** 46:00 Yeah, yeah, maybe I had to see maybe an example, but yeah, Aaron, did you want to go back to your other point?
**Aaron Abbott (Google LLC)** 46:08 Well, I feel like we're all saying the same thing, and then maybe it… just have to look at Ludinola's prototype and get an idea for, how those issues are solved, because… If you could handwrite the code, I guess in theory you can generate it, so it seems roughly the same.
Yeah, one other question I had, I think error handling is a good example. So, like, the normative parts of the spec that aren't captured in structured… in anything structured in, like, the YAML files.
How does that… Does that kind of just get put into the… into a specialization of the template?
So for example, Yeah, like, like error handling, right? Like, There's specific error handling for, I guess, HTTP vs DB vs GenAI.
And we can't… like, the util can't know what to do. The instrumentation has to do something, and I guess… Designing a hook is 1 thing, but then the next part is actually like.
for example, normalizing common error codes or something like that, which you would have to do for HTTP. I'm not sure if that part is… In the schema besides generating like an enum, right?
**Liudmila Molkova** 47:26 It's not, but let me share another one. So this is the CodeGen for Gen AI that's in the PR.
So there is this Weaver YAML that I showed before for the configuration demo. This is a better example.
So, everything that's not in the YAML schema can go here. So, for example, here, I have histogram boundaries, so they are hard-coded, but eventually it will go away. There is some other things. It's, like, just a temporary story. So, for example, for instrumentation, we generate the span and metrics at the same time, and it's, like, it's a little bit convoluted for Gen AI, but essentially, we also have the template for span names and everything, and you can easily imagine that There is a list of, things that are considered hardcore… that are considered error codes for HTTP client here, as just a part of the configuration for the code gen.
**Aaron Abbott (Google LLC)** 48:29 Yeah. Yeah, I mean, the, like, the time to first chunk, time per output chunk is a good example, or, time to first chunk, and then the overall, like, duration is an interesting one, because I think Like the spec, there's a lot of pros in it that says, do not include the time to first chunk in the overall.
Or I mean, I'm thinking of the inter inter token.
Latency one, right?
**Liudmila Molkova** 48:54 Yeah, and what is, here is that the generated code would say, okay.
This is reported for each operation.
And this is just the helpers that are generated, and something needs to call them.
The glue code or instrumentation itself or something. For HTTP and databases, it's much easier.
**Aaron Abbott (Google LLC)** 49:16 Yeah.
Yeah.
Okay, yeah, it sounds, it sounds like… Not everything is solved then, and that's okay.
**Liudmila Molkova** 49:29 Not everything is solved, but it is solvable with some glue config.
And the Glue config, what's good about it, it's also language agnostic, so, like, languages can… Learn from each other.
**Aaron Abbott (Google LLC)** 49:44 Yep.
Cool.
**Liudmila Molkova** 49:48 Cool.
**Lukas Hering** 49:53 Lamila, is that, is what you have, public or do you mind sharing it if, if you're open to it?
**Liudmila Molkova** 49:59 Oh, absolutely! Yeah, it's public. I'm going to undraft it, by the way, quite soon, once I figure out if there is anything else that's blocking it.
**Lukas Hering** 50:18 Okay, yeah, that's all I have there, so… Boom.
**Tammy Baylis** 50:22 Awesome, thank you. Any other last-minute topics?
Cool. Okay, thanks for a great meeting. See you all next week!
**Diego Hurtado (Dash0)** 50:37 Thank you.
**Liudmila Molkova** 50:38 Thank you.
**Diego Hurtado (Dash0)** 50:39 Right.
