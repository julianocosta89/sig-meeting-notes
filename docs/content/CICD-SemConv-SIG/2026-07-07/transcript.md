SIG: CI/CD SemConv SIG
Date: 2026-07-07
Duration: 23 minutes
============================================================

## Zoom Recording Transcript

**Alan Clucas** 04:07 Hello?
**Michele Mancioppi** 04:11 Hi.
**Christophe Kamphaus** 04:18 Hello.
Since Adriel said he might be a bit late, let's do some triage already.
And if you have any topic, add it to the… Meeting notes.
There's been some activity on this pull request.
Not sure if you've seen it.
**Alan Clucas** 07:13 I really haven't.
**Christophe Kamphaus** 07:36 No, I think there's been some activity recently. I will take another look at it after the meeting.
Other than that, I do not see… Much having changed on our board.
Is there anything you'd like to discuss?
**Alan Clucas** 08:20 Got no topics.
**Christophe Kamphaus** 08:34 I don't have anything from my side either.
**Michele Mancioppi** 08:49 I have a question.
**Christophe Kamphaus** 08:51 Sure, go ahead.
**Michele Mancioppi** 08:53 We, yesterday we received a, donation from, a GitHub user that was maintaining an auto CI/CD action.
And we had contributed to it in the past.
And they said that they cannot maintain it anymore, and they were looking for a new home, and we accepted it, and we are going to… To, maintain it.
**Christophe Kamphaus** 09:21 -H.
**Michele Mancioppi** 09:22 Is there?
Currently, a, other GitHub actions that showcase what the semantic conventions should be.
**carlosalberto** 09:41 By the way, before you guys answer that, that's the action I mentioned in the Slack channel, you know, the one that Adriel was reviewing in the past.
**Michele Mancioppi** 09:53 Oh, hi, Adrian. Long.
**Adriel Perkins** 09:55 Hey, yeah, good to see you. How you been?
**Michele Mancioppi** 09:58 Hi, Hazen.
**Adriel Perkins** 09:59 Good, thank you.
I don't know what the general process is for donations to OTEL, I'm not sure if that's what you're asking.
**Michele Mancioppi** 10:08 No, no, no, you don't need it.
**Adriel Perkins** 10:10 Okay, cool, cool, cool, cool.
**Michele Mancioppi** 10:15 And we would love to make it the… Like, excellently complying to the semantic conventions, to…
**Adriel Perkins** 10:22 No.
**Michele Mancioppi** 10:22 Right? Yeah.
**Adriel Perkins** 10:23 Yeah, yeah.
Yeah, I remember talking to, oh, man.
Peter? Is it Peter?
Yeah, I think it's P like early on the day, what?
**Michele Mancioppi** 10:36 Youngton.
**Adriel Perkins** 10:38 Yeah, I think so. Like early, early when dash zero got started about the CID CICD stuff.
But I think this, like, pre- that predated, this, this repository.
Yeah.
From the GitHub is a odd beast, right?
We had a ticket that was on the board for doing a mapping for GitHub attributes.
I'm not sure if it got picked up.
Let me see if I can find it.
Yeah.
And of course, with the environment variable context propagation spec, Things have changed a little slightly.
But not too terribly.
**Michele Mancioppi** 11:31 So if today you should name one code base.
That is the poster child of Cscd semantic conventions.
How could it be?
**Adriel Perkins** 11:46 Hmmm.
That's a good question.
**Christophe Kamphaus** 11:53 Probably the GitHub receiver is the closest one.
**Michele Mancioppi** 12:00 In the collector.
**Christophe Kamphaus** 12:02 Yes.
**Adriel Perkins** 12:09 By no means is it perfect, though.
I just sent the link to it.
**Christophe Kamphaus** 12:22 Therefore, Jenkins, I also propose the pull request to adopt the semantic conventions for CI/CD.
**Michele Mancioppi** 12:29 Mmhm.
**Christophe Kamphaus** 12:30 But, progress on that is slow.
**Michele Mancioppi** 12:36 So is it my understanding that in this SIG you are evolving the semantic conventions faster than the implementations then?
which is legitimate. I'm just asking.
**Christophe Kamphaus** 12:53 Yeah, it has been that way from the beginning.
And afterwards, we started catching up with the implementations. It's also us at TroveSat.real for the collector and me for Jenkins. I think Alan for Argo workflows.
**Michele Mancioppi** 13:20 So, Carlos, let's make another one. And that's the Gith.
**carlosalberto** 13:24 Yeah, I didn't want to start talking. So the thing is that, just for your information here, that when Michele told me about that last week, I was surprised to see that it mostly follows all the same comp, including the latest stuff.
Michele was, updating that yesterday to update some Error stuff, so we're in a good track there, and it should help us.
To try out new stuff, you know?
From this group, I mean.
**Christophe Kamphaus** 14:00 And is it still my… correct when I understand that we need to use a GitHub action if we want to… emit spans inside a specific workflow step.
**Michele Mancioppi** 14:13 Yep.
Okay.
**Christophe Kamphaus** 14:15 And also, if you want to propagates the same context from the GitHub receiver, and link it to So, Spence, inside… This step.
**Michele Mancioppi** 14:28 I mean, technically, we have ways with the nurse zero CLI to create span and send telemetry over that could be embedded in steps, but we need to figure out the context propagation there.
**Adriel Perkins** 14:43 Yeah, so for the GitHub receiver, we had to do a deterministic span ID method.
Which I think generally kind of diverge diverges from.
what, the specification.
want for span IDs, but it is kind of like the lesser of two evils. Like, if you want to be able to connect steps to a… To that, you have to be able to figure out the IDs because the runners are not instrumented, right? If GitHub would instrument the runners themselves.
then all of these problems would go away. But because, that's not the case, and we… we want the, like, our original parent of the… the workflow run.
And jobs.
There's a… there's a way you calculate deterministic spanities that are inside of, that GitHub receiver in the docs.
And then the code, of course.
As well.
But then within steps, if you do the normal environment variable context propagation and calculate or compute those span IDs, then you can get that.
Lower level step detail.
I assume the… The CICD action, because it looks like it's diverged from its original fork, too.
**Michele Mancioppi** 16:03 The original part is unmaintained, like, 3 years without any.
**Adriel Perkins** 16:06 Yeah, and… Yeah, yeah.
Let's see.
Okay, so now it just automatically routes.
Yeah, the OTel export trace action. Sorry, that was the original one that I was thinking of that was unmaintained for many years.
Yeah, that one… Never used deterministic IDs at all. It was just like step level.
I think.
Yeah, sounds right.
and this just covers, right, like, this just covers… actions that where you would run scripts within, right? Like, basically run statements.
No.
**Michele Mancioppi** 16:58 I know, it's actually… Goes and downloads the workflow. I think it overlaps with the GitHub receiver.
**Adriel Perkins** 17:09 Okay, cool.
Okay.
**Michele Mancioppi** 17:16 But we could try to make them interoperable.
And you do need to have.
Some… something built in in your workflow, if you want to be able to trace within the steps.
**Adriel Perkins** 17:32 Right, right.
**Christophe Kamphaus** 17:33 Mmhm.
**Michele Mancioppi** 17:35 Good. Then Carlos and I will have some fun with this. Let's see how we can push it.
**Christophe Kamphaus** 17:40 No.
And maybe even, support locks, because that's something that's not currently… Implemented in it, or… I, read it right.
**Michele Mancioppi** 17:53 Yeah, that's a good idea.
Carlos, you're taking notes, or I already started opening GitHub issues.
**carlosalberto** 18:05 Yeah, it's Zulav.
**Michele Mancioppi** 18:30 Oh.
Yeah, we'll, we'll report in the next few weeks what comes out of this. I think it can be an interesting, learning experience.
**Christophe Kamphaus** 18:46 Yeah, definitely sounds interesting.
**Michele Mancioppi** 18:54 And then, if you touch lead, it turns out to to get of Good quality.
in the future we'll be open to transfer it under open telemetry. If it becomes something that the sake wants to support.
Not just, their serum.
**Christophe Kamphaus** 19:13 Yeah, for sure. And I think We could also use it in the internal OpenTelemetry workflows.
Definitely see how it works there.
**Michele Mancioppi** 19:23 And.
**carlosalberto** 19:23 Actually, that's what I wanted to say, like, maybe it sounds a little bit pretentious, so to speak, but I think it could be good to, Dog feeding dove.
If that's okay, especially given that the plan would be to eventually donate this to hotel, you know.
**Michele Mancioppi** 19:38 Hey, Manjula, when it's good.
**Adriel Perkins** 19:41 Yeah, if it's especially if it's made compatible with the GitHub receiver, because we do already have those traces from all of the pipelines that run within the OTel community today, from the GitHub receiver, we do capture those.
But obviously we don't capture any underlying steps, which is.
where the… that's where… where, Robert and Christoph and I have been talking.
In the chat, Because there's like several different, like in some of the shared workflows, there's like, you know, Python scripts that could use the environment variable context propagation to be able to start getting some of that lower level instrumentation in the steps.
That we've been talking about.
But… We do capture all of the high-level Workflow runs and workflow jobs and, you know, just the top-level step traces today.
I just have to be careful with how much I open that up to everyone.
due to, the vendor that is being used on the back end to store that information. So, I'll leave it at that, I just have to be a little… Right now, the actual, like, you being able to use the information and analyze the traces is a little locked down.
**Christophe Kamphaus** 21:01 I guess if we would also allow any scripts in our workflows to use and export.
OTLP.
You would also have to expose the endpoint to which to send it.
**Adriel Perkins** 21:15 Yeah. If you want to understand how that is exposed now, there is a… I want to say it's been merged. Let me double check, but… Yeah.
I'll send the link to it, but there's information in the community page under assets on who owns that.
It's me.
It's my infrastructure, currently.
Predominantly, anyway. I do use the… Oracle account that we have for AWS, or, I'm sorry, not… the Oracle account we have for OTEL, to host some of the core infrastructure, but then, like, all, all events and the endpoints are coming through my Cloudflare Zero Trust setup. So, that's how it gets there today.
And I'm going to paste this link in the chat for context.
**Michele Mancioppi** 22:38 Yeah, I have probably opened it.
Okay.
**Christophe Kamphaus** 23:09 Any other topics?
I guess we can give you back the time, and… See you next week.
**Alan Clucas** 23:44 Nice.
**Adriel Perkins** 23:46 Cool. Have a good one.
**Christophe Kamphaus** 23:47 You too. Bye.
