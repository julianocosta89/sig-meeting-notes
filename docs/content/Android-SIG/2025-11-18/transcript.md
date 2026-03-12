SIG: Android SIG
Date: 2025-11-18
Duration: 55 minutes
============================================================

## Zoom Recording Transcript

**Mustafa Haddara** 00:59 Good morning.
**Hanson Ho** 01:01 Hello?
**JP Jason Plumb** 01:03 Good morning.
**Bee Klimt** 01:08 Bye.
**JP Jason Plumb** 01:11 Still getting my laptop to understand all the things, now that it's back home.
**Hanson Ho** 01:18 What time did you make it back?
**JP Jason Plumb** 01:21 It's about 9.30.
**Hanson Ho** 01:25 12.30 Eastern Time? No.
**JP Jason Plumb** 01:28 No.
Which means I'm pretty awake right now, and I'm concerned about later tonight.
That's the way that goes.
Let me do one thing right here.
**Hanson Ho** 01:49 I've set up the temp… or the entry in the dock, so.
**JP Jason Plumb** 01:53 Thank you, I'm not there yet. Yeah, appreciate it.
**Hanson Ho** 01:57 No worries.
**Cesar Munoz** 02:02 Hey, good morning.
**Hanson Ho** 02:04 8?
**JP Jason Plumb** 02:05 Hello!
Still getting set up over here.
I think that's the right window.
But I forgot to tear it off, so let's try this again.
That looks better.
Well, the topic du jour at KubeCon… With stability, and also stability.
Seemed like there was a lot of interest in that topic.
So… I think it's good to have this as a top agenda item.
And to state our plan, To hopefully get Cesar's blessing in this, as co-maintainer.
So, the cons… I'll just… I'll kind of recap some of the discussions and distill it down, but I think, you know, the blog post we've been talking about that Austin posted went through a bunch of revisions. It ended up landing.
And it is kind of a north star for stability concerns around OpenTelemetry. Part of that is based on our interest in graduating within the CMCF as a project.
which we've been working on for some time, and… great. I mean, that's… that's awesome. We will get there. And stability is… is one component of that.
And… in order to go from, you know, a blog post announcing our interests, our collective open telemetry interests.
And by that, I mean Austin's blog post, not the Android blog post that I made. To go from that to, like, a really, project-wide… consensus, there will be a series of OTEPs that will probably happen, the open telemetry enhancement proposals.
And we expect those to take a number of months before they ever really gel. We, Android, are going to go ahead and cut an RC, And Cesar, you have, of course, veto power as a maintainer here, and definitely I want your input on this, because you were not able to make it to KubeCon. So, the basic consensus is we can cut an RC1 this month, we can even go stable.
Partially due to us being, grandfathered in, meaning the project has been around and working toward this, like, and we announced our intention to do this before… The concerns about stability, and mainly around having a component that's declared stable only including other stable components.
So we will… we will be fine if we go ahead and do that. We do have… as our own SIG, as our own project, we have our own amount of autonomy here, and our own agency, and we're allowed to do that. And if it gets… if it gets too out of control, then, you know, it's up to the GC and the TC to come slap us on the wrist and say, don't do that, you know, you need to align. But after talking with everyone.
In fact, more people than I expected asked about this stuff.
I think we're in good shape. So, I think, as long as… I haven't even checked yet, because I just got home last night, but I think Instrumentation was releasing last week?
Like, on Friday. I'm not sure that there are any dependencies that we need from contribib to be released, but if not, if there are, we can wait for contribib, and that can… or I can… I can probably do that today. And that's… yeah, that's a lot of words from my sleepy brain.
And I'm curious what people think.
**Cesar Munoz** 06:04 Got it, thanks for the details. I'm just curious, when you say that we're gonna cut an RC… release.
That's… Setting everything as stable?
**JP Jason Plumb** 06:19 Nope.
We will… Just the heat.
**Cesar Munoz** 06:22 plan at the beginning.
**JP Jason Plumb** 06:23 As we planned originally, yep, yep. Everything else will still have an alpha hanging off of it.
**Cesar Munoz** 06:29 I love that idea.
Yeah. To be honest. Yeah, sounds cool.
**JP Jason Plumb** 06:34 Yeah, and that allows us a pretty clear map to promote any of our alpha components to stable in the future without that being a breaking change. To go the other way around is much harder. You can't take something that's stable and then turn it back to alpha, but you can go the other way around, so… I think there's a pretty smooth path.
And then… so, I'm just gonna write it in the docs so that we have a record of this conversation, so…
**Cesar Munoz** 07:11 Actually, interestingly enough, Last week, it seems like there were a couple of people… asking questions on how to use the builder, you know, from Core.
And some of them wanted to do some custom stuff.
And it was a bit impressive to me.
Because… Well, I'm not sure if… maybe, maybe it's a… it's a… It's, it's, you know, we'll just, we'll just get the, the feedback or things that, you know, have issues, but then for stuff that's working well, we don't get any, probably. But I was kind of surprised, because I've, like, I think everybody had some feedback on the core builder.
And not on the, initializer API that, you know, has the Kotlin DSL and stuff.
So… it sounds like… It makes me think of… think of two things, which is… the first one is that, I guess it's a good opportunity to see what is it that's missing from the Kotlin DSL that people wanted to… You know, commonly, configure, and it's not possible right now.
And the second one, I'm also curious… of how much people are using Java.
Because it also seems to me that the people who prefer using the builder it's because they're not using Kotlin, so… I mean, I'm curious because it seems like the general idea is that everybody uses Scotland.
Or at least 99.99999.
percent, or something like that, and… I've just seen, I guess, more than that I… more people than I thought.
you know, using the Java-specific builder stuff, so… Just to keep an eye on that.
Also, I wanted to mention that… well, I know it's a bit of a short notice, but I'm planning, actually, to take some days off Sorry.
I didn't take my vacation this year, so far.
And so, the company's kind of like, you know, I have to take those days.
And, so… I'm gonna take the opportunity to also I have a surgery that it's quite small, and so I'm planning to merge the surgery, Rest in time with the vacation.
So, essentially, I'm planning to be back on… in January.
And, so seriously, I'm not planning to work for the whole month of December.
so, you know, Eve… like… If there's anything I can do this week, because I'm actually off by next week.
you know, please let me know. I'm willing to… I was gonna say that I'm willing to make some stuff stable, such as this buffering, if it's needed, because So far, nobody has complained about the API.
But apparently it's not needed, you know, based on what we were discussing earlier, so it's great.
Well, in any case, let me know, in terms of… I wouldn't like… Things to get blocked.
while I'm away, so… I don't know what's usually the… this… this… this… the, you know, the deal in these kind of scenarios, but I'm guessing during my absence.
I guess, Jason, you'll have the, you know, The… the… like, the full… Final world of things, and… that's great for me. I think we… we have really all… The… Scaffolding that we need to… to… To go stable, at least with the agent, so… So yeah, I don't know what else to say, to be honest.
**JP Jason Plumb** 11:37 Pretty much everything.
Yeah, good for you for taking that time, you don't want to lose it, and I feel like that's very rare that Europeans don't take their vacation time, so I'm glad you get to do this and extend it a little bit.
Even… even with the surgery as a… as a background drop.
**Cesar Munoz** 11:53 Yeah.
**JP Jason Plumb** 11:54 Yeah, I will be around. I don't have too many plans to take any sort of, like, extended time off.
I will probably take… a week or a half a week here and there, like, we have holidays next week in the U.S. is Thanksgiving, so we need to talk about that. But yeah, I'll be around to, to hold it down, and I'm looking to the approvers to help out with some of that, you know, stuff as it comes in, and If it gets… if it gets too… if it gets too out of control, I'll just get grumpy and… and, like, mention you on… on Slack, but I don't think it'll come to that.
Yeah.
**Hanson Ho** 12:29 We don't have…
**Cesar Munoz** 12:30 I think I can eventually take a look at Slack, just the same thing comes up.
**JP Jason Plumb** 12:35 I mean, I wouldn't sweat it, but yeah.
**Hanson Ho** 12:37 Yeah, Cesar, I would say take time to rest if you need, but if you do have a bit of time, I think one thing Jason and I were talking about at KubeCon was documentation is, could use, a bit more help, especially if we're gonna go stable, at least we should have a rough outline of what we have and what we don't have. So, I took a stab at it, updating, README, over there, in Atlanta. So, have a look at that and see if it's okay.
That's, like, the first step. There's probably a bunch of other things that we could do to reorganize, some of the documentation, and include things like, you know, these are the instrumentations, and these are the defaults, and so… so basic things that folks should know. if… if you could take a look at the, disk buffering documentation and see if it's sufficient. And if it's not, maybe add some. That would be great. But going stable is… is not… as big as I initially thought it was gonna be, I think.
I think because the ultimate being careful is too ridiculous to do, that the only logical thing to do is just call it stable, and then… and then, you know, annotate the hell out of things. So… now it's the annotate the hell out of things portion of it, so I think the code is ready, it's the documentation. I think that needs a little bit of a help.
I also have one PR that, I haven't taken a look at. I saw Jamie had some comments in there, about, doing some of the dependencies.
Because I think people aren't using the Rum Builder, because it's transitively being brought in, core, it's transitively brought in if you include just the base module, so people see both the builder and the initializer. So they say, hey, what should I use? I don't know. And I think if we're… if the idea is to push people to use the initializer, we should not make it so easy to access core. They have to explicitly include the core module in order to actually get to core.
So, I have PR that was on, you know, about that, and if we can get that done before, you know, we get stability.
And then make what we in the comments say is private. But it, in fact, is very much, Not part of it. Would be good.
**JP Jason Plumb** 14:51 Yeah, did everyone… did everyone follow this stuff? Did your other PR get merged already?
**Hanson Ho** 14:56 No.
**Cesar Munoz** 14:57 Okay. I… I haven't taken a look at this one.
I'll take a look between today and tomorrow, but I like the overall idea. It's essentially extracting the API to a separate module. Is that the… If I understood correctly.
**Hanson Ho** 15:11 Yeah, and not even the entire thing, like, more can go in there. The only thing that's being extracted out is the open telemetry RUM, so that's the interface that you really require, you know, with the initializer returning an instance of. The implementation of that stuff should be hidden… could be, and should be hidden behind core.
it is technically an API breaking thing, in the sense that their symbols are gonna be slightly different, I think.
But maybe not. I have to, like, look at the way Java looks at it, so… so…
**Cesar Munoz** 15:45 Yeah, no.
Sorry, I haven't… I haven't taken a look, but I'll do so before going on holiday. Probably… probably today, I think it's not a… I mean, it's got a lot of file changes, but it's probably just because of moving files, so… And I think it makes sense what you say about, you know, the builder being available, because it's public, or, you know, transitive, and so… I think it makes sense, and it probably is also related to the first thing you mentioned about Docs, because I think we don't, you know, show how to use the initializer in Docs. So… Yeah, sounds good. Thanks.
**Hanson Ho** 16:25 I think I… I think I updated the… I think the, the… my change for the README, changes, the sample code, or adds a chunk of sample code, that just uses the initializer, so…
**Cesar Munoz** 16:40 Awesome.
I'll have a look.
**JP Jason Plumb** 16:43 Mustafa.
**Mustafa Haddara** 16:44 Yeah, question. I'm looking at this Gradle, Gradle file for the agent, and it's got all the instrumentations that we're gonna mark as…
**JP Jason Plumb** 16:55 Yes, that we're gonna include, they are not marked stable, no.
**Mustafa Haddara** 16:58 Yes.
**JP Jason Plumb** 17:00 These will… It'll be alpha.
**Mustafa Haddara** 17:03 Yeah.
Do we have a way to disable those? Like, if someone comes along and goes, oh, I want to use Agent, but… the crash instrumentation.
is not working for me, or it's not doing what I need, I want to turn it off.
**Hanson Ho** 17:17 if you.
**JP Jason Plumb** 17:18 We do…
**Hanson Ho** 17:19 If you look at the repo and you don't see docs that say that, how you do that, that means those docs are missing, and we need to actually add them. That's the kind of stuff that we need before we.
**JP Jason Plumb** 17:29 That's a very good point, yeah. We do have an API in the agent to do that, to disable them.
Someone else that knows this better might be able to get me there faster.
**Hanson Ho** 17:43 the DSL has, has, basically, ways to access each instrumentation, to basically turn it off. But it's not clear what is on and what is… what the defaults are, and if I want to say, turn it all off, there's no way to do that.
So documentation would help.
**Mustafa Haddara** 18:04 Yeah.
**Cesar Munoz** 18:06 Yeah.
**JP Jason Plumb** 18:06 Yeah, I think it's for exactly the reason that Mustafa, I think it's for the reason you mentioned, is because, like, one or two of those might not work. Like, it's good enough for most people, but they might not want this one or that one, so they can… they can pick and choose.
And I forget, and we don't have an example, so yeah, that's a really good point. So, help wanted on documentations showing that example.
Okay.
**Hanson Ho** 18:42 I've got a bit of time set aside today to… to do some of this stuff, so I'll take a look at what's, what's needed. Or if there are tickets out that say, hey, we gotta, we gotta, you know, go and write this documentation before we GA, or not GA, but go stable, whatever we want to call it.
**JP Jason Plumb** 19:01 Cool. I know we had a discussion around this, but I don't know that we have it written down in the repo yet, so if someone were to come along with a Java app, and they're like, hey, does this support Java, or is it cotton only? I don't think we have it written down.
Am I correct? Because I'll file an issue to at least track that. I think we should have it written down in our docs as, like, as a rationale.
**Hanson Ho** 19:23 I could… I can… I can take a stab at that. At this today. That…
**JP Jason Plumb** 19:28 Okay, cool.
can change.
**Hanson Ho** 19:32 Change it to me to follow… Which is to write it.
**JP Jason Plumb** 19:37 Okay. Yeah.
And, I have found it handy… we have found it handy over the years in the Java repo to have a place that points to certain decisions that we collectively make as a special interest group.
And… cause they will come up over and over and over, and you know, like, some of this will overlap with semantic conventions, like, people are gonna come in and be like, why is this session modeled as an event, or why is this session, like, an attribute? Like, that stuff will still come up, and until we get that codified in semantic conventions or spec.
maybe we don't put too much here, but stuff that is Android-specific, like this decision to… like, maybe we're interoperable with Java, but we do favor Kotlin first, I think writing that down is still helpful.
**Cesar Munoz** 20:24 Yeah, and I…
**Hanson Ho** 20:26 Go ahead.
**Cesar Munoz** 20:27 I was just gonna say that it would be nice to have that kind of page, because I already have, a candidate or something that we can add there, which is something that came up last week, somebody created a PR to… for the… to modify the OpenTelemetry ROM interface, I think it was.
Yeah.
To, to… To make the getter… Vowels, you know, coupling vowels instead of getters.
And then we had a discussion, Around, you know, why… You know, when to use VAL, and when to use getters, and… It was a kind of a big discussion.
But in the end.
We decided to kind of follow what some of the coupling code, style stuff is, which we can link to. So, anyway, I'll send the link.
But it's one of the stuff that I… I mean, it sounds great to have this kind of page, people can go and see why we made some decisions.
**Hanson Ho** 21:36 And I think…
**JP Jason Plumb** 21:37 Yeah, agreed. And I think dropping it in here as a new file would be great. It doesn't have to be all of our rationales in one doc. It can just be, like, a one-page, like, here's what we, like.
here's our rationale around Kotlin first, you know, and have that just be its own doc, it's one page, and we can edit that. Doesn't have to be, like, one huge doc that has all of our decisions in it.
I think this is a good place for, like, especially a starting point for docs and examples. I don't think we have an examples directory yet.
But maybe it could be a subdirectory.
If we want it to be, like, more narrative style, and not just code-code.
Yeah, well, and then, you know, promoting stuff out of here into the dock site as it becomes relevant.
**Hanson Ho** 22:25 Yeah, some background about this Java versus Kotlin thing. This is more to do with, preferring the Java syntax and… not really making it super… not making a huge effort to make it, like, super nice in Java, so, like, using default parameters, but not necessarily providing a bunch of overloads, if not necessary. So if you can pass in, like, parameters to initialize, you know, something in Java, that's good enough.
you know, the fact is that most people coming in, or most projects, will be in Kotlin. Those that aren't, and those that prefer Java, are probably not necessarily Android developers first. They, you know.
So while we shouldn't make it, like, not work in Java, we should always prefer if, you know, the Kotlin syntax, Kotlin idioms, if possible, because this is… This is an Android project.
**JP Jason Plumb** 23:21 Yep, exactly that. And the stuff we talked about before, which is… which is more of that.
**Hanson Ho** 23:26 Oh, yeah, that's it.
**JP Jason Plumb** 23:28 Yeah.
Okay, yeah, I've been mostly ignoring the repo in the last week, because I've been traveling and busy, so I've got some catching up to do. Is there anything else? I want to make sure that we give a chance for… Jamie B. Mustafa, anything around stability or cutting an RC1 this week that you think is… concerning, that you might need… might need a little bit of massaging or alignment, I just want to make sure you have a chance to… Bring up anything you're thinking about.
**Jamie Lynch** 24:06 Yeah, I think, Hansen's change about, the call module not being included by default would be good, just because that minimizes the surface area.
But I feel like it's a pretty small API, I'd be happy with making that.
Particular modules table.
**JP Jason Plumb** 24:27 Cool. Hanson can confirm this, but I think I had him explain this problem 3 times to me before it made sense. I was like, wait, why… why would somebody be using the Rum Builder if they're including the agent? Like, I couldn't get my head around it, and finally I do now, and I think that makes sense.
Okay, anything else from you, Jamie?
**Jamie Lynch** 24:50 Nope, that's it.
**JP Jason Plumb** 24:51 Okay.
Pierre Mustafa, anything you're thinking about around this stuff?
**Bee Klimt** 24:57 I need to play with it hands-on before I have an opinion.
**JP Jason Plumb** 25:01 Fair enough.
Okay, cool.
Well, we have a lot of… we have a lot more time. We can, we can go over some issues and PRs if they're of interest.
Judging by this blue line, there's quite a few new issues that I haven't yet seen.
Oh, and is this a week for Client SIG?
**Hanson Ho** 25:31 No, it's next week.
**JP Jason Plumb** 25:33 Okay.
Someone… there is a… is there a PR or an issue? Let me find this. There's something about the click… The click instrumentation on web… might look considerably different than it looks in Android, because we kind of blazed the trail there, and I think there's some desire to maybe see about aligning those, but it doesn't have to be… And if we're not meeting today, we're not meeting today.
What we should talk about is Thanksgiving week, so next week.
Is Thanksgiving in the U.S.
Which means… and that's… Thursday… Think we could still meet.
I think we could still meet Tuesday.
Yeah, I think that's fine. Okay.
Let's… let's plan… and I don't think that'll change. I think we can still meet on… on… on Tuesday.
**Hanson Ho** 26:39 A few of us are not in America as well, so I'll be… actually, honey, I will be in America on Tuesday.
But… I'll be able to meet, I think.
Like, north?
**JP Jason Plumb** 26:51 North America, or…
**Hanson Ho** 26:54 I'll be in America, America.
**JP Jason Plumb** 26:58 Yeah.
**Hanson Ho** 27:04 And Cesar, you're off starting Friday, right? Your last day is Friday?
**Cesar Munoz** 27:09 Yes.
Yeah.
**Hanson Ho** 27:21 Oh, you also added a bug about disk buffering. Disk buffering not on by default. Is this, Is that… is that still an issue, or…
**Cesar Munoz** 27:35 Yeah, I… It's, It's just that it's… the default in the DSL is to get it to be enabled.
But… the DSL… It's kind of like, that code, it's kind of dead, unless… people actually write the disk buffering part of the DSL.
**Hanson Ho** 27:57 Oh, okay, I get it.
**Cesar Munoz** 28:00 So it's just a matter… I mean, I haven't… I haven't taken… A deep look at it.
It was kind of quick, but essentially, it's just a matter of calling the, part that initializes the default disk buffering DSL config without having to wait for users to actually, you know, call that part of the DSL.
If it makes sense.
**Hanson Ho** 28:23 Yeah, I would think that the default object would be created if none is specified, but it's weird that it's not.
**Cesar Munoz** 28:33 Yeah, I'm not sure if it's just a lazy object or something, I haven't… seen the… the details. Was… took a quick glance at it.
**JP Jason Plumb** 28:43 Yeah, so I put these… I put these labels on there. I think we need to fix that for RC1. It's something we… I mean, that's our main API, we say it's on by default, and if it's not, then we should fix it.
**Cesar Munoz** 28:55 Probably can have a loop before… before Friday.
**Hanson Ho** 28:58 Cool.
**JP Jason Plumb** 28:59 Cool, cool.
I don't think we have many issues left yet. That's the only one in the milestone right now.
**Hanson Ho** 29:20 If there's… Anything that folks think we should do before we declare the agent.
RC, or, stable, or cutting RC, let's raise it and tag it with F, so that, you know, we don't go and… miss that when we do this, especially docs, like, if they're, like, specific docs. Let's track that.
**JP Jason Plumb** 29:43 And I think approvers should have the ability to add labels, and I think milestones?
So if you're looking at an issue like this, for example, I think you can… Yeah, over here, I think you can do one of these and put it in there.
**Hanson Ho** 29:56 Cool.
**JP Jason Plumb** 29:57 I don't know why that 14 is still hanging out.
How do you even remove that?
**Cesar Munoz** 30:06 I haven't used that feature too much, to be honest.
**JP Jason Plumb** 30:09 The milestones. They're pretty nice when you have a bunch of work that you're trying to keep track of.
Toward a specific release. I mean, the labels are good too, but the milestones are kind of intended to be this. Is it projects?
No, I forget how you see that. It might just be issues.
And then do you get into it through… Oh, here it is, look, milestones.
Yeah, can I delete it?
It's foreclosed. Yeah, we can delete that.
Okay.
That's how you do it.
We all learn together.
**Cesar Munoz** 30:48 Nice.
**JP Jason Plumb** 30:58 Yeah, this might be an interesting one as well. Looks like some folks have looked at this.
**Cesar Munoz** 31:09 Shit… Yeah, forgot about that. I think they created a PR, actually. I haven't checked it.
I'll have to do that this week.
It's essentially they want to customize the, the, the processor that we create.
That's pretty much it.
We don't have a way to customize it right now.
**JP Jason Plumb** 31:42 And are they using the agent?
**Cesar Munoz** 31:46 No, the builder.
**JP Jason Plumb** 31:51 So, they're a span processor, or… yeah, so span processor, huh?
I thought we had a way to do that through the builder.
**Cesar Munoz** 32:02 We can customize the, tracer… provider Builder.
Where you can add processors. But then, if you have your own processor, you don't… get access to the exporter that we provide into our internal processor, and they kind of, like, I think they wanted to grab the exporter that we create within their own processor.
**JP Jason Plumb** 32:27 They should be able to do… I'll have to look at the PR and see how it gets there, or how it's an improvement, but I think they should be able to wrap the existing processor.
**Hanson Ho** 32:38 Not the whole customizer stuff was… was… that's what it does.
**JP Jason Plumb** 32:41 Yeah.
**Hanson Ho** 32:42 Is that just…
**Cesar Munoz** 32:43 what I remember… From what I remember, I think you can customize the exporter, but not the processor.
You can add other processors, but they won't have the exporter.
That, that we create.
**Hanson Ho** 32:55 We still need to mix in, basically, the processor into our chain of stuff, then.
That venture goes to, you know, our processor, so yeah, that makes sense.
Or, exporter.
**JP Jason Plumb** 33:20 Okay, well, there's some… there's definitely some triaging. I appreciate folks jumping in and commenting and looking at issues and stuff as they come in. That's really, really helpful.
And yeah, I mean, just given the number, I can just tell at a glance, like, the number of comments and PRs on these things being non-zero is really… is really helpful, so thank you.
**Hanson Ho** 33:41 We may want to not discuss this today, I don't know if we have time, or, you know, maybe next week, talk about, a more formal triaging process. I think the volume of stuff is getting higher than what you two could… well, especially if with Cesar's off for the rest of the year, of what you can handle, Jason, we might want to find a way to distribute this a bit.
**JP Jason Plumb** 34:06 Yeah, I think… I think that's great. So, I mean, I think that is very much important. I think we can talk about that as a group as well. I do wish Manuel was here. I think we can, There is something in… One of the repos that talks about roles and triager?
Yeah… Yeah, I was, I was, like, especially, like, a few years ago, I was always surprised when I found this kind of stuff. I'm like, there's all this, like… internal, like, project-y maintenance management stuff, but I guess that's what you do when you have a project of a certain size, you know? Yeah. But, So, responsible for applying labels defined below. So basically, if a new issue comes in, and you're like, oh, that's definitely a bug, like, putting bug on it, submitters will often put bug on there when it's not a bug, so, like, removing bug when it's not a bug.
I don't think we have these labels at all.
**Cesar Munoz** 35:17 I don't remember.
**JP Jason Plumb** 35:18 I wonder if what I clicked is, like, specific to the spec repo?
And not the project.
**Hanson Ho** 35:33 Probably.
**JP Jason Plumb** 35:33 I bet you it is, like, if I go here, I think I probably clicked on the wrong thing.
**Hanson Ho** 35:39 I would say, though.
**JP Jason Plumb** 35:40 This is specific to the spec repo, my bad.
**Hanson Ho** 35:43 conceptually, I think that's a good way of… actual triage, you know, in the old definition of the word triage is basically to sort through, you know, we can fix this, this person's gonna die, you know, ignore it. We should have that process of processing it once before we even have to go in there and make detailed comments.
So having, having actual triaging, into, like.
Streams before we process further is probably a good idea.
And that'll make, you know, the job of maintainer easier, because you don't have to, like, read every single one.
**JP Jason Plumb** 36:17 Totally, and I think another aspect of that, too, yeah, so applying… like, bug especially.
When it's a bug, that way it stands out.
The other thing I think that is low-hanging fruit sometimes is when people… When users file issues that are not very clear, just asking for clarification, like.
Can you pro- can you provide an example? Like, what's your intent with this? Like, why are we doing this weird edge case we never thought of? And, like, getting… getting some additional clarity around that, and then label… using the… requires author feedback, I think is helpful. If it's, like, apparent that it's, like… if the issue is kind of lazy or vague.
Using that needs author feedback, which I think we probably don't have many of those right now, because we have automation that closes them, which is really helpful. Also, if you're like.
hey, if you're looking at a new issue, and you're like, hey, the maintainers actually need to take a look at this, it's a bigger decision than, you know, using needs maintainer feedback, but let's see if we have any of these. Yeah, we don't have any currently, because they get closed after a week, I think.
Because, yeah, definitely users will come and just, like, they'll just shotgun or just, like, throw stuff over the wall as an issue, and… That's not the way the process is supposed to work. You're supposed to help us to help you.
**Cesar Munoz** 37:51 Do we have a similar attack for PRs? Sometimes people open PRs that are not, you know, clear.
The intention, or…
**JP Jason Plumb** 37:59 We don't? Yeah.
**Cesar Munoz** 38:01 If the system is gathered.
**JP Jason Plumb** 38:03 I mean, you certainly.
**Cesar Munoz** 38:03 Recently.
**JP Jason Plumb** 38:04 You can label any PR, I'm just gonna pick an old one as an example, because this is a year old.
You can put that label on here.
Because labels apply to both issues and PRs, but I don't know if the automation handles that. I don't think it does.
Let's find out.
**Cesar Munoz** 38:25 I'm mostly curious, so I think it's a great… System.
**JP Jason Plumb** 38:31 Do you remember which one it is?
**Cesar Munoz** 38:40 No, sorry.
**JP Jason Plumb** 38:45 So maybe it's this one. So… it'll move it to stale after 21 days, and it will close it after another 14 days. So only the labels that say Need Author Feedback.
And I'm not sure if this applies… I don't see anything that's specifically calling out PRs, so we should be able to do PRs, and then stale.
And then remove clo-open.
Yeah, so these were marked needs author feedback. These were PRs from back in February.
And they went stale, and it looks like…
**Cesar Munoz** 39:37 Yeah, it works.
**JP Jason Plumb** 39:38 It looks like we added that, and then it got marked stale, and then it was closed. So yeah, it does work on PRs, yeah.
**Hanson Ho** 39:43 Cool.
**Cesar Munoz** 39:44 And I did… I did mark it as needed… yeah, I forgot about it.
**JP Jason Plumb** 39:48 Whatever, man, it was, like, all the way back in January.
**Cesar Munoz** 39:54 That's pretty cool.
**JP Jason Plumb** 39:56 Yeah, Yeah, I like that better than just labeling it stable manually, or stale manually, because it gives them a little… a little more time. So it's, what, 4 weeks and then another 2, so 6 weeks is pretty generous.
But also, if we just get in the habit of using that, then it doesn't build up too much. There was a… there was a, an effort in Java that went really aggressively and started marking stuff that was… that had no comments.
after 9 months or something, so any issue that had no comments was gonna mark stable… Stale. I got stable on the brain, sorry. And they managed to automatically close, like, hundreds of PRs and issues across the few repos.
Just because… As a mature… as a project matures and grows up, you get a lot of stuff in… in the history here, and I mean, we should… we should be a little bit better about cleaning up some of this older stuff, like… I think anything that's over a year is probably not gonna get merged. It probably can't be merged.
**Hanson Ho** 41:01 There you go.
**JP Jason Plumb** 41:01 There's been so many changes, but, like.
This is a cool feature, like, we all want this, but this person, why is it so slow?
Come on, GitHub.
It's like pulling it out of, slow storage or something right now.
**Hanson Ho** 41:20 That's probably exactly what it is.
**JP Jason Plumb** 41:22 Oh my goodness.
Look at this just crawling.
**Hanson Ho** 41:28 Oh…
**JP Jason Plumb** 41:29 That's amusing to me. It… that's so…
**Cesar Munoz** 41:31 What an OPR.
**JP Jason Plumb** 41:33 Yeah.
**Cesar Munoz** 41:33 Thank you, huh?
**JP Jason Plumb** 41:34 Frozen.
Yeah.
I mistakenly clicked again, and now we're waiting for the crawl again.
But yeah, like, June, I remember…
**Cesar Munoz** 41:51 person…
**JP Jason Plumb** 41:53 Go ahead.
**Cesar Munoz** 41:54 I think I remember this person, they said that they will take another look.
And that's why we kept it open.
Or maybe I'm… I'm not sure if I'm mixing some stuff up, but… But then they didn't come back.
**JP Jason Plumb** 42:07 Yeah. So…
**Cesar Munoz** 42:10 Yeah.
**JP Jason Plumb** 42:11 Well, this PR is also not coming back.
Yeah, like, this one I'm leaving out here just because it's a reminder that we need to do something about this, like… You know, the instrumentation doesn't apply cleanly anymore.
After a certain version, and we said that we wanted some integration tests to fix that, and I think Cleverchuck was gonna help with that, but hasn't really happened.
I mean, we could just pin that version and move on, But… It would be nice to not have instrumentation that goes stale.
**Hanson Ho** 42:44 The problem with Compose, this specific instrumentation, is that we're relying on internal API… well, not even APIs, internal methods to latch onto, in order to actually, detect what is going on. So I think, like, the Embrace Tap instrumentation also breaks at a certain version, so… or rather, doesn't work, you know, up to a certain version.
So this is a continual, you know, you know, what's that? Whack-a-mole.
it's problematic, to say the least, but it is what it is. So, if… if, not this PR, but the other one, if we want to say, hey, it doesn't work for a specific version, we should have documentation that says that, and then basically close it out and say, have an issue outstanding, and say, somebody can go and fix it if they want. But… you know… We'll see.
**JP Jason Plumb** 43:39 Yep, I mean, maybe the… maybe the… maybe the move, and I think we already have an issue on that, is… I was gonna say maybe we just close the PR and open an issue to track it, but… Let's see…
**Hanson Ho** 43:53 Does this PR, like, break the existing test? Is that why, is that why it's… was it merged?
**JP Jason Plumb** 44:00 Yeah, it does.
**Hanson Ho** 44:01 Okay.
That's good, then, that the test caught it, I guess.
**JP Jason Plumb** 44:06 Totally.
Yeah, so it's on this test… We're not gonna have a… we're not gonna have a Gradle build anymore that works, I'm sure.
**Hanson Ho** 44:19 No.
Yeah, it's even locking it, so it's like… may not… it may actually even work, it's just the test.
**JP Jason Plumb** 44:39 Yeah, it's been a while since I've looked at it, but it was, like, it was… there was no… there was not a good path forward.
**Hanson Ho** 44:44 Okay.
**JP Jason Plumb** 44:47 And then the rest of these, like, you know, June is whatever, like, September, I'm not gonna mark that stale, like, any of this stuff is still, like, fine.
I think draft is interesting, because… it's, like, an indication that someone, like, had some ideas, and they were playing with it, maybe they want to revisit it. And I'm not picking on you, Jamie, this is, like, for anyone that has a draft PR in any repo.
I don't mind those sitting out there for quite some time.
But, probably not indefinitely.
**Hanson Ho** 45:17 Well, draft… draft means that folks shouldn't be looking at it yet, right?
**JP Jason Plumb** 45:22 Typically what that means, although it's a… it can be a mechanism to… I mean, so by default, I would say that we as approvers, triageers, maintainers should not be in the habit of looking at draft PRs. Like, if you see one, and you're bored and curious, by all means, go for it, but I don't think it should be prioritized.
As a submitter, you certainly can request review from other contributors if you have an idea that you're just looking to vet or get feedback on early, so I think that's a great mechanism for that.
But yeah, I'm not… I think typically you're not going to expect a review while it's still in draft.
But yeah, okay. I don't know that we did what we said we might do here, like, to describe our formal triaging process, but, does anybody else have any other words they might add to this when thinking about what triaging should entail?
**Hanson Ho** 46:26 I think it's… it should be… it should be fast. It should be, like, you know, I think it's hard to, like, look at an issue thoroughly and give feedback, but if it's just, like, is this a problem? We should look further, is this a bug? You know, we should be able to do that very quickly. And I think it'd be nice if we could, you know.
have, like, a rotation of, like, for the approvers or something like that, to spend, like, 10 minutes or something like that, to just take a look at the incomings. It's one of those things that the backlog is big right now, because we haven't, like.
tagged a bunch of stuff, but the rate of things coming in, I don't think it's gonna be more than, you know, 5 to 10 a week. So hopefully the triage process is gonna be fast, and then we could actually deal with the discussions and things like that, either in Slack or in this meeting, as they come in.
**JP Jason Plumb** 47:10 Yeah, this one's interesting, right, because look at how many issues they have, and of course the spec repo just gets.
**Hanson Ho** 47:15 Sweep.
**JP Jason Plumb** 47:15 on constantly, and we don't quite have the same, problem yet, but it might be nice as… a maintainer to see that someone has already looked at it, like someone who's not me, or Cesar, have looked at it.
Just by, like… like, I don't know, this is new, right? So I'm guessing this is automation. No, someone commented, okay, so… these labels… Like, they're… they don't… I don't know, they… they use them sometimes… Like, that would be… it would be kind of nice to, at a glance, be able to tell that a triager or someone else has looked at it.
But we don't… I mean, we'd have to create a label, and it would have to be kind of generic.
**Hanson Ho** 48:03 That's fine. I mean… like, having a triager go in there and basically apply a label, whatever it is, at least indicates that someone's looked at it. I think that would be useful, and we should not have no unlabeled issues.
you know, 48 hours, or some other SLA that we could actually define and say, hey, we're gonna… somebody's gonna go and label an issue.
You know, in a certain amount of time.
However…
**JP Jason Plumb** 48:30 This level of detail is bonkers. Like, this would be too much for us.
**Hanson Ho** 48:34 Yes.
**Cesar Munoz** 48:38 But it's right now.
Yeah.
**Hanson Ho** 48:40 I'm basically thinking, like.
needs more time to look further, and then, like, and then, like, some obvious stuff, like, you know, needs clarification, or bug, or… or whatever. So, like, a simple flow chart with, like, 3 or 4 states, I think, would be… would be fine. And the triage will just go into, like, needs to look later.
And, you know, needs clarification. Even if it's just that.
**JP Jason Plumb** 49:04 Yeah.
Well, we could try it, what do folks think?
**Cesar Munoz** 49:12 It sounds good to me, it's just that I won't be here.
**Hanson Ho** 49:15 Nice.
**Cesar Munoz** 49:16 couple of weeks, but… but yeah, once I'm back, it sounds really good.
I'm not sure… I don't guess… I don't think we should have all the… labels defined right now, but as Hanson mentioned, it's… as long as there's some label on it, even if it's not Specific enough?
I think that the bulk one and the needs outer… Feedback… It's probably enough, at least at the beginning.
Not sure what else.
**Hanson Ho** 49:46 Or even one that just says, hey, maintainers need to look at this, more carefully, or something like that.
**JP Jason Plumb** 49:53 just to pick on some random one, like, what… no, that's a bad example. Just like this one. Okay, so… Like, if this was new, and it just dropped, like, seconds ago, what would you label this?
Like, so this is… I want to do something extra with slow rendering.
Okay, so that's an enhancement, right?
So putting that on there, I think, is reasonable.
And that's at least an indication that someone has looked at it.
Right.
And what else? Yeah. Is there anything else that's also… This is mostly the default set, we've only added a few here.
**Hanson Ho** 50:38 Is there a question here, or is this a feature request?
**JP Jason Plumb** 50:42 Oh, look, there's also one for slow rendering, so that would be, like, another label to put on there.
Right?
I think a lot of our instrumentations have a label.
And if not, we should create them.
**Cesar Munoz** 51:01 And when… when I label… when we set enhancement, I just wanna… be clear with the expectations of people. Does that mean that, I mean.
I don't think it should mean that it's decided that we will add that enhancement.
So, just mentioning in case, you know, It might cause confusion.
**Hanson Ho** 51:26 So I'll also put something like, maintainers, like, need to look at this, or something like that.
Maintainers or approvers, or something like that.
**JP Jason Plumb** 51:36 Yeah, there's the needs maintainer feedback.
I mean, that would also work in this case.
**Hanson Ho** 51:43 Nope.
**JP Jason Plumb** 51:44 Like, if you were reviewing Hanson and you put that on there, I would not be surprised or weirded out by it. Like, they think it was totally, totally valid.
**Cesar Munoz** 51:52 Yeah.
**JP Jason Plumb** 51:53 to Cesar's point, I hope that there's no confusion about this. This is not a statement of acceptance. I mean… It's just, like, what you're asking is an enhancement, and not a bug.
Or not a question, right? I think it's just a different… Stuff that makes it… Richer, better, without being classified as one of those other things.
**Cesar Munoz** 52:20 Yeah, at least we know that we… you know, can take our time to take a look at it and see if it's feasible, whereas with Bug, we know that we have to take a look at it as soon as possible.
**JP Jason Plumb** 52:32 Yeah, we don't have a… we don't have a disk buffering feature. We don't have a disk buffering… label, but I think, you know, we've had enough issues come up about it, or questions come up about it, that it's probably worth having.
**Hanson Ho** 52:44 That's more of a canthink, run builder initializer.
**JP Jason Plumb** 52:49 Yeah, I mean, it's true, and they did do that.
**Cesar Munoz** 52:57 Can… So maybe… it's maybe good to have a label for all of the… which is probably what you just said, Hanson, to be honest. All of the configs that are not available in the DSL.
Like, whenever somebody finds something that is not configurable via the DSL, then we label it so that we know if we need to add it or not to the DSL.
**Hanson Ho** 53:21 Well, the good thing about DSL is you can add more stuff in there and not have to worry about it, right? Unless things are, like, truly, truly private-private, but most of them are not. It's simplification, and if it's in DSL and there's a reasonable default.
then it's like, you know, nobody's worse if it's available, so that's the kind of thing that I think, yeah, we can start doing. But as, like, a basic triage, having that label would be nice, but I don't even think it's necessary at this first pass. It's almost like maintainer feedback, you know.
You know, the requester, you know, feedback.
anything else is gravy. It just… it just means that somebody… there is… there is a label that indicates who should look at this next.
And I think that's… that's the most important thing.
**JP Jason Plumb** 54:09 Yeah.
**Cesar Munoz** 54:11 Yeah, makes sense.
**JP Jason Plumb** 54:32 All right. Well, we've kind of hit our time. We do have technically 5 minutes left, but if we want to model after other SIGs, we can end at 5 till.
And give people a chance to switch gears before their next meeting.
**Hanson Ho** 54:46 Sounds good.
**JP Jason Plumb** 54:47 Cool. Well, I will start, I will start running the process for our C1. It's very exciting.
And, you know, if the build works smoothly, I'll bias all around whenever we're together next.
**Hanson Ho** 55:01 Sounds great. Good luck.
Bizarre, see you next year. Happy… Merry Christmas, Happy New Year.
**Cesar Munoz** 55:07 Thank you.
**JP Jason Plumb** 55:08 Yeah, take it easy, Cesar, enjoy your time off as much as you can.
**Cesar Munoz** 55:13 Thanks.
Alright, well, talk to you later. Bye.
**Hanson Ho** 55:16 Got it.
**JP Jason Plumb** 55:16 Bye!
