SIG: LLM Semantic Convention WG
Date: 2026-03-16
Duration: 25 minutes
============================================================

## Zoom Recording Transcript

**Sergey Sergeev** 01:50 Hey, folks.
**aditya (cisco/splunk)** 01:57 Yeah, you're the race.
**Sergey Sergeev** 02:10 Yeah, let's see how many people are joining, if we have any topics.
Maybe we can take this time back.
Hey, Victor.
Looks like it's a bunch of Tiscanians here and you. Do you have any topic right now?
**Victor Lu** 03:29 Yeah, last week, I invited NAC and joined a co-sign meeting.
So it was good. It was actually good, I think we had a… discussion about next steps, so I think it was agreed that we are going to Basically, at least in that meeting, agree that, we're gonna map to, MITRE Defend ontology.
So it will be, On the open telemetry side, it will be, some… Telep… Matrix for, AI security-related metrics.
And then also mapped to OCSF, which will be an analytical matrix.
So… At this point, the people who did the mapping from DFAN to OCSF, they do have experience.
How to map it to, OpenTelemetry is yet to be discussed.
**Sergey Sergeev** 04:38 What meeting is it, by the way? Is it something, or…
**Victor Lu** 04:44 It's a COSI, Coalition for Secure AI.
So let's, I don't know who… Hmm… WHCK the website.
**Sergey Sergeev** 05:00 this?
**Victor Lu** 05:04 Yeah, yeah.
Yeah, so in here, there is, sub-working group called, work, it's under Workstream.
2 for telemetry.
So, yeah, that's where the discussion… Is right now.
Not open telemetry, just telemetry.
**Sergey Sergeev** 05:37 Yeah, interlink, so, people who read it, Can…
**Victor Lu** 05:43 Yeah.
**Sergey Sergeev** 05:44 Get some context.
**Victor Lu** 05:46 So, yeah.
**Sergey Sergeev** 05:49 Yeah, if you can, if you can add here some link, what was the meeting, and what was the outcome, so I think it will help a lot.
**Victor Lu** 05:59 Oh, let me see, Yeah, can you post a link to this? I know it's in the meeting, yeah.
**Sergey Sergeev** 06:15 Okay.
**Victor Lu** 06:18 Yeah, so this will enable a lot of use cases. Actually, you know what, I know Nag is not here, but just some question. Originally, I participated in this, from, perspective, SPDX, build material, where we are building, ontologies to, For AI security. So we've worked very closely with MITRE, on a lot of this thing. So, just curious, when it comes to OpenTelemetry, how is… How is, supply chain information integrated?
I'll give you an example. I know that's, that's too, too, ambiguous. Let's say, so, we have a, like, Kubernetes cluster, right? So, we, we, we run… we set up the cluster, and we run, we start capture, OpenTelemetry matrix, then, but at that point, we don't know what's running on there, right? So we don't know, like, what version of a Linux operating system is running it, and we don't know what library is running on it, so we don't know… what kind of a security vulnerability, could be there, right? So, how do you… How do you define, Like, based on what components are actually running on the cluster, what matrix to capture.
**Sergey Sergeev** 07:55 The metrics, yeah, I'm not sure about the standards here. Again, it's, we, we, this group is mostly focusing on.
generative AI, so for supply chain, and basically how you capture all the dependencies and etc.
Yeah, good… good question, maybe.
Maybe the Tuesday group can help more, so it's borders, somebody like Ludmiwa probably knows, more security… more SIGs.
Work on it.
**Victor Lu** 08:42 Maybe make it more, more, agentic AI-specific, right? So, let's say, we have a, Kubernetes cluster running again, and then We… but because of the… on the cluster, we could be running, different agent frameworks.
such as, you know, there's so many different frameworks, suddenly it just escaped my mind. Let's say, so different frameworks have different, supply chain vulnerabilities. So, how do you decide, which, matrix to capture, which is more relevant?
to that particular framework, agentic framework.
And then the corresponding, I guess, vulnerability monitoring.
**Sergey Sergeev** 09:36 Have I captured the topic right? Basically, agent frameworks and supply chain vulnerabilities tracking?
**Victor Lu** 09:48 Yeah, basically, when we say an agentic telemetry, there's so many different agentic frameworks.
But there are also so many agentic protocols, right? It can be MCP, A2A, those are the existing popular one, but there are many coming.
So, if we capture everything, that would be a lot. That's probably not practical, right? So… how to, if someone, if an organization installed a Kubernetes cluster and want to monitor, not only the cluster itself, but also what's running on there, how do you decide what component exist.
In… that's running in the containers in that… on that cluster.
**Sergey Sergeev** 10:40 Yeah, I'm not sure about it, anybody… has a perspective on it. I think it's something that I see him, and other areas. Yeah, I think it's better if you can join tomorrow meeting, so I think it may be more people on Tuesday with Brother Rich.
In OpenTelemith specifically, and different standards. I think it's more in the security, inventory, No, to me, it doesn't look GenAI-specific.
So, I would, search, maybe… What seem, standards we have.
**Victor Lu** 11:49 Actually, there was actually a… in COSI, was there actually… there was a Cisco contribution? I think this is the one.
It's cool. This one.
**Sergey Sergeev** 12:00 Yeah, if you can, yeah, congruent…
**Victor Lu** 12:06 Yeah, I think this is a Cisco contribution.
So this is not for that working group. This is for a different workstream. The idea is to… For Agentic AI to kind of, make sure the code generated, satisfied many of the security requirements.
So… Yeah, so, so, so, so, this is different.
So that which… the reason I bring it up is, I mean, Cisco is active, COSI participant.
**Sergey Sergeev** 12:41 Yeah, yeah, it will really help if you can, link, if you take, also something like notes we do here, so if you can, provide the links here, so we don't search… It will be really helpful, and if you… Yeah, if you can post the links, To what specifically this group, proposed or contributed. Again, Maybe we can learn a little bit more in detail without, searching too much.
**Victor Lu** 13:20 Yeah, yeah, we'll do it.
**Sergey Sergeev** 13:21 what are the standards and what are the discussions, but, I think it's all good topics. I… I think, overall, just inventory of MCP tools, versioning.
And authentication. There is also a group, Cisco Outshift.
**Victor Lu** 13:46 Yeah. Alright.
**Sergey Sergeev** 13:47 And, they have a project, Agency?
**Victor Lu** 13:55 Yeah, I know that, working through, I'm a journalist, I'm not expert, I'm just going everywhere and…
**Sergey Sergeev** 14:02 I mean, in general, they, try to define, What is the inventory of different tools and agents, and.
**Victor Lu** 14:12 and convinced.
**Sergey Sergeev** 14:12 This will be a hot topic, in terms of, so agent, identity and agent discovery might be… Quite hot topics, and on your interest, for sure.
**Victor Lu** 14:30 Yeah.
When it comes to OpenTelemetry, yeah, I think the… at least next, that he's, from my first time, he's gonna join, by the way, I think… I don't know how it works for the company, I'm independent, so I don't have the… You know, the membership problem, at least when I've joined. So for Cisco, since Cisco is involved, I know Cisco is also a member, so if any of you want to join the meeting there, it should be, similar, to be able to join the discussion there in COSI.
**Sergey Sergeev** 15:04 Yeah, the hardest problem is to define what exactly is the problem we need to solve. So, again, an open telemet is a little bit, how to say, not necessarily Russian to approach, To adopt, some of, newer concepts, so… It will be helpful how to define those in generic terms.
Yeah, if you can provide some links right to this document after the call, basically to the links of the discussion topics and etc, I think it will be really, really helpful.
For the group to understand this problem domain.
**Victor Lu** 15:52 Yeah, I put it…
**Sergey Sergeev** 15:53 Near two of many people.
**Victor Lu** 15:55 Yeah, I put it in here, the discussion. I put it in the, In the COSI document. The actual COSI document, I'm not sure, is a reasonable… You may need to join before you can access the document.
So, yeah, I can, I can put it in the, in the OpenTelemetry.
Document as well.
Yeah, so, so if you look at OCFF, OCSF is a good example.
so, OCSF, is already mapping to, defense.
So they, they're more for analytics.
Who they're, like, columnar formats.
So, and whereas OpenTelemetry is more, how to say for… for… my description may not be correct. I think it's more, like, wrong then.
Rather than… back in.
So, yeah, so that… what I… yeah, what I just… it looks like you already put in the notes, yeah, so that's the… what's… what is being discussed in, co-site meeting.
**Sergey Sergeev** 17:14 Oh, that's great.
Yeah, I'll try to review it, asynchronously, but, yeah, if you can keep, just posting some related to Gen AI, His summaries, and, to work with, Nagumar, on proposal related to security. So, Aditya here on the call, he also worked with Cisco AI defense team.
Just to define the security lens, I… I think we can continue this collaboration on the security front.
I think the same team, works on secure app.
SecureUp basically, maintains, that supply chain and, dependency information captured as logs. I don't know… if there are some standards for it, but I think it would be great to define. Not sure if it's GenAI-specific, or just broader.
More generic concepts applicable to any application.
I would definitely pass the message to, Cisco defense team.
**Victor Lu** 18:43 Yeah, yeah, the main, the main idea is there's a lot of a different, supply chain firm effort. However, most, effort are either what we call one-dimensional. It means that, you know, you have an AI bomb, then you have an S-bomb, you have a hardware bomb, each build material, kind of a separate chain.
But the problem for that is, The, it's, it's, you, you won't be able to, analyze it to multidimensional, supply chain, like data, model, supply… they're all kind of interrelated. And, also the, the, the, it's not, how to say, first of all, the SPX is ISO standard. So… so this is, one, standard that's going to be adopted, very widely. Second is, it's an ontology, meaning, when different company adopt the same, adopt SPDX, the… the terminology used will be, same.
So, similar to why OCSF is adopting MITRE defend ontology.
The, the, so when you analyze, data, using, the OCSF, using LRM. LRM will be to read all the files from different companies the same way, because the term used the same way, rather than differently. Otherwise, let's say, if you let everybody innovate on themselves, which is good, however, it creates a problem.
So, for example, what is an actor, right? So, if RRM read, okay, this is an actor.
In the security domain, usually the actor could mean a threat actor, right? It could be a threat actor.
For a movie director, when he reads an actor, that's an actor playing in a movie.
So, so those kind… that's why having an accurate ontology, not only taxonomy, but ontology, that's universally accepted, is very important.
And, yeah.
**Sergey Sergeev** 21:04 So it's more focused on data access by different, AI components, or AI agents, or…
**Victor Lu** 21:11 It, it, it is, airflow.
to… the end result is LRN will be able to, do a lot of automations. Reading the log file, do thread modeling.
To check whether it meets security requirements, create alerts, say is it compliant or not. All the… it will be, do reasoning, even, on top of it, find out, you know, what kind of problem it is. All that can be enabled, through that process. Have you heard a company called Palantir?
**Sergey Sergeev** 21:47 Yeah, sure.
**Victor Lu** 21:48 Okay, so that's the same idea. Palantir… the reason for Palantir's success in, you know, many fields is sticking to a standard ontology, although it's their own company ontology, whereas MITRE Defend and SPDX are international standard ontology.
**Sergey Sergeev** 22:11 Sorry, I need to step out, for a minute or two, if anybody… Yeah, let's, see, do we have any… sorry, Victor, to cut you short here, so I just wanted to make sure if we have any other… Third bits… To discuss.
**Victor Lu** 22:40 shared another link about, why security typically fail. It's because, thinking in graph.
**Sergey Sergeev** 22:53 Yeah, my ask for this, yeah, if you could, identify, basically, those AI-specific use cases, Which we can review as part of this group.
So it will be a really, really helpful, for the group, or… if you… Yeah, I'm trying to make it actionable for this group, specifically, again, I'll, I'll share it with, the Cisco teams for AI defense and etc.
And please, add more information if you think, we can identify, GenAI-specific, Standards.
Slack channel may be really helpful.
And, I hope you can, update, that security proposal from Vivnagumar.
I'll ask Kim, to summarize his reading, from.
**Victor Lu** 24:13 Yeah.
**Sergey Sergeev** 24:14 Those proposals, maybe… Yeah.
**Victor Lu** 24:18 Yeah, I think Ned will have… because he has a much better grasp on what's being done in OpenTelemetry, and if there's anything new in those, in COSI and SPDX, we'll definitely come back here and, For, make proposals.
**Sergey Sergeev** 24:35 Okay, sounds good. I just wanted to make sure, If anybody else has anything for this group.
If not, we can probably wrap up, this call 5 minutes early.
I mostly need to step out, for 2 minutes, but if we don't have any urgent topics, maybe… We can wrap it up.
Again.
Thank you, everybody there.
Please keep us posted, Victor. Have a good one.
**Victor Lu** 25:22 You too.
