SIG: Technical Committee
Date: 2025-08-20
Duration: 34 minutes
Zoom Recording URL: https://zoom.us/rec/share/wNFRqEjN_lnscSgLl6Yr9suLU6ktVus6PMa-X-1HhqszfzDroyrqZ_QpTXGrtyRo.-D1YPxxrL9quVEeq
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 02:49 Hi, Armin. I too grinch.
**Reiley** 02:51 Congrats.
**Tigran Najaryan** 02:54 Hello.
**Liudmila Molkova** 02:55 I was not sure if you were on.
Okay, it's my turn to run the meeting today. We are very light on the agenda.
And now we'll use this chance to… interrogate Armin about security, things.
… So… It's already 3 minutes past.
Josh, I think, is… On vacation, Jack is not here.
… Carlos… Should be here.
So let's give, maybe… A couple of minutes to join.
So, stupid questions about security. I have to admit, I've… I haven't done anything here.
Carmen did. I don't have access to it.
How do I get it?
**Armin (Dynatrace)** 04:06 I will, add you to the… to the ticket so you can access it.
**Liudmila Molkova** 04:12 Could you also add me to the… this thing?
**Armin (Dynatrace)** 04:21 Which one?
**Liudmila Molkova** 04:23 So, this link for audit logs, if I remember correctly, that dashboard is broken, right? We cannot use it.
But then we use these audit logs.
**Armin (Dynatrace)** 04:37 Yeah, I will add you to that one. I'll send you a ticket, like… Carlos Bright last time.
Maybe we can do it in a… in a… better way in the future, because I don't like the manual aspect of it, but I would just give you the permissions to read the log there, and then when you're done for this week, you would hand it back again.
**Tigran Najaryan** 05:05 Okay. Is that the plan? We'll be doing the, like, temporary granting access to the audit logs, and then… and remove when the week is over? The reason I'm asking next week is my rotation, I think, so….
**Armin (Dynatrace)** 05:18 Yeah, it's the current way of dealing with it that we have. I don't think it's the best way, but it works.
**Tigran Najaryan** 05:26 Okay. Neverly value. Okay, cool.
**Liudmila Molkova** 05:29 Actually, the only reason it works is because you actually go on track of the reactive things. And I've spent 2 plus days without having access Just because I didn't have it.
And I wouldn't know without you.
**Armin (Dynatrace)** 05:47 That's it.
**Liudmila Molkova** 05:48 It doesn't work.
**Armin (Dynatrace)** 05:50 Yeah, that's a good point. For the last two days, there was nothing, today there is something, but I have to manually give you access to it as well, so it's also not… Not great, actually.
**Liudmila Molkova** 06:05 Is it something we should discuss with, GC, maybe? Or to… that… if OTC had access to audit logs, why would it be a problem? Why would it be a security concern if we had this access all the time?
**Armin (Dynatrace)** 06:18 Yeah, I think Trask mentioned that there could be a custom role, but I don't know what the, the state of this is, actually.
**Liudmila Molkova** 06:28 Okay, let me ping, … JC on this, ….
**Tigran Najaryan** 06:35 So this is, currently granted, sort of as a… making… by making the TC members an admin of the org, right? That's how it.
**Armin (Dynatrace)** 06:44 Yes.
**Tigran Najaryan** 06:47 What about the Grafana dashboard?
Is that… do we need that? Do we use that?
**Armin (Dynatrace)** 06:54 We used it in the past until it stopped working, … it allows to view the issue number and the title, and the current status of it, so that's something that can be somewhat more easily shared on a broader base. In order to access it and interact on the ticket, you still need to… to… to gain access to the security advisory itself.
So that's something that, if I got tasked right, a custom role could help us with.
But it provides a good overview. Also, for something that's still open after 1, 2, 3, 4 weeks, you wouldn't necessarily dig it out from the audit log, unless you were specifically browsing through all of them.
It… it would be a better way to see what's… what's been open and in progress.
**Tigran Najaryan** 07:50 But you're saying it's not working right now.
**Armin (Dynatrace)** 07:53 Yeah, I think, the automation was… established by the security Sig at some point, but then somewhat abandoned, then I think that probably… Just some token would need to be… added or re-added, I'm… I'm… I'm not sure.
**Reiley** 08:13 Yeah, and we don't plan to resume that.
The current process is broken, and we want to change the way how we work.
So instead of having… having the security group and the GitHub admins looking at the emails, and then having the TCA look at the privately reported security advisory, and having the maintainers looking at the CVEs, we want to have a consolidated view of the maintainers and hold them accountable.
having TC relaying the message for part of the issue is not working.
And another thing, which is even bigger.
we need to set expectations first. Currently, we have the issue, we do a friendly ping, we tell the maintainers, hey, you got something. But they… they have no idea what's the expectation, like, what's the timeline.
And how should we prioritize? So, I'm trying to clarify this, and hopefully we can fix the process.
… I'm not a big fan of executing a broken process knowing that it won't lead us to success.
So… so my recommendation here is whatever we have today.
let's… let's just, stick with that, knowing that it's not the right way of doing things, and we have to make the change. So, I already got a couple feedback from the GC members, I think, and also, like, Army, I think I got your feedback, I made the update.
… I… I want to get more feedback here, and once I… I think, have got enough feedback.
I'll incorporate the change, and I'll share that in the Tuesday SPAC meeting to all the maintainers.
**Liudmila Molkova** 09:48 Sounds great. So, the process you're suggesting, I suppose, is to fix the access problem, to some extent.
**Reiley** 09:56 So, I want to first align on what we want to achieve.
And once we align on what we want to achieve, then who's going to do it, and how to set up the rotation. I think once we agreed on the goal, there will be a lot of consequence. Like, we need to change the way how we work.
**Liudmila Molkova** 10:17 Okay, I'll take a look. My feeling is that it seems like a long-term project.
In the short term, unless Armin is here and checks things, we… We only rely on our man's responsibility, to check things. Otherwise, it's very, unreliable that the TC member, like me, would detect there is a vulnerability.
So if we are looking for the long-term solution, fine, we should also have some short-term solution to the problem.
**Reiley** 10:54 Yeah, the shelter solution is very simple. If the vulnerability is reported on a repo.
We can't expect the maintainers to do that. We don't need someone from the TC to ping them.
The maintainers already have access to that. It's just, like, they don't know what to do. They just ignored it. Then you need someone from the TC to rally people.
**Liudmila Molkova** 11:15 Okay, so you're saying the process is not broken, unless… at least we hope so.
**Reiley** 11:20 So if they communicate that in the spec, meaning we expect the maintainers to do a frequent check and make sure their repository is up to date. They respond to the security advisory.
That's fine, like, Lumeta, if you look at the semantic convention, which you are the maintainer, you should be able to see the security advisories. Like, do you… Do you think the right way to do it is the maintainers on the semantic convention will just ignore it until someone like Armin or Riley start to ping you?
This is not healthy, right? And what value we're adding here.
But the problem is, if we want to fix that problem, we need to first agree on what's the expectation. Like, we have to tell the maintainer, we expect you to do this. And if you don't do this, then GC will define what's the result. Like, maybe… The result would be we'll have a separate role, we'll have the security response team, or we'll say the maintainers cannot do this job, then you won't be maintainers anymore. So, we have to first agree on how we are going to push for this.
**Liudmila Molkova** 12:26 Okay? Yeah.
**Reiley** 12:27 So, I believe today, the TC role is just, we will do a, like, daily scanning of the issue, and once we notice there's an issue, we'll just reach out to the maintainers and ask them, hey, can you just follow up? And if they don't follow up, we'll just, like, friendly ping them.
So we're not adding a huge value, and also, if you ping them, they come back and say, okay, we understand, but we're busy, we don't have time to work on that. What do you do? You just ignore it, or you just keep pinging them until, like, after a year, you give up. So… So this process is… It's a little bit, like, murky, currently.
**Liudmila Molkova** 13:06 It feels like a safe belt, that if maintainers didn't prioritize it right, then the TC member could definitely Raise the priority and figure out who else, if maintainers are busy or absent, who else could.
**Reiley** 13:21 No, I, I tried.
I tried, I was told, we don't have time.
And then we stopped.
**Tigran Najaryan** 13:31 Was it for something… Serious, an actual critical vulnerability, or something minor.
**Reiley** 13:39 it is a high, high-level, like, CVE. Then the maintainers come back and say, well, we don't use that feature. We don't think we have the issue. Then I'm saying, but you have a problem, because people are using your binary.
they automatically see the CVE, their scanner will see this issue.
And this is high. Like, they won't know. How do you explain to them? If I use Linux, there's a library which has issue. Can I just say, I don't use that library.
I'm not going to patch my system, so we don't have agreement there.
it's very hard to make any progress, because people don't agree on what we need to achieve. So.
I'm trying to fix that agreement problem.
**Tigran Najaryan** 14:20 Yeah, but also, Riley, it's a… it's a… It's a well-known problem in the industry that CVs are sometimes bullshit, right?
**Reiley** 14:30 They aren't.
**Tigran Najaryan** 14:32 they aren't actual problems at the severity level that they are reported in. I know. And so… and so people… it's one of the reasons people ignore them, people who are supposedly responsible for fixing those vulnerabilities.
**Reiley** 14:48 So, the problem lies as much in the….
**Tigran Najaryan** 14:51 I guess, with whoever came up with a system of these vulnerabilities where they don't really reflect the reality of the severity of the problem. So they essentially create work for others by publishing this stuff and creating the pressure on the maintainers, when in reality.
Maintainers may often, in many cases, are the right ones here to ignore that.
So, it's… it's an industry-wide problem. I don't think we can solve it here on….
**Reiley** 15:24 I do think we can solve that.
**Tigran Najaryan** 15:25 no.
**Reiley** 15:25 I would expect, if there's a security vulnerability, like, hi, you as a maintainer, you confirm it's not a problem, then at least you should communicate back, make it clear, and you can public, like, you can make it public.
Just ignoring that, ignoring that, like, you don't even care, you don't give the proper response, that's a problem. That means you didn't even spend time to investigate the problem, and how would you know there's no issue?
**Tigran Najaryan** 15:50 That doesn't fix the problem that you were describing. The scanning tools are going to continue reporting that as a vulnerability.
**Reiley** 15:58 Oh, sure, then we can change the bar, right? We can decide which tool we trust, which CV database we trust. This is something we… the problem is… We don't talk about this.
We just, like, blindly ignore it, and on the other side, we do.
**Tigran Najaryan** 16:12 No, I'm with you on that. Obviously, you can't ignore the reports, but… I think… We should allow some… some level of judgment to be applied by the maintainers when they see it's an actual… not an actual problem.
I… I will… I won't feel myself comfortable going and trying to pressure them on fixing something which is a bullshit report, really.
**Reiley** 16:37 Yeah, so there's a balance. If you can look at the PR, we put consideration.
when we made those changes. So we actually gave people that reasonable balance. We're saying if you have a library that's different, if you have executable, you have different expectations.
So, let's spend time on the PR and find out the balance. I feel, open country, as a community, we need to first agree on What we want to achieve.
**Tigran Najaryan** 17:03 Makes sense, and I think… We probably shouldn't just decide it between ourselves. Let's maybe also seek input from the maintainers.
**Reiley** 17:13 For sure. So, this is the initial run. I want to get feedback from the TC and GC and the security side before I share in the Tuesday meeting. And when I share with the Tuesday meeting, I want to make sure at least Among us, we have the general consensus. Then we're going to get feedback from maintainers, and it will never be perfect. This is an ongoing process. We'll have the initial version, we'll have the maintainers try, give us feedback, then we'll improve.
And the security bar keeps changing, so we have to be prepared for that.
**Tigran Najaryan** 17:42 Okay, okay, good.
**Liudmila Molkova** 17:45 One thing I feel that… If maintainers do a perfect job and react to vulnerabilities, it's still important for the TC members to have access to vulnerabilities.
To know that they happen, regardless whether we need to take action or not. Imagine some vulnerability that affects more than one repo, in some sense.
**Reiley** 18:07 Yeah, not necessarily. We need someone to do that, but that someone needs to be TC, or it can be a security response team, that answer depends on what we decide to do. So, I'm actually open, and if you look at Kubernetes, we have a security response team.
So, I probably need to cover that in my separate topic, so I feel like we should have a security response team, and that team should have all the TC members as the initial members, but over time, if you have someone else saying.
I'm tired of doing this. I still want to be TC, but I don't want to be in this rotation. I think we should give people the opportunity to do that. So having a separate team, but putting all the current TC members seemed like a good initial step. I really try to avoid binding everything, just yielding the TC group.
**Liudmila Molkova** 18:58 Yeah, yeah, yeah, absolutely. So, if there is a group that has access to vulnerabilities, that's not an admin.
Then who… anybody can be in this group.
**Reiley** 19:07 Right.
Trask is aware of this, so let's follow up with him on that.
**Liudmila Molkova** 19:14 Awesome.
**Reiley** 19:14 You know, like, now we have a PR we're discussing, so I'll bring that to the maintainers once we have the initial agreement, and then we'll create a separate group, we'll add the initial TC members, and making sure they have the proper access.
**Liudmila Molkova** 19:28 Okay, wonderful.
Thank you. I'll follow up with Trask and see where we are. Armin, would you… Do the temporary thing, at least this week for me.
**Armin (Dynatrace)** 19:40 Yes?
**Liudmila Molkova** 19:40 Sure. Thank you, I appreciate it.
**Armin (Dynatrace)** 19:43 I already scheduled a message for you on that after the car.
**Liudmila Molkova** 19:46 Yeah, thanks a lot.
Cool. Dan, sorry, Riley, for jumping in front of you on this topic, ….
**Reiley** 19:57 Okay, so….
**Liudmila Molkova** 20:00 They want to talk about this one?
**Reiley** 20:03 Yeah, so before that, I'm curious, because I wasn't driving the TC meeting in the past 2 months, but we never look at the TC inbox. I think we should do that.
**Carlos Alberto Cortez** 20:13 Yeah, there's a new item, and actually I wanted to bring that up.
**Liudmila Molkova** 20:17 Okay.
And there is accurate and efficient approach for calculating a tail record size. Oh, okay.
**Reiley** 20:32 I've been ignoring it, like, for… for a month, or, like, two, maybe.
**Carlos Alberto Cortez** 20:37 Actually, one month, one month ago, the GC… Yeah.
Ask for… yeah, that's the one.
**Tigran Najaryan** 20:43 The inbox was empty for so long, we forgot to check it.
**Carlos Alberto Cortez** 20:48 Yep.
**Reiley** 20:49 Yeah.
**Liudmila Molkova** 20:53 Carlos, do you, … Now, the summary should be just traded.
**Carlos Alberto Cortez** 20:58 Basically, they want to limit how many items you can keep in a log record.
Like, based on their size. The problem is that it's not very efficient.
To try to calculate how many items you can keep there.
Usually, this could be done at the exporter level, but they won't do that at the processor level.
The concern is that this will not be very efficient.
**Tigran Najaryan** 21:26 But this depends on the exporter's format, right?
**Carlos Alberto Cortez** 21:31 It's, it's funny because, yes, in theory, but they are asking here for, in case you want to actually do that based on the, un-serialized, uncompressed versions.
of each word.
**Tigran Najaryan** 21:43 No, I'm saying, I'm saying it… can't be… so in the SDK, at best, you can't calculate the in-memory size.
**Carlos Alberto Cortez** 21:52 Yeah, great.
**Tigran Najaryan** 21:53 The SDK can't know the wire size. How would the SDK know? It depends on the format of the data.
**Carlos Alberto Cortez** 22:00 Yeah, correct, exactly. And that's why they want to do that only in memory, like, just to calculate what the space in memory limits.
**Tigran Najaryan** 22:09 Is this… is this for… okay, so is this about in-memory size?
**Carlos Alberto Cortez** 22:14 Yep.
**Tigran Najaryan** 22:19 And the reason for that is to do what?
**Liudmila Molkova** 22:24 I think… I think they are trying to badge based on the… Size.
So when you reach certain size, then you export.
**Tigran Najaryan** 22:35 But why is it… why do you need the in-memory size for that? So is it a proxy for the… For the batch size on the wire, or what?
**Liudmila Molkova** 22:46 I imagine you don't know the over-the-wire size in the processor.
Yet.
**Tigran Najaryan** 22:54 The batch processor, yes, but the batch processor obviously doesn't know what's the format, so it can't know the wire size. Does it… I'm trying to understand what is the purpose of this. Is it to limit the memory usage by the batch process? What is it, like, what's the goal? What's the actual….
**Reiley** 23:09 layer from the issue, like, it seems the question, what are you trying to achieve? The response is, we want you to do this, but what we really want to understand is what problem they're having, and….
**Liudmila Molkova** 23:23 It seems they are trying to export data.
… To limit the size in the batch processor.
To actually limit over the wire.
Request size limitations.
So they wind up… it doesn't look like they want something in memory. They are forced to use something in memory because they are dealing with the batch processor.
**Tigran Najaryan** 23:51 Right, and that's a valid strategy, right? You use the in-memory size as sort of an approximate proxy for the size that you would see on the wire. It's not going to be perfect, but it will… there will be a correlation, at least, right?
But then, then they say they accurately calculate the size of my… You probably don't need it to be accurate, because it's at best, a proxy, right, for the wire size.
then, I guess, … And it's still unclear to me what the goal here is. Is it to limit the size of the memory usage? What is it? Is it… is it going to be that the batch processor decides that, okay, I now consume too much memory, let's… let me limit the size of the batch based on that?
And, and we have… something like that in the collector already, so there is sort of a prior art for this. Maybe look at that.
**Carlos Alberto Cortez** 24:49 What's the processor? That's not the….
**Tigran Najaryan** 24:52 There's a batch processor in the collector, which can limit based on the size.
And I think that includes the… the actual size, not just the count of the items, if I remember correctly. I may be… I may be, … I may be wrong on this, I will need to take another look.
**Reiley** 25:10 Oh, in Clackart, yeah, I remember, yes. But they're talking about the SDKs.
**Tigran Najaryan** 25:16 I understand. I'm saying that sort of a collector can be a source of inspiration of how this can be done.
**Carlos Alberto Cortez** 25:24 Well, going back to your… Go ahead.
**Reiley** 25:27 I agree with Tigran that, like, I also don't understand what's the concrete problem they're trying to solve, so it seems the issue is just describing, they come and say, hey, give us this, but I don't understand if we gave them whatever they ask for, what are they going to achieve?
**Carlos Alberto Cortez** 25:44 Yeah, that's what I wanted to say. I think we should ask them for details on the motivation for that first thing.
**Liudmila Molkova** 25:51 Isn't this clear? Like, when you're… you want to say, okay, every 5MB, I want exporter to run.
**Reiley** 25:59 But as far as….
**Liudmila Molkova** 26:00 Because 5 megabytes, when you send over the wire, is compressed.
**Reiley** 26:05 So they need uncompromised for what? Maybe they have a service which will uncompromise since they have limited memory. We don't understand that.
**Liudmila Molkova** 26:13 Yeah, so they are… the problem, I think we understand, their solution cannot work.
**Tigran Najaryan** 26:22 Yeah. Yeah, there may be multiple reasons to do this, right? One is to limit the memory size of the SDK itself, like the usage of memory by the SDK. It may be that the destination has limitations, right? It can't process very large batches.
So, and the solutions may look, I guess, different depending on what exactly is the problem we're solving here.
Right. So… I think we really, really need to ask that question and understand what is it, what the goal is, really.
And I also have the question, I think I raised this to the GC, so why would we….
**Reiley** 27:01 Like, take one… One feature request that haven't received many many other support as a priority. I mean, anyone can create a request, but is that a very common scenario we want to solve? Or this is just, like, a low priority thing?
I don't understand.
**Tigran Najaryan** 27:21 Yeah, we don't necessarily take everything for implementation, we just need to triage and decide what do we do about it, right? We can easily put it on some sort of a back burner and say.
until we see enough support for this feature, it's not going to be implemented. And it seems like it's exactly at that phase, right? This is one person, they opened an issue, I don't see any upvotes or anything like that.
**Reiley** 27:45 Yeah, so I'm slightly confused, because I remember the previous conversation with the GCs, if it's a new issue, we should first understand if there's enough demand, and only if there's enough demand we should reach out to the TCNC.
What's the technical solution? Is that a yes or no? And what's the priority? We don't take one ask that nobody else in the world asks for, and ask the TC to give estimation or direction.
**Liudmila Molkova** 28:12 Well, I think according to the current process, we would, say it's a signature, and it's logs.
And we would… assuming we don't understand what the issue is.
And then the log-seq would prioritize it, because it's in active development, actually.
I see. And we probably would put… I don't remember what labels we have here, but, … I think community feedback as the label that assumes it's collecting feedback.
**Reiley** 28:40 Yeah.
**Liudmila Molkova** 28:41 ….
**Reiley** 28:43 then we shouldn't ask TC to handle it. We're still collecting community feedback.
**Tigran Najaryan** 28:50 Yep.
So I think we can comment and say that we'd like to see a better explanation of why this is needed.
And also, we believe that we'd like to see more community feedback and support before we We move forward with the issue.
**Reiley** 29:07 Yeah.
**Carlos Alberto Cortez** 29:08 And anyone goes on, like….
**Reiley** 29:10 Like, this doesn't seem to be only about logs, like, span could have the same issue.
**Tigran Najaryan** 29:15 Exactly, yes.
**Reiley** 29:18 Sorry, Carlos, I keep interrupting you.
**Carlos Alberto Cortez** 29:20 No, no worries. I wanted to say, I wonder to what degree we should actually… also, besides this additional information, we should ask for a prototype. Maybe it's too much to ask.
But if they want to, you know.
Honestly, I think that if they want us to pay attention to this more, a prototype should exist, but that's just my opinion.
**Tigran Najaryan** 29:39 we… we… I think, yes, we can ask for that, but maybe… Maybe only after we actually understand what this is about, right? Otherwise, they may waste a lot of time doing the prototype, and the same question will still remain, why this is needed at all.
**Carlos Alberto Cortez** 29:55 Yeah, okay, yeah, wood straight up.
**Tigran Najaryan** 29:57 they should overcome that hurdle, right? To answer the why question. After that, when we understand that there is good reasons to have this, then we'll think about, okay, but how do you do that? Show us a prototype.
**Carlos Alberto Cortez** 30:10 Makes sense.
**Tigran Najaryan** 30:14 Does anybody want to respond to the issue?
I mean, I can do that if you want.
**Liudmila Molkova** 30:24 Oh, heck, thank you.
**Reiley** 30:26 Thanks, Tune.
Okay, so moving to my topic, … So I have a PR, the idea is really simple. So, so Tigran released this because the profiling sake would want to have their maintainers, sitting on the proto… approvers, so they can have a green checkmark, whatever. So, so instead of… … like, doing… separate groups. I try to use very explicit groups. So here, my proposal is we should have proto-maintainers, approvers, and treadgers.
And I don't plan to change the actual role, so if the TC member already are the maintainers of Prado, I'll just add the TC member as a child group.
under the proper maintainers. So, no… no actual change. And then, if certain folks from ProfilingSeq, they want to be approver, currently they're not, then we'll just follow the normal approver process, asking them to Requires for it, maintainers will discuss.
So in this way, we try to… we try to have dedicated groups for the proto repo instead of tie that to the TC group.
Which allows us to add additional people if the maintainers agree.
That's all this PR is about.
And I, like, if people think that's a good approach, I also plan to create the spike maintainer, spike approver, and spike triage group. And for, like, for all the recalls that we directly put TC and GC, I won't have that separation, so we can… We can add additional people if they want, and the same thing for the security response group.
**Tigran Najaryan** 32:16 And Riley, then the technical committee group becomes part of these groups, is that the plan?
**Reiley** 32:22 So the technical committee is now a member under the proto-maintainers.
So whatever permission we have today, we still remain the power. And later, if the TC agreed, being a TC member doesn't have to be a maintainer of Proudhall, then whoever from the TC decided to step down from Proudhall, we can… we can change the way how it works without having to massively change the groups.
**Tigran Najaryan** 32:49 Yeah, yeah. Essentially, you're saying, let's have, We… let's follow the model that we had for other repositories.
**Reiley** 32:57 Exactly.
**Tigran Najaryan** 32:57 There's a team named after the repository.
**Reiley** 33:02 Yeah.
**Tigran Najaryan** 33:04 Yeah, makes sense to me.
**Reiley** 33:05 Keep all the current axes unchanged.
Until we decided to make the actual change. So… so I… I did this for the Proto Trust, Lex idea, so I… I'm… I'm here to see if anyone has strong objection, otherwise we'll… we'll just merge it, then I'll send, follow-up PRs to… Change the spike repo on other repos.
**Tigran Najaryan** 33:27 to confirm one more time, the effective permissions after this PR is merged, they are not going to change.
**Reiley** 33:34 Remain the same.
**Tigran Najaryan** 33:35 Yeah. Okay.
Sounds good to me.
**Reiley** 33:46 And Tigran, you have the PR on the protocol, so after that, I'll make the comment letting you know that the change is done, and how we can update your PR.
**Tigran Najaryan** 33:57 Yeah, sounds good. And there is a… there's another PR on the… Seek Profiling Repository, we may use just that for now.
Trust Creative One.
**Reiley** 34:09 Okay.
**Tigran Najaryan** 34:11 The very first full request there. Let me post the link, in case you didn't notice it.
This one.
**Reiley** 34:21 Okay, thank you.
**Liudmila Molkova** 34:28 Oh.
Okay.
So it sounds like there are no objections, and we are… Done with our agenda. Any other topics?
**Reiley** 34:48 I think we're good.
Thanks, Laura.
**Tigran Najaryan** 34:52 Yeah, thank you. Talk to you later.
**Reiley** 34:54 Coach. Joe, bye.
**Armin (Dynatrace)** 34:55 Bye-bye.
