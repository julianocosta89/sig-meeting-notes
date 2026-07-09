SIG: eBPF instrumentation
Date: 2026-07-08
Duration: 64 minutes
============================================================

## Zoom Recording Transcript

**Tyler** 03:03 Hey.
**nimrodavni** 03:06 Hello.
**Evan Bradley** 03:07 Hello.
**Pablo Baeyens** 03:12 Okay.
**Tyler** 03:31 Oh.
Wow. Okay. Yeah. Got a lot of people on it. That's great. So, If folks haven't yet already added their names to the attendees list, please go ahead and do that. If you have agenda items you want to talk about.
Please go ahead and add them there as well. I think we'll try to get started, soon here. I know that there's a lot of collector folks on the call, and we want to talk about this first item. Some of you all have conflicts at, like, a half-hour mark, so… Yeah, we can jump in here in just a second.
Maybe. Okay, there we go. Cool.
Awesome.
Okay.
Yeah, welcome, to the collector folks on the call. Thanks for joining, thanks for taking the time to come over here and talk about some, some of this issue.
Yeah, let's jump in it. So, first off, Alex, maybe do you want to start us off, or do you want me to give an overview? Go ahead.
**Alex Boten** 04:42 I… I put the item in here, but really it's more… I just want to put the placeholder in place. I think there's other folks on the call that have a lot more context than I, but we were discussing the… this particular issue at a collector stability call on Monday, and the discussion was… us getting to the point where we were asking ourselves a lot of questions that hopefully you have the answers to, or you folks in this SIG have spent some time thinking about.
And then I just suggested that maybe we should just bring the two sicks together so we can have a productive conversation. So, I… I will allow the other people that are more familiar with this issue to speak. Maybe Pablo, Braden, I know you both have spent some time on it.
**Pablo Baeyens** 05:30 Oh, no.
I mean, I guess… The main thing we talked on Monday that maybe it's good to discuss here is explore a bit more the hook option.
The thing Brayden and Nimrod talk about at the very start.
I… I guess one thing that we were… So, like, yeah, okay, let me step back a bit. So the hook option would be some sort of mechanism in OCBE to allow some sort of code to be run for particular components so that, well, you could… Maybe download the object files from somewhere else. And, That could be an option, to… support use cases like the one from OBI, as I understand it. There was some concerns about… overhead or custom code execution, and I think it would be good to… maybe we can start with understanding those from the OBIC.
**Tyler** 06:42 Sure. Nimrod, did you want to talk a little about it or do you want me to jump in.
**nimrodavni** 06:46 I can start then. Yes, I think regarding custom hooks.
I think it's kind of similar to what, Tyler, you did that was just merged, basically. We had some sort of, like, back script that ran before.
the OBI, like, before the collector builds, and basically what it does is just download the source and unpacks it, and adds the, like, replace statement. Or I think you just… the replace statement is hard-coded there.
So I think that can be an option. It still, like, requires the replace statement, because it expects, like, a local source. You can also have it as, like, a… real custom pre-built step, but for that, you need to actually run the build, and that requires either, Docker, or the, like… or if you don't want to, like, run it with Docker, you need some sort of, I think it's, like, Clang and other dependencies, but probably Docker is more simple. I don't think you need privileged… Like, anything, like, pseudo or something, just to build the, the bindings?
So maybe, like, a dependency on Docker during build is enough. And custom code execution, I think, is… just a concern, because you do, like, you need to specify a custom way to, like, basically do whatever, and people need to trust it.
I don't know exactly what more to say regarding that. If that's something that's acceptable, we can, like, or maybe try to limit it somehow.
**Pablo Baeyens** 08:19 I mean, I guess on that last bit, people using, collector components… I already have to trust that component to not run any code that they don't like. So I mean, this is at compile time instead of at runtime, but it's still — There's a high level of trust placed on whatever you put on the configuration.
So that's why I personally feel it's less concerning.
**Tyler** 08:50 So there's also like the source.
It can be downloaded without a build needed as well, though, right?
Like, we actually already have builds that you can download that have everything there.
**nimrodavni** 09:03 Yeah, so it's not even, it is a pre-built like hook, but you don't run any custom build, you just download the source and unpack it.
**Braydon Kains (Google)** 09:14 Yeah, I.
**Tyler** 09:15 Right.
**Braydon Kains (Google)** 09:15 That's the reason I like the… The build hook option more than the source archive one, just because like, both of those become options. Like, if the pre-build hook is mostly just a hook to run something generic, that could be curling from GitHub releases and verifying the signature. That could be if they have the means compiling the eBPF artifacts themselves as part of it.
It opens up more options, but it also means that the sort of security and the concept of downloading, like, a Go source archive is… moved off of being an OCB concern and moved into whoever's developing the hook.
And then I think the big question with hooks is whether we can find a nice sort of user experience for, like, distributing common hooks. I think there was an idea thrown around that those hooks could be written in Go, so that they could be referenced as a Go module and run as part of OCB somehow. I still don't know exactly how that mechanism would look, but it would mean that someone could, in a GitHub repository.
develop a hook as a Go module that can be pulled in, and the OBSIG could create a… a pre-build hook for OCB written in Go that would do either the downloading from GitHub and doing the proper verifying of the signature, or a custom compilation version if… and say, like, you can use this version if you have Docker or Clang or whatever things you need available, or you can do this version that downloads our pre-compiled artifact based on your input.
Again, this is all still kind of nascent in my brain. I'm trying to come up with a way to do this that is still a good enough user experience, so that I can still feel to an external user, like.
I have real… I have nice, approved OB integration with OCB.
but it still sort of extricates that idea of, like, downloading raw tarballs from being, like, a core OCB concept into something separate that OCB can run.
**Jade Guiton** 11:23 Yeah, I think in terms of trust, using Go modules for the pre-build hooks would kind of help, because it would be under the same namespace as the components that you're trying to import as well.
and… and as to what that could look like. Practically, it could just be the equivalent of a go run command. Essentially.
**Braydon Kains (Google)** 11:42 Yeah, I think that would be the only real way to do it, probably, so…
**Jade Guiton** 11:47 Yeah, there's definitely a lot of work in specifying the interface between OCB on the hook, but… Yeah.
We can start with something simple that can be extended.
**Tyler** 11:59 Is the hook just, like, a shell out to, like, call an external program?
**Jade Guiton** 12:04 Yes, I think that would be the idea.
**Tyler** 12:08 Okay.
**Evan Bradley** 12:11 We could make it, like, a component, too. I mean, our components are essentially Go modules that then get, you know, thrown into a, what do you call it, like a collector binary, so we could do something similar with OCB.
**Tyler** 12:23 Yeah, the only… that was what I thought you guys were talking about, but that… Seems really hard, given… because then you're going to need to do dynamic loading if you wanted to do something, like, where it comes from a configuration, unless you wanted to just build in all the hooks from the start.
**Jade Guiton** 12:38 Yeah, I think.
**Evan Bradley** 12:39 We… go on.
**Jade Guiton** 12:41 Yeah, I agree that trying to load things dynamically would be very difficult in in go. I think it's best to keep it as a separate binary, although that has its own complexities.
But, like, yeah, the way I conceptualize it is that the current kind of canonical way of doing custom things is just to wrap OCB with a bash script, so this would essentially bundle everything before Cb. In the bash script into its own and some binary.
But yeah, there's the there's still the concern of like, how do you pass information to the to the hook?
At least we can hash out the technical details.
of how exactly it's implemented later. What I'm mostly wondering is, like, is this an acceptable option for everyone?
**Tyler** 13:36 I mean, I'm interested in exploring that, yeah. Like, I'd be interested in seeing that. I think it sounds very similar to other things we've tried, so yeah. I mean, if you guys are open to it.
**Braydon Kains (Google)** 13:49 I can try and come up with a proof of concept, because, like… even outside of the OB integration with OCP, I can already kind of think of some other ways that I would use the pre-built hooks just for totally unrelated stuff, so… I'm… I'm open to to trying to proof of concept and see if we can.
Get that working, if that will work for you guys, too.
**Tyler** 14:12 Yeah, I mean, like, at the end of the day, what we really want to do is just provide, like, end users and, like, companies ways that they can just take, like… here's, like… here's a simple way to, like, just build OB into the collector, and, like… not have them go through each manual step. So, like, what you're describing seems like that should work, right? So, like, yeah, that sounds great.
**Braydon Kains (Google)** 14:33 Yeah, that… ideally for me, it would still somehow come out to, like, this is what you have to put in your OCB config, and you will get OB… an OB collector at the end of the day. That's… That's the way I want, like, when I'm trying to think of exactly how that would work, that's what I want in the end.
**Tyler** 14:53 Yeah, I mean, I think we got the.
**nimrodavni** 14:55 I just think, like, maybe it was in my head, like, the pre-build hook I don't know if it's, like… I don't think it should be on a component level, because theoretically, let's say we want to import OB as a receiver.
Yeah, we do need, like, a reference to it to, like, you know, get the actual name, but it doesn't actually, it should not just, like, do the actual Go mod download and then another step, you should also be able to just skip the Go download entirely and, like, override it like we do with a replace kind of thing.
Right.
**Braydon Kains (Google)** 15:33 But.
the way I'm conceptualizing it is that the pre-build hook is something that runs, like.
as a step in OCB before anything else occurs, so… whatever, An OB developed hook would be to set up the source, either by downloading the pre-built ones or maybe building one yourself, depending on what the user wants to do, would set that up in such a way that once the rest of the OCB generate and stuff runs, everything is already there for it.
I still need to detangle this a little bit, but it wouldn't be on a per-component level. I think the pre-build hook would be, like, this is a setup step that occurs before any other OCB steps occur.
And maybe there could be a pre and post, if that ends up making sense.
**nimrodavni** 16:22 Mmhm Yeah, and maybe, I don't know if the ability to add this like of a replace statement is the responsibility of the hook or the user. Because like if you download it from source, you need to like add this replace.
**Braydon Kains (Google)** 16:41 Yeah, yeah, yeah.
**nimrodavni** 16:42 I don't know if it's like something we need to document of like, if you download this way, you add the replace or is OCB like doing this magically in the background?
**Tyler** 16:50 I see it as, like, that's a part of the plugin, right? So, like, if you have the plugin that does, like, the download, like, as Brandon was saying, like, it'd be in your config already, that you're saying, like, use this plugin, the download plugin, then you would also need your config to also say, like, use the replace statement in the config, right? But, like, if we have, like, another plugin that's, like, just build locally.
**nimrodavni** 17:09 No.
**Tyler** 17:10 you probably still need a replace statement, but, like, I think that, like, it's just self-contained in the config, right? As to, like, what that would be, is how I'm hearing this.
**Braydon Kains (Google)** 17:19 Yeah, the the the thought process I have is.
Potentially… We could introduce a standard, like.
artifacts directory that OCB can recognize, and plugins can well, plugins, external wiring, whatever, you know what I mean. They can interact with, like, the artifacts directory and put stuff there, and then the replacements can… Know how to, like, read stuff from the artifacts directory.
It's not a super well-cooked plant, that's kind of what… but That's something I'm thinking about.
**Jade Guiton** 17:58 Yeah, as long… there could just be, like, a… kind of hard coded path for that specific pre-built script.
And then you just add the.
corresponding replace statement.
That could be enough.
**Tyler** 18:12 So we're running up on our time box here, as Alex pointed out, and I do want to be respectful of people's time if they do have to jump off. So I just want to kind of summarize, like, this sounds like a good thing. We just need a proof of concept is kind of the thing.
Braden, you've taken the action item to work on that. Is there anything else you need to get unblocked? And then, obviously, we're happy to review.
**Braydon Kains (Google)** 18:36 I think… If I need anything, I'll probably DM Nimrod about it, if that makes sense. Otherwise, I think I… I think I have what I need to get started on it, and I should be able to late this week.
**Tyler** 18:49 Perfect. Awesome.
**Braydon Kains (Google)** 18:52 Well, cool. Thank you for already. So thanks, everybody. Awesome. Appreciate it.
**Pablo Baeyens** 18:56 Yep. Thank you.
**Tyler** 18:59 Awesome.
Okay.
Jump back to the agenda here.
Nimrod, I think you're up next as well. Last week you had talked about doing a nightly release, process, and, you got a proposal together here. Let's, jump in.
**nimrodavni** 19:19 Yeah, I think I even have, like, a draft implementation of it, but I basically want to take something similar to the Collector, doing a release.
let's say every day, just because I think we are, like, a lot of features we're releasing and doing, pulling from main is kind of a bad practice with, mutable tags and all that stuff.
So I wanted to have, like an immutable, nightly release, let's say every night, and then also kind of a stay, like a stable tag that is mutable for nightly, which is.
It's kind of a worse version of our main, but, you know, maybe it, like, had one day to cook, or I don't know. We don't even, like, the mutable one, not super critical in that case.
Yeah, I just wanted to hear what are your thoughts, just add it as a CI pipeline, it's… I have a POC for it, I don't think it's super complex, just want to hear your thoughts and… If you like this idea.
**Tyler** 20:23 Yeah, this is great. I might recommend.
This, it's kind of a smaller detail, but just, like, the naming on this?
I might… Recommend not having the version here?
**nimrodavni** 20:42 No, I have.
**Tyler** 20:43 Yeah, so, like, so, I don't know, I've got, like, so this… sounds… the problem I'm seeing here is that somebody's gonna think this is, like, some kind of Semver, which it is meant to represent, right? But it's not supposed to represent that, like, this is, like, a new, like, version with, like, a dash, which would be literally a build, flag for Semver, right? So we want to make sure, like, it's not confused.
Yeah.
It also isn't… 010, right? It's something else?
**nimrodavni** 21:13 Maybe the, like the, the current version, maybe it's the, like, if, and if, when we update to like the 11, then it'll be 11 nightly commit.
**Tyler** 21:25 Yeah, I… Nikola Grcevski @ Grafana / OpenTelemetry 21:25 The current version or the next version?
**Mario Macias** 21:27 Yeah, should be the next, right?
**nimrodavni** 21:29 Oh, yeah, you're probably should.
Yeah, but I don't know what… what…
**Tyler** 21:34 Yeah, that'.
**nimrodavni** 21:35 What's the next one? Because we can go to, like, 1.0, or, like, you could say just the next minor, but I don't know if that's correct.
**Tyler** 21:44 Yeah. Okay.
**Mario Macias** 21:45 Maybe, maybe replacing it by a day or something like that.
**Nikola Grcevski @ Grafana / OpenTelemetry** 21:49 Yep.
**Tyler** 21:49 I think the date makes a lot of sense to me, yeah.
Same thing.
**nimrodavni** 21:53 Date, Nightly, Lakash, and…
**Tyler** 21:57 Yeah, and also, I do wonder if you want to do, nightly then date is my other thing, just for it being easier for folks to find it, instead of having to I think sorting and searching from tags, it'd be easier if they were all grouped nicely.
Bundle? Yeah. But I don't know if that's super critical.
**nimrodavni** 22:20 So maybe we don't even need… Like, should we, do we even need the commit if we do like neither?
**Nikola Grcevski @ Grafana / OpenTelemetry** 22:26 Yeah.
**nimrodavni** 22:27 Date?
**Nikola Grcevski @ Grafana / OpenTelemetry** 22:28 No, just a day.
**nimrodavni** 22:29 So nightly dot date and that's all.
**Nikola Grcevski @ Grafana / OpenTelemetry** 22:31 Yeah. And then. Yeah.
**nimrodavni** 22:33 Okay.
**Tyler** 22:35 I do wonder, though, also, like, if this all works out, and, like, this keeps working, like, it might be nice to add, also, just, like, builds for every commit, But I think we probably want to look at the size of what we're actually producing and seeing, like, if we're hitting any limits, but I think this is a great way to start. It's just.
**nimrodavni** 22:53 Oh, you mean, like, yeah, like, I think we're… it's kinda… I don't know how main does it, because we do build on every commit, but I don't know… like, main just points to a new commit, but maybe… I don't know how it works with, like, history. Are those builds getting deleted once, like, main doesn't point to them?
**Nikola Grcevski @ Grafana / OpenTelemetry** 23:14 Yeah, I think so.
**nimrodavni** 23:16 So maybe you can already just tag it with the…
**Tyler** 23:20 Yeah. Okay.
**nimrodavni** 23:21 And I don't know.
**Tyler** 23:23 Yeah, I mean, that's actually a good point. Like, we could do that. Like, there's nothing… it already is there, right? The only thing is it isn't tied back to the commit that produced it. So.
**nimrodavni** 23:32 I think if we do that, then, like, the nightly just makes it a bit more stable, but we don't really even have to have the nightly if we have, like.
Just commit…
**Tyler** 23:43 Submit hashes.
**nimrodavni** 23:44 Yeah, it might be easier to find, like, dates, just to know, like, chronological order, but you can… I guess. Also get that when you're pulling all images. I don't know.
**Nikola Grcevski @ Grafana / OpenTelemetry** 23:56 I mean, to an end user, it's easier to explain the date business, right? Then you want to provide a fix, you want to say, okay, see if this worked for you, and then you can say, use this nightly build.
Without worrying, if down in Maine, maybe something else breaks in Maine, you know.
It shouldn't, but… Main would have other commits other than the fix that we're looking for. So.
**nimrodavni** 24:17 I think it's easier just to tell them, yeah, like, it's more nice to tell them, okay, this is the nightly from this date, then just take this random commit hash, which is… like, it's the main now, but, you know, it could be… Yep.
So I think it's still negative.
Thank you.
**Tyler** 24:36 So the only thing is that, like, Nightly's amorphous, though?
So if you give somebody a commit hash and you say, like, here, try this fix, right, that's never gonna change.
As well.
**Nikola Grcevski @ Grafana / OpenTelemetry** 24:47 Yeah, no.
**Tyler** 24:48 The nightly, like, obviously, I'm saying you're probably suggesting to give them the nightly with the date. That is, I think, similarly stable, but there's also not really, like.
There's somewhat of a false sense of guarantee that, like, that's actually going to be a, like, a workable build.
**Nikola Grcevski @ Grafana / OpenTelemetry** 25:05 Yes.
**Tyler** 25:06 There's nothing really guaranteeing that, like, we… at the end of the day, like, we haven't broken something, and, like, we're checking that before the nightly gets kicked off I guess it's kind of, like, my only concern.
I'm not, like, serious concerned, like, it just seems like it could also just be an additional tag, which people may be interested in.
But I… yeah, it's… Just a, you know, the short commit also could be what we, what we could do as well and like.
I don't I'm not opposed to either, or both.
**Nikola Grcevski @ Grafana / OpenTelemetry** 25:39 Yeah, it works, to be honest. Minor thing. Yeah.
**Tyler** 25:43 Agreed, minor, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 25:44 Yeah, that is just easier to kind of tell without looking at Github history when this was done.
Kind of speaks for itself, but…
**Tyler** 25:53 Yeah, that's true.
And it's telling somebody, go look at, you know, nightly, because it was put out yesterday. You don't have to go, like, what commit was that?
**Nikola Grcevski @ Grafana / OpenTelemetry** 26:01 Right.
**Tyler** 26:01 just to communicate that. So, I mean, I can see that.
**Nikola Grcevski @ Grafana / OpenTelemetry** 26:05 Yeah, and if somebody is actually reporting a bug and they show you the version they're using, you can say, oh, that's like from two months ago.
Right, right. There's something, right?
Yeah, I don't We are efficient commit, but It's a minor.
**Tyler** 26:20 Yeah, okay.
That sounds good.
**nimrodavni** 26:25 Okay, I'll I'll open a stable. Pr, for this.
**Tyler** 26:30 Yeah, is the PR gonna add the short commits to the ones we do on main or is that just a separate PR?
**nimrodavni** 26:38 I can… I… you mean, like, you wanna tag… You also want to have, like, not an ILEAP, but, another tag for…
**Tyler** 26:46 Yeah, so the ones that we're doing right now for every main commit, just have it also commit the SHA as the tag.
**nimrodavni** 26:53 I'll do it in the same bill. Okay.
**Tyler** 26:56 Yep.
Alright, cool. Yeah, I think that's… I think those are great options.
**nimrodavni** 27:00 Write that down.
**Tyler** 27:03 Okay.
Awesome.
Cool.
Okay, jumping back in, there's a bunch of stuff to get resolved, that I've just been wading through, First up, I wanted to talk about, this issue… yeah, 2211. This is an issue that was opened recently with tighter integration to the declarative config.
Right now, like, our V2 configuration, we have it in our extension.
obi, which is not a standardized place for things. So the… This issue was opened with some sort of, like, ability to try to move… To use more standardized forms of declarative config, And there's a lot of, like.
context here, so if I'm just kind of glossing over something that doesn't make any sense, let me know. But it's mostly just that, like, The declarative configuration, especially in the instrumentation side, there's a thing called the instrumentation forward slash development, because it's actually not stable yet, and it's You know, been asked whether we should have our… Oh, we use that for instrumentation. It doesn't work. It's kind of a catch-all. It has instrumentation for different languages that are literally, like, runtime libraries. It has instrumentation, like, general semantic convention, like, catch-alls.
Let me see, I can't remember the name of the repo. Oh yeah, it was just configure, I think.
Okay.
Maybe this is good enough. Yeah.
No, not good enough.
We used to have a kitchen sink.
I don't know where that went.
Okay.
Sorry.
It's not even in the standard configuration because it's not a stable thing. So the ask here is whether we want to integrate closer to the instrumentation and then split across that and this other thing called distribution, which we are using for like a host definition of distribution. So like other vendors can put their configuration there.
I don't think that's the way we want to go. After doing some research.
I don't think that that's usable. For one, we want, like, a single source of truth for OB. Obviously, like, we have it split a little bit, because we take the tracer provider configuration, we take the meter provider configuration, other things as well, from the top-level declarative configuration.
But, splitting across this instrumentation development, and instrumentation, like, or in this distribution, means that, like, our… for instance, HTTP instrumentation would then be split across this, so if we tried to go back to using it in the collector, where we wanted to have, like, this whole capture Split, where that's the portion that's actually gonna be used for… to register the collector.
Like, that's, not going to be achievable, like, because that would then be split across these two different places. And I think it, like, also saying that, like, we want to just move, like, extension.obi into the, distribution and, like, not do the split.
Still, again, like, it's discussed in other semantic convention, or, declarative configuration, Issues around this, around asking… like, for the distribution to change its name, because it is not really reflective of, like, what OB is. OB is not only, like.
runtime, configuration and, like, host, gathering things, but it's, like, the actual definition of instrumentation, so it wouldn't quite fit there as well. This is something that the .NET Auto Instrumentation and, like, the Java Auto Instrumentation also have, like, concerns about, around where they're gonna leave these things.
So my recommendation is to not go and split this up. I don't know… if ultimately that's the direction we want to go, but I would… I'm asking if we wanted to keep it the way that it is. I haven't seen this comment, unfortunately.
But yeah, there's… there's, I think, kind of question around, like, where we want to go here, and do we actually want to make this, split? And I'm… I guess I'm asking the rest of the SIG if… if they're okay with Maybe coming back… at a future time when declarative configuration has this nailed down a little bit better, and then we could maybe do another, like, draft on this, but, like, right now, like, I don't think that that's the place that we're at.
**Nikola Grcevski @ Grafana / OpenTelemetry** 31:38 Yeah, I think we'll just keep it.
**Tyler** 31:40 Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 31:41 5.
I mean, it seems like… We want to get to declarative config, and maybe we can use us as an example for them to kind of figure out what should be the final form, and explain the problems they're encountering with splitting, and how a customer is going to Touch two separate sections to do this there.
**Tyler** 32:01 Yeah, absolutely. Like.
And I've definitely put a little bit of thought into this, like, there's, yeah, there's definitely this issue that I've been talking in as well, like.
Technology specific, things for the distribution, like, this is very, like… hard to understand. Like, I would love it if, like, we could go into the interpretation, like, that sounds great, but, like, there's just canonical limitations, I think, on what's going on here right now. And then, like, one of the main things is that, like, that split that we have with the collector And how we want to try to, like, section things off there. Like, you can't put instrumentation in this, like, general instrumentation development thing here, because this part never goes to the collector. Like, if we're going to use, like, HTTP instrumentation from there, like, that never gets to the collector.
I opened an issue with the collector asking about, like, guidance there as well, around, like, hey, like, it'd be really cool if we could get the full declarative configuration there.
Yeah.
This is… I… I've responded to this author as before, like, the configuration provider doesn't actually provide the full configuration at this point, so that's… that's not really a viable option. so, like, yeah, like, there's definitely some thought around this, but yeah, it's definitely, I think, at a point where, like.
we're not gonna solve that in the next 6 months, for sure. And, like, I think, to your point, Nicola, like, using this as a, forcing Declarative config might actually be the best approach to try to see if we can't get something working there.
But I think for now, let's just stick with what we got.
**Nikola Grcevski @ Grafana / OpenTelemetry** 33:34 Yeah, that's my take. And I don't know what other maintainers or people in the same thing.
**nimrodavni** 33:41 Yeah, I agree. I think we Should probably keep it, keep it.
Yes.
**Mario Macias** 33:48 Yeah. Agree. Yeah.
**Tyler** 33:51 Perfect.
Okay, I will, put a note on that in this, issue. I'll probably close this, and then we can have some sort of other tracking issues, going forward. But just want to signify that, like, that's the direction we're taking.
Yep.
Cool. Then, next up is also a declarative config subset, so this is an older one, this is… this predates the, the V2 configuration. Nicola, you'd open this, just, I think, generally asking, say, that we should use the declarative configuration.
I think it's a great, yeah, I mean, obviously, I think it's great because we decided to use it. the question is, I think, like, is how much, is the use? So, I've been going through some of these things. So, obviously, like, I put this out last time, but I went through a little bit further, The file format right now, like, we don't actually do any restrictions on that. I think that's just a follow-up issue, we should probably do that. One of the things that.
part on this was that, like, we don't actually use the full resource declaration here, but maybe we should. I don't know if it's needed for a V1. I do want to point out that, like, we could always add things afterwards, but, like, maybe it is. Like, I think that, like, one of the… Yeah, global resource definitions was one of, like, the main things that, like, you had pointed out here. I think that, like, that's… it's actually pretty helpful to get that. Like, if a user… like, right now, like, I don't know how much more a user can help configure Obi, Obi's a little bit special, because defining a resource at, like, a top level is kind of, Yeah, it's, you know, we're instrumenting so many different services to have, like, a single resource for that, like, it's an interesting one, but maybe we can take a look closer, as well.
**Nikola Grcevski @ Grafana / OpenTelemetry** 35:32 Yeah, I actually had a thought on that, that something came up recently. So we had a customer ask for resource per definition criteria instead.
**Tyler** 35:42 Mmm.
**Nikola Grcevski @ Grafana / OpenTelemetry** 35:43 so instead of defining global resources that you can kind of pass, as as attributes of telemetry, but to be based on the definition criteria that match that service. So people can segregate, for example.
I don't know, within their company, they have their monitoring services from different departments, And then… Based on… the… I don't know, matching criteria means this namespace, they want to add additional labels specific to that.
Without touching their deployment. So…
**Tyler** 36:17 Yeah, sure.
**Nikola Grcevski @ Grafana / OpenTelemetry** 36:18 I don't know. Maybe that's.
**Tyler** 36:21 Yeah, normally I would say.
**Nikola Grcevski @ Grafana / OpenTelemetry** 36:22 Yeah.
**Tyler** 36:23 Normally, I'd say, like, that doesn't make any sense if you're doing traditional observation, but since we're spanning across all those, like, different zones, like, that seems to make sense to me as well, right? Like.
**Nikola Grcevski @ Grafana / OpenTelemetry** 36:33 Yeah, because in normal instrumentation, it's, yeah, passing the environment variables to the process, and… Yeah, yeah. …because the thing is embedded, but… oftentimes they don't want to mess with environment variables or whatever. And And I just wanted this external configuration that drives the instrumentation to say what should be.
Yeah, I mean…
**Tyler** 36:54 Yep.
So, I think that… Yeah, that's that's that's a great question.
It actually makes it harder. So I was gonna say, like, we could just start… Using this… this here.
**Nikola Grcevski @ Grafana / OpenTelemetry** 37:06 You know, yeah.
**Tyler** 37:07 But I do think that, like, maybe there's, like, another part of the configuration that is, like, a per… Service, like, resource filtering of some sort, or, like, annotation, like, yeah, it's a… Nikola Grcevski @ Grafana / OpenTelemetry 37:20 You know.
**Tyler** 37:21 Maybe adds things or removes things. Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 37:24 Or overrides, yeah, the default, global.
**Tyler** 37:26 Right, right. Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 37:29 I think it should be global. Maybe you're on a cluster, and you're deploying here, and you're saying resource attribute development, and you have another cluster, and that's the production cluster, resource attribute protection, but then Namespaces within those.
Could have their, based on the selection criteria, additional resource attributes.
Yeah, depends on how much people want to mess with OB config, right?
Some don't touch it just to deploy it. Some actually care deeply about fine tuning things.
**Tyler** 38:04 What you described, though, like, I definitely could see as being a cost center, issue for a lot of people. Like, they want to, like, allocate certain.
**Nikola Grcevski @ Grafana / OpenTelemetry** 38:11 Sure.
**Tyler** 38:12 Services and all these kinds of… yeah, like, and that becomes really helpful if you can do that… this with, like, a resource here.
**Yeah. And so, like, yeah, for those kinds of folks, I imagine this would be very helpful, but… Nikola Grcevski @ Grafana / OpenTelemetry** 38:25 Yeah, cost center, exactly, the one that was mentioned, you're right.
**Tyler** 38:29 So… To getting into, like, concrete steps, maybe… like, do we want to include resource support in the V1, and then if we do, do we want to also include, like, this override system into the V1 as well?
**Nikola Grcevski @ Grafana / OpenTelemetry** 38:44 That would be great. I don't know if we have time.
Maybe we focus on getting this done.
And maybe drop some of the other issues we had planned, or… of work and that goes post week one.
Yeah.
**Tyler** 39:00 Yeah, because my question is, is like… yeah, I would think I'd rather get the stable V1 than add these features. Like, even add resource support, like, add global resource support from here. Seems like something we could do after a 1.0.
I just would want to make sure that we can do that after 1.0, like, we're not putting ourselves in a corner, but, like, after implementing it with having a host name and a host ID already supported, like, I don't see why we couldn't add this on later.
**Nikola Grcevski @ Grafana / OpenTelemetry** 39:27 No.
**Tyler** 39:29 Umm.
Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 39:30 Let's try, let's say, let's aim for it and see. I can put it on my list as well to help out with it Selection criteria, maybe.
**Tyler** 39:38 Okay.
Alright, yeah, alright, that sounds good then Okay, moving on then, the tracer provider, I think right now, like, we support, always-on, always-off tracer ID ratio, and then, like, simple parent-based routes. There is, like, more samplers, obviously, that can be included here, and, like, the parent base is a little bit more complex, but, like.
again, I kind of see this as, like, fine. This is what we already support in Obi. Going to the V2, technically, we could support more, but, like.
Yeah, I think it just seems reasonable just to leave it the way it is, and they'll be expanded in the future.
**Nikola Grcevski @ Grafana / OpenTelemetry** 40:16 Yeah, yeah.
**Tyler** 40:18 Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 40:19 Oh, man.
Yeah, we can add more always. Yeah.
**Tyler** 40:23 Yeah, yeah.
Yeah, I mean, we have a little bit of a complication, because it has to go… get plumbed in, but, like, yeah, I think it just seems… it's not like an interface abstraction, where it's really easy to just, like.
Okay, then I'll leave this as, like, a… Leave it in the current state.
**Nikola Grcevski @ Grafana / OpenTelemetry** 40:40 Mmh.
**Tyler** 40:41 These are the other two that I think are kind of like top of mind for me. So the partial, so right now, like for our trace provider and our meter provider, we support like one export path only on this. And The declarative config, you can put whatever, very complex export paths here. Simple processors, you can put periodic readers, you can put poll readers for the meter providers.
Obviously, there's a whole host of other exporters that you can support here as well.
Yeah, I mean, I think I would love it, similar to the resource thing, is if we could support the full, like, ecosystem here. But again, this is one of those things where I'm like, maybe we put a pin in it, and just hold off until we get, like, the… The V1 out.
and our V2 config out, and then, like, come back to this. I think this is… this seems something like… It seems great, I would love to see it, I don't know how Functionally useful it is, because… Most people are just gonna be sending this to a collector, and then doing whatever fan-out you want there. Yeah, so having fan-out at the OB side, like.
Be a nice feature, but it's not, like… it doesn't seem to me to be absolutely critical.
**Nikola Grcevski @ Grafana / OpenTelemetry** 41:55 Is this mostly for people that want to export, say, traces, but also print them on console or something for debugging purposes, that kind of stuff, or…
**Tyler** 42:04 Yeah, yeah, yeah, exactly. So that's a very common use case. Another one is like a long-term storage versus a short-term storage situation.
**Nikola Grcevski @ Grafana / OpenTelemetry** 42:14 Sorry.
**Tyler** 42:14 So if you have, like, cardinality issues, you can filter what you're sending to, like, a metric backend to, you know, do a retention of a week versus, like, you know, six months or something like that.
**Nikola Grcevski @ Grafana / OpenTelemetry** 42:26 Yes.
**Tyler** 42:26 So those are the, those are like the main.
reasons I've seen to have multiple exporters, But it is definitely not, like, from coming from the Go SDK, like, it is not common to find a lot of people using multiple. And if they are, they're likely already sending it to a collector anyways.
**Nikola Grcevski @ Grafana / OpenTelemetry** 42:44 Okay, yeah.
Okay, I mean… I'm Let's do it in the future, I guess, if it's not commonly used And.
**Tyler** 42:53 Yeah, I mean, there's very rarely you have, I guess the other one is migrations, so if someone's migrating from, like, one vendor or one backend system to another, they'll usually double print, but, like.
Again, like, just the normal situation is just, yeah. Okay.
Propagators, I don't… I don't think that's… that's a very… no, yeah, I'm just gonna say we're gonna ignore that continually. The attribute limits would be cool to support, but again, like, I think I don't think that's needed for a V1. It's definitely something that would be interesting.
Let's activate.
**Nikola Grcevski @ Grafana / OpenTelemetry** 43:28 limit. Sorry, I keep asking.
**Tyler** 43:30 So, yeah, no, that's great. The, the value length limits, the, the number of, elements that you can put in, like, an attribute slice type or a map type, the total number of attributes that can be on a metric, data point as well to help, keep carnality down. These are all, yeah, attribute limits, yeah.
it's… it's really helpful for controls for, like, runaway systems that, like, maybe you didn't intend, a particular thing. It helps a lot more, I think, in SDKs, because, To go back in and change your like instrumentation to not produce high cardinality metrics or reduce attribute size like requires.
**Nikola Grcevski @ Grafana / OpenTelemetry** 44:12 I can'.
**Tyler** 44:12 compiling. Here, it's like, well, you could just dynamically restart OB or send in another config to, like, not produce that. So, yeah. So I think it's helpful, but it's not, like, I think as critical for us, yeah.
The disable function, this is essentially, like, a top-level, like, enabled or disabled, for the entirety of OB.
I never thought this was a great configuration, but, like, Java agents love this thing. I don't know why. But anyways, I don't… we currently ignore it. I would say we continue ignoring it until somebody actually wants it.
You just turn off the thing instead of anyways. Yeah. Anyway, enough said.
**Nikola Grcevski @ Grafana / OpenTelemetry** 44:54 Okay.
**Tyler** 44:55 Oh.
Distribution, we talked about this one, can ignore it, there's nothing there that we actually use. Instrumentation development, again, deliberately ignore. I think it'd be cool maybe to eventually start looking at this.
**Log level is parsed, but we… yeah, this is actually an interesting question. We currently still have our log level under the OB daemon. This one… Nikola Grcevski @ Grafana / OpenTelemetry** 45:14 I'm happy to.
**Tyler** 45:15 Yeah, that's my… maybe… do we wanna… do we wanna switch to using the log level at the top? This was a new addition as well.
**Nikola Grcevski @ Grafana / OpenTelemetry** 45:21 Okay, yeah.
**Tyler** 45:21 designing it, so… Nikola Grcevski @ Grafana / OpenTelemetry 45:23 But then, do we need to have a special logger provider?
**Tyler** 45:28 The logger provider, no. So this is… this is similar to the tracer provider and meter provider.
**Nikola Grcevski @ Grafana / OpenTelemetry** 45:32 Unless we want to start…
**Tyler** 45:34 Because we don't actually ship logs, we will annotate with traces, or trace context, right? So, until we start shipping logs, then no, like, I don't think we need to do anything here.
**Nikola Grcevski @ Grafana / OpenTelemetry** 45:45 tomorrow.
**Tyler** 45:46 But yeah.
The other thing was environment variable support, so the… I didn't capture it here, but, the declarative configuration, technically, you can override that with environment variables.
Otelconfx does support this, I just want to make sure that we're actually supporting it. I can't… I don't remember if we're parsing the top-level document with OTelConfX, or if we're just doing partials on this. I know we're… I know we'd support it in things like the tracer provider, because we're actually p But essentially what I'm saying is, like, if you, if you wanted to use, like, again, OTel environment variables right now, you can set, like, OTLP endpoint, right? And you can set that to a particular value.
when somebody migrates to the declarative configuration, we always wanted some sort of path forward with them, and so the way we've done that is that in the configuration, you can say, like, hey, for this specific thing, say, like, the OTLP endpoint, use this environment variable, which can be, like So, yeah, we could… try to make sure we support that, but again, like, that's not, I think, a top priority for us, given, like.
We're already a configuration first, like, system, so saying, like, we support the environment variables. We do in some environments, but, like, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 46:59 Not all, yeah. Yeah, okay.
That makes sense.
**Tyler** 47:02 Okay, so yeah, I think that that gives me a clear understanding of how we want to move forward on this one.
Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 47:10 Nice.
**Tyler** 47:11 Yeah, awesome. All right.
that looks great. There's definitely more to talk about, but I didn't want to overload this issue, or… we definitely don't have enough time for all the other ones, so, Cool. Alright, well, moving on, Nimrod, do you want to talk about testing conventions.
**nimrodavni** 47:27 Yes, it was some discussion I had with Mark.
On, I wanna add, It's not on the OATS test, but it was on, aerospike instrumentation, and I added integration tests, and I did not add, OATS And, like, we discussed, what is, like, the correct way, like, what should we do? Should we do integration tests? Should we do auth tests? Should we do… Like a separate, like, integration thing entirely. Like, I try to do some exploring.
Because on the one hand, I like the, like, declarative nature of OATS tests, that you basically declare what you expect, like, what, what's, what to call, and then what to expect. Like, the one thing I don't super like is that it's really, tied to the, LGTM stack in, in opposed to, like, OTel stack.
So I tried… maybe we can, I think I did some POC of, like, implementing… kind of like a declarative YAML, but instead, with, like, TracesQL, MetricsQL, you use one collector, and you do, like, OTTL to, basically, filter like, the traces and spans you do, and I think there's also some, I forgot the name of it, let me… Check.
Da-da-da I think it's called, Like P data test, which is also something in the collector that I think allows even cool stuff like correlating signals.
So, for example, like, even… I don't know if it's a test that we do have, but, like, trace-to-law cor Because logs are just printed out to STDL, but if we do an application that, like, a collector with a file log receiver, or, like, a STDL receiver, whatever, you can make sure that the correlation matches the traces.
And you can know the exact shape and you can run the Weaver validation inside the same collector as like, like everything is like go through a single thing.
But that's just, like, a concept, but, like, regarding what we… there's also the Kubernetes test, which is, kind of a different test suite.
But I think that, like, makes sense because.
you know, it really does test it in a separate environment that is not document composed.
So I don't know if anyone has any opinions, if they like the normal integration test, built for, like, the freedom of writing whatever you want, but it gets kind of imperative and, like, repeated? Like, all the tests look kind of the same?
I don't know. Tell me what you think.
**Nikola Grcevski @ Grafana / OpenTelemetry** 50:29 Yeah, I'll give you my opinion. I mean, it's sort of like… I, if it's a simpler test, I would choose oats because it's easier to write.
But then if I need to check like trace IDs and compare and make sure that this nest there and then I just go for integration test. But I'll just go with whatever is easiest. I'm also cool if you want to scrap the OATS test and move to another framework that's more OTEL-centric, rather than use any other GTM stack, which was cool for it. Yeah.
Yeah, there's no issues here. Like, the OSTES just sort of came up.
later in Grafana. Somebody from Grafana made. I think they work on the Java auto sig, and they just Came up with this framework, took it home, and… Sort of convinced us to try it and we did, and sort of had a few tests for a bit, but then it became easier to add some of the, like, GenAI stuff and all that. It was, like, much easier to just cookie-cutter add them in, rather than write the integration test.
**Mario Macias** 51:35 Anything else?
**Nikola Grcevski @ Grafana / OpenTelemetry** 51:36 Oh yeah.
**Mario Macias** 51:37 Also remember, I don't… Mike, I think it was, started to move from some tests from Docker Compose.
to our own Go-based. It uses a Go library for tests.
Robert. Yeah, is this third option. I used it for the cloud metadata tests. It works well, but Sometimes it might require some extra work just to set up some special container that We haven't the building block… the building block already created.
Yeah. Also, there was a proposal to donate oats to OpenTelemetry. Do someone remember.
**Nikola Grcevski @ Grafana / OpenTelemetry** 52:24 Oh, it…
**Mario Macias** 52:26 What's the status of that?
**Nikola Grcevski @ Grafana / OpenTelemetry** 52:28 We can ask Gregor. I don't know. I think he attempted or he proposed it. I have no idea.
**Tyler** 52:38 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 52:39 Also, you can also replace the LGTM stack fully, I believe, with a new Docker image that just is auto collector and… Jaeger and Prometheus. That's also another thing. If this arcs you, it doesn'.
**Mario Macias** 52:53 Yes.
**Nikola Grcevski @ Grafana / OpenTelemetry** 52:54 Grafana in there.
Products, then.
No, I just…
**nimrodavni** 52:58 No, I don't mind. Even the… even the integration test, I don't super like, like, Yeager.
**Nikola Grcevski @ Grafana / OpenTelemetry** 53:04 Is there anything?
**nimrodavni** 53:04 And doing like Jaeger queries and like the, like you need to remember like the mappings between hotel and Jaeger. It's kind of annoying.
But, yeah, and, like, the… I have a PR open on adding Weaver validation to it, and, like, the only thing I did is to… Add a collector in the middle of everything, because I need to, like, kind of fork it between Yeah. LGTM and Weaver.
So maybe that's like a preparation, but I don't know.
**Nikola Grcevski @ Grafana / OpenTelemetry** 53:36 For… yeah, yeah.
**Mario Macias** 53:38 -H.
**nimrodavni** 53:39 And, yeah, no, I also caught some like.
issue with… I don't know if it's an issue, but, like, OATSAS are a separate package.
some dependency from OB, and I… like, you basically need to import the entire OB module. I replied to you there on, like… I don't know exactly… like, I think the most correct solution is to separate the integration tests to, like, a different package, because if you… have OB import the Oaths test, then you need to, like, re-declare it as something that, like, a model, a module that we, import.
**Tyler** 54:15 Right? Yeah.
**nimrodavni** 54:16 So I don't know exactly the correct way to go there.
But yeah, so… I can do some POC on that. I don't know if it's super critical, because we can continue the way we're doing it with, like, some doing oaths, some doing integrations, but maybe as a long-term thing.
Standardized.
**Nikola Grcevski @ Grafana / OpenTelemetry** 54:37 Okay.
**nimrodavni** 54:37 Some hotel centric something.
**Tyler** 54:41 Yeah, I mean, that's actually, like, there's an open issue in, like, the goals that Steven and Robert have been working on, on, like, integration tests, like, refactoring, but maybe, like, they would also be interested in this, because, like.
Yeah, to your point, like… yeah, I, like, I would love to get, like, something that works for everybody, but I'd also like to get a policy in place that says, like, this is the way we're gonna go forward, and maybe even clean up the things that we're not gonna use, you know?
**Stephen Lang** 55:09 So that ticket actually got closed.
Because it kind of felt like never ending.
Yeah. So…
**Tyler** 55:15 That's right, yeah.
**Stephen Lang** 55:16 We tried to capture what had been done.
Sort of so far, but we decided that just individual follow-ups and removing it from the goals might be a better idea.
So there's, I think Robert and myself haven't… really have the time either to sort of contribute anything here either. So it's kind of Free for the taking if, if there's more ideas here.
**nimrodavni** 55:40 I can try doing something like a proof of concept for that. I think it will also be good because it will help us, like.
can, we can say, we can, like, validate that every, if we do one standard away, we can make sure, like, every test does, weaver, like, or schema validation, and then, like, every protocol gets covered, and, like, I don't know, maybe we can enforce it, and… Fail on CI on that.
**Marc** 56:12 You mentioned that there is something already in other hotel projects. For testing, can you link some In the docks or something.
**nimrodavni** 56:23 regard… So I mentioned, basically just the collector with, I'll try to find it, I think it's like OTTL, which is the…
**Tyler** 56:33 You mean the P data test thing?
**nimrodavni** 56:35 Yeah, there's OTTL and there's the P data. Yeah.
eData, test.
fucking.
**Tyler** 56:45 Yeah, Mark, that's not a… it's not like a full-featured integration, it's more just like a library that we can use to What are we talking about? Yeah.
**nimrodavni** 56:55 I don't know if there's like… I don't know, like, how other instrumentations… I don't know if they need this, like, end-to-end testing of…
**Marc** 57:04 Yes.
**nimrodavni** 57:05 instrumentations, so I don't know if they do it. I don't know if other products or.
**Tyler** 57:10 I can say, like from, from, like, the Go perspective, like, we definitely do. That's where, like, Robert… a lot of his, like, suggestions were coming from that, because, like.
yeah, when we write GRPC interpretation, we write HTTP interpretation, we need to show that, like, we're actually getting things coming out the other end. We do a lot of this, like, collector validation, where we run… we actually don't set up a collector, because at the end of the day, like.
The thing that you send to the collector is OTLP, and so we just validate the OTLP, keep it as close to the source as possible.
This existed before the pdata test package existed as well, by the way. So essentially, like, we wrote our own, and we just have, like, comparative, like, structures there to, like, say, like, hey, I'm getting this resource, spans, and, like, is this the resource spans that you were expecting, kind of thing, and, like, getting valuations that way.
I think if that works, it's a lot harder when you have, like, OB where it's just continually dumping data, and you're really trying to look at, like, maybe not every specific, you know, trace to match every single trace.
So, yeah, like, it's kind of, like, that's kind of the use case. The Weaver stuff we've always wanted to add, we haven't, though, just because it's just on the backlog. So, yeah, so from perspective on the outside, and a lot of other companies, or a lot of other, projects in OTEL are using Weaver for this kind of testing as well. So, yeah, you're not in the wrong… Wrong place, yeah.
**nimrodavni** 58:38 All right.
Cool. Well, I'll try to get something then hopefully present it in the next few things.
**Tyler** 58:48 Perfect, perfect. Awesome.
Okay, With that, then, we are coming up right here on the end. Any other quick comments or shoutouts people wanted to make before we… Draw the meeting close.
**Nikola Grcevski @ Grafana / OpenTelemetry** 59:05 Yeah, I don't know if you guys are keeping score, but I think OB is the second most popular Docker image download from OTEL after the collector.
That's good news.
**Tyler** 59:17 Let's get that collector.
**Nikola Grcevski @ Grafana / OpenTelemetry** 59:19 Yeah. No, they're like 100 times more. Yeah, there's no way.
**Tyler** 59:25 In fact, now that we're integrating, with the collector, I guess, yeah, maybe I didn't.
**Nikola Grcevski @ Grafana / OpenTelemetry** 59:30 I like that.
**Tyler** 59:31 Yeah, if people didn't see that, like, we're now in the collection contrib as well, so… Technically, those downloads are kind of ours as well, at.
**Nikola Grcevski @ Grafana / OpenTelemetry** 59:39 100%, 100%.
**Tyler** 59:41 Yeah. So cool.
Awesome. Well, Good seeing you all, thank you all for joining. We can end the meeting here. I will see you all in a week's time, or asynchronously. Until then, talk.
**Nikola Grcevski @ Grafana / OpenTelemetry** 59:55 Bye.
**nimrodavni** 59:56 Bye-by.
**Mario Macias** 59:57 Bye bye.
