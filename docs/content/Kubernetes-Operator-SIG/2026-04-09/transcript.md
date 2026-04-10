SIG: Kubernetes Operator SIG
Date: 2026-04-09
Duration: 36 minutes
============================================================

## Zoom Recording Transcript

**Benedikt Bongartz** 04:04 No room.
**Pavol Loffay** 04:05 Oh, what happened?
**Ozzy** 04:11 Hello.
**Pavol Loffay** 04:14 That is true.
**Ozzy** 04:15 Okay.
**Benedikt Bongartz** 04:19 Nobody here, no agenda.
**Ozzy** 04:23 Just have to play some Uno.
I don't think… I guess Uno wouldn't work very well in a remote. I don't really play much Uno, I think a lot of it is putting the cards down in front of you, isn't it? So, I don't know.
Virtual Uno.
These meetings are recorded, aren't they? I have to keep that in mind. If I make a bad joke, then it kind of… it's… it goes down and skips forever.
**Pavol Loffay** 05:29 Yeah, never watched the recording, though. They should be uploaded somewhere, but I never…
**Ozzy** 05:34 I, I have.
I watched, like, the one… I don't know, the one I missed, because of the calendar issue, and so I think I looked up a bit of it and stuff. It was kind of… it was kind of interesting. But it's funny to watch a meeting when you're not in the meeting, it's always… it's almost like a strange… it's like you're watching a kind of a TV show or something, you know?
**Mikołaj Świątek** 06:41 Well, sorry for being late.
**Pavol Loffay** 06:44 Hello, I'm good.
**Mikołaj Świątek** 06:54 Are we waiting for… Jacob?
Did you say he's not coming?
**Pavol Loffay** 07:04 I don't know if he joins… I didn't see anything on Slack.
**Mikołaj Świątek** 07:10 I also don't see anything in the agenda, but I personally added some… I've tagged some issues with the label, so I'm just gonna… Put them in here.
**Pavol Loffay** 07:23 Yeah, I wanted to ask something. So I started, I think, last year on the instrumentation CRD, And I will have time next week, probably, to continue working on that.
So I was wondering if there is anything anyone else looked into it, or… finishing like this.
Hi, Jacob.
**Mikołaj Świątek** 07:47 Hey, Jacob.
**Pavol Loffay** 07:48 I think, Jacob, you discussed the… we discussed the instrumentation CRD at KubeCon, and I started the work a couple months ago, but… Then we decided not to go forward with it, because it was… it was using just, yeah, it was using just the SDK schema without the, kind of, the old config that we have in the V1 Alpha 1. I was just curious if anyone else is looking into it, or if I can refresh my PR, and what I wanted to do is to… Do the cleanup that we discussed.
on the V1 Alpha 1, there is the endpoint and something else, and submit this as a base for V1 Beta 1.
Just the API.
with a spec, without the controller, you know, just the API, and then we would just kind of take it from there. On the call, there is as well, Ozzy, and he… It's as a new member in our team, and he will be contributing more and more into the auto operator, and he could pick up some of the work as well.
**Ozzy** 09:06 Hello. No, it's nice to be here.
**Mikołaj Świątek** 09:11 Nice to have you.
Especially if you're gonna go and make CRDs, because that's the most painful part of working.
**jea** 09:23 Pavel, this all sounds good to me. I'm happy to review.
I'm gonna begin on the injector work sometime in the coming months. Next month, probably.
Or, like, next couple of weeks to the next month, so… This couple as well.
**Pavol Loffay** 09:40 Awesome. Like, the injector integration into the operator, or… Yeah. Okay, awesome.
**Mikołaj Świątek** 09:46 What about the refactor, Jacob?
**jea** 09:50 We're doing… what we said is that we're gonna do the refactor as part of the injector stuff, because that will be the method of doing it.
**Mikołaj Świątek** 09:57 Okay.
**jea** 09:58 I want to just delete the old stuff, I don't even want to touch it anymore.
**Mikołaj Świątek** 10:02 Okay.
I have one request, Pao. I think what we should start with in there is to just create an issue, if we don't have it already, for the view on Beta 1, and just list what we want to do, because I think this just exists in the SIG meeting notes, and doesn't exist in any issue, it would be nice to just have it in one place, saying, like, in the background, we want to have, you know, two different fields for using the collaborative configuration, right? One structured, and one raw, and, you know, we want to do the label instead of annotation, and so on. I don't think this was written down anywhere in it.
Probably should be.
**Pavol Loffay** 10:43 Yeah, that's a great idea, We can actually discuss now whether we want to have the raw or the structured SDK config. I think since the SDK config is already… stable V1, then we should probably try to model it, directly in the CR.
the typed fields.
**Mikołaj Świątek** 11:08 We already discussed this, and we decided that we want to do both.
Per… and the reason for that is roughly that… Even though it's stable, it will have things added to it.
Right? And then we will be the… if we only have the structure configs, we're going to be the gatekeepers of those.
updates, right? People won't be able to use new features in that declarative config until we add support for those. And the raw config is kind of an escape hatch, in case somebody… or if somebody has, like, their own extension of it or something, right?
**Pavol Loffay** 11:49 Yeah, I was not…
**Mikołaj Świątek** 11:50 arguments.
**Pavol Loffay** 11:51 I was not aware of like, the extension part. I'm not sure if there is, like, all those extensions, or if they will be adding stuff, but yeah, probably it might change in the future. I think we discussed the raw… Config, because it was not stable.
And that would be, for us, a way to get started, and then once it's stable, we would deprecate the raw configure. I think that was… But maybe I…
**Mikołaj Świątek** 12:24 Any difference?
**Pavol Loffay** 12:24 something.
**Mikołaj Świątek** 12:25 We can talk about this now. Like, my opinion in general, like, maybe we eventually deprecate raw config. But my opinion, even for stable things, like, if you recall, there was the same discussion about the managed CRD, and whether you want to just embed the configuration schema for… the OTLP exporter into it, and I thought that was… we shouldn't do that for the same reason, and that reason is just that it… like, it couples, it couples us to it. Like, we be, the CRD becomes the gatekeeper of what is doable.
in those configurations. And those configurations, again, the fact that they're stable doesn't mean that they can't evolve, right? They will evolve. There will be no features added to them.
**Pavol Loffay** 13:12 I think in that case, let's start with the unstructured, as, like, a… Not proof of concept, but kind of validating the idea how it works.
And then… Think about how to expose this with all the validation, with typed config.
No, because the… when you look at my old PR, it was quite complex, actually, if I wanted to model all the fields from the declarative config.
In the CRD. It was not any kind of easy way to do.
**Mikołaj Świątek** 13:48 My problem with… so, for the record, my view of this is that Structured config is generally better, like, it's more… way more user-friendly. That's the reason we moved from the… from raw to structure it in the collector CRD.
I think it's good, like, the fact that it's complex doesn't necessarily mean that we shouldn't do it. I think it's fine, especially if it's, like, easy to… relatively easy to auto-generate it, then that's, like, another reason to just do it, to me. And I think we should just… it should just have both. We should tell users, use structured.
If you really, really want to, and you know what you're doing, you can use RAW. That's kind of, like, my opinion on it, and they should be mutually exclusive. Like, we should fail validation if they are both set.
That's, like, my vision of this. I don't know if…
**Pavol Loffay** 14:42 Yeah, I would wait until… There is a new version, so we know we will have to support multiple versions at the same time.
Or, if we know there are extensions that people can actually provide to the config.
Otherwise, if there is just one stable version without any extensions, then it seems like… Redundant to have the two fields, one for destructured and for unstructured.
But I need to double-check what's kind of… how it works in the company.
**Mikołaj Świątek** 15:16 The… what I… my understanding of what stable means is that stable means that they're not going to be making breaking changes, right?
**Pavol Loffay** 15:24 Right, but we don't know if they're, like, planning additions, like, soon, or this thing will kind of change, maybe in two years.
**Mikołaj Świątek** 15:34 you know, if it changes in 3 years, we'll have to deal with it, right? My…
**Pavol Loffay** 15:42 Well, in that case, like, if it changes, like, in 2 years, and there is, like, next major version.
then I think we should… It should be fairly easy to prepare for it.
Right? It's not like with the collector components, like, there is many components, people can write their own components, we don't know how the config looks like, but if the SDK config is something that is kind of well-maintained, well-versioned, and deterministic, then it's going to be easy for us to… To keep up with this.
But I think it depends, like, how often they release it, right, as well.
**Mikołaj Świątek** 16:19 I am… I'm also okay just using structured config for now.
I'm also okay with that. Like, the adding… so my view of this is also that… If we start with structured, we can always add raw if we want, and it's not gonna be a breaking change, it's gonna be an optional thing.
In there.
if we start with raw, then we'll have to migrate from… and if we start with raw and want structured to be the default later, then we'll have to migrate, and that's going to be a pain. So, if we're going to start with one, I would prefer to start with structured, because I think that's, like, the better… The better, experience for users.
**Pavol Loffay** 17:02 Yeah, I'm fine with that, especially if we can write, like, good, Kind of generation code for it, and have good-end kind of tests to validate that the structure matches the spec.
**Mikołaj Świątek** 17:16 Yeah, and this is, like, not… like, this notion that it will have new features, it will have new features, but, like, at this point, not even, like, most of the instrumentation SDK is supported, right? So, it's gonna take a bit before we even get to that point.
**Pavol Loffay** 17:35 Okay, awesome, so I'll start with the issue, and then open the… pull request to… with, like, the CRD.
**Mikołaj Świątek** 17:47 Okay, so… I got… Well, this is something, Jacob, that might be close to your heart, given your comments about the… about me wanting to delete all the, all the service discovery providers from Target Allocator.
There is a user who wanted to add an end-to-end test that just starts target allocator using some manifests without the operator.
And so I said, I mean, sure, you can test this manifest, but does this really help anyone? What we should be doing is, like, we should have an official customized manifest per target allocator. We already have a helm chart, so this is just kind of making that more official.
In a way, so… and there's an issue, there's even a pull request for it, if you have opinions about how this should work and where it should go, you know.
have a look at it. I'm not actually sure, like… Just in terms of, like.
organization in the repository. Where should it be in the repository?
is the only thing I'm wondering about. Should it be, like, under the target allocator subdirectory, or should it be under slash config, where all the operator stuff lives? I'm not sure if I have, like… Good sense of what is better.
**jea** 19:19 Yeah, I'm not opposed to it. I don't… I mean… Is this not why we have a helm chart for the target allocator now, though?
**Mikołaj Świątek** 19:29 Yeah, we do. I'm saying, like… If you want to… Maybe the answer is also this. Maybe the answer is, like, there's a Helm chart, there's tests in the Helm chart.
I hope those tests in the help chat anyway.
**jea** 19:44 There's a few tests in the Elm Chart. I don't know if we have a lot of tests in the Elm Chart.
**Mikołaj Świątek** 19:48 Maybe that's, like, maybe that's a valid thing. It's a question of what we want to support, right?
**jea** 19:54 Yeah.
I mean, I'm not opposed to supporting Customize, given that we do that for the operator, right?
**Mikołaj Świątek** 20:01 Exactly.
**jea** 20:02 It doesn't feel unreasonable. There are definitely people out there that don't want to use Helm, so… I'm not… I'm not opposed to it.
**Mikołaj Świątek** 20:12 I'm also not opposed to it. Abel? Bene?
No votes. Okay.
**jea** 20:26 Cool.
**Mikołaj Świątek** 20:27 Oh, I'm, I'm, I'll nego that.
If you have opinions about where it should actually live, I'll put you… when we're ready with the pull request, I'll put all of you in there so you can voice your agreement or dissent about where it's going.
I'll make a note. Another thing that I'm adding here right now is a… Basically, there is a very, unfortunate unfortunate CDE.
**jea** 21:05 Oh, yeah.
**Mikołaj Świątek** 21:06 in… in… the CV is actually in the Docker server, it's an off bypass.
The problem is that if you have a Docker client.
It used to be the same module.
So you're theoretically importing all the server code as well, so that CVE gets flagged if that's in your Go mod. And it's in a lot of Go mods in those sorts of places.
The second problem is that Docker has since deprecated this, and now they have a separate client package, which is really nice of them, because you don't have to pull the server stuff anymore. But the client package is a completely new package, so your dependencies have to, like, migrate it to it actively. You can't just bump the transitive one in your grommad and fix the CVE that way.
So there's a pain. I'm gonna put the issue link in, in the thing. I've…
**jea** 22:04 I think Medius has fixed this upstream.
**Mikołaj Świątek** 22:07 Yeah, and now we have to…
**jea** 22:10 They're gonna push a new version soon.
**Mikołaj Świątek** 22:12 Yeah, can you… can you put that link also in the, in the intro that we have? Yeah, yeah.
**jea** 22:18 Yeah, yeah, yeah.
**Mikołaj Świątek** 22:21 Alright, so… Yeah, by the way, if you haven't… if you haven't noticed, I also… it also turned out that we were importing this code in the operator for absolutely no reason. It was, like, a holdover from the time that we did… target allocator or parenthes receiver config parsing in a different way, and it was still being kind of imported as a… just, like, as a bunch of init functions, and I deleted that, and it reduced the operator binary side by more than half.
So, if you… if you notice that, that's because… that's why it happened. It's quite nice, or maybe not nice, depending on how you wanna… how you wanna see the situation. But at the very least, the operator the GO mod is flagged by the scanners, but the actual operator binary will not be flagged by the scanners as of the next release, so… It's only gonna be the target allocator in our… and in the target allocator, we can't remove it, because… That's what the target allocator actually is.
Similarly, similarly, there's a related thing where… When this came up, We had a… I should have put all these issues here ahead of time, sorry, I'm not… I'm not… I'm unprepared.
Because when this happened, GoVolumeCheck was blocking every single pull request.
Which, I don't think that's what should happen.
In this situation?
And Go Valentrac ideally shouldn't, like… Right, see on Slack. For the record, there is a discussion about this on Slack.
In the operator leads channel.
**jea** 24:28 Yeah.
I'm bumping to the latest Prometheus, by the way, right now, to fix this.
**Mikołaj Świątek** 24:34 Is it out? Ready?
**jea** 24:36 It is out.
**Mikołaj Świątek** 24:37 Okay, cool. Nice.
**jea** 24:40 At least I'm doing exactly what the, Prometheus, what Contrib has done, so…
**Mikołaj Świątek** 24:49 Nice.
Go, Valentrak!
I… I almost feel like this should be a PR check, but it shouldn't be required.
is kind of where I'm landing with it right now.
Because if it only runs on the main, that's kind of… much less discoverable, but it also shouldn't block unrelated pull requests, it should only block the ones which add new dependencies, but also… This is surprisingly not very easy to… to actually accomplish.
So, like, making it so that GoVolumeCheck pay… that the CI check fails only if…
**jea** 25:37 Here's the PR, by the way.
**Mikołaj Świątek** 25:39 Yeah, thank you.
making it so that GoVolmCheck only fails if the PR in question modified the dependency that it found is… surprisingly not so easy. We can probably make it work like that, but I am not sure if we want to really bother.
What do you think?
**jea** 26:05 I don't know, I mean, I think it's good to have it, I don't think we need to block on it.
I think we should just make it not a required, required action for merge.
**Mikołaj Świątek** 26:20 Where… which repository is this controlled in? Is this already in, like, Terraform, or is it, like…
**jea** 26:26 Probably in Terraform. It's probably in the, the admin repo.
**Mikołaj Świątek** 26:33 And is this, like, an org-wide policy? Or do we control…
**jea** 26:38 We should be able to control it. I mean, that's kind of the idea behind the.
behind the repo is that we have control over these things? Let me check it out.
**Mikołaj Świątek** 26:49 Yeah, yeah, I'm looking at it right now.
Auto operator… Yeah, we do control it, and the required checks are already there, so… if we just move it out of code standards limping into somewhere else, that's just gonna accomplish that, I think.
**jea** 27:08 Yeah, yeah, that's exactly right.
**Mikołaj Świątek** 27:11 Which I am in favor of, because this is something that should be seen, should be visible, but it shouldn't block us from merging.
**jea** 27:18 Yeah.
**Mikołaj Świątek** 27:18 requests.
**jea** 27:19 I agree.
**Mikołaj Świątek** 27:21 Right, cool. So, there's a agreement on that.
And finally, there was one more thing… It was… I don't think we really need to talk about this deeply, but… there is… and there is this issue where we want to make API its own module.
**jea** 27:50 Right.
**Mikołaj Świątek** 27:51 And there is an active discussion about what the options are, and what that means exactly, and there's a contributor here who is, like, testing different approaches to it. So if you have opinions about this.
I'm gonna…
**jea** 28:08 I mean, I'm happy for this to change. I don't know… What this will look like in practice.
Oh.
**Mikołaj Świątek** 28:19 I mean, I think it's pretty straightforward in practice, right?
**jea** 28:22 It looks like he's just moving… he's starting by moving all of the, .
**Mikołaj Świątek** 28:35 I'm not sure.
**jea** 28:36 I don't help.
**Mikołaj Świątek** 28:37 PR that you're… I'm not sure if the draft PR that you're looking at is, like, very representative, necessarily.
**jea** 28:43 Oh, okay.
**Mikołaj Świątek** 28:44 I think that's just, like, experiments right now.
**jea** 28:48 I see.
**Mikołaj Świątek** 28:49 I think the way it should look is just that… there's a separate module, maybe some of the code is moved a little bit internally, is moved somewhere else, or whatever. So, for example, the GoMod doesn't have all the test dependencies in it.
Right? But there's a new module, and the operator main module just depends on it, and there's a replace in there.
**jea** 29:20 Yo.
**Mikołaj Świątek** 29:20 That's… that's basically it.
**jea** 29:24 It doesn't sound terrible.
**Mikołaj Świątek** 29:27 There's some argument against this, some arguments against us, if you can look at the issue.
**jea** 29:34 Oh, yeah, the release cycle stuff is annoying.
**Mikołaj Świątek** 29:36 It's not, no, the release cycle stuff is perfectly normal. You just push another tag.
When you release, and that's it.
**jea** 29:43 Oh, I see.
**Mikołaj Świątek** 29:44 like, Contrib does that with, like, 5 zillion modules. Core does that with, like, 5 zillion modules, and it all works, so… I don't think this is a big problem. I even checked how Prometheus operator does it. They also just, like, push another tag in there with the right prefix, and that's.
**jea** 30:00 Yeah, that's.
**Mikołaj Świątek** 30:01 covers it, so that's also another problem. The main argument, kind of, against doing it this way is that As a point of principle, multi-module repositories suck a little bit.
**jea** 30:14 Yeah, especially in Go.
**Mikołaj Świątek** 30:16 like, I… now, I use Golant now. I use Golant, and I don't have problems, but when I used VS Code and derivatives in the past, I did have problems with these, yes.
**jea** 30:27 Yeah, you have to start using, like, Go work files, and make sure that those are, like, set up correctly.
**Mikołaj Świątek** 30:32 Yeah, so that's… that sucks a little bit.
**jea** 30:35 Yeah, but we're not, you know, we're not, the collector, right?
Like, we're not gonna have a million modules, in my mind.
**Mikołaj Świątek** 30:45 This should be a very, very simple module at the end of the day, just at least in terms of, like, just, like, the mechanics of it, right? Yeah. It should just be struct definitions, whatever the struct definitions require, and that's it. Like, we already moved webhooks out, so it's already simpler than it used to be. And now it's, I think, a question of… Moving things like tests out of it?
**jea** 31:07 Yeah.
**Mikołaj Świątek** 31:07 Because, like, the valid… all the… all the, like, validation, conversion, whatever, things, those also don't need to be there.
**jea** 31:15 Really. Yeah.
**Mikołaj Świątek** 31:19 Yeah, so that's basically it. I don't think we need to make any decision. Oh, there's also another argument. The other argument is apparently Cube Builder doesn't entirely like this pattern.
**jea** 31:30 Yeah, Kube… I remember trying this out, and KubeBuilder does not like this. I thought the way that we were gonna get around this, There was a way that we talked about getting around it, but I forget what that was.
I forgot. I thought there was a way to get around this with Cube Builder.
**Mikołaj Świątek** 31:50 I mean… It's like, I care if controller tools works.
Yeah. Because that's what's used for the.
**jea** 32:00 Well, we use that heavily. Like, we need that to work.
**Mikołaj Świątek** 32:03 I'm not sure if we really need the cube builder, like, add new CRD, whatever, command. I don't use it.
**jea** 32:10 Well, we use that for all the cell stuff, which we do need.
**Mikołaj Świątek** 32:14 Mmm.
What do you mean?
**jea** 32:17 We use that for all of the generation and the, common expression language stuff, right?
**Mikołaj Świątek** 32:22 No, no, no, what I mean is that there's controller tools. Controller tools is, like, the program that you use to… to generate, like, your CRD manifests.
From your struct definitions, for example, right?
**jea** 32:36 Yeah, but I thought we were using… Let me find it.
Yeah, we're using, coo Builder for… All of these, status things and validations.
**Mikołaj Świątek** 32:56 How are we using it? Like, what is the actual invocation?
Yeah, but what I'm saying is that this says Coop Builder, but what… in practice, what matters is, like, which… Because Cube Builder is something that runs on the codebase and generates certain things, or, like, makes changes to your Go code in some structured way, right? Yeah. And this is just a question of whether those things work.
Correctly, because the way this works is that you have these, all these annotations, and then Cube Builder, or, like, things which are part of the Cube Builder suite, let's call them, are gonna do things like turn your… Code builder annotations into the right CRD definition in YAML, right? Yeah. And it's a question whether those tools run correctly, because there's a bunch of different tools. There's a different tool for saying things like.
generate CRDs for me, that's controller. Controller Tools is the binary for that, I believe. And there's a different tool when you want to say, like, hey, KQ Builder, I have this standard project layout, I want to add a new, and use CRDU, webhooks, and all the other bits, right? And then it does that automatically. But that's, like, a different program.
And that program cares about your repository layout a lot. The program that generates CR… that generates the CRD definitions doesn't really care about the repository layout or modules, I think.
**jea** 34:36 Yo.
**Mikołaj Świątek** 34:37 Maybe I'm wrong.
**jea** 34:39 I thought it did, but it might be incorrect.
**Mikołaj Świątek** 34:42 Maybe it does, because it has to actually parse the Go code, so maybe it does actually care about this.
**jea** 34:47 That's what I remember from the last time that I tried to do a migration like this, but it could have been updated. I might be incorrect.
**Mikołaj Świątek** 34:57 No. Yeah, well, anyway, like, this isn't really an urgent thing to do, and it's, like, not really blocking or depending on anything else.
**jea** 35:04 Neither way, I'm supportive of it.
**Mikołaj Świątek** 35:05 well.
**jea** 35:06 So, like… It'd be good… good for us to do this thing, so…
**Mikołaj Świątek** 35:11 Yeah, I agree. I agree with that. I wonder how many consumers of our API packages there actually are.
Oh? I don't have a…
**jea** 35:18 Probably more than you think. There's a lot of these, like, hotel… esque companies that are starting up in the past couple of years, and I think a lot of them, like, Dash Zero, I think, has some dependency on it, or something like that. Maybe they don't, maybe they don't know, but I remember at some point they did, and, like, Odigos is, like, another one.
There might be a few that we don't know about, is I guess, what I'm saying.
**Mikołaj Świątek** 35:44 This is… Something that we can easily do.
**jea** 35:49 Yo.
**Mikołaj Świątek** 35:49 In the…
**jea** 35:51 Okay, do we have anything else?
**Mikołaj Świątek** 35:55 I don't. Do you?
**jea** 35:57 I got nothing.
**Mikołaj Świątek** 36:00 Right.
**jea** 36:01 Cool.
**Mikołaj Świątek** 36:03 Yeah. See you, see you later.
**jea** 36:05 Yep. Yep.
Bye.
