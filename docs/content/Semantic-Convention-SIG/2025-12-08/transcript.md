SIG: Semantic Convention SIG
Date: 2025-12-08
Duration: 61 minutes
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:01:53 Hi, everyone.
Dave Cadwallader (OSO) 00:01:57 Hello!
Liudmila Molkova 00:02:05 Let's give people a few minutes to join.
Donal O'Sullivan 00:02:11 low…
Trask Stalnaker 00:02:41 Good morning.
Josh Suereth 00:02:43 Morning.
Liudmila Molkova 00:02:45 Hello.
Josh Suereth 00:02:50 Ludmila, you have to leave after 30 minutes, Do you want someone else to run the meeting, then?
Liudmila Molkova 00:02:57 Yeah, please do.
Josh Suereth 00:02:59 Okay.
I could probably take a crack at that.
Trask Stalnaker 00:03:05 Thanks.
Josh Suereth 00:03:25 Alright, should we start with, triaging a little bit? And folks, please add your, your items.
Okay.
We'll do a little bit of pre-hard triage.
Oh, we have nothing that's blocked, huh?
That's cool.
Yeah.
Trask Stalnaker 00:04:00 I, we had increased the, well, we had started applying the PR stalebot to draft PRs also.
I don't know if that helped.
Josh Suereth 00:04:16 Yeah, I'm… I'm perfectly fine ignoring draft PRs, and throwing them into the draft phase, but yeah, interesting.
Okay.
Cool. So, under needs more approval, we don't have to go through these, in detail, but there's three, so please take a look. We have, the service criticality attribute, which comes with demo, consolidating RPC metadata attributes, and, updating the dependency on Prettier.
Liudmila Molkova 00:04:48 Josh, you are not sharing the tab.
Josh Suereth 00:04:51 Oh my gosh. Okay, sorry.
Liudmila Molkova 00:04:53 Oh.
Josh Suereth 00:04:53 I thought I clicked the button. Yeah, so we have 3 that have needs more approval, so please take a look at those three. I'm gonna skip awaiting Code Owner's approval, and I don't think we need to go… through untriage, because we'll get those later, I want to just focus to make sure blockers are being resolved and make it through.
Trask Stalnaker 00:05:13 Josh, Josh.
If you have a chance to look at the RPC one, we have… Two approvals, but we need one more, green checkmark.
Okay. And we're trying to push through, several of the RPC things right now.
Josh Suereth 00:05:33 I see. Yeah, I'll take a look then. That, yeah, cool.
Let's go to issue triage.
Alright.
And we'll… we have, like, 2 more minutes for this, so we have needs, info, and accepted.
And needs sake.
What have you… have you guys been doing anything in this meeting with these?
Liudmila Molkova 00:06:05 So we've tried to triage the issues that need triage, but there are 180 of them.
Josh Suereth 00:06:12 So just do, like, one or two of these?
Liudmila Molkova 00:06:15 Yeah.
Josh Suereth 00:06:16 Okay.
Linux MD RAID Metric Conventions.
Does this go to System Semcov, or is this its own thing?
Trask Stalnaker 00:06:37 I mean, we can send it to them, I don't know if they particularly want it.
With… within their current scope.
Josh Suereth 00:06:45 Yeah… Should we send it to them to add to their backlog? I mean, it does… Feel a little bit like… MD stance, MD rate, oh, this is kind of a Linux-only specific thing. This seems like more along the lines of how we want to decentralize and federate, right?
Trask Stalnaker 00:07:11 Bink… So, I mean, I… I don't see how we can own all system… Stuff.
I think there's gonna be a core…
Josh Suereth 00:07:29 There's gonna be a core and other things, yeah.
Trask Stalnaker 00:07:32 Yeah, and maybe the some… maybe the system, some config just… needs to make that decision. I don't know if that's clear for them.
Josh Suereth 00:07:43 Yeah, I'm gonna add this to their thing, and I'm gonna put a comment.
G… System SEMCA approvers.
This is… type of issue the system sync.
Working on… Or, if this is… 2… Federates.
Congratulations.
Simcoev. Okay.
I can't spell stabilize, apparently. There we go.
Alright, that's one, and we're out of our time box, so…
Trask Stalnaker 00:08:52 Cool.
One out of.
Josh Suereth 00:08:56 180.
Trask Stalnaker 00:08:57 Maybe, okay.
Josh Suereth 00:08:59 Cool.
Yeah, I think we're gonna have to do some of these offline, basically, to get through the rest of them, or if we have time at the end of the meeting, we can do some more.
Let's get into the agenda, since I think some of us only have the first 30 minutes.
Dave, since… I believe you're here…
Dave Cadwallader (OSO) 00:09:18 I'm here.
Josh Suereth 00:09:19 Cool. You wanna talk a bit about… I can… I can present, or you can present?
Dave Cadwallader (OSO) 00:09:24 Yeah, would you mind?
Present? I… yeah, I can talk to this.
Yeah, so just real briefly, thank you for having me. I work for Oracle, and some of you may know that we have a public cloud offering, like AWS and Azure and GCP, called Oracle Cloud Infrastructure.
Unfortunately, Nick, with the, with the acronym OCI, which is, already means something else in the, in the, open source, world. So, anyway, we've been, working with, David Ashbull, who's, who's agreed to sponsor some of our work on the OTEL, Collector. We've been working in the OTEL Collector Contrib.
project for the better part of the last year, working on a resource detection processor, basically so that anybody who's using Oracle Cloud as a cloud provider for, you know, running Kubernetes workloads and things like that can get automatically enriched metadata that has information about, you know, the nodes, the, you know, region, availability domain, things like that.
So right now, internally, and I imagine externally, people have to use things like running a sidecar in order to automatically enrich their… their data. So with, with the resource detection processor, they can kind of automatically get that. So as part of that, we've already been working in the semantic conventions repo. We kind of planted our flag last year and put in Oracle Cloud as a recognized a cloud provider, and we're now at the step where we would like to start adding additional Oracle-specific attributes for concepts that don't quite exist in all cloud providers universally, but anybody who's using Oracle Cloud, whether it's internal to Oracle or publicly, is going to need some of these additional attributes. One of them is a concept called Realm, which is, like.
Not quite a region, but, you know, a little bit higher level than a region.
So, David Ashpole, recommended that we start our own vendor prefix, and that way we can have, this can be a place where we can continue to add, things that… that… that don't quite fit in with, like, the broad set of semantic conventions, but would be useful to any public… community users of, of Oracle Cloud. So, I understand that you need to kind of vet, these, these kind of contributions and make sure this isn't going to be, like, a hit-and-run kind of thing, where we just, you know, drop something and then vanish.
So we do have, 3 folks from my team, who are ready, willing, and able to step up and own this.
And I will say also that I've been in touch with folks from other parts of Oracle as well, who, you know, we've kind of, as is often the case in big companies, we're kind of siloed, but folks that are excited to start to also collaborate and contribute, so I'm gonna be working on kind of trying to be the… the open source liaison, and getting folks who are using OpenTelemetry and other parts of Oracle to collaborate on this as well. So I'm hoping that 3 is just the start here. Oracle is also, you know, a sponsor of the CNCF, and I think that there's a lot of a lot that we can gain by improving our, contributions and our public visibility, not just as financial contributors, but as code contributors, so… Yeah, so that's where I'm at, and I would love to hear your thoughts.
Trask Stalnaker 00:13:11 I just wanted to jump in and say that, several of us are very familiar with, Oracle Cloud, because of the CNCF credit, the massive number of CNCF credits, and so that is our go… that is our go-to for project infrastructure for OpenTelemetry, so… Yeah, thank you.
Dave Cadwallader (OSO) 00:13:35 Glad to hear that.
Josh Suereth 00:13:37 I was gonna add that, really glad you guys want to stand up and, like, take ownership of that. One thing that I will say that we need to make sure we are continuing to do is when there is a concept that is defined in OpenTelemetry for which Oracle Cloud applies, we want to make sure that these general purpose semantic conventions are our general purpose, right? And we have… we have this notion of T-shaped APIs, where there's the Broadly applicable convention that people should be using, and then the deep conventions that are specific, like, oh, I'm an Oracle user, so I need XYZ. And we want both.
Right? And so, like, making sure we know where that boundary is, like.
Greenlighting this group doesn't change the fact that there's still a boundary, and we'll still have.
Dave Cadwallader (OSO) 00:14:22 Sure.
Josh Suereth 00:14:23 Yeah. So, the justification you gave for Realm, matches my understanding as well, so I appreciate that. We also, I'm with GCP. We have problems with Availability Zone as well, because we do it differently for reasons.
Where things can have two availability zones, where the manager's on one, and the other, you know, it… Yay. Glad we did that. It makes it so easy. Those kinds of things in OpenTelemetry, we'll have to have a discussion about that, because the goal is, you know, we always want to tie things down to how people are using it, how people see it, so it's not just like, am I modeling Oracle? It's like, what does observability look like?
with that caveat, I think this is great. I'd love to… to make this happen.
Trask and Ludmilla, do we have any other maintainers here?
No, just… there's 3 of us.
Right, because of the holiday.
I didn't realize that an Austrian holiday would take out, what, two… Third. Anyway, What do you guys think… what do you think next steps are for this? Do we want to turn this into a SIG? Do we just turn this into a set of maintainers in an area of the spec? What's the next step?
Liudmila Molkova 00:15:49 I guess it's the question for Dave. I would support creating a group, but if you folks would… like a SIG, it could be a SIG? Like, what SIG could give you if there are people outside of Oracle that are interested, and you need an official up on telemetry meeting time and notes and everything?
And this would be, this would come through the project proposal. For your current goals, it sounds like the group would be enough?
What do you think?
Dave Cadwallader (OSO) 00:16:22 Yeah, that sounds good to me. I think right now our immediate need is just to make it clear, yeah, how we can get contributions in, and kind of who's responsible, especially if there's bugs or issues found, just who's… who's gonna be responsible for picking those up. So I think the approvers group satisfies that goal. I think a SIG could be eventually interesting, especially, like I said, as we're representing multiple teams from different parts of Oracle. I think having a SIG, and that would help us, you know, with some of our own governance, and then it would be fantastic if we could identify some, some heavy users of Oracle Cloud in the community who might want to also chime in on this. So I would like to set that as an eventual goal, but I think it might be premature to spin that up now.
So I think just starting with the approvers group is great.
Trask Stalnaker 00:17:18 We'll probably, need for you all to come to this general meeting, from time to time to kind of talk through and help us understand certain things.
To get there.
Dave Cadwallader (OSO) 00:17:34 Yeah, that's…
Trask Stalnaker 00:17:35 landed.
Dave Cadwallader (OSO) 00:17:36 That's absolutely fine for me. I know that's easy for me to do, and I can certainly see if we can get some attendance from other folks in Oracle as well.
Josh Suereth 00:17:49 Yeah, I think the main thing we want there is to go through, like, the overall goals of the project and the values, and make sure that we're all aligned.
And then… because you're going to have a green checkmark on things, right? So it's not… your green checkmark will mean, does this abide by what is good for Oracle, but also, is this good for semantics conventions? So we want to make sure that second part is, like, fleshed out, and there's a feedback channel.
And then, if you have trouble with semantic conventions, or documentation is confusing, which has never happened, ever.
This is the place where you can come and be like, hey, we're trying to model this, and we can't find the right spot, you know, what should it look like? And we can talk through and fix it.
Dave Cadwallader (OSO) 00:18:32 Sounds great.
Josh Suereth 00:18:39 Alright, so… that sounds good. I think next steps are, let's make a Oracle Cloud area and a, an approver list. Does that sound good?
Dave Cadwallader (OSO) 00:18:51 That's great, yeah, so I think, I've got a, a PR that was linked here that got auto-closed by the bot, So…
Liudmila Molkova 00:19:02 Yeah, maybe… somebody needs to create this approver group, Trask or Josh, I think you have admin rights. Would you be able to do this?
Josh Suereth 00:19:12 There's, if you, if you open an issue against the OpenTelemetry community.
repository to say, I would like to have a… a group, that's… yeah.
We have so many GitHub repositories, so there's more than one. The approver groups are owned by the hotel org, and that's where we do those.
Liudmila Molkova 00:19:31 That'll just remind me to do it, sorry. Can we just transfer this one there, because it belongs there?
Josh Suereth 00:19:38 Oh yeah, actually, we could do that right now, can't we?
I can still transfer issues. Let me move this over to the… community. There we go. Is that alright, Trask? Or did… are the tags gonna be wrong?
Trask Stalnaker 00:19:52 No, it's fine, yeah.
Josh Suereth 00:19:54 Okay.
Alright, now I will remember it.
Trask Stalnaker 00:19:59 And Lyudmila, if you, if you submit the PR to the admin repo to add the team.
I can approve it.
Oh, you're muted.
Liudmila Molkova 00:20:13 Sorry, we manage them through the admin right now.
Trask Stalnaker 00:20:17 Yeah, so the team creation is done through, IAC, which, stores the Terraform state in Oracle Cloud.
And, so yeah, if you send the PR, I can approve it, but not vice versa in that repo.
Liudmila Molkova 00:20:36 Awesome, so I can't try, so let me take this over, Josh.
Dave Cadwallader (OSO) 00:20:46 Yeah, and as we're creating this group, one question I had is just around naming conventions of the group itself. I've noticed that other vendor prefixes in the semantic conventions, when it's a multiple word, that internal to the YAML, it uses an underscore to separate the words, but then the directory itself that contains all those files uses, like, I guess, a snake case with the hyphen.
So is that what we should follow? Like, oracle-cloud for the directory, and then internally, Oracle underscore cloud?
Liudmila Molkova 00:21:26 Yeah, I think so.
Josh Suereth 00:21:29 I want to get to the point where the directory doesn't matter, and the…
Dave Cadwallader (OSO) 00:21:34 Okay.
Josh Suereth 00:21:35 what's in the files is all that matters. So, as long as you use the underscore, that's actually in the naming conventions. The snake case thing is just… Yeah, maybe we keep it, maybe we don't. That's… that one's less important to me.
Dave Cadwallader (OSO) 00:21:49 Got it.
Trask Stalnaker 00:21:52 And you could send a PR to the semantic convention repo to add that area.
Dave Cadwallader (OSO) 00:22:02 Okay, I… I think… I thought that's what I already did, the one that got auto-closed, is… or is that not… Is that something different?
Liudmila Molkova 00:22:09 Oh, there is a file called areas.yaml.
Dave Cadwallader (OSO) 00:22:13 Oh, okay.
Liudmila Molkova 00:22:14 You… we would need to add the yoga group there.
And once I have, okay, I'll send the PR to, create the group.
I'll pass it on Semantic Conventions chat, and then you will know the name of the group I'm going to add, and if you don't mind.
Trask Stalnaker 00:22:38 I put it in chat.
Liudmila Molkova 00:22:40 Oh, right. So there is this… file an UVODETA .
Dave Cadwallader (OSO) 00:22:47 the group.
Liudmila Molkova 00:22:49 Like this one, yeah, and you would list the area OECI underscore cloud here.
Dave Cadwallader (OSO) 00:22:55 Got it.
Liudmila Molkova 00:22:57 And there is no project file, there is no board. If you need a board, please… Let us know, we will create the boards for you.
Dave Cadwallader (OSO) 00:23:08 Sounds great.
Trask Stalnaker 00:23:09 And after, we should… get… I think, actually, I think we'll have to get… The approvers into the org.
Are any of them already org members for OpenTelemetry?
Dave Cadwallader (OSO) 00:23:27 No, I've got some work to do there, so I will, yeah, make sure everybody's, well, actually, yeah, I think they first even have to sign the CLI, and I think I'm actually not even myself an OTEL org member.
Josh Suereth 00:23:43 With the work you did on the resource detector, that… Yeah, well, we need to make sure that your org members first, but I… with that work, you should be able to become an org member relatively quickly. Okay.
Dave Cadwallader (OSO) 00:23:55 Perfect.
Trask Stalnaker 00:23:57 Yeah, I'll give you the link here.
And yeah, you're welcome to use, you'll need two sponsors, you're welcome to use myself, Josh, Lydmilla.
Any two of us.
Dave Cadwallader (OSO) 00:24:14 Wonderful, I appreciate that.
Hmm.
Josh Suereth 00:24:29 Cool. Any, any other questions there?
Alright, with that, should we move on to talk about V2 schema?
Trask Stalnaker 00:24:47 Yeah.
Liudmila Molkova 00:24:48 Yeah, let's do this.
I have just 5 minutes, so I'm going to start showing you the… what… what I've done, and then I'll drop off, and you will keep talking.
Josh Suereth 00:25:01 Thank you.
Liudmila Molkova 00:25:02 Okay, let me share my screen.
I'm sorry.
Oops.
Okay.
Here we go.
Do you see VS Code?
Trask Stalnaker 00:25:29 Yes.
Liudmila Molkova 00:25:30 Wonderful.
Okay, so… Yeah, let me zoom in… R.
So, thanks a lot.
to Josh, who… did, like, 90% FLO work on V2.
So this is… What I'm going to show you is how the changes that happen to some conf inevitably with current state of V2.
And we'll look into the attribute groups, sorry, the attributes for now.
So one… the first thing I want to, show, there is, no… I mean, the structure is pretty much the same.
What's gone is, let's say, the attribute briefs and notes, because there are no groups anymore, right? And there is… there is just a list of attributes in V2.
In most cases, it doesn't matter. This description does not help much. In some cases, it matters.
So if we take a look… Let's say server… This group description could be meaningful.
It probably belongs somewhere else, maybe we should have a public group for the server, and maybe this description should go there.
Or maybe we should figure out some other means to talk about, server in general.
Duh.
Other things I want to highlight is… Sorry, the few minor things that are gone. The display name.
So we can cover it up with, Weaver config. We can say, okay, the speed.net core name is this.
I think we can find, a more interesting solution for this over the time, but I don't think it's a critical problem we have to solve.
The other thing, the last thing I want to highlight that could be a little bit controversial is… We used to have namespaces, which were the group boundaries.
We effectively cannot have them anymore because there are no groups.
And now, all, let's say, AWS attributes are one table of AWS attributes.
Again, we could solve it in one way or another. We can, break down by either two levels, N levels, soft namespacing. We can, introduce, some form of attribute groups, again, which we need for public use cases anyway.
But this is the current state of things. I don't believe any of these problems should block us from having V2, but I want to make sure we are all aware that there are this list of Inconveniences that over the time we will probably need to solve in some way.
Trask Stalnaker 00:28:52 I don't see a problem with the… this one, because the registry isn't what we want people to focus on anyways.
So it's just a registry, it doesn't need… I don't feel like it's important for it to be sort of human browsable.
Josh Suereth 00:29:16 We… I do want to get to the point where we have a registry for metrics and things, where that'll be more interesting.
Yeah, I actually forgot that our registry had so much, like, chunking in it.
Liudmila Molkova 00:29:35 Sometimes it's meaningful, sometimes it's not. If I look into the, let's say, user agent.
sorry, I'm lost again.
We had single attribute separately, for reasons I… don't get… So, yeah.
There is both good and bad in this.
Okay, with this, I need to go.
Thank you all, and see you next time.
Josh Suereth 00:30:10 Cool.
Trask Stalnaker 00:30:11 Thanks.
Josh Suereth 00:30:12 Thank you.
Whoa, oh, are we… are we done? Done?
Trask Stalnaker 00:30:16 Oh, I don't know.
Josh Suereth 00:30:17 Oh, we're just saying goodbye.
Trask Stalnaker 00:30:18 Saying bye, Tilda Miller.
Josh Suereth 00:30:20 I'm gonna, I'm gonna show a little bit about what V2 schema is, what it's about, for folks, so you, you understand.
Ludmila was just talking about some of the challenges with it, but just so everyone knows what we're… what we've done, there, the next release of Weaver, which should be this week, although I have to fix some… some bugs, is going to be using V2 schema. V2's schema… What?
Trask Stalnaker 00:30:48 Wow.
Josh Suereth 00:30:49 Yeah, if you want to use V2 schema, there's a dash dash V2 flag that you'll be able to use. It's gonna be in a preview-based feature, but we got all of Weaver working against it, except for one… problematic bit, which I'll talk about. Anyway, this is what the language looks like now. So the syntax of the file, instead of groups, where you have to have types and all sorts of craziness with that, you actually specify, here's my attributes, here's my entities, here's my events, here's my metrics, here's my spans, at the top level. When you define your attributes, you just define them straight up as a registry.
Which is why we're losing that grouping capability she was showing you, right? Because you're actually going to define your attributes just in a file, straight up.
The other thing we're doing is we're making sure that the names on these match the data model of the OpenTelemetry type and or what you see in OTLP. We want to make it be as consistent as possible. So, an attribute is a key-value pair in OpenTelemetry, so we use key instead of name or we were ID or inconsistent. I forget what attribute was in V1. I think it was name. But now it's key.
which matches what key-value pair is in OTLP to make it parent.
enums and all that stuff is… a lot of stuff is gonna be the same, the way we do enums, the way we do attributes, that hasn't changed.
Attribute groups are a little bit different now. There is both an internal and an externally visible attribute group. If you want to publish an attribute group and say, here's an attribute group people can engage with, you mark it as a publicly visible thing.
An attribute group has an ID and a set of attributes. You can then reference it later, I'll show you what that looks like now.
But we were using a lot of attribute groups to kind of, like, bundle things, but they weren't really important to end users, to docs, to validation. So what Weaver v2 schema does is if it's an internal attribute group, it's used in your file to define things, and it is not exposed publicly to users, it does not complicate their model, all of that gets flattened.
Okay. Then we have the way you define a span. There's a new thing we have in span called a type.
So, the problem we have with spans today is… er, is that the name… is, like, a description for how to generate a name, but we actually can't tie a span to a thing to do validation in Weaver to understand, like, an identity of it. And we… We were previously calling… spans by reference with the group ID, We have officially decided inside of semantic conventions to have a thing called type that we will use to identify as span, and then we'll have a way in OTLP going forward at some point for how you can take any span and figure out what type it is to do validation against semantic conventions. That second part is still a bit TBD, but we're working through that.
anyway, so spend looks pretty similar. Name is no longer a… just a raw string.
If you want a raw string name, you put a note for what that raw string will be. We eventually plan to have name be somewhat, programmatic, so that we can actually synthesize how to produce it, and synthesize how to get back to a span type from the name. That is TBD in the future, but, for now.
This is kind of what span names look like.
There's a description about that and what that future could look like here.
Alright.
Entities, we changed a bit as well. So, with entities, instead of having a raw set of attributes, and you have to provide roles on attributes, you instead define the identity of the entity that is a set of refs, and you define a description, which is also a set of refs. Refs refer to attributes from that attribute array you saw earlier.
Okay.
Metrics, again, same treatment. Instead of metric underscore name, it's just name.
Everything else is pretty similar. Oh, when you define a ref, you can also change things, like the requirement level. Some of these will be required, so when you define a metric.
attribute, you have to define a requirement level. When you define the attribute itself, you don't define a requirement level, because you don't know it, it's not tied to a signal.
I'm starting to rant a little bit, but this is basically… the TLDR is… this is overall trying to clean up how you write things so that the YAML is very readable going forward.
And if you feel like the YAML is not readable, let us know, because we're trying to fix that. The other thing that's…
Trask Stalnaker 00:35:53 What happened with, the part of the YAML that has never been readable for me has been the inheritance.
Stuff.
Josh Suereth 00:36:02 Yeah.
Trask Stalnaker 00:36:04 How is that working in V2?
Josh Suereth 00:36:08 This is… this is some of the inheritance stuff, so you can ref something here, right?
Trask Stalnaker 00:36:13 It's the extends. The ref stuff hasn't… has been clear to me, it's the extends stuff that… Where we've ended up with, like.
These multiple hierarchies in, especially database semantic conventions.
Josh Suereth 00:36:33 Yeah, we kept, let me see if I have that deprecated structure… I don't think that's documented yet. I can show you what it looks like, though.
So… You know, how comfortable are you with Rust?
Trask Stalnaker 00:36:57 So true.
Josh Suereth 00:36:59 Okay. It's a structure definition, so hopefully it's not too in the rust weeds.
But if we look at V2, Let's take a span, right?
There are two types of spans you can define. You can define a raw span.
And then you can also define what we call a span refinement.
Where's that one?
I don't think this has extends.
Yeah, that's a span group ref, span attribute ref. Okay, so the way extend… the only thing that we're exposing right now, because we're not expanding… we're not exposing refinements in the new model, in this way. You can refer to a previous spin, or to a group. So, like.
With extends before, it would grab all the attributes that you had previously.
With this one, what you do is you would write ref group.
in the list of attributes, and it would refer to the span. So let me see if I… I'm gonna come over to the notes.
Okay.
So… Can you… can you see what I'm typing? Yeah.
Does extends… So, in the New World, you have… Man, notes is gonna be rough for this, but we got it. So we have spans… You would have a span with a type, you know, my.span, And then, under Attributes, I can… Refer to an attribute, and this would be some specific attribute.
Or, I can refer to an entire group of attributes, so I do ref group, you know, some shared Group.
And remember, the notion that you would have attribute groups also exists, so I would have spans, I would have attributes, and somewhere in attributes, I should have a key of sum.specific attribute, and I would also have an attribute groups.
And here, I would have an ID of some shared group, and this would have its list of attributes that it is sharing, which would have, you know, refs.
Does that make sense?
Trask Stalnaker 00:39:32 Yeah, yeah.
Josh Suereth 00:39:33 So, there's no… In the definition, there's no explicit inheritance of spans. We do have inheritance of spans in the model that we'll be able to support.
I don't want to add that craziness outside of what you had to do for database, and we can talk about why, and what that looks like later.
Lyudmila, I don't want to run into all that, but anyway, go ahead. I'm not…
Trask Stalnaker 00:40:00 I'm not sure we had to… I mean, I think… I'll probably take a second pass at the database structure. I mean, we can change around the internal structure when we go to V2, possibly we can… Make that clearer.
And I forget where we ended up.
with it, I just remember, I mean, the whole… the goal of Don't repeat yourself.
Sort of… ended up making it super complicated to read the YAML to where I wouldn't even review… I wouldn't review PRs based on the YAML, I would review PRs based on the markdown.
Josh Suereth 00:40:48 Yeah, yeah, I… I, There's Don't repeat yourself, and then there's understand what the hell you wrote, and you need both of those to be true.
Let me, let me see if I can show you a quick demo, actually, if folks are interested.
I think this is on… Which one? Not the profiling stuff, here we go.
I don't know if this will be viewable, let me fix my fonts a bit.
Alright, is… Is this kind of readable right now?
What's going on here?
Trask Stalnaker 00:41:33 Yeah, yeah.
Josh Suereth 00:41:33 Okay, so this is just me running Weaver. I'm gonna do… actually, crap, let's build quick.
I just fixed one bug with Weaver Diff. Not that a lot of people use Weaver Diff, but it now works.
Okay, so we're gonna do registry, we're gonna resolve, we're gonna say V2 schema. This is gonna resolve the latest semantic conventions. I'm gonna dump it into, test… Or, we'll just say semconv resolved.
V2.yaml.
and it's gonna resolve everything, it's gonna resolve it into V2, and it's basically… it says no after-resolution policy violation because it's using V2 resolution semantics when I say V2. We'll get into what all of that looks like then for… some of these, catalogs and things. Anyway, if we come back into Weaver, and we look at this… I think I have to refresh… Here we go.
And then we want this to be full… You go away… Okay, so this is what… this is what the actual Resolve schema looks like, so this is what you're gonna get into JQ. In JQ today, when you use Weaver and you do all the SEMCOF crap, you have to, like… manually use JQ expressions to take groups and extract attributes and all that kind of stuff. What Ludmila was showing is actually, you just have a .attributes.
that has access to all the attributes in the registry straight up. So, that's… that's what you get under the attributes section. Next, under attribute groups, we actually have no public attributes.
exposed today in SEMCOM, they're all private. We can expose public ones, and I think we will have to when we merge to V2. I'm sure Ludmilla has that. And then, we have a signals repository. Underneath signals is all of the underlying things, like, oh, I have this metric. I have, Where's my drop-downs? You know, I have all the ask… Net core metrics, because these are all in order.
Once you get past AppsNet Core, it'll be a different set of metrics, but they're all in a big thing. After metrics, you have spans. Again, everything's extracted, so all the attributes are fully visible.
They're not refs when we resolve, and I think I am… oh, I wanted to close you… And my expansion group thing broke. After signals, we have what are called refinements. This is where all the shenanigans you're talking about exist, Trask. A refinement is where you did something to override the raw signal.
Where you extend crap for databases?
And what Weaver does for semantic conventions is it makes sure the raw signal definition is not violated when you make a refinement. So you cannot make a refinement that doesn't abide by the raw thing.
But you can def… you can have a refinement, and the refinement you can use for code gen.
So that I can say, cool, I'm gonna code-gen how to make MySQL database things. I could use it for docs to say, here's what MySQL looks like.
But when I do validation logic around, does this abide by SEMCOV, I use the signal part.
Does that make sense?
Trask Stalnaker 00:45:06 I think so. Under this refinement, for example, like, for… How does this… How do you know… The context for this refinement.
Josh Suereth 00:45:23 you're supposed to be able to consume it without context, and the next thing that we're building into this… so, for preview.
you can't figure out where this came from. Or you, you can, sorry.
These are bad refinements. Let me see if I can find database stuff. Let me come down and search backwards.
Let's find a good refinement down here.
Yeah, this is all Gen AI. This is where the refinement is the same. I'll show you quick. So basically, when you have a refinement.
Man, we have so much in our Semcov. It's… I forgot how unwieldy it is to show live.
Let's see… So…
Trask Stalnaker 00:46:11 100… just 100,000 lines, no big deal.
Josh Suereth 00:46:14 It's… it's… we got a lot of SunConf. This is an example of a span where it's a refinement, this is the refinement view of the span, but there was no refinement done.
So… the type of the span is GenAI Inference Client, right? And the ID is the same. The ID is the ID of the refinement.
Trask Stalnaker 00:46:35 Oh, okay, I see. So, if you're in a database thing, there would be, like, this would be… Definitely.
Josh Suereth 00:46:41 Yeah, we could say… MySQL. OpenAI inference client, this is a MySQL thing, or whatever, and this would still be the same pure database guy.
Trask Stalnaker 00:46:51 Okay.
Josh Suereth 00:46:51 That's… that's the… so, every signal that's defined has its own refinement, so that if you just look at refinements, you can do everything you need.
What we're not sure of right now is if refinements is going to be just used for advanced semantic conventions and not the rest of the user population, or if they need to be first class for everything.
So, right now we've optimized where there, you know, simple use cases don't need refinements, they just use signals. And advanced use cases use refinements.
Does that make sense?
Trask Stalnaker 00:47:26 Yeah, yeah.
Josh Suereth 00:47:28 Okay.
That's a good question.
I think that is all I can show… outside of… do I have any example… oh, I can show a policy, maybe. If you've done rego policies for semantic conventions, where you want to do, like, our, you know, policy A versus Policy B.
making sure that, you know, names stay the same and all that kind of stuff. I think… Is this the one where we have it? Is it under test?
No, it's the other set of tests. Here we go.
Here's an example of a new Rigo policy, and I think the difference here, if I were to show… I don't have a check. Check was done somewhere else, apparently. Okay. The difference here is, in V1, you would have said input.groups.
And you would say where, you know, group… Dot type equals metric.
Right?
That would be… V1 syntax would have been group colon equals input.groups.
something like this. The difference between V1 and V2 is that, you know, everything is kind of explicitly typed now, and far easier to get access to. So you can actually look at, you look at a metric directly and get metrics.
even for, checking baseline, comparison after resolution. This is where we compare two input signals together, right? So this is where we compare, like, version 5 and version 4 of semantic conventions and make sure we haven't broken things. So this is a policy where we say, cool, look at the metric in the current version, look at the metric in the previous version, and then do a comparison. The fact this is called input and data is like a Rego-specific thing, but… Anyway, TLDR… this should be generally a massive cleanup in terms of how we look at and think about the YAML.
and making the YAML more readable. If you have any questions or concerns, let us know. If you want to try this out at all, every Rego, command has been updated with a dash dash V2.
and you just specify dash dash v2, and you're in V2 world. If you want to specify any files in V2 format, you can actually use that with, With the existing.
Weaver. You can actually specify your definitions, your Wea… the things that are used today in V2, and I think I have an example of that somewhere… here, maybe?
I think I have a raw file here, yeah.
So if you want to specify a new definition model in Weaver v2 syntax.
That's not the one I want.
Maybe it's here.
We look forward to…
Trask Stalnaker 00:50:54 Plan with… what's the plan with updating semantic conventions?
to be too…
Josh Suereth 00:51:04 Yes. So, I think there's gonna be two phases. Let me come back to the notes. I'll just write this in the notes. Here we go.
Oh, come on.
Sure. Chrome tab… alright.
Am I back on the notes now?
Okay.
So, how to use for YAML definitions. Basically, all you do is you start your file with version 2.
And then suddenly you can write attributes colon And this will work, because we actually have backwards compatibility with version 2 and version 1, where version 2 erases its definition back to version 1, and you can use version 1 for everything After the definition, if you wanted to.
Trask Stalnaker 00:51:55 Oh, okay. Oh, so you don't have to specify dash dash V2.
Josh Suereth 00:51:59 You… for… so, we have… let me… let's talk about… evolution now, right? So… Weaver… dash dash V2 means output is in V2 format.
Policies are in V2 format, templates are V2 format, right?
File header… of version colon 2.
Means the definition is in V2 format.
So, there are two things we can do.
to migrate.
to V2, with semantic conventions. We can go file by file to all of our YAML files, and start using the new input format with this version 2.
Trask Stalnaker 00:52:53 Right.
Josh Suereth 00:52:56 The other thing, which is what Ludmila is working on, is we can actually change our output format to V2, where all of our templates… sorry, the… my… we're cleaning out back here.
Alright, I don't think that's gonna go away.
All of our… so, if we use the dash dash v2, all the output formats are in V2, so this is where all the templates, all the policies, all that, V2 format… Ludmila's working on this. This hopefully should be… we can just make changes to all the Rego policies and Markdown template files in SEMCOV in one big bang.
and then update the Weaver calls we make to do dash dash v2.
at the same time, and that should be one CL that just updates everything to V2 for the output. And we can independently update files for input, right?
Trask Stalnaker 00:53:51 Yep.
Josh Suereth 00:53:51 So the idea here is to make it as incremental and painless as possible.
It's still gonna be somewhat… there's still gonna be a little bit of a churn. Another thing I was working on, but I don't know if I have time to finish, was I was gonna actually make an automatic V1 to V2 transition, where it will take a file that you've defined in YAML, give you what the version 2 file would look like, and give you a set of warnings if it cannot translate it due to things you're using that don't exist in V2.
Okay, any questions? Sorry, that was a big, a big dump of stuff.
Trask Stalnaker 00:54:37 Oh, looking good. Excited that it's… Here.
Josh Suereth 00:54:43 Yeah, yeah. The, the other big thing here is, we're going… with the new format, we're gonna start greenlighting publishing the actual resolved Weaver schema.
So today, when you use Weaver, you have to look at all the individual YAML files and merge them all together, every single time you look at a repo.
Trask Stalnaker 00:55:07 Yeah.
Josh Suereth 00:55:08 With this, you'll be able to actually resolve them all into one YAML file, publish that, and then consume that directly, instead of doing the resolution every time.
Trask Stalnaker 00:55:19 Will that be our new schema file?
Ben, that we… Replacing the old diff schema.
Manual.
Josh Suereth 00:55:32 is… We have to talk about that, yeah. I think I… we need to replace it, but it doesn't fully replace it. So basically, when you publish a schema, you'll have to… the idea is you publish the definition.
And you publish the diff at the same time, and then you can consume both.
Trask Stalnaker 00:55:50 Okay.
Yeah.
Josh Suereth 00:55:52 But that… yeah, that… that I… we're still working on. We need, like… Did you see that Weaver now has a GitHub action?
No. That's Weaver? Yes.
So there's a GitHub action where it'll actually install Weaver on the, you know, on your GitHub runner and let you do Weaver-related things in it.
Once we formalize, like, a publishing step, the goal would be to get a reusable action for, for hotel projects that, you know, other people can use as well, that would basically say, okay, cool, I'm gonna run Weaver, here's where my models are, here's where my policies are, and I want to use, you know, default out of the box.
dock generation, right? And this action will let you publish, per version, a Weaver schema.
Where it'll have the diff file or have the definition file, and then people can consume from those. But if we do it right, it'll also have documentation and possibly code gen, that kind of stuff.
Trask Stalnaker 00:56:58 Yeah, the documentation is the part that I want, So that's… so that's gonna be pulled into the… from the SEMCOM repo, because those are in the SEMCOM repo today, right?
I'll be pulled into the Weaver repo as, like, a default.
Josh Suereth 00:57:15 Yes. Whether we pull the SEMCOM one in as the default, or we have something that is… more, like, less tied to how SEMCOM works. SemComf did a few things that I don't know if we're gonna have as a generic feature or not, so we have to… there's a bunch of discussion on that. It'll be very similar to what SEMCOM does, but maybe not exactly the same.
Trask Stalnaker 00:57:37 Sure.
Josh Suereth 00:57:38 Yeah. Another way to phrase it is, we update Semcov, what it generates, and then we update it to something we can pull in and have everyone use.
Trask Stalnaker 00:57:48 Yep.
Josh Suereth 00:57:49 Yep for context, everyone tries to use SEMCOM and runs into the same set of, like, 12 problems.
Where it kind of doesn't quite work. And so, we need to fix those problems.
Trask Stalnaker 00:58:00 And also, everybody ends up copy-pasting 30 files from SEMCONS just to generate the docs.
Josh Suereth 00:58:09 Well, yeah, they copy-paste them, they fix those 12 issues, and then… we all do that every time, right? So it's… yeah, we need to fix that.
Trask Stalnaker 00:58:18 Cool.
Josh Suereth 00:58:19 Yeah, if anyone's interested in helping with that, like, if you wanted to actually work… one of the things LaMilla's doing is fixing up the SEMCOM templates. If somebody wanted to help make a generic set of templates that work outside of SEMCOM, like, start with the SEMConf repo, make it work with that, but also make it work on just general purpose things. Our goal is to federate this tooling, so that we can use it in the collector contrib, we can use it other places. So, that'd be ideal if we could get, you know, more hands on this.
Trask Stalnaker 00:58:50 Yeah, I see that as the main blocker right now for, Giving people a successful route outside of the semantic convention repo.
Like, I wanna… I wanna potentially pull out, the JVM semantic conventions to the Java repo.
Right, I wa- I wanna try to… trim down the semantic convention repo and start pushing people to decentralize that stuff.
But I don't feel like we can do that until… There's an easy path for them.
Josh Suereth 00:59:28 Yeah, yeah, I absolutely agree.
So, at this point, we need to get a repeatable release process for a semantic convention bundle, that we can give to another project. That's, that's gonna be… Step 1. So, we were not willing to commit to the current shape of our YAML because we thought it was too confusing, which has led to V2, which we kicked off Man, 6 months ago, maybe?
And we're finally at the state where I think, you know, like I said, the next version of Weaver will have this preview release, where we're gonna be collecting bugs, and I can assure you there will be bugs, so please try it out and let us know.
Cool. With that, I have nothing else, and I don't think we have anything else on the agenda, so… hope everybody has a good, holiday if I don't see you before the new year. I might be out next week, so I will, see y'all later.
Trask Stalnaker 01:00:29 Awesome, thank you.
Bye, Al.
Donal O'Sullivan 01:00:34 Cheers, bye-bye.
