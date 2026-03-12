SIG: Security Governance SIG
Date: 2025-08-04
Duration: 29 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 01:52 Good morning, Fox.
**Jeremy Corley** 01:56 Morning.
**Trask Stalnaker** 02:01 Happy. Monday.
**Reiley Yang** 02:04 Hey! Hey! Molly!
Share my screen.
**Trask Stalnaker** 02:17 Whoa!
**Jeremy Corley** 02:18 Bye.
**Reiley Yang** 02:25 Yes, I have 2 quick topics, and I remember trust you mentioned. Maybe like this month you will look into 3 or some like auto scanning tool. So 1st one, just a quick link. So please take a look at the the pr, the the main idea is, I'm trying to solve the issue where the current Maintainers and the Tc. Is looking at a list of security issues. But this is not a good list. So I'm trying to clarify what people should prioritize. The main issue, I'm seeing is people treat security advisor is more important, like, if someone report an issue. But they. They have an existing repository where there are a lot of dependencies, and some of them are critical Cve and high cves. There's no advisory, because nobody is reporting that so, my my take is they should look at advisories and the supply chain security, like all the Cve in the dependencies, and and have a single list and prioritize that.
and anything as critical or high should be treated as high priority. So I'm trying to clarify that. Please take a look, and I already informed the Tc. I want them to take a look as well.
The second one is kind of related to security, and also the admin given task here. I want to quickly talk about that. So if you look at the spec report currently, the spec approvers have a corresponding group. But the Spec Maintainer is just using the Tc group, and the Treasurer is in the Gc. Group. And if you look at other repositories like the protocol.
I I see similar issue there. So I I would suggest we have dedicated groups like Spike approval, Spike Maintainer, just for consistency and for the Spike Maintainers. We can add all the existing Tc members. I'm having to maintain it for now. And the Tc. Has some discussion. The idea is, maybe we'll have additional maintainers that are not Tc members. So I think just having this consistency is good.
**Trask Stalnaker** 04:36 So let's see, I was pulling up the list.
so triagers. Oh, I see. And you're suggesting that the yeah, the Gc.
Be the triagers.
**Reiley Yang** 04:51 So, yeah, so in the in the spec report, currently, if you look at the treasures, we just list the Gc group. My suggestion is, we create the Spike trigger group, and we can add Gc. As a subgroup, or we can add all the existing Gc members that would allow us to evolve like. If we have someone who's willing to do the spec triage work, we don't necessarily have to put them in the Gc. They can still be a treasure.
and like, I want to do that across the Repository to have consistency.
**Trask Stalnaker** 05:23 So let's let's make a list of which repos this would affect specification. Proto, you said.
**Reiley Yang** 05:33 Broad. Hall. Yeah.
**Trask Stalnaker** 05:41 Any others?
**Reiley Yang** 05:44 I guess maybe the community report I haven't checked yet.
I can follow up and and put a full list, or I can even send a Pr. If that's something like you want to explore.
**Trask Stalnaker** 06:04 I think the community repo I sort of like it being the Gc. Team itself, because it makes it clear that these are governance.
Issues decisions.
Although it's a little murky, right? Because we also some of it's tc, but I think at that level the Gc. And Tc. Ownership of that make sense to me.
But the spec and proto.
yeah, I mean, I totally agree. I think that's and it seems like from prior discussions with the Tc. That's the direction that you all wanted want to go, anyways.
So if you want to implement that sooner, I would just maybe just ask in the Tc. And just make it a Tc kind of decision, since you all own those 2 repos anyways.
**Reiley Yang** 07:09 What I asked. We we discussed that last week.
**Trask Stalnaker** 07:13 Okay, so the as the Tc, you all want to add Maintainer and Triager groups.
**Reiley Yang** 07:23 We? We don't have the full Tc members in the meeting. So most folks there seem to be okay. I'll send the Pr. And get feedback anyways.
**Trask Stalnaker** 07:32 Cool. Yeah, yeah, I think the I'm I think I've just fully defer to the Tc for those 2 for that decision on those 2 repos.
No objection. I have no objection.
**Reiley Yang** 07:45 Okay.
Thanks.
It's your turn.
**Trask Stalnaker** 07:50 Yeah, yeah. So yeah, let me share. And it's very much also connected to your 1st topic. So we can talk more. About that.
So actually, let's start with your so for vulnerability management, right? So, this, I mean, I yeah, I totally agree with this? The question I have is.
do we want to publish this sort of tool agnostic?
And I guess that's I mean, it may be beneficial to have tool agnostic guidance for repos and maintainers who want to use a different tool.
But I think that we'll have. We'll get more compliance, if we can.
at least, in addition to this, publish, like some clear, some specific, a specific tool that we recommend.
Cause, I have a feeling that will be the maintainers. 1st question back to us is, What does what tool does the security recommend.
**Reiley Yang** 09:33 Yeah.
So here's my thinking, like, first, st I want to explain to the Maintainers, why are we trying to do this? And what are we trying to achieve. And what are the things that you, as a maintainer, should take care of? Then we can take feedback.
We can find the right balance. Then the second part is, if people agree, this is the right thing to do and right thing to prioritize, then we give a suggestion on what are the tools that can help to cover, maybe like 80% of the things automatically for you, then for each repository the Maintainer still has to think about whether they have some specifics that tools won't cover, then they can define their own thing. But, like covering, 80% is already good than the current state.
**Trask Stalnaker** 10:17 Yeah, I mean, maybe I I like that kind of rollout.
makes sense to me like, if you want to take this to the Maintainer spec Maintainer meeting at any point. And just sort of start socializing.
Yeah, yeah, idea.
I think it's a good time. Yeah.
And yeah, I'll keep poking around on the on the specific tooling.
But let me share what?
So I tried out trivia, and it seemed decent.
Right, it produced. Let's see if I tried it on this repo security.
Let's see. So, Code, scanning on Github, you can do it.
No, you can't.
**Reiley Yang** 11:41 Okay, while it's thinking, let's try that.
And you feel comfortable sharing the security vulnerability on the screen.
**Trask Stalnaker** 11:50 It's a good question. It is in my fork.
**Reiley Yang** 11:58 I mean, these are these are all public. Anyone can use the tool.
**Trask Stalnaker** 12:02 Yeah.
**Reiley Yang** 12:02 We use all of them. So I'm I'm not concerned.
**Trask Stalnaker** 12:05 Yeah, yeah, I think so.
Let's see if I ran it over while that's loading. So the other tool that I looked at was just the built in, depend about so advanced security dependabot alerts.
It seems like they've been investing a little bit into this, and it's very similar and you can add some rules. Now.
And I had hooked it is not cooperating.
what did I do? Which repo? Did I do? Okay, so this one I ran, Trivi.
where did I run? Dependable?
Yes, this is the one I ran, depend about on.
So depend about like for Java like it doesn't understand the gradle dependencies transitive dependencies.
But there is a great all action that will submit the dependency graph to depend about what actually submits it into dependency. Graph?
So like this used to be fairly empty. But now that I'm actually pushing all the transitive dependencies, it gets a lot about.
**Reiley Yang** 14:03 Nice.
**Trask Stalnaker** 14:04 Yeah.
So I think for some ecosystems.
You can get better support in that way.
**Reiley Yang** 14:16 Is that like a 3rd party like Plugin or the it's just a official inventory of logins.
**Trask Stalnaker** 14:26 Yeah. So a little bit of both. Let's see, depend upon alert submission.
So there was a page. I'm not finding that right now. On the dependabot site.
It's submission gradle.
Oh, no, that's just the great old site. Yeah, I'll I'll dig that up.
But they described on the Github site a couple of sort of official plugins that will submit that for different ecosystems.
But I'm not sure how well that will cover all our languages definitely, something to still look at.
But yeah, so it did give pretty decent results on here.
From the transitive, dependent dependency. Once I plugged in transitive dependencies. So you know, you get your high, moderate low, so it looks like a good option. Let's see on the.
**Reiley Yang** 16:14 Super cool trust. I have a small question. I remember I learned this from opentelemetry.net. So if we have a library, we normally. Don't put a strict version on the dependency. Give library like our library, open telemetry. SDK, depend on some like full bar library. Then we don't try to say, we need this exact version of our library. Instead of we give a range we're saying, like we support at minimum this version. But like a higher version would be okay as long as it still share the same major version. So in that case I noticed some tools, they might have this false alert because they always assume you take the lowest dependency.
and I feel this sick. We probably need to give some guidance like when people take dependency. How do we think about range?
And I can see.
**Trask Stalnaker** 17:11 Yeah, I can tell you how I think about range which is that the if the if we bring it transitively, if the user doesn't specify anything and only pulls in our dependency. Yeah.
once they override our dependency version and pick a different patch or minor version within that supported range. Then it's not our responsibility.
**Reiley Yang** 17:45 Yeah. So I also have have some similar topics. So maybe like worse. Pr, one example is, if in like github workflow. We're saying we need the latest version of ubuntu. Currently, we just specify the the image used for Ci, CD, like build, image or like test image. And and that seems fine like we. We don't want to be like specifying that that digest of that ubuntu image, because the idea is it's just Cicd. If there's a patch we would automatically benefit from from Github like latest ubuntu. But if we shape something like a helm chart.
or we shape an image, and that image has a base image. Then, instead of specifying a tag like, we say the latest, we want to use a very accurate that digest, because in this way people can always reproduce the build like it doesn't matter what time they are. They can always take the same thing and build from their machine and get the same result. And another thing is by specifying the digest, it's very easy for the scanning tools to tell whether we're safe or not. It's very predictable. If it's latest, then depending on what latest meaning for the tool, it could be different. So maybe today, you're running.
**Trask Stalnaker** 19:07 When the release? Yeah, it was when the release was made. What was latest? Yeah.
**Reiley Yang** 19:12 Then then you can see like, for for a lot of scenarios like we have the Ci CD job.
or we have a base image in our container, like docker file or in the helm chart. We want to use digest.
and we probably want to enforce that. But when we have a base image for Ci, CD job. Like the test or integration like this image, we should use the latest like flow floating version when we use a library. There are also some consideration, and I feel like most maintainers don't seem to have very clear guidance from this group.
and some of them might think like we always use latest because latest is very easy.
or they always use the jest.
And I like, sometimes I I even realize like I'm I've been debating with myself which one do to use.
and for this scanning tool I hope it can work with the whatever recommendation we give.
**Trask Stalnaker** 20:15 Yeah, I think it's really important that the scanning tool be able to either differentiate between test and production resources code or have a way for us to tell it which ones like. I had to do that in the that java repo with the right, even with just licenses.
We have. It was kind of decent at telling like it wouldn't pull in test dependencies.
but it didn't understand that some of our modules are test only modules.
and so it should completely ignore those modules.
So yeah, I I agree. It needs to be the tool needs to be configurable somehow, that you can exclude test, dependent.
**Reiley Yang** 21:23 Wait. I'm I'm I'm I'm curious, like, why would you think test should take a special rule in terms of security? I understand test can take a different bar on license because you you don't ship tasks a bit. For like security. I ask this because earlier this year, I remember, there's a a like a severity like 10.2 or something like a issue. And it's actually a hacker trying to add something to the test case, while the test case seems like a valid script. But it's actually trying to modify the output binary by injecting random, not random, by injecting CPU instructions.
**Trask Stalnaker** 22:14 Yeah, I guess it's a good question.
I can speak from the I mean Java instrumentation perspective. At least we test against a lot of different versions of a library.
And so we, you know, we do test against older versions of libraries from a compatibility perspective.
So we would need some way to exclude those cves being flagged on those.
**Reiley Yang** 22:51 I see. Then, I would imagine, like the the build process would run without the test cases. And it's a reproducible build, so you can verify that then the test will run on top of the the build results. So even if the test got some like security vulnerability, people try to modify the output. They don't even have the permission or the access to, because build is managed by different Ci. CD. Pipeline.
**Trask Stalnaker** 23:18 Yeah, that's actually good. Good! Call out. I suspect that our release build is save but let's see assigned.
Yeah.
**Reiley Yang** 23:39 So.
**Trask Stalnaker** 23:40 Yeah. So we don't run tests. I mean, we run tests in a prior.
**Reiley Yang** 23:46 Okay. Great.
**Trask Stalnaker** 23:47 Step, but that's.
**Reiley Yang** 23:49 None of them.
**Trask Stalnaker** 23:50 Very interesting. Yeah, yeah, I remember this one, yeah.
**Reiley Yang** 23:57 Okay, this is awesome.
**Trask Stalnaker** 24:00 Cool. Yeah, I'll I'll Yeah. Did I find the trivia one? Let's see if we got let me look at oops. Not that.
See if I can show.
**Reiley Yang** 24:13 The the power of TV is, it is able to run deep dependency analysis, like, if you have a base image, then you build a container. It will scan the container. And you understand, in the container you have a a binary executable which is coming from some like goal components, and they can like it can look into the goal components and see if they have transient dependency.
like multiple layers of dependency, which I found very powerful. Also, like. If you have dependency on the ubuntu base image, it can even go and tell, hey, you have a dependency on C lib. And that C lib has a known security issue.
**Trask Stalnaker** 24:56 Yeah, I'll have to do some more research on Trivia, because I think my 1st attempt. I was surprised it didn't find anything other than these, you know, docker images like it didn't seem to understand the Java dependency.
transitive dependencies, but same as get her the depend abot.
Maybe if I push the do the dependency submission for it to populate it, maybe they will use the Github's dependency graph like I thought that was kind of cool that Github.
as that, like the dependency graph is kind of like a separate concept. And you can populate that yourself. You can tell it, hey? I know better about my transitive dependencies.
**Reiley Yang** 25:54 Yeah. And I, I guess, is you're able to figure out the trends and dependency for the greedle system. But if you have a depend like like. If you have a container image which has dependency on the base image, then you can imagine, like someone has to look into the base image and find the executables. And look at if that's a like a C implementation, then what's the lib. C being used? If it's a goal, then what's the goal Runtime being used that that's like way beyond what what you would normally imagine, for as a Java Maintainer, you have to understand a lot of other ecosystems, and I, I remember, like Trivia, was able to do some of this which I find helpful. Another thing is, if you look at Docker.
Docker has an integrated system which allows you to scan the container image security.
**Trask Stalnaker** 26:49 Of the ones that we publish to Doctor Hub.
**Reiley Yang** 26:53 Yeah, there's even a command line that Docker can allow you to use.
I'll I'll find the link.
**Trask Stalnaker** 26:59 Oh, okay, yeah, yeah.
cool. But I yeah, I like the overall, though. I think kind of what you're doing here of the generic instructions, getting and socializing that and getting buy in from folks. And then that gives us sort of we can do that in parallel with. Then looking at trying to come up with more specific tooling recommendations or people.
And I can keep playing around with this. I'm out this week, but I can play around with it some more next week.
To create a couple like play out the scenario with the at least the Java repos of what trivia I can show, what trivia captures versus, what dependable captures.
**Reiley Yang** 28:11 Yeah. So I I share the name. It's called Docker Scott. I'll also put the link in the meeting notes.
**Trask Stalnaker** 28:29 Cool. Yeah, I've seen that in the docker. Hub, ui, the yeah. But if there's a way to run that locally, that would be great.
**Reiley Yang** 28:50 Okay. Cool.
**Trask Stalnaker** 28:54 All right.
**Reiley Yang** 28:55 Because that's all.
**Trask Stalnaker** 28:58 Sounds good, thank you. See, ya.
**Jeremy Corley** 29:02 Thanks folks.
