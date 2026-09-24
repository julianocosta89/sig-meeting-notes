SIG: Developer Experience SIG (EU)
Date: 2026-09-23
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Johanna Öjeling** 00:30 Whoever!
Hi!
Nice to meet you.
**Victor Lu** 00:43 Yeah, nice to meet you. You and I don't join this one, I'm based in the US.
Some of them happen to be on a train, the Cambodian and Corn right now.
**Johanna Öjeling** 00:54 Oh, okay.
Let's see if anyone else shows up. Giuliano, who is a maintainer and usually joins, he's in Brazil, still, so he probably won't make it.
But we usually have Perk joining as well from Europe, so he might show up.
Are you, have you been active within OpenTelemetro before, or…
**Victor Lu** 01:25 Yeah, I joined the, the, the US meeting, this one before.
**Johanna Öjeling** 01:31 Aha, okay!
I, yeah, I haven't seen any meeting notes for a long time. Has there been anyone else there? Or have you been the only one?
**Victor Lu** 01:45 This is the first time I joined this one, so I'm not sure.
**Johanna Öjeling** 01:49 Oh, okay.
So that was some other SIG you joined then, or…
**Victor Lu** 01:55 Yeah, I joined the same meeting, but in the US time zone.
**Johanna Öjeling** 02:04 Right, and which parts of OpenTelemetry are you familiar with?
**Victor Lu** 02:10 I'm actually a journalist.
**Johanna Öjeling** 02:15 Oh, okay.
**Victor Lu** 02:15 Yeah. So, one thing I'm doing right now is that there's a collaboration between OTEL and OCSS.
When it comes to, security metrics?
Bit launch.
I'm, like, kind of coordinating that, effort between, hotel.
OCSF, and, and actually COSI, another organization, non-RF-funded, organization called COSI.
**Johanna Öjeling** 02:53 Okay.
Thanks.
Yeah, my name is Johanna, I am a trainer role.
of the developer experience, like, I work at, IKEA in Sweden, but I used to work at Grafana Labs, So that's how I got involved in open telemetry.
Is there, Anything you wanted to discuss in this meeting, or is there something? Yeah.
**Victor Lu** 03:28 Oh, y'.
**Johanna Öjeling** 03:28 a jumbo.
**Victor Lu** 03:29 I was preparing to continue to listen, but, maybe, maybe you can maybe tell me what, what this, SIG has been covering?
**Johanna Öjeling** 03:40 Yeah, absolutely. So our mission is to improve the developer experience for OpenTelemetry users, and that, you know, can take different forms. What the SIG has focused on so far is running surveys to find out, you know, what are the pain points and frustrations among users.
And then we've been running an initiative Or the outcome of a survey that we ran One year ago, so… was that, users… We're kind of missing guidance for how to move from this, like, quick start, how to get started with OpenTelemetry with the collector, to how to actually configure it in production. So we've been running a series of interviews with, organizations.
And we've interviewed them on how are they using the collector, what does their architecture look like, why did they adopt it, and what… what are the lessons learned, and then we've published blog posts about these stories.
So that's mostly what we've been up to so far, and we have some Interviews and blog posts, also, in the pipeline.
**Victor Lu** 05:08 Okay, yeah. Yeah, I think, can you help me, Have you ever heard of something called OCSS?
**Johanna Öjeling** 05:17 It's the section.
**Victor Lu** 05:18 Severus… Hotel so far has not covered, like, security matrix, a lot. Is that at least your, understanding as well?
**Johanna Öjeling** 05:33 Hmm… I'm not aware…
**Victor Lu** 05:39 If you look at the security matrix, there is a very limited hotel at this point.
**Johanna Öjeling** 05:47 Where, where should I look?
**Victor Lu** 05:51 I don't know the central place to look or not. The one, the one team we are collaborating, I guess I'm coordinating with is the semantic, Agent… Agentic AI semantic, Convention Group.
**Johanna Öjeling** 06:11 Okay,
**Victor Lu** 06:15 At least according to the discussion there, in general, fixes, they're limited.
**Johanna Öjeling** 06:23 So, the… what's limited?
I couldn't hear you.
**Victor Lu** 06:30 I'm sorry, what is it?
What's the question?
**Johanna Öjeling** 06:33 Your sound is breaking a bit, so I can't… I couldn't hear what… what were you saying about the semantic dimension sake?
**Victor Lu** 06:42 Oh.
Yeah. Oh, the hotel security matrix, is very limited at this point.
Hmm.
**Johanna Öjeling** 07:01 And, what, what are you, hoping to, get out of interacting with the developer experience SIG?
**Victor Lu** 07:13 Actually, I'm not sure. I think, Were there any… according to your survey, what do people say about the hotel in general? What is, like, what is… Strong add, and what is, kind of a… still need to, add?
**Johanna Öjeling** 07:33 Yeah, I'll see if I find the link. Hey, Fabrizia.
Okay, I found… Ending… Here, but in general, what users… Where… Asking for were better, like, clearer documentation.
**Victor Lu** 08:05 Yeah.
**Johanna Öjeling** 08:06 Guidelines and, like, real-world examples for how to set things up in production.
**Victor Lu** 08:14 Okay.
**Johanna Öjeling** 08:17 But,
**Victor Lu** 08:17 Documentation.
**Johanna Öjeling** 08:18 People we've interviewed, they are, like, they're pleased with their overall experience is good, and they find the collector very flexible, and some have highlighted the auto-instrumentation features of the OpenTelemetry Operator.
**Victor Lu** 08:40 Okay.
Okay, so this is more, okay. So this is more about the, developer experience for the hotel itself.
**Johanna Öjeling** 08:52 Yes, exactly.
**Victor Lu** 08:57 Oh, okay.
So it's not for user experience.
**Johanna Öjeling** 09:05 What do you mean?
**Victor Lu** 09:09 End user.
**Johanna Öjeling** 09:11 Yeah, it's for… it's end users who… who responded to this.
**Victor Lu** 09:18 Okay, did it mention, like, what feature is, missing, for example?
**Johanna Öjeling** 09:27 Hmm… Not that I can see right now, but there are… there have been some other surveys.
run, Where, yeah, that might have gone more into detail about that, but yeah, I…
**Victor Lu** 09:54 Yeah, okay, that's good, yeah.
Yeah, thank you. Yeah, this is good, information.
**Johanna Öjeling** 10:04 We'll see if I can find… the others. There is a GitHub repo with the, All of the raw data, also, with the responses,
**Victor Lu** 10:17 Yeah, it'd be good, because, I didn't really realize this is the case until, having discussed, you know, multiple communities, and then… AI security, security matrix is, at this point, pretty basic, at least, for hotel. So I wonder, other than security, what other, matrix are also kind of, Need additional, metrics? And work?
**Johanna Öjeling** 10:51 I know there have been some… Okay, also, yeah, if you check the blog there, you will find… some other… like, they have a survey in the title, like Prometheus and Ital Survey. I know there have been some about the collector.
But yeah.
Yeah, we also have a Slack channel on the CNCF workspace, so if, If… if you need any other… Anything else from us, also feel free to ping us there.
Yeah. Oh, yeah.
**Victor Lu** 11:42 Thank you.
**Johanna Öjeling** 11:43 Yep, Faurice. How are you doing, Fabrizia?
**Fabrizia Rossano** 11:47 I'm doing good! I've been away for a while, and then I came back.
And, I mean, you, you know we have OBSCON, so it's been kind of crazy.
**Johanna Öjeling** 11:59 Oh, that's…
**Fabrizia Rossano** 12:01 Sorry I've been missing for a while. There's been a lot of prep around… That, but now it's kind of settled.
So… Not black.
Not that anymore.
**Johanna Öjeling** 12:15 How was Grafana Fest?
Did he go?
**Fabrizia Rossano** 12:18 What's good! Yes, I went. I went. It was over the top, as you would expect.
Something like that. I mean, They organized it for one year.
It was incredible. It was good. I met a lot of people, especially a lot of people that I haven't had a chance to meet before, because there's been.
**Johanna Öjeling** 12:42 Huh?
**Fabrizia Rossano** 12:43 Huge inbound of new joiners.
In the past 6 months.
came to Rafana Fest, which was a good… Good chance to meet them. Yeah.
That's been fun!
That said, like, you know how these things are? There were, like, 1,500 people in one place, which… Like, at this point, you just wanted to be alone in a corner.
**Johanna Öjeling** 13:11 Mmm…
**Fabrizia Rossano** 13:12 Cannot talk to anyone.
How's your new job going?
**Johanna Öjeling** 13:18 Yeah, it's very well. Yeah, I've been here now for almost 3 months, and I'm starting to kind of get used to the processes and, But yeah, we've been going through some reorganizations, so, yeah.
**Fabrizia Rossano** 13:36 But I bet it's pretty different.
from, johanna, as the size is different, the type of things you deal with are different, so…
**Johanna Öjeling** 13:49 Yeah, - yeah, like, very, very different, Yeah, and when I, when I saw the, the pictures that people posted from Grafana Fest, I was like, oh!
I was sad I missed that.
**Fabrizia Rossano** 14:06 But, you know… I'm pretty sure it has other perks, like…
**Johanna Öjeling** 14:11 Yep.
**Fabrizia Rossano** 14:11 You have discounts on furniture?
Who cares?
**Johanna Öjeling** 14:15 Sorry?
**Fabrizia Rossano** 14:15 Do you have discounts on furniture? Like, I'm…
**Johanna Öjeling** 14:18 We do, yes, yes, yes, so that's a good benefit. I just ordered some new things earlier this week that I needed for my home. So yeah, we have a co-worker discount, and yeah.
**Fabrizia Rossano** 14:33 So… So, I was reviewing the notes of what happened, and I see last time there was a future of SIG, I'm happy to continue with service and interviews, too, if you want, like, come in.
**Johanna Öjeling** 14:54 -
**Fabrizia Rossano** 14:54 definitely, if I can run interviews, since we have the… Din… template, we can check if there is any… like, I don't know if we already have a pipeline of people that we already contacted, or should we just start talking to people, but…
**Johanna Öjeling** 15:15 Yeah, so… to… give some background. We, we, yeah, in the past few weeks and months, we've been talking about what should the SIG be doing, like, do… yeah, we've had this initiative with the blog posts and interviews, should we continue with that, or should we… Run some other initiatives, and… Last week… yeah, then Park and I, we kind of concluded that, yeah, we're happy to, continue to, to do the interviews, and if needed, run new surveys, But we also said we'll, we can catch up.
in person, because we're… like, Juliano and me and Park, we're going to this Open Observability Summit, Europe, in Prague, in… on the 5th of October, so we said, okay, we can catch up and talk more then.
Yes, but yeah, of course, since, yeah, not everybody is going, we will also continue to, discuss here. But yeah, right now, we don't… we have some blog posts that are in progress, or being written, or being… getting published, but we don't have any… other organizations in the pipeline, so I think next step will be to, yeah, start identifying organizations that have interesting use cases, and that would be happy to share their experience. And also, is there any particular part of OpenTelemetry that we want to focus on? Like, we've focused on the collector so far, like, do we want to continue, or… explore other areas, so I think this could be…
**Fabrizia Rossano** 17:05 Yeah.
I floated an idea some time ago, But I need to write the proposal. I'm sorry, I haven't had the time. It was just before the holidays, and then it's been crazy. But you were there, so I'll talk you through what I was thinking. I was… I tried to approach the hotel demo and hotel instrumentation.
as, non-technical users. So, my rationale for this is that with, With the race of non-technical founders, so you have a lot of people that now are building up, entirely vibe-coded.
But at some point, they need to instrument the telemetry, right?
And as a non-technical user, I think… The overall… the demo, and also the initial instrumentation.
I tried it, and I had some bumps, so I'm gonna document those bumps, because maybe there are things we can simplify, or propose to simplify, as a… the experience of non-technical users approaching OpenTelemetry, or, like, lightly technical users approaching OpenTelemetry.
Which might be an interesting point of view, since, like, the… User base of… all of this, like, tele… like, not all… like, telemetry is kind of an afterthought, but, sorry, but the user base of… agents and, like, tools like Cloud Code is expanding.
**Johanna Öjeling** 18:59 I'll see.
**Fabrizia Rossano** 19:00 of, of, developers, we all know that good instrumentation, good telemetry is key, even for agents. Like, even if you're, like, you're a non-technical founder, and you're just using your cloud, your codecs, your whatever.
If you don't have good instrumentation, it's going to be really hard for your agent to understand what's happening and troubleshoot your prototype.
And so, if we could… like, guide these people to open telemetry.
And then help them instrument, and help them understand that that's key for success.
That would be, I think… An angle that it's not really explored.
Currently, So, like, how do we… Guide non-technical people to instrument their Badly written code.
**Johanna Öjeling** 20:10 -
**Fabrizia Rossano** 20:11 telemetry.
**Johanna Öjeling** 20:17 Yeah, I think that's, that's an interesting angle, as you mentioned.
**Fabrizia Rossano** 20:26 I mean… The thing is, people will have this question, and if you ask an LLM, it usually goes straight into commercial offering, because it's commercial offering… of, better representation on the web.
and OpenTelemetry doesn't.
And so, if we could have something… Let's say that… It's targeted to this, maybe, it gets surfaced more.
get the end.
goalie?
more people use OpenTelemetry.
As the sun?
**Johanna Öjeling** 21:10 Yeah.
**Fabrizia Rossano** 21:15 Good. I'll need to find some time, I'll write a proposal.
**Johanna Öjeling** 21:19 - Nice! Yeah, I look forward to, to reading more. Yeah, I think that's, an interesting topic.
And do you have, do you have ideas already for what the… Kind of format of the guidance would be,
**Fabrizia Rossano** 21:45 So, I have a couple.
not many, but, like, one of the things that I noticed, like, if I don't use agent.
And I go… Through the Autel demo.
There are different options to set it up.
And it's not super clear what are the benefits.
Of using one over the other.
Because it… it has, like, The… the assumption is that you should know.
But as more and more non-technical people approach it.
I think being a bit more verbose and a bit more… Like, clear and, like… use Docker versus Evit on your machine, like, all the different options you have to set up the demo, and then got sort of, like… Pro and cons of each one.
Or… consider dropping this part of the demo when? Because, you know the demo is modular, you might not want to run all the services.
So… It tells you that, but it doesn't tell you when you actually shoot.
consider not doing a part. So that could be one initial thing, like slimming down and helping, and I was talking… I think it was with Perk.
That's also a maintainer.
of… the hotel demo, and it was like, yes, like, write it down, and we can see what we can work to.
**Johanna Öjeling** 23:29 Nice.
**Fabrizia Rossano** 23:31 And then for the other… the rest should be around docs, basically, but I need to really go in deep into the docks.
maybe have a bit more, like, I don't know.
I need to play a bit and see what I come up with.
**Johanna Öjeling** 23:49 - yep, makes sense.
Great, but yeah, let us know whenever, you have something, you want a review on.
Cool. And also feel free to… to, you know, ask for feedback or, yeah, ideas.
**Fabrizia Rossano** 24:10 Definitely. I write it in this, like, under the proposal tab.
**Johanna Öjeling** 24:15 Oh, yeah,
**Fabrizia Rossano** 24:16 So, everybody can see it.
**Johanna Öjeling** 24:19 - that's great.
Good.
**Fabrizia Rossano** 24:25 Yeah, I don't have anything else. I'm sorry I have a meeting there.
I've passed, so I'm probably…
**Johanna Öjeling** 24:36 Yep, I think that's it, or anything else, Victor?
Perfect sound.
**Victor Lu** 24:43 Nope. I'm good, thanks.
**Johanna Öjeling** 24:47 Okay, good. Yeah, then we can wrap it up here. So, thanks for today. Good to see you both.
**Fabrizia Rossano** 24:53 Here next week.
**Johanna Öjeling** 24:55 And I…
**Victor Lu** 24:55 Rakuten out.
**Johanna Öjeling** 24:57 Bye!
**Fabrizia Rossano** 24:58 Bye. Bye, Johanna.
