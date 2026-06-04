SIG: .NET Auto-Instr SIG
Date: 2026-06-03
Duration: 50 minutes
============================================================

## Zoom Recording Transcript

**Piotr Kiełkowicz** 03:33 Hey guys, I think we can start.
Chris, would you like to drive the meeting today, or not so much?
**Zach Montoya** 03:57 Oh, yeah, I can drive.
**Piotr Kiełkowicz** 03:59 Cool, thank you.
**Zach Montoya** 04:01 Alright, so let's get them squared away… Alrighty. So I know we have some discussion going on with, one of the… The app level, or the app config.
Think… Is that domain… Which one is it? Supplementing resource attributes. Do you guys want to talk about this first?
Let me just start here.
**Piotr Kiełkowicz** 04:36 I think perhaps not today, but we can make the decision.
Based on yours finding, probably.
**Zach Montoya** 04:46 Sorry, what was that?
I didn't quite hear that.
So, essentially, like, the reason why I thought we might want to bring it up, Is because we need to arrive at a sort of design decision here, and Igor and Crisp were commenting on this last week, but I think it would probably help from the SIG to try and accelerate the conversation.
I don't know if it'd be easier to read, or if, Igor, if you could summarize the main points.
**Igor Kiselev** 05:27 I… in my last comment, I tried to summarize it around 6 questions that we should answer, to make a good decision about what we need.
**Zach Montoya** 05:39 F.
Yeah, so the first one is, should we support peropt managed configuration?
So, right now we have the app settings, they… they get promoted.
And so, we basically are maintaining We're promoting any of those attributes to the entire process, rather than per app domain.
**Igor Kiselev** 06:04 My answer rate that I probably prefer to support per-up domain configuration in a usable way, because we already have per-up domain configuration problems explicit, as environment variable could change between different subdomains created.
we read them on updating when we initialize agent inside abdomain. So, as we already not guarantee that different abdomain will use the same configuration, it'd probably be better and more logical to explicitly allow Everson, that is not… Application level to be configured per up domain.
**Chris Ventura** 06:40 Is it true that if the environment variable changes, that when the new app domain loads, it gets the new value? Or does it simply get the value?
That was captured when the process started.
**Igor Kiselev** 06:56 No, it is not. It reads environment variables, and environment variables would be valid readers, so when we need configuration system in new subdomain.
It would… what it get?
And as agent installed separately in each subdomain.
So, yes, process level, what is… In the profiler, it would be… Defined at a provider level, but everything else…
**Chris Ventura** 07:27 Yeah, I'm asking the question because I've just seen too many applications where, once it… once the environment variable's loaded in the process, it doesn't matter if something else gets loaded in, the old values get cached, so I just wanted to… Double-check that behavior.
**Igor Kiselev** 07:46 My understanding, no, it would be at a time when a configuration system isn't sliced.
**Zach Montoya** 07:54 I think the only time that that really comes into play is if we're using… if someone has a Windows container and they're doing, like, an IAS, like, Windows container, because then that one doesn't promote environment variables very well, or… There's just race conditions.
Hmm.
So, if we… I think, like, one question about the per app domain managed configuration is… I think it kind of goes towards the precedence slash merging.
Because…
**Chris Ventura** 08:34 Well, yeah, before we… before we even get there, so… there's… There's a viewpoint where per app domain configuration is beneficial, in general.
no, they're… Can be cases where having per apt domain… configuration can cause confusion, and Igor mentioned that this is related to the ones that affect profiler behavior.
Because that's only loaded once per process.
And so, if you've got a single process with multiple app domains, every single one of those app domains have to have the exact same profiler behavior. And so this is something that we would have to make clear To prev… to minimize a potential source of confusion.
So, my previous argument, on this PR was to just keep things simple in that, yes, we may have tried to lift stuff into the, app domain.
ARF.
Taking the app config settings and setting it via environment variables when the app domain is loaded, But… That can lead to confusion, because now you've got this multi… you've got this single process with multiple apps, and they can't all have completely different behavior.
configured. Some things, yes, some things, no.
**Igor Kiselev** 10:22 Luckily for us, okay, right now it's only luckily, but the set of environment variables that could not… that are profiler level and could not be customized per subdomain is the same set of environment… of things that we do not support through YAML configuration.
So, it was not intentional, but as we have not implemented YAML process in a profiler, we, like, already get very good split, and we already know that only a few of them are process level.
**Chris Ventura** 10:56 my question there is when it comes to… and this is where I'm gonna need some of your help, is with the continuous profiling.
Confused.
**Igor Kiselev** 11:10 profiling, it should not be profiler level, because, continuous profiler, agent, stamp profiler, properties, how it.
**Chris Ventura** 11:26 But we're not filtering down at the apt domain level.
**Igor Kiselev** 11:30 I boot… I would not… I couldn't say how… I don't think that anybody really done a good research how continuous profiling works with multiple abdomains. It may work not as we expect, because it probably, right now, already have an issue that we send, each abdomain send a configuration to a profiler, and then profiler is used first, Azer used last, or it multiplies a continuous profiler per number of domain registered. It's a really great question.
**efshaikh** 12:05 I can speak to that.
**Igor Kiselev** 12:07 Thank you.
**efshaikh** 12:08 So, did… It'll, depend on which app domain is seen the first time, and there is one-time singleton initialization.
So subsequent app domains, even if they try to send config, that will be ignored, because it's a std call once, that that's the C++ singleton mechanism that is used to create a global configuration at process level.
**Chris Ventura** 12:36 Yeah, so basically, continuous profiling is happening at the process level, not the.
**efshaikh** 12:40 Yes.
**Chris Ventura** 12:40 app domain level.
**efshaikh** 12:42 Exactly.
**Igor Kiselev** 12:43 By the way, it can be changed. I'm not thinking that we should change it, but theoretically, it could be changed, and we could make continuous profiling to be per-up domain with a KA.
we have some common threads that are shared between all of domains, but the threads probably… would not be useful because they would not have any managed stack. It may change with FTCAR's suggestion, but…
**Chris Ventura** 13:12 Yeah, so the… What I'm calling out here is that this is just yet another behavior where it's a mix of managed and native.
code where… there can be a source of confusion for this. So I'm just recommending we tread lightly when it comes to saying we support configuration at the app domain level.
I think if we can work out All of these, points of confusion, or, Where we can't really isolate things at the app domain level.
I think we need to solve those problems before we support… fully support.
App domain level configuration.
**Igor Kiselev** 14:07 Right?
I… partly agree with it. I would say that, I'd probably use here a little bit more opportunistic approach and said, let's do it, let's document it up to our best knowledge, and if there would be complaints, we would improve the documentation later.
We… it would probably not make it worse than it was, and we are really looking on a very, very, small number of our customers who would be affected by it. It's our customers who are already affected by Outworking, probably the main concern.
**Chris Ventura** 14:50 I guess my argument is, today.
Even though we're attempting to support per app domain level configuration, we're not… We're most likely not supporting it at all, because the odds of an application changing the environment variables between loading the different app domains is Very small.
**Igor Kiselev** 15:19 No, not small, if you think about it, because if, we have to, so right now, we promote web config settings to environment variables. So, it means that, first up domain would load all settings that is defined in the web config.
Second up domain would load all additional settings that have not been configured by a first subdomain. We're already in a very weird, mixed mode, so…
**Chris Ventura** 15:50 Okay, that's.
**Igor Kiselev** 15:50 Science mixed mold, the worst thing that can be.
**Chris Ventura** 15:55 That's the part that I was missing.
**Igor Kiselev** 16:00 That's… that's why, that's why my recommendation is to… to make it either fully remove it, or make it workable.
At least at some level.
**Chris Ventura** 16:10 That makes sense.
**Zach Montoya** 16:17 Where do you wanna go from here? Or, like, which part, which parts do you still wanna, discuss?
**Igor Kiselev** 16:24 So, okay, should we support per-up domain for managed configuration? We still need to decide, because our option is, first, let's do it, and in that case, we go further, or let's not do it. In that case, we should say that 5055 would track a full removal of web config processing.
So, we're still at… At the point where we need to… decide If we would.
**Zach Montoya** 16:51 Is that this question here, number 2?
**Igor Kiselev** 16:53 Question number two was not about, not about that. Question number 2 was about if we would support parap domain configuration, how exactly we will support it. But, first question is, do we need it, or should we just remove it entirely?
What are our preferences here?
My preference, I already said, to support it, but…
**Zach Montoya** 17:21 A standard… like, in a standard app, like, if we weren't… I mean, of course, our project wouldn't be involved, but if someone… OpenSelement Tree SDK manually in different app domains, like, they would expect it to, you know, they would expect each app domain to be kind of isolated and have their own managed code, so, I think it made sense to have per app domain settings.
**Igor Kiselev** 17:46 Oh… It's what I suggest here, that, we should have a settings if, opt-in settings, to support per-up domain configuration, and the first main up domain should set it, and we should just, always, use per-up domain for IIS.
So, that's my answer here.
**Chris Ventura** 18:08 Yeah, given the part that I had missed.
That we were the ones changing the environment variables between the app domain loads.
I think it does make sense to support the app domain configuration. Part of me still wants to have a simpler solution, but we have the precedent already that we partially support it.
So I think we need to keep it going forward to prevent breaking behavior.
**Zach Montoya** 18:41 I think what we can do, too, is, we can try to limit the scope of which, which settings or which things, cross that app domain line as well. Just try to remove that.
Confusion, or just make that story stronger.
**Chris Ventura** 19:03 Yeah, and going back to continuous profiling, this is more of a separate thing. I don't actually know what the expected end user behavior would be with continuous profiling.
If it's initiated from a single app domain, do they expect it to capture for the whole process, or do they expect it to just apply to code running in that app domain?
**Igor Kiselev** 19:29 By the way, it's a very interesting question, because if we said, once again, what level of isolation we expect for different subdomain, because let's say different subdomains report it to a different backend.
And now we leak, call stacks from one up domain to another application, so…
**Chris Ventura** 19:55 I think you're describing the worst case scenario.
**Igor Kiselev** 20:01 At the same time, if we, right now, it's hard to make two app domains to send data to a different backend. If we support per up-domain configuration, we make it easier. So it's… it's another angle to the same.
Decision.
We probably would not resolve, get, asked for today on a meeting, but… I… I… I think…
**Chris Ventura** 20:30 I think, for now, like you said, we can approach it with documentation.
And simply say, we do not recommend this setup.
But if you need to use this setup.
There are things you have to be aware of.
**Igor Kiselev** 20:48 Second question was, if we support it, should it be through APA config web support, or some other alternative, and which precedence should, Should it be supported through AppConfig?
also some different mechanism, and if we support a swap config, which precedence it should be. So my aspiratory rate, yes, web config is a convenient way for, for, IIS-hosted application.
Probably we may do it isolated only for iOS, and do not allow app config for other types of applications, but it would be back for 10-compatible change for Windows services.
for which we're documenting that you could use upconfig. So maybe for all of them. And, next question was, right now, the precedence is first we use environment variables.
**Chris Ventura** 21:48 Well.
**Igor Kiselev** 21:48 And secondly…
**Chris Ventura** 21:49 Actually, hold on, so if we're talking about using, should we support app config or web config? I think the alternative was to just support the official hotel declarative config.
**Igor Kiselev** 22:06 Yes, okay, right now there is no easy way to support a declarative config, but it is an alternative that I have in mind, because, first, we could make somehow configurable per up domain level what YAML config should be loaded, first option. And second option is we could add templatized parameters that would rate something from app config inside a YAML config, so you still have one YAML config, but in that case, you explicitly read that from app config, or read that from app config, or environment variable, or something like that.
So it's just… other two options in mind that I have.
**Zach Montoya** 22:51 What is the way that declarative config is expected to work? Is it such that you have an environment variable that points to that declarative YAML config, and then everything from there is solely responsible for configuring the app, and then, like, the fallback is… if there's no declarative config, then you just scan through the rest of your, languages, environment variables, or settings, and that configures it? Is it, like, that kind of… Two-phase, or like, yeah, that… Two-pass, like, approach.
**Igor Kiselev** 23:24 So, right… right now, right now, first, YAML config, we decide if we use YAML config or not. If we use YAML config, then we do not use an config.
**Zach Montoya** 23:34 Right.
**Igor Kiselev** 23:35 edibles, because.
**Zach Montoya** 23:35 Yeah, yeah, I just want to try to get an understanding of what the expected SDK behavior is like across languages first.
**Piotr Kiełkowicz** 23:43 And there is no expectation to read from other external sources.
the current design of the OpenTelemetry configuration.
**Zach Montoya** 23:53 So you would only read that, and then… It wouldn't mix… you wouldn't mix them with environment variables. You would say, if I'm pointing to a YAML, that's my only source of… Config, and you just provide whatever environment variable path to that.
**Piotr Kiełkowicz** 24:10 It is almost true, because you can inject environmental variables into the YAML file.
**Zach Montoya** 24:16 Oh, I see.
**Piotr Kiełkowicz** 24:19 So there is a possibility to say, read this value from the end bar, and it should be propagated.
To the configuration.
**Zach Montoya** 24:29 Okay.
**Igor Kiselev** 24:31 That's why it's a point where we could extend it to say that we… you have Some way to sort it from app config, or you read it from end variable, or upconfig, or something like that.
**Zach Montoya** 24:43 Okay, I see why… yeah, I see where that gets really complex, okay.
**Chris Ventura** 24:49 Yeah, and the other part that I wasn't sure of is if there's some sort of, Where you… if there's an automatic lookup at a particular location on the file system.
To figure out which, declarative configuration to load.
So, is there an implicit expectation that if you have Config file with a certain name, next to your application assembly.
Is it expected for that to be automatically loaded, or not?
**Piotr Kiełkowicz** 25:29 For now, you need to read… you need to set environmental variable, and I do not remember if it is just enable, or if you need to set both. Enable it and the…
**Igor Kiselev** 25:44 I believe both.
**Piotr Kiełkowicz** 25:46 I believe both, yes.
I will double-check it.
**Igor Kiselev** 25:51 But probably at some point, we would have some implicit.
So…
**Chris Ventura** 26:05 Yeah, huh.
**Igor Kiselev** 26:07 Again, my answer was, let's use it through app config webconfig, because YAML config is not yet ready, and it becomes more complex, and using it from app config webconfig would not prevent us from doing anything in future with YAML.
Or we could… Think about it as two different tasks right now.
**Chris Ventura** 26:30 the main reason I'm hesitant is just… I don't know if you all experience similar issues where there are just so many ways to configure different settings that there's a lot of confusion with end users about how and when to use which configuration.
And when you're debugging issues, having to check every single source.
**Piotr Kiełkowicz** 26:57 I have an answer.
I think that I have an answer, there is… we need to only set the… enable environment from the config file, and by default, it will be readconfig.yaml.
I think it assumes that it is from the context of the application.
Of the executed application.
But there is a recommendation to define both.
**Igor Kiselev** 27:32 So it means that right now, already, if you set the YAML config, on, up level, it would… and what is the base for that config YAML?
**Piotr Kiełkowicz** 27:46 documentation said config YAML.
**Igor Kiselev** 27:50 He's a really fool Because it's interesting, but I believe it would be based… if it would be based on a codebase, we probably already have a support of using different config YAML per up domain.
**Zach Montoya** 28:03 Yeah.
**Igor Kiselev** 28:05 So… Unintentional. Maybe it already worked, I'm working for it.
**Chris Ventura** 28:12 Yeah, it's either looking at the application's context or working directory, or it's looking at the, auto instrumentation.
directory.
**Zach Montoya** 28:28 Yeah, but I imagine we could… Implicitly add this port, so it would just be relative to the… the app domain or the codebase, that way it's… we can have that separation, like, for, you know.
ASPNet sites.
**Chris Ventura** 28:42 But yeah, going back to that question, short term, the argument is that app config, web config, behaves like environment variables in certain contexts, but it's at the app domain level.
And so we want to continue to support that for now.
And then, once declarative configuration, Becomes the standard. We could potentially phase out.
The other support, or at least recommend people not use it.
I'm just trying to minimize the number of places where configuration gets defined.
**Zach Montoya** 29:28 Yeah, I think it made sense that if we… Whoa.
Maintaining the abdomen level support, and then… we could try to move users onto the, the file base, or the declarative support, or declarative config. So then… So long as, if they customize a path.
Or if they just drop it in their… The directory, the application, then that becomes kind of the true source of all the configuration, minus whatever profile or environment rules are set.
**Chris Ventura** 30:05 And I also feel like, this… The types of apps that we're talking about having this support for.
are primarily .NET Framework apps. I don't think I've encountered… Modern.net app.
With multiple app domains in a while.
**Igor Kiselev** 30:28 It's not supported. Our domains are not supported on .NET, only on .NET framework.
**Chris Ventura** 30:32 Okay, it's just the app load… multiple app load contexts that you can have in Modern.net.
**Igor Kiselev** 30:39 Yes, yes, yes, and ILC is not, borderline for… Or any… so you could not host multiple applications.
What's this anymore?
It's all about backward compatibility for Dutman's framework, and mostly about IaaS.
**Chris Ventura** 30:58 Okay, so this is just really added complexity for… .NET framework applications.
Which, who knows how long they'll be around.
**Igor Kiselev** 31:09 Still, like, it's not really adding the complexity, because we already have that complexity, because we already support it.
**Chris Ventura** 31:17 I just mean in the long term. That's all.
**Igor Kiselev** 31:21 Oh, yep, yep.
Because if we would… if we would never support webconfig promotion to environment variable, I would probably ask for differently, I would say that we don't need it at all. But my answer is based on what we already support right now.
**Chris Ventura** 31:40 Yep.
**Igor Kiselev** 31:42 Whoa.
Theoda's question is what we just talked about. Should we support per-app domain YAML configuration? And our answer is, we probably already support it.
And… Should we make it more comfortable? Should we make it, in that case, perabdomain… Should we add something in future to allow… explicitly set a pass for YAML configuration, web config, or something like that? I don't know, it could be postponed till later time, but it's important design question.
Yeah, for sure.
**Zach Montoya** 32:24 Yeah, I think… well, yeah, I think we should support this, and then we can make sure that that path, or that… yeah, the path to that file can be defined in WebConfigureAppConfig. That way, it makes it easy to adopt the per-app domain configuration.
**Igor Kiselev** 32:39 Then it was next question. Right now, in YAML, we have a way to substitute environment variables, through NVAR. With updomains, it's still NVAR. So should we expect extend a language, in YAML to, get, app config values, or upconfig oil bar, or something like that.
**Zach Montoya** 33:01 Well, actually, actually, you know… there's… there are some environment variables that are already set by IS, like, there's, like… isn't there, like, a site name or something like that?
**Igor Kiselev** 33:13 No, no, okay, not per up domain.
Because environment variables are the whole thing. So, on Azure, yes, you would have environment variables that give you some information about your application, but they never co-host multiple… So, Azure environment is related.
**Chris Ventura** 33:34 And you can't rely on the environment variables anyways. The IIS always-on mode, Some of those environment variables get dropped between, restarts.
**Zach Montoya** 33:49 I see.
Yeah, I don't…
**Igor Kiselev** 33:52 Once again, it's not… it's not very important for that pull request, but it's about a design, how… how we would like to proceed it in future.
Oh, that would be resolved later.
**Zach Montoya** 34:05 Yeah, I don't… I don't care about this part right now.
**Igor Kiselev** 34:09 Next, it's about, should resource… so, right now, pull requests implemented in the way that resource attributes emerged?
Between, application level and, domain level. So my question is about, should we merge it typical for a source attribute or not? My answer, we probably should not.
do it, and it's better if it would be. It's only… you could write on up domain level, but you could not merge it between up domain and process level.
**Chris Ventura** 34:41 Yeah, I agree with that.
**Zach Montoya** 34:42 Yeah, I agree.
**Igor Kiselev** 34:44 And last question about, can we do it in a minor release, or should it be postponed to a major release? My answer is that Probably, yes, if we would do it accurately and isolated, it would be a minor change, still a bug-level change, and we could do it in a minor release. I give a condition when we could expect it, when we could do it in a minor release.
**Chris Ventura** 35:12 Yeah, everything that we've talked about feels like a minor release.
**Zach Montoya** 35:17 Yeah, yeah, I agree with that.
**Igor Kiselev** 35:20 And in that case, right now, I heard that we mostly agree with my answers. Yeah, it would be really great if you would re-read it after the meeting, and market thumbs up or something like that, it would be in that case, I would say, okay, here is our SIG decision, it's summarized in my answers. If not.
We could come discuss it a little bit more and put a summary after next week meeting.
**Chris Ventura** 35:46 Yeah, I can, put a summary on this.
**Igor Kiselev** 35:51 Losie.
**Chris Ventura** 35:53 Sure. Just… move forward. I think I was the only one that… that had…
**Zach Montoya** 35:58 You're the only one that responded to us.
**Chris Ventura** 36:00 Yeah.
So I'll just write a summary of what we decided in this call. Sure.
**Igor Kiselev** 36:07 Sure, sure. Thank you, great.
**Zach Montoya** 36:09 Great.
Awesome.
Let's see, so we're already halfway, halfway through the meeting slot.
Do you want to… are there any other PRs, though, we should talk about? .
**Igor Kiselev** 36:25 The pull request from, FTCAR is nearly ready.
**Piotr Kiełkowicz** 36:30 I'm sorry.
Continuico.
**Igor Kiselev** 36:33 Yes, the airport request from FTCAR is nearly ready. I'm doing a review for it. There are still some polishing required, but Mostly, it is dub.
This week, it should be in… all ready for review, and it would require somebody else to do concentrate, and Zach, I'm mostly looking at you, because it's mostly about a profile of code.
**Zach Montoya** 36:58 Yeah, I delegated that to, my coworker, Gregory. So, I don't know, FTCAR, if there's any, significant changes since that, since he offered his review, which his review was 3 weeks ago.
**Igor Kiselev** 37:13 Yes, there are. Based on his review, based on my review, there was a pretty substantial change, so, I suggest to wait a little bit until, Aptikar would finish, what I asked him.
And after it, we would need one more review round.
Right, unfortunately.
**Zach Montoya** 37:35 Okay.
**Piotr Kiełkowicz** 37:38 Yeah, kind of.
**Zach Montoya** 37:39 My colleague, yeah.
**Piotr Kiełkowicz** 37:41 Next week.
There were a request also from Rasmus to verify the plugin.
API.
there is a lot of comments from the Igor also, but, I'm not sure if it is time to discuss it today, but kind of… Offline tech, it would be great.
**Zach Montoya** 38:05 That's a more specific.
Plugins API? Okay.
**Piotr Kiełkowicz** 38:10 My understanding is that the plugins API Can bring any braking changes with, like, major bumps, if it is correctly documented.
As we require right now, that's the major… you need to release kind of new… new plugin for the new… new auto-instrumentation version.
But it is up to discussion.
**Zach Montoya** 38:40 Is that… I mean, would the… Specification requires to… to make that a major bump?
Or is that… is our interpretation, like, something that we're discussing.
**Piotr Kiełkowicz** 38:57 Our documentation said that the plugins need to be rebuilt… for each… Auto-instrumentation version.
It is the first one site. The second site, it is against the same comp, especially if you provide some public API.
On the Nugget level, and on the binary level.
So…
**Zach Montoya** 39:27 I see. And that's easy. And, the Nougat package we deliver… is it also provide… it provides that public interface, right? Like, it's not just a… not just a runtime.
I said, it's actually compile time.
**Piotr Kiełkowicz** 39:41 Yes, yes, it's kind of, let's say, hooks, which Can be caught without ugly reflections, or… Yep.
That… it makes contracts a bit harder than… Then they're just reflection, and the nice.
**Igor Kiselev** 39:59 And it also makes practical, us more affected by compatibility issues between different versions, so, depends on how much care and how much additional work we would involve in it. If, despite our, precautions that you probably need to recompile plugin between each version of, hotel.
In practice, there was a lot of partial hotel which, have not required recompile. With, that change.
depends on how much care we would do in future. It may require a real recompile between different versions of, hotels, so… I'm not… I… It's… indefinitely, more static… static contract is a good thing in terms of maintainability, but at the same time.
we should… Think and answer through a question how much backward compatibility we should… we'd like to give for… compiler, API.
And Clara mentions that it is probably experimental features or something like that, that it… It would be changed between different versions or between different minor versions.
And most of my comments are… So there are some comments about a design. As we change API already, we could probably improve a design in some ways, but it's not necessary.
can be done later, but there was some comments about how compatible we will make it in future.
**Zach Montoya** 41:51 Got it.
Okay.
Alright, we can continue.
**Igor Kiselev** 41:57 Nothing in that… nothing in that PR actually prevents us to make it more compatible or less compatible. It's about, our idea about guarantees, how much guarantees we would give in the future.
How much effort we would spend on it in the future.
**Chris Ventura** 42:13 Yeah, because I think in this PR, we're introducing an interface that needs to be implemented, but if we wanted the most compatibility possible between releases. I feel like we can't use an interface and instead We need, We need a different approach that's more similar to duct typing, or something along those lines.
**Igor Kiselev** 42:43 Can use interface, but it means that if we add a new method, we probably need to create a new version… a new interface, and that new interface.
**Chris Ventura** 42:52 Sure.
**Igor Kiselev** 42:52 both old interface and new interface. So, that's why I said.
**Chris Ventura** 42:57 Yeah.
**Igor Kiselev** 42:58 it would, if we're compatible, it would be complicated.
If not, It would be probably a little bit easier for plugin maintainers to… You get it, because despite… oh, there is a difference between you need to… to take care when you… when a new version released, you need to test it, but in a lot of cases, it will be, I tested it, it works, I don't need to do anything else, and the difference between, okay, I tested it, it will not work, I will need to do a new release.
And another thing, it's about how a plugin would be deployed to end customers. It would not be cra… it would not be a problem for every, plugin author that, bundles their plugin with entire hotel distribution and auto-instrumentation distribution. But if you have a plugin that do not bundle and then try to deploy it as a separate.
In that case, it would be, more burden on a… customers of the plugin, and plugin also to clearly state which version of auto-instrumentation supported by that version of Swagging. We already have that problem. It's not that it's something new, but It may make that problem worse, because despite… it was already a problem, in practical things, a lot of plugins worked even before, thanks to DuckTyping.
**Chris Ventura** 44:38 I wonder, in practice, how often the plugin model's used outside of individual vendors.
Because with vendors.
It's most likely that you're bundling it with the auto instrumentation, or your version of the auto instrumentation.
But as an end user.
there's a chance that you might just be creating your own plugin. Maybe, or maybe not, you're using the auto-instrumentation NuGet to build your plugin.
who knows?
**Igor Kiselev** 45:20 I would suggest in that case, to open, to follow our process, and open a bug and make it open for at least a week, trying to get, maybe some login authors would report it. If nobody answers about it, it means that we are All who have information about the plugins are already here, and we probably could decide it, based on our understanding, that most of plugins are bundled with, auto-instrumentation.
But our process in that case… our process is that we first open a bug, second we create a pull request, so I'm just trying to make it Polar approaches Follow a documented process for things that may affect people outside of SIG meeting.
Just to make it a little bit more visible.
**Zach Montoya** 46:23 Sounds good.
Alright, Let's see… is there any other comments on this topic?
Alright, so we've got… 15 more minutes, Fortunately… let's see, for… so we have… those are the pull requests.
We talked about this, for now, we're not gonna be doing that. We'll be supporting the outconfig, web config.
And then discussions, there are none.
So, all we have left is actually the board.
Which I don't think there's… Much to update on here.
I guess we have started on .NET 11 support with some PR, so I'll just, I don't know if all the different tasks are attached to this, but… I'll just put this one in progress, because there's some movement here, but…
**Piotr Kiełkowicz** 47:35 Yep.
**Zach Montoya** 47:36 It'll be longer.
**Igor Kiselev** 47:37 Can we converted…
**Piotr Kiełkowicz** 47:39 It should be long… long-term-ish, it is long-term kind of PR open-et, and it looks good. Now, one issue failing, because I've merged some changes only to domain and not addressed it.
One test stood the… on the .NET 11, but basically it's green, and… yeah, so…
**Igor Kiselev** 48:00 And about, committed settings as planet core hosting assembly, it is… I, put all my research in a ticket. It probably waits for Raj to… give some feedback on it, the final feedback, and we could either close it, or as done, or move it to backlog, or something else, I'm not sure, but… All research already provided.
**Zach Montoya** 48:28 So it's the specific ticket, right, that you wanted Robert's response to? Okay.
**Igor Kiselev** 48:32 Yeah, so it wouldn't be… Good.
Because Raj was the most… Was, the person who… Or, poop.
shared most concerns about it, that's why it requires red… opinion on?
I'll need it.
**Zach Montoya** 48:53 Okay.
Cool, not sure there's anything else to update here.
So, I guess we're good for now on this.
Yeah, and then actually… I guess we're all done for today, unless there's any other topics you guys wanted to discuss?
Cool, well, I guess we're all good, thank you. And Chris, did you say you were gonna take on… you're gonna summarize our discussion on the…
**Chris Ventura** 49:34 I'll summarize it.
**Zach Montoya** 49:35 Okay, perfect. Well, thank you guys.
**Piotr Kiełkowicz** 49:38 Sure, bye.
**Zach Montoya** 49:39 Internet's weak?
