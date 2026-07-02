SIG: Technical Committee
Date: 2026-07-01
Duration: 41 minutes
============================================================

## Zoom Recording Transcript

**Reiley** 01:38 Hey, Doug.
**jberg** 01:39 Hey, Riley.
**Reiley** 01:42 Okay, just look at the TC spec inbox, it's empty.
I'm looking at the… Community Box.
**jberg** 01:52 I'll go look at unassigned issues.
**Reiley** 01:55 Yep.
**jmacdonald** 02:20 Good morning.
**Reiley** 02:22 Hey, Josh.
**jberg** 02:25 Good morning.
**Reiley** 02:39 Yeah, we're… we're looking at the… the inbox.
Okay, I updated the meeting notes with the triage result. I think there's only one outstanding PR In the TC community inbox. This is, like, adding networks Monday Convention.
You can track the meeting notes.
**jberg** 03:43 Do you want to talk about that? Do we need to talk about that?
**Reiley** 03:47 I guess maybe… do we have the quorum?
**jberg** 03:52 We do not, so I was just… well, what? I think… We're… we still have 9 members, so, we would need one more.
We're close.
**jmacdonald** 04:08 And Tigran said he would not be here today. Right.
On the topic of… our… Our sensitive topic.
**Reiley** 04:19 Yeah, so I put a placeholder in the… in the meeting house.
Army.
**jberg** 04:33 So we do have Quorum now.
So, I suppose we can jump into this Network Semantic Conventions project proposal. Just some context, this has the TC Inbox label on it. The TC inbox label is added automatically to new project proposals.
This was… this is very fresh. And, I guess what… What I could use a refresher on is… what the expectation is for TC engagement, in terms of, like, the order of operations, when we engage. I know that previously we had issues with, like, slow responses to these types of things, and so we've been trying to fix that type of issue by getting ahead of it.
**Liudmila Molkova** 05:20 So for this one, it's kinda easy. Sorry, I was talking before, but I…
**jberg** 05:24 Oh, sorry.
**Liudmila Molkova** 05:25 microphone. No worries, it was my mistake. So for this one, we had a discussion since semantic conventions, SIG.
And, we have a support from Sieg. I'm going to be an escalating TC member if this comes through, if this is accepted. This is accepted. I still… need to read the proposal in details, because I'm not sure what exactly landed versus what we've been discussing in semantic conventions meetings. The key part here is that Braden, who currently is leading, system semantic conventions, are going to, lead this one as well, and he is experienced with semantic conventions, and he's already leading one of the six, that's why I'm feeling comfortable delegating Leading to him, and being just the escalating sponsor here.
**jberg** 06:20 All right, so one thing I remember hearing about this, and there's some discussion in Slack and on the Spec SIG about this proposal, was it wasn't quite clear whether it was exclusively semantic conventions work, or whether there was some new instrumentation work as well. I'm sure that's somewhere in the details here, but what's your perception of where that landed?
**Liudmila Molkova** 06:40 Yeah, we don't even consider semantic conventions without instrumentations these days. You at least need the prototype, and the people who work on it are interested in EBPF. I think some EBPF folks are participating. The… there are people who work on security.
They don't, they intend it to cover some of their scenarios, but they are not within OTEL. They are vendor-specific.
And, there are… the collector part here is that some of the network metrics are emitted by collector receivers.
So this is, I think, well-grounded into instrumentations, but yeah, I need to reread this proposal and, further details.
**jberg** 07:33 Okay.
So… Does anyone else have any other comments?
If not… in order to move forward with this, do we want to leave it to Lyudmila to review the text more closely and, you know, officially volunteer as TC sponsor in an escalating capacity? And, you know, at that time, remove the TC inbox label?
**Armin (Dynatrace)** 08:07 Good to me.
**jberg** 08:09 Yeah, based on what you said, once we have, you know, you've volunteered as a TC sponsor, once that's, like, in the document, I would approve it. And I guess from an approval standpoint, that's another thing that we've, you know, dealt with in the past, is, like, what does an approval mean? I don't know if we've gotten an official answer there, of, like, when is the appropriate time to approve, and what signal are we sending when we approve?
So maybe we can coordinate in the GCTC channel and essentially just say, like, look, we think that this project should go forward. GC, are you inclined to accept this project? And when everybody feels supportive, we can all give our approvals on the PR.
Alright, I see heads nodding, so that sounds good.
Okay.
Moving on, I added the only agenda item.
And… what was this? This was a request that, that Tyler made to, tag the TC.
So, yeah, this was from a day ago.
And, you know, what's this conversation about? I need to catch up on this whole conversation, but.
**jmacdonald** 09:25 I have some context.
**jberg** 09:26 Please share.
**jmacdonald** 09:27 Yeah, So… the… Go Instrumentation Group has adopted some… like, has a donation from years back that I was a sponsor for, or I reviewed the donation for. So they're generating Go code to facilitate eBPF instrumentation.
And that's just the backstory here. We're moving to a place where, the EVPF profiler is integrated with the collector, and therefore, we're trying to figure out how to build collector using the generated code from the Go artifact… the artifacts that are generated for Go for eBPF.
You can see I don't fully, fully understand this myself.
But what happened was, someone made a proposal in the collector to do a source archive distribution where you'd build the generated code from a release artifact that was, like, pre-computed.
stored as a, like, a Git… like a Shaw release, like, artifact. And, the… and then the collector leads want to do it differently, and it… there's, like, a big disagreement between the Go team and the collector maintainers, and it's such a long thread that it's, like, almost overwhelming. Basically, it's… Go team doesn't want to maintain something, and so has decided not to do something, and the collector can't really see a good, friendly way to build stuff if they don't do it a different way, and there's a little bit of a clash just over methodology, as far as I can see.
That's my best summary.
**David Ashpole** 11:07 I've also been looking into this. Sorry, I'm late. I didn't catch the first bit of this, but I've.
**jmacdonald** 11:13 Oh yes, please.
**David Ashpole** 11:14 To dig into this.
Yeah, I think they're actually distributing the… the built C binaries?
And so there's, like, In some ways, it's not actually… Go code that they're distributing, which is part of what makes this challenging to make work with the Go module proxy.
There are definitely some some challenges with the proxy approach. I don't think… I think there's some issue with Pablo's… Prototype. They're not… they mostly mean that it would be a bit of an operational burden for the OBI maintainers. Like, there are things that can break There's an issue with, like, if you publish something, and then… publish something else, then it breaks everyone, because Go has already computed the… the Shaw from the first thing.
Or if you… If somebody asks for… the go… the static thing that Pablo wrote, I don't think will work, because if somebody asks for it before the artifact is built.
Then they will get a different thing that doesn't have the artifact.
And so, like, there are some race conditions where you can end up with something that can never be used.
it's potentially solvable, it would be a very large operational burden for them, but on the flip side, I do see why the collector is not very interested in becoming a Binary data… like, distribution… Like, having that sort of thing. I… I'm… I'm trying to see if there are ways to… I don't know if we could have either OBI maintain a wrapper around The collector builder that adds their stuff.
Before it gets to the… Pure Go Local Replace portion.
And sort of be a… not a fork, but an extension of the collector builder. Maybe use it as a library or something.
Or… Like, some flavor of that with… Like… being able to rebuild OCB with your own extensions, something like that, so that we can come up with a maintenance story if the isn't.
**jberg** 13:41 Some sort of hook that they could leverage to.
**David Ashpole** 13:45 Braden had proposed just, like, what if we supported generic hooks? Like, here, run this… run this shell script before invoking the collector builder.
And that… that also… would be a workable solution. I'm not sure.
It certainly, like, has fewer guardrails for… OCB, but I think… for OBI, but I think the OBI maintainers would… would take it at this point. They're… They're interested in a solution that gets them a collector, builder.
That produces, the thing that they want.
**Liudmila Molkova** 14:23 It seems like.
**jberg** 14:24 all parties should want a collector builder that gives them the things that they want, right? So, you know, I don't think that the collector maintainers are against including OBI in the collector as an extension, right? And…
**David Ashpole** 14:38 No, no, no, it's that they don't… the… I think the tricky bit is, like.
they don't want a… I think the worry is a bit about, like, how generic it is. Like, yeah, I can go download anything, and as long as it matches a checksum.
Then it becomes… like, they don't want that to be the API that they support in the collector builder. They want something that's… like, more, has more guardrails than, like, download a binary and verify it against a SHA.
**Liudmila Molkova** 15:14 Knave questioned, don't we want or be distributable list collector, or a BPF Profiler Distributable Lisk Collector.
**David Ashpole** 15:24 I think so. I think it's… I think there's… like, it's possible that the collector maintainers once we dig into the issues that running a GoProxy has more, we'll understand better why the OBI maintainers are not Not willing to run that.
Or don't… don't like the risks that it entails.
But I think… I think everybody wants it in principle, but, like, there are definitely… real maintenance burdens on either end that are going to be imposed by whatever solution they come up with, and I think… Right now, everyone is just saying no to things.
to get to… yeah.
**jberg** 16:10 I don't see anybody disagreeing with just, like, the premise that OBI and eBPF Profiler should be, you know, included in the collector and, you know, referenceable in the collector builder.
It's just like, you know, how do we get there? And, like, at what point, should the TC be involved?
And, like, based on this comment from Pablo, I don't think this statement is accurate. We are still discussing different options for this particular issue. Like, so my read on this is, like, Tyler said, like, hey, I think we need to escalate this to the TC, and Pavel's like, we haven't had enough time to fully absorb this and, you know, explore the different ideas. And so, I think from the TC perspective, we let this run its course a little bit longer, and let, sort of, maybe both sides reach the conclusion that they need to escalate to the TC before we engage.
**David Ashpole** 17:04 I… I agree.
**jmacdonald** 17:07 Yeah, there's something that, like, we need a more clear outline explanation for those of us who are not super familiar with this. I, you know, I think we've complained… there have been complaints about the OCB process in the first place. Like, we force you to build everything from source. Why aren't we building this from source to follow the plan, is what I don't quite understand yet. Like, that's my question.
Basically.
But I think it's on them to give us a better technical explanation of the problem.
**jberg** 17:38 So I can leave a comment to that effect.
on this, because I'm also TC on call for this week. You know, Tyler, we heard that you were interested in an escalation. You know, it seems like, from the collector's side, there's still more exploration that can be done, and so why don't we let that play its course? And if, you know, if after that exploration is done, we still are at an impasse, we can get a kind of more thorough technical summary of, you know, what's going on here, and we can escalate it to the TC.
**David Ashpole** 18:12 I did reach out to Tyler, and discuss with him over Slack.
a good bit yesterday, as well. But yeah, I think that would… I think that's the right approach.
**jberg** 18:21 Alright, so I will… I'll take an action item to do that.
And we can put a pin in this.
All right, that's all the… oh, here we go. Riley, you added an item to the agenda. Security at OpenTelemetry email, yeah.
**Reiley** 18:41 So, for folks who, who haven't joined, or maybe, like, you didn't remember, recap. So, security researchers send an email to security atopentelemetry.io.
A little bit more than a week ago, and this is about the… the, like, the released, packages that OpenTelemetry is accountable for. So, there are several concerns, and in general, I think these are good improvements. So, I took one example and reached out to the JavaScript maintainers.
And I told them, like, we'll take some time to absorb all this and figure out a good solution, but meanwhile, there are 3 immediate actions I already discussed with TC, and I want them to take care of, and I'll… I'll quickly mention that. The first thing is for however.
that haven't published any NPM packages, but they're listed as the owner, they have published rights.
I suggest that we have them removed immediately.
Because security, I think one principle is you only have access when you need to.
So folks in general agree. I don't see any strong objection there. The second one is for people who are not the maintainers, I suggest that they should be removed. We will not want to keep maintainers there for now.
And… and this is where I… I learned something interesting. So, the JavaScript SIG is not the only one. Like, people who can publish to the NPM package, you can imagine, are the people who work on the Node.js side, and the web browser side. So, there are multiple SIGs, and they're maintainers.
are all listed as the owner of that NPM package. So this, like, you can imagine, like, people, they only take part of the web browser thing, which is still in progress, nothing, like, reached to stability.
they're also listed as the owner. So, like, I start to see a balance issue. Like, either we can separate them, but from NPM perspective, I also think it kind of makes sense to have open telemetry as a single thing, instead of having, like, three different accounts or something. So, just something I learned.
the last thing I said, I… I told them, like, maybe I gave the recommendations for folks who wear multiple hats, they work for some company, then I, in general, think, like, the company email might have more security, like, guardrail, because they have dedicated IT department things, so they seem encouraged, but we don't have enforcement. I think the first thing is there seemed to be a very strong reaction. I wouldn't expect a lot of people were… we're taking this as we're trying to enforce, and I was like, no, this is not enforced. Then, there are many folks were not convinced. They're saying, I don't see how my company, is doing this more secure, and I worry about if I move to a different company, or I lost my access, like, so there seems to be a lot of hesitation and pushback.
Anyway, so this is more like a suggestion.
we're not enforcing that, so I kind of, like, told them this is, like… like, I still have this suggestion, but… you decide what you want to do, and then the maintainers come back and challenge, like, like, can you explain what's the reason behind the suggestion? So I feel maybe, like, we need to make it more formal, like, if the JavaScript maintainers have this concern, I guess other maintainers would have the question, so it's like.
We had some discussion, but I didn't share the full discussion and the rationality behind that. I was giving them a quick summary, because these are immediate actions.
So I… I feel maybe we… we should have a discussion, So I wonder if folks would be interested in this, like, if we can invite the security researcher… I reach out, and he got back to me very quickly, saying, like, he's willing to work with us, he's willing to join the effort.
And he seems a lot of good points. So, if we can get the security research and the JavaScript and the WebSig maintainers.
in the next TC meeting, or if we cannot make it, we can find a separate, like, breakout session. Just have people, like, discussing about the initial idea, we take this as an example, and then build something on top of it.
Like, would folks be interested? I just feel like… I'm in the… I'm the man in the middle of talking to different groups, and I relate the message, but it'll be great if people have this, like, face-to-face discussion.
**jberg** 23:21 That sounds good to me. I was trying to take some notes as you were talking, and I think I missed one of the points that you were making. Something about a concern when you switch employers.
**Reiley** 23:33 Oh, there are people saying, I've been using my personal account, and in certain environments, for example, in NPM, maybe, like, they ask you to register. Initially, you have to put your email, and you cannot even regret and change your email. Then they worry about, if I stop working for this company.
Of course, we can say, like, NPM might need to make the change.
the reality is, they probably don't support that. So, like, I totally understand those, like, concerns. So, when we said we have this recommendation, people have this strong reaction, because they learned from the past that they actually recommend something else. And you can imagine, like, maybe people working on open source, once you have this particular new guide, I, I, I don't know which exact, like.
repository we're talking about, but maybe the concern is once you register your name and the email, there's no way you can change your email, so you better use your personal thing. It can go with you forever. And that seems like the right recommendation, so they worry about if we gave the recommendation without additional consideration or clarification.
people might just simply take it, and they just relearn the mistakes others have learned before. And that's reasonable.
**jberg** 24:46 So, just to your question, should we, you know, invite all these people to the next TEC meeting so we can get them in the same room and talking face-to-face? That seems like a good idea to me.
**Reiley** 24:56 I would suggest that, but I want to know, like, if folks would like to have that conversation.
I mean, sick security seems a better position, but sick security is essentially just myself, right? So, I want more feedback.
**jberg** 25:13 Yeah, I think if SIG security existed and was robust, they could have that conversation over there, but the TC backstops security. So, while SIG security is, you know, kind of defunct right now, we are effectively SIG security. So, in other words, we have a priority to reboot SIG security.
**jmacdonald** 25:31 Yeah, yeah.
**Reiley** 25:32 Yeah.
And I have a selfish goal, I want to see if that security researcher would be willing to help there.
**jberg** 25:38 Right. Is this unique to MPM? I heard a lot of these examples be given through the context of MPM, yeah.
**Reiley** 25:47 We just picked NPM because the OpenTelemetry NPM packages, they have the highest number of downloads.
And the list of people who have the owner rights is much longer than other, like, projects.
**jberg** 26:02 Yeah, I have the list of people with publishing rights to Maven for the broader Java ecosystem pulled up right now in a different tab, and it has some of the same problems that you just mentioned. There are maintainers from different repos.
So there's the OpenTelemetry Android maintainers, plus OpenTelemetry Java maintainers, plus OpenTelemetry Java Instrumentation. It's a superset of all those.
And some people use personal emails, some people use corporate emails, and there doesn't seem to be… Maybe there's a way to toggle the email address that's associated with you, but I can't find it immediately, or that functionality exists, so yeah, good general advice.
**Armin (Dynatrace)** 26:44 If it's done via Sonotype, it's… it's all very, well, a very low-tech process with sending around emails and asking people to be listed as approved shippers and such, I'm certain it doesn't even allow you to specify that you cannot, publish, the Java SDK if you're an Android maintainer, and vice versa.
Yes. So that… that could use some… Some more… more love from… from those running the system, just as well.
**jberg** 27:22 Okay, so, Riley, do you want to coordinate inviting them to the next TC meeting?
**Reiley** 27:28 Yeah, if there's no strong objection, I'll just, like, reach out, and I'll see what's the right time.
Oh, and by the way, another thing I just learned from the chat, but… some of this, like, like, package publishing destination, already have the OpenTelemetry service account, which is managed by the GC, and seems, like, in some some situation, the maintainers listed as, like, owner, or they have publishing rights, but they cannot remove others. So I'll have to follow up with GC.
And that seems like… so, I got feedback in case, like, someone really got, like, hacked, they're, like, doing evil things, and we have to stop the bleeding.
we don't even have an on-call schedule from GC who can… who can kick… kick that.
Evil publisher out.
We ask, do I have permission? I certainly don't.
**jberg** 28:37 How would… what does permission even look like? Permission is, like, ecosystem-specific, to kick out a…
**Reiley** 28:44 Exactly.
**jberg** 28:45 a rogue publisher, and I don't think… I think probably for most ecosystems, it would come back to official communication from, like, the OpenTelemetry, GC, and TC to whatever powers are, like, sort of managing that package manager.
Like, so, you know, an email from GC and TC to Sonatype for the Java ecosystem, or to, MPM for Node, and so on.
**Reiley** 29:11 The R3 case is, like, one case is the GC already created a service account or something, like a special account. Like, for NPM, we have this NPMGS, something at opentelemetry.io.
So that's managed by the GC. And I… I don't know how the credentials are shared. I guess the credentials are not shared with maintainers. Instead, the CICD job is configured to be able to publish things. And the GC has the credentials, so they can use, like, they can… like, on behalf of that service account, we have the ultimate power to add other, like, individuals or remove the individuals. So that seems like an okay situation, although eventually, I hope that we can remove all the individuals, but there are some technical challenges. Like, people mentioned, if I need to publish the package for the first time.
I must do this in an individual way. There's no such, like, automation or something, maybe, like, just a limitation. So, but… I think the solution is, if you already have the service account created by the GC, and there are some exceptions, you have to keep individuals, that's okay, enough.
And it's good to learn that those individuals don't even have the power to remove the other individuals, or remove the service account created by the GC.
Well… For… for, .NET, if we talk about new guides, like, I haven't been working on that for a while, but my, my previous knowledge is that, We're just adding those individual maintainers there, and there's a goal to have a service account, but the problem is, even if you have a service account, there's still some, like, maintenance job, like deputation, those things.
they can technically build those automations, but it's rare, and nobody wants to spend time on that, so they just, like, feel it's easy, and those maintainers, most of them, like, we'll work on them for years. We have the trust, we're saying, oh, we're not going to waste time there.
And another thing is, even if you have the service account, as long as we keep some individuals there, if they went crazy, like, the account got stolen by a hiker, the hacker, the first thing is, the hiker will just remove everyone else, including the service account.
Then, I imagine the GC would ping me, I'll talk to someone in Microsoft, and because of the trust, someone from Microsoft will just go and restore this for us. And I imagine for Maven, there would be a similar thing.
Yeah, the third situation is we just don't have any service account. All of them are individual, and these things are not widely used, so I know that we have some SIGs like that.
I'm… probably, like, I don't even think we want to spend too much energy there. I think for the first two situations, this already covered the mold, like, the… the highest number of the usage. So I want us to focus on this, and once we establish the pattern, other six can follow.
**jberg** 32:15 That makes sense.
**Armin (Dynatrace)** 32:16 The individual accounts have the benefit that you have an audit log of who shipped what exactly, which you don't have with the service account. It's the same with GitHub users. You also have your individual account, and in the audit log.
**Reiley** 32:30 Yep.
So… so the idea, I'll take down that for example. Like, like, the goal is we don't want to have individual names as the owner of the new guide packages. We should have an open telemetry account.
And then the maintainers, they don't have the password. They cannot just publish on behalf of OpenTelemetry on their machine, and in the end, we don't even know which maintainer published the thing, right? Everyone is just finger-pointing. That's not the case. We want the maintainers to use the official CICD job to do all the package management, so… The… from New Guide's side, everything is coming from OpenTelemetry. They won't be able to track this down.
But from the… the audit log in OpenTelemetry GitHub, we can see who triggered that thing.
**Armin (Dynatrace)** 33:13 And… Huh?
**Reiley** 33:14 And in case of an emergency, someone has to do some manual job, the maintainers can reach out to the admin or the GC, depending on, like, what we end up with, and they will give them the temporary access to the credential, and they can use that, but this is, like, recorded, like, a manual option and operation, and once they finish that, I imagine the credential would be revoked and maybe, like, renewed.
So, it's like a one-time use.
**Liudmila Molkova** 33:46 And this is an ideal picture. We… we might never get there.
In some places, but that's what we are.
Trying to achieve.
**Reiley** 33:55 Yeah.
**Armin (Dynatrace)** 33:59 It also puts some… some burn on things like rotating the API token for publishing from the deployment environment.
At least once a year or something, would then be something that maintainers could no longer do on their own.
**Reiley** 34:17 In that case, it'll be managed by either the GC or the org admin, not the maintainers.
**Armin (Dynatrace)** 34:26 Slick.
Hotel should already get their own IT department, almost.
**Reiley** 34:32 Yeah, sounds like the case.
**Armin (Dynatrace)** 34:34 would also help us in not forgetting to renew our SSL certificates and such.
**Reiley** 34:41 Yep.
**jmacdonald** 34:46 That's called a co-pilot.
**Reiley** 34:54 Yeah, I figure, like, it makes sense to have the conversation and at least have a North Star direction, and depending on the the actual situation, like, if, like, mesos, things are not crazy, we don't see a lot of attacks, maybe, like, like, don't push it too hard, try to, like, solve some immediate problems instead of boiling the ocean, but, like, we need to observe the trend. I think with AI, there's all these, like, crazy things, things might change. So I… at least, like, having… having a direction is important.
Okay, so that covered my topic. Thanks, Laura.
**jmacdonald** 35:36 it seems almost absolutely better to have GitHub Actions publish packages. I think we can all agree.
**Reiley** 35:44 I already see some private chat with the maintainers where they strongly disagree, so…
**jmacdonald** 35:50 Oh, wow.
**Reiley** 35:50 Yeah, so my gut feeling is whatever we discussed, agreed here, we need to have the, like, the awareness that most of us probably don't work on every single project. There are special cases, like the NPM situation I learned.
I didn't know that before.
**jmacdonald** 36:10 Funny, there's a connection between the problem with Go and eBPF here as well, like, that's package publishing, just, like, Google did it weirdly, and now we're facing different problems.
Not weirdly. I think Google Go packaging is great, but, we've got a corner case.
**David Ashpole** 36:25 You just have to stick to GoCode, and then you'.
**jmacdonald** 36:27 Yeah, don't use any foreign codes.
**David Ashpole** 36:30 Seaco.
**Reiley** 36:33 Okay, shall we switch to the private topic?
**jberg** 36:36 Yeah, let's, head over to the private Zoom. See you over there.
**Reiley** 36:40 Okay, thanks, Rana.
