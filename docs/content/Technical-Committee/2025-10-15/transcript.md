SIG: Technical Committee
Date: 2025-10-15
Duration: 25 minutes
============================================================

## Zoom Recording Transcript

**David Ashpole (dashpole)** 00:29 Hello?
**Armin (Dynatrace)** 01:49 Hey,
I saw that Lyudmia already approved your request for this CNCF mailing list, so you should have access now, already. Yep. You will get new emails if we get something sent to us, but if you need any history, then you can look it up on listcncf.io.
**David Ashpole (dashpole)** 02:10 Okay.
Thank you.
**Tigran Najaryan** 02:15 I guess.
**Armin (Dynatrace)** 02:17 Okay.
**David Ashpole (dashpole)** 02:20 Nope.
**Liudmila Molkova** 02:42 Hi, everyone!
**Tigran Najaryan** 02:46 Hello.
**Liudmila Molkova** 02:49 Oh, it's my turn to derive this call.
Let me share my screen.
Okay, let's check the community inbox…
**Tigran Najaryan** 03:43 So, I erased this one a while back. I think I only saw noise there. I don't think I ever saw anything useful out of it.
I don't know if anybody has a different opinion on that, really.
Could be that I looked at the wrong…
Wrong reports, maybe there is something useful there.
I think we had a brief discussion with Rylan on this, and he
I may be wrong, but I think he was going to look into it.
Was a few months ago, so, I'm maybe forgetting things.
**Liudmila Molkova** 04:23 Remember this discussion, and it, let's see…
**Tigran Najaryan** 04:51 Well, either way, if we look at the question that Robert is asking, is the TCE trier in monitoring the bugs, or it should be the responsibility of individuals who added fast tests?
Obviously, we can't be monitoring the… The best results for…
all of the repositories that OpenTelemetry has, and maintainers decide to use it, right? So I think the answer to that is… should be very clear.
We're not supposed to be looking at that.
I don't know if anybody has a different opinion, but I personally don't think I should go and look at…
**Armin (Dynatrace)** 05:26 I agree with that.
**Tigran Najaryan** 05:27 There will be fast testing, or collect, or do fast testing, and then do something about it.
**Armin (Dynatrace)** 05:34 I'm also sure that they would be in a much better position to assess whether those are high-priority issues that would need to be acted on immediately, or just noise.
**Tigran Najaryan** 05:47 Yeah.
**Liudmila Molkova** 05:50 Does anybody remember why we are, the contact there? Is it because we have the email list? Email?
**Tigran Najaryan** 06:00 I think that's the reason.
**Armin (Dynatrace)** 06:02 I have some fussy, no pun intended, memory on this. I think someone reached out… like…
somewhat out of the blue, blue that they were asked to set this up. And…
It was just, like…
We probably didn't consider it much and just gave them this email address as some point of contact to put in there.
But if we can put in the individual maintainer mailing lists, I think that would make more sense.
**Tigran Najaryan** 06:33 Yeah.
Yeah, I think it should be…
Per repository likely should be different mailing lists.
A mailing list for the maintainers of that repository.
I don't see the point of using the, the TC mailing list for this, and we could stop that.
And ask the maintainers of…
And it's not all maintainers. It's probably a small subset that is interesting in this. They should tell them, and they can go and do it for their own repository. If they need help creating mailing lists, we probably should do that, I guess.
That requires some help from the GC, I guess? I don't think I have access to that either.
I'm Bob.
Other than that, I don't see how we can be involved in this on a daily basis.
**Liudmila Molkova** 07:29 Do we know that it's actually useful? Did anybody actually… Found anything interesting?
**Tigran Najaryan** 07:36 I think I… at some point, I… Quickly…
reviewed a couple of the reports, and I found them… really useless.
Well, it could have been, like, bad luck, maybe I didn't…
I don't think I sampled enough to have a sort of a definitive answer.
**Liudmila Molkova** 07:58 It seems it's on… I only have seen it around Go, so maybe we can ask Go maintainers to decide whether it's useful, and maybe we should just turn it off completely?
If it's not useful.
**Tigran Najaryan** 08:14 I think, yes, what you're saying is the right approach, right? All…
SIGs decide on their own whether they want to have this
And if they do, they will be responsible for reviewing the reports.
All we can do as a TC, or actually the GC, should facilitate the creation of the mailing list if necessary.
Right? But then… Take… reviewing the generated reports is the maintainer's responsibility.
If they don't find it useful, we should just turn it off. I agree.
**David Ashpole (dashpole)** 08:46 Do you know where the notifications are configured? Like, is there a way to get issues opened in the repo or something?
**Tigran Najaryan** 08:53 Hmm, don't know.
**Liudmila Molkova** 08:54 It seems Trusk knows.
Oh, at least there is some documentation.
**Reiley** 09:09 I shared a link in the chat.
So, at least from the blog post.
The fast testing is not useless. Like, it actually discovered a lot of issues.
And… And I agree, like, the right owner traging those issues should be a different group.
**Tigran Najaryan** 09:38 Yeah. That's good, if it finds… Real problems and bugs.
then the maintainer should be interested in that, right? And they can decide that how they want to
Triage, or take the reports in, how they work on it, should be their process, not ours.
**Reiley** 10:01 Yep.
And,
I remember it's not something, like, CNCF required, like, you must have it, or they'll kick you out, but there's a OSS security recommendation, so you gotta score, and if you have fast testing, like, you will maybe have, like, 3 additional
points or something. So… I… I guess people would want to…
turn the overall, like, OSS security score to at least a green.
If not, like, silver or golden.
And… and that's probably why they enabled this.
But I would say, if you want to get the score, you want to enable this, then you should follow up, instead of just ignoring all the alerts.
**Liudmila Molkova** 11:04 Cool. I can summarize it and write this down in the… this year.
**Reiley** 11:10 Yeah, so… so from… from the TC position, I… I would say I… I think…
We should have it, like…
I don't want the collector maintainers to come and say, oh, we don't have time, let's just turn that off. I think that's wrong. So from CNCF standpoint, I think the general recommendation is, if you have a component
which takes input from a network, like, from the users, then you should have the fast testing, and you should be accountable for it.
**Tigran Najaryan** 11:44 Well, I generally agree with what you're saying, but I don't know…
the particular tests that are being run here, how they work, whether they are actually useful or not useful, I would still make it a maintainer stall to decide.
Whether they think this is the right tool.
For them to use.
**Reiley** 12:05 The heart is fun.
**Tigran Najaryan** 12:06 For fast testing.
**Reiley** 12:07 Yeah, that part is fine, but I think from the TC position, we should say we think collectors should have fast testing for the receivers, like, for various protocols it supports.
Which tool, and how people want to do that is their choice. Like, we'll leave that to the maintainers.
**Tigran Najaryan** 12:27 Yeah, and it may be that if the receiver is using a particular… well-known protocol, which already
As fast tests somewhere else, then probably you don't need
A duplicate of that in the collector repository.
So, for example, right, open OTLP receivers using protobubs. Protobuffs…
I'm fairly confident there is fast testing somewhere in the protobufs repository, so… I don't think you need fast testing for the protobuf decoders.
If you're using an existing implementation for decoder. But if you write your own, if you roll out your own, then probably you do, right?
again,
what I'm saying is that it depends, right? So, maintainers are in the best position to make the right call here.
**Reiley** 13:23 I'm not sure, because I'll give you one example. You use the protobuf library to deserialize things, so the deserialization part is already covered by Protobuf.
However, it is a particular field, and you put that in a hash map, and you believe that HashMap should have almost, like, linear performance, but someone smart enough to find a way to give you this crazy
like, DDoS attack, trying to cause all the collision. This is not deserialization, but this is how you use the data after desolarization. Still, you could get DDoS attacks, right? I think overall fast testing is… we assume you have problem unless you can
Like, technically, or logically show people how you shouldn't have that problem, or someone else is already covering that.
So the default assumption shouldn't be, it's already covered.
**Tigran Najaryan** 14:20 Yes. Yeah, I agree with that. If you have a receiver, you need to know
how well it is tested. Is it covered, not covered? Where is it covered? Do you need additional coverage on your own? I agree with that, yes.
**Reiley** 14:34 Right.
**Liudmila Molkova** 14:48 So, sounds that the recommendation would be to have it on, some form of it.
**Tigran Najaryan** 14:57 I think… Yeah, we endorse having fast testing, right?
We don't require usage of a particular tool, I think that would be the wrong thing to do.
Because we are not the ones who are running it, and not the ones who are fixing the problems it finds, and if it has false positives, then it's a headache not for us, but for the maintainers. I would rather make sure that they have the power to decide which tool they find useful.
For their particular language or repository.
Unless you're investing, there is, like, a…
clear-cut solution to this, like a well-known tool, if this…
what is it, OSS buzz thing is…
is that the only thing that we should be recommending, then maybe, but I personally don't know.
I'm not aware of.
How widespread it is used, and how well it works.
**Liudmila Molkova** 16:09 So, if we want everybody to use it, it's only available… it's only enabled on Collector and Go and GoContrib, it seems so.
Because it's… the tool is probably specific to Go.
we would… Want to document some way
For other repos to enable appropriate tooling.
**Tigran Najaryan** 16:37 And I think, maybe an interesting way to do that would be for anybody who is actually using it to
Show to the other maintainers the value of it.
So if it's the Go repository, who is the first one to use
Maybe we… once they… after a while, we can ask them to come to the maintainer's call.
And, tell about their experience, maybe a bit.
**David Ashpole (dashpole)** 17:19 Yep, I think that definitely makes sense. I recall this being added as part of the, like, scorecard…
Effort, and we just did it to tick a box, but…
I'm sure we would love to have these reports, if there's a way to get them filed as, like, issues, or somehow give them access to the GoSig.
Forgive a sec.
They do look useful, actually, especially for the YAML parsing stuff.
**Reiley** 18:03 Okay, so, if you look at the OpenTelemetry Collector.
repository on the main README file, there's the OSS file… Edge.
And it shows fiving.
And also, the OSS best practice, I… I think it… the fast testing is checked.
So essentially, people are getting the credit, and they should do the job.
**Liudmila Molkova** 18:36 Jim and Dish.
**Reiley** 18:37 Yeah.
**Liudmila Molkova** 19:09 Okay, sounds like we have a recommendation, and I can summarize it and write it down in the issue.
We'll see if Go maintainers would share the findings, and we… I also…
Well, depending on what they say, I would like to… for them to present it on the spec call.
So, should we move on to the next topic?
**Reiley** 19:40 I think so.
**Liudmila Molkova** 19:42 Okay.
Sigrin, do you still want to talk about SQL Comment, or is there something else to discuss?
**Tigran Najaryan** 19:48 No, I think we're good there. We responded to the issue. The issue, I think it got closed evenly, so… nothing else to do there.
**Liudmila Molkova** 19:57 Okay.
So Dan, any other topics?
**Carlos Alberto Cortez** 20:06 There was a document that Josh shared with us about specification maintainers, so probably consider taking a look at that one, if you haven't.
That's in Slack.
**Liudmila Molkova** 20:20 So let me end the link.
Do you want to review it, online? Or, I mean, synchronously here?
**Carlos Alberto Cortez** 20:33 No, I don't think we have to. There are some… All results, items, and discussion.
it's not too long, but I think it probably makes more sense to, you know, if Josh was here, probably he could make a summary of the last iteration, but we can do offline, I think.
**Tigran Najaryan** 20:54 Yeah, I think we should review it offline, and when Josh is here, maybe we can have a live discussion.
**Carlos Alberto Cortez** 21:00 Yep.
**Liudmila Molkova** 21:14 Okay.
So if there is nothing else, then… Thank you all.
**Reiley** 21:24 Bye.
**Tigran Najaryan** 21:24 Thank you. Bye.
**Carlos Alberto Cortez** 21:26 So…
