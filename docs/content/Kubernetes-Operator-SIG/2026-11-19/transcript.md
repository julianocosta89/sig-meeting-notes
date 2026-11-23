SIG: Kubernetes Operator SIG
Date: 2026-11-19
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Pavol Loffay (Red Hat LLC)** 01:48 Hello, I'm Mikola.
**Mikołaj Świątek** 01:56 What's up?
**Pavol Loffay (Red Hat LLC)** 01:58 Doing good, how are you? How's CubeCon?
**Mikołaj Świątek** 02:01 I would say surprisingly, like, a little bit dead?
It didn't feel like there were that many people at it, I would say.
**Pavol Loffay (Red Hat LLC)** 02:11 I heard the same comment from a colleague, that it felt smaller than before.
**Mikołaj Świątek** 02:15 I don't know if it really is, or… that venue has a weird shape, so… so it's possible that, like, just Solution Showcase was like this?
Because you kind of really needed to go different places, whether you wanted to attend talks or walk around the showcase. But at the very least, like, I was at… I was doing booth duty in Amsterdam this year, and it was… Busy.
And here, I was kind of like, you know, walking around, getting coffee, relaxing a little bit.
**Pavol Loffay (Red Hat LLC)** 02:46 Okay.
**Mikołaj Świątek** 02:47 come in, people would come in and ask, hey, I'm using Elastic on-prem, when is your, like, you know, currently alpha AI SRE products coming to, to Kibana on-prem? And I was like, I don't know what it is.
But it was kind of, it was kind of chill in this respect. A lot of the maintainer summit was for, like.
how do we do… how do we deal with CVEs? How do we deal with AI pull requests that, like, you know, are lots of text, but… but often… often the quality isn't great, and… and so on.
**Pavol Loffay (Red Hat LLC)** 03:31 Was it, was it, like, discussed, or, like, is there any funding from CNCF to have this, like.
AI tools to review pull requests, like…
**Mikołaj Świątek** 03:41 It actually is, not even from the CNCF, you will… you might notice that we're using a GitHub action called Shared Workflow from OTAL.
And that allows you to, like, or… by itself, that doesn't give you code review, but you can use the same kind of setup that it uses to, like, build a co-pilot to OpenTelemetry.
So you can actually, can actually do this kind of stuff. Supposedly, you can also… because, I don't know if you're aware, but we are now officially all CNCF maintainers.
as of OTEL graduating, we all count as CNCF maintainers, so we have, like, the… you know, all the programs are available to us. You can, if you go… if you want to, you can go ask a Trask Stonemaker to go to the CNCF Service Desk and ask for a Copilot Enterprise license for you.
**Pavol Loffay (Red Hat LLC)** 04:47 Okay. But I was more looking for something that kind of automatically runs on all PRs as a first-part review.
Not something that I have to do, kind of, explicitly on the PR.
**Mikołaj Świątek** 05:00 I think you can… I don't think it exists, but I think you can… you can, like, at the very least, set it up.
Goodbye, and have it, like… because for me, the main question is kind of, like, where do I build this to, right?
Yeah, I can set up a PR, a workflow that, like, Copilot's gonna review pull requests, right? It's just a question of who's gonna pay for it.
**Pavol Loffay (Red Hat LLC)** 05:22 Well, that's the question, like, is the CNCF funding such a… such an approach?
**Mikołaj Świątek** 05:27 CNCF by itself, I don't think is funding it at, like, an infrastructural level, but OTEL is actually funding it. And I think that, like, eventually goes back to the CNCF, in terms of, like, who actually pays for it. Or, you know, nobody actually pays for it, it's just that, you know, Microsoft says, yeah, you're a CNCF, so you can have the tokens.
But, yeah, you can, like, actually set things up so that it's, like, built to… build to hotel, essentially. If you look, I go to, like, Where?
**Pavol Loffay (Red Hat LLC)** 06:02 Is it something… is it something we would like to have in the Operator Repo?
**Mikołaj Świątek** 06:06 I think so. I don't know if I… I don't… I'm not, like, a big… Believer in, kind of, general-purpose code review.
I think that if you want to have AI code review as a first pass, I think… You have to scope it down.
Like, you have to, like, write a skill that it can use, so it actually, like, reviews, like, in a targeted way.
That you're, like…
**Pavol Loffay (Red Hat LLC)** 06:36 We use CodeRabbit internally, and in some cases, I think it's pretty useful, actually.
**Mikołaj Świątek** 06:40 It is, but I like… sorry.
**Pavol Loffay (Red Hat LLC)** 06:43 And we don't have any kind of customizations to it. It's… there is no additional skill or anything like that. I'm not sure if it's sourcing the skills from Dorito.
But, 30% don't have any skills, and it works quite well.
**Mikołaj Świątek** 06:58 I… I would say that there's certain repetitive things that I say in pull requests that I think an AI could easily say instead of me.
But for that, you actually have to have a scale. Like, for example… like, if you're adding a field, or making a field on, like, a CR work that, like, gets passed down to some downstream.
resource, then there should be… then that field should be in, like, the end-to-end test that checks this, for example. Like, I tell people all the time to do that in the pull request, and that's, like, something an AI reviewer could easily say, because it's just, like, a very mechanical check, even, at the end of the day.
Something I would like… I can tell you what I think is more useful than pull requests right now, necessarily. It's, like, doing initial triage on issues.
**Pavol Loffay (Red Hat LLC)** 07:56 Yeah, that as well. I… I can look into that if… if we would agree to have the… AI reviews and AI triaging of the issues.
**Mikołaj Świątek** 08:08 I agree. It's just like… I think we should be clear.
that this isn't… the… like, this isn't… I don't want… I don't want contributors to feel like they've made an effort, you know, maybe the effort they made is just, like, pointing their AI agent, right, at an issue, but they've made an effort to contribute, and then the only engagement they get back is, like, an AI review, or a bot posting under their issue, right? So I want to make… I think we should, like, make clear that this isn't the only engagement they're getting.
from us, it's just, like, an initial Initial engagement and, and… you know, fixing some… some stuff that's, like, obvious for us. For example, for me, if somebody opens an issue, a bot can easily go there and try to reproduce the issue.
Automatics, for example.
Or look at the code and verify whether, like, this looks like something that's actually, you know…
**Pavol Loffay (Red Hat LLC)** 09:06 Makes sense.
**Mikołaj Świątek** 09:07 Yes, yes, right. But it isn't like that. It should say, you know, this is an initial triage, you know, a maintainer will still look at the issue and reply to you, right? Or a pro or staff member.
I don't want to get into this, like… weird feedback loop where it's just, like, bots talking to bots.
On everything.
**Pavol Loffay (Red Hat LLC)** 09:34 Okay, and what… maybe a different topic, what do we feel… about, kind of, merging automatically the, the dependency pumps, if they pass CI.
**Benedikt Bongartz** 09:52 I think I'm…
**Mikołaj Świątek** 09:54 I think I… I think that's mechanically not that easy.
is my, like, understanding of it. Like, it's not that easy to set that up.
Because I think there are, like, requirements from the org that we are not so… can't so easily, like, walk around, let's say. I would start… I would start by grouping them more aggressively.
Personally.
Like, if we're okay auto-merging them, then, you know, maybe we don't need.
a pull request per dependency, like we have right now, maybe we can group more aggressively and just, like, merge them together. So, like, one, we're going to have, like.
4 pull requests per week instead of 10, or more.
That's like…
**Pavol Loffay (Red Hat LLC)** 10:36 I think that there is higher chance of failure on the CI, in that case.
**Mikołaj Świątek** 10:42 Maybe, but it's like… You're gonna have to deal with the failure anyway.
Like, if one of them is failing it, then you would have to deal with the one failing PR.
Anyway… And I'm saying it, like, increases. What it does… It just changes, like.
**Benedikt Bongartz** 11:00 cosmics.
**Mikołaj Świątek** 11:01 Sorry, go ahead.
**Benedikt Bongartz** 11:04 I think you often can bypass failure even with grouping it. So, for example, with all these Kubernetes dependencies, sometimes you cannot bump them individually, so it's even better to… Cook them up.
But as far as I'm aware, we just need… to change a few things, not on the org level, just on the repo level, for having Renovate, for example, auto-merging.
Stuff.
**Mikołaj Świątek** 11:27 I think there is a requirement that, like, that it needs approval.
From… from, like, one of the, from the approvers group.
**Benedikt Bongartz** 11:38 Hmm.
**Mikołaj Świątek** 11:40 I'm not sure if we can disable that on our own.
I would like to…
**Pavol Loffay (Red Hat LLC)** 11:45 personally look into that as well. Like, if there is a chance we can get them auto-merged, I would be… All for doing that.
It's a lot of noise, and if they pass the CI, I don't think I have ever the case that, like, the CI was green, and I decided, okay, I don't want it.
Maybe only for, like, a Go version, if we bump, in the Go mods?
like, the minimum goal version, because… Of some internal stuff that we have, but otherwise… I haven't had that case, and if we have that case, we could maybe change the renovate config to kind of… Wait for approval in such a case, anyways.
**Mikołaj Świątek** 12:28 I think there are some dependencies which are potentially high impact and should be… we should be able to be careful of them, like the Prometheus stuff, for example.
Like, the fact that you're bumping a Primepheus Operator version has… potential for changes. And some of them are sometimes, like, not… immediately visible. And the required Go version, we don't have automation for at all. We have automation for the Go version we use in CI, we're actually building, but not for the one in Go mod.
Which makes sense, because it's, like, it doesn't change very often, like, once per year.
Incidentally, there is a pull request from me, which replaces the changelog check that we have right now, which is our own, with the changelog check from shared workflows.
But that's, like, one thing.
That's small, and and helpful.
Yeah, I'm generally… I'm generally in favor of improving our automation.
I would say.
Including with the use of… AI tools.
And I'm fine auto-merging a lot of the Go mods, dependency updates.
Personally.
Maybe we can start by saying that we only auto-merge patch versions, or that we auto-merge the test dependencies, for example.
These are all things that we have right now.
Looks like… If those pass, then cool, right?
it's minimal. I'm not so… I'm not so keen on, like, automatically merging, for example.
Production… the production base images, example, because we have, we have, dependency updates for the base images for the auto-instrumentation.
And that's a little bit, you know, a little bit sensitive.
Sometimes you have to kind of make a decision.
do it. Especially, especially since, like, in the age of, of, like, rapid, rapidly.
of the rapid wave of CDEs approaching, it's like, sometimes you have to, like, you make the decision, yes, you know, I'm approving it, so it's merged, and as a result of that, you are, like, resolving a bunch of… a bunch of CDEs.
that those base images fix, right? So it's… I think it might be better if that's, like, intentional.
Fucked.
**Pavol Loffay (Red Hat LLC)** 16:12 Maybe, shall we move to the issues discussed at the SIG?
**Mikołaj Świątek** 16:16 Yeah, can anyone actually share their screen?
temporarily unable.
**Benedikt Bongartz** 16:29 Fortunately, currently not able to do it.
**Mikołaj Świątek** 16:32 By the way, Belle, what shirt are you wearing?
**Benedikt Bongartz** 16:37 the Sumo Logic shirts.
**Mikołaj Świątek** 16:39 similar.
**Benedikt Bongartz** 16:40 Sure.
**Mikołaj Świątek** 16:41 That you got.
**Benedikt Bongartz** 16:41 One weird guy.
**Mikołaj Świątek** 16:43 Was this when we first met? In Amsterdam, like, for 3 years ago, or something?
**Benedikt Bongartz** 16:51 Yeah, yeah.
**Mikołaj Świątek** 16:53 I thought it… I thought it looked, I thought it looked familiar.
Alright, let me, let me, let me…
**Benedikt Bongartz** 17:00 It's the version which is way too large. Still too large, even if it was washed 10,000 times.
**Mikołaj Świątek** 17:10 Okay, let me try again, okay? Let me try again.
**Pavol Loffay (Red Hat LLC)** 17:22 I'm not sure I can share.
**Mikołaj Świątek** 17:26 I have this problem where I have multiple screens and multiple virtual desktops, and Zoom is incredibly confused right now about, like, which I actually want to share. Give me a moment.
Now, you see this?
**Pavol Loffay (Red Hat LLC)** 17:41 Nope.
**Mikołaj Świątek** 17:43 Okay, cool yo.
So… Future gates… I don't think anything really changed in here.
This is stable, and we might remove it, but there's also a… an issue asking to be able to turn it off, I think.
Because… Because there's, like, There's some extension in the collector that does… that does the same thing, but is smarter, and if you set GoMemLimit, it stops doing anything.
Oh.
But I don't think this actually affects anything. I think we should just get rid of this one.
This is alpha, and it'll be removed.
Once I get to submitting my pull requests that allow you to configure this normally.
This we just merged very recently, and I don't think it should go into beta until we fully decide which other metrics in a target allocator should also have the additional attributes that this adds, because this adds attributes to metrics.
Network policy, I don't think, is ready yet.
We have to, like, resolve all the problems.
around it.
Same thing here, this is also network policy, but for something different.
Cluster observability, I don't know what the status is.
And this, I think we should also just delete.
Does that sound about right?
These two stable… Teacher gates should just be removed.
I don't hear objections.
**Benedikt Bongartz** 19:38 Nope, sounds good.
**Mikołaj Świątek** 19:41 And… issues.
Right, so there's… I think we used to have a feature request about this already, where the user wants to be able to set the instrumentation image tag using an annotation.
Do we have objections towards this?
**Pavol Loffay (Red Hat LLC)** 20:06 I…
**Benedikt Bongartz** 20:07 instant override.
**Pavol Loffay (Red Hat LLC)** 20:10 I think it overrides what is specified in the… In the instrumentation CR.
I don't know, like, there's… Users can already do it by creating multiple instrumentation CRs in the cluster.
I know that this is more fine-grained, but…
**Mikołaj Świątek** 20:27 They don't like this.
**Pavol Loffay (Red Hat LLC)** 20:31 And if you move to the injector project, then all this will become obsolete?
**Mikołaj Świątek** 20:40 Will it?
Bye.
**Pavol Loffay (Red Hat LLC)** 20:44 Because it's gonna be a single image, you know?
**Mikołaj Świątek** 20:48 I mean…
**Pavol Loffay (Red Hat LLC)** 20:49 Or there will be new annotation for the injector image.
**Mikołaj Świątek** 20:53 No, I think it's gonna be the same thing, like, moving to an injector, to the injector projects is, like, two different things. One is to use the injector in our existing images, which I don't think are gonna change, and the other is to use, like, the… one big image with everything in it. But that's gonna be a separate feature, I think. You're going to have to configure it differently.
It's not gonna be, like… If you use, like, whatever they're using, Python instrumentation right here, it will keep working the same way it does.
the only thing the injector does is it, like, stops you from having to, you know, explicitly, explicitly set whether you're using Muzzle, or glipsy, or another, or, like, which PHP version.
It is, specifically.
Like, that… that it, like, fixes for you, but it doesn't… Obviate this problem of… I have a Python application, which might already include an OpenTelemetry SDK in its dependencies, and then I have to pick a compatible Hotel, auto instrumentation.
It's… maybe… maybe this is something the injector should do, but the injector is only able to do, like.
Decide not to inject, basically.
Right?
But here, what they're… what they're doing is, like… They want to have, like, the same exporter configuration?
maybe the same, like, sampling settings and so on, but they want to have different versions of the actual instrumentation, because their applications might already depend on something. And if you try to load, like, two different versions of the Python Auto SDK in this way, you get conflicts. You can get conflicts.
Does that make sense?
**Pavol Loffay (Red Hat LLC)** 22:48 No, it does. I think, like, the end goal with Injector was to have, actually, this single image.
Or a single volume with everything in it.
**Mikołaj Świątek** 22:59 I mean, that's… I agree that we can have it, I just don't think that we should get rid of what we have right now.
At the same time.
Like, this is, A way for… if nothing else, it's nice to have smaller images.
Right? If we combine all the images into one big image, it's gonna be one big image with everything, it's gonna be, you know.
six times there are… it's going to be significantly bit larger, and it's also going to have all the CVEs, instead of just the CVEs from the language that you're using. So, there's, like, there's reasons. Or… or you might want to… you only use the Python instrumentation, and you want to build your own custom image for Python instrumentation, that's also a reason to use the current setup.
Anyway, like, I don't think Injector actually solves this, either way. Even if we could.
Like, let's say, let's say… Even if we're going to have one image, the image is still going to be versioned, and in this case, they would still.
**Pavol Loffay (Red Hat LLC)** 24:04 Yeah, Jesus.
**Mikołaj Świątek** 24:05 different.
**Pavol Loffay (Red Hat LLC)** 24:05 I'm not saying it's gonna be… I'm not saying that it's gonna solve this, I said that if we go to that approach, and if we drop individual annotations, then it's gonna be obsolete.
**Mikołaj Świątek** 24:21 Yes. But, like, if we had a single image, this user would be asking for the ability to set the tag for that single image here, using an annotation.
So it, like, doesn't, I don't think, fundamentally change what's going on.
The question for us is whether we want to allow it.
**Pavol Loffay (Red Hat LLC)** 24:55 Yeah, I think at the same time, it… it's not probably… difficult to implement. It's just… Source the annotation from the… from the… both spec and… Overriding the tag.
**Mikołaj Świątek** 25:16 Yeah, I think it's easy to implement. I think I'm okay with doing it for the tag. I'm not okay with doing it for the full image. I think the instrumentation CR should be in charge of picking the registry in the image.
And, like, end users who are adding the annotation to their pods should not get to pick whichever image they want.
to be added this way. Because this kind of… Goes around some controls that you might have, like, if you have, like, let's say, admission policies for the instrumentation that says that they're only allowed to use your own, you know, your own registry with this specific image in there.
And then the, the owner of the pod can pick which tag they want for this.
But they can't pick.
But they don't get to ask for, like, a completely different image.
Let's say. I also think that it's possible. Sorry.
**Benedikt Bongartz** 26:17 Which makes sense, because otherwise you could just overwrite the image of the init container, which runs there, and… We could even think about… not sure if that's a bit of an overkill, but technically you could allow, like, tag override on the CR. So you would just have a CR where you just tick the boolean and say, allow tag override, and then this will take into account, and if… you don't enable it on the CR, this has no effect. So this means it's a bit more explicit, and… Yeah.
**Mikołaj Świątek** 26:55 I agree. I agree that there should be some way to control it.
control what… for the CR offer to be able to control whether this is allowed.
**Benedikt Bongartz** 27:05 Yeah, then just a small boolean, like.
**Mikołaj Świątek** 27:07 Good luck.
**Benedikt Bongartz** 27:08 allow tech override or something. And if this is enabled.
we allow you to set this annotation. If it's not enabled, No chance.
**Mikołaj Świątek** 27:19 Okay.
Alright. Pavol, do you object?
for this.
**Pavol Loffay (Red Hat LLC)** 27:32 I don'ts.
**Benedikt Bongartz** 27:41 should make sure that we inform people. So if you have it specified, for example, And you deploy it.
And it's not allowed that you will get some kind of information, like, it's not working because of And the other way around, too.
So if you… yeah.
That's a detail from afterwards.
**Mikołaj Świątek** 28:32 Alright, cool.
And… I put… this… oh, actually, maybe we should talk about this.
So, we used to have an issue in… 2024?
where… I don't know, what am I looking at that?
So… Yeah, we had an issue in 2024 which asked for, like, a basic base collector configuration that you, like, merge into all the other collector configurations from all the CRs.
And I guess it was accepted back then, and now here's a contributor who implemented it, and now it's like… Do we actually want to?
Do we actually want to let users do this? I kind of don't like this feature, because it, like, makes the… quietly makes the collector config that your collector is running different than what you put into the CR.
This is what I don't really like about it.
**Benedikt Bongartz** 29:39 Isn't this something that should be covered by the cluster observability CR?
So it provides some kind of… it's some kind of default.
And… If you want to do some additional tweaks, there is the proposal.
I didn't look into this for a while now, but with the patchCR, so that you can just patch things on top if you want to.
Which means… You don't define the defaults, but there is a default, so you get it up and running, and you can tweak it, and…
**Mikołaj Świątek** 30:13 I think… I think the reason this was… actually, Israel opened this issue.
Alright, so… I think the reason this existed originally is so that you could specifically force all of the collectors That are, like, created by the given operator to… To, like, have a certain basis to do certain things.
in a particular way. In this case, I think it was, like, memory limiter.
Configuration, or batch, sir.
**Benedikt Bongartz** 30:53 But isn't this something people implement with Customize or something anyway?
**Mikołaj Świątek** 31:00 Maybe. I don't know.
**Benedikt Bongartz** 31:01 a base for something, and if you have 5 different collectors, whatever, you just… Patch it.
**Mikołaj Świątek** 31:11 Maybe, assuming the merging works correctly and customized, which I'm not sure it does.
**Benedikt Bongartz** 31:16 But that's the same thing with the operator, assuming the merging works if I have some defaults, and I just… override something, it needs to be merged. So it's basically shifting the problem from customized to the operator.
**Mikołaj Świątek** 31:29 Yeah, but the operator can actually, like, load this into a… Although, I don't think we actually do this, but… In principle, the operator can actually, like… pipe check this to some extent, right? Which Customize will not do.
It has no idea what this is. But we can actually, like, verify whether the end configuration is correct.
And we can actually, like, if you submit a collector and this is set.
then we can, in the webhook, merge it with the… with this, with the base, with the default config, and check whether it's valid, at least to the extent that it's possible to check as valid, right?
But I don't know if we actually want to do this, like, I don't know what it's like.
**Benedikt Bongartz** 32:26 I didn't say no.
It's too much complexity for too little… output.
**Mikołaj Świątek** 32:36 Well, I feel like, even though this is, like, plus 100 lines, there's, like, a lot of… Consequences that aren't immediately apparent to doing this.
Oh, what do you think?
**Pavol Loffay (Red Hat LLC)** 32:52 I share this little opinion.
**Mikołaj Świątek** 33:01 Oh, actually, actually, Mujib, sorry, I didn't realize you were actually here. I was talking about you as if you weren't. I'm sorry, sorry about that.
**Mujib Ahasan** 33:13 That's fine.
**Mikołaj Świątek** 33:15 Welcome, by the way, to the upper… to the, Operator SIG meeting. As you see, like, this is, You picked it up, and I'm sorry this is our bad, because this issue had, like, yeah, you know, we discussed during the SIG and said yes, which I don't remember saying yes to this, personally. But, you know, we made you do the work, and now we're kind of waffling about as to whether… Whether we want to do it. I don't… I think we don't want to do it just yet. I think somebody has to come up and give us, like, a very specific, well-defined case for whether they need it.
and for what exact reason they need it, and that there's no better way to achieve what they want. So for now, I would like… park it. Like, just close this pull request, and I'll post here under the issue, saying that's, like, you know… For now, we don't want that if anybody wants to come up and, like, try to argue with us that this is a… this is, you know, the only possible solution to the problem they have, then.
we'll reconsider. But for now.
Sorry. For now, it doesn't look like anybody's demanding it. Maybe Israel, who is an approver, is gonna come back and ask for it, and then we'll have a conversation at the SIG meeting. But for now, I don't think we want to merge this.
Right.
**Mujib Ahasan** 34:41 Yeah, sounds good.
**Mikołaj Świątek** 34:42 Sorry, sorry for that.
**Mujib Ahasan** 34:44 Sunday.
**Mikołaj Świątek** 34:46 Okay, and finally… There's this, which I don't… We even have a pull request that implements this stuff, and… Well, basically what they want is to have more… more… more of an ability to Filter what is… like, what we're watching. Like, which resources the operator actually handles. We have watching by namespace, and they want to, like, make it real, proper selectors.
Like, do we wanna?
**Pavol Loffay (Red Hat LLC)** 35:27 I'm not sure I understand, like, they want to have multiple CRD versions in the cluster, and… As well, have an operator that kind of uses that specific instance of the collector CRD is that they ask?
**Mikołaj Świątek** 35:45 they want different operators, so right now, you can already say, like, you have two oper… multiple operators, and each gets its own set of namespaces that it handles, right?
Yeah. So they just want to make that so that you can, instead of just saying namespaces, you can actually just… you can actually use labels.
So you can say, operators labeled like this are handled by this, and operators labeled like that are… sorry, CRs labeled like this are handled by this operator, and CRs labeled like that are handled by the other operator.
I'm pretty sure Prometheus Operator does this.
I'm pretty sure in Prometheus Operator, you can tell… you can say that this Prometheus Operator handles these resources, and this other Prometheus Operator handles these other resources in this way.
So… that's a reason to accept it, I guess, because… We trust the previous Operator maintainers more than we trust ourselves.
Look.
**Pavol Loffay (Red Hat LLC)** 36:43 Okay, so the label… they want to have a label selector on the CR instance.
**Mikołaj Świątek** 36:46 Yes, yes.
**Pavol Loffay (Red Hat LLC)** 36:54 I think it's reasonable.
I don't know what are the consequences, though.
**Mikołaj Świątek** 37:05 Like, I don't think the consequences are really much different than the namespace stuff that exists.
Like, it works the same way.
It's just that the selector itself is different.
And, like, I guess one of the consequences is that moving… you can't really move stuff between namespaces, but you can't remove and add labels to things very dynamically.
It's maybe, like, worth considering what happens if you do that.
If you have something that is being reconciled by an operator, then you remove a label, and that operator stops reconciling it. Does that have any… does that have any… unexpected consequences? Like, should there be some kind of… I don't know, events emitted about this, or should there be something written to that CR status saying, hey.
You know, I'm not being reconciled anymore.
Or some such.
But I don't know, overall, I think this sounds fine to me.
Okay, I don't see… sure, you can probably shoot yourself in the foot with it, but we're not forcing anyone to use it.
Do you really want to?
They can knock themselves out.
And I don't think it really costs us much in terms of implementation, like, an implementation of it.
It's, like, plus 100 lines of code.
And the only thing it does is, like, let's see… Yeah, it just, like, modifies what the cache is, see?
**Pavol Loffay (Red Hat LLC)** 39:03 Yep.
**Mikołaj Świątek** 39:05 Which is… Cool.
That's fine.
**Pavol Loffay (Red Hat LLC)** 39:12 I will review, I don't have anything against it.
**Mikołaj Świątek** 39:18 Alright, I'll, I'll remove Discussed sake, and… And we can, like, proceed with it. Like, at the very least, there isn't, like, any opposition to it, so… So that's okay.
Alright, is there anything else we need to talk about?
**Pavol Loffay (Red Hat LLC)** 39:58 I don't have anything else. Thank you for the… for the meeting.
**Mikołaj Świątek** 40:02 One point I have is that we have, in case you haven't noticed, we've merged a change to sign the packet allocator and OpenBridge images, and the next release is going to be the first one, which… Actually… Actually does this.
Mmm… Oh, actually, I, I did, I did, like… Let me actually reshare my screen quickly, okay?
Yeah, it's the freaking… Zoom opens… Zoom opens this, showing thing on the wrong… desktop, no matter what I do, fortunately.
Alright, here we go.
Right. This is assigned to you.
Guys.
You have to figure out where… when it's okay for us.
For us to bump this.
**Pavol Loffay (Red Hat LLC)** 41:01 I checked, I think.
Today or yesterday, and there was no official built at Red Hat for that version.
But I hope it's gonna come soon.
**Mikołaj Świątek** 41:14 Yeah.
Another thing related to… to OpenShift and also EKS is that I think very soon, the very old OpenShoot version, I think it's, like, 4.20, is going to go out of extended, extended support.
So I think in February, we'll be able to, like, bump our… required Kubernetes, like, the lowest Kubernetes version we support by quite a lot.
I'm, like, 250 from, like, 121… From, like, 1.25 to, like, 1.31 or something. I think we'll be able to go.
Because EKS also doesn't support that.
And finally… One more thing.
Pavol.
This is waiting for you.
**Pavol Loffay (Red Hat LLC)** 42:11 Yeah, there is a draft pull request, and… how I would like to do it is to first set the B1 alpha 1 as not served.
on the CRD, and then… Let it sit there for maybe one or two releases.
So if it causes any issues, people could just patch the CRD, And then get rid of the… the V1, Alpha 1 altogether.
**Mikołaj Świątek** 42:41 Don't you want to do feature gates instead? Feature gates are much easier to flip versus just, like, versus patching the CRD.
And that was the original, sequence.
**Pavol Loffay (Red Hat LLC)** 42:56 I… I think in this case, it's better to… to go with direct CRD patching, because the CRD is not created by the operator, and we would need to have this code live in the reconciler, which I don't like.
And in a helm chart, I think… it's anyways, I think CRDs are installed in a separate step, right? So the Helm chart can have an option to set a field in the CRD, probably?
**Mikołaj Świątek** 43:29 Depends on which hunt chart.
Because you can do it two ways. The operator helm chart does this. CRDs are installed as a template.
the OpenTelemetry CubeStack one doesn't. Into the OpenTelemetry KubeStack, the CRDs are installed as, like, as Helm sees CRDs, so you can't actually modify them in any way.
**Pavol Loffay (Red Hat LLC)** 43:52 I see.
**Mikołaj Świątek** 43:54 You can… or you… rather, you can't… you can't, They… you can't control their content using the Helm values file.
Like, they have to be static.
**Pavol Loffay (Red Hat LLC)** 44:12 I see. Anyways, I… If you prefer the… Future gates.
Maybe I can take a look. I think it's way easier to just have it flipped to… Not served, and then if some people have issues with it, in the release notes, we would have the… there is a command how to make it served again.
It doesn't require any kind of restart on the operator, right?
From that standpoint, it's better.
**Mikołaj Świątek** 44:49 I am okay with this, personally.
But, like, you should post under this issue and say, like, we're just going straight to served false, and, you know… create an issue, or create… either use this issue, or create a new one and pin it, right? And say, you know, if we're removing this.
If you want to get it back, this is how you need to patch your CRD to get it back.
And then, you know, however many versions later, we're going to get… just completely remove it.
**Pavol Loffay (Red Hat LLC)** 45:23 Okay, I'll do. It's just a draft PR, I think there is some… some failures, but I will… I will work on it.
**Mikołaj Świątek** 45:32 Alright, that's all I had. Sorry to call you out, but I really want this gun. Gun, like, it bothers me.
**Pavol Loffay (Red Hat LLC)** 45:43 Yeah, it's gonna be nice. Simplification.
**Mikołaj Świątek** 45:47 Alright.
Oh, cool, that's all I had. Does anyone else have anything?
Sounds like no. Thank you, everyone. Andy? Yeah? Or did you… Okay. Just, just, just, just, just the social call again, I see.
**Andy Keller** 46:09 It's not just social, I'd like to… I actually know what's going on, either myself or maybe somebody on my team will hopefully get a little bit more involved, but for right now, just getting up to speed. So, yeah, I know, I know, it would be appreciated. If you want to return the favor and start joining Opamp SIGs, you're welcome to do that.
**Mikołaj Świątek** 46:30 I… I know, it's hard. You have… your schedule is hard on me. Like, it's… it's difficult for me to… to, like, get… to be available at that time, but I'm trying. I'll try… I'll try to… to be.
**Andy Keller** 46:44 No, it's not necessary, that's just… I just know what it's like to be in a SIG where there is a small group of people committed to it, so…
**Mikołaj Świątek** 46:52 I will say that, like, since you're… a lot of your interest is in the Open Bridge, right?
**Andy Keller** 46:57 fruit.
**Mikołaj Świątek** 46:58 you can… something I would like to help with, like, if you're actually running anything like it in production, you could, like, look at pull requests that actually are changing it. We have a bunch of them.
Like, that are, like, setting… trying to set, like… I don't know if this is actually… maybe this is someone from your… from your org. Like, we have a pull request where it's, like… we want to set, the instance UID to be, like.
based on the cluster UID and consistent.
within, like, some context, specifically, and I can approve it, it looks correct to me, but I also don't run this application.
**Andy Keller** 47:42 Right.
**Mikołaj Świątek** 47:43 so I'm, I'm, like, my view of… What the consequences are is, like, intrinsically limited.
**Andy Keller** 47:48 Yeah, I'll take a look at it.
**Mikołaj Świątek** 47:50 Alright, cool. Thanks.
**Andy Keller** 47:53 Yeah, no problem.
**Mikołaj Świątek** 47:56 Alright.
**Andy Keller** 47:58 I got YouTube gone, too, so… We've had a rough week.
Still get over it.
**Mikołaj Świątek** 48:07 I was sick, and then I got better, and then I traveled to Salt Lake, jet lag, got sick again, and got better, then had to travel back to Warsaw, and then had to jetlag, and got sick again afterwards.
You can kind of hear that I'm still not completely over it, but I'm better. No more flying over the Atlantic for me, like, for at least, like, a month.
**Andy Keller** 48:34 Yeah, yeah, sounds good.
**Mikołaj Świątek** 48:38 All right, let's, let's, let's, let's, let's, let's conclude. Thanks, everyone. Have a, have a good evening slash morning.
**Pavol Loffay (Red Hat LLC)** 48:49 Right.
