SIG: Prometheus WG
Date: 2026-07-17
Duration: 34 minutes
============================================================

## Zoom Recording Transcript

**Arve Knudsen** 01:44 Hello!
**Kevin Landreth** 01:52 Hello.
**krajo Krajcsovits** 02:43 Hey there.
I'm still Oh.
I still have to look at that.
Incident.
We put up something.
Too many times a night's really biting us.
Wow, that's… Anyway, this is recorded, so… I'm not going to say anything.
By the way, but on topic, about the… Design doc, there is design doc.
like… I think the… The idea is is is probably.
A good one to… To make things, like, more clear and better, and… And disconnect.
Job instance from the service name.
Especially since… With entities, there will not be a strong connection anyway.
Entities will carry their own information.
But I'm really worried about the compatibility, backward compatibility.
**Arve Knudsen** 04:15 Yeah, but I think the backwards compatibility will be.
Would be better if… if, job and instance research attributes are namespaced, at least? I mean, that's option B in the design doc.
**krajo Krajcsovits** 04:29 Oh, yeah, yeah, I'm… I'm not… not even talking about that, but just, like, how do you even Define.
Like, because… right now in the in the Pr. At least there's talk about this honor honor labels.
flag, which is fine, but I don't know if that's good enough, because looking at the current specification, it's basically underdefined. So there are cases that are not well-defined. I started this table of just cases.
And there's some cases where the spec is just not deterministic, basically. It doesn't say anything.
**Arve Knudsen** 05:05 Hmm, okay.
**krajo Krajcsovits** 05:06 And then… Implementations did something.
Like, is… I don't know if the owner label will… Honor that.
Or we should just say legacy, like, we should have a label, say, legacy, and then it works how it worked, like, we don't care.
And try to be better.
Anyway, I really hope David turns up.
Oops.
This might be…
**Arve Knudsen** 05:36 Yeah, I I haven't really dug into the use cases myself like.
**krajo Krajcsovits** 05:41 Yeah, it's not really a use case, it's more like, like, scenarios, like, which… labels exist, and which attributes exist, and then how do you deal with it? And, like, there are some cases where It's just not defined in the current spec. The new spec is better in the sense that You know, it's… it talks about what happens if there's a conflict, but the old spec doesn't say And, like… Obviously you had to implement something so like.
The auto collector and, like, the Prometheus receiver, for example, implements something, and… And that's how it is. That's the de.
**Arve Knudsen** 06:43 Yeah, I think I… I have to look at this design doc again next week.
And…
**krajo Krajcsovits** 06:52 Yep.
I think… this is standardization. And and Flashbacks of open metrics.
Discussions come into my mind where.
I think we really have to go into the details, and really have to Narrow it down and cover all the cases.
**Arve Knudsen** 07:11 Yeah, I agree with that.
**krajo Krajcsovits** 07:14 If you're going to change it, then let's do it properly.
**Arve Knudsen** 07:17 Yes, so I think when I have the time to dig into this, I will… have a look at option B first, and try to target an Llm. At all the documented use cases, and then.
**krajo Krajcsovits** 07:34 No.
**Arve Knudsen** 07:35 I guess.
It will probably point out that use cases are missing, I guess. So then.
**krajo Krajcsovits** 07:41 Probably, I started to write this, I was like, oh, this is going to be easy, so I'm just going to do this by hand.
But then… I wrote up the use case, and then I had to use LLM to check what the spec says, and then what the code does. Because, again, some cases the spec just didn't specify, like, what should happen.
And you have to do this for the old spec and the new spec from the PR as well.
To see if there's a breaking change in the middle.
And it's like, that wasn't, you know, indeed in the details.
Let me ping David. I don't know if it's going to turn up. Is it tur.
**Arve Knudsen** 08:23 Doesn't look that way so far.
**krajo Krajcsovits** 08:29 I mean, we can continue offline, would be nice.
**Arve Knudsen** 08:32 I I figured on, you know, after I kind of kind of like tested option B with an Llm.
I I'll consider whether you know I I should submit my my own and Decide, you know, up.
option C.
**krajo Krajcsovits** 08:50 Yep.
**Arve Knudsen** 08:51 So that's, I guess, yeah.
I guess, that's sort of what remind really remains on my side.
regarding the design look.
like, I don't think you should… I don't think you should assume that either of the current options in the dock are are the right one… is the right one, I mean.
**krajo Krajcsovits** 09:18 M.
**Arve Knudsen** 09:19 I think we should have the door, you know, we should have, have an open mind to potentially coming up with a An alter, like an alternate solution.
**krajo Krajcsovits** 09:32 Oh, sorry, Kevin, let me see. I think I put the design doc into the or.
into the… Mids of meeting, but let me double check. Just a sec.
**Kevin Landreth** 09:44 Yeah, it had the link to the notes. I didn't.
you know, I may not have scrolled down enough or something.
No, I just have meeting notes.
And.
Sorry, I hate disrupting y'all.
**krajo Krajcsovits** 10:01 No, you're not distracting, and you're pretty low volume. So I didn't. Oh, maybe I.
**Kevin Landreth** 10:08 It might be me.
Probably some type of auto.
sensitivity.
**krajo Krajcsovits** 10:20 Oh yeah, the design doc is… Okay.
So, we are talking about the first item, discuss this PR, And… I'll link the design doc.
As well.
**Kevin Landreth** 10:33 Okay.
**krajo Krajcsovits** 10:36 This is a design book written by David.
That's cool.
And and like.
the reason why I'm at least like concerned.
Is that this really brings me flashbacks of.
When we… Incorporated, Seemingly, Innocent change from Prometheus.
From a Prometheus release, Prometheus 3.
in in Grafana. I don't know if you know about that, where where promoters change from left close to left open.
Time ranges in, in evaluations.
It literally was just like, how do you find samples? Is the interval closed or left open? And we were like, this is not going to cause a big problem. It's just marginal. And then it really beat us in the ass.
And… And we have plenty of users using OTRP and this kind of spec change.
this is like much more visible. And so we need a migration path like. So I I don't dispute the the aims of this design look. I'm just like very worried about the the impact.
**Arve Knudsen** 11:54 I just wanted to say that I think the risk is higher here because I don't think this will just be about migration. I think, you know, it could be a… potentially… it could, you know, it could… potentially lead to persistent pain, like beyond the migration.
**krajo Krajcsovits** 12:13 Yeah, yeah, yeah, yeah.
And there's also the risk of… if we get this wrong, and then OTEL does something, and the collector does something different than the… than Prometheus, and… Thereby Grafana would do something different because we reuse Prometheus.
And now there's 2 words, and then, you know, even more confusing for people. So This is very, very tricky.
Anyway, I did ping David, but I don't… I… he's offline at this CNCF Slack, and he's not answering.
And Arthur is on vacation until August.
So…
**Arve Knudsen** 13:07 Maybe there's anything Kevin wants to discuss. I don't know if, have you been in this meeting before, Kevin?
**Kevin Landreth** 13:13 Oh, no, this camera.
Hey!
**Arve Knudsen** 13:17 Hello.
**Kevin Landreth** 13:17 This is my first time, joining this. I'm trying to get more into this. I'm trying to get into the OTEL, kind of working groups as well, because it… what I was kind of seeing between and hearing in the discussion is that there doesn't seem to be a liaison in between all the different groups. So it's like, Hey, this new group comes out with any spec, and then You know, the other ones have to react.
So my my overall goal is to kind of Be embedded in all of them, and Keep them aware of each other's design docs if it's relevant.
That's my goal.
So not. I'm not smart enough to contribute, but I'm good enough to.
know when things collide.
**Arve Knudsen** 14:02 It sounds, you know, potentially very helpful.
**krajo Krajcsovits** 14:05 Yeah, I agree.
Yeah, I I tried to go to one more open time commuting.
Which is the entities SIG.
Which is pretty good.
But, like, I don't have to go to a lot of them. There's so many other things. So, yeah.
Sounds… sounds awesome.
**Arve Knudsen** 14:25 So do you have a specific role within the OpenTelemetry landscape, Kevin?
**Kevin Landreth** 14:31 No, I don't have a specific role. My background is an SRE, so telemetry.
is every day. All this Agentic stuff.
You know, OTEL's got this new Gen AI.
Working group that.
I'm trying to get into for products not just at salesforce, but at other companies. They're looking more and more into just how to.
what do they call it? Agentic tracing, which is basically tracing.
**Arve Knudsen** 15:04 Mmh.
**Kevin Landreth** 15:04 But they're also not collecting stats. Like, I don't think they're collecting enough stats around, agents.
and stuff. So kinda wanna so from my perspective, at least at salesforce is to get more embedded and to see what the communities are doing. So that way, anything that we do becomes aligned, and it's not just, hey, Salesforce came up with this new thing, and nobody uses it.
So.
Oh.
That's what I was kind of hired to I'm gonna do.
**Arve Knudsen** 15:35 Cool. Yeah, I think Gary and I have a bit the same problem. Like we invent things, but we don't know, you know, whether anyone will actually be interested in the end.
Yep.
**krajo Krajcsovits** 15:48 By the way.
**Kevin Landreth** 15:49 So…
**krajo Krajcsovits** 15:50 the… You know, so this is advertisement time.
So this is… I'm very, very… No, I am very… like, I am going to advertise something, just to make clear, this is not… that Grafana does have an AI observability solution now, which we are I don't know if it's GA yet, probably soon. It used to be called Sigil.
So when you mentioned, you know, statistics on AI agents, we do have a solution for that.
And, and the other… sorry, sorry, yeah?
**Kevin Landreth** 16:23 No, I was saying very cool.
**krajo Krajcsovits** 16:26 Yeah, and the other thing is that Arva and I are working on.
proposal in Prometheus on adding features that Kind of, Help AIs to do their job and spend less tokens.
That's the native metadata proposal.
We are going around it.
you know, Basically.
let Prometheus store and retrieve more kind of metadata information. That's not strictly the core functionality, the time series, but like adjacent stuff.
**Kevin Landreth** 17:06 Sounds really cool. Public yet.
**krajo Krajcsovits** 17:09 Yeah, it's public.
**Arve Knudsen** 17:10 Okay.
**krajo Krajcsovits** 17:11 The design doc is public. It's, you know… in the requirements gathering phase, but there's a POC as well.
Let me send it to you.
if I can quickly find the link.
**Arve Knudsen** 17:26 It's also supposed to help Prometheus integrate better with OpenTelemetry.
So it's not like, it's not all about the AI, but there's also an intersection there. We think that this integration with OTEL, like.
like more high fidelity storage of resource attributes. For example, that's also going to help AI agents.
**Kevin Landreth** 17:46 Yes.
**krajo Krajcsovits** 17:47 Yep, yep.
**Kevin Landreth** 17:48 Oops, one second.
**krajo Krajcsovits** 17:54 The one time when I don't have it open.
**Arve Knudsen** 17:56 Okay.
**krajo Krajcsovits** 17:57 This is, yeah.
Yeah, I was on call today, so I didn't have time for it, actually.
**Arve Knudsen** 18:06 I was also on call today. It's been quite a busy day.
**krajo Krajcsovits** 18:11 Yeah, yeah.
**Kevin Landreth** 18:12 Yeah, it's like, it's kind of like, yeah, we wanted to work more together, but then there's this thing that's kind of like forcing the integration.
Kris "Cowbert" more alignment between all 3.
of platforms like Grafana.
Prometheus and Otel.
It's kind of like, oh, yeah, we should all kind of do the same thing and that way all our products work together. That's that's what I'm learned so far.
**Arve Knudsen** 18:43 Yeah, that's kind of what we're.
**krajo Krajcsovits** 18:48 Is chat not available in this?
In Zoom, I cannot open the chat window. I'm clicking on it, and then…
**Arve Knudsen** 18:56 I have the chat window open.
**krajo Krajcsovits** 18:59 Okay, can you put in the…
**Arve Knudsen** 19:02 Cool, yeah.
**krajo Krajcsovits** 19:03 Yeah, thank you. Maybe this will work.
You know, this is going to be Linux desktop year for sure, any year now.
Man, Arve, would you mind putting in the link to the design doc?
Into the chat.
You're welcome.
**Arve Knudsen** 19:25 Yeah, I just have to… To find it, find it back. I think, okay, I think I found it.
**krajo Krajcsovits** 19:30 Yes.
**Arve Knudsen** 19:31 Yes, I found it.
**krajo Krajcsovits** 19:33 Okay, good.
**Arve Knudsen** 19:48 Okay, paste it in chat.
**krajo Krajcsovits** 19:50 Thank you.
**Arve Knudsen** 19:51 So, yeah, I hope you find it interesting, Kevin.
**Kevin Landreth** 19:57 It's already interesting. It's just Wow, that's cool that y'all are able to share this. I'm really really happy with this.
**krajo Krajcsovits** 20:06 Yeah, I mean, yeah.
again, advertisement time, but, like, Grafana is really into open source, so we try to do everything upstream as much as we can.
**Kevin Landreth** 20:16 Yeah. I think Salesforce is getting we're we're trying to move more in that direction. There have been some initiatives, but I think for something as important as this.
This whole Agentic thing and everything.
Composing of it is where we really want to step in.
I don't think doing our own thing is gonna work.
**Arve Knudsen** 20:39 So would this be relevant to Salesforce, given this native metadata initiative?
**Kevin Landreth** 20:48 Yes, this will help quite a bit. Okay.
**Arve Knudsen** 20:52 That's super interesting.
**Kevin Landreth** 20:54 Yeah, it'll help shape some decisions around the new products that are being developed.
**Arve Knudsen** 20:59 Oh, really? I mean, so we are looking for feedback and attention, like we… You know, we're still, you know, at the proposal stage and trying to get sort of like buy-in from other Prometheus developers onto getting this into… into Prometheus. So I think, you know, like interest in this is crucial.
**Kevin Landreth** 21:24 Yeah. No, for sure. I will ask that you give me more than 30 seconds to read through it.
**Arve Knudsen** 21:30 Take your time.
**Kevin Landreth** 21:33 But no, I won't be able to read all this on this meeting, but just… Just the idea of it is… That's great.
And I'm glad it's something that's already being talked about.
**Arve Knudsen** 21:45 Yeah, actually, this dates back to 23. There's an issue from 2023.
**krajo Krajcsovits** 21:52 Yep.
**Arve Knudsen** 21:53 And it's been, like, moving slowly ever since.
**krajo Krajcsovits** 21:56 Yeah, I think, I think auto and, and, and AI really pulls it into focus now.
**Arve Knudsen** 22:03 Okay.
**krajo Krajcsovits** 22:03 Because…
**Arve Knudsen** 22:04 Yes.
**krajo Krajcsovits** 22:05 So.
**Kevin Landreth** 22:11 Is this the only working group around Prometheus? Are there other, like, subsections? Because, like, I know OTEL has, like.
30 working groups. and you have to go. You have to go through a gauntlet to even get invited to one of those meetings. So I'm still in the gauntlet for one of those.
Are there other working groups for Prometheus or other metrics? Or is this this one?
it.
**krajo Krajcsovits** 22:43 I don'.
**Arve Knudsen** 22:43 No, but…
**krajo Krajcsovits** 22:44 Everyone.
**Arve Knudsen** 22:47 Yeah, maybe not… I mean, is… Is there this UX working group? Can I…
**krajo Krajcsovits** 22:54 That's Prometheus, I, I thought Kavya had open, open telemetry working group.
**Arve Knudsen** 23:00 That was some. Okay, I'm not Did you mean, did you mean open telemetry working groups specifically, Kevin?
**Kevin Landreth** 23:08 Yeah, cause I was, I wanted to get.
**Arve Knudsen** 23:09 Okay.
**Kevin Landreth** 23:10 They pointed me as like, hey, go join Gen AI discussion so we can keep up apprised of what's coming. I'm like, okay. And it's got like six steps, I think, in order to get approved in order.
**Arve Knudsen** 23:21 Mmhm.
**Kevin Landreth** 23:22 join. You know, like, one of them, your company has to be a silver supporter, and it's like, okay, we have that. I had to get my Linux Foundation account all sorted out, and then I got a… I think there's something I need to sign, and then eventually I'll get a meeting invite.
to actually go to just the GenAI, and I don't know what it's going to take to get into the other OTEL metric ones, but it wasn't as easy as this one where there's a scheduled meeting.
**Arve Knudsen** 23:52 Mmh.
**Kevin Landreth** 23:53 And you can contribute. And I was like.
**Arve Knudsen** 23:55 I… I never joined, I've never been in it, but I think there might be a working group for like an open telemetry working group around infrastructure metrics.
**Kevin Landreth** 24:08 Oh, okay.
**Arve Knudsen** 24:09 I know about that because I Because I got involved in fixing some exporters, like Postgres, for example.
So, as I recall it, I was told there's a… Working group or saved, whatever.
Around exactly that, and… And maybe the… Maybe the open telemetry entity is interesting to you.
Yeah, yeah. Are you familiar with the, do you know what I mean by the entities data model in, in.
**Kevin Landreth** 24:46 Yeah, that's more of like the core of the protocol, right?
**Arve Knudsen** 24:50 Yo.
**Kevin Landreth** 24:50 Entities and stuff. Yeah.
**Arve Knudsen** 24:52 Because it's an extension to the resource data model.
**Kevin Landreth** 24:56 Yeah, I'm not as familiar with that as I want to be. Yeah, I'm just kind of before I was just.
**Arve Knudsen** 25:02 But these are.
**Kevin Landreth** 25:03 And now I'm… Diving in deep.
**Arve Knudsen** 25:06 But they, entities has a SIG with calls. You can join, you can join those.
If you're interested.
**Kevin Landreth** 25:12 Oh, okay.
**Arve Knudsen** 25:14 So they, they're very, you know, welcoming and friend So that would be like a recommendation from my side.
If that's, you know, fits the bill.
**Kevin Landreth** 25:27 Yeah, no, that that really does.
Sweet.
Yeah, okay, yeah, yeah.
So thank you. Well, I'm sorry I hijacked this.
**Arve Knudsen** 25:43 Okay.
We are only happy, kind of, that you're interested in our project.
Okay.
**Kevin Landreth** 25:53 I'll say it seems intimidating from the outside, because it's like Prometheus Working Group.
You know what I mean. It's it's not a branding problem. That's that's what it is. But mentally think it's like 30 people joining and debating.
**Arve Knudsen** 26:09 That's actually more, that's more like our data summits. Yeah.
**Kevin Landreth** 26:15 Exactly.
**Arve Knudsen** 26:17 Especially in person, I think. It's kind of like that.
**Kevin Landreth** 26:24 No, it's it's really not. It's been really nice to meet.
Both y'all.
**Arve Knudsen** 26:29 Likewise, keep joining if you like.
**Kevin Landreth** 26:33 Yep, I've got it on my calendar for I I I added it, so I'll keep joining. I got a lot of reading now. Thank you.
It's… is… so this design doc… native metadata.
That's the one we're discussing. That's the proposal.
From Grafana.
But then… Where's… Where was the… Design doc.
Oh, man, I closed the page somewhere.
The design doc that y'all were discussing originally.
**krajo Krajcsovits** 27:16 That's in the… if you look in the meeting invite, there's a minutes of meeting doc, and the top one.
Oh.
There.
I pasted it so there's a backlog and we discussed the top Item from me for you.
**Kevin Landreth** 27:35 We discussed the topic.
**krajo Krajcsovits** 27:39 And by the way, that native metadata Design doc, it's not… Like… It's kind of, We put that together with Arva as Prometheus maintainers.
And we didn't… I… I don't think we put anything in it that's Grafana-specific, so… And if there is, then there shouldn't be.
because we did that with our Prometheus maintainer hat.
Yep, right.
**Arve Knudsen** 28:13 I agree. It's supposed to be generic to Prometheus.
**Kevin Landreth** 28:18 It's a sponsorship, I guess, is what I mean.
**krajo Krajcsovits** 28:21 Yeah, yeah.
**Kevin Landreth** 28:22 Yeah, okay.
**krajo Krajcsovits** 28:23 So we didn't take into account, basically, feasibility in Grafana. That's, like, you know.
We're trying to look at it from It should be useful for users in the end, and then how we implant it, and if it's hard to implant, then… Sucks for us, but, like… It's just the waiters.
**Kevin Landreth** 28:45 Okay.
So I have skimmed and not read this current proposal, which is the job and instance reservation to OTEL.
on.
Kevin C: I haven't gotten down to the part where you were saying.
or you 2 were discussing.
like, is this something we make a change for? And you know, then you would have to go back.
you'd have to basically rip.
redo all the other metrics that came in that way. Is that what I on.
**krajo Krajcsovits** 29:20 I… so, retroactively changing metrics is… is not a thing in… in, like.
that that vendors do. So this would be a change that would impact a newly processed matrix only.
Yeah. Which means that if… yeah. So… so… which is why it's… it's… it's… it can be really breaking, because imagine you… you change it, and then your dashboards don't work anymore.
**Kevin Landreth** 29:48 Yeah, you essentially lose all those metrics.
**krajo Krajcsovits** 29:52 Yeah, yeah.
I mean, it would be cool if you could do that, but, like, some people keep metrics for, you know, 5 years and terabytes of data, and it's just not practical to change it.
And in fact, OpenTelemetry has This notion of schemas, where you can even Make a change, but still… access your old data, because the system knows about the change, and understands that when you ask for the new data, it has to look up the old as well. So this, you know, opens up the schemas.
so, yeah.
**Kevin Landreth** 30:32 Yeah, okay, so… If I'm reading this, this is the classic service name.
Job, and then service Id to instance.
debacle. And you guys are discussing on whether or not you should align.
With that or not.
Sorry I've only I've only got to skim through this, and So just wanna make sure I'm on catching up to the same page.
**Arve Knudsen** 31:00 Yeah, I mean, it is the initial revision of the design doc, and what we were discussing was, you know, potential revisions, I mean, to it, like, for example.
a day adding another design proposal like, as as far as I understand, David now has 2 2 design proposals in there.
And after, you know, going through it properly, maybe I'll propose, maybe I'll suggest a third proposal, maybe.
So, so that, you know, that's kind of how design docs work in general, that you, you have, let's say you have four proposals, of designs, and then you, the, the, you know, the stakeholders, let's say, or interested developers, they, they kind of agree, they kind of reach a consensus.
On which, which design to, to.
COVID.
So you have, like, a stated problem you want to solve, and then you kind of, like, you hash out the best design.
And so typically these documents, they go through many iterations.
Just to make that clear that this is not necessarily a documentation at the moment of how it's going to be. This is maybe just a starting point.
**Kevin Landreth** 32:26 Kris "Cowbert" Yeah, this is the proposal of Kris "Cowbert" this is the iteration of the proposal for it. Get Kris "Cowbert" for it.
**Arve Knudsen** 32:35 Yes, I think so. Yeah, it's like a working documents.
**Kevin Landreth** 32:40 It's the, the pre-me.
**Arve Knudsen** 32:42 Yeah, so So I think… I think the main problem David tries to solve is, like, Round tripping, I think, kind of to preserve preserve job and instance labels from Prometheus.
through OTLP and then back. I think so, at least. That's, like, the fundamental issue.
**Kevin Landreth** 33:08 This is pretty big. I'll take a minute to It'll be a little minute before I'm able to provide any good feedback.
Because I'm.
**krajo Krajcsovits** 33:17 Yeah, well.
Also, this design doc is really a companion piece for that OpenPR, so that's where the discussion started.
**Kevin Landreth** 33:25 Gotcha. Thank you.
**krajo Krajcsovits** 33:28 I actually have some messages that I have to Attend to, and an incident that I'm in?
Just a maintenance one, so, like, not things on fire, but I think I'll drop… But if you want to keep discussing, then feel free.
**Arve Knudsen** 33:50 I think I'm going to drop also, but Kevin, it was great having you in the call, and we'd be super interested in hearing feedback from the Salesforce org.
On the our native metadata.
The sign doc, and sort of, like, our ideas.
If, you know, if Salesforce would see that this would actually, you know, solve problems for you.
We'd be super interested in hearing it, and maybe you could even you know, present potential in new use cases, you know, apart from the ones we we have there already.
**Kevin Landreth** 34:32 That's what I'm.
**Arve Knudsen** 34:33 Yeah, that would be fantastic, actually.
**Kevin Landreth** 34:35 Awesome. Well, thank you everybody for being so nice.
**Arve Knudsen** 34:38 Yeah, okay.
**Kevin Landreth** 34:39 Next time.
**Arve Knudsen** 34:39 Yeah, see you next time.
**krajo Krajcsovits** 34:41 See you. Bye-bye.
**Arve Knudsen** 34:42 Bye-bye.
