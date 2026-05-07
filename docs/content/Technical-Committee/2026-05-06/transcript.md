SIG: Technical Committee
Date: 2026-05-06
Duration: 62 minutes
Zoom Recording URL: https://zoom.us/rec/share/BCsa-wp-5uO76FWupub6tQ2l_HdSEqbUFPOqIR0N94xJ2ZI11tF_ufr_8rxitmgo.74PgwTEw4zlqdG4e
============================================================

## Zoom Recording Transcript

**Reiley** 00:24 Hey, good morning, Cigaret.
**Tigran Najaryan** 00:30 Hey, Riley.
**Reiley** 00:40 Okay, so while we're waiting, let me take a look at the inbox. TCSpec inbox, empty.
The community inbox has one item.
Another one item seemed to be a… I just put the link.
In the… Agenda dog.
It's updating a link, okay.
**Tigran Najaryan** 01:38 Looks like the fix is already there, there seems to be the.
**Reiley** 01:41 Yeah.
Yeah.
And the fix is already merged.
**jmacdonald** 02:02 Good morning.
I just closed eyes.
**Reiley** 02:06 Okay, I… Josh.
So, we were just, like, looking at the TC inbox.
**Tigran Najaryan** 02:12 Morning.
**Reiley** 02:23 Hey, Chuck.
**Jack Berg** 02:26 Hello.
**Reiley** 02:31 I think the mail is, the on-call this week.
Hey, Lamila.
Okay, so we just look at the TC inbox, there's one duplicated PR just closed.
I think it's time to… look at the unassigned spec PRs.
**Liudmila Molkova** 04:08 It's my turn. It's my turn to pause the call. I didn't realize that, sorry.
Cool. We are looking at unassigned PRs.
**Jack Berg** 04:35 There's a link at the top of the notes that, that, you know, finds this.
**Liudmila Molkova** 04:40 Alright, thank you.
So there are four… We… let's open them up. I assume we don't look at draft PRs?
**Jack Berg** 04:54 Yep.
**Reiley** 04:56 We don't look at the old tab.
**Liudmila Molkova** 05:00 Sometimes, I think we do, but okay, implementation status of EdLink and Ruby.
I don't think it needs any assignment, it just needs somebody to merge.
**Jack Berg** 05:15 Yep.
**Liudmila Molkova** 05:20 Okay, I believe OpenTelemetry UR is the right thing.
**Reiley** 05:26 Yeah, I think we're ready to merge.
**Liudmila Molkova** 05:29 Yeah.
And… done.
Define identity scope.
**Jack Berg** 05:39 This is, Josh Gereth's, entities related.
**Liudmila Molkova** 05:44 Right, should we just assign it to Josh, then? And he'll pick it up once he comes back.
Oh, great.
**Jack Berg** 06:00 So I think that's it.
**Liudmila Molkova** 06:03 We don't see other attempts here, though. Why is that?
We have a Cygnus forever.
**Jack Berg** 06:14 Yeah, we've been bad at, at following this assignee You know, rules consistently.
**Liudmila Molkova** 06:21 Okay.
**Reiley** 06:22 It can be assigned, but doesn't have to be assigned. I think that's our utilization.
**Liudmila Molkova** 06:29 Right, is anybody in the GC interested in this one?
**Reiley** 06:35 I am.
You can put my name there.
**Liudmila Molkova** 06:38 Okay.
Awesome.
**Jack Berg** 06:46 So while we're in triage, I added a quick item, which is I'm taking a more active stance on closing and following up with PRs that don't follow the process that we have laid out. You know, when somebody opens a PR that, you know, does not have a triaged issue associated with it.
And they just kind of jump into an implementation. Like, this one was a good example, like, after a bunch of back and forth.
You know, what this person is actually asking for is a new feature where views and the attribute key filtering in views intersects with the attribute advisory parameter in such a way that a user can, like.
express only the attributes that they want to opt into, rather than needing to enumerate all of the attributes that they want present on the ultimate metric. And, you know, after a lot of back and forth, we arrived on that, but I'm like, hey, there's no issue associated with this. The PR title and description don't describe this.
you know, you gotta go back, you gotta go open an issue, and we can go from there. So, I encourage other people to do the same on this, and, you know, if we get some things wrong, we can correct ourselves, but, better to, better to follow a process and be wrong some of the time than just let a bunch of noise waste our time.
**Carlos Alberto Cortez** 08:09 Yeah, support.
**Jack Berg** 08:13 And, you know, I don't have the bandwidth to do this right away, but also our process is sort of poorly documented.
And so if anyone wants to take a crack at, you know, updating our contributing.md to reflect the reality of what we do, that'd be good as well, but I can't do that right this moment.
**Reiley** 08:35 I believe we have that. I've closed multiple PRs and providing the link, letting people know what's the process. I can find the link there.
It's just like, like, we're doing this inconsistently, because sometimes it requires Like, some, like, personal judgment.
**Jack Berg** 08:52 Exactly. And, like, one of the things I referred to recently is, like, hey, don't open a PR until you have an issue that has been accepted. We have this set of issue labels, like triage, accepted ready, triage, accepted ready with sponsor, and we don't talk about those labels in our contributing.md.
So, you know, it's sort of an informal, practice.
**Reiley** 09:14 Yeah, so as the meta is showing, like, we… we do have this section, you see, like, we want people to have the issue, and the issue needs to be triaged and approved before they send the PR.
**Jack Berg** 09:26 Do we talk about what the definition of approved is, and what the definition of triage is? Because I don't think it actually reflects…
**Reiley** 09:33 In the… in the flow, and I… I think we also explained the tags.
**Jack Berg** 09:39 I don't think we explained the tags.
**Liudmila Molkova** 09:41 But I couldn't find the tags, yeah.
Well… if… I think, Jack, you have this process documented somewhere in the Google Docs. If you, I don't know, feed it to AI and tell… tell it to find gaps and cover them, it could do a pretty decent job.
**Jack Berg** 10:03 Yeah, so I guess, like, I can do that if folks are open to it. I don't want to kind of fight against the currents, right? But if people… if other people agree that our contributing.md is out of date and could use a sort of spring cleaning, I'm willing to do it, but I don't just want to… I don't just want that PR to open and not receive any attention.
**Reiley** 10:25 I'm supportive, so if you have a PR, I'll review and approve.
**Jack Berg** 10:29 Okay.
I'll take a crack at them, then.
**Liudmila Molkova** 10:33 Well, our current guidance is enough to scary someone contributing trivial documentation fixes so that they need to clarify if they need to create an issue. I think we should make it scary for substantial PRs and easy for trivial ones.
**Jack Berg** 10:52 Yep.
**Liudmila Molkova** 10:58 Cool. So… Moving on to the agenda, Riley, Security Advisories.
**Reiley** 11:05 Okay, so the first thing is, last time we talked about it's hard to fund maintainer slacks, I sent a PR, and that got merged, so it covered all the TC member, GC member, and the SPAC sponsors.
And then, I think we still have a long list of, like, SIG maintainers, which I don't have enough bandwidth to do that. And also, I won't do it once, because the maintainers will change. I need someone to handle that, and I think GC is in the right spot, because they maintain the community.
So… my plan, like, I already got that merged, GC seems to be supportive. I'm gonna ask them to collect the maintainer slack and maintain it somewhere.
Sounds good.
Okay, then, give maintainers proper access. So, I have a PR that clarified the security, accountability, and responsibility, and that got merged as well. And now, I think while we're talking about responsibility, we've got to give the maintainers the power and the tools so they can do the job.
And the current issue, I think Jack pointed out, which I haven't realized, is for maintainers to be able to publish a security advisory, they need certain permission, and there are only four ways they can get the permission. Two of them are the org-level access, like org-level owner or something. Obviously, we don't want to do that.
So, on the repo level, I think the only… viable thing is to make them the repo owner. So currently, the maintainers, by default, they have the maintainer, role, they don't have the owner role.
And… and we have some process there saying if you need a short-term, like, maintenance or something, this is a process. You send a PR on the admin repo, then as long as other maintainers from the same repo, they approve that.
the PR gotmerged and not mentioned will give you the owner rights, so that means, like, you can shift-delete the repository that you're a maintainer for.
So, I want to change the wording there by saying this is not just for short-term maintenance. If you need some, like, security advisory work there, this is the recommended way for you to get access.
And… and they can… they can solve this, like, among the maintainers for sake. They don't need any GC or TC involvement there, and it's tracked, so it's very clear there's a peer review. Jack?
**Jack Berg** 13:30 Two quick corrections. It's the admin role within a repository, not owner, but it's no matter.
**Reiley** 13:38 So basically, the highest level that gives you the power to shift, delete, or repo.
But not the org level, where you can shift delete all the repositories. That's not what we want, because we don't want a Java maintainer to know the security problem from .NET, because they don't have to know.
**Jack Berg** 13:55 Correct. And then the other small thing is it's worse than just publishing, not being able to publish a CVE without this permission. You can't even accept the advisory.
Yeah. And you can't add collaborators, you can't request a private fork, so you can't effectively do anything on the advisory except for comment on it without this, elevated permission.
Yep.
**Reiley** 14:20 So I have a proposal how to fix this, already talked to the security stake folks, and I give heads up to Trask, because trying to reuse a mechanism that he helped to establish, and he's… he's fine with this.
So if… if, like, we're fine from the TC perspective, I'll… I'll make some updates, then next week I'll go to the SPAC meeting and give maintainers a heads up.
**Liudmila Molkova** 14:48 I'm pretty sure I've seen maintainers this week creating Private forks accepting advisories.
Is it because they already have some exceptional permissions, or…
**Armin (Dynatrace)** 15:01 Yeah, some tools, for example, in chess,
**Liudmila Molkova** 15:04 Right.
**Armin (Dynatrace)** 15:05 the collector, they don't. About creating the fork, I don't know, maybe that works without admin permissions, but that's, like, a very minor step. The whole other stuff needs intervention.
**Jack Berg** 15:18 I confirmed that you can't create a private fork without admin, so it's…
**Armin (Dynatrace)** 15:22 Oh, it's up.
**Jack Berg** 15:22 unfortunate.
**Armin (Dynatrace)** 15:24 Alright.
**jmacdonald** 15:25 We had talked about using, a bot to do some of this. Is there a way we could give a bot permission to, like, create a fork on every advisory, we had talked about wanting to, like, open a Slack channel as well to get the code owners involved in this, but that's a sort of secondary issue. Just wondering…
**Reiley** 15:44 Yeah, sure. I think automation will be the next step. We first want to make sure folks have the right access. Then, if we can automate that, great.
But automation is not a blogger for this, I think.
Okay, so there are two things, seems like we agree. The first one is the Slack, I'll leverage GC, and we'll clarify the expectation. For example, the maintainer who's handling security advisory should be available on Slack with some, like, Reasonable, response time.
And then… We gave them the power, they can shift delete the repo, and they should be able to handle all the security advisories with that power.
**Jack Berg** 16:30 Yeah, so I agree with all this. I just want to make sure everybody's kind of listening to the details of this. So, by elevating people from maintain role to admin role of their repositories, they are able to you know, control things that they weren't able to control. Most notably, we've been using Terraform to manage things like branch protection rules and other standard repository setup across the organization. And, you know, as an admin, you can just kind of go around that and do whatever you want. You have carte blanche. And so, like, we're extending the trust in the maintainers, and it's necessary.
So, those are the two things.
**Reiley** 17:13 Yeah, and if you look at the link, the permission change, we have some document explaining, like, when do you need this admin role, and how do you apply for it. I'm going to make the update there, like, that's the very bottom of the doc.
So I'm going to make some update there, letting people know, before you ask for this power, you got to know what does it mean, and these are the things you shouldn't do. Like, you don't want to misuse the power.
Including, like, just changing the configuration directly without going through the admin repository.
**Jack Berg** 17:45 Right, and be cautious about who you bring on as maintainer. You should already be cautious, but you should be more so cautious, because, you know, everybody that has this admin permission, because I think it's going to be assigned to the team, not to the individual.
And so, because of that, everybody that's a maintainer of the repo will have the ability to, you know, delete the repo and cause a lot of damage.
**Reiley** 18:07 Yeah, and they have to pay attention to their… to their permission and account management. They don't want to run some random cloud bot and destroy everything.
Yep. Okay, yeah.
**Liudmila Molkova** 18:22 I think it's time-sensitive.
And also information sensitive.
Yeah. This looks like an issue in the community article, looks like a very… potentially very long.
Way to get access.
**Jack Berg** 18:40 Are you saying we should accelerate it and, like, grant it proactively?
**Liudmila Molkova** 18:45 I'm saying that maybe, the maintainers could reach out to admin, admin, subtle admins to… on Slack to get it faster, especially if it's sensitive.
**Armin (Dynatrace)** 19:00 They can also create the PR in the admin repo right away, and just send them the link that's, like, doing it.
**Reiley** 19:08 Yeah, the beauty of this is if you have two maintainers of the repo, one maintainer can make the ask, the other maintainer can approve, they don't need admin or, like, trust or me to help, they can just… as long as the SIG maintainers agree with themselves, that's done. So we require at least one peer review from the same repo maintainers.
**Jack Berg** 19:28 And Riley, who has merge permissions to that admin repo? So, like, you know, Maintainer 1 opens the PR, maintainer 2 approves it, who.
**Reiley** 19:38 And they converge that.
**Jack Berg** 19:39 They can merge it, okay.
**Reiley** 19:40 Right.
**Liudmila Molkova** 19:44 Cool, so then, should we change this to create a pull request and get the second approver?
**Reiley** 19:49 I'll make the update. I think the purpose of this discussion is I want to explain the direction where I'm trying to head towards and get buy-in from this group. And if we agree, I think I have enough feedback from you guys to work out the details.
**Liudmila Molkova** 20:11 Oh, cute.
**Jack Berg** 20:12 Thanks for following up with this, Riley.
**Liudmila Molkova** 20:14 Thank you, Mom.
Love you!
Thank you.
And the security best practices.
**Reiley** 20:24 Okay, so another security topic, I saw a PR. It's really great. I think the author has a lot of background in this area, and seems he's from Cisco.
And I talked to him. He's mainly working on this for the Blueprint project, because there are many customers reaching out, saying, I'm running this legacy system, and you're… like, built for OpenTelemetry recommendation won't work for me, so how do I do this for legacy systems? So he started, and I approved this PR at some point.
Then, he made additional changes, make this, like, a, like, very official best practice or recommendation. So my question here is.
I personally don't feel blog post is the right place. I think blog posts can talk about, hey, this is a very challenging area, and this is the, like, some of the points that you should think about, and it should link to a document, and my reason here is We can publish a best practice, but things could change, and we need to react to those changes. So, blog post is not designed for us to go back and make the update.
So I tend to… like, I mean, the content is really awesome, but I just don't think the blog post is the right place.
And I want to get some feedback here before I push against the current approach.
So I want the content to live somewhere in the doc, maybe it takes security or whatever doc. And then in this document, we generate this awareness and excitement so we let people know, like, this… Legacy environment is complex, and you should think about it, and these are the problems you can think about, but we don't position it as the best practice, and we link to the best practice stock.
**Tigran Najaryan** 22:19 Is this the best practice, though, or it's an opinion of a person?
**Reiley** 22:25 Oh, okay, so if… yeah, so if you look at the PR, you see the conversation history, like, initially I approved because, If you just go to the… the… The last comment.
Just go through the conversation. The last comment there.
Yeah, so… I initially said it was good, it's reading awareness, but the document is not suggesting best practices, because the title wasn't saying that. And then the author changed the title.
You saw the change after that, right, one hour ago, right after my comment. The author changed the title, and now… now it is the best prices.
**Tigran Najaryan** 23:08 Yeah, I mean, it's… it's… it's author's opinion, right? Anyway, so… What I'm saying, the litmus test for me, whether something should be a blog post or be part of I don't know, the official documentation is whether it's one person's opinion, or it's the official position of the open telemetry. Right. In this case, if we're assuming this person has the experience, but it's just their opinion, it's fine if they make a blog post there, right? So, we may… I mean, if the wording suggests in some way this is official, we can adjust the wording, but…
**Reiley** 23:46 Right.
**Tigran Najaryan** 23:47 it's okay for them to say, I think this is a good practice, right? It's good to do this thing.
**Reiley** 23:53 Not today.
**Tigran Najaryan** 23:53 I think we've opened telemetry.
**Reiley** 23:55 Yeah, so my position is wearing my security sick leader hat here. I want to make sure we give people the right content, the useful content. But here, my bar is, if it's just, like.
My personal experience, or something that I just want to raise awareness, I'm fully supportive. If the position is this is the OpenTelemetry community official recommendation from the security perspective, I have a lot of doubts.
**Tigran Najaryan** 24:21 Yeah, yeah.
Is it suggesting that? Is it… is it… for someone who's reading that, can be… can it be confused?
to be the official position of open telemetry? I think that's the question to ask you.
**Reiley** 24:35 Right. Yeah, and this is why, after seeing the title change, I… I changed my…
**Tigran Najaryan** 24:40 What's the title says? Applying OpenTelementary Security Practices in Legacy Environments. That's what I'm seeing.
**Reiley** 24:47 Yeah.
**Tigran Najaryan** 24:48 Since the new cycle.
It doesn't seem to suggest anything. It says applying open telemetry security practices I don't know, seems fine to me.
**Reiley** 25:00 Yeah, so it's… I'm a little bit on the fence. Jack.
**Jack Berg** 25:04 I'm with both of you, just discourage any language that suggests that it's the official position, but also, like, you know, maybe we can encourage this person to engage with the security SIG, and say, hey, this is okay content, strip it of anything that suggests that it's the official position, and consider opening a corresponding PR in the SIG security.
And, you know, codifying this and having a conversation to make this part of the formal recommendation.
**Reiley** 25:34 Yeah, I tried that last week.
**Jack Berg** 25:36 Okay.
**Liudmila Molkova** 25:40 earned by.
**Reiley** 25:41 And I got low.
**Jack Berg** 25:43 You got, you gotta know? What?
They just don't have time, or are they, like, are they opposed to doing it?
**Reiley** 25:50 No, he has limited bandwidth, and he has a tight schedule, he would want to focus on the Blueprint product, but I'll try again. I mean, like, there's a bar I want to make sure, like, we hold people accountable.
**Liudmila Molkova** 26:06 Oh, so you've gotten now on participation in sick security, not on, scoping this down to a… Practice.
**Reiley** 26:15 So, it's a very reasonable position, I think. It's just like.
like, not exactly what I would wish, but… but I… I mean, that's totally fine.
Initially, I thought, this is a great thing, maybe I can recruit a sick security member, so it's not a Microsoft shop, then I got no. Then, I think after discussion, I was trying to steer towards, hey, maybe, like, we… we put some of this thing under the security guidance document.
And then blog posts can link to that, so that part we're still discussing.
Okay, so I… I think I have some good feedback from you. Thank you.
**Tigran Najaryan** 26:57 So I guess, if the person doesn't want to participate in sick security, that's fine. If you're still seeing some wording that you… you think can be confusing to people who read this? It's fine to… I guess, suggest some changes to… To make it clear that this is an opinion of a person, and then we should be good, right?
**Reiley** 27:19 Yeah.
**Armin (Dynatrace)** 27:20 It's the official hotel block after all, and not the private one, so it's fine if…
**Tigran Najaryan** 27:25 I get it, but yeah, the official blog post, I think that's a question that probably we should be asking as well. Do we allow opinions there, or is it just for official announcements?
I think I saw… Things there that aren't necessarily what you could call an official position in the past.
**Reiley** 27:45 Yeah, I agree with Tigran. I don't think we're using blog posts to give people security best practice.
The official one should be the spec, or the security guideline, or whatever, like, we put, you know, very formal Repository, have peer review.
**Tigran Najaryan** 28:01 Or the documentation, right? We have the actual documentation pages.
So, blog posts, I think, for me, the bar is lower there. It's a person, they are publishing something interesting for OpenTelemetry community, it's an opinion in my… that's how I'm seeing blog posts.
**Reiley** 28:19 Yep.
**Liudmila Molkova** 28:20 And this is effectively a case study of them doing something, right?
**Tigran Najaryan** 28:24 The case studies is the perfect example. Yeah, exactly, yes, yeah.
**Liudmila Molkova** 28:32 Cool.
So, I also want to talk about Stability by default, but before that.
I am going to change jobs again. This is my… tomorrow is my last day at Grafana.
I'm starting at Google in two and a half weeks. It will trigger some changes in the TC. I think Josh has some ideas about it, but we… I don't know what's going to happen. I… I… I could step down at this point, we will see.
yay to me, but I don't know. We'll still see each other for the next couple of weeks, at least.
**Tigran Najaryan** 29:16 We're ending up with 3 people from Google, I see. I got confused for a moment.
Sometimes… con… Congrats!
Is what we should be saying, at the very least.
**Liudmila Molkova** 29:33 Thank you.
**Carlos Alberto Cortez** 29:34 They'll be like, you know that this is public, right? Just triple checking.
**jmacdonald** 29:37 Yeah.
**Liudmila Molkova** 29:40 I'm in, yeah.
It will become public anyway, sorry.
at least I passed my background check already. Okay.
**Reiley** 29:56 I need something really quick. I think we're probably at the right time to talk about identifying new potential, like, TC candidates.
**Liudmila Molkova** 30:08 Should we jump into the private channel?
**Reiley** 30:11 No, no, just, like, quickly mention that, because I want all of you to think about it, and maybe, like, next couple weeks, we should have a more, like, formal discussion in the private channel.
**Carlos Alberto Cortez** 30:22 We had a document regarding potential, new members, yeah.
So we need to just look for that, resurrect that, update that.
**Reiley** 30:32 Yep.
**Liudmila Molkova** 30:38 Cool, okay, so I… since we're late on the agenda.
We had some additional discussions about stability by default in the SPAC channel.
And I want to make sure we are fine with, de-scoping the original ATAP, or the direction we discussed in the spec call. So the recap is, so maybe I'll just pull it up so we don't forget anything.
See, this is rotary… Talked about.
if I… understand correctly what Had is suggesting.
That, essentially, this OTAP either becomes a vision OTAP, or we even kill it completely and scope it down to just the the Contribo, management story.
I… think there are parts in this OTAB that would be… Missed with this?
Specifically… the contrary… well, it's just the part of the story. The part the devil means is what should be the distribution, but I think it can come later.
I'm curious how people feel about de-scoping the RTAP, and is it too small?
**Carlos Alberto Cortez** 32:27 By the way, if I understood correctly, I think that he said he was going to close it and open a new one.
**Liudmila Molkova** 32:38 I think you wanted to rewrite it, and call it a graduation criteria.
**Tigran Najaryan** 32:54 I think it's fine. He wants to read it, right? So, I think we should wait to see… As a leader, what he wants to propose there.
Do we need to do anything until then?
**Carlos Alberto Cortez** 33:10 I don't know, maybe… What I could do is ask him to… you know, provide a draft whenever he has one, review that, in case anybody in DC wants to really help and provide, free feedback.
Other than that, I think we can just wait.
**Liudmila Molkova** 33:29 Yeah, waiting is also fine.
**Carlos Alberto Cortez** 33:33 But, Mila, probably there's something in your head, about this, and probably, you already have some opinions.
It could be great to pass that from now, even without any draft or anything.
**Liudmila Molkova** 33:47 Yeah, I… I will, I will… if there is any draft, I will definitely comment on this, but I think, what we discussed in the past, that, We need some form of a vision of where we're going as a project, and this could be our vision if we're just limiting it to the… country management. This is a separate story. It's still a good one.
**Jack Berg** 34:17 I don't mind this as a vision.
When I look at these work streams, they're not… There's 6 of them, and each of them on their own, you know, are pretty daunting-looking.
And… I don't think they're all equally important.
From a user perspective.
and I don't think they're all equally pressing.
You know, we talk about performance benchmarks and security standards, like, I don't expect people to… I don't expect there to be consistent performance benchmarking for every component in the ecosystem.
Benchmarking takes a lot of work to set up and tune.
applied times thousands of components, because that's how many distinct instrumentations and SDKs and exporters and receivers and processors we have. It's unrealistic, and we don't even have the resources to run those on dedicated hardware. So, like.
that's… I think that's like a pie-in-the-sky idea. Security standards, we say we lack, you know, commitments around CVE response timelines. I think that's wrong.
Like, I think that SIG security does lay out these practices, and, you know, we just gotta get better about sort of socializing them and doing the things that we've been doing recently to make maintainers aware of their responsibilities and actually do the things.
The most important thing in here to me is this distribution definition.
Is, like, hey, we need to have… distributions from OpenTelemetry that Where a distribution is, like, you know, for a particular language, bundles together a bunch of components and instrumentations, and has You know, a reliable release schedule, where they can make breaking changes on some sort of cadence, where there's expectations about which components are used from a stability standpoint by default, and how you opt into the experimental ones.
And, you know, a similar thing for the collector, but the collector's sort of… it's its own beast.
And… I get the feeling that the daunting scope of this, and the fact that, like.
you know, some of the sentiment I'm expressing, like performance benchmarking and security standards, like, skepticism in here, is probably driving the fact that, like, this hasn't been able to go anywhere.
And so, like, I agree with all these things in principle, I just, like… I don't know, imp… putting them on the… putting them as, like, checkboxes that we have to do in order to graduate, it… I don't want to do that. I think it's, like, it's all aspirational.
And we shouldn't hold ourselves to this in order to graduate.
And we… probably shouldn't hold these, like, you know, all equal to each other. I don't think all of these work streams are on an equal footing.
**Liudmila Molkova** 37:30 Is it fair to say that we don't envision there is, at least we don't have any energy for changing any of it?
Comparing to what we have already.
We already have some standards around this, and probably… Yeah.
**Reiley** 37:47 I feel that's a little bit scary position, and here's my take. I think when you look at CNCF projects, many of them, they're more like a self-contained thing that you can deploy. Well, open telemetry is different. OpenTelemetry is, like.
It's a reusable thing that you can install, and it might run as part of your process address space, or it might run on your machine.
That means, like, the security bar might be different.
So, I… I feel like OpenTelemetry is probably the… the number one project under CNCF umbrella that requires the highest level of security.
bar.
like, if we're not secure, then anything using OpenTelemetry, they have security problem. We don't have, like, SLA, then how would other open source components, depending on OpenTelemetry, have I SLA? How would the vendors build ISLA?
**Jack Berg** 38:47 I don't disagree with that, Riley, but, like, OpenTelemetry has this scope that is an order of magnitude or two bigger than other, other projects, because it has this open charter. It wants to do everything.
It wants to be a protocol, it wants to have semantic conventions, it wants to have a collector with, like, a contrib model, it wants to have instrumentations, it wants to have language implementations with a contrib model where anybody can contribute anything. Like, how do you… how do you make security guarantees at a high bar for that… with that, you know, breadth of scope?
And, you know, I think you just have to, like, you can't hold everything to the same standard. You have to rely on federation, and, like, where in different groups, we'll have… Be at different points in the maturity model.
**Reiley** 39:37 Oh, yeah, that part I agree. So I feel like we need to be clear, at least we need to give certain transparency. We're saying this is the aspiration, and each SIGH should be very clear about their security posture.
And we have a general guidance and process, but we don't try to, like, like, shut down a particular work stream just because they don't meet certain high aspirational standard we have. Like, we're not trying to do that. But the SIG maintainer should be very clear where they are, and they need to let their users know.
The same for performance. Like, just let people know what they're using, instead of making it appear as if, like, everything is just performant and secure, then later.
Tell the user, sorry, we're not going to be accountable, there's no expectation.
**Jack Berg** 40:34 Yeah.
**Reiley** 40:36 And even thinking about the graduation conversation, I think we're not looking for, like, graduating everything at the same time, right? We decided we're going to pick a couple, like, core repositories, and we're not talking about moving OpenTelemetry Swift to graduation very soon. And there's the other side of the voice, do we really want to graduate?
And… like, I… I haven't seen clear answer for that.
**Jack Berg** 41:07 I mean, it's not like, just on the graduation thing, it's not like if we graduate with a reduced scope initially, that we're gonna come back later and say, hey, we want to do a second phase graduation with SWIFT. Like, once the project is graduated, it's graduated.
It's not like…
**Liudmila Molkova** 41:22 As a whole, right? Not individual components.
**Jack Berg** 41:25 Exactly. It's not going to go at that level of granularity. And so, we'll say that our graduation criteria doesn't include all of the scope of the project, but, you know, it'll be a one-time event.
**Reiley** 41:36 Yep.
**Liudmila Molkova** 41:43 Sorry, I want to return to my question. We already have some… Criterias for stability, and we already have the Standards around, benchmarking requirements for, for performance, The aspirational goals here are pretty much the same as we have documented today. They don't create anything new.
**Jack Berg** 42:10 Yeah, it's just like drawing attention to them, right? Like, it's with the SIG practice, the security practices as well. Maybe they could be refined over time, maybe they could be made better, but there are best practices and expectations of maintainers today. And so, it's like socialization and actually embodying the practices that we've written down already.
What does that mean? Like, you know, so if we've already written down these things, and we just want to do better at doing the things that we've written down.
What does it mean to have an OTAP that talks about that?
what does it mean to merge an OTEP that should… that talks about that? Like, what's… what's actionable?
Like, if I want to champion that, if I say, I want to champion performance benchmarking, what do I do?
**Reiley** 42:57 I agree with Jack, and I left a comment on that old tab. My question was, like, if people don't do this, what are you going to do? And I got zero answers. Then my position is, I'm not going to spend more time on this PR, because if I don't get the answer, if people don't do the job, what are we going to do? Then it's just, like, wasting time.
So we already have all the things, it's just, like, we're not making the consistent execution.
And depending on the SIG, I think the situation is different.
I have a question. Do you think the TC is in the right position to to enforce certain maintainers to do the job. For example, we'll say, if the maintainers are not doing this job, then you'll be moved to somewhere else, like, not a maintainer. Like, we'll revoke the maintainer access for you.
do you think that the TC is in a position to clarify or define such process, or make such execution, or it should be the GC accountability?
**Liudmila Molkova** 44:05 It's true.
**Armin (Dynatrace)** 44:07 to me.
**Reiley** 44:09 Sorry?
**Armin (Dynatrace)** 44:11 Okay.
**Liudmila Molkova** 44:12 Hi, Carmen.
**Armin (Dynatrace)** 44:13 Yeah, to me, that sounds like governance, like, the definition of governance, right?
**Reiley** 44:19 Yeah, so I'm on the fence. I kind of feel this is more like GC accountability. This is how the community works, this is governance. TC will not be the bad cops. TC will… will provide technical aspects. But on the other side, I can see the argument the GC might be saying, the TC is accountable for security, and the TC can delegate to seek security, but if there's a security problem, and nobody is accountable, if the GC is trying to hold someone accountable, that'll… that'll be the TC.
So for the… let's take one example. If OpenTelemetry Java has a big performance regression, and we did some investigation, we noticed the Java maintainers, they don't follow any of the best practices, they just don't care about performance, then should the TC try to enforce it, or the GC try to enforce it?
**Jack Berg** 45:10 It's, it's, it's gonna be collaborative, is the practical answer.
**Reiley** 45:15 I agree, it's always the practical answer, but who's ultimately accountable?
If there's lives on…
**Jack Berg** 45:22 Making the personnel decisions, like, you know, I would say that, like, the GC has to take the action on the TC's recommendation.
**Reiley** 45:33 Yeah, I think…
**Jack Berg** 45:34 GC, like, underwrites the technical aspects of the project, and so it's the one that has to say, like, hey, look, like, the JavaSig is not following the best practices that we lay out for benchmarkings, and it's putting our, you know, our users and our reputation on the line. GC, you need to act. And then the GC takes that recommendation and does something about the maintainers.
**Reiley** 45:56 Okay.
Yeah, and from my personal experience, I've never seen that action being taken. I've seen many cases where the community members are not following the code of conduct, where the TC, like, the TC raised awareness, the GC chimed in, and they sort it out.
But I've never seen a case… a single case, I've never seen that in the history, that we see some performance issue or security issue, and we read this to the GC, and the TC, like, the GC took the action.
Like, it never happened, at least from my observation. So, I feel like if that's something we want to, like, we believe and want to try, maybe, like, we'll take one concrete case and just practice the muscle.
**Jack Berg** 46:43 Hugren, we can.
**Tigran Najaryan** 46:43 I agree.
**Jack Berg** 46:43 I see your.
**Tigran Najaryan** 46:45 I just hope we don't choose a person randomly, Riley.
Sorry, bad joke.
**Reiley** 46:52 Yeah, I agree with you.
**Tigran Najaryan** 46:53 the muscle.
**Reiley** 46:54 It's a very tough situation, but if we… we never got started, then it'll never be done, I think.
**Tigran Najaryan** 47:01 No, I think, yeah, I agree with what was said. The TC can recommend that a person is not performing the duties that they are supposed to do as a maintainer, the GC can make a call on that. I don't remember if we ever had a situation like that, not officially at least. Maybe there were cases, but if you know of a situation, we certainly can do that, and we can Also, codified, if necessary, in the community guidelines.
So, if there is a person you have in your mind, we can do that in the next TCGC call.
**Reiley** 47:41 I don't.
I'm just stating my observation that if we don't have any of this, like, execution, then we'll just keep talking, then I guess we'll not get, like, we'll never get where we want to be.
We'll just be, like, nice people talking about things, and then things will just work… keep working as previous.
**Tigran Najaryan** 48:03 Riley, but it's… it has always been about soft power in open telemetry.
**Reiley** 48:08 Yeah.
**Tigran Najaryan** 48:09 We, we, we almost preferred… to… to avoid, I guess, unnecessary confrontation, and use the soft power, and… See if we can convince people and collaborate.
this approach has been quite successful. I don't see a need to change it drastically.
There certainly may be cases where it doesn't work, and you do need to take an action.
If your question is, I guess you're feeling that it sort of is… Pointless to go and define guidelines on security if we don't have a way to enforce them.
That's what you're feeling. I think that's fair, and we can say that no, we do have a way to enforce them. We never needed to have an enforcement action like that in the past, but if we're feeling that the security guidelines are not being followed.
then we can do something about it. It's not like we're powerless. That is not the case.
if you are feeling that you need our support, the support of TC and the GC to do your job as a lead of Sikh security, you have it unquestionably. You define the standards for security, and if you're seeing they are being violated.
In a significant manner, we can enforce the action there.
**Liudmila Molkova** 49:41 What else?
**Tigran Najaryan** 49:41 I see absolutely no problem in doing that.
**Liudmila Molkova** 49:43 That's the point The cool thing that works is automation, and if you pay attention, Marilla sent a script that tracks maintain our activity. And we can track number of advisories, and in theory, I don't know how we can track the time to response, but at least we can reuse existing GitHub data.
And this makes us not bad cops, but it also eliminates the human factor and understanding if certain SIGs react in time, like, just collectively.
Oh, it's already in our Security Oversight dashboard? Nice.
**Armin (Dynatrace)** 50:27 Yep.
**Liudmila Molkova** 50:28 Yeah, huh?
**Tigran Najaryan** 50:31 So, just to reiterate, it's not… definitely not a wasted effort, Riley, what you're doing. If you define the standards and find that people are not following it, we definitely can do something about it.
Or not without power here.
**Reiley** 50:46 - Yeah.
Understand, that's why I'm still spending energy there.
**Jack Berg** 51:05 What do we do about this OTEP? Let's go back.
**Tigran Najaryan** 51:07 So, about the OTEP, I guess… Ted's idea that we turn this into a graduation criteria.
I think it's fine to talk about the graduation criteria, but in my mind, graduation criteria may include… stability concerns?
But those two things are fundamentally… Independent things to make calls on, in my mind, right?
Do you want to have performance as graduation criteria, that's something to be discussed on. You want to have security definitions as part of graduation criteria, something that's to be discussed on.
I do not think turning this OTEP wholesale into a graduation criteria is the right approach.
And I don't know if Ted even wants to do that, so we may be discussing something that he has no intention of doing. What I would suggest to do is go and Talk to Ted to understand what is his plan.
what he wants to do. If the plan is that he wants to define the graduation criteria, we certainly can work on that.
maybe some of this OTEP informs that graduation criteria, but in my mind, those two things are definitely… In many ways orthogonal.
That's how I'm seeing it.
the stable by default O-Type, I think it… Had a very bloated scope.
And… at least for graduation, it has too many things. I agree with you, Jack. So, Ted wants to work on graduation, I think that's very valuable, he can work on that, and we can take a look at what that graduation criteria includes, independently from this LCAP.
And if… there is no other person who wants to focus on stable by default, then yes, we close the OTED, and TED works on the graduation.
**Liudmila Molkova** 53:22 Thank you for all the thoughts.
Yeah, Josh?
Welcome in.
**Josh Suereth** 53:31 Hey, sorry.
I heard you announce, Ludmila, that you, were switching jobs, so I just wanted to… Oh! Yeah.
I wanted to let everyone know that my intention is to let David and Ludmila step up into the TC, and that if we… due to the corporate policy.
of not having more than, you know, X amount of people from a corporation, that my plan is to step down from the TC. So, I'll do that as soon as Lydmilla joins Google.
Which gives us, I think… I don't remember how many weeks, to get things sorted out, but I still plan to lead and do everything I'm doing now, so it doesn't change any of that.
**Liudmila Molkova** 54:14 I didn't want that to happen, Josh, seriously.
**Reiley** 54:19 Some doctors want to retire and focus on something else, I think.
**Carlos Alberto Cortez** 54:26 Jobs aside, the obligated question is, Josh, are you planning to stay in the loop, working in OpenTelemetry?
**Josh Suereth** 54:33 Yeah, I plan to spend the same amount of time I do now in OpenTelemetry. I just would, spend more time on, like, the independent projects and less time on TC-related things.
**Jack Berg** 54:46 We could use this as an opportunity to revisit some ideas that have been discussed in the past, like decoupling spec maintainership from the TC.
the… you know, there's a lot of people that contribute to the spec that are not TC members, but that do it at a high enough level that I would feel comfortable giving them merge permissions to that.
And, you know, if we want to keep the number of TC members bounded to 10, which we've said in the past.
Then we can extend the set of people that are able to have, like, influence and get things done in the community by having a wider group, potentially, or a different group of people that have elevated permissions in the spec.
So, yeah, just a thought.
**Josh Suereth** 55:51 Sorry, I… I can only speak for a little bit, because I'll start coughing.
I didn't manage to finish all the things I wanted to do with the TC Charter, but yeah, Jack, I did want to finish some of the, you know, maintainers, like, having a specific list of proto-maintainers, spec maintainers, and all that. But I'm sure you guys can sort that out. Like, I would encourage that work to continue.
And I'm happy to help from the outside as well, in the future. So, let me know what I can do to help, and yeah, I agree.
**Jack Berg** 56:28 Yeah, I think… I think if we want to do stuff like that, what's been slowing us down or preventing us is just, like.
We deliberate too much.
We just gotta make a call, and be decisive, and do things, and, accept that we're not gonna be perfect, and that we'll evolve along the way, so, Yeah, I think that's kind of what has slowed us down from, you know, revitalizing or, you know, refreshing the TC Charter, is just, like, we talk about things a lot.
And perfect is the enemy of good.
**Carlos Alberto Cortez** 57:15 By the way, I have some questions regarding escalating capacity for TC members, but we don't have enough time, I will ask offline.
**Liudmila Molkova** 57:28 Okay, sounds good.
So… Thank you all.
**Jack Berg** 57:34 Thank you, Josh, I hope you feel better.
**Tigran Najaryan** 57:37 Coop.
Yeah, bye, everyone.
