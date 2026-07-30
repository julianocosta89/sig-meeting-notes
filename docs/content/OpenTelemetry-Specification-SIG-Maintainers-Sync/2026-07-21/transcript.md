SIG: OpenTelemetry Specification SIG + Maintainers Sync
Date: 2026-07-21
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 01:34 Hello, hi everybody. I think it's my turn to run this.
Let me pull up the agenda… Okay.
Please add to your name.
I have a few topics, if you have any topic you want to discuss.
Reset it here.
Let's give people 2 more minutes to join, and… I have quite a few PRs.
**SRIDHAR REDDY SURVI** 02:48 Hey, can you add my peer also into today's list, please? This is the first time that I'm joining.
**Liudmila Molkova** 02:56 Yeah, you, you can edit, I'll just… Leave a link in the chat.
And feel free to add your topic.
**SRIDHAR REDDY SURVI** 03:06 Okay.
**Liudmila Molkova** 03:14 I found out that we… our stale bot is not closing anything.
So we have a few PRs that's been… Pretty much dead, for example.
This one?
And nothing closed it.
So if anybody, if Antoine is here, or if anybody cares about it, please leave some Something on this PR.
Oh, I'm not transferring anymore, sorry.
Chair now.
Awesome. Works.
Awesome.
Cool, so… let's get started. There is a small… PR that we wanted people to know about, it removes the attribute ordering requirement from the compliance matrix. It was not… it's not in the spec, there is no requirement like this, but somehow it's in compliance matrix.
And somebody kind enough.
Helped us clean this up. I think. Carlos, he wanted to socialize it.
Carlos is here, do you… do you think we need to do something special?
**Carlos Alberto Cortez** 04:43 I just would like the Maintainers to take a look at this one. There was never actual, like, normative language around this, but this appeared in the matrix, like.
Regarding how attributes should appear in the way they were set.
we do a best effort thing at sea level, and that's all. But I would like Maintainers to take a double look, in case they think this is, something unexpected. But otherwise, I would say that we're relaxing the things for… You know, to make them easier, so it should be fine.
But I would say, if in a couple of days we don't get any more reviews, I think we're good to go, in my opinion.
**Liudmila Molkova** 05:35 Awesome.
So then let's move on. Josh, build those changes for product build.
**Josh Suereth (Google LLC)** 05:43 Yeah.
**Liudmila Molkova** 05:43 You wanna be that?
**Josh Suereth (Google LLC)** 05:45 No, it's fine. Like… if we present, it's gonna be a lot of ugly stuff, so I want to talk through what we're doing and why. But basically, BuildTools is a repository that is lovingly maintained very infrequently, but is somewhat core to, like, how we build and do things, and we are trying to get rid of a lot of components of it that were not well maintained, like, we got rid of some things for Weaver, GoBuildTools moved into a separate repository. There's a few pieces here, but the one that we really rely on for Protobuff is a thing that can build both gRPC and Proto For all the different languages to verify our protofiles are correct.
We do not expect people to depend on this, and we kind of warn them against doing so.
In various places. Yet people do.
So, I… what this attempts to do is bring it up to the modern era of versions and dependencies. So, there's a few things that were principles that I went into this with, was one.
We should not be downloading zips without having some sort of SHA check to make sure the zip is still the right zip, because that is a Salsa build compliance security hole.
So that's number one, what it does. Number two, we attempt to provide that same attestation on these things as in line with all our new security policies. And then number three.
try to get the latest possible version of all dependencies. I literally had to do some source code patching between, like, gRPC and Protobuf to get them to compile together at latest head for each one.
That, er, latest released version.
So that's fun.
And then, as part of this, we removed Dependabot.
The reason we removed Dependabot is because the versions of these source files that were being downloaded were never seen by Dependabot, never evaluated, never told us that we were out of date or anything, but we have many issues, both in the protorepo and here, that were people were like, hey.
The Proto-C is way out of date and is giving me warnings that seem like they're a problem. So, that's what this is attempting to fix. It's a bit aggressive, all in one PR.
But I just wanted to give you the chain of reasoning behind it. If you want to fragment it up, I can, but it was a pain in the butt to get this to build, because that… protobuf Docker image takes forever to build. So, I'm happy to make changes. I'm hoping that you don't want me to fragment out the build-related changes here, because that is rather expensive to test, verify, and iterate on.
Yeah, anyway, yeah, if you want, if you want to see, it's basically, we're using Alpine Linux, and we are using the version of Absal and Alpine Linux, and for some reason, some of the C++ types aren't getting automatically inferred, and so we had to add a couple casts here and there to get it to work.
Anyway, since this is not a… A thing that most spec Maintainers look at.
on a daily basis. I'm calling out… this is a, I think, a rather large and important PR for us to review and get through. Thank you, Florian, for the comments. I'm gonna make those changes. I don't know Renovate very well, so I leveraged what Gemini thinks Remini should be, or what Gemini thinks Renovate should look like, the config, and it looked reasonable, but I really don't know what I'm talking about with Renovate, and I can't test until it's submitted, so if anyone knows Renovate, wants to make comments, please do. I would appreciate that.
**Trask Stalnaker** 09:25 If you want to test it, the only… what I do is I push it to my fork, main on my fork, and I enable renovate on my fork.
**Josh Suereth (Google LLC)** 09:35 I am at capacity with things I can do on my personal account right now.
Because I have too many personal hobbies that are… so I can see if Renovate will run, but last time I tried Renovate it, it refused to do anything more for me, unless I pay them or something.
Anyway, I can try it out, but that's a good idea.
Cool.
**Liudmila Molkova** 10:05 Do we not have, maintainers for this repo anymore? Like, I… unrelated to your… to your PR, just who… like, spec sponsors is great.
**Josh Suereth (Google LLC)** 10:17 No, the… technically, I should not be a maintainer of this anymore, either. The maintainer is the OpenTelemetry Technical Committee.
**Liudmila Molkova** 10:28 I mean, you can be a maintainer of this repo if you want to.
**Josh Suereth (Google LLC)** 10:33 Right now, I think nobody wants to be the maintainer of this repo, is part of the problem.
So I, I… follow-up work here, I might end up moving the Docker build to the proto… the proto-repository as well.
And then have a weird cycle where we build and release that as part of Proto.
And then use it in Proto for its own build and release cycle, but… The main reason this exists is if you don't build it once and share it, the build times for the proto-repo go from about a minute to, like, you know, 30 to 40 minutes.
**Liudmila Molkova** 11:15 Yeah.
Cool, so then this anyway comes independently, and if it happens… here, it can later on be moved to Proto repo, and can be released every once in a while from the Proto repo, and then, yeah.
**Josh Suereth (Google LLC)** 11:35 If we do something in Protorepo, it would just be a copy-paste of this, it would not be, like, yeah.
Okay. The second thing, because I'm also the second thing, this is somewhat related, because I've been trying to go through proto-related bugs and fix them.
I think you saw, posted a, Agentic triage skill that has, like, a set of… themes around things to fix in Proto. And actually, build, tool, release, CICD issues were one of the number one things that we had that have been hanging and open for a while, and they're all kind of legitimate. This next one is around the, Blaze support. Not Blaze, Bazel. Sorry, Blaze is the internal Google version. Bazel support for Bazel Build.
And there's this Bazel repository where you can push packages, where it builds from source code.
This is an interesting one, because I think there's a decision here that I wanted to make as a community.
Right now, in Proto, we do not recommend using that proto… the file you just saw. We don't recommend using that for, client-side libraries. Similarly.
we don't actually build client-side libraries in OpenTelemetry Proto for all the different languages. Instead, we ask language SIGs to maintain building their own protos. And some of them have actually made custom implementations that aren't the same as, like, Proto-C compiled things.
we found issues with ProtoC, where it's not always binary compatible, etc, etc. Okay, the hard problem here is there was some submitted, Bazel support.
Bazel builds everything from source.
The Bazel support is not working because we need a build file locally to build our proto repo.
Building locally means building everything from source, which takes the build time up to that 30-minute build time again.
It's also kind of against our policy where we aren't building client libraries from source.
So we have two potentials here. One is, we pull in Bazel builds into the proto repo, and actually support them ourselves, and publish to the Bazel module system.
our repository.
Option number two is we say, actually, we're not going to support Bazel out of the box. The Bazel community needs to provide its own support, and they can actually issue pull requests to the BCR repository in Bazel Community, and put overlay builds and things, and maintain everything themselves. And it's not going to be part of OpenTelemetry Proto.
I'll be honest, like, as an OpenTelemetry maintainer… so, as someone who works at Google, obviously I want Bazel support, but as an OpenTelemetry maintainer, I would prefer not to.
For a variety of reasons.
But I wanted to run that by everyone and see what we think. You can look at the issue, you can look at the comment and the back and forth we have, you can look at the PR, which I plan to close, depending on the outcome of this discussion, but the PR basically tries to fix BCR publishing.
And to do so, I wanted a test that would validate whether or not BCR Publishing works, and I had to create a build file and a module file.
The build file and the module file look like they will not work unless they're actually part of our repo itself.
So, I would have to change it that way. And this build verification check takes about 30 minutes to run, last I ran it on GitHub. So, I'm kind of not happy about both of those things. Unless we as a community say.
we want Bazel support natively, in our proto repo.
So I'm just gonna open it up for thoughts from people. My tentative proposal is to close this PR and open one that actually removes Bazel support and says that the Bazel community should self-service.
**Florian Lehner** 15:36 I'm not sure I can bring much input here, but, I just released, created a new release for the Proto repository, and, Bazel, publishing failed, for various reasons. So…
**Josh Suereth (Google LLC)** 15:52 That's… my PR should fix that failure.
But it can only fix it if we have a Bazel module defined locally. Like, that's… so the failure you had in your release, that's what that PR is supposed to fix.
**Florian Lehner** 16:07 Yeah, my problem is that I… I don't have… knowledge on BCR and Bazel that I can give a judgment, or investigate, or… help or fix this issue. That is just my… My problem.
**Josh Suereth (Google LLC)** 16:26 Yeah, I… I hear you. That's, that's why this PR exists, is because I was looking into the failure from the last release that we did.
And trying to, like, fix it for real, before you made your release. I didn't make it in time, because I ran into all sorts of other problems. So, I think the reality is, do we want proto Maintainers to maintain a Bazel build?
If the answer's yes.
I can change this PR and make it so that we have a Bazel build in our proto-repo, and we can, you know, support it going forward.
If proto Maintainers do not want to maintain a Bazel build, we should remove the current BCR publishing, because it will not work unless we have a local Bazel build.
That's what we found out. In the comment thread on the PR, you can see one of the Bazel users found that. And we would say, okay, we're gonna remove it from our build, and we're gonna ask the Bazel users to maintain their own fork.
in the Bazel Community Repo GitHub, where they can do overlays and all sorts of shenanigans to use our Proto files just fine, which is what they're doing for, I think, two… the previous two versions of Proto, or there's a version in there that you can use that's stale.
But it's working. So they would just, like, update that to latest.
If no one.
**Liudmila Molkova** 17:43 That's.
**Josh Suereth (Google LLC)** 17:43 Same opinions, that's an answer in itself, by the way.
**Liudmila Molkova** 17:47 Yeah, it sounds like it.
Do we have Tigrin, or somebody who works on Prado?
And since we don't have Tigrin… Yeah, and it sounds like it doesn't work now.
And it probably hadn't worked for a while.
**Josh Suereth (Google LLC)** 18:10 It never worked. The initial PR was, we're gonna submit this, and then after release, we're gonna see what we have to fix.
So this is the after-release, here's what we'd have to fix. I figured it out.
**Liudmila Molkova** 18:22 And nobody cared about it.
**Josh Suereth (Google LLC)** 18:24 Well, I don't want to do it, is what I'm saying.
Like, I… here's… the reality is, I don't think anyone who's a proto maintainer will maintain the Bazel build.
And so, if no one's willing to stand up to say, we want to maintain this going forward.
I think we just remove it from the build. So I think that's the answer I'm getting here. I will open an issue for comment and leave it open for, like, a week before I actually remove it, but I'll close my PR with that as a comment.
**Liudmila Molkova** 18:55 Awesome.
**Puneet Singh** 18:58 Just a point that we might want to announce this in the OpenTelemetry channel, because when I was looking into it, I found that C++… Sdk of OpenTelemetry depends on the… The basel, proto-dependencies, so… They might be impacted by this.
**Liudmila Molkova** 19:31 Okay, anything else on this?
We'll then move on to the next topic. Robert for Love is Jack on… Attribute depth limit.
**Robert Pająk (pellared)** 19:48 I'm not sure if Jack is here, because Jack said that he won't… he blocked his PR to follow up this week.
So… I think we can just skip this.
It was the latest comment, first on the bottom.
On the bottom.
**Liudmila Molkova** 20:04 Right.
Why doesn't it bring me there?
**Robert Pająk (pellared)** 20:11 Amazing, from the bottom.
Sorry, I saw one comment.
**Liudmila Molkova** 20:22 Okay, so you wanted to ask if Jack had any, if he has tried it.
**Robert Pająk (pellared)** 20:28 Yep.
**Liudmila Molkova** 20:36 Okay, so we will put it into the next meeting.
Done?
Okay.
The next topic is from Riccardo for the continuation strategy, and you are… Asking for reviews.
**Riccardo Magliocchetti** 21:03 Yep.
Yeah, like… If you remember the story, like, visa has been proposed some times ago.
as some addition to the propagators, and after the feedback from reviewers, this has been reworked as an SDK component instead.
We've got, fairly thorough review from Tyler, and thank you for that.
Yeah, like, I think I addressed all the comments.
At least the one from Dyla.
And if anyone… Wants to take a look?
Feel free to, and Eager to wait for more comments?
Thanks.
**Liudmila Molkova** 21:53 Hmm, interesting. Is it using the policy? The new policy proposal, or is it something new?
**Riccardo Magliocchetti** 22:03 Come again?
**Liudmila Molkova** 22:06 Not sure if you have seen, there was a policy OTAB that proposed some… something very similar, but not through, necessarily, through declarative config.
**Riccardo Magliocchetti** 22:21 I'm not sure… like, do you mean the telemetry policy OTAP?
**Liudmila Molkova** 22:25 Yeah.
It's something else, not related.
**Riccardo Magliocchetti** 22:29 Yeah, yeah, not related.
Let me see select for deciding.
Where to start, or not a new trace?
At Ingress?
And… doing the same, like, where to decide if inject or not, trask context on Aggress.
**Liudmila Molkova** 22:59 Conditionally based on… this pan properties.
**Riccardo Magliocchetti** 23:04 Yes.
**Liudmila Molkova** 23:06 I see.
**Riccardo Magliocchetti** 23:09 like, attributes that most of the time comes from… they are the same that are on the… The spong, yes.
**Liudmila Molkova** 23:24 Cool, I will take a look. I am curious about, In this in general, but also the slightly related scenario of External versus internal context.
Where you would, want to keep the external context and pass it around.
But internally, for your… within your services, you would want to trace Things, independently, but it probably can't work together.
**Riccardo Magliocchetti** 24:03 look forward.
Will you refute that?
Thank you.
**Liudmila Molkova** 24:12 Yeah, thank you.
Anybody has any comments?
Cool, then moving on to the next topic, the issues, Diego.
**Diego Hurtado** 24:30 Right, okay, thank you, Liudmila. So… Last week, we just, we had this discussion about, Having, like, 600 and so issues open, and still issues, and what we do about that, and… If you want to close them or not, and so on, so… I offered to do two different things.
One of them was to ask Cloud to take a look at all the open issues that we have.
And… Report back with the issues Cloud believes.
Can we close?
And the other thing was, to… I'd, PR… With, changes to the contributing document.
Saying that, explaining… adding a section that explains Why… An issue was closed, and basically telling the user.
Hey, sorry that we closed your issue, that doesn't mean we don't like you.
Please, keep contributing.
I just want to explain myself better, because I think there's a lot of confusion Regarding the intention of these two different things?
First thing I want to explain is that these two things are completely independent of each other, they are not related.
the effort here could happen without that PR, that PR could have happened without the effort here. I'll start with this one, okay? So, what I did here was just, suggested Ask Cloud to take a look at the open issues and tell us which one Which ones can be closed?
Then I added a comment in every one of these issues, with, a short description of what cloud thinks, and why this issue… why cloud thinks this issue can be closed, right? The intention here is not to just let an AI agent to make the decision for us and close things automatically. That's not the intention here, I just want to clarify that. The intention here is to use AI to assist us In identifying issues that can be closed.
And, make it easier for whoever is gonna review these issues to make a decision.
So… The idea is for a human being to read that comment into that issue, and then make a decision. Okay, yes, this issue can be close or not, so… So far, what I did was, grouped these issues by author, and I contacted a bunch of people.
Who opened these issues and told them, hey, you open these issues, Cloud thinks they can be closed, please take a look. If you think they can be closed, you can close them. If you think cloud is wrong, you can just leave them open, right? So, I think that was pretty effective.
In one week, 54 issues were closed, mostly by their authors, right? So… So, yeah, I think, this is useful, We identified there, many of… many issues that were, like, completely obsolete, like, stuff that was related to GA, 6 years old, and so on, right? So… So, yeah, there was… I think there was some confusion.
And what I was trying to do here, so I just wanted to clarify this.
And, well, now, if anyone has any questions, comments, I'll be happy to answer any questions.
**Liudmila Molkova** 28:55 I think last time we talked about, okay, there could be, whatever, AI-assisted, AI-driven, human-driven, practice that triages issues and, closes the ones that are not relevant anymore.
There is another process of, like, scaling issues and closing them after a certain amount of months, like 12, 24, whatever the number.
And, these processes are essentially similar.
But the stale, issue thing would… provide… would be consistent, it will run in the repo, and it would not require anyone to spend their time or tokens on this analysis.
And deterministic check That is then later enforced by somebody, coming back and saying, no, actually, I care about this issue.
is a much stronger signal than AI would give otherwise.
Right, so many of the issues that should stay open, they just don't have enough context. They are relevant, but you need the author of this issue to actually come back and tell you things. And maybe sometimes it's better to close it.
And just let it… somebody else create the actual issue.
**Diego Hurtado** 30:17 Yeah, that's another way of, doing things.
The problem I see with that approach is that, an issue Can still be valid.
Many months after… It was opened, even if it has no… no, If nothing is happening, if nobody's, talking about it, the… And, something else that you mentioned was that, It was important to close issues Using human judgment, And just… And that is, in my opinion, not using human judgment, right?
It's just a…
**Liudmila Molkova** 31:09 saying that it's, like, AI… human judgment costs a lot.
and… using… like, we cannot delegate it to AI, but if it's a deterministic criteria, then author of the issue, who cares, and comes back and says, okay, you're going to close my issue automatically. Actually, I do care. This is human judgment.
**Diego Hurtado** 31:35 Alright, okay, that's fine, I think, you and I are proposing different ways of handling issues, which is fine. I think, we can continue that conversation.
maybe in a separate issue or something. I just wanted to clarify my intention here, because, I thought, it was… I was under the impression that there was some confusion.
maybe somebody else has any other questions or comments?
**Michele Mancioppi (Dash0 Inc.)** 32:16 I mean, if I understand correctly, the proposal, the two points of view that you and Ludmila have expressed, they are actually complementary.
So there is the staleness based, simply on time.
Which leaves us with potentially a large amount of, dad issues NPRs for a very long time until they get cleaned up.
plus a proactive, on-demand, best-effort thing like Digo's doing.
I do not see them as… Competing as approaches.
And I also am not sure whether the time-based stillness markers is something that we're doing consistently.
At least I am pretty sure that is not the case, given some of the repos we have, where there is stuff from 2 years ago that is not… is still open, right?
**Diego Hurtado** 33:09 Right, actually… Both… we could have both things. We could have, an AI process that runs, I don't know, every month or something, that tries to identify issues, and… and we could also have a deterministic automated process that just closes them after.
some months.
We do not have… Any of those in place right now?
We identified, with this process, we identified issues that were, like, 6 years old.
And we're completely obsolete.
There's something, related, Can someone take a look into the PRs and find mine, please?
**Liudmila Molkova** 33:57 This one?
**Diego Hurtado** 33:58 Yes, thank you, thank you very much. Right, this is, what I mentioned earlier.
In last week, SIG, I… I volunteered to add this to the documentation.
And what's happening here in this PR, is just, user-facing documentation. I'm just adding… Documentation that says… If your issue was closed, We… please don't take it as, Please don't take it personally, we still like you, we still want you to contribute, right? But… For technical reasons, sometimes we need to Close issues, right?
Ryan, this is something that, I think it's, It's useful right now, because right now.
From what I understood in the PASSIG, Something that is happening.
Two Maintainers is that they are… Reluctant to close an issue because they don't want, to give to give that impression to people who are coming from the community and trying to contribute, right? So, many issues that people think should be closed don't get closed.
Because, Maintainers don't want to do that. So the idea of adding this documentation is helping Maintainers Close these issues, and have something in the user-facing documentation that explains why.
Again, this is independent from what I was… what I'm doing in the other… Issue we just discussed.
And, I think this is something that's good right now, because, right now.
we don't have in this documentation, so I just wanted also to clarify my intention here. Something else that I noticed in the comments in this PR Is that there may be a disagreement regarding How valuable is the… is keeping… is closing issues that we think are no longer relevant. From the comments I read, I feel… That there is some disagreement that there… that, I personally think that we should close issues that Are no longer relevant?
And that means keeping the issue counter, number as low as possible, but I feel that there is some discrepancy here.
And, and other people may not feel that is, that important. So, if there is some comments or questions, I am… I'm happy to clarify anything right now.
**Liudmila Molkova** 37:10 Maybe, Tyler, you want to comment? I don't read Tyler's comments as, let's not close issues, but more like that the language you use is… that, way… Here, in this text.
**Diego Hurtado** 37:31 Yeah, I removed that part, just to… Just in case.
**Liudmila Molkova** 37:37 Sir?
**Tyler Yahn** 37:43 Yeah, sorry, I can't talk too much on this one, but, yeah, I'm, like, I'm fine with closing issues, I just… we need to make sure that… I think… the way we're communicating these things is really critical.
You know, saying things that are, like.
just very hollow is not gonna come across well to people who have their issues closed. That's why I'm also kind of more partial to Lududmila's proposal, where we just close these things based on some sort of staleness policy. Like.
It's a lot easier to justify closing things when it's an impersonal versus some subjective, personal thing that, like, we don't think this is important or something like that.
So, I mean, I'm fine with whatever way we want to do, but I do make sure that, like, we communicate this in, like, an authentic Not, like, placating way.
It's kind of critical for me here.
I do think that, like, I am… Of the opinion that, like, if we want to close issues, like, we should probably Ask yourself if that's our… if our goal?
or, like, if we're trying to structure backlog, is our goal? Or if we're trying, like… like, what is our goal here? Because, like, closing issues itself is not necessarily, like, the goal, I imagine. It's… we want to try to have some sort of organization and structure.
So that needs to, I think, be really, like, focused on. Can we achieve that with a roadmap? Can we achieve that with, like, milestones?
I think it's kind of also the other thing, and I think if these are… better define what our goals are. It's a lot easier to say, like, this issue is closed or this issue isn't closed for these reasons because of policy, not because of, like.
Oh, you know, some subset of, like, the Maintainers or some group of approvers think this is no longer relevant. I think it's a lot easier to say, like, this does not align, or this does align, and I think we have a lot better strategy at that point.
**Diego Hurtado** 39:46 Right, you're seeing, milestone… Or any other mechanism to track progress is… Not related to this… Topic here, Perfectly fine with, using any kind of mechanism to track progress?
the… Yep.
**Tyler Yahn** 40:18 I think… I think it is, is my point, though. Like, why… why are you closing issues?
Because, like…
**Diego Hurtado** 40:23 the.
**Tyler Yahn** 40:23 There's a number… there's a number on, like, a UI, right? Like, that means absolutely nothing.
So, like, what is the engine here?
**Michele Mancioppi (Dash0 Inc.)** 40:29 Nope, that's good.
**Diego Hurtado** 40:31 That's right.
**Michele Mancioppi (Dash0 Inc.)** 40:32 I disagree.
There is, When you go, when you see repositories with hundreds of open issues and open PRs, it doesn't look well maintained.
**Tyler Yahn** 40:48 Yeah, but I mean, I, like.
**Diego Hurtado** 40:49 Exactly.
**Tyler Yahn** 40:49 Okay, so… so your goal then is that you want to show some sort of, like, active maintainership here.
Right? Because, like, that's the action goal. I also think that it's, like, a subjective feeling to say that, like, that is reflective.
In a positive or negative way.
Like, that's, you know, maybe that's just your opinion, and you need to make sure that you understand that that may just be your opinion.
And… I think if we can… if we can say, like, oh, we want to actually show this is a well-maintained project and this is validated, like, that… that sounds great, but, like, let's actually talk to the people that would be responsible for that, because I don't think that the voices in this conversation are reflective of that.
**Diego Hurtado** 41:27 Well, first, yes, that's my goal to… keep that number representative of the things that are actually, waiting for some kind of work for some… from someone, right? Issues that, I believe, are stale or something.
Reflect negatively on… on that number, and I… and I also feel like the… Last week, we discussed about, the fact that there was a huge number there, 600 or something, and people were not happy about it, so this is an effort.
to help here.
No.
**Tyler Yahn** 42:11 Yeah, I mean.
**Diego Hurtado** 42:12 I get that.
**Tyler Yahn** 42:12 I guess that's, like, something, like, that you're trying to do, and I applaud that. I really do. Like, thanks for putting the effort in. Like, this community… Values these kind of things.
But what I'm saying is that, like, Are you focusing too much on the method? Because, like, even what you just said there might be different than what Michele was saying as well.
like… I, like, I don't think that, like, we're actually aligned, and, like, if our goal is really to just drop these numbers down at the expense of, like, our broader community and their feelings, like, that's not appropriate. If it's to drop these numbers down because the broader community would like that, I think that that's, like, really good feedback to know. But, like, saying that, like.
We just know this without actually having any feedback is unfounded.
**Michele Mancioppi (Dash0 Inc.)** 42:59 I, are we sure that the community is… Nice to have a niche open for 6 years without anybody interacting with it.
And that is… less.
Emotionally relevant than having that closed in a reasonable amount of time.
**Liudmila Molkova** 43:25 I feel like we have a solution, we have a tool.
That's easy, that's cheap, and it's effectively enabling the stale issues in the existing stale PR action, and we can just start with this, and this will close maybe a few hundreds of issues, and we probably wouldn't care about it anymore. But if we still do, we can keep going.
**Diego Hurtado** 43:51 I… That… I think that's not the same thing. Again, Look.
what I… what this PR is doing is very simple. It's just telling users, your issue got closed.
please don't take it personally, we may… we sometimes need to make that decision of closing an issue, and that can happen for any reason. That can happen because an automated, The mechanism closes automatically, or maybe it happens because we actually, or Maintainers actually feel like That issue is not relevant and can be closed.
So, having this documentation here is not affecting any process, or that can close issues. We can have this documentation here, and we still can have a mechanism that closes them after a certain amount of months, or we can have an AI automated process, or whatever.
my message here is that this PR is completely separate and different from… and separate from… from all those topics. This is just that in documentation saying, if your issue got closed.
Please don't take it personally, it was just a technical decision.
And please keep contributing. And that's it. That's… that's what I want to clarify here.
**Liudmila Molkova** 45:16 Yeah, awesome. So then, assuming we, we don't do this to justify individual humans closing issues, and we do it automatically. The ask here is to review the language.
And… Well, I will probably review it, and I'll lose some feedback, but it sounds to me that in this context, this can be, trimmed down to Just a few lines explaining things.
To match the text around, because, well, this looks like, maybe way, way too human, comparing to everything else we have, and maybe a little bit, AI-generated.
I think the ask here is to find the right words to describe this, and it makes sense.
**Diego Hurtado** 46:09 Yes, thank you, any comment, Related to… Trust?
**Liudmila Molkova** 46:22 Trask, you have your hand raised?
**Trask Stalnaker** 46:28 Okay.
No.
Yes. Yeah. I think what I was hearing was that If we do… was to do the issue staling first.
Because, like, this would be covered in the staling message when it auto-closes. Like, we could review that wording in the, PR that enables the issue staling closing And may not. And then, kind of, see how that goes, and see if there's still need and desire to add more layers on top of that.
**Diego Hurtado** 47:20 Yeah, but that's something that still needs to be discussed, right? We could… Add this here as a first step, because we actually have zero documentation telling users, hey, why my issue was closed right now.
**Liudmila Molkova** 47:40 This, I mean, it… I see what you're saying, Diego, and we… we can do this, we close PRs.
already using the same approach, and there is a message in the stale issue. Does anybody want to enable stale?
issues the illness to start with.
We can polish the words and… add them.
Independently of this practice.
**Trask Stalnaker** 48:09 As I mentioned last week, I found it useful in… I resisted enabling it in the Java instrumentation repo for a long time, like, but then as the issue number got out of control, or large, and the number of years of the project got long.
it felt like the right thing to do, and I don't remember, it's been at least a year or two since we did it, and I'm very happy with that decision.
**Liudmila Molkova** 48:47 That's awesome. I rented…
**Trask Stalnaker** 48:49 We haven't gotten pushback from users. I mean, occasionally somebody will comment on the closed PR and will reopen it.
**Carlos Alberto Cortez** 49:00 I have some questions that I will probably ask offline, otherwise we will keep on going in circles now. So I will ping you, Trask.
**Liudmila Molkova** 49:11 Okay, I want to give some time to the final topic, the feedback failover endpoint support for GLP exporters.
Sridar, did I pronounce your name right, or…
**SRIDHAR REDDY SURVI** 49:22 Yeah, yeah. Can you help me? I pronounced it right.
So, means.
I want to introduce myself. My name is SRIDHAR. I work for Mastercard. I'm currently observability lead, and we are shifting our strategy from vendor-dependent agents into completely open telemetry stack, and We have been investing heavy amount of, effort in migrating that. So, as part of that, when we are migrating our stack to OpenTelemetry, we found an issue. So, as MasterCard, we have many data centers. We are very strict, very strict on the reliability the applications and also the reliability of the observability ecosystem. So, we have OpenTelemetry Collector set up on, primary site, DR site, and we have other sites as well. So when one collector goes down, then the apps should be able to send the data to the other collectors in other regions or other sites.
consider that as an AZ, maybe.
availability zones, different availability zones. So currently, the only way to do that is we need to have an F5 or load balancer, to do this, but that is very infra-heavy.
way. What my proposal was to have some kind of a way where the OTL SDK itself detects the failures coming from the collector.
and it decides that the primary is not working, then I'll use a fallback endpoint. So this way, this will avoid having heavy infra-based load balancing and failover mechanism to a very simple switch on the agent side.
So, I've raised this PR for that, and I also have the code ready, but as this is the new… this is the first time ever that I'm interacting with open source community, someone from the community suggested that I need to raise a spec here, and I need to work through this.
**Liudmila Molkova** 51:42 Yeah, the ask makes sense. I'm curious if we heard this.
In the past, does anybody remember?
Yeah? Riccup?
**Michele Mancioppi (Dash0 Inc.)** 52:02 I do not remember this coming up before, but what it is reminding me of… Is all the exporter queues in the collector.
So, what I, what I would expect is… This to be… Largely resolvable today, but running… a sidecar container near the applications and use the exporter queues instead of changing every single exporter and every single SDK, and that strikes me as the better way to tackle it.
**SRIDHAR REDDY SURVI** 52:36 Yeah, so on the sidecar approach, we thought about it, but the Sidecar was heavy, because all of our applications are using PCF.
And having the resources shared along with applications will have an impact on the applications, resources, and it will have an impact on the actual transactions. So Sidecar was not an option for us. I explored that option, that was the best option, actually, but, we didn't want to, Butcher the performance of the application by adding more, Details, a more, heavy side, heavy application into the code.
**Michele Mancioppi (Dash0 Inc.)** 53:18 I assume that by PCF you mean Pivotal Cloud 100?
**SRIDHAR REDDY SURVI** 53:22 Yes. Cloud Foundry, yes.
**Michele Mancioppi (Dash0 Inc.)** 53:26 I have more than a passing notion about that. If you want, you can take it offline, and we can talk about a better solution, because in your case.
what I would advise you is to… is to run a Bosch deployment, adding a set of VMs, running the collectors, and buffering it in there. It's, what you want to achieve with this, with this spec change would take a significant amount of time to roll out and become useful to you.
while you can have a solution that is composable to your current PCF setup.
Right away, that doesn't complicate further the code of the exporters.
**SRIDHAR REDDY SURVI** 54:07 Yeah, so the problem with that is, our PCF, our Cloud Foundry infrastructure is completely horizontal, and it is shared. So… our infrastructure teams are very reluctant to touch or change anything. In fact, they have disabled the dockers also, so they have very limited set of access that they give it to the application users to deploy. So that's where we are, like, stuck in that place.
And the sidecar approach, the bigger challenge for us was we have around 20,000 microservices running in our ecosystem. Adding this sidecar in all of those 20,000 microservices will be very heavy.
And it is, like, too big of a effort for us to work on.
Yeah, this solution works really, really good if we use Kubernetes or Docker or any Cloud Foundry, public cloud places, but when it comes to a restricted Cloud Foundry environments like cars, this has become a challenge for us.
**Antoine Toulme (Splunk Inc.)** 55:23 Michele. I think we were overeating on Slack over the weekend.
So, I'm going to repeat what Michele just said, because I agree with him.
you want to be using a sidecar for this because of multiple reasons. The main reason for me is actually, even before we get into the discussion of having multiple fallback endpoints or anything like that, if you want to have a buffer, you don't want this to be your application memory. You want this to be a separate place.
It's actually very, resilient this way, because the collector is meant to do these retries and manage its queue and all those things, and there's been a lot of work that's placed into that.
If you make the application smart enough to be able to buffer and retry and try different backends and whatnot.
And inadvertently, you're going to worsen your runtime, and this is based on real experience. The other thing is, back again to what Michele said, PCF is actually a very mature ecosystem for this. There's a number of add-ons, we maintain one.
that are allowing you to run a collector as part of your PCF orchestration. And I know that the… PCF has been also working on OpenTementry native support. We've seen some of them, sometimes at KubeCon or other places, where they've been, very public about some of their plans to have a collector as part of PCF.
So, I would ask them what's the latest on that, and kind of identify with them how to go about this, if possible, and kind of push them to give you Something to work with.
**Michele Mancioppi (Dash0 Inc.)** 56:57 Yeah, I would like to, to stress what, what, Antoine said.
If you buffer telemetry inside your, your Diego cells inside your containers, you have absolutely no guarantee that that telemetry is gonna get out.
The moment that somebody triggers an update of the landscape, and you turn.
The, the trigger cells, it's gone.
The moment PCF wants to rebalance the load, it's gone.
So it doesn't actually provide you with a better setup. If you want persistence for telemetry, put it on file with a shared volume, and the route that Antoine is talking about with the add-on is the correct one, in my opinion.
**SRIDHAR REDDY SURVI** 57:45 So, can we, use Kafka as our buffers?
**Michele Mancioppi (Dash0 Inc.)** 57:49 Absolutely. What you could do is to have, the… I mean, there are… Very few.
exporters that I know of outside of the collector to write to a Kafka topic, but if you deployed an array of collectors as, As, an add-on, and have your, your, your applications running on Diego, actually talking to the collector, and then the collector puts it on Kafka, you get to a very similar setup to what I was telling about with the file export queue.
And… And you have all the variability of Kafka.
**SRIDHAR REDDY SURVI** 58:30 So this is on the collector side, but we want to have this on the agent SDK side.
**Michele Mancioppi (Dash0 Inc.)** 58:37 Yeah, what you could do in that case is to create exporters that talk to Kafka, and then mount Kafka as a CF service inside your application. That would work.
I am not aware of Catholic exporters.
been a common thing across other SDKs, though?
That's something that you may have to do yourself.
**Liudmila Molkova** 59:00 Yeah, we are almost out of time, and before we say bye, thanks for coming through there. Have you explored the alternative, Jack suggested here, to just, implement the fallback inside?
Exporter.
Was your… you can have, like, a rubber… That'll get to an exporter.
This would be the…
**SRIDHAR REDDY SURVI** 59:27 This is on the collector's side, is it?
**Liudmila Molkova** 59:29 No, this is on the SDK side, inside your application.
**SRIDHAR REDDY SURVI** 59:34 Oh, okay. Yeah, let me explore that, I have not seen, I guess.
Let me see.
So his speech has just… I'm so good.
**Liudmila Molkova** 59:44 Cool. Sorry, we are out of time. I appreciate everybody joining, and see you around.
**SRIDHAR REDDY SURVI** 59:51 Yeah, thanks, Mike.
**Liudmila Molkova** 59:53 Thanks.
**Trask Stalnaker** 59:55 Bye.
