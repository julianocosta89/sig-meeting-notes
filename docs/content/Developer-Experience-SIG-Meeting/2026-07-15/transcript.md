SIG: Developer Experience SIG Meeting
Date: 2026-07-15
Duration: 28 minutes
============================================================

## Zoom Recording Transcript

**tristan** 00:57 Good.
**Juliano Costa | Datadog** 00:59 Good morning.
**tristan** 01:03 on it.
**Johanna Öjeling** 01:13 Hello?
**tristan** 01:15 Luke.
**Johanna Öjeling** 01:16 Hey!
Possibly.
**Juliano Costa | Datadog** 01:21 Distant How is the new work?
**Johanna Öjeling** 01:24 Yeah, it's, it's good. It's, always a lot to take in, when starting a new job. So, yeah, my head is, like, full of information trying to.
**tristan** 01:37 Yep.
**Johanna Öjeling** 01:38 Yes.
How are you, Jude?
**Juliano Costa | Datadog** 01:44 Alive.
Yeah, sure.
**Johanna Öjeling** 01:46 Are you still working, or do you have any upcoming, yeah, picture?
**Juliano Costa | Datadog** 01:53 Nothing planned for the next, months, actually, so.
No.
I think I'm gonna.
**Johanna Öjeling** 02:02 Stay alive then.
**Juliano Costa | Datadog** 02:05 We have to save some days to go to Brazil at the end of the year, so.
**Johanna Öjeling** 02:11 Oh.
**tristan** 02:12 Yes.
**Johanna Öjeling** 02:13 Please.
**Juliano Costa | Datadog** 02:13 It's a long trip, so we need to stay a couple of days to be worth it.
Okay.
**Johanna Öjeling** 02:20 -
**Juliano Costa | Datadog** 02:24 Oh.
**tristan** 02:25 I'm not doing anything. I never take any days.
**Johanna Öjeling** 02:28 Mmhm.
**Juliano Costa | Datadog** 02:32 You are in Canada, Tristan, not in US anymore. You have to take some days off.
**tristan** 02:40 Well, I'm not in Europe, so I don't get all of August off, but…
**Johanna Öjeling** 02:45 Mmhm.
**tristan** 02:46 It's close.
Okay.
**Juliano Costa | Datadog** 02:54 Oh.
cool. So I think I I didn't open the agenda. Actually.
But we have two… Two blog posts to… to get going. I mean, we need to review them. I know that, Johan already reviewed the… The one… or give the initial review, the one from… Atlassian.
I haven't actually checked any.
Go ahead, Johanna. Sorry.
**Johanna Öjeling** 03:33 Yeah, I made a first pass at the Atlassian blog post and it looks really good. I just had some comments to kind of make it more aligned with the existing blog posts about.
For instance, using Excalidraw for the, architecture diagrams and… I, inserting some quotes, if suitable, and so on.
And I've started to review the keycloak, but just… yeah, I threw it briefly, but I will, Have a closer look.
**Juliano Costa | Datadog** 04:21 Oh, yeah, yeah.
**Fabrizia Rossano** 04:22 And.
Oh, sorry. I started reviewing the key clock again. Also, I've I did a couple of, suggestions that I see now they are accepted, But, yeah, for that too, we would… need, I think, a diagram or some quotes that are missing.
**Johanna Öjeling** 04:50 Yeah, I think…
**Juliano Costa | Datadog** 04:51 By… by missing, you mean missing on the blog post, or missing from the…
**Fabrizia Rossano** 04:57 From the interview.
**Juliano Costa | Datadog** 04:58 It was tough.
**Fabrizia Rossano** 04:59 On the blog post. On the blog post.
**Juliano Costa | Datadog** 05:03 Okay, so maybe we do have the… The context is just… Actually, the the key clock guys are are actually… pretty approachable.
Oh.
They are also CNCF, so it's easy to… To get to them.
Yeah.
Fabrizio, as you were here last week with Perk, would you mind… sharing with me what you discussed about the hotel demo. I'm interested because I'm a hotel demo maintainer, so…
**Fabrizia Rossano** 05:48 Yes, and I was planning to add a proposal there, but I didn't get the time this week, so I tried to run the hotel demo, but of course, I'm not a developer, so I was missing a lot of the, Prerequisite, like… versions of Python, different libraries and stuff. And I was wondering, would it be useful to have a script Or a scale, or something that… Like, you run before running the demo that checks all the prerequisites and tells you this is what you're missing and all you need to install before you start Making the demo work, because I start, like… For me, it was, okay, I'm at this point, and then I was blocked, and then I had to go and install something and come back, and if I had some… thing at the beginning that would tell me this is what you're missing, and this is all that is outdated. Please go do this, and then it would have been faster.
that… to get started.
**Juliano Costa | Datadog** 07:02 Yeah, it's interesting. Now that you're saying, I'm actually curious of what you were missing, because in theory.
you would only need Docker.
But I can be wrong.
**Fabrizia Rossano** 07:15 I was missing Docker.
It's it's what some Npm. Libraries is also said. You need them, or something go related. That says you don't have this library.
**Juliano Costa | Datadog** 07:26 It's.
**Fabrizia Rossano** 07:27 And it was old and it was like, you need to update because I never write software.
**Juliano Costa | Datadog** 07:34 Mmh.
**Fabrizia Rossano** 07:34 So, yes, you only need Dockers if you have an environment that is fully configured. If, like, you're a product manager, and… and I'm saying this from a person that is not a developer, but you still want to run this to show Oh.
Like what the benefit of open telemetry would be.
the setup is pretty burdensome, because I have to.
And…
**Juliano Costa | Datadog** 08:04 Yeah, no.
**Fabrizia Rossano** 08:05 No.
**Juliano Costa | Datadog** 08:06 Any any suggestion is welcome. Yes, please. Yeah, I thought I thought we we have, because The demo has… 12 different programming languages.
**Fabrizia Rossano** 08:20 Yes.
**Juliano Costa | Datadog** 08:21 And I… You do not need to have all of them installed on your machine. I think for Node, it may have one or other script that actually checks some stuff.
But in theory, you would only need Docker and resources because the demo is heavy. So if you have CPU memory and Docker.
**Fabrizia Rossano** 08:45 Plenty. And maybe I just made some, like, did something wrong following the instruction.
And… I forked somewhere, and it went…
**Juliano Costa | Datadog** 08:56 This is actually perfect. This is the type of feedback that we need because you came with a totally new perspective and it failed. So our docs is wrong. The way that we are explaining is wrong. So please.
**Fabrizia Rossano** 09:13 I don't like.
I'll remove everything, I'll do it again, follow the same path, I'll document this, and I'll write a proposal. So that's my plan for next week, because it was kind of like… I'm lost, I cannot work, and I was two hours in, and I'm like, what? It's not working! And then I didn't have time, so, I'll do this.
**Juliano Costa | Datadog** 09:40 Okay, thank you. Yeah, I appreciate that.
**Fabrizia Rossano** 09:43 No worries.
**Juliano Costa | Datadog** 09:50 I also see that you and Perk added a note here to discuss next week or today.
**Fabrizia Rossano** 09:57 Yep.
**Juliano Costa | Datadog** 09:58 How we can collaborate better with the hotel blueprints.
**Fabrizia Rossano** 10:03 Yeah. Oh, okay.
**Juliano Costa | Datadog** 10:04 I think that came from the Dan's message, right, on the… Yeah.
**Fabrizia Rossano** 10:10 It's like, I see a lot… and maybe it's just me. But there's a lot of overlap between the blog post and the blueprints like the blueprints are kind of a shrinked version.
more technical of the blog post that just extract the information. And so I thought, since we have a lot of blog posts already. Maybe we can feed them something for creating more blueprints, or we can go there and help.
**Juliano Costa | Datadog** 10:43 Okay.
**Fabrizia Rossano** 10:44 Talk to them, Maurice, and.
**Johanna Öjeling** 10:46 The blog posts have been added as reference implementations. So they make the distinction that a blueprint is like a living document and it's like a pattern. And then there are reference implementations that are Publish, like, once, so they may become obsolete at some point, but it's, like, how actually organizations…
**Fabrizia Rossano** 11:12 Okay.
**Johanna Öjeling** 11:12 implement open telemetry. So the blog posts have, like, served also as the first, number of reference implementations, but correct me if I'm wrong, Juliana and Tristan, but I think these blog posts, like, when this initiative started with conducting the interviews and writing the blog post, then the blueprint project hadn't really been started, or it hadn't reached very far, so that's why The first interviews that were done weren't, like.
sync to with the reference implementation template. So that's… yeah, but… from now on, if we do more interviews, yes, it would be good to, follow Dan's recommendation and, target these towards reference implementations.
**Juliano Costa | Datadog** 12:08 Exactly. Basically, those interviews predate the creation of blueprints.
But that that actually brings no go ahead.
**Fabrizia Rossano** 12:20 No, I just was wondering if is there any of this.
blog posts, these interviews that have not been translated into blueprints yet.
Because,
**Juliano Costa | Datadog** 12:33 I don't know.
**Fabrizia Rossano** 12:35 Okay, I can go and ask and investigate and ask Andre because it's on the blueprint project.
**Johanna Öjeling** 12:43 Yeah, I think, like, I think we have published three blog posts, and all of those three have been also added as reference implementations.
**Fabrizia Rossano** 12:52 Good.
**Johanna Öjeling** 12:53 So I think also the Atlassian one and the Keycloak one will probably also get added to that.
**Fabrizia Rossano** 13:01 Hmm.
**Johanna Öjeling** 13:01 Bye for right now.
**Fabrizia Rossano** 13:03 Thanks.
**Juliano Costa | Datadog** 13:06 But what I wanted to say is that this actually brings back the discussions that we were having.
What is the plan for?
for the next steps of this group.
I… Didn't have time to take a look again on the trace verbosity thing after the topics that we discussed two weeks ago or even more.
The demo is taking all my time of my life. I need to release a 3.0. Everything is broken. But yeah, I'm kind of — Lacking help there, so it's just me trying to… Solve everything before publishing, so, yeah.
We have two maintainers that changed jobs, so they are in the onboarding process, so yeah, all of that, things, and yeah, I understand that, Maintaining the demo may not be their priority at the moment.
That's why I'm on my own.
But I, whenever I release, I hope to have something for the demo.
by the end of this week, so then I'll go back to the trace verbosity.
Which is one of the options that we wanted to tackle. There is the documentation as well.
And the other one that we haven't — we don't have a draft yet.
We…
**Johanna Öjeling** 14:51 She's.
**Juliano Costa | Datadog** 14:52 Fair enough.
**Johanna Öjeling** 14:52 Interviewing these six or running a survey.
**Juliano Costa | Datadog** 14:57 Yeah, exactly. Yeah. Interview six to see what they are doing different, what they are doing, why they are doing different from respect.
Yeah. So that's it.
One thing to to everyone. Cncf came to to the project, and mentioned that we will need to change all the Zoom Links, all the meeting links.
So, if you are like me, and Just cloned the meeting to your own calendar.
Whenever we have an update that hopefully we will be notified when they update the link, you will need to update your own calendar because it's not actually reflected.
I have the OpenTelemetry calendar on my Google Calendar, but I just cloned the two SIGs that I joined. Otherwise, I would have a bloated calendar with all the SIG meetings, and I don't want that.
And the thing is that whenever the OpenTelemetry calendar updates, my… The cloned one doesn't. So yeah.
**Johanna Öjeling** 16:16 Okay, yeah, thanks for…
**Juliano Costa | Datadog** 16:17 Just,
**Johanna Öjeling** 16:20 But is there anything… is there anything we need to do to update the… all… Yeah, they.
**Juliano Costa | Datadog** 16:26 No, GC will take care of that.
I think for this meeting, the GC liaison is Austin. So most probably Austin will update and then let us know.
**Johanna Öjeling** 16:38 Okay.
Thanks.
Yeah. And about the, documentation template proposal and trace verbosity. My bad with is also a bit limited now and starting a new job. Yeah. Onboarding. So.
Just for your awareness.
**Juliano Costa | Datadog** 17:11 Okay, then I think we can maybe take this time that we have left and maybe go and review the blog posts.
**Johanna Öjeling** 17:22 Yes.
**tristan** 17:23 I had to ask for… I requested access to them, so hopefully I get that soon. I don't know.
Which one? Both of them for Key Cloak and… the Atlassian one.
**Juliano Costa | Datadog** 17:36 I can add you, I think. Tristan… the… send?
So.
**Johanna Öjeling** 17:49 I want The access expired on the…
**Juliano Costa | Datadog** 17:54 Well, next year.
**Johanna Öjeling** 17:54 this document.
**Juliano Costa | Datadog** 17:56 the…
**Johanna Öjeling** 17:57 Because I see some of the, yeah, because the initial reviewers like Neil from Skyscanner and Bogdan from Adobe, they're not there anymore. They don't have to be there since they're published.
**Juliano Costa | Datadog** 18:11 Yeah, I don'.
**Johanna Öjeling** 18:12 Thank you.
**Juliano Costa | Datadog** 18:13 So this one I created on my Datadog account, and I don't know if they have some policies that.
**Johanna Öjeling** 18:19 Oh.
**Juliano Costa | Datadog** 18:20 Fol.
**Johanna Öjeling** 18:20 Okay.
**Juliano Costa | Datadog** 18:21 Sorry about that. I will try to create on my own Gmail account for the next ones.
Because, yeah, I do… like, Perk is not here anymore.
Fabrizio is, Johanna is, Tristan is, I just invited.
Yeah.
But, like, all the others are not.
So yeah, this is.
Interesting.
Oh.
I just shared with you both of them, Tristan, you.
You should have, access.
Yeah, okay, let's try to… Any preferences on order? First Atlassian, and then KeyClock? Because then we kind of wrap up all the… Users that we interviewed, or… All the companies, and then we talk about the project.
Or… We go key clock, and then Atlassian.
add.
Just asking, right?
**Fabrizia Rossano** 19:39 Alphabetical Atlassian key clock.
Has anyone…
**Juliano Costa | Datadog** 19:44 Oh, we started with mastodons.
**Johanna Öjeling** 19:47 Okay.
**Fabrizia Rossano** 19:48 Well, at least for the list for the last two, because at Skyscanner there should have been.
**Johanna Öjeling** 19:55 Yeah, I don't think I have a preference either, so we can do it whenever the first one that gets approved by all involved parties. It might be faster to get Keycloak approved, since the external, like, the interview, the people who interview already approved, where for Atlassian, we're still… I don't… did you give a video of the contact details, Tristan, to… James, I think, was his name.
**tristan** 20:21 Oh, I gotta find it.
**Johanna Öjeling** 20:22 He needs to be added to, yeah, the document.
**tristan** 20:25 Yeah, I'll get.
**Johanna Öjeling** 20:26 So I think Keycloak will be faster too. Yeah.
**Juliano Costa | Datadog** 20:32 If you, if you can pass the… the… his contact to me, I can invite him to the dock.
So then he can access that.
Cool.
Cool, cool. And, I also see here on the list, we have Grok, Did we? Did we publish? No, right? It was not.
**Johanna Öjeling** 21:01 No, yeah, exactly. So the Grok one, I wrote the draft and reached out to Andreas, but then he was in the situation where he had moved to Nvidia and they're in this like strategic partnership with Grok.
The blog post is about Grok, so he involved… some legal person from Grok, but I tried to contact them several times, and they never… you know, responded. So yeah, I can ask Andreas again how he wants to proceed since.
yeah, I still can't get in touch with this person who wanted a pearl from.
**Juliano Costa | Datadog** 21:45 Yeah, it would be sad to lose the story. It's like the title is pretty catchy. One engineer, 12,700 collectors.
**Johanna Öjeling** 21:55 Yeah, and I think they had some really interesting use cases also with the Prometheus exporters and yeah, monitoring.
After, yeah. Yeah.
**tristan** 22:10 Okay.
**Juliano Costa | Datadog** 22:10 Okay.
**Johanna Öjeling** 22:12 So yeah, I also, it would be sad to not get it out there.
**Juliano Costa | Datadog** 22:18 Mmhm.
**Johanna Öjeling** 22:19 But yeah, I'll reach out to Andreas again.
**Juliano Costa | Datadog** 22:22 So I'll add here to-dos — not here. I'll add to-dos here to our meeting notes.
Reach out to Grok.
And… review. Okay.
blog posts.
Oh.
And also, yeah, James contact.
James… James what? James Moses?
Thank you.
Yep.
Cool.
Cool. On the key clock interview doc.
Let me just take a look on one thing. Perfect. I was just about to tell Fabrizia to add her name on the review tracker.
Oh.
Okie dokie.
I think we have… Everything that we need.
Anything else anyone.
**Johanna Öjeling** 23:55 Okay.
**Fabrizia Rossano** 23:56 We're all good.
Thank you, bye!
**Juliano Costa | Datadog** 23:59 Have a great.
**Johanna Öjeling** 24:00 Thank you, have a good day.
**tristan** 24:01 But.
**Johanna Öjeling** 24:02 Cheers.
**Juliano Costa | Datadog** 24:03 Cheers.
