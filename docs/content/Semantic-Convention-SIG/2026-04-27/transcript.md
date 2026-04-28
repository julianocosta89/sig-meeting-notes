SIG: Semantic Convention SIG
Date: 2026-04-27
Duration: 62 minutes
Zoom Recording URL: https://zoom.us/rec/share/J4AB9dxwQQ2VC5hOQUzdEz54n7dsRVfBmKhezRt50ndOPA_GVVi6Br2-s6uRXRrc.HeEFaK2fxtPLIgw7
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:00:37 Hello!
Josh Suereth 00:00:40 Hey Go ahead.
Liudmila Molkova 00:00:43 How are you? Long time no see.
Josh Suereth 00:00:48 It's only been, like, a week, weren't you just at a conference for a week or something?
Liudmila Molkova 00:00:52 Yeah, but it feels like a life ago.
Josh Suereth 00:00:57 So, a good conference is what you're saying?
Liudmila Molkova 00:01:01 Yeah, a lot of things. By the way, it's probably my turn to drive the meeting.
Does anybody know where this number comes from? I see it every once in a while, and I think somebody manually populated, but I have no idea.
Josh Suereth 00:01:16 I think Armin comes back and manually adds it.
Liudmila Molkova 00:01:19 Wow.
Josh Suereth 00:01:20 That sounds like an Armin thing. Like, he is on top of it, and just does stuff like that. It's kind of awesome.
I don't know if he's here right now, but, yeah.
Oh, actually, you know how you can find out, Lunbella?
There's a history, there's a history. Oh, look, no. But you can go to the history, and you can see who edited it.
And then we can figure out which edit made that number.
Liudmila Molkova 00:01:53 I think if this.
Josh Suereth 00:01:53 I see cool history, actually, yeah.
And then you have to kind of click through. Oh, it's all anonymous users, so it's not going to tell us which person did it. Never mind. But you'll see… you'll probably see someone having added it.
Liudmila Molkova 00:02:08 Cool, yeah.
So… Let's see, we talked about federated SimConf last week, nice.
And… we have a lot of stuff for this week.
Okay, I've spent my jet-lagged brain on this board a little bit.
So we have a bunch of pull requests that are ready to be merged. Most of them, they're not really ready, there are some final Feedback things.
That people might come back to.
The bullock thinks.
This one, I have no idea about.
It's on hold or something?
Pete, there is some alternative proposal… I'm going to leave a note asking if we should close this.
Okay, this one I blocked because it… Added a bunch of constants to GenAI.
Provider name without any… Anything but constants, and… I've tried to find guidance where we documented that we don't allow it anymore. I think we… it's just verbal. I don't think we've ever documented it clearly.
So, the author of this PR was not really happy with my feedback, and I think we should document it somewhere.
Josh Suereth 00:04:43 Yeah, I'd agree.
Trask Stalnaker 00:04:44 we discussed.
Josh Suereth 00:04:47 I agree it needs to be documented. I think the concern is, is the, the advertising concern of, like.
If I see other AI frameworks there and I'm not there, that's not fair.
So I understand the… so I think we should document it to make sure it's clear why we're doing what we're doing, but also what the bar is for being included in the initial set of things.
Trask Stalnaker 00:05:17 as with everything else, GenAI, it may… Deserve a slightly different answer.
Josh Suereth 00:05:33 Do we make an AI bot that answers?
you have to make it past this bot. And then… You make it through the approvers, too.
Trask Stalnaker 00:05:45 Gauntlet.
Liudmila Molkova 00:05:48 Can I stop making the AI bots, please?
Trask Stalnaker 00:05:54 So, we need to make more AI bots on our team.
Liudmila Molkova 00:05:58 We need to make AIB.
Fight other AI bots.
Okay, I created an issue, maybe… So, docs… Okay.
Let's move on… So, there is a bunch of pull requests that need more approvals, I think… I added some of them to our triage because they're interesting.
There are some trivial ones, so if anybody wants to approve, This one, please go ahead.
And I think there are a few other… This one is also… Okay, I probably can.
There are some approvals.
anyway, if you are a general SamConf prover, please take a look at things that interest you here.
And with this, let's move on to the… Main agenda?
Okay, so I've seen a bunch of pull requests related to data.
Root namespace.
And I… Don't… know if it's, like, yeah, Josh, go ahead, I think there is some… something from the service and deployment sync.
Josh Suereth 00:07:50 Yeah, I'll speak to this. This was in the initial proposal for the service in SEMCOM SIG, and then we asked them to reduce scope to take it out, so, like… but, like, to clarify what this is, because I think we all need to understand what they're trying to build and do. Data is annotating the data that a service is interacting with.
So if a service is interacting with data that's not sensitive, you might treat it differently than if the service is interacting with highly sensitive data, and One of the things that this is proposing is this data sensitivity might be annotated on baggage to go downstream that could change telemetry, like, in all systems that interact with data that could be sensitive. So, let's say I'm, you know, in, like, I have, like, a user database or credit card database or something, or I'm interacting with data that's sensitive in that fashion, and I have some kind of restriction where I don't want this data leaving the device.
I can have a local collector that says, if you see data sensitivity high, do not send it further. Keep it local, right?
And so they have a… actually, they put a prototype together of this. There's a… like, if you look at the document that's proposing the data sensitivity attribute, the PR, they have a document attached to it, supporting document, that talks about what it is, why it's used, they have… they have some demos of using this in the OTEL thing, they talk about where it's used across things. I actually think that this is a really cool use case.
That's outlined.
The only thing that I would say, from my own personal view, is whether, like.
there's also an argument for why the service and deployment SIG is the right place to deal with this, because this is, like, an abstract service-y concept of this service deals with sensitive data and the handling of that through a system.
I think it'd be fair if we said, you know what, we think that this deserves its own SIG or not. I think the idea behind it's pretty cool, honestly, and if you look at some of the demos of what they were doing, I think there's some power there. So I'd like to find a way for us to enable this in, like, an alpha-beta stage to continue.
But I would recommend reading through this of, like, what they're trying to do and why. I think it's not like… It's not saying the data of the telemetry is sensitive, it's saying this is a service that interacts with sensitive data, and then you can take behavior downstream based on that.
So it's… it's, it's, it's rather interesting. Might not be how we want to model this in the long run, too, but I think if you look at the… examples of what they call out, things that they see, and, the way they have it wired into the hotel demo. I think it's something we could… Green light as an area of exploration.
Liudmila Molkova 00:10:44 Yeah, it's pretty cool.
I… I think the scenario makes sense. I am concerned about the data as a root namespace, because it's so broad.
Josh Suereth 00:10:56 The SIG… the SIG debated between data and data source.
And was basically divided down the middle.
of, like, we… but the… we haven't… how do I want to phrase it? The bike shedding has not occurred, I will say that.
So… or it hasn't gone through the whole community. But I agree with you, like.
calling it data is broad, but I also challenge, if you… if you know the use case, what the hell name would you give it? We need suggestions that make sense. Data source was rejected. Data was like a… nobody… Nobody likes it, but no one had a better one, would be the way I would phrase the SIG discussion.
Trask Stalnaker 00:11:40 And, what was the reason against service.data?
Josh Suereth 00:11:47 I'm trying to remember.
I don't… I don't remember why service.data wasn't picked.
But it's been… it's been, like, a month, so apologies.
Liudmila Molkova 00:12:03 If I…
Josh Suereth 00:12:03 Or it's been… it's felt like a month, how about that? It might have been last week, I don't even know, but it feels like it's been a while.
Liudmila Molkova 00:12:11 So we are intending to use it First as a resource attribute, the entity, part of the service entity.
And… The second, more… even more interesting case is it flowing downstream, and then it would be associated with specific spans, right?
Josh Suereth 00:12:34 Yeah, I think that's why it's not service.data, because the… because of the baggage use case that they had for it.
Yeah, that is making more sense. Thanks, Ludmilla.
I believe that's what the discussion was about, and that, I don't know, is… I don't know if anyone from that SIG is here.
I don't see Anthony Marabella, I don't see Matt, okay.
Yeah, so I… I believe that's what that discussion was about, and I think that's where, looking at the examples makes sense, and I think it's fair to start asking these questions, and I think we can take this back to the SIG for discussion.
So, like, all of that is totally fair. I guess the question would be, do you want, a more formal proposal around the namespacing of this?
So that we can make a decision about whether to use data, service that data, etc?
Christophe Kamphaus 00:13:28 I think it's fine if it's documented on the issue or PR.
Liudmila Molkova 00:13:39 I was raising it because I wanted more context, and I think I've got some context. I'll go back with this and probably read the document more closely, so I understand. Maybe I will have some suggestions.
I'm… I'm… like, if it was just service data, it would be 3V, right? But then… I was thinking we have some similar stuff in GenAI, where we do Gen AI and document content. Would we… Use data content there, would it be applicable?
And I probably need to spend some time thinking about it.
Josh Suereth 00:14:18 I, I think it absolutely would be.
And so it'd be good for us to spend time thinking about it. I actually think, like, I'm glad you brought this up here, because I do think this needs just a general discussion across the SEMCOM SIGs. In fact, almost everything the service and deployment folks do, I think, will have impacts across all SIGs, so I think it's good for us to bring it here for discussion.
Trask Stalnaker 00:14:42 And so that I underst… to understand… The data, sensitivity would… you would apply across… all… everything independent of… it's not related to whether we're capturing, like, in Gen AI, whether we're capturing request and response bodies. It's not related to the… whether we're capturing detailed telemetry. It is purely… Related to whether this system is interacting with sensitive data, period, whether or not it's exporting.
Josh Suereth 00:15:21 Yeah, like, so, for example, let's say you have, in-gen AI, you're talking through, like, an MCP server or one API, or a, what's it called? OpenAPI, or a CLI, or something that you're communicating with that does talk to sensitive data, right? So, when that thing generates its data.
the collector might say, you know what, this, like, there's parts of this that should not be logged outside of this machine or in this region, or something. Cool. So, you would actually use the fact that it's on the resource to prevent it from going further. When it comes into Gen AI, if it's on the baggage.
We could say, we could actually have a thing that says, if this baggage gets annotated on the GenAI prompt responses.
that GenAI prompter response would have had access to sensitive data, and I actually consider it too dangerous to log those, or send them outside of region, or something like that. So the idea would be then that system, because… again, that's phase two. Phase 1 is just annotating the first thing. Phase two would be using baggage, and then being able to have the second thing say, you know what?
this is dealing with sensitive data, I'm going to be more careful about what I do with the telemetry.
And so I can have that annotation and take different actions. That… right?
Trask Stalnaker 00:16:36 Okay, so it's not entirely orthogonal to the concept that we've discussed before of annotating semantic convention attributes.
as potentially having sensitive data, like a response body.
There's some… in the future, there's possible connection between the two.
Josh Suereth 00:17:00 Yeah, you could imagine if we actually knew which attributes could potentially be sensitive, we could have an automatic redaction that would say, if you see sensitive data criticality of high, I can just automatically redact all things that could have sensitive data.
And that could work together. And I think… that's why I think this is pretty exciting in the long run, but I also think this is a… Commitment. And we'll be a court, you know, we have to let this play out, effectively.
So, this is a thing I think would be in alpha stage for quite some time as we flesh it out, and that's the thing, for example.
Trask Stalnaker 00:17:40 Thanks.
Liudmila Molkova 00:17:44 Cool. So, If we targeted stability anytime soon, given that it works with baggage, it would probably deserve its own SIG because the baggage is so tricky, and nobody actually, as far as I'm aware, made good use out of it.
Josh Suereth 00:18:05 Hey, I have a demo that uses baggage well that fell into obscurity and no one touches anymore.
Liudmila Molkova 00:18:11 Demo, yes.
Michele Mancioppi 00:18:13 That was.
Josh Suereth 00:18:14 Oh my god.
Michele Mancioppi 00:18:15 There was a demo by Daniel and Skyscanner guys at the last KubeCon, baggage is older, right?
Josh Suereth 00:18:25 Baggage is overrated, huh?
Trask Stalnaker 00:18:27 All the rage.
Michele Mancioppi 00:18:28 I said all the rates.
Josh Suereth 00:18:29 I wasn't…
Michele Mancioppi 00:18:30 Of course, be sarcastic.
Josh Suereth 00:18:34 Yeah, I… I… I think I agree with you, the bill. Like, like, when I… when I review this and I look at the investment and the cost here, I… I do think that there's, if we were to limit the scope and say we're just gonna do service tagging in service and not do the baggage-related stuff and not expand this to its full potential, maybe, but I… it does feel like this needs… attention cross… Journey.
Liudmila Molkova 00:19:05 Yeah.
If we limited it to just to the… tagging entities. We would probably start with this. But this is probably another example of the embedding. We would… might have app.
Data sensitivity and everything else, data sensitivity.
Yep. Cool, I'll take another look at it, and if I have any better suggestions, I'll leave them.
Christophe Kamphaus 00:19:36 So it would also… it could also be added as an attribute on any emitted telemetry.
From the baggage, by mapping it.
And that's how you would process it in the collector, is set it.
Liudmila Molkova 00:19:57 And then… if it's stamped there, it's not clear what it applies to. They can get… If I've received it from the baggage.
I know that the span deals with something sensitive. There is something sensitive about the request that it processes. It's not a property of data, it's a property of request. But it might be some… trivial call to, I don't know, HadMeta to check if something exists, then it has… it doesn't… it's not actually sensitive by any means.
Josh Suereth 00:20:32 Yeah, yeah, yeah, it just tells you that it could possibly… so if you were trying to be safe, right, you might say, cool, I'm not gonna log prompt responses from Gen AI that deals with sensitive data, by default, so I'm gonna turn that off. Or it could be that you would only run your sensitivity checker.
Right? On those things, so you don't have to pay it for every single prompt response you're making. Like, if something's looking up, you know, the address of Starbucks, you'd be like, cool, I don't have to check that to see if there's sensitive information in it, because it can't talk to a sensitive system. But the thing that is dealing with user information, you could then have that flag, you know?
Liudmila Molkova 00:21:12 To deliberately apply the… content you've got from the baggage on specific calls to… like, be smart about it.
Josh Suereth 00:21:20 Yes, yeah, yeah. So basically, because you've tagged it to say this could have sensitive, you can now be intelligent about when you do the filter and when you don't, you know?
Yeah, so my lookup locations of local businesses.
I'm not gonna redact anything, I don't care. Like, that's all wonderful, you know? But my, you know, what's the home address of all the users in my database? That one I might be a little more careful about.
Liudmila Molkova 00:21:49 Nice. Anything else on this? I think we can move on.
Cool, another one. I don't think we have anybody from the process… system and process SIG here.
Let me know if there are some people, but I was… Wondering, this PR is ready to go, but it only marks attributes as RC. It does not mark process entity as RC, And there is… there is an open discussion on… something related to it, I forgot. But essentially, I cut… I… I would love to merge it, but also we should probably have a policy on do we mark attribute, just attributes as… A certain stability without marking the signal that they appear on.
I'd rather not.
Josh Suereth 00:22:52 I'm… I'm good with that. I thought this one did mark the entity stable, did it?
Oh.
Did it… did it change since I reviewed it? It might have.
Liudmila Molkova 00:23:05 So I… NGT.
remains in development.
Josh Suereth 00:23:14 Yeah, yeah, no, I mean, like, I thought that they had marked it as stable, or at least one of them.
Interesting.
Christophe Kamphaus 00:23:22 Yes, that discussion comes up again and again.
Josh Suereth 00:23:32 Yeah, I'll add, I think we need to have a call-out specifically for attribute groups as well. So, if there's a public attribute group, the way that we define them in V2, you can stabilize that. That will involve stabilizing the underlying things, since we don't… We don't have a great model for some of these, you know, could attach to multiple signals, things, we're using attribute groups, but I think it should be required that there is something that is not the attribute that you're stabilizing with the attribute. So you're either stabilizing an entity, a metric, a span, an event, or a group.
A public attribute group that says, here's a set of things that people might Great.
Liudmila Molkova 00:24:25 Oh, and I guess we also need a policy to… Documented.
Josh Suereth 00:24:44 I thought… I thought we had… oh, no, we only have the inverse, don't we?
You can't mark a group stable without the attributes being stable, but we don't have vice versa.
Liudmila Molkova 00:24:54 Right.
We have a policy that we don't define attributes without the signal.
And maybe you wish this, this one should belong.
There as well.
Trask Stalnaker 00:25:14 Can that be a REGO policy?
That you can't have… stable… oh, I guess… no, okay, I understand.
Josh Suereth 00:25:29 We could make a Rigo policy that… it'll take a little while to build it, that requires at least one signal or attribute group, public attribute group, to be stable, for an attribute to be stable.
Like, there's a way we can do this in Rego. I… hopefully it's not tedious and annoying for people.
Or flaky, but I think we can do that, actually, relatively safely.
Liudmila Molkova 00:26:30 I don't know how to write it. I would assume if it's the staged approach, it's just broken down into multiple PRs, that's fine. It's the… the reviewer… Human judgment.
more than rego policy.
Okay, moving on.
So this is an FYI PR, I think… We have a new entity for the… Browser document.
I reviewed this pull request, it kind of makes sense to me. I'm a bit worried that browser people don't have a presentation In the general SEM config, And, if anybody is interested and has opinions, please review the PR.
But otherwise, I would rather merge it than let it stay in limbo.
Boo.
Somebody, christus asked for the same quant release. We haven't done one in a while, right?
So, it should be… Able to just schedule it.
Would anybody have time?
This week?
Trask Stalnaker 00:28:24 I can do it, that'll be… I can use that as a chance to port the release process over to the new GenAI repo.
Liudmila Molkova 00:28:35 Nice.
Josh Suereth 00:28:38 Shit.
I don't remember how to do this, but I heard that we can get, like, Slack integration going. Should we set up, like, a GitHub action that just pings Slack to say, hey, think about a release every month?
What do you think?
Or should we be more?
Trask Stalnaker 00:28:56 Yeah, we could… we could do that in our… the maintainer channel.
I forget, but yeah, there's, like, a slash command you can set up a scheduled reminder.
Josh Suereth 00:29:08 Oh, really? Like.
Trask Stalnaker 00:29:09 Yeah, it's just… Oh yeah, yeah, it's just a built-in Slack feature.
Josh Suereth 00:29:14 Okay. Yeah, I think just getting something to remind us, like, I don't think we're intentionally forgetting to release, but being explicit about reminding ourselves to release would be good.
Trask Stalnaker 00:29:27 I'll do that in the channel.
Liudmila Molkova 00:29:35 Awesome, thank you.
Another FYI PR, I think it has necessary approvals.
But I think, Josh, you commented, and maybe somebody asked… asked you, or replied to your review. If you want to take another look, go ahead, otherwise… We can just merge it.
quite… And… Trust! Finally, not me, not me.
Trask Stalnaker 00:30:08 Ayy.
Liudmila Molkova 00:30:08 About New Repo?
Yeah, yeah. You wanna share?
Trask Stalnaker 00:30:11 I do.
Let me… Get that… Going… All right, so we've been discussing this for a while, and been building this out for a while, and I think I'm ready to pull the Pull the plug and, do the… do the switchover, discuss, signing to take it to the Gen AI SIG tomorrow.
But we've been discussing it in that SIG already.
So… This is, so, it is using Weaver, for the federated SEMCOM, there's a few things that we can… that it kind of works around today that we can… That I will kind of work, at upstreaming in the future. Probably the biggest one is right now, it is using the semantic conventions.
Weaver templates, like, the remote templates that way, as opposed to, I think ideally.
It would be nice to use the new Weaver packages stuff.
And there's a couple of little workarounds due to that.
But that's all working. It's got, you know.
your contrib is ready to go. It talks about these, reference scenarios. So this is a big part of this new repo, is… Reference implementations, that live here, and so these show us, like, okay, let's look at, create… invoke agent client.
Or Invocates an internal. So we've got 3… libraries that… implement that. You can go in, and then you can see, actually, attribute by attribute, which reference implementations emit those attributes. That is done by… running the scenarios, so, for example, say, Auto Gym, Right, it's just got, basic… Python script that runs, and it's all, like, reference manual instrumentation here.
And… Using the actual… Pieces of the actual attribute values that are then kind of demonstrating that this, for example, here, hopefully, is… oh yeah, this is coming from here, this is coming from the JSON results, so you can kind of trace through and validate that these things are coming from actual pieces of data that are capturable.
Kind of like a capturability, study, in a way.
And… So the… yeah, so the contributing, talks about that. It kind of included some other basic things that we've kind of discussed in the past, how to, you know, get things done, get your PRs, how we can move faster, keep PRs small, like, how to join SIGs, that kind of thing.
There's also a pull request template.
That… Talks about, this Josh… And, Jamie last week also, brought up this kind of concept of the, the use case, the user journey, documenting that piece.
So, you know, I think, in addition to the reference instrumentation being part of the PR, we also really want, people to focus on, including the motivation, what's the user journey, who's using it for what, what's the prior art here, and the prototype, which is generally the reference scenarios, but in some cases, it may be an external, Prototype, or, you know, dashboard, screenshots, that kind of thing, if it's for something different.
Yeah, I think that's it. So, this… in the makefile, if you're interested in seeing the kind of Weaver-y workaround stuff, is kind of documented in here. But I think it's in a good place to… land and, work, it's working, and we can make improvements. We can use this to kind of drive improvements to the weaver packages and stuff like that, afterwards.
That's what, so, yeah.
Josh Suereth 00:36:14 What templates are you? You're using the, So, I just saw that in the main file. You're using the templates for just the docs, like, for, for making the markdown, or are you also using the policies from CEMCOM as well?
Trask Stalnaker 00:36:29 I think it's using policies?
Oh, maybe not.
Josh Suereth 00:36:36 Huh.
Are you… are you doing any kind of policy checks?
trash.
Trask Stalnaker 00:36:44 I will look into that.
Josh Suereth 00:36:46 Yeah, yeah, I, I think it's either in Ludmila's OTEP or my OTEP, there's an example.
But yeah, just having to check policies make file. Maybe it's in your GitHub, maybe, maybe you're actually using the Weaver, because I think you can now use the Weaver GitHub action for it.
Trask Stalnaker 00:37:05 I do have a check… Policies… Why are we not checked.
Oh, yeah.
Local, registry check, which… okay, local policies… I think this is… I think this is from… Cash from the upstream… yeah, from the semantic convention. I think so. I think it's using all the policies from the SEMCOM repo today.
But I won't.
I will double-check that.
Josh Suereth 00:37:44 I'm pretty sure you can use the Weaver packages for that now.
Liudmila Molkova 00:37:50 They are V2.
Josh Suereth 00:37:52 It was a…
Liudmila Molkova 00:37:53 Oh, it doesn't matter. Or they have it too.
But I'm thinking, should we… okay, should we just take it and immediately convert it to V2? Everything in this new repo.
Josh Suereth 00:38:07 Yeah.
I… I think we use this as the… is V2 ready to… for prime time?
Liudmila Molkova 00:38:15 Yeah, and we actually, I think we made a deliberate decision in Weaver packages to do V2 there, because it's the future, we want everybody to… Have some carrot and stick to move to the future.
Trask Stalnaker 00:38:29 Okay, so if I convert to V2, then you're saying I should be able to use the Weaver packages policies?
Liudmila Molkova 00:38:37 Yeah.
Trask Stalnaker 00:38:38 And those are… essentially cover the same thing Same things as the SEMCOM repo today.
Liudmila Molkova 00:38:47 Not everything, but some of it. I think it enforces backcompat, but it does not enforce attribute naming.
It does.
Josh Suereth 00:38:56 That's your big name now.
It… there's 3 packages.
One does back compat, one does attribute naming, and the third one does some kind of… stabilization, like, lifecycle management. So you would use all three packages. It's… this is in… again, I think it's in MyOTEP. I don't think it's in the Miller's OTEP, but if you read the OTEP on Federated SEMCOM, it lists the three packages you're supposed to use.
Liudmila Molkova 00:39:23 But they are not… the naming is not in the Viver packages yet.
Josh Suereth 00:39:28 I think it is.
Liudmila Molkova 00:39:30 I don't… I don't see it, maybe I'm…
Josh Suereth 00:39:32 OpenTelemetry, we… The attribute naming stuff?
Liudmila Molkova 00:39:37 Yeah.
I think we thought… so the viewer packages… Oh, name. Yeah. Oh, sorry.
Josh Suereth 00:39:44 Yeah, here, I'll put a link in chat.
Liudmila Molkova 00:39:46 Oh, I see ya.
Josh Suereth 00:39:48 If they're not all there, then I failed, but I thought I moved everything over, so…
Liudmila Molkova 00:39:52 Yeah, it was, it was me, sorry.
Josh Suereth 00:39:55 Yeah.
But those are the three that you want to use. Those are the three… so we took SEMCOM and split it into three components so that people can take them individually if they want, but yeah, one is about back and bat, one is for attribute naming, and SEMCOM naming conventions in general, and the other one is about stability lifecycle management. So if people are making their own repos and want stability lifecycle.
they can pull it in without using our naming conventions. But I think everything's migrated over, or there were things that weren't migrated over that aren't needed, because V2 implicitly enforces them.
So that might be what you're thinking is missing, but it should… everything should be over there.
Trask Stalnaker 00:40:34 Cool, I will do this.
Anything else that… jumps to your mind that I should check on?
Christophe Kamphaus 00:40:50 Well, Yeah, where will the… Gen AI is somehow going to be published.
Trask Stalnaker 00:41:02 I, yeah, go ahead.
Liudmila Molkova 00:41:07 So I think they will be… there is a… as I see Weaver manifest, that provides the new schema URL.
Which is, on up in Telemetry UI as well, but we'll probably need to build this.
info on Atella, once we are ready to make the first release there.
Whoa, what?
I wanna… okay, doesn't answer your question, Krista, sorry.
Ruediger Schulze (IBM) 00:41:38 Isaiah, this is really good. Just… first of all, this is great. So, we have been discussing this with the other sick lead from the mainframe SICK last week, and actually, we think this is really good stuff.
if we want to start this, and Trask, obviously, you run this under your name, we would start with something similar, semantic conventions Mainframe, lays this out, and then at some point, you know, this would have to be promoted, and I assume there is then we bring it to this secure with initial content.
And then have a… I think my question is, what's the process to promote, then, once we, as a SICK, have been deciding to move forward with a… With a federated approach for mainframe semantic conventions.
of how to… Bring this to the community.
Trask Stalnaker 00:42:34 Yeah, I think, the… The main… I think probably we just need a vote of the maintainers of this repo.
To, you know, to split it out, which I'm… kind of looking for implicit… I mean, the maintainers of this have been discussing this for a while, but I still need that, like, official stamp that, hey, yes, this looks good, let's go. And then, I will create the repo in OpenTelemetry.
And I will send… it starts out as a blank repo, and I will send a PR, basically, to dump the initial content into there, and then… because that covers us from the whole CLA, aspect, and then, The maintainers can review, approve that, and then… We, you know, we… Obviously, there's a transition path, we've got to remove it from the core repo, we need to… inform people who have open PRs that, sorry about this disruption, please reopen your PR over here.
But yeah, pay attention, just kind of, if you kind of follow this process along, you'll get to see what works and what doesn't.
And then you can do it better.
Ruediger Schulze (IBM) 00:44:00 Okay, thanks. Okay, no, this is great. Thanks a lot, and again, I think we will take this forward.
Josh Suereth 00:44:12 So, two things for you, Trask. One is, should we merge Ludmilla's OTEP and the federated SEMCOM OTEP for this, or are we doing this as a prototype independently?
Trask Stalnaker 00:44:31 Let's see where.
Josh Suereth 00:44:33 Either way, personally. But yeah, like, I think Ludmila's… Ludmila's OTAB, That's… that's just… my… mine is just the Federated SEMCOM, which depends on the Millas. So, like, the Millas is the one I really want merged right now, if possible.
Oh yeah, I'm assigned to it, so it's my responsibility to get it merged, too. We only have 3 approvals, and we have no one from, SEMCOM outside of, I think, myself on here.
So I think that maybe we just didn't advertise it enough in this meeting, but I think it'd be good to at least… especially since you're building this.
Trask Stalnaker 00:45:14 Yeah, I will.
Josh Suereth 00:45:15 Yeah.
Trask Stalnaker 00:45:16 Yeah, yeah. Now that I have context, I… yeah, now that I have… and after I… I'm gonna… I'll convert it to Schema V2, and then I will… I will review this and get either comments or approval on it.
Josh Suereth 00:45:32 Right, because there was a… in the notes, there's that question about where will this be published, what's the file format. Ludmila's OTEP answers those, and so that's why at least it's the initial design, but I would like… I'd love to get this at least merged, prior to, like, doing the more prototyping, and then mine is more, like, the follow-on work of, like, what policies are required, you know, that sort of thing that you're also doing, actively.
So, I'm fine if we continue to, like, use this as a guinea pig, but I'd love to see us get the actual, like, approvals on stuff for the design, and use what we're doing there. What's the phrase? Don't get the cart ahead of the horse, or something.
I feel like you're executing on these designs already.
So, let's just make sure they're… yeah.
Trask Stalnaker 00:46:24 Yeah, you can hold me accountable for getting approvals on both of those based on the, prototyping, the Gen AI work.
Josh Suereth 00:46:33 I mean, so it's a sign, like, I'm the one responsible for getting Ludmilos through.
Liudmila Molkova 00:46:39 It's interesting, though. But we need more… we need more feedback.
Trask Stalnaker 00:46:42 Checkmarks.
Liudmila Molkova 00:46:43 Yeah.
Yeah. I promised you'd trust prototype for multiple areas to get your approval, but it turns out you've already done all the prototypes yourself.
Trask Stalnaker 00:46:53 Which is better, because that forces me to actually understand it.
Josh Suereth 00:46:58 So, Trask, can I just promise you a bunch of things and then watch you do them? Is that… is that how this works?
Trask Stalnaker 00:47:05 It has to be something that, is… that I want to do.
That fits into, yes, this Gen AI stuff right now is, yeah, I feel like we've got a lot of pieces to this puzzle, you know, that are sort of coming together, starting to come together nicely. We've got a lot of work to do, but I feel like this is… The first piece that is ready to… almost ready to land.
Josh Suereth 00:47:39 Cool. Great work, by the way. I had one other thing to say.
Which is around versioning.
This might be contentious, so please yell at me if I'm being.
Trask Stalnaker 00:47:49 Oh, yes. Yes, I had that question here.
Josh Suereth 00:47:53 I would prefer… if we call this thing an alpha until GenAI is ready to say it's stable, and then we treat 1.0 as we only make stable breaking changes from there.
in the 1.0 series before we go to 2.0. You could say, cool, I'm gonna go 1.0, and if I make a breaking change, that's the same as going 2.0 from there on.
I'm also okay with that, if that's where you think you are as a SIG, but I would… Personally, I would caution and say maybe we go alpha, and then we'll have a 1.0, you know?
Liudmila Molkova 00:48:27 I think we… It's related to what we do with the current semconf that we have in Core Repo.
I think we should japricade them.
Deprecation means… we discussed it with Trask a bit, that effectively, this is stable, because if it's deprecated, we're no longer making changes to it.
and they are V1.
I kinda feel that it would be logical to mark the new thing.
as V2, but it's not a… Strong thing, because the namespace, the name of the registry is different, so we can stay as we want, as well.
Josh Suereth 00:49:15 you might be able to… you could call it V0, too, and then when it goes 1, it's fine, but the key thing that I really need Because I just implemented all the dependency resolution hell in Weaver, like, where we can handle multiple dependencies, and we can resolve multiple dependencies, and you can have, we can figure out what the latest version is and pull the sem count from the right thing. For that to work, you have to use semantic versioning.
If you deviate from semantic versioning in any stupid way.
all the code I just wrote, is broken.
And it is really tediously annoying to fix it.
it's rather complicated. So, my request would be use semantic versioning. If you want to have it be, like, a 2.0 alpha for a while, you have 2.0 alpha 1, 2.0 alpha 2, go for it. But do not call it 2.0 and then not have it be stable, or the resolution rules that we're building will break.
Trask Stalnaker 00:50:14 Josh, how does that work with, like, even if we call it, like, everything is marked stability development?
Today, So, if it's… If we throw a V2… on it.
Aren't all of those… Things still in development.
Josh Suereth 00:50:37 They are… we don't… So… we don't have a resolution. Right now, the resolution's completely done with this.
Trask Stalnaker 00:50:45 Oh, this is the idea of having two different schema URLs, one for the development stuff. Okay.
Do we have that?
Liudmila Molkova 00:50:55 We have that in Dartab, and we initially would publish everything only the dev version from.
this new repo. Once we stabilize something, we can publish the stable version.
Josh Suereth 00:51:08 Now, you can see some of my comments with Milla on your OTEP, like, I actually think… when we deviate from how semantic versioning works, we might be in trouble. So I think we actually have to give the development version a different name.
Liudmila Molkova 00:51:23 But it is semantic versioning, right? It's the suffix in somewhere.
Josh Suereth 00:51:28 So, what will happen is the development version can basically never get used.
Because the suffix… the suffix makes you a lower version than not the suffix.
So, in terms of dependency resolution, the stable version will always get chosen.
and kind of oust the development version, so it gets really awkward. So, there are ways, like… I can show you the details of, like, the issues I ran into. It might just be a bunch of bugs we can fix on the Weaver side. It just makes dependency resolution hellish for me. If they had different names, it's a lot easier.
Right? So, like, if it… if it's a different.
Liudmila Molkova 00:52:02 form.
Josh Suereth 00:52:02 Directory name for the development versus the stable.
Liudmila Molkova 00:52:06 Put your camera off.
Oh, so…
Josh Suereth 00:52:08 Boolean if you want, but yeah.
Liudmila Molkova 00:52:12 But essentially, it would… we would publish it, when we have the schema URL. This will be, like.
dash def.
And then version.
Josh Suereth 00:52:27 Yes. Yeah.
And then you would have dash stable version that would only have stable bits in it.
Liudmila Molkova 00:52:33 Or no dash stable, just Gen AI.
Josh Suereth 00:52:37 Sure. Oh, yeah, yeah, just Gen AI, yeah.
The other option is you, you, have the dash with a incrementing version.
And then, when you stabilize, you just take away the, like, dash dev, and then everything's in the core. It just… it's… it's… Awkward. Anyway, we might… that is a topic that I was planning to spend 30 minutes on Wednesday.
Because it's rather complicated, but my initial investigation into, like, doing the dependency resolution stuff.
we won't be able to do anything sophisticated for some time, and what… what I have right now is, I think, good enough, but a little bit naive. And so, where we deviate, I think we need to be very careful and kind of talk through the odd corner cases.
Liudmila Molkova 00:53:29 Crap.
Cool, I think we have talked… enough for the next steps on this, and I want to give I lost 5 minutes to Christoph. Would everybody be enough? Okay with it?
Trask Stalnaker 00:53:43 Yeah, just to summarize on this, it sounds like we don't have… like, there's really good reasons for both this and for carrying to V2, so we need to discuss that more.
But we have at least a month before the, who we want to release from Gen AI.
Alright, thanks.
Liudmila Molkova 00:54:12 Thank you.
Christophe Kamphaus 00:54:15 So, this issue came up, in a pull request about, metric details in Go.
And, so we split that off.
You can open the issue, so we can discuss it.
Or I can share my screen.
Liudmila Molkova 00:54:36 Yeah, sure, please.
Christophe Kamphaus 00:54:47 There we go.
So yeah, it, it's about how can you Optin to detail.
And, the discussion went around to… two sorts. One would be… To use the same attribute, but with different values if you opt in.
And the other was to use two separate attributes, one with underscore detailer suffix, And then you could, Use a detailed value for the attribute in that one.
And the audio or dashboards, audio alerts would work.
Still for the simplified attribute version.
I saw that there was no guidance around any kind of opt-in to details.
So that's why I bring it up here in the group.
Trask Stalnaker 00:55:56 I feel like the… in the past… these… I mean, we have added opt-in attributes on metrics.
Because they… because of the cardinality.
Of them, but some people may want them.
So I'd be… Is the… what's the reason for not doing that? Is it just that, like, metric views don't really support that well yet, and so it has to be instrumentation by instrumentation opt-in flags?
Christophe Kamphaus 00:56:32 You are asking, why not just make the whole… Detailed one opt-in, and not emit the simplified one at all.
Trask Stalnaker 00:56:42 Not emit the simplified one.
Liudmila Molkova 00:56:46 So I think the question, the choice here is… What are two… In a rich attribute value result.
Trask Stalnaker 00:56:54 Oh…
Liudmila Molkova 00:56:55 Worse.
Trask Stalnaker 00:56:55 Sorry, I missed that. Yeah, I get it.
Liudmila Molkova 00:57:04 And I think the pattern so far that we… We, we haven't… I don't remember a case where we change attribute.
Value based on the… Opt-in.
Bing.
Trask Stalnaker 00:57:20 Why isn't it just a second attribute that has the second component?
to it.
Christophe Kamphaus 00:57:29 Oh, okay, you mean just this one.
Trask Stalnaker 00:57:32 Yeah.
Christophe Kamphaus 00:57:34 Probably because, okay, you would see it better in the original PR.
Because it's not just a slash second component, it can also be inversed, and… It's picked up from the language runtime.
Yeah, so here… He created a mapping table.
Or… One of the attribute mappings.
So this would be the simplified one, and here it would be the detailed metric value.
Trask Stalnaker 00:58:28 Okay, so back in the… so I think… I understand now, I think, and having the second one that is the attribute detail.
feels… like, the… what we've done before, where it's… you opt into this new attribute, but as Lydmilla says… said, I don't think we've ever, like, had an opt-in to change an attribute value itself.
And I think that would be… could be confusing.
Christophe Kamphaus 00:58:57 Yeah, because it could break your dashboards if you have mixed services.
Where some are opted in and others not.
Liudmila Molkova 00:59:09 Yeah, I can see pros and cons to both solutions, but it… Sounds like weird.
Have the pattern, and… The proposed thing here totally matches the pattern that we have.
Christophe Kamphaus 00:59:25 Yeah, here's a pattern, it's more… But it's really one-to-one, and here it's just the first part of the attribute value.
But yeah, for the memory, it was not straightforward one-to-one.
Liudmila Molkova 00:59:46 Cool.
Trask Stalnaker 00:59:46 Yeah, but it makes sense to not… I can see why it makes sense to not strip the GC from that, because, like, it is a value, it does have semantic meaning, the whole thing together, it's coming from some data source.
Liudmila Molkova 01:00:10 We are at time, so should we just comment on the issue, saying that…
Christophe Kamphaus 01:00:15 Yeah, feel free to comment on it.
Basically, who you think it should be?
Should we give some guidance on this?
Or… Would we keep it case-by-case for now, when we see it in PRs?
Liudmila Molkova 01:00:34 I think it would be great to document the guidance, and Christopher, if you are upright.
It would be awesome.
And feel free, I think you're already on this issue, if you leave a comment, that would be great.
Christophe Kamphaus 01:00:46 Yeah, I will.
Liudmila Molkova 01:00:49 Awesome.
Trask Stalnaker 01:00:51 Thanks, Al.
Liudmila Molkova 01:00:52 Thank you.
Teen you?
Trask Stalnaker 01:00:54 Aye.
Armin (Dynatrace) 01:00:55 That's the…
