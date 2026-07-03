SIG: Go Compile Time Instrumentation SIG
Date: 2026-07-02
Duration: 86 minutes
============================================================

## Zoom Recording Transcript

**Kemal Akkoyun** 03:54 Hello, hello.
Okay.
Who wants to facilitate this meeting?
I've been doing this.
In a row for a while, and I have connection issues today. Yes, my camera.
It goes down, as you can see.
So, I need a volunteer for facilitation.
**Xabier Martínez** 04:29 I don't…
**Kemal Akkoyun** 04:37 On what?
Volunteers?
**Dario Castañé** 04:40 I can volunteer.
**Kemal Akkoyun** 04:42 Awesome.
**Dario Castañé** 04:46 Okay, so let's do this, Give me a second, I will share a screen.
Do you see my screen correctly? Big enough?
**Xabier Martínez** 05:10 Yes.
**Kemal Akkoyun** 05:11 Yes.
**Dario Castañé** 05:12 Perfect.
Anything… Oh, it's this one… Is anybody else missing from the attendees list? Please… At yourself.
If you are not.
Excellent.
Yaki's not present.
Let's see what card.
Okay.
So, let's go through the agenda before starting. Any last-minute ballot point?
Agenda item that you want to add?
Okay, let me copy this.
Pure.
Okay, well… Let's do it like this.
Probably easier to follow later.
So… First point, problematic.
That's Kabul the Rahman.
Any comments? Updates? Anything that…
**Kemal Akkoyun** 06:52 I think, we have a lot of PRs open for all these issues.
Everything is in motion. I don't know if there is a task… I think there is only the vending one, that there is no PR.
And rendering is not… Actually, not, like, mandatory to have.
I think we just need to review, make sure that if… the PR creators, if they're not responsive, a maintainer can just, like, push that to the conclusion by just, like, committing directly to that branch, we have the rights.
So that we don't, like, omit the contributions for the original order.
And then just, like, make sure everything is handled. I already seen that, like, Avin claimed certain issues, that's amazing, thanks for that, and we should do the same, and yeah.
I don't know if you… do you have any questions on that, or, like, any comments? Do you disagree, agree?
**Xabier Martínez** 08:04 I totally agree. Also, I think that we need to… focus mainly on the pull request related to this P1 release.
and avoid, like, reviewing other PRs until we finish, this V1. So we just focus full on this, like, try to close it, and then we continue with the rest of the tasks.
**Kemal Akkoyun** 08:29 100% agree. Yeah, we should prioritize the ones that, like, waiting.
If you go to the issue, I think there's the sub-issue section, and you can see that, like, in that sub-issue, there's, like, 3 items that we actually don't have, the other one, the roadmap one.
Yes, if you scroll down… I think in this view, yeah, sub-issue view, you can see that, like, there's, like, 3 issues that we don't have PR for.
I think so, if it's accurate. Yeah, like, maybe the DNS parser lacks extensibility. That one… Maybe someone needs to take care of that?
If you don't have… an issue, like… Oh, we have one.
**Dario Castañé** 09:25 There is a PR, I don't know why it's not showing in the sub issue.
**Kemal Akkoyun** 09:30 Maybe it doesn't say it's fixes or anything.
**Xabier Martínez** 09:33 Mmm, yes.
**Kemal Akkoyun** 09:36 Yeah, I think, yeah, if you can edit the… description and say that, like, this is fixing that issue, I think it should map that.
I stayed at, like, the… go to the bottom, I think it's 5-4.
8 already.
They have the, they have the issue link, but it's not… it doesn't say that, like, it's fixes. And I think the PR owner, he's not responsive, so maybe we can take this over?
**Dario Castañé** 10:13 Okay.
I can try to take a look today to this PR.
**Kemal Akkoyun** 10:19 Awesome.
**Dario Castañé** 10:19 Oh, I'm going to assign it to myself.
There you go. Now it appears, yeah. It's.
**Kemal Akkoyun** 10:30 Cool.
And we have the website, like, the website issue, and I guess we have another agenda item for that anyway, so we can discuss.
**Dario Castañé** 10:42 Nope.
Okay, do we want to go item by item now, or…
**Kemal Akkoyun** 10:53 I think we know what to do. What do you think? Like, we're just going to review, take over, like, we can do this async on the issues. If you see that it's not claim, let's, like, claim. I will do the same, and, like, we can sync over on the Slack channel.
And yeah, Azar is already… Yeah, okay, sorry.
**Xabier Martínez** 11:15 No, I agree with you. I think that all the issues already have a pull requests open, so we just need to unlock some of them and review others, so let's try to push them and try to close.
**Kemal Akkoyun** 11:32 Yes.
Yeah, I think we can, like, close all the issues this week, for sure.
And maybe next week, or depending on the progress this week, we can cut the release.
And… yeah, before we actually… I don't know.
Announce it. We can take our time for, like, the documentation pieces, and maybe crafting the blog post, and then we can start to be super vocal about it.
**Dario Castañé** 12:09 So, in conclusion, we are going to work synchronously during the… The two days left in this week.
And try to push.
As much as possible, right?
**Kemal Akkoyun** 12:21 Yes.
**Xabier Martínez** 12:23 Yes, but, I mean, I wouldn't… Like… commit directly to try to finish this week. I mean, if we need a couple of extra days, that's no problem. Yeah.
And also related with the P1 release, that's the next point.
I think it will be good to define exactly which are the tasks that we want to push, and maybe define the owners.
or leave them, or… we can do it async in Slack, or in a GitHub issue, but try to…
**Kemal Akkoyun** 13:01 A weekend?
**Xabier Martínez** 13:02 I doubt it.
**Kemal Akkoyun** 13:02 We can do it right now.
**Xabier Martínez** 13:05 Yes.
**Kemal Akkoyun** 13:06 Let's not defer this, let's just decide on it. I would be happy to coordinate with Jurassi and other, like, GC members on the announcement and the blog post.
I'm happy to take those two issues, if there are no takers.
**Xabier Martínez** 13:27 Hmm, sure.
Let me know if you need help with that, or for reviewing the, those things.
**Kemal Akkoyun** 13:36 Of course, like, we can always, like, share the burden, I will let you know.
And I think the cutting the release is also, like, super easy. It's just a tag right now. I think we have the pipeline, and I would be happy to take that as well.
**Xabier Martínez** 14:00 So, you know, they can't…
**Dario Castañé** 14:01 On the blog post, the announcement, and after the… The action of cutting the release once everything is ready.
**Kemal Akkoyun** 14:10 Fair.
I don't mind. If there are any other volunteers, please go ahead, like, I don't want to block.
I mean, this is my sole thing this week, and maybe the next. I really want to finish, that's why I'm, like, I have time.
I'm already dedica- I already dedicated my time to finish this up.
**Xabier Martínez** 14:35 Okay, let me know if you need help with the blog post, or I can also spend some time on that.
Do we need… are there other ideas, or this is enough for releasing the big one?
**Azhar Momin** 14:55 I…
**Kemal Akkoyun** 14:56 I think it is.
**Azhar Momin** 14:58 Yeah, I wanted… I mean, other OpenTelemetry Go projects use the… go.opentelemetry.io module pass, so… do we also have to switch to that module pass, or are we going to keep the grid somewhere?
**Kemal Akkoyun** 15:13 I think this is a great topic. I don't know what is the convention in there, but, like, we should definitely check the OBI.
And similar projects, and if… if… if what is… if that is what they are using already, we should just do this before the V1, for sure.
Let's be consistent within the projects.
I haven't checked this. Have you checked? Like, the… for example, OBI comes to mind.
**Azhar Momin** 15:44 I check. GoContrib and other… some other Go build tools, which uses the go.opentelemnetry.
**Kemal Akkoyun** 15:51 Yeah, OBI is also using Go OpenTelemetry.io.obi. I think if this seems like the convention, so let's do this.
Yeah.
Let's do it.
And let's check… Azar, do you want to take care of this?
**Azhar Momin** 16:18 Sure, sure, I can also…
**Kemal Akkoyun** 16:19 Okay.
Thank you. Can you also check, like, is there a special way, like, that we need to do for, registering?
for, the Go OpenTelemetry I.O.
**Azhar Momin** 16:33 I will look into that.
**Kemal Akkoyun** 16:35 Yeah, I think… This is… this is, by the way, a great catch.
Thank you for, like, noticing this, especially before V1.
Yeah, if you can… if you go to go.opentelemetry.io, it actually lists all the projects that is using that, but I don't know if there's… maybe this is just, like, something automatically generated, so we don't need to do anything, but we just need to make sure that… Yeah, that's the case. This could be automated.
But, yeah, maybe we talk with the admin.
like, asking this, OpenTelemetry maintainers channel on the Slack, after creating the PR, whether we need to do something else.
**Xabier Martínez** 17:28 So we have an issue under the… Roadmap B1, just to track this.
**Kemal Akkoyun** 17:35 I don't think we have… I don't think we have an issue, but we can definitely create one and add…
**Xabier Martínez** 17:42 Yes, I say yes, creating one.
**Dario Castañé** 18:01 Okay.
**Kemal Akkoyun** 18:05 Maybe we should talk about, like, the name, which modules we want to use.
Like, should we go with compile-time instrumentation, or should we go with OTLC directly?
**Azhar Momin** 18:18 I think we are using compiled instrumentation already in some parts of our course, we can use maybe that.
**Kemal Akkoyun** 18:26 Yeah, like, they used OBI, which is, like, super concise.
But their compile time, okay. I think… I don't know, what do you think? I kind of like that, the concise nature of, like, using just something like OPI, but then…
**Azhar Momin** 18:47 I think we can go to Sudan.
**Dario Castañé** 18:52 The only issue I see is using all teleg… So, what LC is that it's pretty close to this one.
**Kemal Akkoyun** 19:00 Yeah, it's inevitable.
Yeah, it's… I think it's inevitable to use those things.
But…
**Dario Castañé** 19:07 Yeah.
**Kemal Akkoyun** 19:08 Hotel is so ubiquitous.
Yeah, Autel… that's OpenTelemetry Go SDK and HotelC, the compiled one, or VI, the auto-instrumentation, which is not Go-specific. So, yeah, maybe, like.
I am kind of… Leaning against to just to have the hotel C.
What do you think?
**Azhar Momin** 19:32 I think both satisfied.
**Kemal Akkoyun** 19:38 Because it's… especially if you go to our, like, submodules, in the repo, it becomes, like, it's already, like, too long, and it becomes, like, open parametric, like… compile time instrumentation, slash instrumentation, slash DNS, some, like, or, like, SQL, blah blah, like, it's just too long, so maybe… Hotel C's.
**Azhar Momin** 20:02 Sure.
Or does he do?
**Xabier Martínez** 20:17 Therefore, for me, okay, if that's aligned with, other OpenTelemetry variables, using Autel-C here.
I like it.
**Dario Castañé** 20:27 Okay.
**Kemal Akkoyun** 20:46 Okay.
**Dario Castañé** 21:07 Okay, Any question, concern about this last bullet point? If not, we can go to the last one, OVI Berthus Hoteli.
**Xabier Martínez** 21:22 Yeah, I just put this one just to discuss a bit about the differences.
If we want to contact them.
And, Kamala explained, I think, well on the maintainer side.
We should definitely…
**Kemal Akkoyun** 21:51 Go ahead, please, sorry. I thought you finished.
**Xabier Martínez** 21:55 Oh, no, no, I was saying that you define correctly in maintainer set, but that's not visible for all the team members here.
That, OBI just defined the… no, OTC defined the USDT proofs.
and OBI just kind of finding the… new signals based on EVPF.
So, but… I'm not sure if… those use cases are well-defined or documented. Like, it could be confusing for users.
So maybe we need to align with them, like, how… We define this project, like, how to announce or make these differences a bit more clear for the users.
**Kemal Akkoyun** 22:48 Okay.
What we should do… Yes, ma'am.
**Xabier Martínez** 22:52 Digital.
**Kemal Akkoyun** 22:54 I think my idea is, like, what we should do is talk with the governance committee and reach out to some OBI people, and create a joint blog post on how do you auto-instrument go in hotel ecosystem, and in that blog post, we have… we can have like, co-authors, one from OBI, one from our side, and we can discuss pros and cons, and clearly guide the community members, like.
What would be the trade-off?
Between choosing these two projects.
And… I think that would be the most, like.
Clear message that we can send all together, right?
We have different goals, right? We should document those, and then we can also talk about Ave?
For future, and how we can collaborate.
Between two projects, right?
Like, in… In a really high-level view, we try to solve the goal auto-instrumentation problem, but we have different trade-offs.
trade-offs, and I don't know, like, how you know about the OBI, OBI is eBPF-based.
And… You can just enable it on the runtime. You don't need to change anything in your Go application.
But then, the… it… You know, some, like, some shortcomings, like… if you deter… like, terminate the TLS within your process, you can't access all the details, for example. I think there are some brittle facilities around context propagation, because it's, like, a hard thing to solve from… kernel site using just eBPF to find the correct context header and inject that, and, like, coordinate between incoming and outgoing connections, network connections.
And, yeah, you need to do a lot of in-memory offset calculations to make sure that, like, you're reading the correct places, whatnot. When you compared all those aspects with OTLC, OTLC is just, like.
it's more stable, right? If it compares, we know that we're gonna generate all these, all these signals, if it compiles in any Go compiler, it would… any architecture or platform, it would just work. We can handle all the, like, context propagation clearly, whatnot, but then you need to change your build pipeline, right? Like, compared to that. So if we can clearly Like, word out all these, like, trays off.
Yeah, and I… as I all told in the maintainer channel, what we can also explore is what… how we can enable the OBI.
We can, for example, go compile time toolchain. It doesn't have a way to generate USDTs, user-defined trace points for Linux, but we can actually build some facilities to Hotel C, And actually, somehow, like inject these, because we can also patch the compile time and runtime itself, and we can, like, patch… come up with patterns in a way that basically generate the USDTs and add those to the F binary section, so that they can discoverable. I am, like, I actually drafted a like, super early draft of these things, using, our, like, own tool, Orchestrian, but, like, they're interchangeable. And then what would happen is, like, it would live OBI really… OBI life, like, super, easy, more convenient, because now you have the USTTs, you can hook into the USTTs from the eBPF. If you put those tracing points into the correct places, it's easier. So, we can come up with, like, a joint project in the future like this.
But, like, yeah, let's start easier, come up with the first blog post, and then maybe we can talk about our project, and come up with a joint RFC, and, like, move forward with that.
I think have been already, like, getting in touch with our BI people. They are working on I think… correct me if I'm wrong, Habin, you are proposing a joint talk for the next KubeCon with OBVI and OTLC. It's already a great, collaboration opportunity, and I think he's also working on some other stuff together with the OBI. Yeah, he can confirm.
I think he… we couldn't hear him, but he opened his mind.
**Haibin Zhang** 27:55 Yeah, yeah, yeah.
I, I think we, I will, look into the difference between the OBI and, our system about, for the goal, application, and I will, to the next week's meeting about the OBI, to introduce our… our, project.
**Kemal Akkoyun** 28:24 Is this meeting as part of the SIG meeting? .
**Haibin Zhang** 28:28 Yeah, yeah, yes.
**Kemal Akkoyun** 28:32 When is it? We can also attend? Like, I… Next week, you said?
next Wednesday?
**Haibin Zhang** 28:39 Yeah, Thursday, Thursday, Beijing time is the, the…
**Kemal Akkoyun** 28:46 Oh, okay.
**Haibin Zhang** 28:47 Turf. Turf in unique.
**Kemal Akkoyun** 28:51 Okay, so it's not the part of the SIG meeting, this is something different than the regular SIG meeting?
**Haibin Zhang** 28:59 Okay, I'm a, Senator, committing to our Slack.
**Kemal Akkoyun** 29:06 Okay, thank you.
**Xabier Martínez** 29:20 And, going back to the blog post idea.
I think it's the right move. We can push it.
**Haibin Zhang** 29:27 I…
**Xabier Martínez** 29:27 I really like it, and… We more or less have, The ideas, of what to put there, so… we can push, this collaboration. I think it's right.
we can also comment in the next meeting that, Hyping just commented.
We can propose that idea to them.
**Dario Castañé** 29:59 Okay.
Anything else that you want to discuss about this last point?
I think we have an agreement, right?
**Kemal Akkoyun** 30:12 Yes.
**Dario Castañé** 30:17 Anything else that we have missed today to talk about?
**Kemal Akkoyun** 30:23 Since we have time, maybe we can open the PRs, that's waiting for… Review, and maybe assign a maintainer to review those, like…
**Dario Castañé** 30:37 From the Rombo.
**Kemal Akkoyun** 30:38 Since we have time.
**Dario Castañé** 30:40 Yeah.
I took the issues… Don't promise.
**Kemal Akkoyun** 30:53 There are some other issues also, in the body.
If you go to Roadmap again, like, scroll down, yeah, there are some other open issues.
Yes.
**Dario Castañé** 31:06 Okay.
OpenAI… One… I think there's one.
**Haibin Zhang** 31:20 Yeah, Obama and the Kafka is, he's already, and I will… I will change things.
**Kemal Akkoyun** 31:32 Yeah, we can assign this to Habin. He's already, like, checking these.
This issue, and maybe the PRs?
**Haibin Zhang** 31:39 The PR is, more to the man about the OpenAI SDK, and Kafka is, now, It's a CI test.
**Kemal Akkoyun** 31:55 Yeah, you can assign this to Habina as well. He's taking over another, yeah, that one, for example.
**Haibin Zhang** 32:00 January.
**Dario Castañé** 32:08 I will assign all to the PR.
**Kemal Akkoyun** 32:11 Yes.
**Dario Castañé** 32:14 This one… Don't… this other one had the PR, but it's closed.
**Kemal Akkoyun** 32:23 Yeah, we merged some alternative now.
**Dario Castañé** 32:26 Okay.
**Kemal Akkoyun** 32:27 Just merge that.
Yeah, let's… let Habin decide if we need to do another follow-up, or just, like, consider it done on the issue.
**Dario Castañé** 32:46 Is there anything missing with this PR? Hi, Lim?
Or if you.
**Haibin Zhang** 32:51 Yeah. And… the roadmap, I would say it's, the studios about this SDK.
**Kemal Akkoyun** 33:10 But that means… but OpenAI, I think that means it's done. You can close the issue as well, I think.
**Dario Castañé** 33:15 Okay.
**Haibin Zhang** 33:17 Yeah, yeah.
**Dario Castañé** 33:18 Okay.
Let's do that issue, okay, I… useful.
But I think the PR didn't mention this, but that's why I was looking at.
**Kemal Akkoyun** 33:42 Yeah, it's a distance.
**Dario Castañé** 33:43 portal.
It's open.
Yeah.
Nice.
One less.
**Kemal Akkoyun** 34:00 Yes.
**Dario Castañé** 34:02 This one…
**Kemal Akkoyun** 34:05 There… there is a PR to this, I think.
**Dario Castañé** 34:09 Yo.
**Kemal Akkoyun** 34:09 the merge one, and there's another open PR.
I remember pinging them, but… Yeah.
**Dario Castañé** 34:21 Okay.
**Kemal Akkoyun** 34:22 It needs a rebase and whatnot.
**Xabier Martínez** 34:25 Sign… Meaning?
**Dario Castañé** 34:28 Okay.
**Xabier Martínez** 34:30 Yeah, I would take care of this one.
**Dario Castañé** 34:35 I will… Here, so… You have everything aligned.
Perfect, thank you, Shabir.
And… what else? Define injected code overhead SLO and enforced in CI.
**Kemal Akkoyun** 34:54 I think this shouldn't be a non-blocking, yeah.
**Xabier Martínez** 34:59 Yes.
**Kemal Akkoyun** 35:02 You don't need it.
**Dario Castañé** 35:03 and… Ignore it.
**Kemal Akkoyun** 35:06 Yeah, you can change that in the roadmap issue if you need.
**Dario Castañé** 35:12 gets to be… perfectly… Yeah. Clear on… on the… on the issue, yeah.
**Kemal Akkoyun** 35:23 Yes.
**Dario Castañé** 35:24 Okay, don't… Support projects using bundling… I think Azar was working on this as well? Yeah.
Yeah, but I saw a SARS.
Feedback.
**Kemal Akkoyun** 35:43 Okay, maybe we should assign this to Azar, if it's okay?
**Azhar Momin** 35:49 Yeah, I left some real comments, but I think I will take over if they don't respond.
**Kemal Akkoyun** 35:55 Yeah, first try to, like, not, like, ping them again. I think he's, like, responsive enough, but, like, remind him that, like, we are blocked, like, we are waiting for this.
And then, like, if he's not available, he can take it over.
**Xabier Martínez** 36:11 Also, I think Diya has some context about this rendering.
So, it will be good to have, his feedback on here. I think it's… So that's good.
**Kemal Akkoyun** 36:24 You can assign… you can assign Dario to both of them, like, not to… we don't want to discourage him.
this issue…
**Dario Castañé** 36:34 Okay.
**Kemal Akkoyun** 36:35 Yeah.
**Dario Castañé** 36:41 No problem.
**Kemal Akkoyun** 36:44 you…
**Dario Castañé** 36:46 You're welcome.
I'm on GitHub.
Don't fail on me.
Other risk-rating version metrics test to verify supported branches, Wakar is also taking care of the website. That's something I started.
He took over.
**Kemal Akkoyun** 37:22 Okay.
**Dario Castañé** 37:23 I mean, I asked him to take over because he was willing to, and more viable to work on this.
**Kemal Akkoyun** 37:31 Nope.
**Xabier Martínez** 37:32 Yeah, I approve this beer.
Yes, if someone else wants to take a look.
Mmm… And if not, we can't merge it.
**Dario Castañé** 37:44 Okay, I can do… a last pass.
I'm going to…
**Xabier Martínez** 37:50 Thank you.
**Dario Castañé** 37:50 It sells.
You're welcome. So, this one can be matched to the, probably, speaking of the website…
**Kemal Akkoyun** 38:01 Yeah.
**Dario Castañé** 38:07 You're ready.
**Kemal Akkoyun** 38:07 He's working on it, and maybe you can follow up on this, Dario?
Since you're already on it.
**Dario Castañé** 38:15 He left a comment here, but I think he dropped the comment.
because he was asking something, but I think he already decided how to… how to… approach, no.
the creation of the website. It should be simple, but I didn't have enough time.
this week, so I will follow up with him. Actually, we have the meeting assistant here taking notes for him, so he's going to probably know about it.
**Kemal Akkoyun** 38:47 Awesome.
**Dario Castañé** 38:47 Let's hold the next button.
Computation fine-tuning, intervals in External Source Schema Guides…
**Kemal Akkoyun** 38:54 This is mostly documentation work.
I can do this.
It's already on there.
**Dario Castañé** 39:00 sign.
**Kemal Akkoyun** 39:01 See, yeah.
**Dario Castañé** 39:01 Yeah.
**Kemal Akkoyun** 39:02 I will do this.
**Dario Castañé** 39:04 Okay, this one is already assigned to me. I will also take care of it today.
Building projects with older gRPC versions and instrumentation dependencies causes build failures. Assigned to Azar.
**Azhar Momin** 39:21 Yeah, it will be sold with hotel pins, so I will send a PRO today.
**Kemal Akkoyun** 39:28 Awesome.
**Dario Castañé** 39:32 Okay, so we can skip this one.
Visible WiFi.
**Kemal Akkoyun** 39:38 Yeah, I think this one is closed, but I don't know if the… Aditya, if you… if they are, like, responsive?
I remember pinging.
**Xabier Martínez** 39:48 Yeah, I just revised and added, like, changes.
So if you can review it, we can merge it. I just, make the CI pass.
And apply your suggestion to this PR, so…
**Dario Castañé** 40:02 Okay.
**Xabier Martínez** 40:03 would be fine.
**Kemal Akkoyun** 40:05 You just wait for the reviews, then.
**Dario Castañé** 40:07 Right? Yes.
**Kemal Akkoyun** 40:09 Okay.
**Dario Castañé** 40:10 Okay.
**Kemal Akkoyun** 40:10 I will do that.
**Dario Castañé** 40:14 Or I can assign… Kamal and I for… for reviews.
Also, yes.
Person that has been pushing this one.
Okay, myself, don't come out, so…
**Xabier Martínez** 40:32 I mean, I haven't been pushing, like, I just tried to unlock it.
But yeah, you can assign this.
**Dario Castañé** 40:39 Yeah, just so that we can easily find what we.
**Xabier Martínez** 40:43 Yes, surely.
**Dario Castañé** 40:43 on GitHub. That's the thing.
Okay, and here we can keep at it, yeah.
Just waiting for reviews now.
Remote interaction support, hotel… Toll go fight to bulk.
I think this one is the last one to review today, and it had a PR. Okay, there is another PR.
**Azhar Momin** 41:12 Yes, it's rough, but I'll just do another look, and I'll mark it ready.
**Dario Castañé** 41:21 Okay, okay, this is…
**Kemal Akkoyun** 41:24 This is a big one.
Yeah. Can you also assign me as a reviewer?
**Dario Castañé** 41:30 Okay.
**Xabier Martínez** 41:31 they are also assigned to all, like, I think that, once this is ready, we can just… Try to push this one. Try to pull the reviews.
I think it's an important one.
So we can put effort on this one.
**Dario Castañé** 41:49 Okay.
Perfect.
Then, I think we have covered all the bases. We… Have everything assigned.
So… We can go and complete the work before releasing P1.
**Kemal Akkoyun** 42:06 Yes! They are closer than we think, I think. We can do this.
Maybe tomorrow. Come on.
**Dario Castañé** 42:16 I don't know.
**Kemal Akkoyun** 42:19 Yeah, we need… this is V1, like, maybe we should also… I don't know, we don't have an issue, but, like… We have the integration tests and everything, like, smoke tests, we can, like, rely on our testing infrastructure and CI, but, like, let's make sure that, like, things doesn't break and it works as expected, because we will call this V1. Yes, we can always patch, but yeah, it's V1. It's supposed to be stable.
**Dario Castañé** 42:48 Yep.
**Xabier Martínez** 42:48 Have you tried to use, with some of your services already?
**Kemal Akkoyun** 42:56 Not yet. We are, like, we plan to do a full migration this quarter, so we will be converting all our, like, tooling, from Orchestral to this, this quarter. But yeah, it's… It's a lot of work, that's why, like, I don't think it will be ready for V1. If we discover something, we will fix it, but we don't anticipate big, like, API changes.
Yeah, V1 is okay, I think.
**Xabier Martínez** 43:26 Okay.
**Kemal Akkoyun** 43:28 But maybe for Alibaba, this is easier to achieve.
I don't know if you tried, I've been converting the long suit services to OTLC, since, like, the hook injection is the most stable.
And maybe it will be easier for you to convert all those files to the new one with the help of an AI agent one, not before the V1.
**Haibin Zhang** 43:54 Yeah, yes.
**Kemal Akkoyun** 43:57 Maybe you can try that? What do you think?
**Haibin Zhang** 43:59 Okay, I would, I would do that.
**Kemal Akkoyun** 44:03 Awesome, awesome, thank you so much. And if you, like, because if you do discover something while you are converting all those instrumentation, that… that's definitely a red flag for us before releasing this.
**Xabier Martínez** 44:16 Yeah, also we can start with the POC, like, you don't need to migrate all, but yes, try to test it with a couple of them and see how it works.
**Kemal Akkoyun** 44:25 Christmas.
**Xabier Martínez** 44:25 Julian have said, we have tests.
But, you know, sometimes maybe the, I don't know, like, the compilation time or other things with real services.
Will be slightly different from what we expected with the tests.
Just to see if everything works fine, I don't know.
some real bug test. Always would.
**Kemal Akkoyun** 44:49 I suggested to convert them all, because they all use, like, trampolines, right? So they're technically the same thing. So, for… with an AI agent, this should be super easy to… okay, this is the old longsuit YAML format.
And this is the new one, just rewrite everything, and, like, run the testers, like, see how everything works.
like, it's a little bit difficult for orchestrian, because we need different joint points, like, it's… it's a mixed bag. That's… that's… That's why I haven't attempted to do this yet, but we will do this.
**Xabier Martínez** 45:28 Yeah, I mean, if that works, in theory, it should work. That would be amazing.
At least for a launch rate, like… Too much value there, so…
**Kemal Akkoyun** 45:45 Also, like, another value would be… like, Azar already created a, thing for registry to discover all this instrumentation.
**Xabier Martínez** 46:00 Huh.
**Kemal Akkoyun** 46:00 But if we already convert all the long-set ones, which is very way more integrations than what we support, and if we can register them to the OpenTelemetry registry.
For compile time already.
I mean, for day… from day one, people can go and, like, make Their applications already instrumented.
Right?
That would be also, like, a… another VIN.
For us.
**Xabier Martínez** 46:33 there's too much value. I mean, once we have all that instrumentation.
You add a lot of value, like, you can instrument almost every… every service, so… I don't know if, hyping you can create, an issue.
Just for tracking, this of.
**Haibin Zhang** 46:51 Okay, okay.
**Xabier Martínez** 46:52 That's me.
**Kemal Akkoyun** 46:54 I mean, like, how many, integrations? I'm, like, checking the long suit rules now.
**Haibin Zhang** 47:01 About… About 30 or 40.
**Kemal Akkoyun** 47:06 Yeah, that's totally unfortunate. Like, some of them we already have, but, like, if from… if day one, if we can claim that we have already, like, 30 plus integrations, that would be amazing for the blog post.
**Haibin Zhang** 47:21 Yeah, okay.
**Kemal Akkoyun** 47:28 Awesome. Thank you. Thanks, Abin, for taking care of that.
**Dario Castañé** 47:45 I think… Now, we are in an even better position.
2.
That'd be one.
Any last-minute suggestion, idea, discussion that we should… Do you know?
**Haibin Zhang** 48:08 Okay.
**Kemal Akkoyun** 48:12 Nothing on my side.
**Dario Castañé** 48:17 Okay?
Then… I think we can just wrap up here.
Thank you for your time, Anne.
See you next week, I guess.
**Xabier Martínez** 48:33 Yes, thank you so much.
See you.
**Dario Castañé** 48:36 Okay.
Bye-bye.
cycle.
Bye-bye. Yes.
**Xabier Martínez** 48:40 Alright.
**Azhar Momin** 48:41 Right, no.
