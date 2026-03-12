SIG: Kubernetes Operator SIG
Date: 2026-02-26
Duration: 61 minutes
Zoom Recording URL: https://zoom.us/rec/share/T7SVYxaIbUGi9WYqQSjdtQc8Et93C8Q9BDQ2QtgQZEVLUGJIpHQBEkURs4ZTCpf-.05OhqkC8EeqlHImK
============================================================

## Zoom Recording Transcript

jea 00:02:21 Hello?
Anton, do you kick the butt?
Kai L 00:02:33 Hello, hello.
atoulme 00:02:35 I think I just did. I don't know what this thing is, but I don't want that. I don't want that.
Like, you… you can watch the recording by yourself, needles.
jea 00:02:46 and Nikolai.
atoulme 00:02:48 I don't know who that is.
jea 00:02:50 That is not the Bogdan that I know.
atoulme 00:02:54 I know at least a couple Bogdans at this point. One is a triager, on contrary, but another one is a maintainer.
jea 00:03:01 Well, there's Bogdan Drutto. Who's the, other one.
atoulme 00:03:06 Bogdan's tensu.
jea 00:03:07 Bogged down to, that's what I was thinking of.
This was neither of them.
atoulme 00:03:14 No, I don't know that person. Hey, David. Hey, Kai. Sorry, we're just getting started, we, If you have anything you'd like to talk about, just make sure you put it on the agenda, and then we'll, we'll definitely go and roll through. We have usually a few more people joining.
Sorry, I don't mean to… ignore you here.
David Ashpole (dashpole) 00:03:35 Just here to talk about… the node's proxy…
atoulme 00:03:41 Okay.
David Ashpole (dashpole) 00:03:41 permission thing, so I'll put that on.
atoulme 00:03:44 You got, looking for that doc, too, and I'll just put it in the notes as soon as I can.
There we go.
Oh, this is ridiculous.
There you go.
Alright, so… here's the doc again, the new one asking… Is this the right time? You've… wait, we don't have today.
Who wants to add today?
I'll just stop, down there.
Put your name and info here… oh, shoot.
Agenda… If you want to move your agenda item here, I would be best.
And then today's date.
Here we go.
Yeah, sorry.
Bolding things.
- Hey, Evan.
jea 00:05:38 We can get going, we're, like, at the 5 mark.
atoulme 00:05:42 Let's do it.
jea 00:05:43 So, let's see what we got.
So, David, you have this, change for, this nodes proxy, nodespods sub-resource. Definitely in favor. The way that we've done this in the past is with this concept of auto-detect on Cluster.
David Ashpole (dashpole) 00:06:06 And so…
jea 00:06:08 We have a check that runs at the start of the operator that verifies what, is available to you, essentially. So, like, you can enable… it's sort of like, automatic feature enabling, and this would be one of them.
So I think it makes sense to do that there. I think the problem… is… Well, no, it's just a string, though, right? Like, it doesn't require any resources, right?
David Ashpole (dashpole) 00:06:38 It's just a string.
So that… well, this is part of the… RBAC config, right?
jea 00:06:45 No, yeah, but it's not, like, a new CRD that we have to, like, include in the bundle or anything. Yeah, so I think it should be fine to just, add in, like, an auto-detect For the cube version, which I actually thought we had, for what it's worth.
David Ashpole (dashpole) 00:06:58 Yeah, yeah, well, I have no clue about anything, so if there's any prior art or anything you can point me to, I can go figure it out, as well.
jea 00:07:07 Oh, we do have this already. Okay, let me show you.
David Ashpole (dashpole) 00:07:10 Yep, yep.
jea 00:07:12 You can see here…
David Ashpole (dashpole) 00:07:15 Some of the comments made it sound scary and hard, so…
jea 00:07:18 No, it's like, it's very easy, or at least it should be. So we have this concept here of detectors, there's a discovery client which can get the Kubernetes version.
And then this thing is used in this auto-detect… package. We currently use this for native sidecar support. Pavel added this in a few months ago.
This one was even more wiring, because you had to, like, wire in, some different places for containers, so this should be a… this change that you're making should be a lot simpler.
And so you can basically just do the same, like, bool error check here.
For, if your feature is available, and then use it accordingly.
So, should be pretty easy.
If you run into any trouble, just let me know. I can, I can assist.
David Ashpole (dashpole) 00:08:22 You know, I got roped into this from some person on the GK team.
So true.
jea 00:08:29 Yeah, so…
David Ashpole (dashpole) 00:08:31 Yeah.
jea 00:08:32 Yeah, it should be straightforward. The Helm chart one will be a little bit harder, because that one… there are Helm features where you can check the Kubernetes version, but.
like many things in Helm, I don't trust it at all. I just… I feel like that's the type of thing that has burnt me in the past, with these, like, static checks, because if you're installing it with Argo, I don't think it runs that on the templating command.
Don't quote me on that, I might be wrong, but that was when I ran Argo, like, 4 years ago, that was the case.
Maybe it's smarter now, but who knows?
David Ashpole (dashpole) 00:09:11 I should not trust the Kubernetes version that I can get from Helm.
jea 00:09:15 Helm has this… yeah, Helm has this thing, it's like a templating variable built in for, getting the kube server version, but if you're running the template not connected to a cluster in your, like, for example, in, like, a CICD pipeline, and you're just running a template locally, it won't be able to get that information correctly.
David Ashpole (dashpole) 00:09:40 So it'll essentially be from, like, a fake server or something.
jea 00:09:44 Yeah, so… because it's not able to, like… you're not bundling Helm as, like, a binary, right? Like, it's.
David Ashpole (dashpole) 00:09:50 Yeah.
jea 00:09:50 bundling the YAML, or like, you know, just rendering YAML for you.
So… with that one, that being said, like, we in the Helm group don't have as, strong guarantees about versions, like, version compatibility.
David Ashpole (dashpole) 00:10:10 It looked like there were…
jea 00:10:11 Well, we do have a prereq for COBE 124+.
David Ashpole (dashpole) 00:10:15 That's what I… right. So I read that and was like, yikes. Yeah. Like, that's a big jump to 133.
jea 00:10:22 Yeah, we should probably, talk about that in the Helm group. I might… I don't know if you have an issue already open for talking about, like, version support. The reason I said what I said earlier is because we haven't had this conversation of, like, what minimum version should we support, whereas the operator is much more, we have to care a lot more about kube version support, because we're taking advantage of, like, kube features, right? I'm sure that the guarantee that we're making for kube 124 support is actually not accurate, because there's definitely features that we use that are not correct there. Sorry, one… But… anyway. Yeah, we'll talk about it in that issue in Helm.
David Ashpole (dashpole) 00:11:19 You want me to… so I… right, where's the… so the issue is in the… Helm charts repo. Okay.
jea 00:11:26 Yeah, yeah.
So… Yeah, but we can talk about it in there. I'll bring it up with… What was the thing?
I'll talk with Tyler and the other Helm leads, and get you a better answer there, but I don't wanna… we don't need to take up the time in this sync to…
David Ashpole (dashpole) 00:11:56 Is this the wrong SIG for that?
jea 00:11:58 No, Helm doesn't have an actual, meeting. We sort of rolled it into this one and the collector one, because it's not as high trafficked as something like this or the collector group is, so we kind of divert people to one or the other.
David Ashpole (dashpole) 00:12:15 Okay.
jea 00:12:16 like, the maintenance burden on the Helm charts is much less than here in Collector, obviously.
David Ashpole (dashpole) 00:12:24 Cool, so I'm unblocked for the operator, and… We'll discuss what to do on the Helm charts issue for the Helm chart.
jea 00:12:32 Yeah, if you could DM me the.
David Ashpole (dashpole) 00:12:36 Do you want me to ping you on the issue?
jea 00:12:39 Yes, and also in Slack, so I have it in both places. Github gets lost for me, for some… I keep, like, missing notifications on pings on GitHub, which has been very frustrating.
It feels like their notification system has gotten worse, which I didn't think it could.
Anyway… We can move to the next one, if that… if we're good to move to the next one.
David Ashpole (dashpole) 00:13:04 Yep.
jea 00:13:04 Thank you.
Kai, you want to talk about this, cert manager?
Kai L 00:13:12 Yes, of course, thank you so much.
So, hello, this is Kai from Ericsson, and we created an issue in the OpenTechMeasure operator for enabling MTRS spread of Source Manager. To bring a little bit of a context, so we run the operator in a restricted enterprise platform.
Where Surf Manager isn't really available and allowed.
But we do have an internal PKI, and can provide certs as Kubernetes secrets.
Our use case to enforce MTRS between the target allocator and the collector in production.
So today, we know that it looks like the operator's empty areas flow is tied to the search manager.
And with certain meter isn't detected, it falls back to known TRS and the expected secret. Volume amounts.
Will not get applied.
Yeah. So, we created this issue, and we mainly want to check if… This is something that is already on the radar, and if we want to make a contribution, is there any preferred Partner approach that you would suggest us to follow?
Or is there anything that you see Can be done immediately, or in short term in this area.
jea 00:14:27 Yeah, so this is definitely something that, I don't think anybody would be opposed to. I think that we don't have the, like, availability to work on this ourselves, though, but if you have somebody on your team that's able to actually, like, get this fixed out, and it looks like you already have, sort of the guidelines for it, definitely something that I would be happy to review. Mikolai said he'd also be happy to review it, so I don't think it's blocked there. I think it's just blocked and we don't have time to… To dedicate to, sort of, testing with this. Certainly, the harness for this is a lot more challenging.
On my end, I don't have, like, my own cert manager to… instance to deal with.
So, if you have somebody on your team that can, like, make the change, I think it would be a pretty reasonable thing. And ideally, you could plug in actual Cert Manager, too, to verify that the Cert Manager essentially just becomes an abstraction on top of this, right?
Kai L 00:15:25 Yes, and so my understanding is that We don't actually have anything from the community at this moment for such implementation, but… If we want to make a contribution, then there's no blocker for this.
jea 00:15:40 Cool. Yeah, no, I think you should just go for it, and then ping in the operator channel when it's ready for review.
Kai L 00:15:47 Yes, right, thanks. You mentioned about these guidelines. Are there anything that we can, refer to?
I'm just…
jea 00:15:54 Yeah, so… I need to do yours.
I'm just looking at the PR, the issue that you have here.
No, I don't think there's anything… specific here. I would just, when you're making the PR and, like, doing the CR change, if you could reference existing work in, like, Prometheus operator or Istio or something.
Just because we like to follow convention of other operators when possible, and this feels like a feature that would exist in either of those operators already, just so we're not doing our own naming scheme. That'd be helpful.
Sorry, one sec.
Kai L 00:16:40 I see.
jea 00:16:45 Sorry, my dog is barking.
Kai L 00:16:48 Yeah, no worries.
jea 00:16:50 Anyway, yeah, so that all sounds good.
Thank you.
that's okay.
Cool. Anything else for the group?
Kai L 00:17:07 Right, yes, thank you so much for the.
jea 00:17:09 Yeah, no worries, no worries. Thank you.
Kai L 00:17:11 Thanks.
jea 00:17:13 Evan, did you have something to bring up?
We're coming to hang out.
Evan Torrie 00:17:17 Just coming to hang out, and I have used the operator in the past, and sort of getting back into it a little bit, so… Awesome. Just catching up with what's current.
jea 00:17:26 Cool, always a good thing. Let's see… We have one disgusted SIG.
this is maybe from a bit ago.
So… Antoine, this is related to the managed CRD work from your team.
We did merge this draft PR, right?
atoulme 00:17:53 We did, because, yeah, it's fine, it's not impacting anything, yeah.
jea 00:17:58 Have you gotten a chance to mess with it internally?
atoulme 00:18:02 No.
jea 00:18:04 One second.
atoulme 00:18:05 time has not been friendly with us. I think also… I'd like to get some feedback from Red Hat on this one, because this is eventually an OpenShift-level, like, thing. We really mean this to be for OpenShift environments. Yeah. And, I'm chasing a little bit on the product side, some of the… some of the Red Hat OpenShift folks to make sure that we have a strong commitment for this as part of what we're trying to do.
jea 00:18:32 Yeah.
atoulme 00:18:35 So, yeah, we're working on, that. The thing to think about is how also this meshes well with the injector-type discussion we're having, which I think are more interesting at this point, because they would definitely remove a lot of code that we have to manage in the operator.
jea 00:18:52 Yeah.
atoulme 00:18:53 So I'm more excited about that. Also… This would even take a backseat to some of the work that you had in mind, Jacob, to redo a little bit the way we run the webhook, because right now it's pretty expensive, since we're checking, using the Kube client every time we want to instrument a pod.
Yeah. Which may be too much in some situations, so we really do need to, kind of, adopt that caching mechanism instead, but I just don't have time.
jea 00:19:25 No, that's… yeah. Also, the injector hasn't been to the point where, like, we've had the release In a place where we could do that, right?
atoulme 00:19:34 We're getting there. We're getting really quickly there. They just added Python support.
jea 00:19:40 Yeah, I'm following all the things. Like, I know, sort of, like, where it's at. I mean more, like, I… we're not at the point that we can do a full swap-in just yet.
atoulme 00:19:50 Oh, no, even if we did, like, to be clear, like, I think the right approach would be that we don't swap anything until, like, we offer both for at least 6 months before we move over, right?
jea 00:20:00 That's what we talked about at the last SIG meeting, right?
atoulme 00:20:04 Okay, cool, yeah.
jea 00:20:05 I think… I think that was the discussion, is that, like, we would… I forget who said that they would work on it. Let me see who was here last week. Oh, Arthur said it. Yeah, Arthur was going to look… start to look into this, so… I am on the lookout for a PR… for a PR from him.
on this, but definitely, like, I… once we get that done, I think it opens up the… managed CR world.
atoulme 00:20:36 A bit more. Clearly, like, it helps, because…
jea 00:20:40 Yeah, we, we…
atoulme 00:20:41 So the managed CR, what's kind of cool about it is that it doesn't do that much, because it's itself just deploying additional CRs.
jea 00:20:49 Yup.
atoulme 00:20:49 Instead of trying to recreate whatever you have in your operator, we're just going to manage best practices through some very opinionated lens. And I think the feedback from Jack was actually very much on point, and there's no real daylight when I saw any issue between what he's saying and what we'd like to see, which is use declarative config, don't recreate your own.
jea 00:21:09 Yep.
atoulme 00:21:09 Absolutely, we've been waiting for this. And there are all sorts of common sense arguments, like, do not try to do anything. But the reality of it is that all those projects right now, they're kind of floating on their own, and we're gonna need some people to, at the top, kind of Organize this, because they're all 80% done, and none of this is actually done in a way that would actually make it possible, like.
The declarative config for Java is somewhat, like, there, but it's not the same way for other SDKs, so we can't just put all our chips on it and make sure that it's going to be the way forward.
jea 00:21:43 Yo.
atoulme 00:21:44 So, we're in the long tail of a long list of things that need to happen in a very nice order, so we can have that, and that means we need to also have a release train, and some idea how we organize this, and we need to engage with SDKs, maintainers who are themselves, like, quite strained, So, I think this managed CRD is, a vision type statement, it was like, this is the way we want to go. Yeah. Stop having people, like, having to think about how they're going to do some YAML.
jea 00:22:13 Yeah.
atoulme 00:22:14 I'm happy where it's at at this point.
jea 00:22:16 Yeah.
atoulme 00:22:19 it needs to be a community effort, too. It cannot just be me and Dajiro pushing this, I think.
It needs to be, like, people care about this because they have this pain.
Yeah.
jea 00:22:31 No, I totally agree. I think this will be the topic of discussion when we get to KubeCon next month, is just, like, how do we coordinate this? Maybe we should reach out to… I'm sad that, David dropped already. I should have told him. This would have been a good discussion to get his point of view on.
But…
atoulme 00:22:49 Yep.
jea 00:22:49 I definitely think that we're reaching the… state of maturity for the project, where we need to be better at, this larger organizational stuff.
And… we, I think, could benefit from… a… Yeah, like, better coordination of these types of things, just to understand status and.
atoulme 00:23:17 Yeah, but if you remember, like, I think we voted for GC back in, what, October?
jea 00:23:22 Yup.
atoulme 00:23:23 Okay, I think those people are supposed to help with that?
jea 00:23:27 Yeah, and… but it's a different type of share-out that we get, right? It's like, the… I get the context that I need for what we're doing on a day-to-day, but I don't know if we're getting the context that you're talking about of the larger, like… I don't know what's going on in the Java SDK, I don't know what's going on in, like.
atoulme 00:23:43 What would you? That's too much trafficking of you. What I would like is that, so, the GCS decided that they wanted to have a TC liaison and a GC liaison in every SIG meeting for the reason that we just stated, which is we need to have better collaboration, and we need to have a better understanding of what the… the SIGs are doing. And the DC event, through some discussions, were saying we need to renew the Charter of SIGs. We can't just let SIGs to go on forever. There needs to be a reason why they exist, and we need to make sure they are coordinated in some effort.
jea 00:24:14 Yeah, yeah.
atoulme 00:24:15 So, right now, there's a packaging SIG, option that is in front of them with, Dazziro, and Michael is trying to do his best to push forward for that, and we, you know, the feedback he's getting.
Is maybe get more people involved?
So that we have more coverage. This is really difficult. But eventually, I think, the GC needs to kind of step into the arena and start to say, look, here is… here are the compartments of the submarines, and each compartment needs to be submerged in some way, so we can actually take dives, right?
jea 00:24:47 Yeah.
atoulme 00:24:48 Technology.
That the back of the submarine is still, like, way too much in the air, because the ballast won't actually get.
jea 00:24:57 Yeah. Yeah. Well, I think, you know, at the last KoopCon, the topic was basically, like, how do we… well, what I was talking about with David at the last KubeCon was that, like, we, as our SIG, become… we are sort of the only, like, packaging SIG right now, in a way.
The only one who cares about Java SDK breaking changes.
Yeah, and so I think I'm happy with, like, Michele's effort to do packaging group, and I want that to be successful.
But, you know, I think the TC is right, like, there needs to be more staffing on that, because if it's just him and, like, Dash Zero people, they don't have all the time in the day.
atoulme 00:25:43 I put my name down, too.
jea 00:25:45 You're also over… you're… you're on everything, Anton.
atoulme 00:25:49 Would you like me to put your name down? This seemed like a…
jea 00:25:51 No, you did this with the injector crew.
The injector one, I at least have some time to do reviews every now and then, but I couldn't do another one.
atoulme 00:26:01 You're doing a better jump than I am.
jea 00:26:04 I don't think that's true.
atoulme 00:26:06 Well, no, no, you're definitely doing a better job than I am, on that. The injector discussions as a maintainer are mostly managing it from a project standpoint. It's like, the questions we have at this point, it's like, what's done elsewhere? I'm like, oh, when the collector, this is how we do things.
And sometimes it just falls flat on its face, but at least it's helpful to have some level of compilability. Like, you can do that too, right? You can just look at things like, oh yeah, we do renovate this way, right?
jea 00:26:31 Yeah, yeah.
I have been using for my own… for, like, my company stuff for releasing, I've been using, this thing called Release Please, which has been very good. I don't know if you're aware of this project, but…
atoulme 00:26:45 I am not.
jea 00:26:46 It's really good, I can show you very fast what it looks like.
atoulme 00:26:50 Sure.
jea 00:26:50 So, I don't… your last comp… sorry, Evan and Kai, we're going off, off-script here.
Kai L 00:27:01 No worries, yes. Thanks.
atoulme 00:27:03 Signed up, they signed up for listening, so…
jea 00:27:06 So, working on this, like, other spec proposal with, Javas RF.
And I've been using this thing, Release Please, and the idea… Where's my file?
Oh, no, I'll show you the Rust one, which is more interesting.
atoulme 00:27:25 Okay.
jea 00:27:25 So… Is it Rust? I thought it had a… I thought I had it here.
What is the one that I have before?
Oh, no, it's, it's, this one. Sorry.
I'm working on a lot of libraries. So in here, you can basically define, like, what version you want, so this is, you know, 0.6.3, and then you have a config, which defines how you, like, traverse files to then modify versions, right?
atoulme 00:27:55 Okay, yeah.
jea 00:27:56 And here, it's like I modify the collector manifest when I bump my version, and it's like a generic thing, right? And so then when I go to do a release.
Well, when I push a PR, I'll just show you this. So… It enforces the, the structure for, like.
I need to go to the PR. It enforces the structure for, conventional commits, so you have to do, like, fix, chore, perf, whatever. And then when you merge it, it automatically will spin up this release PR for you.
Yeah, okay. With all of the changes that you're making, grouped into, like, a changelog. And then, in the files change, it will, like, parse through and then automatically do the version change here.
atoulme 00:28:43 In the manifest, and then also do the changelog as well.
So you're always a release, away. You can merge this anytime you like. If you don't like it, you can just keep that PR open and keep working.
jea 00:28:55 Yeah, exactly. So you're not on a release calendar… the release calendar is, like, whatever you want to make it, essentially, right?
atoulme 00:29:02 Yeah, continuous development.
jea 00:29:04 Yeah, and so the benefit of this is that I can just keep doing, like, patch versions, and then as soon as I push a… push… as soon as I push a feature, I will bump the, minor version.
atoulme 00:29:17 Yeah, it's using the semantic convention.
jea 00:29:20 Yeah, yeah, like, semantic versioning correctly. I kind of fucked this up initially, though, in my other repos, and so all of them started at 1.0.0, when they should have started at 0.0.0.
atoulme 00:29:30 Oh, man.
jea 00:29:31 Which, that was my… I didn't know to use the tool, but now I know to use it, so… But it's really good, and then it also automates, like.
You know, it does the release thing here, and you can set up in CI… on release, all it does is run the, like, you know, my Docker… this is, like, my custom Docker release thing on the tag push.
atoulme 00:30:00 I see.
jea 00:30:01 Right? And so, I can, like, test it very easily, because this is just workflow dispatch, and I can do a dry run, so it doesn't actually push anything.
And because this is after the fact, it doesn't need the release to exist for me to do it.
atoulme 00:30:16 Yes? Okay.
jea 00:30:17 I can just do this on Master, which is… which is easier.
And then I also set this up… my company uses a thing called Task Files, which I had never heard of until this project, until this company, but it's essentially, like, what I want make files to be, because it's actual, like… I don't know, it's YAML, and I can just embed commands, and it's not really funky syntax.
atoulme 00:30:40 Whoa.
jea 00:30:41 And you can do, like, you know, task, test coverage, test verbose, and you can just, like, script out all of the things that you do for the project much easier.
atoulme 00:30:52 So, that's for YAML, what's the… what's the executable to run those? Is it make, or take, or…
jea 00:30:58 No, it's its own thing, it's like task, so.
atoulme 00:31:01 Physical task? Okay.
jea 00:31:03 Yeah, so it's like… Okay.
Yeah, it's super easy, and it will do caching for you and all these other good things.
atoulme 00:31:14 I mean, I lose so much time in make files just because there's a tab in the wrong place.
jea 00:31:19 You know, I really hate big files.
atoulme 00:31:22 Built enough scar tissue by now, it's… I know it's due, but yeah. Yeah.
jea 00:31:25 You can also do things where, you can have sub-task files, so it's like, if I have a, like.
well, like, in, contrib, you could have, like, the repo-level task file, and then each component could have its own task file, so that, you can just coordinate it like that, and then you can use… it accepts glob patterns.
You could glob, like, task, processor, star, and then name of task in there, and then it could just delegate correctly that way.
atoulme 00:31:56 I'll take a look. Is it… do you know how it's written?
jea 00:32:00 Like, what language it's written in?
I think it's GOAT.
atoulme 00:32:04 Oh, some good stuff. So yeah, brew install? Brew Install, something like that?
jea 00:32:09 Yeah, just brew install. It's super easy, and… Good.
I've been… I'm a big fan of it. It's actually made my life, like, a lot easier.
atoulme 00:32:19 Yeah, I bet. No, it's just, it's the type of stuff, it's like, you… if you have, GitHub Actions and the ecosystem that goes with it, it's very important, because you can have the best little tool that works in the machine, but then, you know, if it requires some… You know, yeah, I'm…
jea 00:32:36 The last thing that we use, which kind of makes this all work really well, is this thing called Hermit, which I had never heard of before.
atoulme 00:32:43 permit.
I'm not sure.
jea 00:32:45 project from Cash App, funny enough, but it's sort of like… Virtual environments, but for… Everything.
And so… you can, rather than, like… I'll show you in the…
atoulme 00:33:00 Like, in VM, but better.
jea 00:33:02 Yeah, yeah, basically. So, like, in here, you link all of the, you, like, specify all of the things that are required for this project, and then you activate this, like, small little script.
atoulme 00:33:14 So it's like… Is it vigilant.
It's like virtual nanv, pretty much. Virtual Env, but…
jea 00:33:20 Beautiful.
atoulme 00:33:21 Okay, and this is also a better approach than install tools that we have right now, which is kind of forcing us to do a bunch of dumb things. Okay.
jea 00:33:29 Yeah, yeah.
atoulme 00:33:30 Oh, that makes sense.
jea 00:33:32 This is, like, super easy, because then when I'm… I'm gonna stop share for one sec so I don't leak any company stuff.
atoulme 00:33:38 Please.
Yeah, no, that's cool. I appreciate you sharing your tools and your… your stuff, I… I gotta say, I don't have time these days to invent, to find new things.
jea 00:33:55 I'll show you the… I'll show you this very fast.
So, in my, like.
collector, distro, copy. I can do source, activate hermit, and then I get all of my… all of the tools, and I can just do, like, hermit list.
And it tells me, like, you're using Go at this version, and Task at this version. And then if I need to install something that I don't have, so, like, if I needed, You know, like… what's a good example?
what's, like, a tool that I might use?
atoulme 00:34:26 Girl.
jea 00:34:28 It will, like… well, this is part of, like, Brew, so Curl…
atoulme 00:34:32 Oh, okay.
jea 00:34:34 It's more like.
atoulme 00:34:36 Anyway, yeah, whatever.
jea 00:34:38 I don't know. You could do Hermit, no, Hermit Search, I think?
atoulme 00:34:44 Hmm.
jea 00:34:46 Oh, gRPC Carol, yeah.
atoulme 00:34:49 Okay.
jea 00:34:50 And then I can just do this.
And then you'll see on the change, it does an actual, like, diff. Sorry.
atoulme 00:34:56 Oh, because that's local to your thing.
jea 00:34:58 Yeah, but it doesn't install the, like… Yeah. It just uses this locally. And then on your machine, even if it's, like, a different, different laptop. It'll read the version, and then install your, like.
atoulme 00:35:12 Ugh…
jea 00:35:12 Local version for it.
atoulme 00:35:14 This is so nice. This is the first time I've had a discussion about just tech tools like this in months.
Okay.
jea 00:35:23 It's… it's very good. I really like the… this, like, sort of pattern. It's also made, like, CI a lot easier, because then I'm like.
atoulme 00:35:30 when I need to set something up for CI.
jea 00:35:33 I just have a task.
atoulme 00:35:34 Yeah, yeah, okay.
Okay, that makes total sense.
jea 00:35:37 Yeah. It's a nice thing, but I don't have the wherewithal to argue that we as a project should move to this setup.
atoulme 00:35:44 I mean… No.
jea 00:35:47 Yeah.
Evan Torrie 00:35:49 Probably a lot of opinions on different types of tools like that as well. Some people use Hazel, for example.
jea 00:35:55 Oh, I… we're not doing that, I hate.
Evan Torrie 00:35:57 I know, I know, I'm just saying, some people might suggest that.
atoulme 00:36:02 Yeah, and then you have to have a really good idea why you would push back on that. We… We… we definitely need to be… Appropriate to the different audiences we have in our project.
The makefiles will stay… For a long time. I guess that makes files and contribute have proven to be very challenging at times, because they were pretty slow, and I realized some of our CI tool time was just spent just reading the makefile, because the makefile is doing incredibly complex stuff, like reading all the go.mud files, and like… Doing all sorts of things that are not really a good idea, but you don't know that until it's too late. And… Yeah. Anyway…
jea 00:36:40 Anyway, yeah, so I just thought you'd enjoy a little bit of… of tooling talk.
atoulme 00:36:47 Oh, man, you made my day.
Thank you for watching.
jea 00:36:49 Can I show you one more cool thing? If you have time?
atoulme 00:36:52 You sure?
jea 00:36:53 I don't know if you read the thing that I… that I've been working on with Josh, the, like, OTEP?
atoulme 00:36:59 No. I'm sorry.
jea 00:37:01 That's okay. You're… you're busier than anybody I know, Anton, so it's… it's alright.
atoulme 00:37:06 I'm not doing much, come on, what are you talking about?
jea 00:37:08 Get outta here, you're doing the most.
You're doing so much.
So… Anyway, I'm trying to introduce this new concept for policies as, like, a global thing, where…
atoulme 00:37:21 That I heard about. Okay. I heard from my team that they're pretty excited about this, actually.
jea 00:37:27 Oh, I'm glad, I'm glad to hear that. It's… it's a new… concepts, and my… like, I've been doing all this implementation work for my company, and so…
atoulme 00:37:37 Makes sense.
jea 00:37:38 a bunch of stuff already done for it. I have all these, like, clients and things, so now what I'm doing… what I've been doing recently is just benchmarking to see, like.
atoulme 00:37:46 how my implementation in Go stacks up against, like, what this looks like in the collector today. I see.
jea 00:37:53 And so… Nope, not that.
I'm gonna stop share for one second, just so I can pull this up without it being… .
atoulme 00:38:03 Lois.
jea 00:38:06 Because I think you'll find this very exciting.
Okay.
So… I wrote, like, a little pro- I have a library called PolicyGo, and then I have a processor that, uses that library. And a policy file is, like, very simple, so you just have, like, a list of these rules. You have, like, a matching condition, and then a, action. So this is, like, none, right?
And then I also have, like, I just wrote a conformance suite.
This is all public, so I'm not showing you company secrets here.
But… I have this conformance suite, which… tests a few different implementations, and then I have all of these tests for it.
And so, you can do, like, log sampling… this is, like, a 50% log sample policy, based on the, like, trace ID.
Wonderful.
atoulme 00:39:04 So the test is you take some input, like, configuration, and you can actually see the expected outcome of applying the policy to it, is that right?
jea 00:39:15 Yeah, yeah, exactly.
atoulme 00:39:16 testing… you're testing that on actual logs, so you're… it's not even… you're not even show… doing the diff on the config, you're doing the diff on the data that goes through the configuration. Okay, makes sense.
jea 00:39:28 So, here I can, like, validate that for all my implementations, if I give them this input OTel JSON log, then this should be the output JSON log.
atoulme 00:39:39 That's much more mature than I thought we would be at this stage.
assumed that you were just working through the grammar of the policy. I didn't pay attention to how advanced you were. Cool.
jea 00:39:51 No, yeah, the grammar is, like, I mean, it's a pretty simple grammar, like, I didn't do anything too crazy here. It's just, like, you have a list of matching conditions, and then you have a bunch… you have a few actions you can take, right? It's nothing.
atoulme 00:40:01 Yeah, that's true.
jea 00:40:02 And I have, like, basic transform support, where you could, like, You know, add a body when nobody is provided or something, right?
atoulme 00:40:11 Okay.
jea 00:40:12 like that. So… But you can see how, like, this is a parallel to, like, the transform processor and filter processor, right?
atoulme 00:40:20 Yeah, okay, and you want this to be specific to the collector, or you want to apply that to SDKs as well?
jea 00:40:25 everywhere. So, SDKs, collector, like, all over the place. The idea is that we have, like, one shared configuration for doing these, doing these things, and you can apply them with very small libraries built on top of OTEL.
atoulme 00:40:42 Like…
jea 00:40:43 has its own, mechanism. Not tied to the collector, not tied to an SDK.
atoulme 00:40:48 Oh, I see. Interesting.
jea 00:40:50 You want to do this with the declarative config folks as well, or… So, they… there's a few ways that we could do it with declarative config. One way is that we could, compile the policies, like, each of these actual, like, objects into declarative config directly, because they provide a lot of the bindings for this type of stuff.
But…
atoulme 00:41:11 Yeah.
jea 00:41:11 don't know if they're going to want to do that after I show them performance data for what I've done.
atoulme 00:41:18 Okay.
jea 00:41:19 For the collector, initially what I was going to do was compile each of these policies into filter processor and transform processor rules.
atoulme 00:41:26 Yep.
jea 00:41:26 But I would all… in, the first language I did, because we were doing it in the injector, was Zig, and I did this performance improvement using this thing called Hyperscan, which compiles a bunch of regexes into a database, so you can do, constant time matching on, like, thousands of policies.
atoulme 00:41:46 That's cute. That's… that's cool. I… I did not know that was possible. Yeah.
Why are you so hung up on performance?
jea 00:41:54 Because we should care about performance, Antoine.
atoulme 00:41:57 Performance is a great feature, but I have to say, getting social acceptance and consensus around the need for the telemetry policy is a very difficult discussion by itself. I understand that performance makes it easier if you can'.
jea 00:42:12 Yup.
atoulme 00:42:12 alleviate any issues around performance, but I think it's, the project is barely able to even articulate this declarative config, and you're like, okay, let's put on top of that this notion of policies and governance, right? Because this is going to come to that. Yeah. Frankly, OpEmp and all that stuff is also in play. Now you have this extremely complex soup of all those concepts. You can maybe talk to five people, and they'll be able to make sense of what you're saying.
jea 00:42:37 So, I don't… I hear what you're saying, but I also think that this solves the problem that op-amp has, which is that there's no universal configuration for OpAM.
atoulme 00:42:47 You're right. That's why we're excited about it, but we are so deep inside OpEmp that we understand your… if I was to explain that to a random, like…
jea 00:42:57 you know, IT person.
Yeah.
atoulme 00:42:59 it would take me, like… I would need to kind of start with, like, first there were stars, and then, you know, the Earth formed, and then the transformation happened, and then we built it, and then we had more problems, because not temperature was too static, and people wanted to do stuff, and
jea 00:43:16 Well, I have an easier… I have an easier explanation, which is that, the benefit of a policy is that this is easy to under… like, this single block is easy to understand the intent Without needing to, like, understand a lot about syntax. So you don't need to know OTTL to… to write this and understand this, right?
atoulme 00:43:36 That might be the death of a tutorial, my dad.
jea 00:43:39 I don't know if it'll get to that.
atoulme 00:43:41 Oh, I know why Josh is so excited about this now.
The Dodge Sheriff has been, like, yammering about the fact that OTTL is this kind of cottage cheese thing that just took hold at some point. There's nothing wrong with OTTL, it's just that it's very much like an attempt in earnest to try to build something meaningful, but it escaped its Pandora box a long time ago, right?
jea 00:44:05 Yeah, yeah. But, like, this thing, I think, is easy to understand, right? If the name of the thing… the name of this is add body to logs without one.
Right.
atoulme 00:44:15 I mean, even better, right? I don't have to write this. I would like to copy-paste it, please. Be done.
jea 00:44:20 Exactly, you can just copy and paste it, and you don't need to put it into the pipeline in just the right way, you don't need to instantiate anything, you just have a list of policies, and you have a… it'll just read the list, right? It's like… That's the concept, is that I just want ad-body policy today.
atoulme 00:44:35 young, right?
jea 00:44:36 Done. That's it.
atoulme 00:44:37 I have a registry somewhere on the Penteometry I.O. that says, here are the 50 accepted stable policies we will go with.
jea 00:44:45 Yes.
atoulme 00:44:45 You need to stop thinking.
jea 00:44:47 Yes.
atoulme 00:44:48 Yeah, okay. And you can build your own, but… Sure, why would you?
jea 00:44:51 But you can imagine, then, that as you increase that number of policies in, like, a large enough organization, that's when performance matters. That's why, like, when I was talking to Josh, their initial version of this, they're running, like, millions of these things.
atoulme 00:45:07 Oh, okay.
jea 00:45:08 And so, I was like, how can we scale up to match that? Like, essentially, right? Like, what happens to the collector right now if you were to run, like, a few thousand, transform and filter rules?
Right.
Evan Torrie 00:45:24 Yeah, I think the idea… I don't know that much about this, but just since this is my first meeting here, but aim high is always my… my mantra. Maybe shot down, but aiming high is a good idea.
jea 00:45:36 Yeah, and so, Anson, what do you think happens when you start to run, like, a thousand filter policy, filter processor rules?
atoulme 00:45:45 Yeah, probably does not do anything good to the collector.
jea 00:45:48 So, here's the data that I've collected.
This is, requests per second, in a log scale for X and Y axis.
So, for… I tested it against Vector and Baso Collector, and then my distro with the, this processor, and then just the ZIG implementation that I wrote.
atoulme 00:46:09 Okay, that's cool.
jea 00:46:11 And so… This is for Datadog… I did Datadog logs and Datadog metrics, because those are JSON, and then I did OTLP logs and OTLP metrics, because those are Protos, so…
atoulme 00:46:20 See?
jea 00:46:20 Just to see what the difference looks like. And so, keeping in mind log scale, you can see that, like, for JSON performance, for my, binary, it's, like, basically flat, right? We're at about 80,000… 88,000, 90,000 requests per second, no matter the amount of policies that you're running.
atoulme 00:46:40 Okay.
jea 00:46:41 Whereas, like, vector craters very fast, and then down here, you can see that, like, the collector for JSON performance is not great, but it also goes down as you start to run it more.
atoulme 00:46:52 Yep, great.
jea 00:46:54 Same thing happens for metrics, so that's, like, pretty consistent.
Evan Torrie 00:46:58 Sorry, what is vector in this case?
jea 00:47:01 Vector's another, like, telemetry pipeline agent. It's written in Rust, it was… it's good performance.
Evan Torrie 00:47:08 For a lot of people.
jea 00:47:11 Yeah, they have their own language called VRL, which is their version of OTTL.
Which is what I wrote these tests in.
But this one, I think, says it all, right? It's like, the blue line is my modified collector, green line is my proxy, and then orange and purple are the collector and vector, respectively.
atoulme 00:47:31 Yeah, I mean, that makes sense. Okay.
Yeah, just, I really… I haven't run into situations where people run thousands of rules, but you're right, that eventually everybody will go there.
I feel like we had some time before we had to think about that that much.
jea 00:47:45 I think, yeah, I think we're starting to reach the point in the project's maturity where, like, when I was talking to Andy and I showed him this stuff, he was like, yeah, we have people that run an OTTL statement with, like, 2,000 OR conditions.
atoulme 00:48:03 Oh, that's funny.
jea 00:48:04 And so… Like, the performance story, as you start to run a lot of these, gets crazy.
atoulme 00:48:12 Yeah, I mean, OTTL was… you could just also just take OTTL on a bench all day and just make it better. Like, it's just… I don't think if anybody has spent the time to really optimize it. And I… and, well, pretty much here, you're doing it. Great.
jea 00:48:28 Yeah. So this is the… this is the, like, excitement, is that we can now sort of understand this… this performance, and…
atoulme 00:48:35 Yeah, that's great.
jea 00:48:36 Looks at it.
atoulme 00:48:37 I'm sure.
jea 00:48:37 and… There's a bunch of interesting stuff. The collector, like, memory actually performed a lot better than I was expecting.
So… It does that at a sacrifice of, like, RPS, but it's actually pretty stable overall.
atoulme 00:48:54 I mean, the feedback I would give you is, the collector is not really constrained by its processors that much, usually it's more by its exporters.
True. They seem to crap out much easier than whatever…
jea 00:49:07 Thank you.
atoulme 00:49:08 you know, you're pushing 80,000 logs a second into your collector, that's not really the story. The story can be backend actually take it.
jea 00:49:15 In the back end, handle it, yeah.
That's a great point.
atoulme 00:49:19 the vacuum's crapped out on me so many times that you have memory pressure constantly in some situations, like, it's just… I love… I love to be… I love to have my processors be my source of pain, but it's just not been true, and network.
jea 00:49:31 Oh, yeah.
atoulme 00:49:32 and all that. I don't mean to demean any of this, because this is great.
jea 00:49:36 That's a great point. It's funny, because I actually have had the same… you know, when we were… when I was, like, running ingestion at LightStep, it was the same problem, right? It's like, how can our backend keep up so that the collector doesn't get, doesn't go haywire, right?
atoulme 00:49:51 Yeah, and then the only solution is you get out of the way and push in Kafka as fast as you can, or something like that, right? Just… Yeah. And… and you're… now you have two problems, right? So, but yeah, I… okay.
Awesome stuff. Thank you. This is really encouraging, and it shows a lot more maturity than I was ready for. Just so you know, if you need someone to sign off on, telemetry policies, or if you… if you need someone to say nice things about it, we're around, and we are looking into it, but we're just getting started, because we are… trying to build as much open capability into our stuff.
jea 00:50:28 Boom.
atoulme 00:50:29 I'll give you… I'll give you a little bit of what I'm thinking is my next move, which is that I would like us to, for OpenTeometry, and even for Splunk, build a OpenTeometry installation, sorry, that is going to resonate well with people. I've made… I've been very clear about that before, that packaging sync is a good idea, but I think also people just want to, probably have an APT install OpenTeametry story, and it will go for us too, right? So… and that would install everything, injector, all the stuff, and all that.
But, I'm thinking bigger.
I'd like to install the JMX scripper.
I mean, all sorts of things.
So…
jea 00:51:11 That's also a thing that we desperately need, is, like, better installation story. Because again, like, nobody's considered what it looks like, for a lot of these things.
atoulme 00:51:22 We need a Skunk Works approach to this, too. Like, we don't… we don't want to be taken too seriously by the community, but… Having some sort of install there would make a lot of sense.
jea 00:51:30 I mean, you're part of the Obi stuff, right?
atoulme 00:51:33 Yeah, so OB guys also have a pretty big part to play there.
So, I noticed something too, by the way. So… The biggest struggle I have right now with the collector is that we have a number of customers who have used some of our old stuff for scripting.
I realized that the Python SDK is actually very mature for when it comes to be able to script your own stuff.
So, I'm about to do a 180 and go to the Python SDK and make it an installable thing that will allow you to do your own cron jobs, where you could do your own execution of Python scripts that would do custom scripting for you.
jea 00:52:15 Yeah.
atoulme 00:52:16 And when we do that, that would actually be part of the install, too. And that would also help me in some systems, like AIX and HPUX and Solaris and whatnot. The collector will never work here, but Python will, so install that.
jea 00:52:32 Interesting.
Yeah, one of the things that I've… I've thought about is, like, How can we, Take advantage of all of the parts of the ecosystem to… actually reach the goal effectively. Because there's two parts of the story that, like, my policy work… there's, like, my policy work fits into one of them, which is, like, what do we do with this data? But the other one of, like, how do we get all this data, is one that I don't think we've… I mean, we can now get all of the data, right, at this point.
atoulme 00:53:09 Kim.
jea 00:53:10 But… Coordinating that is still very challenging.
atoulme 00:53:14 Yeah, it needs to be… dumb as bricks. It needs to be, like, just one big package you install. And your policies would then make sense. So, what I've been trying to tell people is.
Right now, we're telling people, hey, you configure everything at install time. I would like this to be separate thing altogether. So, when you install, it should have a default configuration based on best practices and very conservative settings, and allow you to kind of get by.
But then your stuff comes in, agent management comes in, and you have an enrollment into a fleet, and then your policies start to trim in based on what you want to see in terms of managing those things at scale.
And that's how we do it. We need to separate installation and configuration. If we do both at the same time, we're just setting ourselves up for a world of pain. Even in Siebel is a great way to do that, right? You can do… We can do these type of things at first with Ansible, without op-amp, but eventually OpEmp and things like this would make sense.
jea 00:54:11 Yup.
Yeah, I mean, OpEmp is… it has a protocol, it can do all of this stuff, it's just that the coordination around it is not good.
atoulme 00:54:19 Like… No, don't.
jea 00:54:20 And that's, that's what this is, like, sort of… You know, hopefully this is solving a lot of those frustrations.
atoulme 00:54:28 Yeah, I've just seen the discussion we're having with the OPAM Supervisor D?
jea 00:54:33 No, I stay away from the supervisor, I don't like it.
I've made it clear to them that I don't like it. I don't… there's… the way that it works in Kubernetes is,
atoulme 00:54:43 Oh, good to know.
I haven't looked at it that much, but I got myself as a co-owner on it for some reason.
jea 00:54:52 This is what I mean, you're everywhere.
atoulme 00:54:55 But that doesn't mean I do much. So, but for the Open Survivor, he actually put my foot down, I was like, I do not know what to do about this. Someone came up and said, I want to have a fallback configuration if the configuration fails.
And I'm like, that's disgusting.
I don't like it. I don't know, I can't quite put my finger on it, but there's something wrong about this.
jea 00:55:16 Yeah.
atoulme 00:55:18 I would, for example.
Push on telemetry policies be a better approach, if you want to be conservative about your config.
jea 00:55:26 Young.
atoulme 00:55:26 we make it that your policy application could also be very, like, reversible, or allow us to survive a, like, a bad install. So the configuration stays the same, but you're just applying different policies on top. And before… therefore, you actually survive this, because.
jea 00:55:43 Yo.
Well, so the benefit of the policy being this very constrained grammar is that the… you… you limit the blast radius, or, like, the possibility for failure.
atoulme 00:55:56 Later.
jea 00:55:56 The way that I've been trying to design the actual proto is so that you can't have conflicts in the typing.
atoulme 00:56:03 Oh, it's even better, yeah.
jea 00:56:04 So, that's part of it, and then the other way I've designed all of the libraries is that the actual compilation of those databases and matching indexes is totally separate from the hot path of, like, evaluation. And so, were you to fail the compilation process, it wouldn't affect the hot path, because the hot path is going off of a, read-only snapshot.
Of the… of the data. And so only after you're able to compile a successful snapshot do you take the lock and then swap the snapshot.
atoulme 00:56:35 Let's see.
jea 00:56:36 And there's only ever one process that's doing that background job, so you don't have to worry about, a race condition, like, changing it out from under you, right?
atoulme 00:56:46 Okay.
That sounds great.
jea 00:56:49 And so, that hopefully is going to result in, like, the next test that I want to run that I'm worried about, because I think it might just crash my laptop, is, checking what would happen as you try to do remote config with op-amp with the supervisor of the collector, like, doing a SIGHUP process.
And seeing how… how often you could do that with, transform… like, transform and filter processor versus these policies, and seeing what the performance, like, characteristics.
atoulme 00:57:21 That's true.
jea 00:57:22 from that.
atoulme 00:57:23 I have some… I mean, the way I would look at it is, we actually had a person come to us and ask about this recently. They wanted to do a partial restart with just one pipeline.
And we told them to get lost, because we don't know how to do this, right? Yeah. Like, but the other thing, of course, is that it's… you might be fine if your queues are empty.
Because one of the biggest problems of the SIGHub is that you're going to start… you shut down everything in order, and in orderly fashion, and you restart them all. And when you shut down, you have to empty your queues, that may take a modicum of time.
For sure, you're going to come up on top, but it might not be a big difference if the collector's sitting idle, but it might be a huge difference if the collector's very busy.
jea 00:58:07 Yeah. I think when it's busy, it's going to… Crash.
atoulme 00:58:12 Yep.
Every single one of those components is a source of contention. Like, anybody who's making a mess of shutting down things properly, you're about to feel it really tenfold.
jea 00:58:24 Yup.
atoulme 00:58:24 And you might not, like, for a TLP, you might just be fine.
But then one day, you're gonna try with Splunk Heck Exporter, and then we didn't do a good job with killing the HTTP client, or… bleh, right? Because we haven't tested that as close as we should have.
jea 00:58:39 Yup.
That's why, like, I think the idea of separating the… the routing logic from the, internal stuff?
Is going to be beneficial, because then… People are not configuring routers to that same level, right?
atoulme 00:58:57 I mean, we have Receiver Crater.
jea 00:59:00 Nothing terrifies me.
atoulme 00:59:02 But it should, but also, what I'm trying to say here, we already have this aspect of dynamicity in the collector today.
jea 00:59:08 Yeah.
atoulme 00:59:09 having the same aspect of dynamicity in the processor makes sense, and it's kind of… I'm just trying to give you a precedent if someone gives a crap about, oh, but what about the immutability, and how do I make sure things work the right way? It's like, well, we already do this.
So… It's completely scaring you. We just had a fun, problem with the JMX receiver. The JMX receiver was in the receiver creator, and it would tag all the Java processes running around, and it started to start one JVM per JMX receiver.
And it just went out of memory.
jea 00:59:43 I mean, sense. It's Java.
atoulme 00:59:47 Yeah, so the fix is, and this is why we're going to depict GMX receiver is we want it to be a separate process that runs on its own, and you're going to do some Helm deployment of that as part of your deployment of whatever.
jea 01:00:01 Sorry, say that one… say that once more.
atoulme 01:00:05 you're going to deploy this JMX Craper. There's… so the JMX Craper now is a Java jar that you can… you want to Dockerize this, and make it part of a deployment of a Java application, which, it's one more container in your deployment that is going to do all the JMX things that it needs to do, and then it's going to talk to whatever OTLP endpoint is local, and send that data. And then, therefore, it becomes the duty of the application to deploy its own GMX creeper.
And if you don't want that, then we can do some other things, as the demon set, or whatever, but it's going to be less fun.
jea 01:00:38 Yeah.
Yeah, but that's why you care about the, packaging group and being able to just install JAMX, like, directly in the application. Or with the application.
atoulme 01:00:47 Really, really tough, man, yeah.
jea 01:00:49 No, it's tough. I mean, it's a lot of coordination. I think the hard part is that, like.
Users want everything, and we need to have Golden Path.
But every organization is so different.
atoulme 01:01:02 I see a little bit of a change from users, it's like, tell us what you want. Tell us how it should be done, and we'll follow.
So there's also.
jea 01:01:08 Check. Yeah.
atoulme 01:01:10 there's a lot less opinions, like, back in 2021, I don't think you'd be able to make that statement, but we have proven to them that we were caring about this.
Anyway, I gotta go. Take care.
jea 01:01:23 No worries, me too. Thank you.
atoulme 01:01:24 Good job.
jea 01:01:25 Bye.
