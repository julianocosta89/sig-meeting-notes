SIG: Kubernetes Operator SIG
Date: 2026-07-16
Duration: 61 minutes
============================================================

## Zoom Recording Transcript

jea 00:01:37 Hello.
Mikołaj Świątek 00:01:42 Alright.
Do we have any topics?
It looks like it, although we don't have a…
jea 00:02:08 Yeah, I can…
Mikołaj Świątek 00:02:09 Oh, I'll do it, I'll do it.
jea 00:02:11 Okay.
Mikołaj Świątek 00:02:15 And the first topic is Tyler's, which is unfortunate considering he's not here.
Oh, there he is.
jea 00:02:52 Tyler, I thought you were on vacation.
Tyler Helmuth 00:02:54 That's next week, two weeks.
jea 00:02:56 Oh, it's next week.
Tyler Helmuth 00:02:57 Start next week.
jea 00:02:59 Hope you have a good vacation. You going anywhere.
Tyler Helmuth 00:03:01 Thank you.
Yep.
jea 00:03:05 The whole continent.
Tyler Helmuth 00:03:06 Two weeks, whole continent.
jea 00:03:10 Plenty of time.
Tyler Helmuth 00:03:14 How big can Europe be?
jea 00:03:15 Someone's doing some stitch.
Mikołaj Świątek 00:03:18 Parts you cut, you count exactly, is like… surprising, actually, how far it extends into Russia, for example.
So, but I wouldn't, I wouldn't go, I wouldn't really go there unless you're feeling very adventurous.
jea 00:03:34 Teller is quite a thrill seeker from what I've heard.
Tyler Helmuth 00:03:38 Yeah, let's take my family to Russia. It's a great time.
jea 00:03:42 Yeah, it's beautiful this time of year. Great, great time.
Tyler Helmuth 00:03:45 Great time for Americans to travel to at the moment.
Mikołaj Świątek 00:03:49 It's actually quite unfortunate, but that's not Russia, right? But Crimea is actually really, really pretty.
Tyler Helmuth 00:03:56 Yeah, I think it would be an amazing place to visit. I just don't think the climate at the moment is good for me. Someday, hopefully.
Mikołaj Świątek 00:04:05 Yeah, someday, hopefully.
I think, I think we can get started. It's actually yours, before it's yours, Tyler, because yours is the only topic other than the…
Tyler Helmuth 00:04:20 Cool.
Mikołaj Świątek 00:04:21 Recurring ones that we have.
Tyler Helmuth 00:04:25 So this is about, this is again talking about.
Instrumentation CR, as we're working on A V1 beta.
should we make a breaking change to drop a default version? We talked about slightly at, KubeCon EU.
I believe.
And I know that Jack has been… has been pushing on this, it sounds like, at least.
I wanted to bring it back up because more semantic conventions are getting closer to becoming stable. I'm thinking about, like, the… Kubernetes semantic conventions, we've already marked some of them as stable, like the caves attributes processor is about to be marked stable And so while that's, like, a collector thing and not so much an instrumentation thing, like, as Python and stuff does more AI stuff, and they're gonna try to mark things stable really fast, I'm just thinking about, like, how can we avoid the pain we experienced with the HTDP semantic conventions, where we got stuck on old old versions, because we were worried about hurting users, which was… I'm still convinced was the right thing to do. I don't… we would have broken a lot of users, and it would have been really sad if we had just bumped to, like, Java Agent 2 immediately.
So yeah,
Mikołaj Świątek 00:05:43 Well, I wonder about that a little bit, right? Because we actually did bump it, right? We bumped it in a way where we, if somebody has 1.x, they stay on 1.x and they get a warning.
Saying, we can't upgrade you.
Because you're on… because there's a serious breaking change, and it links them to the issue, and so on. But this has happened, like, several releases ago, where now, if you create a new Java instrumentation, and you don't specify the image, you're gonna get 2.x.
There has been no reports, no issues, nothing about this change.
So I'm sometimes wondering…
Tyler Helmuth 00:06:22 It's been a long time. The HTTP semantic inventions have been stable for two years, I think, now. Java 2 has been out for a really long time.
Mikołaj Świątek 00:06:30 And yet, in some of the SDKs we support, it's not enabled by default, right?
Tyler Helmuth 00:06:38 What do you mean? Oh, for the other languages. Yes, I agree for the other languages. Absolutely.
Mikołaj Świątek 00:06:45 Neither Python nor Node.js.
Tyler Helmuth 00:06:47 Or in JavaScript, I think. Yeah.
So… the thing that I'm wor… like, most worried about when we do these breaking changes is, like, a user who has… for… for Java example, who had… The most mature, they were running full semantic conventions.
If we had upgraded them right to 2.0, anything that they had been using would have immediately stopped working.
and,
Mikołaj Świątek 00:07:15 Even worse.
Tyler Helmuth 00:07:16 To avoid, right?
Mikołaj Świątek 00:07:17 Right, even worse. Like, it's one thing — and I talked about this at KoopCon. It's also in the issue that I opened about this.
The problem isn't that it breaks. If it's like, if they upgrade and suddenly their stuff immediately stops working, like that is…
Tyler Helmuth 00:07:35 Better.
Mikołaj Świątek 00:07:36 That is, there's a correlation between two events and so you can roll back, right? And you're good. That's how it works with most things.
that you try to upgrade. But here it's different. You upgrade and nothing happens. And then sometime later, your pods start getting cycled for some completely unrelated reason. And now it's broken.
Tyler Helmuth 00:07:57 Yeah.
Mikołaj Świątek 00:07:58 And then you decide this was the operator doing the upgrade. So let me roll back the operator. That also does not fix it because you also have to cycle all your stuff. And I think even the rollback doesn't even help because we don't actually roll back the instrumentation version. So the only thing that does help is explicitly setting the specific.
Tyler Helmuth 00:08:22 The image.
Mikołaj Świątek 00:08:23 the image in the specific instrumentation. Yeah. So that's like that. That's the reason we are so careful. And I am like largely convinced by Jack's argument, I would say. We were all convinced by Jack's argument. What we didn't want to do is, like, block V1Beta1 instrumentation on this, and the reason is that in order to do this, I think we have to or maybe not, maybe, maybe not. I am open to being convinced otherwise, but the main problem is that when we tell users you have to pick what you want.
Yes, we can then, like… make our documentation, you know, contain always the latest one. If you're creating, like, if you're creating a new instrumentation, you're copying the manifest from our, like, getting started guide, then you can always have the latest one, we can have some automation that updates that documentation, like, whenever there's a release, that's fine.
that's that's like a minor thing. The bigger problem is that the release process for these images is very.
Tyler Helmuth 00:09:24 Yeah.
Mikołaj Świątek 00:09:25 Minimal, let's call it.
And it's one thing that's minimal. It's, like, basically what it does right now is that whenever you bump anything… whenever you bump the… version in the… Whenever you bump, like, the major version of the SDK in the manifest.
Then it creates a new package.
Or a new… it creates… it builds and uploads a new image. But this is incredibly, undiscoverable. The only way to know that this exists is to actually just go click on packages in GitHub. That's the only way.
Tyler Helmuth 00:10:15 Yes, agre.
Mikołaj Świątek 00:10:16 So I think that has to be fixed.
One of two things needs to happen there, or maybe none of them. And we just say, just check it out here, whatever. Just go here and check what's available if you want to know.
But either there has to be, like, a release announcement of some sort when a new thing comes out.
Because right now, it doesn't exist. We just release the operator, and the operator in the release notes, it says which images it uses. And that's all of it.
Sometimes it might be that there were two bumps of something between operator releases, and you're only going to see the newer one.
In there.
So… That has to be improved and/or the actual process needs to be improved, as in we need to define when we — what is the versioning scheme? When do we release new versions? Is the versioning scheme literally just what it is right now, by which I mean we just go by the SDK version?
But what happens if we need to issue, like, a new Image, because we bumped something else in there for security reasons.
Tyler Helmuth 00:11:34 Yeah.
Mikołaj Świątek 00:11:34 I don't know, that kind of stuff does happen. So what's the versioning scheme then?
I will. How? What does it look like?
I don't think these questions are super, like, super difficult to answer necessarily, but there's a bunch of things that you need to be able to do, and, like, a bunch of additional, like, GitHub actions, whatever, automation you need to write for this to work.
Tyler Helmuth 00:11:58 Yep.
jea 00:12:00 I think we still should do it, though. Like, I think we should just iterate through these are the decisions. This is the process we're going to follow, because I think that this makes life a lot easier. I think this also goes back to the discussion we had when Jack was here, when I was saying, like, I really don't want them to do what they're doing.
And if we can prevent.
Tyler Helmuth 00:12:19 True.
jea 00:12:20 Splitting.
Tyler Helmuth 00:12:20 to… you don't want Jack or the Java, like, doing what doing?
jea 00:12:25 Sorry. I don't know if you were here for that. Basically, Grafana is like writing their own operators.
Tyler Helmuth 00:12:31 Oh, the injection controller. Yeah, yeah, yeah.
jea 00:12:34 And…
Tyler Helmuth 00:12:35 Okay.
jea 00:12:35 I'm just like, why are you guys doing this? This is useless. This is actually really frustrating.
Mikołaj Świątek 00:12:41 I had a reminder that this is recorded, Jacob.
jea 00:12:46 That's okay. I told, I told Jack to this. I told.
Mikołaj Świątek 00:12:49 I know, but now you're telling the whole world to listen to this.
jea 00:12:54 That's okay. I told him in this meeting last time, so it's all right. I said very explicitly, I don't think we should split the community in this way. I think that it's pretty harmful.
And I think that doing this type of split is like.
very frustrating, especially when it's like, we could use the help from people who are writing injection stuff. You know, it's like, why not contribute to this thing that you're already a part of? I don't know.
It struck me as…
Tyler Helmuth 00:13:21 I think that Jack does have plans to contribute that, the injection controller.
like, there are plans to contribute that. I work at Grafana, I can say that there are plans to contribute the injection controller to OpenTelemetry. I don't have the history of why it was started internally at Grafana, I just started here myself. Yeah. But talking with Jack, I know that they want to contribute it eventually.
jea 00:13:45 eventually is the thing that I am uncertain of. There has been a promise of that in the past for, like, other, like.
Projects like this, like, I think Dela was one of them, right?
Tyler Helmuth 00:14:00 I think they're,
jea 00:14:01 If I'm wrong.
Tyler Helmuth 00:14:02 Bela is OB, right?
jea 00:14:04 Is that normal.
Tyler Helmuth 00:14:05 Bill is a brand name for OB, yeah.
a brand name, I don't know if that's the right term. Bela was what Grafana called it when it was open sourced to Grafana, but I believe Bela was donated and is now named Obi. That's my knowledge of.
jea 00:14:18 Yes, it has. Okay.
Cool.
Either way, I'm of the opinion that like, if we can take the things that they would like.
the operator to do and just integrate them, like, we should do that. I know none of the things that he said, I think, are things that we are opposed to or, like, don't want to do ourselves, and so we should just do a good job to, like, incorporate that feedback, right?
Yeah.
Tyler Helmuth 00:14:45 I mean, I.
jea 00:14:46 Well, that notwithstanding, like, I think that the.
The assertions that Jack made are all correct, like, I don't think that we should.
You know, I don't think that we should.
automate the, like, images and things. I think that it makes it actually a lot more opaque to users in the wrong way.
And I think it'd be better for us to… automate that process. I think it'd be better for us to do that for a couple of things, where it' the… Some of the automations we do around like port, I think is a good example of like we do that for good reason where there's like an override hash, but it's not really like a breaking change. But I think that when we overstep our bounds a bit too much, like when we're doing too much Prometheus rewriting, we get into this territory of doing like.
Opaque stuff that negatively affects, like, user experience.
And so I think we should really only do that type of thing when we are confident that we want to own that.
like, upgrade process.
Is, is maybe the, the, the barrier to me.
Mikołaj Świątek 00:15:54 I think the problem.
Tyler Helmuth 00:15:54 For the inference…
Mikołaj Świątek 00:15:55 Sure.
Tyler Helmuth 00:15:57 Go ahead, Nikolaj.
Mikołaj Świątek 00:15:59 I just want to remark the Prometheus. The Prometheus stuff, I think, just… The problem there isn't upgrades. Prometheus is largely stable.
jea 00:16:12 Sorry.
Mikołaj Świątek 00:16:12 that presumably.
jea 00:16:13 Referring to the problem that we had, like, 3 years ago with the label map stuff.
Mikołaj Świątek 00:16:18 Yeah, right.
And… I also wanted to say that… It's unfortunate that Pavel isn't here because he's the author of the instrumentation.
jea 00:16:38 Yeah.
Mikołaj Świątek 00:16:39 Data, RFC.
I am… open to fixing the instrumentation.
image release problem, let's call it.
I'm also open, because I recently did an experiment with the injector, and that experiment just basically worked.
The only problem, all of our tests, everything just works fine if we replace what we're doing with the injector inside of our images right now.
No problem.
The only problem I run into is that they don't have builds for some of the architectures that we support. And I think there's a pull request by Antoine to fix that right now.
jea 00:17:23 Yeah, I can maybe go review that actually right now.
Mikołaj Świątek 00:17:27 Assuming it actually builds.
jea 00:17:30 I think it did. Let's see…
Mikołaj Świątek 00:17:34 We might want to, and the injector might want to as well do some kind of platform support tiering.
The same way the collector does. To just make clear that, like, I don't know, I don't know if our S390X images work. I have no clue. They build.
Right?
I don't have any way of testing it. I'm assuming the people at IBM who contributed them originally are doing something.
with them. But I don't know. So it would be nice to — now that we also have structured documentation, it's much easier to just create a new document or add to the support.md.
jea 00:18:18 Yes.
Mikołaj Świątek 00:18:19 whatever it's called, and just say, hey, you know, on AMD and on ARM, you're good, and on, like, S390X and PowerPC or whatever, you're kind of on your own, we just build the binaries that they build.
And that's it. We can just literally copy the same language that the collector has.
but going back to the going back to the instrumentation images, I will happily adopt the injector, and I will also happily solve another problem that we have.
Involving this, where there's no… actual spec for what the images should contain, if somebody wants to build their own.
They have to go and look into our Docker images.
Tyler Helmuth 00:19:12 Sounds good.
Mikołaj Świątek 00:19:13 Yeah, yeah. And we can just standardize on the injector. We can just say.
you know, if you want the .NET image, you just… you know, you build your… you build your, you build your image, and then you have to have the artifact under this environment variable that is already defined by the injector.
And that's it.
And then the only thing the operator does is it, like, takes the injector and, and and and and runs it, you know, sticks it in Ld. Preload as is the.
jea 00:19:49 I mean, Mikko, what we could say is that for users on S390X and S390X, PVC64 is we just told them to build their own injector.
I don't know who's using those, and we could just say that we don't want to… the injector, it seems like, Michelle doesn't want to support that in the injector because we can't, we don't have runners that can test that.
Which I think makes sense, like, we don't want to distribute something that we can'.
Mikołaj Świątek 00:20:19 The operator does.
jea 00:20:22 We do. We have runners for this.
Mikołaj Świątek 00:20:24 We don'.
Tyler Helmuth 00:20:25 No, we'll be admitted on the test.
Mikołaj Świątek 00:20:28 We distribute the binaries. We also distribute instrumentation images for those.
jea 00:20:32 Yeah, but I think we should just say that if you want to use the newer version, given that we're recommending that we're not going to Like, we are not going to support.
Like, we are not going to automate this version thing for you anymore. If you want to run a… One of these other architectures, you should build your own image for it.
And then we just call that.
Mikołaj Świątek 00:20:56 We will. So we'd just drop, drop the drop support for those architectures.
In the…
jea 00:21:04 I think essentially, yeah.
Mikołaj Świątek 00:21:06 Because that's what it comes up. I also had a conversation with Antoine about this on Slack. And he said that the injector is kind of leaning towards — Saying that we should just.
Because I asked him if we can have, like, an official Docker image from the injector, and he said that it's better if we just ship it with our own… with the instrumentation images that we have.
Which I am okay with, but that means that we can only support the architectures that the injector supports.
jea 00:21:39 That's… Fine.
Oh, that's good.
Mikołaj Świątek 00:21:44 It's like 2 megabytes. So I'm not concerned about the additional size.
jea 00:21:49 There is a Docker file. Why don't we release an image for this? Because there is a Docker file in here Do we just say that people have built it themselves?
What does Dash Zero do?
Mikołaj Świątek 00:22:01 I think that 0 just ships a single image of everything.
So they don't have any need to ship their intake. Yeah.
Tyler Helmuth 00:22:11 For instrumentation V1 beta.
Are we planning to use the OTEL injector, or are we going to continue to use the auto instrument page?
Mikołaj Świątek 00:22:20 These are independent. Using the injector is like for the existing instrumentation images, which is what the V1 beta 1 deals with.
This is an implementation detail.
Tyler Helmuth 00:22:35 Okay, okay, cool.
Mikołaj Świątek 00:22:36 In fact, you can decide at runtime which method you want to use if you've shipped the injector with the image. So this is not blocking, but the default image required or not is blocking. We can actually deal with this in the conversion webhook. We've decided there's going to be a conversion webhook. There's no other choice.
It's the.
Tyler Helmuth 00:22:59 We talked about that, I remember.
Mikołaj Świątek 00:23:00 Yes, yes.
jea 00:23:01 So sad.
Mikołaj Świątek 00:23:02 We can't. Unfortunately, Kubernetes stops us. I thought we could support both versions at once with different controllers or something.
Tyler Helmuth 00:23:11 Yeah, okay.
Mikołaj Świątek 00:23:11 You cannot. You have to serve one of them. And serving one of them.
Tyler Helmuth 00:23:15 Process.
Mikołaj Świątek 00:23:16 The way it works is that — or no, the problem isn't that you can serve. You can serve both. The problem is that you have to store one.
Tyler Helmuth 00:23:25 Hmmm.
Mikołaj Świątek 00:23:25 And because you store one, the API server has to have a way to convert one to the other.
There's no way to keep too, like, too physical, you know, too serialized.
versions of the same CI.
Tyler Helmuth 00:23:46 You know?
Mikołaj Świątek 00:23:47 Central in XD.
Tyler Helmuth 00:23:50 Unfortunate, but that's fine. So for the problem, the blocking project being the instrumentation CR requiring a default image.
Do we… what's the status of the packages, Sig? Because I know that we are kind of sick of publishing our own images for stuff, and we would love to just use everyone else's images like we do for .NET and Java, but I'm guessing we're not going to wait V1 and V1 beta 1 for instrumentation is not going to wait for the packages SIG, right?
Mikołaj Świątek 00:24:24 No, and, like, for .NET, we still, for both .NET and Java, we, we publish our own images as the operator project. It's just that those images, like, have very little of our own opinions inside them, basically.
Tyler Helmuth 00:24:39 Do we do we republish the?
Because I know we have, like, an automated process for bumping a version.
Mikołaj Świątek 00:24:46 Oh, yeah.
Tyler Helmuth 00:24:47 We do have our own Docker file.
Mikołaj Świątek 00:24:49 I don't, is there an upstream Docker file?
For this?
Tyler Helmuth 00:24:55 Alright.
Mikołaj Świątek 00:24:56 I'm not aware, I'm not aware, like, I'm not aware of any that exist, but I'm not gonna complain too much. Like, at this point, at the very least, the Docker… the .NET image, at least, is code-owned by the .NET maintainers, so at least that's done. I don't… I'm not gonna fight too much of a fight right now, and I don't want to, like… if the… If the V1 beta 1 instrumentation is going to get blocked by trying to make other SIGs take responsibility for these images, we're going to be here until at least six months.
So…
Tyler Helmuth 00:25:34 So for our own — for unblocking ourselves then, it sounds like we're going to stick with our process. We just need to mature our process in order to feel good about dropping it.
Mikołaj Świątek 00:25:46 I would even say that we should start by just documenting this.
Like, write the other document that says, here are the instrumentation images.
Yeah, and because I think the very minimum, the very minimum.
requirement for us to be able to say set your own image user is to just have documentation telling them where they can figure out what images exist and what's in them.
Tyler Helmuth 00:26:14 Yeah, okay Okay.
Is it a… I don't know what our project planning process is at the moment, and I'll go back because Pablo's not here, but is there, like.
a main issue or something that I can attach.
Mikołaj Świątek 00:26:30 There is a milestone.
Tyler Helmuth 00:26:31 52552, a milestone, too.
Mikołaj Świątek 00:26:34 I believe there's a milestone.
Tyler Helmuth 00:26:37 Am I allowed to attach this to instrumentation V1 beta 1?
Mikołaj Świątek 00:26:42 Yes, I well, I don't. I I guess that's a matter of opinions. In my opinion. Yes.
Tyler Helmuth 00:26:48 OK, I will comment on the issue of the discussion we had today. I will ping Pavel. Do you know Pavel is on PTO right now? Is that why he's not at the meeting?
jea 00:26:59 It is European summer, so I assume that he is out hiking a mountain in Switzerland.
Tyler Helmuth 00:27:04 Yeah, so I'll ping him, I'll ping him, and I'll put our discussion on this issue, that we want to do this, and I will write up a plan for kind of, like, the requirements in order to do this, and then I also commit to, like, working on those. Now, I will not be here for the next two weeks, so my commitment to that is committing in August. I don't know what the timeline is for V1 Beta 1.
Mikołaj Świątek 00:27:30 I don't think it's gonna happen before it's gonna happen that quickly. So that's probably fine.
jea 00:27:35 And so, Mikhail, I want to go back to what you're saying about the PR that you have open for the injector.
Mikołaj Świątek 00:27:42 I don't have a PR open. I have a local branch, which I…
jea 00:27:45 Local branch you have.
Mikołaj Świątek 00:27:46 My local branch, yeah, which was actually like a — I wonder how good CloudFable is at autonomous tasks.
jea 00:27:55 Yes.
Mikołaj Świątek 00:27:55 Origin of.
jea 00:27:56 Because I'd like to see what it did, at least. I mean, I'd like to merge it. It'd be good if we could start using the in And we could just start with this path where we just say, you know, we don't have injector support for these architectures. And if you're on these architectures, you have to go build the injector yourself. I think that that's reasonable.
But I'd like to just start using it Sooner rather than later.
Mikołaj Świątek 00:28:21 There might, because the way I have it done is by using a feature flag.
There might be a way to, under that feature flag, say something like… Is the injector on disk? If the injector is on disk, then use it. If not, fall back to the previous one. I kind of don't like that idea because I'd like the codes to be simpler rather than more complicated.
jea 00:28:46 Yup.
Mikołaj Świątek 00:28:47 But it is kind of a problem, right? Because right now, we have to do a breaking change, right? We have to say, we no longer support — these images, which is why I would have really liked for the… because the simplest solution to this problem is for the injector to just build this and say, this is tear-free, we just build it, we don't test it.
And that will be exactly the same status as the operator's instrumentation images for these architectures. We build this. It builds. We don't test it. Good luck.
And I think eventually, eventually, like, the injector will actually need to do something like this anyway, because there's, like, some convergence about, in general, which architectures hotel as a project supports, and in what way? Like, for example, the AIX support for the auto collector is, I think, actually, like, near-ish?
Like, a lot of it actually does work right now.
So even if you say no right now, you might have to say no, say yes, or be pressured to say yes in the future.
jea 00:29:57 if we move to this path where, you know, the user has to specify the image, this matters less, right? I mean, it'd be more annoying for the users that are on these architectures, but… We could just say… You know, if you want to use the injector, you have to supply the injector image and then we use that. And then this is what you do to do that.
Mikołaj Świątek 00:30:16 But the problem is that for me, I don't want to keep the split of injector and non-injector indefinitely. I want to say, this is a feature flag. And I am very — if there's no complaints, once it's enabled by default, I want to very rapidly just delete the — Option with no injector, and keep injector as the only canonical.
jea 00:30:39 Yo.
Mikołaj Świątek 00:30:39 Way of doing this.
Is that what it's really.
Tyler Helmuth 00:30:42 that instrumentation code.
That we have.
Mikołaj Świątek 00:30:46 Am I getting.
Tyler Helmuth 00:30:46 or… What do we get by using the OTEL injector? What does it let us stop doing ourselves?
Mikołaj Świątek 00:30:57 All of the…
jea 00:30:58 environment, like…
Tyler Helmuth 00:30:59 that bar.
jea 00:30:59 Excellent.
Tyler Helmuth 00:31:00 Okay.
jea 00:31:00 Yeah, that's one of the big things. And then also the copying of… the… Packages.
Like needing to do CP and there's one more thing that I'm forgetting. Yeah.
Tyler Helmuth 00:31:15 All that infinite container stuff.
jea 00:31:18 We'd still need an init container for now.
Mikołaj Świątek 00:31:21 We have to copy the thing because it has to like, the actual artifacts need to be available to the main pod, which means we have to copy them to like a shared volume.
Right, to be able to do that. So it doesn't save us from that. What it does save us from is from setting a bunch of, like, platform-specific environment variables.
And it also fixes the problem where the user, for example, has to know whether they're running Muzzle or libc, if they're using Python or .NET, for example, because the injector actually Notes.
jea 00:31:55 Well, the injector just copies everything. It just moves it all over.
It just says, oh, you're… you have these things, let me move these to these places.
Mikołaj Świątek 00:32:08 I don't know what you're talking about, Trey.
jea 00:32:11 That's fine.
I'm split brain currently, so that's all right.
Mikołaj Świątek 00:32:17 From my perspective, the injector is just like an LD preload hook that we set LD preload equals injector. And then we maybe set one other environment variable that tells the injector where the instrumentation binary is.
And that's the extent of our use of it. But yes, you could — again, it is actually able to tell at runtime whether something is like Muzzle or Ellipsee.
Which is actually quite, quite a nice feature. So it doesn't simplify that much for us, but it kind of removes The need for us to even think about this problem, essentially.
jea 00:33:01 Yeah.
Mikołaj Świątek 00:33:02 Which is, I think, a big win. I mean, it's a big win for the operator project. It's not a big win for the injector project, to which we're going to send all of the users complaining that something is broken in there.
And.
But that's the idea, essentially.
and then I would… it will also, like, at it will also kind of solve another problem we have, where people want to do PHP instrumentation, someone wanted to do Ruby in the past, and explaining to them what they actually need to do and how it needs to work is quite a lot of work, whereas we'll be able to say.
You need to add support for this to the auto injector, and then we will accept that it's going to be simple for us.
Tyler Helmuth 00:33:50 Mmhm.
Mikołaj Świątek 00:33:53 Because right now, again, this is just the Wild West. We have a PHP image published, which was a big mistake.
And that… We should delete it.
Probably. I don't want to delete things which were already published, but we never advertised that we published it, so maybe it's fine.
Tyler Helmuth 00:34:09 You can't do anything with it. Well, I guess you can, not with the operator. I guess you could go do your own stuff with it. It is technically published.
Mikołaj Świątek 00:34:17 Yeah, yeah, but like, if you look at the build process for that thing, it's like…
Tyler Helmuth 00:34:21 Yeah, I.
Mikołaj Świątek 00:34:22 I don't want to own this stuff, man. I don't want to, I don't want to think, I don't want to think about Oh.
Go… but yeah, going back to the… going back to the view on Beta one and the required you know, and the image definitions. Yeah, essentially, what I think needs to happen is, A, there needs to be the documentation saying how to get there. You don't have to wait for U1Beta1, any of that. You can just add the documentation as it is.
and And the other thing is, how does the… release process work exactly? And we can actually talk about that right now, if you want. I'm not sure if this is, like, a high-impact discussion, necessarily. Anything… But I would be… I would accept a process that's very similar To the home charts.
Tyler Helmuth 00:35:14 where…
Mikołaj Świątek 00:35:15 like, this is a simple enough artifact that you can say when a change is made to any of the things that affect this artifact, we publish a new version, and then it's just a question of what, how, how are we versioning things? And I think I think we should just kind of… Because we should just pattern ourselves over, like, what Linux distributions do for packages, right? Where they just, like, pick the upstream version, do a dash something, and that's it.
Where you're gonna see, like, you know, something, something, something dash Ubuntu 3.
Tyler Helmuth 00:35:56 Mmhm.
Mikołaj Świątek 00:35:56 R are just, like, dash number.
That's,
Tyler Helmuth 00:36:00 Ours would be, like… Well, let me think. So for the Java one, we have an upstream. I guess we have an upstream version for every single version for every single instrumentation we release.
Mikołaj Świątek 00:36:15 Mmh.
Tyler Helmuth 00:36:15 Like, Java is, like, 2 point something, it's, like.
Mikołaj Świątek 00:36:18 The… This is our already…
Tyler Helmuth 00:36:22 Same, and then Python is, like, if I scroll down to the bottom of our… Release notes, we have our weird versioning.
Python is like… I'd… commit version, right? So, Are you… are you thinking we need to standardize our versioning for the images?
So, like, instead of using Python v0.commit Shock. We would… Have some sort of December that we would get.
Mikołaj Świątek 00:36:56 Do it.
Tyler Helmuth 00:36:57 You wouldn't.
Mikołaj Świątek 00:36:58 Wait, wait, wait, wait. Is that how Python is? Maybe that's It's Python V064B0 is what I see.
Tyler Helmuth 00:37:06 It's, when I look at the Python one, the release that we're pinned to is version 1.4 3.0.
slash 0.64B0.
Mikołaj Świątek 00:37:23 yeah, okay. So there's no comment hash in there. It's just,
Tyler Helmuth 00:37:28 Not a commit hash. I think that's technically the beginning of a commit hash.
Mikołaj Świątek 00:37:33 Yeah, OK. But yeah, this is mostly fine, I think. It's fine to just take the existing version in there. And these versions are literally just a version of what is, in some sense, the main SDK package.
Tyler Helmuth 00:37:50 Yeah.
Mikołaj Świątek 00:37:51 That's it.
So… it's fine to keep these.
I think that's, like, very simple, very easy for users to understand.
And then we just need to be able to add something at the end to indicate that we're building something with the same version of the SDK, but also something else changed in the image. An example of that might be, for example, if we need to stick a new injector version in there.
Tyler Helmuth 00:38:19 Yeah.
Mikołaj Świątek 00:38:20 Or…
Tyler Helmuth 00:38:20 So in case we need to change something off our own build process, we have to do another release. We can't be only tied to their version, because…
Mikołaj Świątek 00:38:27 Yes, yes, we might have to, like, change the base image, for example, because there's, like, some serious CVE, and everybody's complaining that their scanners are, you know, sounding an alarm. So, in that case, it would be much nicer to bump the base image, and then… you know, issue a new release with the thing. That's how I would think about this.
I am not really sure whether we want a release, as in GitHub release.
Tyler Helmuth 00:38:56 Each of.
Mikołaj Świątek 00:38:57 Because it's, like, a lot of spam, essentially.
Tyler Helmuth 00:39:00 So, it would be a lot of spam, and it… But that does — on one hand, it's a lot of spam. On the other hand, it does help with the discoverability. It does.
Mikołaj Świątek 00:39:14 But I will say that.
Tyler Helmuth 00:39:16 Yeah, there's no grouping in… there's no grouping in GitHub releases, is there? It'.
Mikołaj Świątek 00:39:22 Whenever I'm in a repository that publishes a lot of packages from a single repository, the releases page is completely useless.
Tyler Helmuth 00:39:30 Yeah.
Mikołaj Świątek 00:39:31 It's impossible to find there, but it's like, might still be, it might still be okay.
Like, it might still be, because you know what's useful? Useful is… can you actually do that? Can you set multiple releases as latest?
Tyler Helmuth 00:39:45 I don't think so.
Mikołaj Świątek 00:39:46 Yeah, so that's useless.
Tyler Helmuth 00:39:48 But what we could do is we could.
Never set… a image release as latest, because that would just be an option when you're creating the release. So we could make a release in the list, but not set it as latest.
Mikołaj Świątek 00:40:08 Yeah, something like this. Like, I am… I'm ambivalent as to whether we need releases. I do think that what we should have is, like, better descriptions on the package pages themselves.
And we only publish these into GHCR, if I'm right.
Let's see if I'm actually right.
Tyler Helmuth 00:40:30 I'd be shocked if we're pushing.
Mikołaj Świątek 00:40:33 I would also be shocked, but sometimes I am shocked.
Tyler Helmuth 00:40:36 Hahaha.
Mikołaj Świątek 00:40:44 We do log into Docker I.O.
Tyler Helmuth 00:40:50 Okay, I guess I need to go look at Dock.
Mikołaj Świątek 00:40:58 Auto slash auto instrumentation Java. Docker, Docker.
Tyler Helmuth 00:41:03 That one is in… that one's in Docker Hub I see it.
Mikołaj Świątek 00:41:07 Okay.
OK, so that's two places where it would be nice to have a description.
Tyler Helmuth 00:41:13 All of our other… I was wrong. They all go. They all go to Docker Hub.
Or at least Node.js.NET, Python, J I see, I'll go there.
Mikołaj Świątek 00:41:27 Yeah, and this is… This just goes to the readme, which is largely fine. We could have a little bit more of a description in here, but that's cool. This is reasonable enough, I would say. So if somebody wants to know what versions are published, they can go into Docker Hub and just scroll through it.
I don't know why there is a tag called true in here, but it probably should go away.
But this is… I think this is pretty alright.
Overall.
Tyler Helmuth 00:42:02 Where did the overview, where did the… I wonder where these get set from.
like, when I'm in Docker Hub and I'm looking at the overview, who's… who decided that this was the I wonder what's pulling that Or if it's just, like, one of our Docker admins came in here and was able to.
Mikołaj Świątek 00:42:20 The most likely answer is it's just whenever it was created, somebody put something in there that was just… given.
Tyler Helmuth 00:42:30 I'm gonna take a note.
Mikołaj Świątek 00:42:32 You know, at the time.
Wouldn't be bad to update.
Tyler Helmuth 00:42:39 shows.
Mikołaj Świątek 00:42:40 Notably, the package in GHCR just has our normal readme in there, which is not really ideal, I would say.
Tyler Helmuth 00:42:50 Yeah.
Agreed.
Yeah.
Although I don't know if we can control that pack that.
Mikołaj Świątek 00:43:00 Should be some way.
Tyler Helmuth 00:43:03 Yeah, maybe when you… I'll have to look into that. My guess is that it's pulling our README because it knows that this image was pushed from our repo, but I'll have to look into how… JCR works.
Mikołaj Świątek 00:43:15 It's possible. There's, like… I am… unfortunately, I know more about this now than I did a year ago, and there is, like, some magic label… some label magic going on in there, where you, like, put something in your Docker In your in the labels on your image and based on that GHCR infers certain things and then puts it in. Okay.
Tyler Helmuth 00:43:38 I can look into that, too. We can make that one of the things that we would we should do.
Okay.
And that's, like.
Mikołaj Świątek 00:43:46 I don.
Tyler Helmuth 00:43:46 So…
Mikołaj Świątek 00:43:47 No.
Tyler Helmuth 00:43:48 amount of things. On top of what's already defined in the issue, like, I think the idea of auto, like… I like the idea of, like, templating parts of the README, so, like, if you're copying and pasting The latest image, so that the burden isn't on the customer.
Or the user, I mean. So, yeah, that… these are in addition to some of the other things that Jack laid out in the issue, I think.
Mikołaj Świątek 00:44:15 Yeah, although I would, in your position, I would, like, tag Pavel in the operator's Slack channel.
Tyler Helmuth 00:44:23 Yeah, I'll be tagging Hubble.
Mikołaj Świątek 00:44:25 as well.
Tyler Helmuth 00:44:27 Yep, and it's all based on… yeah.
Full approvals from all maintainers.
Mikołaj Świątek 00:44:35 Yeah, I think this is good. I thought that we didn't really want to block on this, but if you're going to come in and just do it, essentially out of band.
of…
Tyler Helmuth 00:44:45 Yeah, I mean, I.
Mikołaj Świątek 00:44:46 on that.
Tyler Helmuth 00:44:48 I can help. I'm gonna… I'm gonna approve her. I've done very little for a while. I can come back and help with instrumentation again.
It's the thing in the operator I understand the best, so…
Mikołaj Świątek 00:44:59 It's good, it's good. Oh, actually, Jacob, how's.
jea 00:45:04 Well, it sounds like you already did it.
Tyler Helmuth 00:45:07 That refactor's been going on for a.
Mikołaj Świątek 00:45:09 Just a small, just a small bit. Just a very, very small bit. I thought you wanted to refactor all the other parts which are in compression.
jea 00:45:16 I know, I was… so it's funny, because I'.
Tyler Helmuth 00:45:18 comprehensible.
jea 00:45:19 And then the day that I was going to do it, I was, like, on a train, and I was… finally got access to Fable, and I was like, okay, I know exactly the architecture that I want. I'd, like, written it down, and then, Fable got pulled.
And so it's like, damn, like, now I have to do this by hand? So I did it by hand, and then I hated what I wrote.
Sure.
Every time that I do it, it just gets worse. That's the thing, is that the code itself is just really… Like confusing and terrible and I just hate it like I think we should just this is why I would just want to use the injector and get rid of this.
Because…
Mikołaj Świątek 00:45:54 Thank you.
I thought the thing that you hated was the stuff that lives above the injector. It's the stuff that, like, sets things like resource attributes by the environment variable and so on.
Because the injection stop us from doesn't help us with that.
jea 00:46:11 No, the injector does help us with that because we're going to change the, by doing the V1 beta one stuff that we're doing, it gets rid of that because we're not doing the, we're moving to declarative config and we're just not going to do that stuff automatically.
Right.
That's my understanding of it.
Tyler Helmuth 00:46:29 Declarative config helps a lot, that's for sure.
jea 00:46:32 And I think the idea is that like we, it's really my problem with it is the fact that we can just set environment in like five different ways today. And it's the like precedence that's really bad. Also, it's the actual injection code that's bad because we have to move things to the right place. That's what the injector solves that we're going to get rid of.
It's that we have a bunch of, like, duplication between Each of the languages while also having these like really specific hacks.
To get them in just the right place.
And that's also frustrating, but that, that is something that the injector does solve.
Mikołaj Świątek 00:47:10 Well, we still have to copy it, right? It's like in.
jea 00:47:13 Yeah, but it's just one copy, rather than needing to do, like, 6 different types of copies, and, like, piping in the right… environment variables, and then having to deal with the… if somebody already said it, or remember the problem that Pavel had, where somebody was like, hey, can you just read my config map for Java? It's like, no, we're not going to read your config maps. Like, we shouldn't have permissions to do that, you know?
Mikołaj Świątek 00:47:37 That is something that the injector does solve, yes.
jea 00:47:41 Yeah, so all of that is going to go away. I think that we should do the change that you have and just delete the old stuff and be done with it.
After Pavel finishes the V1 Beta 1 stuff. I think that…
Mikołaj Świątek 00:47:55 So, yeah.
jea 00:47:57 I think they're trying to like I'm going to, maybe this is not the right phrase, but put lipstick on a, on a dead horse and combining two of them because they're both bad. It's like.
This is a, it just doesn't… it's not right. You know, we should just get rid of it.
Mikołaj Świątek 00:48:21 I'm.
Tyler Helmuth 00:48:21 Question.
Mikołaj Świątek 00:48:22 I can submit my change. I think it's relatively clean-ish, and it was just surprisingly simple. I expected to face a lot of problems along the way, but it just really didn't. It just works.
Tyler?
Tyler Helmuth 00:48:41 Yeah, I was gonna actually ask a separate question outside of the… injector.
Umm.
One thing I know that… The CAVES injection controller that Jack is working on does differently from our operator is — It doesn't require… Like, an annotation on the pods?
that want instrumentation. Instead, it's, like, it's set up to be, like, any pod that Has these annotations we'll inject, so, like, it means that users don't have to go update their… update their deployment, definitions?
Is that something that we would be willing to take on in that type of a feature? Is that something that we would take on in the operator?
Mikołaj Świątek 00:49:30 We even have an existing issue and even like an open pull request that's stalled that tried to add something like this. The actual shape of, sorry.
jea 00:49:39 We did have an open issue for this that we wanted to do. But annotations are fundamentally the wrong abstraction here, which is why we shouldn't use them for this problem.
Tyler Helmuth 00:49:50 Okay.
jea 00:49:50 Sure. Yeah. But —.
Tyler Helmuth 00:49:53 for.
jea 00:49:54 We, we can do, there's a proposal that I think we're going to close. It's going to be automatically closed soon, which probably should be for the issues called instrumentation support select.
And that's what Jack is proposing. And I think we should support that as well.
Okay, yeah.
Tyler Helmuth 00:50:13 Yeah, like, more… like, selector would be, like, more complex set of rules, more than.
jea 00:50:17 Yeah. T.
Tyler Helmuth 00:50:18 table or something? Okay, yeah.
Mikołaj Świątek 00:50:19 It's.
jea 00:50:19 No, no, it would be a label selector.
Tyler Helmuth 00:50:22 Oh, wait, let's.
Mikołaj Świątek 00:50:23 I don't know if you want to necessarily — label selector is one implementation of this that's really very Kubernetes native. But I don't think we're married to anything, to any specific format of this. But the general concept of — kind of inverting where this is controlled from, because right now the pod controls whether it's instrumented or not by putting an annotation on itself. And the idea here is to invert that and control it from the instrumentation object.
In some way, right? Yeah. Yeah, somewhere. Yeah, we are open to this for a long while. Okay. Conceptually, it's already accepted for a while. It's just that the person who was working on it kind of, I think, lost interest.
midway, because it's a pretty big feature, and you have to do a bunch of, like, spec work ahead of time to… to actually, like, get it in. But yeah, sure, if you have, like… if… maybe the Dash0 folks have, like, a working implementation of this. It would help to see it, because I've seen what Jack wants to propose, and it sounds quite complex. I'm not… I haven't looked deeply.
Tyler Helmuth 00:51:37 I haven't looked deep into the implementation details of the CAIDS injection controller yet, but I can.
Mikołaj Świątek 00:51:44 It's.
Tyler Helmuth 00:51:44 Yeah, I'm just trying to g.
Mikołaj Świątek 00:51:46 Oh.
Tyler Helmuth 00:51:46 I think in August, I guess not just in August, like, I've got… I have some time, I guess, to, like, figure out what I… what is the best thing to work on right now, and this operator stuff could be a good… a good fit, so… I know I want to get the instrumentation V1… help get instrumentation V1 beta out.
Especially with the thing we just talked about on the agenda, but this could be, like, a second thing I do later.
Like, I would commit to helping.
this inversion.
jea 00:52:25 That would be great. I definitely would appreciate the assistance because I'm pretty like.
At my limit in terms of things that I have currently taken on because my like policies thing just got merged and we're about to do a bunch of work there.
And I need to focus on that. There will be like an operator part of that as well, but that's kind of like a later thing. The collector is the first part of it.
Once the collector has it.
Tyler Helmuth 00:52:52 start touching… if I start helping out more with the bridge as well,
jea 00:52:57 Oh, that'd be.
Tyler Helmuth 00:52:58 Grafana's fleet management wants to support Kubernetes. And you can either build a supervisor that has a collector in it in one image, which is something I've done in the past, which is kind of hard.
Or you can use the bridge, or maybe we make the collector be its own op-app client. That's what I really want to do. I want the collector to just… have an embedded OpAmp client, like the BindPlane distro.
But we're not there.
jea 00:53:26 Yeah, I mean, there's some other concern that I brought up with the… the people that do that. Like, I brought that stuff attached here. Everybody… this is my own, like, hill to die on, but I think that it's wrong to do, like, remote config Like that within the collector process in Kubernetes.
Because you're restarting the process, you're not restarting A subcomponent, which is a different thing.
And it's dangerous.
I can explain.
Tyler Helmuth 00:54:00 But that's okay.
jea 00:54:01 That's fine. I don't know why I.
Tyler Helmuth 00:54:03 But that's fine.
jea 00:54:04 The issue is that when I was at LightStep, I did this for a bit, and we had a really annoying But… Like incident where, because.
One collector got the new config version, the other one didn't, but they still were the same. They're still part of the same replica set. You have this telemetry issue where they both are reporting.
That they are the same, configuration, like the same, process.
But they're running two different configs, which is bad.
Tyler Helmuth 00:54:41 Yes.
Does that… does that… Does the op amp concept of effective config not?
solve that problem.
jea 00:54:50 It doesn't.
Tyler Helmuth 00:54:51 See.
jea 00:54:52 It's not part of the collectors.
Telemetry, and it's not part of what would be tagged on the collector's, like, Kubernetes telemetry.
Right, because the…
Tyler Helmuth 00:55:03 You're adding, like, a config map hash or something to your outgoing telemetry?
jea 00:55:09 You wouldn't be doing, it would be on the, there'd be a label on the pod for the config hash that it's running and that wouldn't change.
Tyler Helmuth 00:55:18 That wouldn't change, correct.
jea 00:55:20 Yes.
Tyler Helmuth 00:55:20 Yeah.
I mean, I think in… if I was gonna do remote config with… in Kubernetes, I wouldn't even want a config map. I would want it to all come from The remote.
jea 00:55:35 Yeah, that which I think is all is more reasonable, but.
Mikołaj Świątek 00:55:39 I, I really, I really don't…
Tyler Helmuth 00:55:41 Okay.
Mikołaj Świątek 00:55:41 I really don't think that's, like, a good idea in a platform where you can't… or it's a good idea if you can, like, put a, stable identity to each of your collectors, and force them to have, like, a local volume, and so on, but other than that, I have no idea how you'd track identity at all in that kind of setup.
Which is why I kind of feel like.
Tyler Helmuth 00:56:04 Specifically.
Mikołaj Świątek 00:56:05 Well, the problem is kind of that everything in Kubernetes is stateless by default.
jea 00:56:11 Yes.
Mikołaj Świątek 00:56:12 It's If you do the bridge, then your state, such as it is, your way of tracking collector identity lives in the CRs.
That are created by the bridge. So you have some way of, like, associating things to another. If you just start a collector pod somewhere, and that collector pod just talks to a remote, and gets some config, and that's it.
it gets restarted, like, you have a new one, right? Is that okay? Maybe it's okay, maybe not. Maybe if it's in a daemon set, you can take the identity from the node you're on.
But it's all kind of like it's like a confluence of hacks for different special cases, essentially. And if you want like a general general solution to this problem.
Then you need some way of telling what a given collector is.
In… in some way. And… I don't know.
Tyler Helmuth 00:57:11 I guess in the past, when the pod cycled, like, the op-amp server.
would drop that agent ID, and when the pod came back up, it got a new agent ID, which…
Mikołaj Świątek 00:57:23 You're okay.
Tyler Helmuth 00:57:24 Your telemetry is… Yeah, I mean, in the telemetry, what you see is, like, the pod died, the pod came back up, you've got a new.
Mikołaj Świątek 00:57:33 The problem in general is that in Kubernetes, unlike — because the OpAmp model directly makes sense if you have a collector running on a host, and that's it.
But in the Kubernetes world, where you often have replicas of something running, like we have a replicated service running, it makes more sense to say to key of the identity of the whole service than the identities of the replicas. And that's like, I think, a big problem.
with a lot of the stuff that happens. If you have a gateway collector that you're controlling for uphamp, it's gonna have a bunch of replicas, as gateways often do, and like one of them disappears. Another one appears. You really want, like, have a new thing to appear on your in your like, you know, fleet Ui.
your remote management UI, in that case. You kind of have to, even if you do that, I think you have to, you need to have some way of being Kubernetes native and, like, acknowledging that these things are all the same. Like, these things are part of a logical unit that has the same configuration. OpAmp by itself doesn't really let you do that.
Tyler Helmuth 00:58:44 You have no concept of that, yeah.
Mikołaj Świątek 00:58:46 Yeah, they they the and and even like, not even a sense, not even like on a conceptual level.
You have no guarantee that all of those collectors actually have the same configuration in principle, right? Because if you're only using OpAmp, even if you tell all of them to use the same, right? If you configure it, they might actually have different ones just because of like kind of general distributed system consistency problem.
Tyler Helmuth 00:59:11 I see what you're saying about the replica set. When I've done this in the past.
We like that, thinking about everything in the replica set as the top-level object.
wasn't something that I had considered. Like, because OpAmp cares only about, essentially, the pod.
Like, we… of course, you had a replica set, we could spin up 500 pods. Each one of those pods was just an agent in the op-amp sense.
And our effective config — like, the effective config was how we determined whether or not — and some of the, like.
Mikołaj Świątek 00:59:45 It would…
Tyler Helmuth 00:59:46 status responses and stuff built into OpAmpSpec, or how we determined if all 500 of the agents in that deployment had received the Remote Config.
And so we were able to track… we were able to track each one of those agents individually, I don't… I don't… we didn't have any problems with that.
Mikołaj Świątek 01:00:11 If it works.
Tyler Helmuth 01:00:12 We were either.
Mikołaj Świątek 01:00:12 Yeah, I'm.
Tyler Helmuth 01:00:13 We were using supervisor — we were using a container image that contained the supervisor and a collector in the same image.
Mikołaj Świątek 01:00:21 Mmh.
Tyler Helmuth 01:00:21 two processes running in the same engine, which is its own problem in Kubernetes, because all of a sudden, health checks don't work, because how do you know which services? So that's bad.
But, like, the way that…
jea 01:00:34 Taxed a lot of them. Yeah.
Tyler Helmuth 01:00:36 The bind plane solution of having a wrapper around OTel coal so that it can call dot run and dot stop.
And then…
jea 01:00:45 Oh, I gotta jump to my next meeting, so I.
Tyler Helmuth 01:00:47 I don't know. If this is an interesting conversation, I might be helping out with the op amp bridge. That's.
jea 01:00:51 Tyler, I'd love to get you up to speed with that, and then… Let's maybe continue chatting about instrumentation in the channel, Nikolai, if you want.
Mikołaj Świątek 01:01:01 Yeah, yeah.
You could — if you're interested in the bridge, Tyler, you can start by reviewing a PR that implements restarts.
Tyler Helmuth 01:01:10 I'm not comm.
jea 01:01:11 Oh, I started reading that.
Tyler Helmuth 01:01:14 August, I will review Operator.
jea 01:01:16 Bye guys.
Tyler Helmuth 01:01:16 in August. So, yeah.
Mikołaj Świątek 01:01:19 See ya.
