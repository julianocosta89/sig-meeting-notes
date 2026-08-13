SIG: JavaScript SIG
Date: 2026-08-12
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Abhinav Mathur 00:00:17 Hello.
Trent Mick 00:00:48 No, no.
Abhinav Mathur 00:00:55 ill.
Jamie Danielson 00:00:59 Hello.
I was just gonna give it.
A minute or two to see if any other folks trickle in.
Okay.
Inc.
We have a few folks here we can probably get started. I can't remember if we have any, like, standing amount of time that we want to give it. I feel like I usually wait too long.
Okay. So, Trent, you have the first topic on the list.
Trent Mick 00:02:33 Yeah, which one's that? Is that the user interaction one? Let's come back to that. If I see David pop on, I want to task him. But, actually, he…
Jamie Danielson 00:02:43 I mean, this has been in there, too.
Trent Mick 00:02:45 People got merged.
Jamie Danielson 00:02:46 Depression before the merge?
Trent Mick 00:02:48 Yeah, no, I'd reviewed it, and I wanted a browser or someone to take a look at it to make sure it was the same.
Cool. Looks like David did. So, done.
Jamie Danielson 00:02:57 Nice.
Roll?
So next up, we don't have Marylia here, But, so she had, need someone to collaborate to create update documentation on ODEL. Oh, I'll give it one more second, because it looks like Marylia just joined.
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:03:16 I just heard my name, and I joined.
Jamie Danielson 00:03:18 That's true.
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:03:19 I got someone.
Jamie Danielson 00:03:20 Like, wait a minute, I hear my name!
Hey, yeah, so we were just, coming up to your topic, for collaborating to create and update documentation here.
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:03:30 So basically, so we are having this issue on, like, the hotel.io that A lot of content is being created, and we have very few maintainers, and, like, crazy amount of blog posts that are being created, like, updates for, like, just the content itself, like.
the equivalent, like, okay, JavaScript updated something on the documentation, and it's been hard for us to keep track of everything, so this is why we always ask for the owning, like, SIG to review first, and then we have to, like, take a look and approve.
But we have been doing something with the localization that is kind of, like, similar, like, the maintainers of that language can review first, but now they have a command that they can merge. They don't need to be a maintainer of comms to re-merge things related to their own, area.
So we want to start doing this, not just with localization, but with everything. So, for example, now if JavaScript want to update the documentation on it, somebody can just create the doc, like, create the update itself.
And then they have the command to merge without the need for us. We still want to look, like, provide guidance if things are, like, not in the right place and things like that, but this is a way to also give, like, more autonomy to the SIGs to own their own, documentation, and so… basically, I say, like, okay, I can… we want to, like, test it out with a few SIGs, so we're going to do, like, the Java, and I offer to do the JavaScript, but the thing is, like, I am an admin on the org.
So if I try this, everything's gonna work for me, because I have, like.
So, I can, like, maybe if there is, like, any documentation that we want to update, I can, like, work on the documentation, or someone else can work, but I just need to pair with somebody that then can run the commands that don't have all those permissions that I have, just to see if this works, and also just get, like, any feedback if this process makes sense.
Jamie Danielson 00:05:34 Okay, so…
Trent Mick 00:05:36 And this is, okay, well, I haven't read this stuff. What's the mechanism that's being used? You talked about process.
Anyway, I was gonna volunteer.
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:05:45 Yeah, basically, like, you open a PR, normally, like, some other maintainer from the JavaScript does the review, and whenever we think we are ready, there's, like, a comments that you can just add, and that comments will merge your PR. So that is the flow.
Instead of, like, having to wait for… Any of us to merge.
Jamie Danielson 00:06:05 Right? So, like, if someone, like, came in with a PR and said, oh, actually, I want to change something in this code snippet sort of a thing, then, like.
I could go approve it and merge it in without.
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:06:19 Yeah.
Jamie Danielson 00:06:20 for a docs maintainer specifically to merge.
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:06:23 Correct. Yeah, so you have to be a maintainer of the SIG, so this way, like, not other people, like, merging left and right, so whoever… because we have, like, the code, like, the owner of that part, so from that, we can see if the person adding the comments, it is a maintainer.
That, like, for that part of the calls, then the… the flow would work.
Jamie Danielson 00:06:51 I was not in here.
Yet.
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:06:54 So yeah, part of, like, this workflow, I think we need still to do some updates, because I wanted to check, like, here first, if you guys are okay with doing the test, and then we can add the flow.
Jamie Danielson 00:07:06 Yeah.
Yeah, so, like, a change that happens in here, someone of at least JavaScript approver status is okay to approve it. Do you have an… is your question then, do we have, like, an open PR where we want to test it now to see if that works?
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:07:22 So I don't think right now it's gonna work, because I… the, like, Patrice is still updating the… the script to be able to work on this, but I just needed to have, like, somebody to, like, help, like, volunteer to work with me on this.
Trent, I see a hand. Okay, cool. I will let you know when I need your comment. Great.
Trent Mick 00:07:42 Great, thanks.
Jamie Danielson 00:07:53 Okay, cool. So, like, TLDR changes to public docs on JavaScript content can be approved and merged by JavaScript approver, not required to have docs maintainer to merge.
Cool.
Trent Mick 00:08:19 I'm curious, also, how we'll deal with the browser.js overlap there, too, whether we just decide to lump us all in together.
That's okay. We could be reasonable, I guess.
Jamie Danielson 00:08:30 Yeah. I mean, I feel like we often defer, like you did on the PR that we just talked about, we do often defer to… if it is browser, we probably want someone who's more familiar with browser to take a peek, and probably vice versa.
We've generally been pretty good with that, yeah.
Okay.
Cool.
Next up, Trent.
Trent Mick 00:08:54 Okay, this one's huge. I'm inclined to put this one at the end.
And do the other ones below, so that we don't starve all the other points.
Jamie Danielson 00:09:02 I might copy and paste the whole thing down to the bottom, is that cool?
Trent Mick 00:09:07 Yeah.
Jamie Danielson 00:09:09 So I don't forget to come back to it.
Okay. Also Trent.
Trent Mick 00:09:16 Okay, so there's a P1 on HTTP instrumentation. I did a review. I have a couple.
Subjective comments on it, so, other reviews would be welcome.
I don't think it's a case that's gonna hit people frequently, so it's not like we need to stop the world, but Take a look. It's a bit wordy, because I suspect I don't know that this AI is used to generate this, so it's a bit wordier than maybe it needs to be.
Anyone?
And that's it. Let me get my phone.
Jamie Danielson 00:09:50 Cool.
Okay.
Next.
I don't think we have this person on the… No, I think we…
Trent Mick 00:10:03 is pron.
Jamie Danielson 00:10:04 country.
Trent Mick 00:10:07 Oh, no, maybe not. Okay.
Jamie Danielson 00:10:08 Aw, sure.
Trent Mick 00:10:08 My mistake.
Jamie Danielson 00:10:10 We can take a…
Trent Mick 00:10:13 Maybe just links for now. This was… this is what Aaron was mentioning last week, I think, right?
Jamie Danielson 00:10:18 Correct.
Trent Mick 00:10:20 matelets.
just note the links for now, and if Bernav shows up in the next little bit…
Jamie Danielson 00:10:25 Oh, okay, they're just, tracking issues, it looks. Oh, no, wait, one… Is an issue, and one is a… PR. So this is a tracking issue for generally all of those open inference JS instrumentations that were donated, similar to the tracking issue that was done in Python, it looks like.
And so… let's see… So, some notes for anyone who is… porting these over, and then this, I guess, is what we talked about last time. Like, if there's already a package in the repo, don't report from scratch, look at the difference between the two.
And just update the existing package to match. This, I believe, is what we decided on. I don't know if it was last week? I don't know what time it is anymore, But that was kind of the thing. Like, the merge.
Two packages, if it already exists.
Trent Mick 00:11:39 Do we know if the… No, wait a second.
the Anthropic PR, so it's a concrete…
Surya Teja 00:11:49 Yeah, I was the one who… What is the anthropic PR?
Jamie Danielson 00:11:55 Yeah, I saw the comment in Slack, because we weren't sure if Anthropic was going to… Build it natively or not?
Surya Teja 00:12:04 Yeah, that's for Cloud Agent SDK. We are not sure there are some outstanding GitHub issues on Cloud Agent SDK, but for the JS… SDK, we don't have some instrumentation, so I ported this from Open Reference, primarily. This is a stub.
More work needs to be done.
Around this.
I can cut this down and follow the Python path, which is just first creating the skeleton and adding instrumentation around each method, if that is less robust and, Cognitively better for reviewers.
Jamie Danielson 00:12:48 Okay.
Trent Mick 00:12:50 I… yeah. We can… Decide that later when someone… is able to step up and take a review.
Jamie Danielson 00:12:57 Take a look at that, yeah. Thank you for working on this. I'm pretty sure this is one of the top ones, isn't it?
Yeah. Cause that was gonna be the other thing I guess I was just thinking about, is… if we were working on these things, it's probably worth paying attention to prioritizing, right? Like, this is obviously a good one, but I was just realizing.
Surya Teja 00:13:16 Like, you're.
Jamie Danielson 00:13:17 If you're looking to pick things up, this is probably a lower priority, for example, right, the one on the screen. Yes.
Surya Teja 00:13:22 Yeah, Prinav from Google is leading the effort. He is double-booked, so he couldn't join. He has a… He has an entry in the, notes.
So, we would be working similar to how, we have in Python. First, we'll be trying to create a GenAI utils with telemetHandler, which is going to create inference.
Agent and tool spans.
I guess you're quite aware of it.
And, then, we're just going to put the existing ones with OpenAI and Langchain to use that one, and the new ones to use that one, and just add the instrumentation. That's the plan, the natively.
Jamie Danielson 00:14:03 Okay.
So I think right now… so this is sort of, like, in progress, I'm thinking, like, right now I want to start with, like, updating this, maybe, to add you as a signee and the link to that PR, so that no one else picks it up.
I should have access to edit this, I assume.
Oh, jeez.
Surya Teja 00:14:24 I am working on OpenAI agents also, so that PR is also incoming.
Jamie Danielson 00:14:32 Okay, I gotta find an easier way to update that table, other than in the UI.
Trent Mick 00:14:39 I can do it while you're driving.
Jamie Danielson 00:14:39 Yeah, if that's cool, I'll just put a note down here… Okay…
Surya Teja 00:14:55 Since we are on the subject, I have another question, and I can wait until you complete all these things.
Jamie Danielson 00:15:02 I guess one of the questions that I have is… I haven't looked at the PR at all yet, but also, so we have, like, the PR checklist for ported libraries. Do we want to… I don't know if we do it all at once, I don't remember what all the things we are.
doing, but I guess if we're doing some of these things, I wonder if it's useful to put this… into the PR description.
Yeah. As kind of a… a guide of the things that have been updated.
Surya Teja 00:15:29 Yeah, sure, sure.
Jamie Danielson 00:15:30 Cool.
Sorry, what was the question?
Surya Teja 00:15:35 I see an outstanding issue where, JS folks are trying to create, the semantic conventions for GenAI. I guess your colleague I'm going to butcher his name, so I'm not going to hit him.
Jamie Danielson 00:15:52 Wolfgang. No, that's okay, I was working with Wolfgang on this a little while ago, yeah.
Surya Teja 00:15:56 Yeah, so he said that he's going to create some JavaScript Thing for those semantic conventions.
So, is he able to create something that we can pull in into our NPM, thing and, import those, semantic conventions as constants and work around the Gen AI Tils thing.
Jamie Danielson 00:16:18 Yeah, I think we'll want to follow up on that to see if that's still on the table, or if we want to, it's probably in regulars, isn't it?
Or if we want to open that up as, like, if someone has, bandwidth to work on it, I don't know if that's the question that you're asking, if you.
Surya Teja 00:16:37 Yeah.
Jamie Danielson 00:16:37 With to work on it.
Surya Teja 00:16:38 No, I… I don't know how to do that, so… and I'm not… I'm completely new to JavaScript ecosystem, so I might do a poor job of porting it.
Jamie Danielson 00:16:48 Okay.
Cool. So, I'll follow up. I know I just chatted with him a little bit this morning about it, that he has this on his list still, too, and Trent probably will look to you to help out a little bit, too.
Surya Teja 00:17:01 Yeah.
Jamie Danielson 00:17:02 So…
Trent Mick 00:17:03 Yeah, I can… I can help with that. Is that still the plan that we do? If the plan's roughly the same, like, no.
Jamie Danielson 00:17:08 Yeah, as far as I'm aware, the plan hasn't changed in terms of having the separate package for GenAI, so we can allow for independent versioning.
Did the new release go out yet? I haven't had a chance even to get to…
Trent Mick 00:17:22 Of Sunco?
Jamie Danielson 00:17:23 and AIC, yeah.
Surya Teja 00:17:26 I'm not sure.
Jamie Danielson 00:17:29 Doo-do-do… slash recommendations… Okay, so it hasn't been published yet, so we can't actually, like… have the new version.
Trent Mick 00:17:42 Yeah, we could… we could.
Jamie Danielson 00:17:43 Yeah, we can start prepping, like, the scripts and everything that we need to have to be able to do it.
Surya Teja 00:17:48 Yeah.
Jamie Danielson 00:17:50 Yeah, so that might be a follow-up, too, is just checking on what the latest is on here. I haven't been able to get to this in a bit, but I know that's the plan, is to do a release. I think the idea was to see what cleanup can be done before putting the release out to avoid Breaking changes that are avoidable early on.
Surya Teja 00:18:10 Yeah, so I have a basic doubt, sorry for this dumb doubt, but in Java, when I was working, we… I had Who created the classes around all the attributes.
produce around the attributes, because the alpha that we have in Java is not in a state where that can reflect the new attributes that we're working. Are we going to use the similar kind of stuff in JavaScript also? Like, how does it work with JavaScript?
Jamie Danielson 00:18:35 So, what we've done with JavaScript is that we'll have, like, if a semantic invention is not yet stable, which these won't at least right now, are not stable, I don't think they're planning to stabilize before publishing the package. Then we have a, file that essentially hardcodes the semantic conventions that are still experimental to avoid the breaking changes. So, like, as an example, if we look at, I don't know, let's just say… Express, maybe? Although, this doesn't have money, does it?
Aww.
Trent Mick 00:19:10 Oh, let's not use that pattern.
Jamie Danielson 00:19:12 Let's not use that pattern. We're gonna ignore that for a second and look at something else.
Pure, okay.
So, like, in this particular case, for this package, we have a semconf.ts file, that's essentially, like.
copied in, or… I think, Trent, you might have a script that…
Trent Mick 00:19:34 There is a tool in the contribibrory postscript that can be used, so, Yeah, so this, this can be basically a generated file, that is a… Okay, so, sorry, two things. So, the… using the semantic conventions package that we have right now, not the Gen AI-specific one, there are two entry points for it. The top level.
Import that you have is for stable semantic conventions only, and then there's another one called slash incubating.
That's for, experimental.
Things, And so, yeah, so you can just scroll down on the usage there a little bit. Oh yeah, I guess here, where you were showing, too.
And so… there's this usage of OpenTelemetry semantic conventions, which is… you can find and use that for stable, but if you want to use unstable things, then those are exported under the incubating Entry point, but the recommendation which was borrowed from what Java's doing and others, I think, is that shipping code should not import from this incubating thing, that's just there to… to show And provide the constants. The recommendation is that each instrumentation has their own copy, and we're kind of biasing towards using source slash semconconf.ts or js if you're a pure JavaScript implementation. And there's a tool that… or a script that's not, like, exactly production-ready or anything, but it helps copy those things in, so it'll get cloned to relevant semantic conventions. Oh, well, okay, so that tool will need to be updated for the GenAI thing, because right now it's just assuming there's one SunCom repo.
Jamie Danielson 00:21:19 there is.
Right?
If we were to do it today, we probably would pull… semantic conventions from the regular Gen AI repo anyway, right? They just show deprecated.
Trent Mick 00:21:32 But at some point, it may be already those things are going to be out of date, right? Because the… well, okay. Yeah, so there might be new… unstable… GenAI-related SEMConf in the new repo.
Jamie Danielson 00:21:46 Don't exist in the old world.
Trent Mick 00:21:47 rent.
Jamie Danielson 00:21:48 Yes.
Trent Mick 00:21:48 So if people want to use those ones, then this tool has to be smart enough to copy from. But anyway… Tooling aside.
For unstable ones, the recommendations and instrumentation has a local copy of those things. And that's to guard against things just being broken when there's a new version of that SEMCOM thing, because if it's unstable, it's allowed to be broken in a… in a… dot release.
Surya Teja 00:22:14 Okay, so… And it's traditional…
Trent Mick 00:22:15 Shouldn't be broken.
Yeah, sorry.
Surya Teja 00:22:17 Sorry, sorry, Trent, sorry for Trent. So it's similar to, like, Java. Like, have your own copy of the POJOS, and locally in the repo that you are instrumenting, and once the stable version is available, use the stable version package, and remove the SIM comps that you add.
Jamie Danielson 00:22:35 Correct.
Surya Teja 00:22:37 Cool. I am going to, raise a PR.
not me, but Trent or someone can raise up here when they're writing the GenAI utils library.
And I'll advise him that this is the pattern that you're following, and you guys can pitch in in the PR if we are deviating from the expected pattern.
Jamie Danielson 00:22:59 That sounds good. Yeah, and here we can see, like, an example of that in place, right? Where import the stable attributes from the package itself, and then import the unstable or experimental packages from the local copy.
QuickBold.
Surya Teja 00:23:16 Thank you. Thanks a lot. This is really helpful.
Jamie Danielson 00:23:21 Okay… Okay, I have too many things open now, I forgot how to get back. Okay, cool. So… Anyone else have comments or questions on this before we move to the next one that we didn't cover?
If not… Okay, next up.
Abhinav Mathur 00:23:53 Yeah, hi. So, this one I want you to take up.
And I messaged a plan in the comment, but I haven't been assigned this, so I just wanted to bring this up and see that. So I know it's not a… It's not… tagged as something up for grabs, but, or it was, I guess.
Jamie Danielson 00:24:12 Oh, I guess the original… there's an original one?
That's up for grabs.
Abhinav Mathur 00:24:18 Oh, God.
Jamie Danielson 00:24:24 Huh.
So that was for… Oh, there might be one, actually.
Has this been reviewed?
David Luna Bistuer 00:24:36 Yes, it was reviewed.
No, no, no, not the answer for that, from… On the other.
Jamie Danielson 00:24:45 Okay.
So… Convinced that having instrumentation is too restrictive.
David Luna Bistuer 00:24:55 Well, it was… this PR was quite an ambitious, so we wanted to deprecate the core instrumentation is instrument in NASJIS core.
Only the… so the subpackage, and now this one wants to create an image validation from SCS.
So we can implement microservices and all this kind of stuff, instead of… so make it… make it… making it wider.
So yeah, he was trying to duplicate one instrumentation and creating a new one.
Which allows to instrument microservices and all this kind of stuff.
So, a lot of changes, I proposed a plan for doing that, that big change.
But never got an answer for that.
Jamie Danielson 00:25:39 Okay, so then it sounds like if there's interest in… Working on this.
So… Start with a focus PR…
Abhinav Mathur 00:25:56 It'll be multiple pairs, basically, just kind of take one small slice at a time.
Jamie Danielson 00:26:01 Okay, so I think Trent just assigned. Now, I guess maybe I'll just put a note in here of… to maybe take a look at David's comments here to see if that helps, if they're still relevant for it.
Okay. Cool.
Abhinav Mathur 00:26:34 Thank you.
Jamie Danielson 00:26:36 Thank you.
That should now be linked in here somewhere. Yep, cool.
I wonder… If this should also be assigned, then… I might need you to… Oh, here we go.
So I'm just putting… Your name on this one, too, just because they're kind of… similar ideas.
And then that way.
We don't accidentally duplicate.
Abhinav Mathur 00:27:25 Yeah, take inspiration from the… From this PR, and go from there, actually.
Jamie Danielson 00:27:32 Yeah, perfects.
Oh, that's already there. Whatever. That's fine. Okay, thank you.
Okay, so we have one for… please take a look, is Matt… Here… yes. Yes.
Matt Wear 00:28:06 Oh, yes.
Oh my god.
Trent Mick 00:28:08 So my update on this, Matt, is, in the spirit of guilt-driven development, David and I are gonna chat about this tomorrow, and David's gonna make me feel guilty enough to spend… actually spend some time on this.
Matt Wear 00:28:23 Awesome. I still have that.
Trent Mick 00:28:24 to it.
Matt Wear 00:28:25 I just wanted to make sure it didn't totally drop off the radar, so that…
Trent Mick 00:28:30 No, it's to… it's… yeah, this is… Well, perennially next on… the declarative config stuff that I want to look at.
Matt Wear 00:28:38 Awesome.
Thanks.
Jamie Danielson 00:28:41 Trent, you want me to put you as an assignee? Does that help? Or no?
Trent Mick 00:28:47 I… I… sure, if it helps someone, but yeah.
Yeah, I mean, I plan to look at it, so that's fair.
Jamie Danielson 00:28:54 Okay.
Cool.
Alright.
So now we have the big, the big topic.
Do we want to see… does anyone have any tiny topics that we want to throw in before this one?
Speak now.
Forever hold your peace. Okay, Trent, you're up.
Trent Mick 00:29:18 Okay, this is me and Jackson. So, an hour apart, both of us submitted a PR to work on resource-related stuff. Not exactly stomping on each other, but in the same area.
Yeah, I guess mostly this is gonna be information sharing. I don't expect everyone else to… collect all the information in state for this, other than maybe Jackson and I, maybe Marylia, she's been watching.
So resource creation, and with resource detectors, and with declarative config changes, and with in-development changes in the spec make things interesting here, so… Still, I guess, I don't know, as background for people. So, since… okay.
So, a resource starts from a base set of things. The spec says, thou shalt have some… default attributes, mostly that's telemetry.sdk.star.
And thou shalt always have a service.name defined. So there's this default base resource includes an unknown… some string value, so unknown, service, colon, the name of the process, is meant to be the default.
Two other things the spec says is that, the environment variable OTel… this is for rules for SDKs… the hotel resource attributes… environment variable should be read, and then there's also another one called, hotel service name, which is… I guess it was added at some point as a convenience for setting the service name, because that's, you know, the most important, or one of the most important resource attributes to set.
So, we hadn't yet gotten to this section that you're seeing now, where there's a list of names there, Container, host, Process Service. Those things hadn't been defined yet. So then, Hotel Java and others moved on, and they created their own resource detectors, and they had ways to configure in their SDKs which resource detectors you wanted to use, and they defined their kind of own set of what the default resource detectors are.
And this was all in development, and people did. So, for Node, we have the environment variable, hotel node resource detectors, which is a list of convenient short names. Java has somewhat of an equivalent of system property and environment variable. It's a different name. But they use the… the arguments to this environment variable are fully qualified paths to Java classes for things, so there are these… these long names that really aren't that convenient, but I guess, fine, people can put them in a system properties file and move on.
The issue… one issue that comes up now is that the names, convenience names that we were using in this environment variable now are clashing slightly with names that are added to the spec, which came, I think, as part of the declarative config work, for… The spec basically, saying these are reserved names for a particular meaning.
And so the question is, how do we adapt to that, and where should changes be? Should it be in our resources package, and or should it be in our various SDK packages for creating… mostly SDK node for creating a resource?
In particular, the order of, Priority for how to set service.name from the 4 or 5, depending on how you count, different ways to create to set the service name is… gets interesting. The spec actually created a little bit of a twister in there, in that you can't… trivially… create dumb resource detectors that are not aware of each other. So, anyway.
I'm not exactly sure where to go from here, other than, like.
people can get involved in the discussion. This… this link on… Jackson's issue is probably… that's where I did my longest brain dump on this stuff, so… And I'm curious what you think, Jackson or others.
Assuming you've had a chance to read up.
Jamie Danielson 00:33:43 Oh, you're muted even though you're not Zoom muted.
Trent Mick 00:33:47 Can't hear you.
Jamie Danielson 00:33:48 Your mic isn't coming through anyway.
Jackson Weber 00:33:58 Sorry about that, it looks like, Zoom decided not to pick up my, microphone. I hope y'all can hear me now.
Jamie Danielson 00:34:04 You're good.
Jackson Weber 00:34:05 Cool, cool, cool. Yeah, the pain of having a dedicated microphone that every software detects differently on Windows. In any case, yeah, I left some comments below. I kind of have the same thing, Trent, where you were trying to get started. This whole issue just, like, exists in my brain, and I remember it sometimes, and then I context switch, and I completely lose all my contacts, so I tried to, like, dump my thoughts here.
For everybody. But as I understand it right now, I pretty much have A light version of option 2 from what you discussed?
Which we align on the spec, unify the detector names, and then accept the braking change, and package this in for, Hotel V3.
I, I think that was your, your, your point for, your second, option there. But…
Trent Mick 00:35:00 Okay, I, would have to take a look at the particulars.
For sure.
I guess the major concern that I have is that the resources package is stable.
And we're looking at taking a braking change on it to align to… unstable… section of the… like, these namings in the spec aren't stable yet, so, like, we could… They could change the meaning, and we could have to break them again, so… there's a part of me that's… Wondering if… maybe we don't want to align with those names, it's just a small paragraph in the spec. The… I think where it comes… Most… becomes most visible to users, or would do once we… kind of announced that we have declarative config work is that the names in a declarative config file would be different than the names that you would use in the OTL node resource detectors environment variable. So, like, another potential option would be to not change a resources package, but change the names in OTel node resources Detect or take a breaking change there, in that environment variable.
To align with what the declarative config names are. What it would mean then is under the hood, if you're doing it with code, then… You're not using Just straight up using the resource.
detectors… That are offered by the resources package. Yeah.
That was a long way of saying, I guess there's an option 3 there, too. So yeah, a major concern there is, like, do we want to… be changing a stable package to be trying to follow along with an unstable part of the spec. I'm a little bit hesitant there.
Jamie Danielson 00:36:52 I… I haven't read through all of this, so I could have just missed something in what you were just talking about, too, but… is… is part of the question, like.
Handling environment variables in addition to declarative config?
like…
Trent Mick 00:37:11 No, I think that's mostly straightforward, I think.
Jamie Danielson 00:37:14 Right, where we ignore the entire declarative config is…
Trent Mick 00:37:17 Yeah, well, I mean, modulo, we haven't finished doing that work, but…
Jamie Danielson 00:37:21 Asterisk.
Trent Mick 00:37:22 the spec for declarative Config is clear on that, and, like, once we're doing declarative Config file, the only MFIRs we use are the ones that are sitting in that… that are referenced in the config file, so…
Jamie Danielson 00:37:33 Right, that early.
classified.
Trent Mick 00:37:37 Right.
Yeah, it just gets a little bit gross, because the semantics are slightly different for SDK creation, and the specs are a little bit torturous.
In hotel right now.
I'm not sure how much this discounts for, but the current OTEL Java implementation for declarative config is they're handling… they have not changed the resources package.
to match these new namings, but instead, when you say… take the easy one, when you say the host detector, which is, like, the middle of your screen here, in a declarative config file, they merge the results from the OS and host detectors that they have in their resources package.
Instead of having gone to the resources package and changed the definition of what host means. But again, they don't have this name conflict with the… the hotel node resource detectors environment variable that we have, so… There's that.
I… I guess a fair thing to do, and maybe I should bring this to the configuration repo, is open an issue there and ask, Ask them, mostly Jack.
what their experience is with this, because I think Jack's… I mean, he's most heavily involved in the hotel Java side, Clarative config, and maybe for the resources stuff as well. Curious if… Yeah.
Jamie Danielson 00:39:15 Yeah.
That's probably a good next step.
Jackson Weber 00:39:24 Yeah, I mean, I can also update this, to avoid the braking change for now, and then if we want to accept the braking change that the spec implies, then we can take that later.
just as a halfway decision, but up to you guys. I don't know how, if there's any urgency, or folks want to get this through faster than, rather than later.
Trent Mick 00:39:48 What's an option that avoids a braking change?
Jackson Weber 00:39:51 I believe it was your option 1.
Okay. Keeping the…
Trent Mick 00:39:55 So I have…
Jackson Weber 00:39:56 Sector names separate.
Trent Mick 00:40:00 Right.
Okay, so my PR does that, I think.
I think I might be missing part of the equation here.
My PR's doing other stuff as well, so that's debatable separately.
Jamie Danielson 00:40:26 Okay.
So… Right now, is it, like… folks think about it. Are you, and see whether to use… Trent's PR to avoid the breaking change.
Trent Mick 00:40:50 If we do mine, it doesn't rule out Later coming back.
you know, whether that's SDK 3.0 or even later, if we're worried about the specs stabilizing, we can still come back and do what, Jackson's PR is doing.
On top of the changes that I'm doing.
So yeah, I guess… And the only reason I have a block on here is not because I think this stuff's awful, just because it's a breaking change in the resources package, so it would have to go into the milestone, at least.
So yeah, I think if there was another maintainer or approver that wanted to get involved and offer opinions, that would be great, though it does require you spending some time reading.
Background.
Sorry, I said Jack's PR there. That's because there's so many Jacks involved.
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:41:47 Yeah, as soon as we.
Jackson Weber 00:41:48 Oh, like.
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:41:48 first comment like Jack, I was like, wait, that's not Jack?
Jamie Danielson 00:41:52 I won't be having two syllables and names anymore, sorry.
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:41:55 I was like, is Jack opening Meetings on the JavaScript? I was like, no, I was talking with him this morning, he was not talking about…
Jamie Danielson 00:42:02 Trent calls me Jay at this point, too, it's fine. Just kidding.
Trent Mick 00:42:07 There's a separate Jack who works on… Java agents at Elastic that I work with, who's also working on declarative config stuff.
So…
Jackson Weber 00:42:16 Well, then it's actually really lucky I have a different name. It'd be pretty bad if we all had the same one.
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:42:22 Is that a requirement to work on this area, your name has to start?
Jamie Danielson 00:42:25 Weird.
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:42:27 Subject.
Jamie Danielson 00:42:28 Nope.
So, does that sound… Accurate, then? Oopsie.
So, like, Jackson's PR is a breaking change on resources, so we may want that for SDK 3.0. Trent's PR is non-breaking, it may happen first, with Jackson's as the follow-up later in 3.0.
generally needs… review and… Opinions?
Overall. Yep.
Trent Mick 00:43:07 I think we do need opinions on the… Yeah, whether we want to take a break and change some resources right now.
Or even in 3.0.
So, Jackson, separate question. If we, like, didn't take your PR, is this breaking something you need?
Jackson Weber 00:43:24 No, no, I was honestly…
Trent Mick 00:43:26 Working to…
Jackson Weber 00:43:26 contribute to, declarative config. So I was just going through the, A board you guys created. Picking up the first thing at the top.
So also, if you, as a similar, point, if you have anything where you're like, another declarative config PR that we really don't want to write ourselves.
Let me know.
Trent Mick 00:43:48 Okay, for sure, will do.
Jackson Weber 00:43:50 Yeah.
Jamie Danielson 00:43:52 Do we have that board?
Jackson Weber 00:43:56 That's actually a good question. I have a link to it if you want it in the chat.
Jamie Danielson 00:43:59 Excuse me, sorry.
Jackson Weber 00:44:07 He beat me to it.
Jamie Danielson 00:44:09 Okay…
Trent Mick 00:44:11 I have a whole bunch of state that isn't necessarily well reflected in the issues.
Jamie Danielson 00:44:20 Let me say that again?
Trent Mick 00:44:22 I just have a whole bunch of… Stayed in my head on that declarative config stuff.
Stuff that I'm trying to work through that isn't… I don't know.
isn't necessarily… Matched well to a lot of the issues.
Jamie Danielson 00:44:37 So if we go on each of the issues and say, Trent is thinking about this, maybe…
Trent Mick 00:44:41 Yeah, well… Yeah.
Jackson Weber 00:44:43 Just assign them all the.
Trent Mick 00:44:44 There are a whole bunch of… so, like, once… once the… so, Marylia, you know, I've been working on this fail fast thing, so I've been… there's… in… mostly in SDK node, I'm doing a refactor of… most… most… a lot of the code for the start node SDK.
CodePath, this is a code path that supports a declarative config and will support the environment-based config, will be a replacement for Node SDK.
On some timeline.
To migrate that stuff to… do a pass through to catch edge issues and change the semantics to, instead of just warning, they fail fast, which is a recommendation in the config spec.
I'm most of the way through that, so, like, trace provider, meter provider, logger provider are done.
Propagator's done, and the resource was this kind of the last one in that Because that ended up… it should be the simplest one, or second simplest one, it ended up being the most hairy. So after that, Part of those works added a lot of to-do comments, for which most of them have open issues, so there are a bunch of issues that are referred to as, like, to-do, open paren.
4-digit number, close paren, in the SDK node package, and if you do want, kind of, hints I'm not sure I put them all in the…
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:46:12 Yeah, I was gonna ask that if they are…
Trent Mick 00:46:14 projects, so they're not on the board, yeah.
I did some of them as I was going through, but I'm not sure that they all got landed in there. So, yeah. There are a number of pieces there that could be worked on.
I think this should be fairly digestible chunks.
Yeah, so there's one example.
Jamie Danielson 00:46:34 So, this one… Support resource…
Trent Mick 00:46:42 Yes, that's true.
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:46:43 That should probably be moved to the… Pick up callers.
Jamie Danielson 00:46:46 That's what I was just thinking.
Trent Mick 00:46:49 Well, that one is backlogged because it should wait until my current resource refactor thing goes in, I think, right? Because it needs this PR to get in, and then you can start working on it.
Jamie Danielson 00:46:59 So that one needs this one, right? I might just put blocked on this… In the, like, just… Easy findings.
Yeah.
Okay, cause I'm gonna forget.
Okay… So yeah, that was the… that's the only to-do in this particular, PR.
Trent Mick 00:47:29 In that PRPI. If you grew up to do an SDK node package, you'll find a bunch.
Jamie Danielson 00:47:38 Oh, yeah, faster ways to do it, not like that.
Trent Mick 00:47:51 the headers list, already had someone who did a PR, but that was before I'd refactored meter provider and tracer provider, so that's, like, should be redone.
Hmm.
Jamie Danielson 00:48:04 Is it already merged in?
Trent Mick 00:48:07 Yeah, no. Oh, the trace provider, meter provider are, yeah, so I think you could… the header list one could be done now.
Jamie Danielson 00:48:14 Okay.
I don't… See it in here?
Trent Mick 00:48:20 Yeah, probably didn't add it to the…
Jamie Danielson 00:48:23 Okay.
Sweet.
Okay.
Project.
Right.
Did I do that wrong?
Am I losing it?
What is happening?
I did it, right? I put it on the thing?
Pick it up.
Jackson Weber 00:49:17 Pick off.
Jamie Danielson 00:49:18 Declarative.
Jackson Weber 00:49:19 a save somewhere?
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:49:24 I don't know, refresh the issue page that it maybe picks? I don't know.
Have you tried?
Jamie Danielson 00:49:30 And I couldn'.
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:49:31 computers…
Jamie Danielson 00:49:31 I know, does anyone know?
Jackson Weber 00:49:33 Computer.
Jamie Danielson 00:49:34 Computers are a mistake.
Okay, so that's definitely there.
If I click into here… We're just… It's probably just thinking. It's probably fine.
Trent Mick 00:49:49 I noticed that… Wow, status.github.com says it's fine right now, but it took a half an hour to find… GitHub Action runners for some of my PR things, so I think it's… Slow, is maybe…
Jamie Danielson 00:50:02 I was having a little bit of trouble today. Okay.
Well, that's a thing that can maybe get picked up then, I guess.
And a few others to… Okay, just curious.
That one's in here.
6957, So are we thinking that this then… I know, sorry, now maybe I'm on a tangent on declarative config, but I'm wondering if we want to move a few over, since we just got offers for… Working on it.
I haven't looked in a bit, so I'm hesitant to put anything in pickup that isn't necessarily ready to pick up, but support options for console metric exporter seems like… That should be ready to pick up.
Trent Mick 00:50:51 Yep.
Jamie Danielson 00:50:54 We'll do that.
For now, that's a good start.
Okay.
Cool.
Alright. So we're… Close to time… let me put this on… Oops. And JavaScript. Okay.
Any other comments on… declarative config, I guess, or any topics that we didn't cover?
Okay, let's see… Commonjs entry crashes Webpack production builds.
Open this with a small fix that keeps local bindings for the defaults.
Self-reference dependency has unused export name.
And this… Okay, so now we have followed the recommendations for two sets of testing.
the main… Change is just…
Jared Freeze 00:53:06 Yeah, I… I can chime in here. So the main change… so before this diff, you can… if you scroll up to main fields, it chooses main by default to force it to pull the package from that key.
Instead of relying on what actually happens. So, I… that's why… I mean… I don't totally agree with… this PR, but if you… wanted to test this, that's how you would do it, so that's what I suggested, is just to make a new… you know, NodePath, because each bundler's gonna pull a different key based on its own config.
So, I'm not sure this is totally on base, but that's why I wanted others to look at it. But that is the only change, that line you have highlighted.
Jamie Danielson 00:53:56 Yeah.
Trent Mick 00:54:01 I'm a little lost. If someone… No, I'm totally lost, actually.
that configuration to a Webpack config is necessary to Use main as the entry point instead of… what? Instead of… Browser.
Jared Freeze 00:54:22 I think it depends on if your own package is an ESM.
Or CJS mode. It puts… it… it makes Webpack request whatever matches your project.
Jamie Danielson 00:54:35 The actual error seems to come from Webpack.
Oh, this is closed.
Jared Freeze 00:54:50 This also, I just have to call out, this will not be an issue after 3.0 is released, and the PR I have open for, re-architecting the build system goes out.
So… messing around with main keys and imports and exports and things, I would probably just pause on, since that's coming up in, like, what, 2 weeks?
Yeah, this will likely… Not survive that conversion.
So, if this helps somebody today, that's cool, but those… those keys are all changing, so…
Jamie Danielson 00:55:28 Well, and I guess, is this… is this also saying, basically, that, like.
With this fix, if this is now in a release, then… it will be fixed for this version of Webpack anyway, also?
It's kind of how…
Jared Freeze 00:55:52 That, I'm not sure about.
Jamie Danielson 00:55:54 Yeah.
Trent Mick 00:56:06 I realize I'm 5 minutes behind in the discussion, but how can that change to SDK trace base source utility.ts make a difference?
Jared Freeze 00:56:24 That is… that… I actually question that too, but I kind of thought this would get close, so I didn't worry about it.
That's actually what gets exported.
After… compilation.
Doing it here, I'm not sure really matters.
So, that's why I… I was a little confused by that as well.
Jamie Danielson 00:56:55 Hmm.
Alright, so maybe just take a look at… this, because, yeah, I'm a little bit… Confused by this, also.
Jared Freeze 00:57:09 Yeah, it says, you know, it puts it on an exports key, but I think it already does that. That's… I think Webpack already does that, where… it doesn't get shoved into CommonJS, like, default, like.default.
But I think that's what the claim is, so… But yeah, like I… like I said, if you… if you're overriding, main fields, or fields, like, whatever the other one is, preferred fields, I think it's really a specific config problem.
Yeah.
Trent Mick 00:57:47 Are you willing to add a comment on that one, saying this goes away with 3.0, and…
Jared Freeze 00:57:51 Yeah, we can do that. I… I've hesitated to do that because I saw, like, the very first topic was user interaction.
User interaction goes away soon anyways. Like, we have open tickets to deprecate everything in core and contrib, and migrate to browser. User interaction's actually already replaced, and people are closing bugs against it. I think I've seen 3 or 4 things just in the last week, so I think the… AI tidal wave is coming for tiny bugs and things we're gonna delete. So…
Jamie Danielson 00:58:21 Whoa.
Jared Freeze 00:58:21 I was sort of like, you know, like, how much work do we want to do around stuff?
The one thing about user interaction is that it does… it is sitting in auto… instrumentation web.
So, I presume that will keep going. I think Honeycomb uses it, you can correct me if I'm wrong, but I think that was the request there.
I mean, what… You know, it would be preferred that those get replaced with the browser versions as well.
But it… but that's absolutely breaking, right? Like, I understand, like, auto starts with a zero, which means experimental, ours is also experimental, but it does not generate the same.
telemetry with the same keys in the same way. It is completely different. They're not one-to-one, but… That is a much larger conversation, but we do have tickets out that's literally just, like, deprecate this one for this one, and, you know, move people over to newer keys, newer code. You know, no CommonJS is one of the things that browser does, right? Because CommonJS is not valid on the web, so… Maybe, yeah, we can, Trent, maybe we can take that offline, or whatever, into the… into Slack, because that's much, much larger. Or even, like, a separate meeting, maybe? I don't know. 3.0 is going to be a big one, so…
Trent Mick 00:59:43 So there's a lot of work in 3.0. Thank God for the build system changes that you're making and get us over that… the ESM jump. I agree the tidal wave's coming. I'm not sure this was an indication of the tidal wave. I don't remember. I think this… the rush of ones on user interaction was because And I haven't looked at what the source was for this week map edition, so it changed internally to use a weak map for a thing, and then that caused two follow-on issues. So I think that was the three, so I don't know what the motivation for the first one was.
Jared Freeze 01:00:14 Yeah, I was concerned about that too, because it was… the conversation was about Node, but then the output is browser anyways, so… It was like, oh, this doesn't work in Node 18, and I'm like, there is no node. Not really. So, if the test is failing because weak map is not available, it actually doesn't affect us at all. And then there was a polyfill written for a browser I don't think we support.
So that one, I, like, need to leave more comments, but I'm not sure we should be doing that either.
Trent Mick 01:00:44 Okay. That was my comment on that one thing. That was about Weak Map supporting… Whether a given browser or runtime's weak map implementation supports The… the subset of symbols as keys?
Jared Freeze 01:01:00 Right, right.
Trent Mick 01:01:01 Like, everything else, if… on MDN, everything else about Weak Maps was… widely available. But I wasn't sure about that one, because there's a note in the widely available box at the top saying some features on Weak Maps are not widely available. So, and… and I can't read a CanIUs.com page enough, well enough to determine if that's a thing. But you're right, it did feel a bit weird. I caught myself towards the end, though I didn't say it, that… why am I talking about Node 18 compatibility on a browser instrumentation?
On the deprecating the browser instrumentations, I think that sounds great from my point of view, but we do, I think, have to have a… that might happen after 3.0, because I don't think it needs to be rushed right now, but I think we do have to have a bit of a migration process there, because I think there are probably a number of vendors and users that are using the old ones, and that's such a big change, to the new instrumentations using If I'm correct.
Jared Freeze 01:02:00 Yeah, I misspoke.
Trent Mick 01:02:01 Tracing everywhere, so, yeah.
Jared Freeze 01:02:03 Yeah, I misspoke. Those are not coupled. It just feels like it's all happening at the same time. So yes, forget I made that connection.
Jamie Danielson 01:02:14 Alright, we are at time. Thank you, everyone, for the discussion and the work.
I guess we'll see y'all next week.
Jackson Weber 01:02:24 Have a good one.
David Luna Bistuer 01:02:24 Bye.
