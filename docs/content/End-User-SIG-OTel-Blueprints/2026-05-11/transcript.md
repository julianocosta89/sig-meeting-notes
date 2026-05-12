SIG: End-User SIG: OTel Blueprints
Date: 2026-05-11
Duration: 58 minutes
============================================================

## Zoom Recording Transcript

**Dan Gomez Blanco** 02:09 Hello?
**Tiffany Hrabusa** 02:12 Hmm.
**Dan Gomez Blanco** 02:14 But you're here with all the note-takers. I'm going to, log in… Claim post.
Okay.
Welcome back.
**Tiffany Hrabusa** 03:17 Thanks.
**Dan Gomez Blanco** 03:20 Mmm…
**Tiffany Hrabusa** 03:27 I haven't had a look.
at anything.
**Dan Gomez Blanco** 03:30 That's, that's okay. It's okay.
Mmm… I think, lucas.
Certainly would be 15 minutes late.
She's okay, we can talk about hotel graduation.
**Tiffany Hrabusa** 03:55 That's exciting.
**Dan Gomez Blanco** 03:57 Exciting.
**Tiffany Hrabusa** 03:58 It is.
**Dan Gomez Blanco** 03:59 that.
**Tiffany Hrabusa** 04:00 Everybody is talking about it, except OpenTelemetry.
**Dan Gomez Blanco** 04:04 I did post something, but yeah.
**Tiffany Hrabusa** 04:07 No, I mean, that's what I mean, it's like, all individuals, everybody's talking about it, but Open Telemetry hasn't said anything, because we're waiting for the GC, and I think they want to time it with whatever… announcement CNCF is gonna make, so…
**Dan Gomez Blanco** 04:21 Yeah, yeah, that makes sense.
I mean, yeah, I guess.
People build the anticipation.
We're just, we're just hyping it, really.
**Tiffany Hrabusa** 04:37 There you go, there you go.
**Dan Gomez Blanco** 04:39 Mmm… Alright, let me open the… the notes.
**Tiffany Hrabusa** 04:59 We've actually made really good progress.
**Dan Gomez Blanco** 05:02 Yeah, yeah, there has been quite a lot of progress.
M… And actually, I'm gonna share this link.
Just realized I need to make this…
**lciukaj@splunk.com** 05:58 Hi, Jen. Hi, Tiffany.
**Dan Gomez Blanco** 06:00 Hello!
**Tiffany Hrabusa** 06:01 Fresh.
**lciukaj@splunk.com** 06:02 Happy Monday!
**Tiffany Hrabusa** 06:04 Happy Monday.
**Dan Gomez Blanco** 06:07 Happy Monday.
I thought, you were gonna be 15 minutes late, but .
**lciukaj@splunk.com** 06:13 Yeah, I wrapped up. Actually, my call was canceled, but I had to finish something, so I'm just 6 minutes late.
**Dan Gomez Blanco** 06:21 Very good, very good.
**lciukaj@splunk.com** 06:25 I was thinking one of my colleagues from Splunk will join, because I had an interesting discussion last Friday. One of our OpenTelemetry contributor, Kyle, he pinged me that there is some internal initiative at Splunk to write on… to work on the blueprints.
And what we do, and how to align it, if it's possible to have, like, more, like, upstream blueprint, and then the vendor blueprints.
And if that is something that we are discussing, I said, rather, we didn't discuss that, but sounds like a good idea, maybe, for future. So he said that he will join our bi-weekly call to discuss this, but so far I don't see him, so maybe next time he will join.
**Dan Gomez Blanco** 07:06 Cool. Yeah, that's good. That would be a good, good, good topic to discuss. I think we briefly touched on that when we were at KubeCon.
**lciukaj@splunk.com** 07:15 Yeah, that would be difficult, in my opinion, because, Yeah, technically, when we work on our upstream blueprint, the general blueprint, we would need to be, like, very, like, general, don't, you know… and think ahead about some features or solutions that maybe vendors… vendor implementation do not support. I don't know. I think that is a classic, right? It's… It's similar to the regular features that we have in upstream, you know, distribution, but anyways, like, I'm open to discuss that. So far, it's not part of our plan, but maybe we can open that for future.
**Dan Gomez Blanco** 07:51 I think right now, it's better to focus on the ones that we've got.
And progress, and get the… get the… I think, you know, get the workflow Established, and .
**lciukaj@splunk.com** 08:04 Dean.
**Dan Gomez Blanco** 08:07 Alright, I think probably that'll be us for today.
I'll go and share my screen.
**Tiffany Hrabusa** 08:15 While Dan is doing that, Lukash, I… would just want to apologize, I have been completely… Offline, from a… hotel perspective for the last week, and I have not had a chance to review anything that's come in over that time, so I will get caught up shortly. I know you have a blog post up, and you have the, the blueprint, so…
**lciukaj@splunk.com** 08:37 No worries, that's okay. So, blog post, it's… there was, someone from SecuritySeq reviewed that and provided comments, so I already responded to that, so I think that's now… it requires the final review from your side, and I believe that will be ready to be published.
**Tiffany Hrabusa** 08:54 Okay, I'll take a look this week, for sure. Hopefully today, but we'll see.
**lciukaj@splunk.com** 08:59 Thank you so much, Stephan, I appreciate it.
**Dan Gomez Blanco** 09:00 That's… that's not this blog post, right, whether we're talking about.
**Tiffany Hrabusa** 09:03 No, and I haven't even looked at yours, Dan. Like, I'm…
**Dan Gomez Blanco** 09:06 Right. That's okay, yeah.
**Tiffany Hrabusa** 09:08 I'm so far behind.
**Dan Gomez Blanco** 09:11 You're only human.
Yeah, but I guess, you know, let's talk about… in that order. I mean, now that we're talking about the blog post, I think, you know, the blog post is probably ready… to be reviewed from the perspective of copy edit, I think. Yeah.
what I was trying to achieve with this is just… Introduce why we're doing it.
It's actually a bit… longer than I thought I would write, but then I started writing, and I was like, actually, you know, I think… You let me know. I think it makes sense to introduce it in this… in this frame, and then ask for contributions, but, like, if you have any comments, I think it's… I don't know, it's too long, then I'll…
**lciukaj@splunk.com** 09:52 No, I think that it's okay from the, you know, the size perspective, and I provided my comments, and I really like the mermaid diagram that you added. It's actually what I was looking for, and I… think that the end users, they tend to be, like, more, you know, that they like this, you know, simple diagrams, if they want to scroll and see something very quickly, and this one is very useful, like, okay, I have an idea, what should I do next? So instead of reading, like, a couple of programs, I can take a look into the diagram, and I know what is the goal here.
**Dan Gomez Blanco** 10:25 Sounds good.
**lciukaj@splunk.com** 10:25 This is a good one. Love it.
**Dan Gomez Blanco** 10:28 Awesome. Alright, so…
**lciukaj@splunk.com** 10:30 Can you get back to that, the mermaid? There is something that came to my mind, because the reference architecture can be linked to the blueprint, right? So we could perhaps maybe put some arrow here, or reference, what do you think?
**Dan Gomez Blanco** 10:49 Yeah, I mean, we've already got this.
**lciukaj@splunk.com** 10:52 Oh, right. Okay, gotcha.
this is here, then we are fine. I was thinking maybe in this, And the last one, because we want to share reference implementation…
**Dan Gomez Blanco** 11:06 I guess, you know, there would be, like, yeah, I mean, this will… These two are… what I'm trying to say here is, like, they are… They are effectively the two processors of, contribute in a reference momentation or a blueprint. Are… independent.
Right, you don't need to do one.
That's why I tried to keep them separate.
**lciukaj@splunk.com** 11:30 No, what I think is that in the second phase, the second process is, like, from the end user perspective, okay, want to share reference implementation. OpenSync end user, collaborate to craft and review reference implementation.
and a reference implementation is published. But what if we have already the blueprint where this reference implementation could be linked to. Should it be part of this process, or that will be sorted out during this review, reference implementation, etc? Maybe…
**Dan Gomez Blanco** 12:01 Yeah, I guess that would be here in the Collaborate to craft it, I guess, you know.
**lciukaj@splunk.com** 12:05 Exactly. Maybe… you can put some comments in the brackets, like, if the blueprint already exists, this reference architecture will be linked there, or something like that, you know what I mean?
**Dan Gomez Blanco** 12:16 Or the opposite, or basically the blueprint.
You know, basically someone that is… collaborating to craft the blueprint that will… you know, these will feed into that as well, so I don't… it's like, I don't know where I would put it, because.
**lciukaj@splunk.com** 12:29 Maybe… Maybe don't overcomplicate it, I think, okay.
**Dan Gomez Blanco** 12:35 Ultimately, I think, you know, it's this set of steps, right, that people either want to share a blueprint or get a blueprint, and then open an issue.
Which I think that was the most… perhaps, like, we haven't done it yet.
But I don't see why not, that people could say, hey, you know, I would… like, a blueprint for this, and then I'm not ready to write it, but I've got an idea. I was like, okay, well, that's… I think that's valid. And, yeah, for reference implementations is… It's a bit more like… We cannot do something.
we're gonna do anything without the input from the person that's sharing it, right? I mean, we could help them write it, but, like… If someone, you know, if… Yeah, if we don't have that input, then… Won't be able to do anything.
**lciukaj@splunk.com** 13:24 Yep.
Alright.
**Dan Gomez Blanco** 13:25 Okay, cool.
What else?
Emm… Yeah, so let's talk about your… blueprint, then I've had an initial look, Yeah, so… I guess this PR.
**lciukaj@splunk.com** 13:50 And one more comment from my colleague from Splunk. So he reviewed that, and he said why we don't have, like, some YAML sample configurations. He was a bit confused why we don't go deep dive with these recommendations, etc. And I said.
Our goal is to have more, like, general, high level, we don't want to go with this.
Specific. That's good. Yeah.
**Dan Gomez Blanco** 14:14 And I think it's a good question. I think, you know, like, There should be… And this is something that I wanted to discuss as well, is like… what level of detail do we need, right? I think the… you can be… very detailed, and this is not what this is supposed to be. We're not supposed to be rewriting any other form of documentation.
But at the same time, I do think it's, we need to add detail about the reasoning behind it sometimes. As in, like, you know, why is it that we're… what is it that we are, proposing a certain recommendation? And I think, you know.
And if you say…
**lciukaj@splunk.com** 14:57 Yeah.
**Dan Gomez Blanco** 14:58 Yeah, we are recommending doing this, and this will help you, you know, dry this particular… Behavior of this particular, you know, optimization.
**lciukaj@splunk.com** 15:11 I've seen a couple of comments from you, like, can we be more precise, can we provide more details? So, I agree with you, like.
there was one question, and it was a good one, about the available collector distributions, which I put there, and then I realized, okay, that's… when I would be the end user reading that, and I read that sentence, for me, it's like, okay, so give me the list, or give me the link to the list of available distributions. So, I think we need to be, like, careful with what we are also, you know.
Including in the blueprint.
**Dan Gomez Blanco** 15:47 Yeah, so I guess, for example, like, what I mean is here, in this… when we say, like, okay, I understand that, you know, the… The recommendation, or the action, basically, is to enforce resource and attribute… attribution and correlation standards.
So, here we've got a checklist that says, you know… sorry, this one in particular, no, this is… because this one in particular is about having a… The output of this is basically a recommendation that you can do in… or a document that you can… You can review. But in… there was one… Or was it, Oh, no, no, this, no, this is the… this is, number 5. Yeah, so here, for example, like, you know, we've got the… the recommended resource attributes, but then… how do we actually go… I mean, this would be my question as an end user, right? How do I go and ensure that the application telemetry includes at least that? It's like… There's, you know.
injecting the standard resource attributes through SDK configuration, then I think here, maybe, like, what we can do is, like, explain… expand a little bit more on… how you would… maybe we can use an appendix here to give an example of, like, how you would do that in a particular you know.
I don't know, maybe… I was thinking a particular language, but maybe not. Maybe what's better to do is, like, expand and say, and this is how you would configure the SDK and link to that in here. So, like, okay, and this is how you go and… use the open tele… well, no, the operator or not, but, like, how… this is how you would go and… Create… a Docker image or a script that initializes the SDK, and these are the environment variables that you need to.
**lciukaj@splunk.com** 17:40 The thing is that for each checklist, for each section, we should have this reference to the appendix, and some kind of…
**Dan Gomez Blanco** 17:49 Yeah.
Here's a… here's a question maybe for Tiffany.
As well, in terms of, like, one of the things that I found reading is that… We've got the… so at the moment, we've got the, sort of, like.
The action, and then we've got some documentation And then we have that over there. I can see how this can be, like, all the links are in one place.
but also… If this becomes, like… more expanded, then… how do you reference that over here? As in, for example, like, that would apply… OpenTelemetry semantic conventions, how does… and what… which one of these does it help me, right?
Mmm…
**Tiffany Hrabusa** 18:34 Yeah, the links… The links are most useful.
In context, But… There is the argument that by clicking the link, you pull the user out of the flow of the blueprint.
So, it's like, do you… I guess, do we expect people to read through this kind of all at once, to get a sense of what the flow is? In that case, maybe the links at the bottom is fine.
Do we expect that they're gonna… Jump around a lot, kind of, like, take it section by section, and, you know, being pulled out to the docks is fine, because they'll come back and work on another section later.
my personal preference is to keep things in context, but there are those who would say that, Having a link in every sentence.
is disruptive to the… to… to the reading experience, so…
**Dan Gomez Blanco** 19:41 I… I would say that I prefer them in context, too, because I've… I mean, maybe this is why I found reading this, is that the, Then when I came to the links, I didn't really know where they would… What part of this would they apply to, right?
For example.
**Tiffany Hrabusa** 20:01 Yep.
**lciukaj@splunk.com** 20:03 So what do you think? Should we keep this as it is, with the subsection documentation, or try to put it in context for the particular bullet?
**Tiffany Hrabusa** 20:14 I think… Go ahead, Dan.
**Dan Gomez Blanco** 20:18 I was gonna say, I'll vote for Putin in context, or at least put in a… I don't know if you can do that, like, the… 1, 2, like, I don't know what the name for that.
**Tiffany Hrabusa** 20:27 Oh, yeah, footnote kind of thing.
**Dan Gomez Blanco** 20:29 No style.
**Tiffany Hrabusa** 20:32 Even, I mean, even footnotes is kind of a bad user experience, if we're talking about that. I would prefer just to have, like.
The text within the sentence become the link.
I think that's fine. I think that you might come across a couple links in that reference list that don't correspond directly to something in the bulleted list, and those you could keep as reference.
But if there is, something within, you know, the sentence that you want to link directly to, that's what I would do, and I would then remove it from the reference list below.
And maybe… I forget… so it says documentation, so you could say, like, additional documentation, or something like that.
**Dan Gomez Blanco** 21:19 And that would be… That'll be good.
Yeah. So I guess, for example, here, when we're talking about provide pre-baked images and service container definitions for containerized deployments.
Yeah, if we were to expand here on this and say… And then, you know… if I were to pick this up as an end user, and go, like, well, okay.
I get the point.
I need to use that, but then… how do I actually configure?
the OTEL SDK.
And this is the part that we don't need to rewrite here, right? That we can just link.
to the SDK configuration for… You know, and then, not for each language, but in general, like, you know, this… there's a part of the dog.
**lciukaj@splunk.com** 22:03 If we don't… what if we don't have, like, documentation matching to that pool, like, should we write this?
Appendix, or… Now, the thing is, how I see that done is, like, I don't want this to be, like, overcomplicated. Like, for me, this might be… this should be lightweight document, like, okay, I read that, I learned something, I know where should I go, what should I check or discuss.
I'm… I don't know, that's my understanding of Blueprint, like… I don't know if we… if we start… providing examples, samples, appendings, if we don't, like, overcomplicate it, and then maybe there will be negative effect as well, or negative impact on next blueprints, because other contributors can see that, okay, that's too complex, I don't want to even start working on this.
Something like that. That's how I see it. I don't know if you agree with me or not.
**Tiffany Hrabusa** 23:01 Nope.
So, I kind of see… like, the reference implementations being the detailed portion. And of course, that's going to be very specific to the environment, but I'm not an end user, but I would expect to see YAML configurations and, like, specific parameters in the reference implementations, and not… In the blueprint, necessarily, unless it's something universal, like that, you know, a flat.
**lciukaj@splunk.com** 23:32 I heard.
**Tiffany Hrabusa** 23:32 Something that you would definitely always use.
So I agree, I don't think we need to complicate it. But I think… the concern is, is someone going to read this and say, yeah, but how do I do it? Like, the idea with the Blueprint is that they should know where to go and how to get started on this stuff.
if we don't have documentation for something.
That's obviously a gap in our docs.
**Dan Gomez Blanco** 24:05 I would agree with that. I think, you know, for example, here, what I would… maybe this is, like, one of the things that we should have, Like, that being the test, right? So, saying, okay, so… Do we have a follow-up? I don't think we need to cover here how one would create a pre-baked image, or… and also, like, in the OpenTelemetry space, we wouldn't be talking about creating images, because it's not a no-tail thing, right? So, but however, we're saying configuring the SDK, or publish, you know, I think here, what I'm missing here, for example, is, like.
how do we link this to… well, you can create… you can give an example, like, not an example, but saying, like, hey, you can configure your pre-baked images with tools like, you know, Packer or equivalent, blah blah blah, and in the setup script, you can… M… You can then use… any form of OpenTelemetry SDK instrumentation, like like, the ones included here, and then you link somewhere out. Like, you don't really explain how to actually configure the SDK, but, like, give people that.
the actual… follow-up after, you know, from this blueprint.
**lciukaj@splunk.com** 25:19 Okay, I'll think about this.
**Dan Gomez Blanco** 25:23 Sounds good.
**lciukaj@splunk.com** 25:25 So, what are we missing here, like, from… what do you think? Like, where are we in terms of getting this, you know, public? Like… So…
**Dan Gomez Blanco** 25:34 Yeah, so again…
**lciukaj@splunk.com** 25:35 I think that checklist part, to provide, let's say, some next steps, or details, or samples.
and then get the review from collector and OpArmp team, correct?
**Dan Gomez Blanco** 25:50 I think so, yeah. I think that's… that's pretty much it. I think the, I don't think we require… The reason why I tagged the OPAMP and the hotel collector folks is that we, this is… Heavily geared towards those two components.
Mmm… I was arguing maybe, like, the SDK part, but, like, you know, I think that should be it. Also, like, let me ping… I will ping, Riley, as well, to have a look at this. Riley being the TC, sponsor, the technical committee sponsor for this, For this effort. So, yeah, it'll be good to get his point of view as well.
And then… Yeah.
get a little bit more consensus with the actual maintainers and the TC.
**lciukaj@splunk.com** 26:49 Absolutely, that is super important. So, I'm not sure, maybe better to ping them and ask for review, because I'm not sure how this tagging works. Perhaps they are busy with other stuff, and maybe they treat it as a low priority, so we can get that.
**Dan Gomez Blanco** 27:03 Yeah, I can… I can… I mean, we can post it in the… In the specific Slack channels as well.
**lciukaj@splunk.com** 27:10 App channel is a good idea, yep.
Do you want me to take action on that, or will you overdo it?
**Dan Gomez Blanco** 27:17 If you want to do it, that would be great, and I'll…
**lciukaj@splunk.com** 27:19 So I will follow up directly with them and ask for review for this blueprint.
**Dan Gomez Blanco** 27:23 And I will ping Riley to also have a look at this.
**lciukaj@splunk.com** 27:27 Cool. So we have next steps here.
**Dan Gomez Blanco** 27:30 Good stuff.
Mmm…
**lciukaj@splunk.com** 27:33 A deadline, or… When do you want that to be published?
Because I believe my blueprint is the most, like, advanced now, too, and most ready to be published.
**Dan Gomez Blanco** 27:45 Yeah, I think so. I don't know, I think it depends on, like, you know, people… on the comments from… from them, but hopefully, you know, I would hope that we can get this published in the next couple of weeks.
**lciukaj@splunk.com** 27:58 That would be great. So, I'm, like, fully committed to that, and I would like to complete this. So, once we have a review from them, I will address all of the comments, and I will try to find out a way for expanding a bit that checklist part to be more, like, intensive.
**Dan Gomez Blanco** 28:14 Sounds good.
**lciukaj@splunk.com** 28:15 Awesome.
**Dan Gomez Blanco** 28:16 And another one… I guess, you know, Alex is not here, but I saw that he commented something on the Kubernetes one.
As in, like… Yeah, on the PR, I've not had a look at, at it yet.
No. I guess that… yeah.
So, on that one, I was gonna say that… be good to get. That is a… is this a different… there's a different challenge there, which is that the… So the Kubernetes semantic conventions SEG is now basically stabilizing the semantic conventions for Kubernetes. So the… and that includes, as well, the instrumentation that we deploy… that we deliver with the collector.
And I'm of the opinion that we should probably be… opinionated here, and say, you know, this is the way that we recommend instrument in Kubernetes with OpenTelemetry even if… This is the new way of doing it.
I don't see much.
Value and, like… having a blueprint now that says, you need to deploy CubeState Metrics, and you need to deploy Node Exporter, and then have these components, like, you know, being created by this and that.
And then in… two months' time, completely change and say, you don't need KubeState Metrics, you don't need Node Exporter, you just… you can deploy an OTL collector, and it will do everything for you.
So, I think, yeah, don't know… I have not had a chance to look at what, Alex… .
**lciukaj@splunk.com** 30:08 I think he started reviewing or answering the to the questions, or to the comments, so it was just initial response to the review. I'm happy to review it once he addresses your comments.
**Dan Gomez Blanco** 30:24 Nice.
**lciukaj@splunk.com** 30:25 I didn't want to, you know, confuse with another review. I don't know if that is even good practice in the open source, to have, like, two simultaneous reviews for the same document, or the same, you know, PR.
**Dan Gomez Blanco** 30:40 Yeah, I think that is… it's good. I think, you know, the more… There have been, I mean, I don't know, I can pull some of the PRs for OTEPs.
They have hundreds of comments.
Okay. Yeah.
**Tiffany Hrabusa** 30:55 Yeah, ideally we could work one by one, but… That's not really… Not really how it goes.
**lciukaj@splunk.com** 31:05 Great loan denial? Okay.
**Dan Gomez Blanco** 31:07 It's okay, yeah.
Okie dokes. And then I started, apart from that blog post, I also started to work on… this, which is the… I started to work on it, as we said previously, just as a doc… that I plan to share at some point. I wanted to just give, Mmm… right, okay. Yeah, I just wanted to give this a first round of reviews, just to get the… The common challenges.
section, reviewed. So I think, you know, the… The sooner I get feedback on this, the better, right?
So, I'll share it in the channel as well, in the Slack channel. It's in the notes. But if anyone wants to drop some comments there… on the common challenges section, anything that may have been missed, or in what we're trying to achieve here, maybe some ideas on things, problems to solve, then I would appreciate it. I also have some stuff here to… Say that I'm missing diagrams already.
**lciukaj@splunk.com** 32:11 Do you want to get the review in the Google Doc, or you will open PR and some comments there?
**Dan Gomez Blanco** 32:19 Google Doc, I think the Google Doc first, I think, is good too.
**lciukaj@splunk.com** 32:22 Okay.
**Dan Gomez Blanco** 32:22 you know, the moment that we get to the PR is a… is a lot more… I guess, just copy-edit and… Okay. And the last comments, I think.
**lciukaj@splunk.com** 32:34 I mean… Please share link in the document. I'll take a look at this.
**Dan Gomez Blanco** 32:38 Cool, awesome. I'll share it in the chat later, in the Slack channel.
But it's in the NOX as well.
**Tiffany Hrabusa** 32:45 So that is the third blueprint, right? So…
**Dan Gomez Blanco** 32:51 Yep.
**Tiffany Hrabusa** 32:52 Wow.
Am I throwing a button?
**Dan Gomez Blanco** 32:56 So, yeah, so I think, you know, we'll have these three, and I think people have already been… I guess, having ideas about others.
**lciukaj@splunk.com** 33:05 I have one more idea as well, but I need to put it on hold. I'm a bit busy now. So, the one for industrial systems, and specifically, I've been working a lot recently with… Modbus, OCP, UA, like, you know, there's these industrial protocols, we don't have, like, a good… OpenTelemetry coverage there yet, but there are some works being done, like the private repos, etc.
I think that's a good idea, that maybe there will be some progress for, you know, open telemetry enablement. So, I think we are not yet there to have the blueprint, but I have it in mind, so at some point, I will start working on this.
**Dan Gomez Blanco** 33:49 Yeah, I think, if we try to follow the process that we've got now in the how to contribute.
Perfect. And that would be… yeah, so ideas for that… for that, there's the… Prometheus interoperability, that's why, I think that deserves… its own blueprint.
**Tiffany Hrabusa** 34:09 We've been making progress on it. Our mentee is… setting up VMs in, AWS, and… she's going to try building her own collector distribution with OCB. All of that is, necessary for understanding the recommendations that we would make for guidelines and implementation, so… We've narrowed down the challenges. Yeah, it's… it's looking good.
**Dan Gomez Blanco** 34:39 Nice.
**Tiffany Hrabusa** 34:40 We're work… we're kind of doing it a little bit backwards, because we want to work with her through the technical components during the mentorship itself, but then we'll follow the contributing process.
The other interesting thing is that there is a yet-to-be-published interview that was conducted by the developer experience SIG.
That will be a reference implementation of this blueprint. So, we'll actually have our first, crosslink.
**Dan Gomez Blanco** 35:12 Nice. Yeah. Nice. I think, I was planning to put the… At least for this one.
For the centralized cloud-native telemetry platforms.
This is actually, like, less, At least this guy is Scanner 1, I know that very well.
So, Yeah, so I think at least that's part of it, or at least follows part of this. And I'm assuming that, I think.
all the other ones, like Adobe.
And Mastodon will be following a lot of this advice as well, so I think I might be able to link those.
That sounds cool.
Okay. Good stuff.
Hey, Alex.
**Tiffany Hrabusa** 35:59 Hey, Alex.
**lciukaj@splunk.com** 36:00 Some idea that I have.
**Alexandre Ferreira** 36:01 For the demo.
**lciukaj@splunk.com** 36:03 There was one, and… article or blog by Lockheed Martin, published, I believe, 2 years ago, about their OpenTelemetry story. So there is no, like, outer of that, but perhaps if someone, OpenTelemetry, knows who published that, and if we still have some relationship with Lockheed Martin Team, maybe we could reach out and check with them, if they would be happy to work on the reference architecture that would fit into one of these blueprints.
I think that would be a good, good idea.
**Dan Gomez Blanco** 36:33 So… It was a…
**Tiffany Hrabusa** 36:34 blog post from OpenTelemetry?
**lciukaj@splunk.com** 36:37 Yeah.
I can find it, I believe, Lockheed…
**Tiffany Hrabusa** 36:41 I can find it, I just wanted to clarify.
**lciukaj@splunk.com** 36:43 That's.
**Dan Gomez Blanco** 36:44 Again, that would be…
**lciukaj@splunk.com** 36:45 No, sorry, that was on CNC app, it wasn't…
**Dan Gomez Blanco** 36:48 That's what I thought it was. It was in the CNCF architect… End User Architectures.
**lciukaj@splunk.com** 36:53 But still, like, Lockheed Martin, enterprise operations choose hotel for better observability, so…
**Dan Gomez Blanco** 36:59 Yeah, I remember that.
**lciukaj@splunk.com** 37:00 So there's something that…
**Dan Gomez Blanco** 37:02 So something that we talked about with Alolita was, we should… bones… things between each other, like the CNCF and… so, for example, if there is a reference implementation that's shared within OpenTelemetry, we should at least recommend them to go and Share that with… the CNCF reference architectures that are more global.
And then the same for, I guess.
the other side, so if they see… anything on that side, so that they can just say, well, take part of your reference implementation that is related to a hotel, and you might want to share that with us, so I think we should… what I'm trying to say with this is, like, yeah, let's try to identify Who was in there, and yeah, we can ask them to contribute.
**lciukaj@splunk.com** 37:52 And the person.
**Dan Gomez Blanco** 37:53 What would be cool?
is that we could get someone, because all the reference architectures that we've got at the moment are Kubernetes.
M… Prometheus.
Hopefully soon.
this type of, like, centralized telemetry platform and so on. It would be good if we could get someone that… That is on the non-Kubernetes side.
**lciukaj@splunk.com** 38:17 I have one customer, but they, no, I… I… I… don't… I know them, and they will be not happy to share anything because of liability, and I… we even wanted to publish their story on our Splunk, you know, blog, and they refused. They said, no, we are not allowed quite… they are part of the bigger, you know, the group, and this parent group is not allowing for, you know, any cross-sharing information, so… so this is the only customer I have in mind. They have lots of Kubernetes implementations, But they will be not able to share, unfortunately.
**Dan Gomez Blanco** 38:52 Yeah, unfortunately, that's, very common.
common pattern.
**lciukaj@splunk.com** 38:57 But maybe once we publish the blog on the LinkedIn, maybe we can get some customers reaching out to us.
Oh, there is another one, it's, what was the… Airbnb. They had a nice open telemetry story. They shared that during the KubeCon last year.
**Dan Gomez Blanco** 39:18 Yeah, I think I actually do know the person there, maybe.
And it… I can't remember.
**lciukaj@splunk.com** 39:23 contacts there too, but I don't know if that is pure Kubernetes or if they have something non-Kubernetes, so we would need to check with them. They are very happy to share their stories, they have a couple of publications already on YouTube and others, so that is a good candidate to get some insights from them.
**Dan Gomez Blanco** 39:39 And eBay as well, if we spoke to, Vijay, like, that would be… Yeah. There are quite a few out there that I think have… actually, if you go to the adopters list.
talking about, yeah, so if we go to OTELIO, If you come to… sorry, Community.
that is… Where was it?
**Tiffany Hrabusa** 40:04 It's ecosystem, I think.
**Dan Gomez Blanco** 40:06 Oh, as an ecosystem.
**lciukaj@splunk.com** 40:09 end up there, same.
**Dan Gomez Blanco** 40:11 Some of them… have… blog posts already published, right? Which means that…
**lciukaj@splunk.com** 40:17 Hmm.
**Dan Gomez Blanco** 40:18 they're already… Happy to share it.
**lciukaj@splunk.com** 40:25 Interesting.
**Dan Gomez Blanco** 40:26 We could… we could reach out.
**lciukaj@splunk.com** 40:29 Yeah, we can then review that and try to find out what fits into the blueprints, and maybe we can check if we could.
Convert that into reference architecture at some point.
Good idea.
**Dan Gomez Blanco** 40:42 And, maybe, what we can do, Tiffany, is… We have these, that basically we tell people.
Well, we used to be, like.
We would only allow people to, like, put their name here if it had a blog post or something, then we've relaxed that restriction.
But it would… what do you think if we had an extra column? At the moment, it would be, like, 3 of these companies, maybe. But if we had an extra column for, Or maybe in the same column, but something that links to the reference implementation.
**Tiffany Hrabusa** 41:12 Yeah, I think that's a great idea.
**lciukaj@splunk.com** 41:15 Well, they can.
**Dan Gomez Blanco** 41:16 Do you want me to open an issue for that?
Yeah. On the website. I'll do it, yeah.
**Tiffany Hrabusa** 41:21 That'd be great. The other… And I haven't cross-checked this list with the one that I'm going to mention, but… I was reading through the, the graduation evaluation, and, you know, the TOC interviewed several end users of OpenTelemetry, and if they're not on this list, they may… they may also be willing to share reference implementation.
**Dan Gomez Blanco** 41:48 I think we picked them from this list. I think it's because we gave them… Yeah, we gave some… Users, basically.
During the graduation process, we… we gave him the list of users that… that he could go and interview, I guess.
I guess that was part of the thing, Or maybe they picked others that we didn't.
**lciukaj@splunk.com** 42:11 I need to drop. Someone is trying to get me on call, so I need to take it.
**Dan Gomez Blanco** 42:16 Okay. Right, okay, see ya.
**lciukaj@splunk.com** 42:17 Anyhow.
Gotcha. Bye.
**Dan Gomez Blanco** 42:21 But yeah, good point. I think they're over there, but not here.
I actually see some of… the customers that I work with over here, so I could… Definitely reach out through those channels.
This is why it's good to have, like, folks working with… within users, we can actually reach out through different channels.
**Tiffany Hrabusa** 42:45 Yeah, yeah, Alex, that would be great.
I think the more… the more we get, the more willing people will be to ride their own.
**Dan Gomez Blanco** 43:00 Sounds good.
**Alexandre Ferreira** 43:01 I can ask them if they're willing to share their architecture.
The only point is, if I'm not mistaken, the architecture that they use.
This is a bit unorthodox.
**Dan Gomez Blanco** 43:16 That's okay.
**Alexandre Ferreira** 43:17 He got to a architect.
**Dan Gomez Blanco** 43:20 Are you talking a specific?
**Alexandre Ferreira** 43:22 Yeah, so…
**Dan Gomez Blanco** 43:23 In general, yeah.
**Alexandre Ferreira** 43:27 And I'm on the phone, so my connection drops, that's because of it, but I'll be on my computer, and… Two minutes or so.
**Dan Gomez Blanco** 43:38 Cool.
There is this issue template, right, that people can use.
So… We have now, basically, the… if you want to point anyone to how to contribute, I reference implementation, this would be the place to do it.
There's this link here that explains how to do it.
**Alexandre Ferreira** 44:00 Good night.
Can I ask you a favor, can you send me this link on Slack?
Oh, yeah, yeah We have a few minutes, but, I saw your comments, Dad.
pool request?
And I agreed to all of them, if I'm not mistaken, so I will change some stuff.
And on the matter of… Prometheus interoperability.
Should I just remove the references, or just point, hey, we do have another blueprint in the works for this?
**Dan Gomez Blanco** 44:45 I… I would… just scope, I mean, yeah, I'm doing that here in mine, somewhere, that I'm saying… Yeah, something… I mean, maybe this will be a proper, like, note thing, and markdown, but, like… The idea being that, you know, you can say, hey, the scope of this blueprint will not… will follow… will be focused on following.
Set challenges, and almost, like, comp… Explicitly call it out of scope there.
And say, you know, general premise… we may focus on how to… Scrape components here, or maybe you can make some reference about, like, yeah, you're gonna have to scrape some data out of… kubernetes native components that don't support OTOP, and for that, we will be using the Kubernetes receiver. However.
for, in general, scraping Kubernetes, Prometheus metrics, and… And the way that… one might work with Prometheus in multiple ways, we will have a separate blueprint.
Maybe that's one way of approaching it.
**Alexandre Ferreira** 45:51 Yeah, I'm…
**Tiffany Hrabusa** 45:52 one caveat about the… the Prometheus interoperability Blueprint that we are currently working on in the mentorship that I'm… that I'm having or doing.
It is non-Kubernetes.
So, it will not talk about anything specific to Kubernetes, so… We may need another one.
Okay, nice.
**Dan Gomez Blanco** 46:14 That's fine. But I guess, you know, you will be… well, you'll be talking about Prometheus receivers and all that, which is basically how to configure your SDK for… for, Prometheus, for example, and… Might want to use.
**Tiffany Hrabusa** 46:31 I don't think we're talking about the SDK so much. I think it's more… Focused on, the specific challenges related to trying to scale, in a non-Kubernetes environment. So you're having VMs, and how do you make sure that you're scraping the right targets, and how do you, set things up? So then there's… using the Prometheus… receiver plus the OTLP exporter, but apparently, I didn't know this. The collector imports the entire Prometheus codebase, and there's a specific way that you can tell the collector to do that, so that at the go runtime, whatever.
it creates a lighter weight version of Prometheus that will help with network costs. I don't know. I'm not… I'm not on the technical side of things, but it's… it's, the idea is to show how to scale, Prometheus collection in non-Kubernetes environments. That's…
**Dan Gomez Blanco** 47:35 I see.
But I guess, you know, from your perspective, Alex.
it probably, I think, makes it… what I was trying to say is that… It probably makes sense to… assume that… There will be other things that people may want to… configure about OpenTelem… like, Prometheus.
in Kubernetes. As in, like… Not using OTOP.
Maybe you want, for some reason, you want to have your, you know, your SDKs configured to do OpenTelemni, sorry, Prometheus export, rather than OTLP, and then have your… your collector doing a target allocator to scrape these… these Prometheus…
**Alexandre Ferreira** 48:21 Yeah, cool.
**Dan Gomez Blanco** 48:22 one.
these are completely application-specific, so I would almost, like, stay away from that, because that may… that may… you may go then into configuring the hotel SDK for Prometheus, and blah blah blah. I would, you know, put that out of scope, and then focus on, like, there is an open… there is a Prometheus endpoint out there.
that is already, configured for you, basically. As in, like, there will be the out-of-the-box things that you may want to scrape from Argo CD, or from Cert Manager, or whatever. And then, yeah, how do you go about getting those metrics that are… I guess, standard in Kubernetes environments, but… But they're not in Audio.
**Alexandre Ferreira** 49:00 Yeah.
Yeah, I think I got a point, like, a few years ago, when I was, configuring output telemetry and Prometheus, we had to use the target allocator, and that is a complete history on its own, I would say, so… it's interesting to leave this out, like, application-specific Prometheus stuff. I agree with that.
And I guess then the other part that I should refactor is… the, the current Blueprint references, like, getting Prometheus… I mean, getting Kubernetes metrics out of Prometheus components, like Node Exporter and, and all that.
And… I think almost all of Kubernetes-related metrics.
There's a hotel… counterpart these days, like, so node exporter will be host, metrics receiver.
And there's other ones as well, so I will refector that to reference this.
Yeah. And… yeah.
**Dan Gomez Blanco** 50:10 I think that'll be… I do.
That's one of the things that I… yeah, we were mentioning earlier, that.
**Alexandre Ferreira** 50:15 I…
**Dan Gomez Blanco** 50:16 I personally think that even if this is a new way of doing it.
That may be out there in the field, you'll see… a lot of… end users using KubeState Metrics, using Node Exporter, and that's completely fine.
But from the perspective of OpenTelemetry.
I think we… if we have now a golden path to follow, which is… You only have to use the collector, and the Kubernetes semantic conventions are stable.
then that should be the one that we should be recommending, right?
And then, this is why I tagged in… Jacob that was working on a Helm chart that… would… almost, like, take the implementation steps, but then be a lot easier, because then with the implementation steps, you can say, hey, here's a Helm chart to implement a lot of this, maybe not everything, but, like, there's a lot of this that could be… that could be done in this Helm chart, and then so on.
**Alexandre Ferreira** 51:13 Yeah, and… It probably will be even less complex than using the Prometheus components, because you don't have to deploy a node exporter, like, a separate component that would expose the metrics. I think that the collector itself, I mean, the component, but then the collector, the receiver, actually scrapes the API, so there's… a cell… When it's unmuted, right?
**Dan Gomez Blanco** 51:38 Yeah, and actually, I was having a chat with them and the… I think… Again, you know, we need to check… this is a consensus-driven thing.
But from the perspective of the end user, the moment that I spoke to end users about the new, like, leader, extension, and then the fact that you can just… ideally, just deploy. The only thing you… at the moment, if you were to deploy… Well, not at the moment, but let's say a year ago.
If you were to deploy this type of monitoring with a collector alone, without KSM or no exporter, then you had to deploy a single replica deployment That would be doing the cluster-level metrics, because otherwise you cannot, like, you need to have one single point, one single collector replica that does it, right?
So… The other option that you've got now is that the only component that you deploy is a daemon set.
And that demon set does everything that you need. And, for… For the cluster-level metrics, you use the leader extension.
And that leader extension, basically, make sure that only one replica of that demon set is… quitting… doing the class several metrics. When that replica dies.
The leader got moved to some other… some other place. So that could be something that… I don't know if you want to recommend it or not, but it does sound pretty cool, and pretty simple.
**Alexandre Ferreira** 53:04 Well, you just…
**Dan Gomez Blanco** 53:05 Deployd a demon set, and that's all.
And maybe that…
**Alexandre Ferreira** 53:08 Yeah, that's a very good point. I remember in one of our comments, like, I wrote that this blueprint assumes that a collector is already deployed, and then you ask if that was the case or not, and then I thought, oh.
Oh, hold up, back when I did that, I had to deploy a singleton or a deployment just to get the cluster-wide metrics, but I didn't know about this leader extension.
I'll take a look on that, and possibly recommend this, because by doing this.
we make sure that the collector architecture are completely separate from the kid's blueprint itself, right? Like, you can just apply a demon set, and you're good to go.
**Dan Gomez Blanco** 53:50 That should be what the… I think that should be what the… the Helm chart does, if I'm not mistaken, but yeah.
**Alexandre Ferreira** 53:58 Yeah, so take a look on that. Great point.
**Dan Gomez Blanco** 54:01 And, yeah, and also lastly.
you may want to mention in that. I think I probably should mention that too.
Do we look at as well? There are… there may be certain parts of this, centralized platforms, I'll share the link later, but… I'm starting to put together this… this one, this blueprint. There may be certain parts here that you… that inter… that either… Overlap?
Or, like, you may want to say, hey, you know, you… You can export things directly from the daemon sets that are… you can export metrics directly from the daemon sets That you deploy, or the replicas you deploy.
However, we recommend that you do it through a gateway if you want to do any… any other type of, like, centralized management, and here is a blueprint for that. Maybe you don't… you don't need to mention it now, but then when we publish one in other blueprints, they will start to… To relate to each other, right?
Because normally, I guess, organizations will be deploying their Kubernetes and monitoring, but then at the same time, they'll be deploying a collector gateway.
And then that… maybe they have, like… what Lucas was working on, which is the non-Kubernetes environments, maybe those non-Kubernetes environments they operate them with Kubernetes environments in which they can run a gateway, and they can connect between, you know, they can deploy the gateway in Kubernetes, and still do non-Kubernetes environments. So they start… everything starts to map a little bit to how they connect, right?
**Alexandre Ferreira** 55:35 Yeah.
Yeah, that's… that's an interesting point as well.
I had a customer that tried to use the Demon set, but they defaulted on using the gateway because they manage their own monitoring nodes, right? Like, they deploy a type of node that's only for monitoring and deploy the gateway there, and… It seems that it's pretty 50-50 across organizations on using DemonSATs versus decentralized gateway.
**Dan Gomez Blanco** 56:06 Yeah, yeah. I think, you know… It's something that we can propose and review and, yeah, come to an agreement.
**Alexandre Ferreira** 56:13 Yeah, perfect.
**Dan Gomez Blanco** 56:14 Yeah, cool, awesome.
Yeah, I'll drop the… I'll drop the link to this. You may have missed that, Alex, when you joined in, but I'm trying to get some early feedback on the challenge… on the common challenges for this blueprint, and the summary in the background.
And then, haven't really done the guidelines or the implementation, but yeah. I'll share it in the Slack channel.
**Alexandre Ferreira** 56:40 Alright.
**Dan Gomez Blanco** 56:42 Okie doks, damien… Thanks for joining!
Sorry, we haven't got to you. Is there anything that you want to share?
Damien, now that you joined, welcome to… Welcome to the call.
**Damian Ogedengbe** 56:57 Hello, thank you so much.
I guess I was a bit late.
I just checked my calendar, and I saw that I signed up for these a long time ago, and I thought it was important I check in to know what's going on here.
And I'm impressed by what I've seen so far, well done. Great job to you, Dan Gomez.
It's not, it's not just me, it's not…
**Dan Gomez Blanco** 57:20 It's not just me, but thank you. It's all of us.
But, yeah, so let us know, you can see the work that we have currently in progress and things that are in review.
If you want to… If you go to the notes, to the meeting notes, which should be in the calendar invite.
You will get to this.
to this board, and then you want to provide any comments on the PRs that are raised, or the issues themselves?
That would be super appreciated as well.
**Damian Ogedengbe** 57:51 Alright, thank you so much.
**Dan Gomez Blanco** 57:52 Alright.
Okay, thank everyone, thank you everyone.
And, happy hotel graduation day.
**Tiffany Hrabusa** 58:00 Congratulations, everyone.
**Dan Gomez Blanco** 58:03 Alright. To you, boy.
**Tiffany Hrabusa** 58:06 Bye.
**Alexandre Ferreira** 58:06 Sisu, folks, yeah, bye-bye.
**Tiffany Hrabusa** 58:08 I…
