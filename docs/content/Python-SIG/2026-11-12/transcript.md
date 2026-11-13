SIG: Python SIG
Date: 2026-11-12
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Riccardo Magliocchetti** 04:09 Hey, everyone.
**Hector Hernandez** 04:13 So…
**Diego Hurtado (Dash0)** 04:14 Let's go ahead.
**Tammy Baylis** 04:18 Hello!
Hello, okay, let's get started. Meeting notes that you should see are in the chat, and… Welcome back to the OTELPython SIG meeting. I'm not at KubeCon, but I think lots of people are, so… We'll see how much we have to talk about today.
Please add your name if you haven't already.
Let's just do some triage for 5 minutes.
I think I did the core board last time, so we'll just look at some contrib PRs right now.
So… Big table, sorry, where are we at? We're waiting on reviewers… And, this has some reviews already, but let's just have a look at 5066.
Fix Confluent Kafka, align producer and consumer spends with SimConf. That's a great idea.
You have a linked issue… Oh, sorry, that's, PR… there's 3 issues.
Okay, these are… We'll request these… Is this the issue?
Okay, maybe that's it. But there is a lot of context, and there's been discussion already.
Yeah, some maintainer comments already. Okay, it's, Yeah, please keep having a look at this one, thank you.
Processor baggage… Lukas… This is being reviewed already, but we have… Have some discussion on it.
Thank you, Riccardo, for reviewing this one.
And this one as well, whiskey… Capture content, type, content length, request headers.
That's triage already. I should be looking at the ones that don't have any reviewers.
Bishop, HG Server Metrics opt-in server… I think we have… Some effort going on already to add HTV server metrics.
And I talked about this with a student contributor a while ago.
Yeah, I'm gonna have to look at this one later.
Yeah, I'll keep that open for myself.
Hmm… That is ready for review. No, I'm… I'm sorry, gonna comment on that later, I'll leave it alone for now.
Mmm… This one's been reviewed by… Non-approver.
I'm curious as to what it's about.
Fixed tornado records server metrics. Once, boom, more server.
I'm gonna take a look at this one, too.
Hmm, this one already looked at by Riccardo, thank you.
Different one, AOHTP, A, I, O, HTTP, the server library. Capture all values of repeated headers.
No linked issue, but some explanation.
Hmm.
I think we can look at that.
And neural lib 3… Because the same contributor approved by, got a gray check already.
Yeah, please have a look.
Kafka Python, add no op tracer. Oh, we love, we love tests.
Yeah, that'd be great.
It's 10-10, let's move on to some… Regular topics.
Okay, let's start with Lukas and SDK… Add support for advisory attributes on metric instruments. Go ahead.
**Lukas Hering** 12:11 Yeah, just wanted some, eyes on this again, since, Aaron merged some changes to allow us to add, Additional keyword arguments to… Some of the meter methods.
So I've just updated this PR, To just add an additional advisory attributes, keyword-only argument.
Yeah, so, I see Leighton already reapproved, but I've requested reviews from other folks that have looked at this, so, yeah, that's pretty much all I wanted to mention. Yeah, this is also, I think, I forgot, I forgot Dashpull's real name, but Dashpull, he has, yeah, David has, some other work that's blocked on this, for metrics, so… Wanted to unblock him.
**Aaron Abbott (Google LLC)** 13:13 Yeah, awesome.
**Lukas Hering** 13:14 But I have this one.
**Aaron Abbott (Google LLC)** 13:16 Yeah, thank you, Lukas. I was wondering… like, I know my PR added the… the things, so technically we're good to go, where it would add keyword orgs if needed, when the API definition is different than the SDK, but… I was gonna ask, like, or sorry, rather when the SDK doesn't have star star keyword args.
I was gonna ask, do we, like, know all the places we need to add it? Should we do… should we do, like, the Star Star keyword arcs in a separate PR from this one? Any thoughts?
**Lukas Hering** 13:51 Yeah, I was actually, I'm gonna bring that up in the second point of… Or the, the second topic, I guess for bloggers, but, Yeah, I can add that to… I can… I can add the keyword arguments, to this PR, that should be fine.
Do you have any opposition to that?
**Aaron Abbott (Google LLC)** 14:17 Well, this one does add it, right? I think I looked at it yesterday.
Maybe I'm thinking of a different one.
**Lukas Hering** 14:24 Let me… let me take a look again. I think…
**Aaron Abbott (Google LLC)** 14:28 See what Claude did.
**Lukas Hering** 14:29 Oh, yeah, I did, yeah, yeah, yeah, yeah, so, Just so we don't have to do the wrapping.
**Aaron Abbott (Google LLC)** 14:35 Yeah.
**Lukas Hering** 14:36 Wait…
**Aaron Abbott (Google LLC)** 14:37 I don't know… Yeah, I don't know if… Yeah, I don't know if, Dylan, you want to speak also, but there was, like, this idea to just allow the wrapping to do it.
instead of the star star keyword args on our API, but… like, I personally think we should just add it so that the… The code is kind of, like, obviously… Correct, or obviously not breaking every time.
So I think I'm in favor of… Does this one update the API as well, actually, Luke?
**Lukas Hering** 15:11 Yeah, so actually, I was gonna… I was gonna also ask on that. So, I added the keyword arguments to the SDK, so we don't have the wrapping.
We also get, I guess, the little performance boost.
But I didn't add it to the API.
So that was actually… I guess we can just jump into my second topic, which is the, the… oh, wait, never mind. I guess I removed it. But, We can just go back to the PR. So we can either… We can add that.
like, keyword arguments… the empty keyword argument signature.
To kind of just hint that implementations should be diagnose, but because we're the wrapper, it's probably not really necessary.
It also kind of makes the API a little uglier, in my opinion. So… I'm, like, slightly, like, in favor of just… not having the keyword arguments in the API definitions, because we have the wrapper. But, I mean, I could go either way,
**Aaron Abbott (Google LLC)** 16:21 Gotcha.
Yeah, I can… does everybody feel like they have enough context to talk about this right now?
I know it's kind of in the weeds, but
**Lukas Hering** 16:38 Yeah, so I think the only open question is whether we want that star starK works empty in the ACAS intro itself. I think adding as an SDK is, like, a no-brainer, like, there's no downside.
**Aaron Abbott (Google LLC)** 16:51 Yeah, I'm kind of in favor of putting it in the API, just… so I think… There's, like, a couple variants as well.
One of them… one of them where we use, like, a specific type dict… type dict… argument for this unpack thing, it would prevent people… it would prevent downstream SDKs from, like, experiencing this as a breaking change, but they also wouldn't be alerted to the fact that there's a new parameter that they can optionally handle if they want.
So, I guess, like.
in terms of communicating that things are breaking, I feel like putting in an API… sorry… communicating to SDKs that they should do this StarStar Keyword Args thing.
in, like, a way that's not, you know, just pros or whatever, I kind of like putting it in the API.
But yeah, I could see how it makes things a bit uglier.
**Lukas Hering** 17:45 Yeah, we can, chat more offline, and yeah, I think that that can also be maybe its own PR, So, yeah, like, if you want to open that, or I can open it as well, we can add that to… at least all the API definitions that extend the signature combat.
Let us…
**Aaron Abbott (Google LLC)** 18:08 Yeah.
And I think… So the other thing is this star here that we add,
**Lukas Hering** 18:14 Yeah.
**Aaron Abbott (Google LLC)** 18:15 So unfortunately, there's no way… if there's no arguments, like, after… Say, like, you didn't add Attributes Advisory here, if you didn't do that, you can't put the star in Python, so there's no way to communicate, like.
if an SDK adds an extra parameter, that it needs to be by name only.
Unless you add, like, star, and then some kind of dummy, or you use star star keyword arc. So I think there's a couple, Honestly, it's… it's, like, way too nuanced. I feel like this is a kind of ugly part of Python.
But yeah, we can take it offline. I think there's some pros and cons.
**Lukas Hering** 18:54 Yeah.
Sweet, thanks. Yeah, second one is… Also, another kind of nuanced topic, but… So the, click on the next, yeah, the next one here. So currently, like, our declarative config, we use pyaml, which is… YAML 1.2, it parses with YAML 1.1.
Whereas the spec kind of wants 1.2. There's a few, like, subtle differences, which are kind of outlined here.
So, Riccardo already looked at this, and like, his concerns are valid.
like, I mean, this RUAML is not very… it doesn't seem like it's well maintained, and it's on, like, CurseForge or something, or SourceForge, But the… I guess the benefit is that we'll then be 1.2 compliant. I… it seems like this is really the only other option here, so I guess I just wanted to see what people think, like, if this is a really big deal or not. Like, if not, we can just stick with 1.1 and just… you know, say, okay, we're not going to support YAML 1.2, because it's not really that practical.
Yeah, Diego?
**Diego Hurtado (Dash0)** 20:21 Sorry, it's, Is this… is the motivation for this is only to be able to parse YAML 1.2?
Is this an effort to… not have the Pyaml dependency.
**Lukas Hering** 20:39 So, there is some benefit with this, is that, RUAML is, like, pure Python.
So it's easier to vendor, I think Pyaml does have a pure Python implementation, But yeah, yeah, the big one is just the YAML parsing compliance.
So… Yeah, so yeah, that's really the primary one. There's some, like, subtle differences between BIAML and RU-AML.
Yeah, Riccardo.
**Riccardo Magliocchetti** 21:21 Yeah, I have a true question. The first one is… well, not sequest, but, like, I'm a bit afraid, like, I'm not able to understand if… This new library is introducing, Or not breaking changes.
Because, like, they have a big banner in PPI, but we're probably going to change the namespace.
Sometimes in the future.
And… but, like, at the moment, I worry if, like, 0.19… as the same API, as the one you… you're using VPR, because otherwise.
You know, if we're still breaking… APIs, because it's 0. Something.
That could be a problem, I guess, for the packaging people.
Might as well.
**Lukas Hering** 22:22 I can maybe follow up offline, but it kind of sounds like we're kind of… stuck here.
Yeah. Yeah, I don't really know of any, like, I mean, there are, like, a few packages out there that'll give us 1.2 support, but they're not… they're not well maintained.
Or they look like they're bi-coated or something, so, Yeah, I'm not sure, I, like, yeah, so… Alright, yeah, we can discuss more, so… later.
**Riccardo Magliocchetti** 22:55 Yeah, and then the other question I have is.
Can we extend, like, somehow Pyaml to… To handle, like, this… Specific, values we want to.
**Lukas Hering** 23:11 Are you saying, I did see there's, like, a library that can make Pyaml pars 1.2. I didn't really look into it that much. Is that kind of what you're suggesting?
**Riccardo Magliocchetti** 23:23 Yeah, that, or, like, do a post-process to whatever, Paill gives, gave us.
**Lukas Hering** 23:31 Yeah, I can… yeah, I'll look into that, I just didn't know if, like, that's, like, reliable or not. But yeah, okay.
**Riccardo Magliocchetti** 23:39 like, assuming that, we just care about, like, 6 values or so. Yeah. Let's talk about that, like… Like, they or no for yes, no, yeah.
**Lukas Hering** 23:52 Okay, yeah, thanks for the… the suggestion.
Yeah, we can probably move.
move to the final topic. Don't want to take up too much time. Do you mind if I actually take over screen share for part of this?
Yeah, so, I guess, Just for context, there's been, like, I know we had a lot of back-and-forth discussion about vendoring and, the hotel injector and making Python, You know, friendly for, like, automatic… injection and not having library conflicts. So… I know we floated the idea of, like, creating an agent package, and… the PR that I've linked.
Kind of has a prototype That we could consider to go down.
And yeah, I just kind of wanted some initial thoughts and feedback, maybe.
So basically what I've done is I've kind of created a vending package CLI, That's similar to the vendor package that PIP uses.
So… If I go into the agent here… I can… so let me first just clean everything out.
So we just have, like, a requirements.txt with all the hashes of all of our dependencies.
And then, we can sync, which will take all those dependencies, load them in.
And it'll actually do the… all the import rewriting, for us.
with, libcst. So it's actually, like, A little more versatile than the… the, the veterinary package, and then… All this is kind of, like, configurable in the… PyProject Homo here, so… You can draw, like, certain files, and there are, like, a few manual patches we'll have to add here.
And I guess the interesting part is that I was actually able to… purely vendor protobuf, Since it does provide a pure Python implementation, And I did even go a step further, and was able to vendor DC extension by basically taking the SDIS, And applying a patch.
And, basically we can ship a pure Python wheel, and then also, like, wheels for each architecture.
So, yeah, I guess for people that are interested, like, feel free to take a look at this.
I don't know, like, whether this belongs in Contrib.
or a new repo, I think it can belong in Trib, although, like, admittedly, if I commit all vendor files, it's, like, over 250,000 lines.
So… Yeah, just… just wanted, like, maybe… Feedback, whether, like, we want to do something like this?
like, an OTL agent, kind of similar to Java.
**Aaron Abbott (Google LLC)** 27:17 Cool. Yeah.
**Diego Hurtado (Dash0)** 27:20 Maybe this, sorry, this should have its own repo?
**Lukas Hering** 27:27 I was kind of thinking that, just to keep it clean, because, yeah… Yeah, are there… does anyone else think it just belongs in its own repo, or, I mean, yeah.
**Aaron Abbott (Google LLC)** 27:43 I didn't get why there was 250,000 lines. Was it, like, are you checking in the vendor code kind of thing?
**Lukas Hering** 27:50 Yeah, so there's two options here. We could, like, keep the vending out, or do the rendering as, like, NCI, or commit them.
I think typically, like, most peop- most, Packages that do vendor, they commit all the vendor stuff.
Just to, but assuming this is, like, fully reproducible, I guess there's not… there's no reason to keep it checked in.
**Aaron Abbott (Google LLC)** 28:20 Yeah.
**Lukas Hering** 28:22 So… but if we did check it in, I think that's where the separate repo would make more sense.
**Aaron Abbott (Google LLC)** 28:30 Yeah, I feel like… I'm not sure about Python, but I feel like it's a bit split, like, in Go, I think you typically check it all in, because there's a vendor folder that gets generated, and then I think for the Java agent, the… I think it's called Shade.
plugin, I'm pretty sure it just is, like, a compile time thing.
But yeah, I agree, like, if it's hermetic, it seems… And we have… and we have, like, a deep block file, it seems fine to just… Do it as part of the build.
How big is the, like, the wheel?
**Lukas Hering** 29:08 I haven't actually… Checked. I assume it's… Maybe, like, 5 megabytes? I would have to double-check again, but, Yeah, I mean, in theory, it would be no bigger than you would normally have, assuming you don't install these extra dependencies.
Yeah, the approach I did also take is, So this isn't actually the full size. I think. It's probably best… And maybe we can… we can talk about this, but I did just… I also vendored every… all of our hotel packages inside this as well.
So… you know, even if the user hypothetically had their own, you know, version of OTEL installed, it would still work.
**Aaron Abbott (Google LLC)** 30:08 Yeah, I know… I'm pretty sure the Java agent does something similar. I think it might… even vendor, like, the SDK and the API context, so that, I'm actually… I'm not 100% sure how it works, because I think they really don't want to conflict if the user has, like, a different API requirement, so… We could probably, like, learn from them the best way to do it, but… Yeah, I think that it's always tricky with the context, because they're just, like, a global namespace, even if you have multiple SDKs. So if you don't have multiple versions of the SDK, This is another issue, and I think in JS, or in, In Hotel.js, I think they do… isolate context keys, because you can install… you can already install with NPM multiple versions of the SDK.
Just something to keep in mind.
**Lukas Hering** 31:02 Yeah, so yeah. Yeah, actually, so one call-out, the only thing I wasn't able to vendor right away was, GRPC.
It's… yeah, that's a very big pain. So they only have native wheels, and they also ship a wheel for every single Python version and system, so they have, like, 40 wheels.
**Aaron Abbott (Google LLC)** 31:21 Yeah.
**Lukas Hering** 31:23 And so, like, we could do, like, like, I think it might be possible to vendor it. I think a better approach would be maybe extending our gRPC exporters to additionally support a… there's another one that uses H2 that we could use that's… that would be easy to vendor.
So we could, we could discuss that as well.
**Aaron Abbott (Google LLC)** 31:49 Yeah.
I mean, I think I'm generally in favor of this, we could kind of work out the details, but it seems like it would… like, we can… as a SIG, mainly focus on, you know.
normal Python stuff and targeting library developers, and then this can have all the customizations for injectable stuff, like… Yeah.
Actually, I am curious how different this is, after all is said and done from what's already done in the packaging SIG. I don't know if you could speak to that, Diego.
**Diego Hurtado (Dash0)** 32:27 Right, so… It isn't in… in theory, any different, right? Considering the fact that we have been Vendoring our own… We're making our own exporters that use our vendor with the Versions of, By portal and stuff.
So, yeah, in essence, this is, The same we have been doing, but bigger, right?
your scope?
**Lukas Hering** 33:05 Yeah, maybe it's worth, like, Diego, I'm sure you probably have, like, a lot of comments on this, and obviously, yeah, it's just a prototype, so, like, we went down this, Yeah, I could definitely use, like, feedback here, but… Sorry, what was my, what was I trying to get at?
I think, I do agree, though, like, I think this would… it would benefit not just the injector to have something like this, like, maybe, like, AWS Lambda with layers, for example. They could just ship this agent, so it would never conflict with user dependencies.
So, yeah, that's just not something to add. So, like, So, like, I guess what I'm saying is, like, we could definitely take, like, some of what has been done in Injector, and maybe bring it into Contrib for the agent, the agent baggage itself.
I think that could be worthwhile. Because, yeah, I mean, this would… this does have, like, some benefit outside of just the injector.
**Diego Hurtado (Dash0)** 34:14 Yeah, it is an independent thing. I'll have to… to… Trial with the injector itself to make sure that the that it's… it's… it worc… it works, because, I don't remember exactly the… The order in which we injected in the… System packages, directory, right? So, I don't know which… If it gets loaded first or less, but, Yeah, I'll experiment, we did, And, I mean, if this is a solution for… We're doing the Hector will, well, sounds great, wait.
Because, yeah, the only solution that, The only other solution, which actually I have tried, but I… I didn't… continue the effort was fixing Python itself.
fixing pip, fixing Python, fixing… so that it works like, I think it's Node.js, right, where you can actually have.
**Lukas Hering** 35:15 Yeah.
**Diego Hurtado (Dash0)** 35:16 Multiple… Dependencies, in the same virtual environment.
Which would be… would be great, but I guess it's, it'll take years.
If it's even possible, right?
**Lukas Hering** 35:34 Yeah, for sure.
Yeah, if there's not any other… any other comments, I can… I can hand it off, to the next person. Thanks for all the… all the input we can… maybe continue the discussion in Slack, or in GitHub as well, so…
**Aaron Abbott (Google LLC)** 35:51 Yeah, thanks for working on this.
**Tammy Baylis** 35:58 Cool, Hector and log stabilization.
Go ahead.
**Hector Hernandez** 36:06 Hello, yeah, thanks. Just checking again, I just come every 6 months to check on this, Just wanted to see… I'm trying to… to help to move this forward. I can see there's a couple of PRs that are open, most of them by Lukas.
Is there any other issues that are pending here? We have, like, two projects linked here. I think that the last one is the one that is actually… the correct place. So, my question is more about… Is this the correct place to track this? Is there other pending stuff that we need to do? Do we need to go again through the technical committee review, that kind of stuff?
And, the other thing is, like, JavaScript just released its table logs, like, last month. So I'm like, yeah, not sure what's going on in Python, but, Yeah, happy to help here, just checking on this.
**Tammy Baylis** 37:11 Yeah, Lukas, go ahead.
**Lukas Hering** 37:13 Yeah, just to comment here, so, so there was a few things that kind of blocked this for a bit, so Aaron brought up that we should look into just optimizing a bit, so we've So that work, I think, is done now. The only other work is the question of the forward compatibility.
we were thinking about yeah, the whole discussion with the keyword arguments, which is what I don't need to go into, but, once that's resolved, like, we should be able to, I think.
start merging those stabilization PRs.
Unless I'm missing anything. I see Aaron came off mute as well. Maybe he has something to add?
**Aaron Abbott (Google LLC)** 37:52 Yeah, I was gonna say the same thing. We made a couple, small changes recently.
But yeah, I mean, Hector, you're right, like, we need to… We need to ship something, it's like, it's been a long time, and… I don't think we need to do a TC review again, especially because the mill has been… I think Ludmilla did the original TC review. She's been joining the SIG, yeah, like Riccardo just said in chat.
Yeah, that said, like, maybe we can shore up our… tracking a little bit, if… what do people think about the board that Hector shared? Should we be using that one, or… I think there's, like, literally a handful of bugs left that we should probably address and then make an RC.
**Hector Hernandez** 38:45 Yeah, I'm definitely fine with whatever. I'm happy to help driving this. I can go through the open issues to see if something is, could be potentially being added here.
Just let me know.
**Aaron Abbott (Google LLC)** 39:00 Yeah, I mean, would you want to drive this? Would you have time to drive this?
**Hector Hernandez** 39:04 Yeah, definitely.
**Aaron Abbott (Google LLC)** 39:07 Okay.
Yeah, so maybe, I don't know if you want to… Yeah, Tammy shared this issue we had also. Oh, no, sorry, that's just the TC review.
I think there's a couple issues floating around, like, honestly, Hector, if you just want to make a decision and be like, we'll use this board, or we'll use, like, an issue to track the remaining items, and… Since MPRs, I'm happy to review, try to get this over the finish line.
**Hector Hernandez** 39:37 Sure, sure thing. Yeah, let's… let's have some traction here. Last… last part of the race, right?
Thank you.
**Lukas Hering** 39:50 Yeah, I think, yeah, personally, I think we should target the next release for, or target log stabilization for the next release.
And yeah, I'm not sure, so the issues on there, I don't know about any of them are actually blocking stabilization either.
I think the big one is just the… the… the… Yeah, those keyword arguments went in, I think… There was a… I think we already… we already… that other issue actually should be closed, I think. I can look into that.
**Aaron Abbott (Google LLC)** 40:35 Which one, Lukas? The severity one?
**Lukas Hering** 40:38 Yeah, the switching to Indium, there was a PR open, and I believe we merged it.
**Aaron Abbott (Google LLC)** 40:43 Oh, okay.
I can also track that one down, but yeah, that's… that's the only, like, remaining… blocker that I know of, at least, besides the performance stuff we were talking about. Sorry, the, keyword args thing, which we'll take to Slack, take it offline.
**Lukas Hering** 41:00 Yeah, and then there's also the logging instrumentation library, but that, again, is not going to block the SDK stabilization.
**Aaron Abbott (Google LLC)** 41:27 Well… I guess… That's the end of the agenda, if nobody else has anything.
**Diego Hurtado (Dash0)** 41:32 Sorry, sorry, a quick thing. Can someone open contrib?
PR5221, please.
This is gonna be real quick.
Right, okay, thank you. So… We have a lot of, security alerts, right? If you click on security and quality up there, please, thank you. Vulnerabilities, and open the first one.
see that it says dependable couldn't fetch all your path-based dependencies. Okay, so… This, I have a couple PRs, 5221 and 5223, that, should, fix this, error. I wanted to clarify it here, because it's super confusing.
We have decided to migrate to renovate.
That doesn't mean that we don't need to fix this problem. Renovate, it's… a thing that, basically opens PRs to update dependencies.
Dependabot is the name that we give to several different things.
One of them is something, roughly equivalent to renovate, but worse. And the other things that we also named Depend Abbott is, the thing that opens this kind of alerts, right? So… We're still gonna have these, this problem where we get a dependable alert with this error if we don't fix these things, right? So, I have closed a few PRs of mine that added Dependabot configuration, because those are actually not necessary now that we have, now that we have decided to migrate to renovate. But there are… there will be a couple of other PRs that also include Depend Abbott in their name, so… Lisa still… Review and approve, because we still need them.
To finally clear… Dependable alerts that we are still gonna have when we immigrate to renovate.
So yeah, I don't know if anyone has questions. This can be super confusing, it was super confusing for me.
**Tammy Baylis** 44:25 Riccardo.
**Riccardo Magliocchetti** 44:26 Monthly.
Yeah, I agree, we… Need to help tools, parse our requirements files?
But said that, I think we'll always have warnings or security issues, because we're testing with very old,
**Diego Hurtado (Dash0)** 44:43 No, we… no, we should, Renovate should be fixing that. I'll be opening… Prs, that, the… Okay, wait, Emilio, by the way, do not merge the renovate PR in contract. I just found a problem, a serious problem there.
the, I have found… I just found a solution for what Riccardo said about these old, environments, when we moved to renovate.
We will be able to exclude those environments.
But now that I've mentioned it, I don't know if it's gonna exclude them from the alerts.
We may need, no, I think Karinovich should handle that. Okay. Anyways, just, Stick with me on this, PRs for Innovate, sorry for Dependabot, because we still need to fix these warnings.
And, I hope that by next week, I will have a… A complete plan on how to fix as many problems that we have right now with Dependable and Renovate, including the… The… the alerts that we're getting, because we have all the… Testing environments.
**Aaron Abbott (Google LLC)** 46:17 Cool. Just a quick question to you. The fix is to make it, relative paths?
Like, it's not to just remove these, right?
**Diego Hurtado (Dash0)** 46:30 Yeah, exactly. It's changing the way that we specify the paths, not moving it.
**Aaron Abbott (Google LLC)** 46:36 Okay.
Yeah, sounds good. I think one… I'm not sure, in a couple places we use uvpip compile.
And I don't know if it generates the correct, like, format that DependentBot is expecting, so… If you already have a PR, I can just take a look at it, but that's… that was my only thought. Sounds good to me.
**Diego Hurtado (Dash0)** 47:00 Yeah, I'll… I'll post a Slack message in the… in the approver's channel, with these PRs, that should help us get rid of this, warnings, which are… I think, a lot of them that we have right now.
But yeah, in any case, thank you for your attention to this topic. We are moving forward, we have closed hundreds of alerts already.
**Tammy Baylis** 47:40 Okay,
**Diego Hurtado (Dash0)** 47:41 That's it on my side, thank you.
**Tammy Baylis** 47:43 Thanks, Diego. Anything from anyone else?
Okay, let's call it for today. Thank you, and enjoy the rest of your day. Bye.
**Aaron Abbott (Google LLC)** 47:58 They're on…
**Diego Hurtado (Dash0)** 47:58 Two, smooth.
**Lukas Hering** 48:01 Thanks, everyone.
