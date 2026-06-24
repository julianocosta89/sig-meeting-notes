SIG: CI/CD SemConv SIG
Date: 2026-06-23
Duration: 40 minutes
============================================================

## Zoom Recording Transcript

**Christophe Kamphaus** 00:32 Hello? How are you doing?
**Adriel Perkins** 00:37 Okay, how are you?
**Christophe Kamphaus** 00:39 A bit hot.
**Adriel Perkins** 00:44 Are you getting hit with that, heat wave in Europe?
**Christophe Kamphaus** 00:49 Yeah, it's, everywhere at the moment.
**Adriel Perkins** 00:53 Oh, wow.
Stay cool.
**Christophe Kamphaus** 00:57 Yeah, I'm drinking a lot.
**Adriel Perkins** 01:00 Good.
**Christophe Kamphaus** 02:20 And maybe let's get started, and if… Others might join.
Later.
**Adriel Perkins** 02:27 I was about to say the think tank.
We're gonna start with.
These items that we got.
So I came back this morning and read some of these comments here.
The two main things I want to talk about is, one, prototyping, and then two, like, what actually would constitute a VCS span.
Like, I think Git probably makes sense, like the Git CLI, because it is the utility that is meant to operate with version control systems.
But I think a lot of the CLI utilities that, you know, would run Even… even just the scripts themselves that would run inside of an action aren't VCS type things.
They're just units of work that may… Define their own span.
however they want.
Because they're not really specific to… The version control system, they're just general scripts.
So I was wondering if we had thought about that, and, and, like, what… scenarios do we feel fit with regards to, like, BCS action?
**Christophe Kamphaus** 03:50 One question, when you are talking about scripts, Do you mean… If you invoke a Git CLI, In your script or individual shared steps in the script itself.
**Adriel Perkins** 04:05 Yeah, like, individual shell steps, for example.
**Christophe Kamphaus** 04:09 Yeah, for me, that's not a VCS plan, definitely not.
If you want to, you can always use the… OCMZO.
As there is a CLI to emit spans.
You could use that if you want to manually instrument step.
Otherwise, we have the environment variable propagation, and CLIs that you use in your script could emit Zone telemetry.
**Adriel Perkins** 04:44 Right, but they still probably wouldn't be VCS.
Spans, would they?
**Christophe Kamphaus** 04:50 No VCS plans, it's really if you interact With a version-controlled system to check out code, to push, pull.
So, a bit similar to HTTP spans.
It covers the logical operation, so if you have multiple HTTP requests or SSH requests.
Underneath… You could regroup them under one VCS span.
**Adriel Perkins** 05:25 Okay, so the key word there is the VCS operations.
I assume that there is no prototype that exists.
**Christophe Kamphaus** 05:37 Not yet.
**Adriel Perkins** 05:38 I also…
**Christophe Kamphaus** 05:40 I also talked with the, General Samkonf yesterday in the SIG.
They said, yeah, it should be relatively simple to just point the AI at it and come up with one.
**Adriel Perkins** 05:53 Okay.
**Christophe Kamphaus** 05:54 I thought about doing it for Jenkins.
What about the, collector for GitHub?
**Adriel Perkins** 06:10 Oh… I'm sure it's possible.
I'm not sure how delightful it would be, though.
Because, like, for checkout, like, in… if you just talk about in GitHub, for example, they have a dedicated action, and so, like, realistically, that's probably the place… the action itself being instrumented, is probably the place for… for the checkout, because you don't control check out, or checkout commands, or get commands in that context. You just import the thing, and it does it for you.
Which means that, you know, all you really get is the… this was a checkout step, and you don't get anything beyond that.
And GitHub doesn't give you anything beyond that either, so either that would have to change, or there would have to be a custom one that… The mitts directly.
**Christophe Kamphaus** 07:02 Yeah, I think to start with, it would be sufficient just to recognize the GitHub, check out action.
and emit a PCR spend for that.
Other than that, yeah, you don't know, If any of your scripts would call it CLI.
It would need to be instrumented itself.
limit, VCS plans.
**Adriel Perkins** 07:33 So then in that context, even though it's a CI-CD task for checkout, it would also… it would be converted to a VCS span. Is that what we're saying?
**Christophe Kamphaus** 07:44 Yeah. So, underneath the CICD task, you would have the VCS spam.
So it would be two separate spans.
**Adriel Perkins** 07:59 Yeah, I mean, unless you change the underlying action for the checkout, I don't think we're gonna get that information. We're gonna… we're not gonna get the second span. It's still gonna show up as a task. Or… or we just convert it to a… BCS fan, is what I'm saying. Because that's a dedicated action. Does that make sense?
**Christophe Kamphaus** 08:17 So, basically, in the collector, In the GitHub receiver, you would detect if it's a GitHub Check out action.
and emit a VCS band instead. Is that what you're saying?
**Adriel Perkins** 08:33 That's… yeah, that's what I was asking.
**Christophe Kamphaus** 08:36 Yeah.
Yeah, I guess you could recognize it, and if we really want to, we could emit two spans instead of one.
What's that one?
**Adriel Perkins** 08:54 Yeah, I think the underlying thing it does would be the VCS spam, because that's the actual thing doing the operation, but the task itself wouldn't… but you don't have access to the underlying stuff, unless you instrument the action itself.
And just producing a span by recognizing it, it would just, like, it would just implement, essentially, a span that has the same… almost the same length, but doesn't tell you actually what's going on, because it has to be an artificial one, based off of what information you get from GitHub.
So that's probably not… I probably wouldn't go that path, for… unless we change the action itself, and I don't think that action's gonna… like, GitHub's not gonna change that action.
you're not.
**Christophe Kamphaus** 09:37 I mean, because it doesn't provide much, benefit.
We wouldn't have much more information.
**Adriel Perkins** 09:46 Yeah, we wouldn't have any different information. It'd be essentially just the same span duplicated twice, one with a task, a CSCD task, the other one with a VCS name.
**Christophe Kamphaus** 10:01 Yeah, fair enough.
**Adriel Perkins** 10:03 But, a potentially different option would be calling the GHCLI utility to create a release.
Do we con- do we consider a release interacting with the VCS as an operation?
condoning a VCS span?
**Christophe Kamphaus** 10:27 Currently, Release is not, we have not… defined it in our PR.
It's something to think about.
**Adriel Perkins** 10:50 Okay So I probably would, like… I'd like to see the prototype in some concrete… Which maybe I just missed some of the reading, because I will admit I… I didn't super deeply.
Read every word.
Because I got hung up on…
**Pellared** 11:11 I just have a question.
**Adriel Perkins** 11:12 Yeah, that's.
**Pellared** 11:12 releases, because I'm not sure if I follow… you mean releases, like GitHub releases? I'm not sure if it's really, like, related to Git or anything like that. I think it should be something separate, unless I'm missing something.
**Adriel Perkins** 11:27 Yeah, GitHub releases. A release against the VCS repository.
**Pellared** 11:36 That's a good question.
**Christophe Kamphaus** 11:37 question whether it should be part under VCS, or is it something else?
Yeah, that's.
**Pellared** 11:43 So I would propose to have something else, like, I don't know if GitHub or something related.
I think that also a release, at least in GitHub.
I think it could be just kind of an event.
which, of course, could, public, you know, it can cause, the tag creation itself, to have some, you know, workflow, but then we go back to the, you know, workflows, cementing conventions, etc. But I think the release itself, probably it will be more like an event.
**Christophe Kamphaus** 12:17 Yep.
**Pellared** 12:24 You can continue.
**Christophe Kamphaus** 12:26 We do also have CE.
Artifact semantic conventions, so… Probably it doesn't fit 100% under set.
**Adriel Perkins** 12:40 It would probably have those attributes attached with it, but the release event itself would be not an artifact, I don't think.
Like, who wouldn't fall under the artifact SimCom?
But I think that's something we gotta figure out.
Because…
**Christophe Kamphaus** 12:59 Yep.
**Adriel Perkins** 12:59 Because just the way that I… when I'm… when I'm thinking about the VCS, I'm struggling to find, like, what like, are we just essentially talking about instrumented Git… commands, or instrumented JJ commands, or instrumented… mercurial commands, you know, HG control, and are… is that really what we're just talking about, is those three CLI utilities being instrumented such that they can emit things like checkout, branch, merge, etc, and that's the scope of VCS spans? Or… Are we thinking, like, beyond that?
And so that's why I kind of am looking for, like, a prototype and, I guess, clarity around that, because I was just really struggling to figure out, like, what what things would really emit a VCS span.
In the context of a CI-CD pipeline.
**Christophe Kamphaus** 14:03 No, I think it would be any… use of the CLI and CLSS.
And for sure, if it's a… remote calls to a central system, then, You would have HTTP spans underneath, potentially.
**Adriel Perkins** 14:23 Alright.
Okay, well, I'll, I'll comment on that issue.
Referencing the request for the prototype.
We can go from there.
**Christophe Kamphaus** 14:51 Yep.
Sounds good.
**Pellared** 14:56 do we consider having a prototype in the Git, for instance, in the Git repository itself? Because, for instance, I know that Docker build, you know, has, like, kind of, you know, this kind of built-in instrumentation for open telemetry. Isn't something we even consider?
**Adriel Perkins** 15:21 I don't know where the prototype lives. I also don't know… Docker Build would… I don't know if Docker Build would be a VCS fan. I think that's what I'm.
**Pellared** 15:29 No, no, no, no, no, no, no, sorry, maybe I explained it wrongly. I mean that in the instrumentation code.
I think, in theory, could live in, for instance, in the Git Scylla itself.
Because, for instance, if I remember correctly, if you use some, I don't know, environment variables or something, for instance, the Docker build could, itself, you know, instrument and emit spans.
And, in theory, Git could do it the same.
Instead of, you know, wrapping all the things, if it could be, you know, included into Git itself.
**Adriel Perkins** 16:06 Gotcha, like actually opening a pull request for Git to support instrumentation.
**Pellared** 16:12 Yeah.
**Adriel Perkins** 16:13 Just like having a prototype of that implementation.
**Pellared** 16:16 Yes, that's what I thought, just having a prototype of this information, some draft PR, or something like that.
I'm just checking quickly…
**Christophe Kamphaus** 16:24 I think there is already something.
On my research, I found this.
**Pellared** 16:40 Oh…
**Christophe Kamphaus** 16:46 No choice, that's… A standard build of the Git CLI.
**Pellared** 16:54 Even if not, there is someone, you know, you have an author.
we wish we can even contact with something, you know, for collaboration with Jeff, yeah.
On the top, there's the author.
**Adriel Perkins** 17:17 Yeah, that might be something to look at.
**Pellared** 17:26 Because in my world…
**Adriel Perkins** 17:26 I remember this post, actually.
**Pellared** 17:30 Because my worry is if it will not be included into Git or something like that.
then I'm not sure how… Feasible it will be to, you know, have this… have this instrumentation, have it working, if it will be something that people actually will be used to adopt.
**Adriel Perkins** 17:48 Yeah, agreed.
**Christophe Kamphaus** 17:50 Yeah, because there's so many uses of the Git CLI in scripts.
**Adriel Perkins** 18:05 So I… in that message that we send on the thread, I can mention that it would be good to, like, for a prototype, it'd be good to try to Create a branch.
For Git.
I'm showing that that work… can work natively.
That'd sound good.
**Christophe Kamphaus** 18:22 Sounds good.
**Adriel Perkins** 18:25 Alright, let's hope I remember that.
I'm a bit… bit behind. Alright, I think the next one was… Swan.
**Christophe Kamphaus** 18:37 Yeah, so release candidate PR for VCS.
**Adriel Perkins** 18:46 Yup.
**Christophe Kamphaus** 18:48 Okay, you're approved.
**Adriel Perkins** 18:51 Yeah, I saw the, I saw Carlos' approval through my email this morning when I was going through, and then I was like, realized that Trask had messaged me a week ago, so sorry about that.
**Christophe Kamphaus** 19:02 No problem.
I think, Sam, that one is good too much.
**Adriel Perkins** 19:11 Agreed.
**Christophe Kamphaus** 19:24 And from my side, the Jenkins PR for adopting the CICD semantic conventions is progressing now.
He's a new guy.
Started reviewing it.
But yeah, let's see.
Oh, it goes.
**Adriel Perkins** 19:48 Cool.
It's not a ticket, but I've been using, I know we've talked about adoption in the past.
And I've been recently using, Tukton for, a side gig.
And they have instrumented the controller with, openTelemetry?
But, it's really hard to find.
anything about your CI CD pipeline from the telemetry? It's a fairly difficult experience. It's great that we have the traces, but… I've… I've struggled.
Looking through that, the telemetry, like, by hand.
And so, given how much they've… how much effort they put into instrumentation, I think they might be in a really good place for, like, me or someone else to open a contribution, seeing if we can help them get, onto the semantic conventions for… For CICD. So, I'm gonna be reaching out, I'll… Hopefully, I'll put an issue, up on the board.
So we can track it. Let me just write that to-do.
**Christophe Kamphaus** 21:07 Yeah, that would be great.
That we would have… the Argo workflows. Alan did that part.
Jenkins, hopefully soon.
And GitHub and GitLab.
**Adriel Perkins** 21:25 So I'll open a SU for that, but I'm gonna reach out to them.
They're pretty… they seem still fairly active, pretty stable.
And they have done a good job of tracing in their controllers, so… Just a measure, I think, of semantic convention adoption, which would make it easier to actually analyze this stuff anyway, so… I'll be opening an issue for that then.
Okay.
Going back to this…
**Pellared** 21:56 I have a question regarding, like, the knowledge sharing, because I have missing knowledge. Do we have something working for the GitHub instrumentation for CICD SAMCon?
**Adriel Perkins** 22:12 I didn't follow that, I'm sorry. Can you repeat that?
**Pellared** 22:14 you mentioned right now the CICD conventions, the semantic conventions, and you mentioned, you mentioned GitHub, right?
**Adriel Perkins** 22:22 Yes.
**Pellared** 22:22 sections.
Do we have something working, or is it just about registry as some con… or do we have some, I don't know, workflow, some, I don't know, custom GitHub runner, or anything like that?
**Christophe Kamphaus** 22:35 So.
**Adriel Perkins** 22:36 I'm a receiver? Yeah, go ahead, sorry.
**Christophe Kamphaus** 22:39 No, you did, you implemented it, go ahead.
**Adriel Perkins** 22:42 We have a GitHub receiver in OpenSelemetry Collector Contrib that takes, essentially all the workflow run, and workflow job events that come from GitHub webhooks.
and converts them into traces. It's actually been running for quite a long time. We demoed it at KubeCon a couple years back.
And… but we still get, actually, traces. I need to go update the actual receiver, because it's still using a bug version… a version with a bug. But every repository in OpenTelemetry actually Already has… traces being emitted from all the actions. So we actually have this information available to us, within OpenTelemetry as well.
But that's… it's just converting, essentially, events to spans, is really what it's doing. And then tying them to semantic conventions, so… But it does exist.
**Pellared** 23:47 Wow, awesome.
**Adriel Perkins** 23:56 There is a… I'm so lost on where my tabs are. There is a effort that I heard about, with regards to having shared workflows within OpenTelemetry.
That they're kind of working on.
And if they go that path, it actually might enable us to get some more granular instrumentation available to us.
And do… and, like, federate that out through that shared workflow mentality. So if there's, like, If, like, we own actions directly, we can instrument them, and then if we own the underlying aspects of the action, like what the action is calling or doing.
in the step, then we probably could start to leverage some of that deterministic ID and start getting more granular traces into the backend.
But I don't know if… I don't know if they're thinking about that, yet. I'm just saying it's opening the door for possibility there.
**Christophe Kamphaus** 24:58 You are talking about the part where we can also set the environment variables.
**Adriel Perkins** 25:05 Yep. Which also kind of is… would be cool, because then we're also using the environment variable context propagation spec to handle the underlying calls.
So it all comes together.
Ben, actually, that might be cool for the, like, to show in the blog post. Actually, if we do implement that in OpenTelemetry, that might be a cool little teaser in the blog post.
**Pellared** 25:34 if I understood correctly, that… that's… that's why also why I was asking, like, have, you know, for the blog post, for the context, for the event carrier, etc, to have it, you know, like, end-to-end. So right now, it's not working, right? Do I understand correctly?
Or we do not have anything that can, like, you know, backfish from the CLI tools, the spans which are created back to the collector.
**Adriel Perkins** 26:01 We could enable it. We could make it work, yeah.
It's not there today, because the spec didn't exist when I set up the infrastructure.
But, the way the infrastructure works is, it takes everything from the webhook, and it goes through a Cloudflare tunnel.
And I… we were doing it as part of the InfraSig, but the InfraSig has shut down, so I have an outstanding task for me to, like, update the community form showing, like, that it… where the infrastructure lives, and that it's going back to my own repo.
But, the point there is, is that we already have a secure connection out to that cloud instance, so if we do instrumentation of our actions at the step level using the environment carriers.
then, we can just open an OTLP, endpoint in that same infrastructure, and then as long as we do… as long as the environment variable context propagation is the deterministic ID, then it will show up in the same set of traces.
But at a more granular level. Does that make sense?
**Pellared** 27:07 Yeah, it makes sense. So, this collector is running, inside the GitHub workflow, or somewhere separately?
**Adriel Perkins** 27:16 It's running inside of a K3S cluster inside of OpenTelemetry's Oracle Club.
**Pellared** 27:22 I see. So we need to establish and show what, like, use the same endpoint, so that the steps… I see. I think I follow. Yeah. You can continue later.
**Adriel Perkins** 27:34 Yeah, we can, we can definitely.
**Christophe Kamphaus** 27:39 And for the deterministic trace IDs.
there was a GitHub was it action to construct some and set the environment variables, so it matches generated by the… GitHub receiver.
**Pellared** 27:57 Fair enough.
**Adriel Perkins** 27:59 Yeah, so we can essentially just export to the same path, but slash OTLP, and the event… Would you go there?
And this is… again, backed by Cloudflare, so, this is technically not open to the world. We have some controls there that not everyone can just send OTLP data. It has to come from within the CI runners, so… Yeah, if you want to, like, take that offline, and as we talk about the blog posts, then I'm happy to help assist in that.
**Pellared** 28:41 Yep. Worse for me.
Do you want me to… do you want to discuss the blog post right now, or is there anything else?
**Adriel Perkins** 28:54 Sir, whatever, whatever you'd like to do.
**Pellared** 28:56 Yeah, so my… my main question is, do you, I had two ideas for this one.
One was, just to create it together with, jesus, I have forgotten, I have forgotten the name, I'm very bad at names.
Sorry for that. With Alan, I thought about meeting with Alan a blog post, because we were preparing a talk for KubeCon, but later I thought that maybe we should Maybe we should try to do something together. I mean, even with you as well, with you, Christoph, and maybe also with Alan, something called, like, you know, as a group.
And I thought about just creating some Google Docs, even to… Grab ideas. What… what do you propose? What should be there?
Initially, I thought just about saying about the environmental carrier, but then I thought that I think we should… it would be better in a blog post, like.
has a story, and maybe has an example where it could be used, and this… this is when I started thinking about, you know, this GitHub, the GitHub workflows may… I may be addressed the thing that you show.
to show how it can be used as an, you know, as an example in practice, how open telemetry dogfoots its own, you know, semantic conventions, its own ideas.
So yeah.
I don't think it would be bad, even if the blog post will be kind of lengthy, because I think it will be an article. Because I thought about having, you know, one blog post right now, when we are trying to hit the release candidate.
And then, when we'll have, you know, stabilized it after some months, then it will be a very… maybe this will be shorter. But if we try to publish something now, before it's stable, I think we can also have the opportunity from the community to get some feedback, you know, requests, etc.
And probably the more detailed, you know, the adventure will be, if we put some examples how to use, we increase the chances that people will actually use the semantic conventions and not only read it.
**Adriel Perkins** 31:12 Yeah, no, that'll make sense. I think two sounds… two, at least, sounds… sounds good. It could be also, like, a little series, so to speak, right? I mean, there's a huge win in doing… announcing stabilization. This thing's been going on for… you know, it was proposed, like, what, 5 years ago? So… And then it took a, like, like, 4 years to get the, like, OTEP actually through the door.
And I think it got recreated, like, 3 separate times, and then now we're, like, almost a year later, maybe a little bit more, maybe a little less. We're actually stabilizing it, so, like, that's a whole journey that you could talk about, in, like, one post, but then, like, the how to use, and, like, what the practical implications are, and how this unlocks the door.
For things, and, like, that concrete… Set of, Not guidance, but example usage and code and, like, showing it working in real life, would be a very cool second blog post, for sure.
**Pellared** 32:11 What do you see the value of the first blog post?
**Adriel Perkins** 32:15 Mainly, like, content, historical context, championing the Open Solomonetry community for swarming around this issue. A lot of good work has gone into it. It's unlocked the door. And just, like, general, not marketing, but, Notification, I guess is the way I'd phrase it.
**Pellared** 32:39 Okay, because I thought… About combining the first and second.
Because I think that if an example, it will strengthen why it's important, you know, and how it will be used. That's why I thought maybe having even some, like, lengthy blog posts, but yeah, I'm not sure, I'm just, you know.
thinking out loud. You know, there's also one disclaimer for you as well, just to, like, make you more happy. I'm not sure if you know that, for instance, trace context is not yet stable at all.
The W3C, I don't know if baggage is stable as well, so things that we are, you know, using, still, like, release candidates or things like that.
So you're doing a pretty good job here.
**Adriel Perkins** 33:23 Awesome.
I mean, I'm down for whatever, so… they're just ideas. But yeah, if you want to spin up some Google Docs, one or many, like.
Happy to… Right?
**Pellared** 33:38 Yeah, probably I just want to use the Google Docs just for grabbing ideas and things like that, you know, brainstorming, you know, some… maybe proposing some use cases, you know, some setup. How do you imagine having some example use case?
that you'll use to, you know, and then probably you'll prefer to have a PR, which is easier to comment, address changes, use Copilot, and stuff like that.
**Adriel Perkins** 34:04 Sure, sounds good.
**Pellared** 34:06 Christoph, what about you? What do you think?
**Christophe Kamphaus** 34:08 Yeah, sounds good.
I can also contribute some ideas if you want.
**Pellared** 34:13 Yeah, I'd love to.
**Christophe Kamphaus** 34:17 I remember also… when we defined the initial CICD, semantic conventions, we also wrote a blog post, and I think it was even one of the mostly viewed ones, one of the mostly viewed pages in all of OpenTelemetry.
**Pellared** 34:37 So I'll double-check this one.
That's it from my side.
**Christophe Kamphaus** 34:59 And, yeah, thank you very much for driving the environment variable.
effort.
**Pellared** 35:07 Thanks for your reviews helping me as well. Do you have any comments, Christoph, from your side regarding these implementations? Any thoughts? Anything that you think that I should, you know, look at it before going RC or stable? Any concerns?
**Christophe Kamphaus** 35:22 The one you highlighted about the caching behavior, I think that's an important one, because there's differences between the Implementations on that, definitely.
**Pellared** 35:34 Okay.
**Christophe Kamphaus** 35:39 And yeah, we did have some changes still in the last time, so I'm not sure if every implementation has taken them yet.
**Pellared** 35:49 Yeah, I want to double-check it in propose PRs to make sure that they are having it.
the only problem for me was C++, like, I didn't want to install a lot of stuff and make it build.
So I just asked Mark if he could do it.
**Adriel Perkins** 36:07 Don't blame you. I don't blame you at all. Do you know if, I haven't seen any movement on, the issues.
But have you heard anything from whether or not the Rust or Ruby or PHP or Erlang folks are gonna do anything, or do you have any plans to try to contribute to those?
**Pellared** 36:28 I think Rosa…
**Adriel Perkins** 36:29 They're the last four.
**Pellared** 36:32 For Rust, there is some PR. I was talking with CJ, and he told me that he can take… right now, he's a company in India, and he said that he may try to help in this area.
for, for PHP and Arabi, I can try to just create DPRs myself. I haven't seen any movements there, so I can just try to… I can try owning it, and I know Azure, you can do it as well.
**Adriel Perkins** 37:01 Yes, yeah.
**Pellared** 37:03 Okay.
**Adriel Perkins** 37:05 Cool. Yeah, that's good to know.
I mean, do people still write PHP? I guess.
No, they… they do, so, that's, well, that'll be good. I mean, still, it's, like, way more progress than I expected, so…
**Christophe Kamphaus** 37:22 We'll support all the WordPress sites.
**Adriel Perkins** 37:24 Yeah.
**Pellared** 37:25 would… I just want to make a joke that once my friend told that if someone in work will tell him to write PHP ever again, he'll quit the job. I hope that I will not do it.
**Adriel Perkins** 37:36 Yep.
**Pellared** 37:38 This is just a joke.
**Adriel Perkins** 37:42 I, there might be some truth there.
Okay, no, no, cool. So… That sounds, yeah, absolutely what Kristoff said. Appreciate you running with all this stuff, that… it's super appreciative.
Have you gotten a chance, by chance, to re-look at the Python one? I think the original implementation I did in the Python one might have diverged from the changes in the specs, so I don't know if you circle back to it.
**Pellared** 38:11 Yes, yes, yes.
**Adriel Perkins** 38:11 If not, I can take a look.
**Pellared** 38:13 I think that someone already addressed, and made it compliant. I created, I think, an issue to make it compliant. Maybe you can find, yeah, this entire career, the second one, and just, you know, find history around this one.
if you go, you know, top right, top right stuff… no, you can look at the history. I think someone else Feed update, you see in the middle.
8 of May. I think this was changing, a lot, this PR.
Was making the most of the changes to make it compliant with the specs.
**Adriel Perkins** 38:50 Oh, yes, okay.
Sweet.
**Pellared** 38:54 I think there's some edge cases.
But it's mostly done. These are only, you know, like, at cases, tiny issues, like, I don't know, normalization of empty name, which is impossible to do in a real-case scenario, and things like that, probably.
**Adriel Perkins** 39:15 Okay, no, cool. Fantastic.
**Pellared** 39:20 I already use the… it should, like, I think all the languages.
Even if they are not 100% spec compliant, they should be usable, and they should, you know, cover most, you know, all happy path scenarios.
**Adriel Perkins** 39:37 Yeah.
Fantastic.
Cool. Anything else for the day?
**Christophe Kamphaus** 39:51 Not from my side.
**Pellared** 39:56 Nothing for me.
**Adriel Perkins** 39:59 Well… Sounds good. Thanks for joining.
See y'all next week, and probably throughout the week, so… Take care.
**Pellared** 40:06 Yeah.
**Christophe Kamphaus** 40:06 Steal.
